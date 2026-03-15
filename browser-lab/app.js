import { getRuntimeFragment } from "./runtime-fragments.js";

const ROUTES = [
  {
    id: "dashboard",
    name: "Dashboard",
    file: "dashboard.html",
    path: "/dashboard",
    minWidth: 2048,
  },
  {
    id: "assessments",
    name: "Assessments",
    file: "my-journey.html",
    path: "/my-journey",
    minWidth: 1500,
  },
  {
    id: "scores",
    name: "Scores",
    file: "scores.html",
    path: "/scores",
    minWidth: 1500,
  },
  {
    id: "insight-areas",
    name: "Insight Areas",
    file: "insight-areas.html",
    path: "/insight-areas",
    minWidth: 1500,
  },
  {
    id: "data-points",
    name: "Data Points",
    file: "data-points.html",
    path: "/data-points",
    minWidth: 1500,
  },
  {
    id: "business-intelligence",
    name: "Business Intelligence",
    file: "business-intelligence.html",
    path: "/business-intelligence",
    minWidth: 1500,
  },
  {
    id: "bi-detail",
    name: "BI Detail",
    file: "business-intelligence-a3bd6321-3069-42a6-9b5f-4566c8a4b8de.html",
    path: "/business-intelligence/:id",
    minWidth: 1500,
  },
  {
    id: "metric-card-study",
    name: "Component Study · Metric Card",
    url: "./studies/metric-card.html",
    path: "/studies/metric-card",
    minWidth: 1720,
    themeIds: ["study-metric"],
  },
  {
    id: "dashboard-2",
    name: "Dashboard - 2",
    url: "./studies/dashboard-2.html",
    path: "/studies/dashboard-2",
    minWidth: 1960,
    themeIds: ["study-dashboard2"],
  },
];

const THEMES = [
  {
    id: "prod",
    name: "Prod Exact",
    description: "No CSS overrides. This is the exact captured prod snapshot running in a local iframe.",
  },
  {
    id: "calm",
    name: "Calm Premium",
    description: "Restrained premium direction: calmer surfaces, quieter borders, better spacing, and near-black action anchors.",
  },
  {
    id: "editorial",
    name: "Editorial Warmth",
    description: "A warmer, more private-wealth interpretation with softer paper tones and more editorial hierarchy.",
  },
  {
    id: "executive",
    name: "Executive Slate",
    description: "A cooler, more formal tone with stronger contrast and sharper strategic framing.",
  },
  {
    id: "dashboard-subtle",
    name: "Dashboard Subtle",
    description: "A lighter-touch refinement of the live dashboard clone: softer stat-row icons, calmer spacing, and gentler card shadows without reworking the full structure.",
    usesSharedCss: false,
  },
  {
    id: "dashboard-corporate",
    name: "Dashboard Corporate",
    description: "A cooler, more neutral-authoritative branch of Dashboard Subtle. Same structural gains, but with a more enterprise and advisory-grade tone.",
    usesSharedCss: false,
  },
  {
    id: "dashboard-base",
    name: "Dashboard Base",
    description: "A Coinbase-inspired branch: simple, accessible, and trusted, with crisper blue accents and a cleaner product-builder tone.",
    usesSharedCss: false,
  },
  {
    id: "study-metric",
    name: "Metric Study",
    description: "Card-first visual language study. This surface isolates the dashboard metric card so we can tune typography, spacing, and status treatment before restyling broader screens.",
    usesSharedCss: false,
  },
  {
    id: "study-dashboard2",
    name: "Dashboard 2 Study",
    description: "Standalone dashboard exploration. This applies the softer icon-led card treatment across the metric row and the broader dashboard panel system.",
    usesSharedCss: false,
  },
];

const STORAGE_KEY = "point93-browser-lab-state";
const THEME_SHARED_URL = "./themes/shared.css";

const els = {
  routeSelect: document.getElementById("route-select"),
  themeSelect: document.getElementById("theme-select"),
  viewportWidth: document.getElementById("viewport-width"),
  reloadButton: document.getElementById("reload-button"),
  openRawButton: document.getElementById("open-raw-button"),
  themeDescription: document.getElementById("theme-description"),
  customCss: document.getElementById("custom-css"),
  applyCssButton: document.getElementById("apply-css-button"),
  resetCssButton: document.getElementById("reset-css-button"),
  statusLine: document.getElementById("status-line"),
  screenTitle: document.getElementById("screen-title"),
  screenPath: document.getElementById("screen-path"),
  themePill: document.getElementById("theme-pill"),
  previewFrame: document.getElementById("preview-frame"),
};

