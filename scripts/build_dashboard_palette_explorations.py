from __future__ import annotations

from textwrap import dedent

from build_point93_figma_pages import OUT_DIR


CSS = """
:root {
  --pearl: #f7f7f5;
  --slate: #1f2630;
  --obsidian: #171b21;
  --evergreen: #1e5a52;
  --champagne: #d6b273;
  --smoke: #d9dde3;
  --mist: #eef0f2;
  --sand: #ede7dd;
  --card: rgba(255, 255, 255, 0.8);
  --text: #20242b;
  --muted: #66717d;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: var(--text);
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at top left, rgba(214, 178, 115, 0.14), transparent 24%),
    radial-gradient(circle at top right, rgba(30, 90, 82, 0.08), transparent 22%),
    linear-gradient(180deg, #f4f0e8 0%, #edf1f3 100%);
}

.capture-root {
  width: 1920px;
  padding: 56px 72px 96px;
}

.cover {
  margin-bottom: 36px;
  padding: 38px 42px;
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(214, 178, 115, 0.24);
  box-shadow: 0 22px 50px rgba(31, 38, 48, 0.09);
}

.eyebrow {
  margin-bottom: 12px;
  color: #5c6a78;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.cover h1 {
  margin: 0 0 10px;
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 44px;
  line-height: 1.02;
  letter-spacing: -0.05em;
}

.cover p {
  max-width: 1040px;
  margin: 0;
  color: var(--muted);
  font-size: 14px;
  line-height: 1.75;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 18px;
}

.chip {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.68);
  border: 1px solid rgba(214, 178, 115, 0.24);
  color: #596474;
  font-size: 11px;
  font-weight: 700;
}

.palette-row {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 12px;
  margin-bottom: 28px;
}

.swatch {
  overflow: hidden;
  border-radius: 18px;
  border: 1px solid rgba(31, 38, 48, 0.08);
  background: rgba(255, 255, 255, 0.88);
  box-shadow: 0 14px 28px rgba(31, 38, 48, 0.06);
}

.swatch-color {
  height: 66px;
}

.swatch-info {
  padding: 12px 14px 14px;
}

.swatch-info strong {
  display: block;
  margin-bottom: 4px;
  font-size: 12px;
}

.swatch-info span {
  display: block;
  color: var(--muted);
  font-size: 10px;
  line-height: 1.45;
}

.stack {
  display: flex;
  flex-direction: column;
  gap: 34px;
}

.variant {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.variant-meta {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 18px;
}

.variant-meta h2 {
  margin: 0 0 6px;
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 28px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

.variant-meta p {
  max-width: 940px;
  margin: 0;
  color: var(--muted);
  font-size: 12px;
  line-height: 1.7;
}

.variant-badge {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.68);
  border: 1px solid rgba(31, 38, 48, 0.08);
  color: var(--muted);
  font-size: 11px;
  font-weight: 800;
}

.frame {
  width: 1440px;
  overflow: hidden;
  border-radius: 28px;
  border: 1px solid rgba(31, 38, 48, 0.08);
  box-shadow: 0 26px 52px rgba(31, 38, 48, 0.12);
}

.theme {
  --shell-bg: rgba(255, 255, 255, 0.76);
  --sidebar-bg: #efece5;
  --sidebar-line: rgba(31, 38, 48, 0.08);
  --main-bg: rgba(251, 250, 247, 0.92);
  --card-bg: rgba(255, 255, 255, 0.76);
  --card-strong: rgba(255, 255, 255, 0.92);
  --card-soft: rgba(238, 240, 242, 0.52);
  --line: rgba(31, 38, 48, 0.08);
  --headline: var(--slate);
  --body: #525d69;
  --label: #6d7885;
  --primary: var(--obsidian);
  --secondary: rgba(255, 255, 255, 0.64);
  --accent: var(--champagne);
  --accent-strong: var(--evergreen);
  --surface-shadow: 0 18px 30px rgba(31, 38, 48, 0.06);
}

.theme-a {
  --shell-bg: rgba(255, 255, 255, 0.76);
  --sidebar-bg: linear-gradient(180deg, #f1ede6 0%, #ece8e0 100%);
  --main-bg: linear-gradient(180deg, #fbfaf7 0%, #f6f5f1 100%);
  --card-bg: rgba(255, 255, 255, 0.82);
  --card-soft: rgba(232, 236, 239, 0.52);
  --accent: var(--champagne);
  --accent-strong: var(--evergreen);
}

.theme-b {
  --shell-bg: rgba(255, 255, 255, 0.7);
  --sidebar-bg: linear-gradient(180deg, #222932 0%, #1b222b 100%);
  --sidebar-line: rgba(255, 255, 255, 0.08);
  --main-bg: linear-gradient(180deg, #f7f7f5 0%, #f0f3f4 100%);
  --card-bg: rgba(255, 255, 255, 0.86);
  --card-soft: rgba(30, 90, 82, 0.08);
  --headline: #1d232b;
  --body: #55606d;
  --label: #7c8793;
  --accent: var(--evergreen);
  --accent-strong: var(--champagne);
  --primary: #15191f;
}

.theme-c {
  --shell-bg: rgba(255, 255, 255, 0.72);
  --sidebar-bg: linear-gradient(180deg, #f0ece4 0%, #ebe7df 100%);
  --main-bg: linear-gradient(180deg, #faf8f4 0%, #f2f3f1 100%);
  --card-bg: rgba(255, 255, 255, 0.78);
  --card-strong: linear-gradient(180deg, rgba(31,38,48,0.98), rgba(31,38,48,0.92));
  --card-soft: rgba(214, 178, 115, 0.10);
  --accent: var(--champagne);
  --accent-strong: var(--evergreen);
  --primary: #14181f;
}

.shell {
  display: flex;
  align-items: stretch;
  min-height: 1308px;
  background: var(--shell-bg);
}

.sidebar {
  width: 228px;
  padding: 26px 18px 22px;
  background: var(--sidebar-bg);
  border-right: 1px solid var(--sidebar-line);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.logo {
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -0.03em;
}

.theme-a .logo,
.theme-c .logo {
  color: var(--slate);
}

.theme-b .logo {
  color: #f6f7f8;
}

.nav {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 14px;
  color: var(--body);
  font-size: 12px;
  font-weight: 600;
}

.theme-b .nav-item {
  color: rgba(255, 255, 255, 0.72);
}

.nav-item.active {
  color: var(--headline);
  background: rgba(214, 178, 115, 0.14);
  box-shadow: inset 0 0 0 1px rgba(214, 178, 115, 0.12);
}

.theme-b .nav-item.active {
  color: #f9fafb;
  background: rgba(214, 178, 115, 0.16);
}

.nav-item .meta-dot {
  margin-left: auto;
  width: 6px;
  height: 6px;
  border-radius: 999px;
  background: var(--accent-strong);
}

.nav-item .meta-pill {
  margin-left: auto;
  padding: 4px 7px;
  border-radius: 999px;
  font-size: 9px;
  font-weight: 800;
  background: rgba(214, 178, 115, 0.18);
  color: #a67932;
}

.sidebar-account {
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px solid var(--sidebar-line);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sidebar-label {
  color: var(--label);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.tier-pill {
  display: inline-flex;
  align-items: center;
  padding: 7px 10px;
  border-radius: 999px;
  background: rgba(214, 178, 115, 0.16);
  color: var(--headline);
  font-size: 11px;
  font-weight: 700;
}

.sidebar-copy {
  color: var(--body);
  font-size: 11px;
  line-height: 1.5;
}

.theme-b .sidebar-copy,
.theme-b .sidebar-label {
  color: rgba(255, 255, 255, 0.7);
}

.progress-track {
  width: 100%;
  height: 4px;
  border-radius: 999px;
  background: rgba(31, 38, 48, 0.12);
  overflow: hidden;
}

.theme-b .progress-track {
  background: rgba(255, 255, 255, 0.12);
}

.progress-fill {
  width: 32%;
  height: 100%;
  border-radius: 999px;
  background: var(--accent);
}

.main {
  flex: 1;
  padding: 34px;
  background: var(--main-bg);
}

.content {
  width: 100%;
  max-width: 1144px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.topline {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.kicker {
  color: var(--accent-strong);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.title {
  margin: 0;
  color: var(--headline);
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 42px;
  line-height: 1.01;
  letter-spacing: -0.055em;
}

.subtitle {
  color: var(--body);
  font-size: 13px;
  line-height: 1.7;
  max-width: 720px;
}

.grid-hero {
  display: grid;
  grid-template-columns: 1.35fr 0.65fr;
  gap: 18px;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.card,
.soft-card,
.dark-card {
  border-radius: 24px;
  box-shadow: var(--surface-shadow);
}

.card {
  padding: 24px;
  background: var(--card-bg);
  border: 1px solid var(--line);
}

.soft-card {
  padding: 22px;
  background: var(--card-soft);
  border: 1px solid rgba(31, 38, 48, 0.03);
}

.dark-card {
  padding: 24px;
  color: white;
  background: var(--card-strong);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.card-label,
.dark-label {
  margin-bottom: 14px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.card-label {
  color: var(--label);
}

.dark-label {
  color: rgba(255, 255, 255, 0.6);
}

.section-title {
  margin: 0 0 8px;
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 24px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

.card-copy {
  color: var(--body);
  font-size: 13px;
  line-height: 1.7;
}

.dark-card .card-copy,
.dark-card .sub-copy {
  color: rgba(255, 255, 255, 0.78);
}

.sub-copy {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.65;
}

.action-row {
  display: flex;
  gap: 10px;
  margin-top: 18px;
}

.btn-primary,
.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 16px;
  border-radius: 14px;
  font-size: 12px;
  font-weight: 700;
}

.btn-primary {
  color: white;
  background: var(--primary);
}

.btn-secondary {
  color: var(--headline);
  background: rgba(255, 255, 255, 0.58);
  border: 1px solid var(--line);
}

.progress-card {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.progress-card .metric {
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 34px;
  line-height: 1;
  letter-spacing: -0.05em;
}

.status-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.status-pill {
  display: inline-flex;
  align-items: center;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(31, 38, 48, 0.05);
  color: var(--body);
  font-size: 10px;
  font-weight: 700;
}

.status-pill.warm {
  background: rgba(214, 178, 115, 0.16);
  color: #8f6a32;
}

.status-pill.verdant {
  background: rgba(30, 90, 82, 0.10);
  color: var(--evergreen);
}

.score-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
}

.score-ring {
  width: 98px;
  height: 98px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  border: 3px solid var(--accent);
  color: var(--headline);
  font-family: "Saans TRIAL", "Saans", "Helvetica Neue", Inter, sans-serif;
  font-size: 36px;
  font-weight: 700;
  line-height: 1;
}

.map-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 14px;
}

.map-card {
  padding: 16px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.64);
  border: 1px solid rgba(31, 38, 48, 0.05);
}

.theme-b .map-card {
  background: rgba(255, 255, 255, 0.9);
}

.map-card strong {
  display: block;
  margin-bottom: 4px;
  font-size: 14px;
}

.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin-top: 16px;
}

.list-card {
  padding: 18px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(31, 38, 48, 0.05);
}

.list-card h4 {
  margin: 0 0 14px;
  font-size: 15px;
}

.line-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.line-item {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  color: var(--text);
  font-size: 13px;
  line-height: 1.45;
}

.line-item span:last-child {
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
}

.verdict-card {
  min-height: 236px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  justify-content: flex-start;
}

.verdict-chip {
  display: inline-flex;
  align-items: center;
  align-self: flex-start;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(30, 90, 82, 0.10);
  color: var(--evergreen);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.verdict-copy {
  max-width: 440px;
  font-size: 14px;
  line-height: 1.75;
  color: var(--body);
}

.theme-c .verdict-copy {
  color: rgba(255, 255, 255, 0.82);
}

.micro-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.mini-card {
  padding: 18px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(31, 38, 48, 0.05);
}

.mini-card h5 {
  margin: 0 0 8px;
  font-size: 15px;
}

.dot-row {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.module-card {
  padding: 18px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.82);
  border: 1px solid rgba(31, 38, 48, 0.05);
}

.module-card strong {
  display: block;
  margin-bottom: 6px;
  font-size: 15px;
}

.module-meta {
  color: var(--muted);
  font-size: 11px;
  line-height: 1.5;
}

.module-progress {
  width: 100%;
  height: 6px;
  margin-top: 12px;
  border-radius: 999px;
  background: rgba(31, 38, 48, 0.08);
  overflow: hidden;
}

.module-progress span {
  display: block;
  width: 66%;
  height: 100%;
  background: var(--accent);
  border-radius: 999px;
}

.rationale {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  width: 1440px;
}

.rationale-card {
  padding: 16px 18px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.74);
  border: 1px solid rgba(31, 38, 48, 0.06);
}

.rationale-card h4 {
  margin: 0 0 6px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.rationale-card p {
  margin: 0;
  color: var(--muted);
  font-size: 11px;
  line-height: 1.6;
}

.theme-b .dark-card {
  background: linear-gradient(180deg, rgba(30,90,82,0.96), rgba(27,73,66,0.92));
}

.theme-c .hero-dark {
  background: linear-gradient(180deg, rgba(31,38,48,0.98), rgba(31,38,48,0.93));
}
"""


