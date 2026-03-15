#!/usr/bin/env node

const fs = require('fs/promises');
const path = require('path');
const { execFileSync } = require('child_process');

async function loadPlaywright() {
  try {
    return require('playwright');
  } catch (error) {
    throw new Error(
      'playwright is not installed for this script. Install it in a temp folder and run with NODE_PATH set, or add it locally.'
    );
  }
}

function getAuthCookie() {
  const script = [
    'import browser_cookie3',
    "for c in browser_cookie3.chrome(domain_name='point93.ai'):",
    '    print(c.value)',
    '    break',
  ].join('\n');

  const value = execFileSync('python3', ['-c', script], { encoding: 'utf8' }).trim();
  if (!value) {
    throw new Error('No Chrome auth cookie found for point93.ai');
  }
  return value;
}

function slugify(route) {
  return route
    .replace(/^https?:\/\/[^/]+/, '')
    .replace(/^\//, '')
    .replace(/[/?#=&:]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '') || 'home';
}

function normalizeHtml(html) {
  let next = html;
  next = next.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
  next = next.replace(/<script[^>]*\/>/gi, '');
  if (!/<base\s/i.test(next)) {
    next = next.replace(
      /<head([^>]*)>/i,
      '<head$1><base href="https://point93.ai/"><script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>'
    );
    return next;
  }
  next = next.replace(
    /<head([^>]*)>/i,
    '<head$1><script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>'
  );
  return next;
}

function buildRouteList() {
  return [
    '/dashboard',
    '/my-journey',
    '/assess',
    '/insight-areas',
    '/data-points',
    '/scores',
    '/reports',
    '/business-intelligence',
    '/business-intelligence/a3bd6321-3069-42a6-9b5f-4566c8a4b8de',
    '/areas/507ac887-0f3f-4ea5-a427-b105c814dd7f',
    '/admin/content-builder',
    '/admin/bi-builder',
    '/admin/ai-hub',
    '/admin/graph-view',
    '/admin/users',
    '/admin/analytics',
    '/admin/feedback',
    '/admin/beta',
  ];
}

async function main() {
  const { chromium } = await loadPlaywright();
  const cookieValue = getAuthCookie();
  const outDir = path.resolve(__dirname, '..', 'prod_snapshot_exports');
  await fs.mkdir(outDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1600 },
    deviceScaleFactor: 1,
  });

  await context.addCookies([
    {
      name: 'sb-znwrmzcmiwaqgqidmtpc-auth-token',
      value: cookieValue,
      domain: 'point93.ai',
      path: '/',
      httpOnly: false,
      secure: true,
      sameSite: 'Lax',
    },
  ]);

  const manifest = [];

  for (const route of buildRouteList()) {
    const page = await context.newPage();
    const url = `https://point93.ai${route}`;
    const slug = slugify(route);

    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(4500);

      const title = await page.title();
      const finalUrl = page.url();
      const headings = await page.evaluate(() =>
        Array.from(document.querySelectorAll('h1,h2,h3,[role=heading]'))
          .map((el) => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim())
          .filter(Boolean)
          .slice(0, 40)
      );
      const links = await page.evaluate(() =>
        Array.from(document.querySelectorAll('a'))
          .map((a) => ({
            text: (a.innerText || a.textContent || '').replace(/\s+/g, ' ').trim(),
            href: a.href,
          }))
          .filter((link) => link.text)
          .slice(0, 100)
      );
      const text = await page.evaluate(() =>
        document.body.innerText.replace(/\s+/g, ' ').trim().slice(0, 8000)
      );
      const html = await page.evaluate(() => document.documentElement.outerHTML);

      const screenshotPath = path.join(outDir, `${slug}.png`);
      const htmlPath = path.join(outDir, `${slug}.html`);
      const jsonPath = path.join(outDir, `${slug}.json`);

      await page.screenshot({ path: screenshotPath, fullPage: true });
      await fs.writeFile(htmlPath, normalizeHtml(`<!DOCTYPE html>${html}`));
      await fs.writeFile(
        jsonPath,
        JSON.stringify(
          {
            route,
            requestedUrl: url,
            finalUrl,
            title,
            headings,
            links,
            text,
            screenshotPath,
            htmlPath,
          },
          null,
          2
        )
      );

      manifest.push({
        route,
        requestedUrl: url,
        finalUrl,
        title,
        headings,
        screenshot: screenshotPath,
        html: htmlPath,
        json: jsonPath,
      });

      console.log(`Captured ${route} -> ${finalUrl}`);
    } catch (error) {
      manifest.push({
        route,
        requestedUrl: url,
        error: String(error),
      });
      console.error(`Failed ${route}: ${error}`);
    } finally {
      await page.close();
    }
  }

  await fs.writeFile(path.join(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
  await browser.close();
  console.log(`Wrote ${manifest.length} route records to ${outDir}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