const state = {
  routeId: "dashboard",
  themeId: "prod",
  viewportWidth: 2048,
  customCss: "",
};

const themeCache = new Map();

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function loadState() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return;

  try {
    const parsed = JSON.parse(raw);
    if (parsed.routeId) state.routeId = parsed.routeId;
    if (parsed.themeId) state.themeId = parsed.themeId;
    if (parsed.viewportWidth) state.viewportWidth = parsed.viewportWidth;
    if (typeof parsed.customCss === "string") state.customCss = parsed.customCss;
  } catch {
    // Ignore broken local state and continue with defaults.
  }
}

function getRoute() {
  return ROUTES.find((route) => route.id === state.routeId) ?? ROUTES[0];
}

function getAvailableThemes(route = getRoute()) {
  if (!route.themeIds?.length) return THEMES;
  return THEMES.filter((theme) => route.themeIds.includes(theme.id));
}

function getTheme() {
  return getAvailableThemes().find((theme) => theme.id === state.themeId) ?? getAvailableThemes()[0];
}

function ensureValidThemeSelection() {
  const [fallbackTheme] = getAvailableThemes();
  if (!getAvailableThemes().some((theme) => theme.id === state.themeId)) {
    state.themeId = fallbackTheme?.id ?? THEMES[0].id;
  }
}

function enforceRouteWidth() {
  const route = getRoute();
  const minWidth = route.minWidth ?? 1440;
  if (state.viewportWidth < minWidth) {
    state.viewportWidth = minWidth;
  }
}

function buildPreviewUrl(route) {
  if (route.url) return route.url;
  return `/Point93/prod_snapshot_exports/${route.file}`;
}