def document(body: str) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Point93 Dashboard Palette Explorations</title>
          <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
          <style>{CSS}</style>
        </head>
        <body>
          <div class="capture-root">
            {body}
          </div>
        </body>
        </html>
        """
    )


def cover() -> str:
    return dedent(
        """\
        <div class="cover">
          <div class="eyebrow">Palette Application · Dashboard</div>
          <h1>Dashboard visual explorations using Pearl, Slate, Evergreen, Champagne, and Smoke.</h1>
          <p>These explorations keep the dashboard architecture intact but move it away from white-on-white flatness. The goal is a more layered, more premium expression with a darker primary button, stronger hierarchy, more breathing room, and a headline voice that feels closer to Saans-style product branding.</p>
          <div class="chips">
            <div class="chip">Primary button pushed to near-black</div>
            <div class="chip">Reduced outline dependence</div>
            <div class="chip">More tonal layering and quieter premium cues</div>
            <div class="chip">Google × Tesla × Porsche × Deutsche Bank energy</div>
          </div>
        </div>
        """
    )


def palette_row() -> str:
    swatches = [
        ("Pearl", "#f7f7f5", "Base surface"),
        ("Slate", "#1f2630", "Primary text"),
        ("Evergreen", "#1e5a52", "Trust accent"),
        ("Champagne", "#d6b273", "Selective highlight"),
        ("Smoke", "#d9dde3", "Structure and lines"),
    ]
    html = []
    for name, color, label in swatches:
        html.append(
            f"""<div class="swatch"><div class="swatch-color" style="background:{color};"></div><div class="swatch-info"><strong>{name}</strong><span>{color}</span><span>{label}</span></div></div>"""
        )
    return f'<div class="palette-row">{"".join(html)}</div>'


def nav(theme_b: bool = False) -> str:
    return dedent(
        f"""\
        <div class="sidebar">
          <div class="logo">Point93</div>
          <div class="nav">
            <div class="nav-item active"><span>Dashboard</span></div>
            <div class="nav-item"><span>My Results</span><span class="meta-dot"></span></div>
            <div class="nav-item"><span>Assessments</span><span class="meta-pill">1 in progress</span></div>
            <div class="nav-item"><span>My Areas</span></div>
            <div class="nav-item"><span>Business Intelligence</span></div>
            <div class="nav-item"><span>What Clients Are Asking</span><span class="meta-pill">Soon</span></div>
          </div>
          <div class="sidebar-account">
            <div class="sidebar-label">Account</div>
            <div class="tier-pill">Comprehensive</div>
            <div class="sidebar-copy">5/17 modules · 29%</div>
            <div class="progress-track"><div class="progress-fill"></div></div>
          </div>
        </div>
        """
    )


def module_card(title: str, meta: str, action: str, progress: bool = False) -> str:
    progress_html = '<div class="module-progress"><span></span></div>' if progress else ""
    return dedent(
        f"""\
        <div class="module-card">
          <strong>{title}</strong>
          <div class="module-meta">{meta}</div>
          {progress_html}
          <div class="action-row" style="margin-top:14px;"><div class="btn-primary">{action}</div></div>
        </div>
        """
    )


def dashboard_variant(name: str, badge: str, description: str, theme: str, mode: str) -> str:
    hero_class = "card hero-dark" if mode == "c" else ("dark-card" if mode == "b" else "card")
    verdict_class = "dark-card verdict-card" if mode == "c" else "soft-card verdict-card"
    progress_card_class = "dark-card progress-card" if mode in {"a", "c"} else "card progress-card"
    hero_copy = (
        "A tailored strategic readout of where the practice stands, what matters now, and where the next lift will come from."
        if mode != "b"
        else "A more institutional and high-confidence dashboard with clearer hierarchy, calmer accents, and more concierge energy."
    )
    return dedent(
        f"""\
        <div class="variant">
          <div class="variant-meta">
            <div>
              <h2>{name}</h2>
              <p>{description}</p>
            </div>
            <div class="variant-badge">{badge}</div>
          </div>
          <div class="frame">
            <div class="theme {theme}">
              <div class="shell">
                {nav(theme_b=(mode == "b"))}
                <div class="main">
                  <div class="content">
                    <div class="topline">
                      <div class="kicker">Practice standing</div>
                      <h3 class="title">Dashboard</h3>
                      <div class="subtitle">{hero_copy}</div>
                    </div>

                    <div class="grid-hero">
                      <div class="{hero_class}">
                        <div class="card-label">Layer 1 · Welcome & Orientation</div>
                        <h4 class="section-title">Welcome back, Adam</h4>
                        <div class="card-copy">Point93 measures and compares your practice across modules, areas, and intelligence layers. This version tries to feel less like an admin panel and more like a premium advisory briefing.</div>
                        <div class="action-row">
                          <div class="btn-primary">Continue FT.2 Technology Capabilities</div>
                          <div class="btn-secondary">View Welcome Tour</div>
                        </div>
                      </div>
                      <div class="{progress_card_class}">
                        <div class="card-label">Progress</div>
                        <div class="metric">29%</div>
                        <div class="sub-copy">5 of 17 modules completed · 3 of 6 areas touched</div>
                        <div class="progress-track"><div class="progress-fill"></div></div>
                      </div>
                    </div>

                    <div class="grid-2">
                      <div class="card">
                        <div class="card-label">Layer 2 · Executive Summary</div>
                        <div class="score-row">
                          <div>
                            <h4 class="section-title" style="margin-bottom:6px;">Overall P93 Score</h4>
                            <div class="card-copy">83rd percentile among comparable advisors, with the strongest depth in structure and operational discipline.</div>
                            <div class="status-row">
                              <div class="status-pill warm">B · Competitive</div>
                              <div class="status-pill">5 modules complete</div>
                              <div class="status-pill verdant">2 BI profiles active</div>
                            </div>
                          </div>
                          <div class="score-ring">74</div>
                        </div>
                      </div>
                      <div class="soft-card">
                        <div class="card-label">Area Assessment Map</div>
                        <div class="map-grid">
                          <div class="map-card"><strong>PF</strong><div class="sub-copy">100% assessed</div></div>
                          <div class="map-card"><strong>FT</strong><div class="sub-copy">67% assessed</div></div>
                          <div class="map-card"><strong>IM</strong><div class="sub-copy">20% assessed</div></div>
                          <div class="map-card"><strong>PI</strong><div class="sub-copy">0% assessed</div></div>
                          <div class="map-card"><strong>SC</strong><div class="sub-copy">0% assessed</div></div>
                          <div class="map-card"><strong>FV</strong><div class="sub-copy">0% assessed</div></div>
                        </div>
                      </div>
                    </div>

                    <div class="grid-2">
                      <div class="card">
                        <div class="card-label">Top strengths & gaps</div>
                        <div class="columns">
                          <div class="list-card">
                            <h4>Top strengths</h4>
                            <div class="line-list">
                              <div class="line-item"><span>Client autonomy systems</span><span>91 · PF.2</span></div>
                              <div class="line-item"><span>Repeatable workflows</span><span>88 · FT.2</span></div>
                              <div class="line-item"><span>Compliance oversight</span><span>84 · PF.1</span></div>
                            </div>
                          </div>
                          <div class="list-card">
                            <h4>Top gaps</h4>
                            <div class="line-list">
                              <div class="line-item"><span>Investment communication</span><span>49 · IM.1</span></div>
                              <div class="line-item"><span>Practice management cadence</span><span>56 · IM.2</span></div>
                              <div class="line-item"><span>Value articulation</span><span>59 · PitchPerfect</span></div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="{verdict_class}">
                        <div class="card-label">Hub Verdict</div>
                        <div class="verdict-chip">AI generated</div>
                        <div class="verdict-copy">Your current position is solidly Competitive, with strength clustered around structure and operational clarity. The next lift will come from turning that internal quality into more visible client-facing confidence and differentiation.</div>
                      </div>
                    </div>

                    <div class="card">
                      <div class="card-label">Layer 3 · Detail & Action</div>
                      <div class="micro-grid">
                        <div class="mini-card">
                          <h5>Quick Win</h5>
                          <div class="sub-copy">Complete IM.2 Practice Management to unlock deeper cross-module synthesis.</div>
                          <div class="action-row"><div class="btn-primary">Continue IM.2</div></div>
                        </div>
                        <div class="mini-card">
                          <h5>Data Point Health</h5>
                          <div class="sub-copy">A cleaner, more curated signal of score confidence and current data coverage.</div>
                          <div class="dot-row">
                            <div class="dot" style="background:#1e5a52;"></div>
                            <div class="dot" style="background:#1e5a52;"></div>
                            <div class="dot" style="background:#d6b273;"></div>
                            <div class="dot" style="background:#d6b273;"></div>
                            <div class="dot" style="background:#1f2630;"></div>
                            <div class="dot" style="background:#1f2630;"></div>
                            <div class="dot" style="background:#d9dde3;"></div>
                            <div class="dot" style="background:#d9dde3;"></div>
                          </div>
                        </div>
                        <div class="mini-card" style="background:linear-gradient(180deg, rgba(30,90,82,0.10), rgba(255,255,255,0.84));">
                          <h5>Moenio Nudge</h5>
                          <div class="sub-copy">A new BI profile is available once you finish SC.1 Client Service & Communication.</div>
                          <div class="status-row"><div class="status-pill verdant">AI reference</div></div>
                        </div>
                      </div>

                      <div class="module-grid" style="margin-top:18px;">
                        {module_card("PF.1 Compliance Fundamentals", "Completed · ~8 min", "View Results")}
                        {module_card("FT.2 Technology Capabilities", "In Progress · 67% done", "Continue Assessment", progress=True)}
                        {module_card("IM.2 Practice Management", "Recommended next · ~15 min", "Start Assessment")}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="rationale">
            <div class="rationale-card">
              <h4>What changed</h4>
              <p>Moved away from white-on-white stacking by introducing pearl and smoke surfaces, deeper shadows, and tone-based separation instead of repeated outlines.</p>
            </div>
            <div class="rationale-card">
              <h4>Luxury signal</h4>
              <p>Primary action is now a near-black button, headline treatment is more assertive, and accent color is used with more restraint so the screen feels more expensive.</p>
            </div>
            <div class="rationale-card">
              <h4>Why this direction</h4>
              <p>{badge}. This version is testing how far Point93 can move toward premium advisory software without losing product clarity.</p>
            </div>
          </div>
        </div>
        """
    )


def page() -> str:
    body = "".join(
        [
            cover(),
            palette_row(),
            '<div class="stack">',
            dashboard_variant(
                "Exploration A · Slate Command",
                "Closest to current structure",
                "The cleanest translation of the palette. This version stays closest to the current grid but replaces flat white surfaces with a warmer, more premium material stack.",
                "theme-a",
                "a",
            ),
            dashboard_variant(
                "Exploration B · Evergreen Stewardship",
                "Most institutional",
                "This direction introduces a dark institutional sidebar and deeper evergreen authority, making the product feel more private-bank and less generic SaaS.",
                "theme-b",
                "b",
            ),
            dashboard_variant(
                "Exploration C · Private Briefing",
                "Most editorial",
                "This version pushes the concept furthest: darker hero surfaces, richer contrast, and more curated hierarchy so the dashboard feels closer to an executive briefing.",
                "theme-c",
                "c",
            ),
            "</div>",
        ]
    )
    return document(body)


def write_outputs() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / "dashboard-palette-explorations.html"
    path.write_text(page())
    print(f"Wrote {path.relative_to(OUT_DIR.parent)}")


if __name__ == "__main__":
    write_outputs()