async function fetchText(url) {
  if (themeCache.has(url)) return themeCache.get(url);
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Failed to load ${url}`);
  const text = await response.text();
  themeCache.set(url, text);
  return text;
}

async function getThemeCss() {
  const theme = getTheme();
  if (theme.id === "prod") return "";

  const parts = [];
  if (theme.usesSharedCss !== false) {
    parts.push(await fetchText(THEME_SHARED_URL));
  }
  parts.push(await fetchText(`./themes/${theme.id}.css`));
  return parts.join("\n");
}

function setStatus(text) {
  els.statusLine.textContent = text;
}

function populateControls() {
  enforceRouteWidth();
  ensureValidThemeSelection();
  els.routeSelect.innerHTML = ROUTES.map(
    (route) => `<option value="${route.id}">${route.name}</option>`
  ).join("");

  const availableThemes = getAvailableThemes();
  els.themeSelect.innerHTML = availableThemes.map(
    (theme) => `<option value="${theme.id}">${theme.name}</option>`
  ).join("");

  els.routeSelect.value = state.routeId;
  els.themeSelect.value = state.themeId;
  els.themeSelect.disabled = availableThemes.length < 2;
  els.viewportWidth.value = state.viewportWidth;
  els.customCss.value = state.customCss;
}

function syncHeader() {
  const route = getRoute();
  const theme = getTheme();
  const minWidth = route.minWidth ?? 1440;
  els.screenTitle.textContent = route.name;
  els.screenPath.textContent = `${route.path} · min ${minWidth}px`;
  els.themePill.textContent = theme.name;
  els.themeDescription.textContent = theme.description;
}

function updateFrameWidth() {
  els.previewFrame.style.width = `${state.viewportWidth}px`;
}

function replaceNodeFromHtml(doc, node, html) {
  const template = doc.createElement("template");
  template.innerHTML = html.trim();
  const nextNode = template.content.firstElementChild;
  if (!nextNode) return;
  node.replaceWith(nextNode);
}

function repairDashboardGeometry(doc) {
  const container = doc.querySelector(".recharts-responsive-container");
  const wrapper = container?.querySelector(".recharts-wrapper");
  if (!container || !wrapper) return;

  // The captured snapshot freezes the chart at a narrower width than live prod.
  if (wrapper.getBoundingClientRect().width >= 700) return;

  const liveChartMarkup = getRuntimeFragment("dashboard-score-summary-chart");
  if (!liveChartMarkup) return;
  replaceNodeFromHtml(doc, container, liveChartMarkup);
}

function repairSnapshotGeometry() {
  const doc = els.previewFrame.contentDocument;
  if (!doc) return;

  if (getRoute().id === "dashboard") {
    repairDashboardGeometry(doc);
  }
}

function removeInjectedStyles(doc) {
  doc.getElementById("point93-theme-style")?.remove();
  doc.getElementById("point93-custom-style")?.remove();
  doc.documentElement.removeAttribute("data-point93-theme");
}

async function injectStyles() {
  const doc = els.previewFrame.contentDocument;
  if (!doc) return;

  removeInjectedStyles(doc);
  doc.documentElement.setAttribute("data-point93-theme", state.themeId);

  const themeCss = await getThemeCss();
  if (themeCss) {
    const themeStyle = doc.createElement("style");
    themeStyle.id = "point93-theme-style";
    themeStyle.textContent = themeCss;
    doc.head.appendChild(themeStyle);
  }

  if (state.customCss.trim()) {
    const customStyle = doc.createElement("style");
    customStyle.id = "point93-custom-style";
    customStyle.textContent = state.customCss;
    doc.head.appendChild(customStyle);
  }
}

function resizeFrame() {
  const doc = els.previewFrame.contentDocument;
  if (!doc) return;
  const height = Math.max(
    doc.documentElement.scrollHeight,
    doc.body?.scrollHeight ?? 0,
    900
  );
  els.previewFrame.style.height = `${height}px`;
}

async function refreshPreview(forceReload = false) {
  const route = getRoute();
  syncHeader();
  updateFrameWidth();
  saveState();

  const nextSrc = buildPreviewUrl(route);
  const sameSrc = els.previewFrame.dataset.src === nextSrc;

  if (!forceReload && sameSrc && els.previewFrame.contentDocument) {
    setStatus(`Applying ${getTheme().name} to ${route.name}…`);
    repairSnapshotGeometry();
    await injectStyles();
    resizeFrame();
    setStatus(`Ready: ${route.name} · ${getTheme().name}`);
    return;
  }

  setStatus(`Loading ${route.name} preview…`);
  els.previewFrame.dataset.src = nextSrc;

  const handleLoad = async () => {
    els.previewFrame.removeEventListener("load", handleLoad);
    repairSnapshotGeometry();
    await injectStyles();
    resizeFrame();
    setStatus(`Ready: ${route.name} · ${getTheme().name}`);
  };

  els.previewFrame.addEventListener("load", handleLoad);
  els.previewFrame.src = nextSrc;
}

function bindEvents() {
  els.routeSelect.addEventListener("change", async (event) => {
    state.routeId = event.target.value;
    ensureValidThemeSelection();
    enforceRouteWidth();
    populateControls();
    await refreshPreview(true);
  });

  els.themeSelect.addEventListener("change", async (event) => {
    state.themeId = event.target.value;
    await refreshPreview(false);
  });

  els.viewportWidth.addEventListener("change", async (event) => {
    state.viewportWidth = Number(event.target.value) || 2048;
    enforceRouteWidth();
    els.viewportWidth.value = state.viewportWidth;
    await refreshPreview(false);
  });

  els.reloadButton.addEventListener("click", async () => {
    await refreshPreview(true);
  });

  els.openRawButton.addEventListener("click", () => {
    window.open(buildPreviewUrl(getRoute()), "_blank", "noopener,noreferrer");
  });

  els.applyCssButton.addEventListener("click", async () => {
    state.customCss = els.customCss.value;
    await refreshPreview(false);
  });

  els.resetCssButton.addEventListener("click", async () => {
    state.customCss = "";
    els.customCss.value = "";
    await refreshPreview(false);
  });

  window.addEventListener("resize", () => {
    resizeFrame();
  });
}

async function init() {
  loadState();
  ensureValidThemeSelection();
  enforceRouteWidth();
  populateControls();
  bindEvents();
  syncHeader();
  updateFrameWidth();
  await refreshPreview(true);
}

init().catch((error) => {
  setStatus(`Error: ${error.message}`);
  console.error(error);
});
