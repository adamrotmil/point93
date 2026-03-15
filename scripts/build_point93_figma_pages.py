from __future__ import annotations

from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "figma_exports"


BASE_CSS = """
:root {
  --bg: #f4f5f7;
  --surface: #ffffff;
  --surface-2: #eef0f4;
  --border: #d1d5de;
  --text: #1a1d27;
  --text-muted: #5c6478;
  --accent: #2563eb;
  --accent-glow: rgba(37, 99, 235, 0.08);
  --green: #059669;
  --green-bg: rgba(5, 150, 105, 0.08);
  --amber: #d97706;
  --amber-bg: rgba(217, 119, 6, 0.08);
  --purple: #7c3aed;
  --purple-bg: rgba(124, 58, 237, 0.08);
  --rose: #e11d48;
  --rose-bg: rgba(225, 29, 72, 0.08);
  --teal: #0d9488;
  --teal-bg: rgba(13, 148, 136, 0.08);
  --orange: #ea580c;
  --orange-bg: rgba(234, 88, 12, 0.08);
  --blue-bg: rgba(37, 99, 235, 0.06);
  --gray-700: #64748b;
  --gray-bg: rgba(100, 116, 139, 0.08);
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --radius-sm: 8px;
  --radius: 12px;
  --radius-lg: 20px;
  --shadow-sm: 0 4px 12px rgba(17, 24, 39, 0.05);
  --shadow-md: 0 12px 24px rgba(17, 24, 39, 0.08);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 26%),
    linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
  color: var(--text);
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.capture-root {
  width: 1920px;
  padding: 56px 72px 88px;
}

.page-cover {
  margin-bottom: 40px;
  padding: 36px 40px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 28px;
  background: rgba(255, 255, 255, 0.92);
  box-shadow: var(--shadow-md);
}

.eyebrow {
  margin-bottom: 12px;
  color: var(--accent);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.page-cover h1 {
  margin: 0 0 12px;
  font-size: 40px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

.page-cover p {
  max-width: 1040px;
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.75;
}

.cover-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 20px;
}

.chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 999px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  background: var(--surface-2);
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
}

.section-block {
  margin-bottom: 42px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 24px;
  margin-bottom: 18px;
}

.section-header h2 {
  margin: 0 0 6px;
  font-size: 28px;
  line-height: 1.1;
  letter-spacing: -0.03em;
}

.section-header p {
  max-width: 920px;
  margin: 0;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.7;
}

.count-pill {
  padding: 8px 12px;
  border-radius: 999px;
  background: var(--accent-glow);
  color: var(--accent);
  font-size: 11px;
  font-weight: 700;
  white-space: nowrap;
}

.card-grid-2,
.card-grid-3,
.mini-grid {
  display: grid;
  gap: 16px;
}

.card-grid-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.card-grid-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.mini-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.doc-card,
.panel-card,
.token-card,
.component-card {
  padding: 20px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.92);
  box-shadow: var(--shadow-sm);
}

.doc-card h3,
.panel-card h3,
.token-card h3,
.component-card h3 {
  margin: 0 0 8px;
  font-size: 18px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.doc-card p,
.panel-card p,
.token-card p,
.component-card p {
  margin: 0;
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1.65;
}

.meta-line {
  margin-top: 12px;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
}

.list {
  margin: 12px 0 0;
  padding-left: 18px;
  color: var(--text-muted);
  font-size: 12px;
}

.list li + li {
  margin-top: 8px;
}

.swatch-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 14px;
}

.swatch {
  overflow: hidden;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 16px;
  background: white;
}

.swatch-color {
  height: 72px;
}

.swatch-info {
  padding: 12px;
}

.swatch-info strong {
  display: block;
  margin-bottom: 4px;
  font-size: 12px;
}

.swatch-info span {
  display: block;
  color: var(--text-muted);
  font-size: 11px;
}

.type-sample {
  padding: 16px 18px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 16px;
  background: white;
}

.type-name {
  margin-bottom: 8px;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.type-meta {
  margin-top: 6px;
  color: var(--text-muted);
  font-size: 11px;
}

.scale-table {
  width: 100%;
  border-collapse: collapse;
}

.scale-table th,
.scale-table td {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(209, 213, 222, 0.9);
  text-align: left;
  font-size: 12px;
  vertical-align: top;
}

.scale-table th {
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.scale-table tr:last-child td {
  border-bottom: none;
}

.token-inline {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 12px;
  background: var(--surface-2);
  font-size: 12px;
  font-weight: 700;
}

.token-dot {
  width: 12px;
  height: 12px;
  border-radius: 999px;
}

.component-preview {
  padding: 18px;
  border-radius: 18px;
  background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
  border: 1px solid rgba(209, 213, 222, 0.9);
}

.component-meta {
  margin-top: 14px;
  color: var(--text-muted);
  font-size: 11px;
}

.screen-section {
  margin-bottom: 48px;
}

.screen-block + .screen-block {
  margin-top: 28px;
}

.screen-meta {
  margin-bottom: 12px;
}

.screen-meta h3 {
  margin: 0 0 4px;
  font-size: 22px;
  line-height: 1.1;
  letter-spacing: -0.03em;
}

.screen-meta p {
  margin: 0;
  color: var(--text-muted);
  font-size: 12px;
}

.app-frame {
  width: 1440px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 24px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.desktop-shell {
  display: flex;
  align-items: stretch;
  min-height: 960px;
}

.sidebar {
  width: 220px;
  background: var(--surface-2);
  border-right: 1px solid rgba(209, 213, 222, 0.9);
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sidebar-logo {
  padding: 0 18px 16px;
  margin-bottom: 8px;
  color: var(--accent);
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -0.02em;
  border-bottom: 1px solid rgba(209, 213, 222, 0.9);
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 18px;
  color: var(--text-muted);
  font-size: 12px;
  font-weight: 500;
}

.nav-item.active {
  padding-left: 15px;
  color: var(--accent);
  background: var(--accent-glow);
  border-left: 3px solid var(--accent);
  font-weight: 700;
}

.nav-item .badge {
  margin-left: auto;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--amber-bg);
  color: var(--amber);
  font-size: 9px;
  font-weight: 800;
}

.nav-item .dot {
  margin-left: auto;
  width: 6px;
  height: 6px;
  border-radius: 999px;
  background: var(--green);
}

.sidebar-footer {
  margin-top: auto;
  padding: 18px;
  border-top: 1px solid rgba(209, 213, 222, 0.9);
}

.sidebar-footer .label {
  margin-bottom: 6px;
  color: var(--text-muted);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.progress-track {
  width: 100%;
  height: 4px;
  margin-top: 8px;
  border-radius: 999px;
  background: rgba(209, 213, 222, 0.9);
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 999px;
  background: var(--accent);
}

.main {
  flex: 1;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.content-width {
  width: 100%;
  max-width: 1188px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.page-title {
  margin: 0 0 6px;
  font-size: 28px;
  line-height: 1.1;
  letter-spacing: -0.03em;
}

.page-subtitle,
.meta,
.subtle {
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1.6;
}

.meta {
  font-weight: 600;
}

.row,
.stack,
.cluster,
.screen-grid-2,
.screen-grid-3 {
  display: flex;
  gap: 16px;
}

.stack {
  flex-direction: column;
}

.row {
  align-items: stretch;
}

.cluster {
  flex-wrap: wrap;
  align-items: center;
}

.screen-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.screen-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.panel,
.surface-card,
.metric-card,
.module-card,
.area-card,
.bi-card,
.form-card,
.question-card,
.table-card,
.cta-card {
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 18px;
  background: white;
  padding: 18px;
}

.panel-header {
  margin-bottom: 12px;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.metric-card strong,
.surface-card strong,
.module-card strong,
.area-card strong,
.bi-card strong,
.form-card strong,
.question-card strong {
  display: block;
  margin-bottom: 6px;
  font-size: 16px;
  line-height: 1.2;
}

.score-circle {
  width: 78px;
  height: 78px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 3px solid var(--accent);
  border-radius: 999px;
  color: var(--accent);
  font-size: 28px;
  font-weight: 800;
}

.score-circle.sm {
  width: 52px;
  height: 52px;
  font-size: 18px;
  border-width: 2px;
}

.band-pill,
.state-pill,
.tier-pill,
.voice-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
}

.band-pill.comp {
  background: var(--accent-glow);
  color: var(--accent);
}

.band-pill.top {
  background: var(--green-bg);
  color: var(--green);
}

.band-pill.needs {
  background: var(--amber-bg);
  color: var(--amber);
}

.band-pill.risk {
  background: var(--rose-bg);
  color: var(--rose);
}

.state-pill.info {
  background: var(--accent-glow);
  color: var(--accent);
}

.state-pill.warn {
  background: var(--amber-bg);
  color: var(--amber);
}

.state-pill.neutral {
  background: var(--surface-2);
  color: var(--text-muted);
}

.tier-pill {
  background: var(--purple-bg);
  color: var(--purple);
}

.voice-pill.v1 {
  background: var(--gray-bg);
  color: var(--gray-700);
}

.voice-pill.v2 {
  background: var(--amber-bg);
  color: var(--amber);
}

.voice-pill.v3 {
  background: var(--green-bg);
  color: var(--green);
}

.section-label {
  margin-bottom: 10px;
  color: var(--accent);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.ai-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid rgba(37, 99, 235, 0.16);
  background: var(--accent-glow);
  color: var(--accent);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.ai-inline {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: var(--teal);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.treatment {
  border-left: 4px solid var(--gray-700);
  border-radius: 16px;
  background: var(--gray-bg);
  padding: 16px;
}

.treatment.v1 {
  border-left-color: var(--teal);
  background: var(--teal-bg);
}

.treatment.v2 {
  border-left-color: var(--amber);
  background: var(--amber-bg);
}

.treatment.v3 {
  border-left-color: var(--green);
  background: var(--green-bg);
}

.lens-card {
  border: 2px solid var(--amber);
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(217, 119, 6, 0.05), rgba(245, 158, 11, 0.08));
  padding: 20px;
}

.cta-row {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.button,
.button-secondary,
.button-ghost {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 16px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
}

.button {
  background: var(--accent);
  color: white;
}

.button-secondary {
  background: var(--teal);
  color: white;
}

.button-ghost {
  border: 1px solid rgba(209, 213, 222, 0.9);
  background: var(--surface);
  color: var(--text);
}

.progress-bar {
  width: 100%;
  height: 8px;
  border-radius: 999px;
  background: rgba(209, 213, 222, 0.9);
  overflow: hidden;
}

.progress-bar > span {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--accent);
}

.dots {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(209, 213, 222, 0.9);
  text-align: left;
  vertical-align: top;
  font-size: 12px;
}

.table th {
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.table tr:last-child td {
  border-bottom: none;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field label {
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
}

.input,
.select {
  padding: 12px 14px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 12px;
  background: white;
  font-size: 12px;
}

.toggle-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 0;
}

.toggle {
  width: 40px;
  height: 22px;
  border-radius: 999px;
  background: var(--accent);
  position: relative;
}

.toggle::after {
  content: "";
  position: absolute;
  top: 3px;
  right: 3px;
  width: 16px;
  height: 16px;
  border-radius: 999px;
  background: white;
}

.toggle.off {
  background: rgba(209, 213, 222, 0.9);
}

.toggle.off::after {
  right: auto;
  left: 3px;
}

.tabs {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.tab {
  padding: 8px 14px;
  border-radius: 999px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  background: white;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
}

.tab.active {
  border-color: var(--accent);
  background: var(--accent-glow);
  color: var(--accent);
}

.question-shell {
  max-width: 760px;
  margin: 0 auto;
  padding: 28px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 24px;
  background: white;
  box-shadow: var(--shadow-sm);
}

.answer {
  padding: 14px 16px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 14px;
  background: white;
  font-size: 13px;
}

.answer.selected {
  border-color: var(--accent);
  background: var(--accent-glow);
}

.stepper {
  display: flex;
  align-items: start;
  gap: 12px;
}

.stepper-line {
  flex: 1;
  height: 4px;
  margin-top: 18px;
  border-radius: 999px;
  background: rgba(209, 213, 222, 0.9);
}

.step-node {
  min-width: 108px;
  text-align: center;
}

.step-node .bubble {
  width: 36px;
  height: 36px;
  margin: 0 auto 8px;
  border-radius: 999px;
  border: 3px solid var(--teal);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--teal);
  background: white;
  font-size: 14px;
  font-weight: 800;
}

.step-node.complete .bubble {
  background: var(--teal);
  color: white;
}

.step-node.locked {
  opacity: 0.45;
}

.timeline {
  width: 100%;
  height: 220px;
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(255,255,255,0.94), rgba(248,250,252,0.94));
  border: 1px solid rgba(209, 213, 222, 0.9);
  padding: 12px;
}

.note {
  padding: 14px 16px;
  border-radius: 16px;
  background: var(--surface-2);
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1.6;
}

.warning {
  background: var(--amber-bg);
  color: #8a4a09;
}

.success {
  background: var(--green-bg);
  color: #065f46;
}

.teal {
  color: var(--teal);
}

.teal-card {
  border-color: rgba(13, 148, 136, 0.28);
  background: linear-gradient(180deg, rgba(13,148,136,0.05), rgba(255,255,255,1));
}
"""


def document(title: str, body: str) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{title}</title>
          <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
          <style>{BASE_CSS}</style>
        </head>
        <body>
          <div class="capture-root">
            {body}
          </div>
        </body>
        </html>
        """
    )


def cover(title: str, summary: str, chips: list[str]) -> str:
    chips_html = "".join(f'<div class="chip">{chip}</div>' for chip in chips)
    return dedent(
        f"""\
        <header class="page-cover">
          <div class="eyebrow">Point93 mechanical system pass</div>
          <h1>{title}</h1>
          <p>{summary}</p>
          <div class="cover-chips">{chips_html}</div>
        </header>
        """
    )


def sidebar(active: str, in_progress: bool = True, data_available: bool = True) -> str:
    def item(label: str, icon: str, is_active: bool = False, badge: str = "", dot: bool = False) -> str:
        class_name = "nav-item active" if is_active else "nav-item"
        suffix = ""
        if badge:
            suffix = f'<span class="badge">{badge}</span>'
        elif dot:
            suffix = '<span class="dot"></span>'
        return f'<div class="{class_name}"><span>{icon}</span><span>{label}</span>{suffix}</div>'

    return dedent(
        f"""\
        <aside class="sidebar">
          <div class="sidebar-logo">Point93</div>
          {item("Dashboard", "◫", active == "Dashboard")}
          {item("My Results", "★", active == "My Results", dot=data_available)}
          {item("Assessments", "✎", active == "Assessments", badge="1 in progress" if in_progress and active != "Assessments" else "")}
          {item("My Areas", "◧", active == "My Areas")}
          {item("Business Intelligence", "◈", active == "Business Intelligence")}
          {item("What Clients Are Asking", "◇", active == "What Clients Are Asking", badge="Soon")}
          <div class="sidebar-footer">
            <div class="label">Account</div>
            <div class="tier-pill">Comprehensive</div>
            <div class="meta" style="margin-top: 10px;">5/17 modules · 29%</div>
            <div class="progress-track"><div class="progress-fill" style="width:29%;"></div></div>
          </div>
        </aside>
        """
    )


def page_shell(active: str, title: str, subtitle: str, content: str, min_height: int = 960) -> str:
    return dedent(
        f"""\
        <div class="app-frame">
          <div class="desktop-shell" style="min-height:{min_height}px;">
            {sidebar(active)}
            <main class="main">
              <div class="content-width">
                <div>
                  <h1 class="page-title">{title}</h1>
                  <div class="page-subtitle">{subtitle}</div>
                </div>
                {content}
              </div>
            </main>
          </div>
        </div>
        """
    )


def showcase(title: str, desc: str, frame_html: str) -> str:
    return dedent(
        f"""\
        <div class="screen-block">
          <div class="screen-meta">
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>
          {frame_html}
        </div>
        """
    )


def score_circle(score: str, band_class: str, band_label: str) -> str:
    color = {
        "top": "var(--green)",
        "comp": "var(--accent)",
        "needs": "var(--amber)",
        "risk": "var(--rose)",
    }[band_class]
    return dedent(
        f"""\
        <div class="row" style="align-items:center;">
          <div class="score-circle" style="border-color:{color};color:{color};">{score}</div>
          <div class="stack" style="gap:8px;">
            <div class="band-pill {band_class}">{band_label}</div>
            <div class="meta">Percentile anchored to firm category and peer group</div>
          </div>
        </div>
        """
    )


def dashboard_screen() -> str:
    content = dedent(
        """\
        <div class="panel">
          <div class="section-label">Layer 1 · Welcome & Orientation</div>
          <div class="row" style="justify-content:space-between;">
            <div class="stack" style="max-width:620px;">
              <strong>Welcome back, Adam</strong>
              <div class="page-subtitle">Point93 measures and compares your practice across modules, areas, and intelligence layers.</div>
              <div class="cta-row">
                <div class="button">Continue FT.2 Technology Capabilities</div>
                <div class="button-ghost">View Welcome Tour</div>
              </div>
            </div>
            <div class="surface-card" style="min-width:240px;">
              <div class="section-label">Progress</div>
              <strong>29% complete</strong>
              <div class="subtle">5 of 17 modules · 3 of 6 areas touched</div>
              <div class="progress-bar" style="margin-top:12px;"><span style="width:29%;"></span></div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="metric-card">
            <div class="section-label">Layer 2 · Executive Summary</div>
            <div class="row" style="align-items:center;justify-content:space-between;">
              <div class="stack">
                <strong>Overall P93 Score</strong>
                <div class="meta">You are in the 83rd percentile among comparable advisors.</div>
              </div>
              <div class="score-circle" style="border-color:var(--accent);color:var(--accent);">74</div>
            </div>
            <div class="cluster" style="margin-top:14px;">
              <div class="band-pill comp">B · Competitive</div>
              <div class="state-pill info">5 modules complete</div>
              <div class="state-pill info">2 BI profiles active</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="section-label">Area Assessment Map</div>
            <div class="screen-grid-3">
              <div class="surface-card"><strong>PF</strong><div class="meta">100% assessed</div></div>
              <div class="surface-card"><strong>FT</strong><div class="meta">67% assessed</div></div>
              <div class="surface-card"><strong>IM</strong><div class="meta">20% assessed</div></div>
              <div class="surface-card"><strong>PI</strong><div class="meta">0% assessed</div></div>
              <div class="surface-card"><strong>SC</strong><div class="meta">0% assessed</div></div>
              <div class="surface-card"><strong>FV</strong><div class="meta">0% assessed</div></div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Top strengths & gaps</div>
            <div class="screen-grid-2">
              <div class="surface-card">
                <strong>Top strengths</strong>
                <div class="stack">
                  <div>Client autonomy systems <span class="meta">91 · PF.2</span></div>
                  <div>Repeatable workflows <span class="meta">88 · FT.2</span></div>
                  <div>Compliance oversight <span class="meta">84 · PF.1</span></div>
                </div>
              </div>
              <div class="surface-card">
                <strong>Top gaps</strong>
                <div class="stack">
                  <div>Investment communication <span class="meta">49 · IM.1</span></div>
                  <div>Practice management cadence <span class="meta">56 · IM.2</span></div>
                  <div>Value articulation <span class="meta">59 · PitchPerfect</span></div>
                </div>
              </div>
            </div>
          </div>
          <div class="panel">
            <div class="section-label">Hub Verdict</div>
            <div class="ai-badge">AI generated</div>
            <div class="note" style="margin-top:12px;">Your current position is solidly Competitive, with strength clustered around structure and operational clarity. The next lift comes from how that operational quality translates into client-facing confidence and clearer differentiation.</div>
          </div>
        </div>

        <div class="panel">
          <div class="section-label">Layer 3 · Detail & Action</div>
          <div class="screen-grid-3">
            <div class="surface-card">
              <strong>Quick Win</strong>
              <div class="page-subtitle">Complete IM.2 Practice Management to unlock cross-module synthesis in Investment Strategy.</div>
              <div class="button" style="margin-top:14px;">Continue IM.2</div>
            </div>
            <div class="surface-card">
              <strong>Data Point Health</strong>
              <div class="dots" style="margin-top:10px;">
                <span class="dot" style="background:var(--green);"></span>
                <span class="dot" style="background:var(--green);"></span>
                <span class="dot" style="background:var(--accent);"></span>
                <span class="dot" style="background:var(--accent);"></span>
                <span class="dot" style="background:var(--amber);"></span>
                <span class="dot" style="background:var(--amber);"></span>
                <span class="dot" style="background:var(--rose);"></span>
                <span class="dot" style="background:var(--border);"></span>
                <span class="dot" style="background:var(--border);"></span>
              </div>
            </div>
            <div class="surface-card teal-card">
              <strong class="teal">Moenio Nudge</strong>
              <div class="ai-inline">AI reference</div>
              <div class="page-subtitle" style="margin-top:10px;">A new BI profile is available once you finish SC.1 Client Service & Communication.</div>
            </div>
          </div>
          <div class="screen-grid-3" style="margin-top:16px;">
            <div class="module-card">
              <strong>PF.1 Compliance Fundamentals</strong>
              <div class="meta">Completed · ~8 min</div>
              <div class="row" style="margin-top:10px;align-items:center;justify-content:space-between;">
                <div class="band-pill comp">78 · B · Competitive</div>
                <div class="button-ghost">View Results</div>
              </div>
            </div>
            <div class="module-card">
              <strong>FT.2 Technology Capabilities</strong>
              <div class="meta">In Progress · 67% done</div>
              <div class="progress-bar" style="margin-top:10px;"><span style="width:67%;background:var(--amber);"></span></div>
              <div class="button" style="margin-top:12px;">Continue Assessment</div>
            </div>
            <div class="module-card">
              <strong>IM.2 Practice Management</strong>
              <div class="meta">Recommended next · ~15 min</div>
              <div class="button" style="margin-top:12px;">Start Assessment</div>
            </div>
          </div>
        </div>
        """
    )
    return page_shell("Dashboard", "Dashboard", "Three-layer intelligence briefing with quick action, executive summary, and detail surfaces.", content, 1120)


def my_results_overview() -> str:
    content = dedent(
        """\
        <div class="tabs">
          <div class="tab active">Score Overview</div>
          <div class="tab">Strengths & Gaps</div>
          <div class="tab">Trends</div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Overall score + band</div>
            """ + score_circle("74", "comp", "B · Competitive") + """
            <div class="note" style="margin-top:14px;">Same platform score as Dashboard, but expanded with benchmark framing and comparison detail.</div>
          </div>
          <div class="panel">
            <div class="section-label">Area scores</div>
            <div class="screen-grid-2">
              <div class="surface-card"><strong>PF · 73</strong><div class="band-pill top">A · Top Tier</div></div>
              <div class="surface-card"><strong>FT · 71</strong><div class="band-pill comp">B · Competitive</div></div>
              <div class="surface-card"><strong>IM · 62</strong><div class="band-pill needs">C · Needs Work</div></div>
              <div class="surface-card"><strong>PI · —</strong><div class="state-pill neutral">Not assessed</div></div>
            </div>
          </div>
        </div>

        <div class="table-card">
          <div class="section-label">Module score grid</div>
          <table class="table">
            <thead>
              <tr><th>Module</th><th>Your score</th><th>Average</th><th>Top 5%</th><th>Band</th></tr>
            </thead>
            <tbody>
              <tr><td>PF.1 Compliance Fundamentals</td><td>78</td><td>66</td><td>88</td><td>B · Competitive</td></tr>
              <tr><td>PF.2 Compliance Infrastructure</td><td>76</td><td>69</td><td>91</td><td>B · Competitive</td></tr>
              <tr><td>FT.2 Technology Capabilities</td><td>71</td><td>64</td><td>86</td><td>B · Competitive</td></tr>
              <tr><td>IM.1 Client Relationship Depth</td><td>62</td><td>67</td><td>85</td><td>C · Needs Work</td></tr>
            </tbody>
          </table>
        </div>

        <div class="panel">
          <div class="section-label">Benchmark snapshot</div>
          <div class="screen-grid-3">
            <div class="surface-card"><strong>Your Score</strong><div class="page-subtitle">74 overall · 73 PF · 71 FT</div></div>
            <div class="surface-card"><strong>Peer Median</strong><div class="page-subtitle">68 overall · 66 PF · 64 FT</div></div>
            <div class="surface-card"><strong>Top 5%</strong><div class="page-subtitle">88 overall · 91 PF · 86 FT</div></div>
          </div>
        </div>
        """
    )
    return page_shell("My Results", "My Results", "All scores, bands, and benchmark comparisons across completed modules.", content)


def my_results_strengths() -> str:
    content = dedent(
        """\
        <div class="tabs">
          <div class="tab">Score Overview</div>
          <div class="tab active">Strengths & Gaps</div>
          <div class="tab">Trends</div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Full edge list</div>
            <div class="stack">
              <div class="surface-card"><strong>Can your clients operate without calling you?</strong><div class="meta">91 · PF.2 Compliance Infrastructure</div></div>
              <div class="surface-card"><strong>Are your workflows repeatable across advisors?</strong><div class="meta">88 · FT.2 Technology Capabilities</div></div>
              <div class="surface-card"><strong>Is your oversight framework durable?</strong><div class="meta">84 · PF.1 Compliance Fundamentals</div></div>
            </div>
          </div>
          <div class="panel">
            <div class="section-label">Full exposure list</div>
            <div class="stack">
              <div class="surface-card"><strong>Are investment decisions consistently framed for clients?</strong><div class="meta">49 · IM.1 Client Relationship Depth</div></div>
              <div class="surface-card"><strong>Is your operating cadence visible to the team?</strong><div class="meta">56 · IM.2 Practice Management</div></div>
              <div class="surface-card"><strong>Do prospects hear a clear value story?</strong><div class="meta">59 · PitchPerfect</div></div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Your position detail</div>
            <div class="note">You are currently closer to Top Tier than to Needs Work overall. Technology and operational structure support that position, but investment communication remains the clearest risk to upward movement.</div>
          </div>
          <div class="table-card">
            <div class="section-label">Priority gap analysis</div>
            <table class="table">
              <thead>
                <tr><th>IA</th><th>Current</th><th>Competitive floor</th><th>Gap</th></tr>
              </thead>
              <tbody>
                <tr><td>Investment Communication</td><td>49</td><td>70</td><td>21</td></tr>
                <tr><td>Practice Management Cadence</td><td>56</td><td>70</td><td>14</td></tr>
                <tr><td>Value Story Clarity</td><td>59</td><td>70</td><td>11</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        """
    )
    return page_shell("My Results", "My Results", "Full Edge and Exposure rankings with position detail and gap prioritization.", content)


def my_results_trends() -> str:
    content = dedent(
        """\
        <div class="tabs">
          <div class="tab">Score Overview</div>
          <div class="tab">Strengths & Gaps</div>
          <div class="tab active">Trends</div>
        </div>

        <div class="panel">
          <div class="section-label">Score progression</div>
          <div class="timeline">
            <svg width="100%" height="100%" viewBox="0 0 1100 190" xmlns="http://www.w3.org/2000/svg">
              <line x1="70" y1="150" x2="1040" y2="150" stroke="#d1d5de" stroke-width="2"/>
              <line x1="70" y1="106" x2="1040" y2="106" stroke="rgba(37,99,235,0.18)" stroke-width="1"/>
              <line x1="70" y1="70" x2="1040" y2="70" stroke="rgba(5,150,105,0.18)" stroke-width="1"/>
              <polyline fill="none" stroke="#2563eb" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" points="120,138 300,130 470,118 680,98 900,86"/>
              <circle cx="120" cy="138" r="6" fill="white" stroke="#2563eb" stroke-width="3"/>
              <circle cx="300" cy="130" r="6" fill="white" stroke="#2563eb" stroke-width="3"/>
              <circle cx="470" cy="118" r="6" fill="white" stroke="#2563eb" stroke-width="3"/>
              <circle cx="680" cy="98" r="6" fill="white" stroke="#2563eb" stroke-width="3"/>
              <circle cx="900" cy="86" r="6" fill="white" stroke="#2563eb" stroke-width="3"/>
              <text x="90" y="174" font-family="Inter" font-size="11" fill="#5c6478">Jan 9</text>
              <text x="270" y="174" font-family="Inter" font-size="11" fill="#5c6478">Jan 22</text>
              <text x="440" y="174" font-family="Inter" font-size="11" fill="#5c6478">Feb 1</text>
              <text x="650" y="174" font-family="Inter" font-size="11" fill="#5c6478">Feb 19</text>
              <text x="870" y="174" font-family="Inter" font-size="11" fill="#5c6478">Mar 8</text>
            </svg>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Before / after</div>
            <div class="stack">
              <div class="surface-card"><strong>FT.2 Technology Capabilities</strong><div class="meta">68 → 71 · ↑ +3</div></div>
              <div class="surface-card"><strong>PF.1 Compliance Fundamentals</strong><div class="meta">74 → 78 · ↑ +4</div></div>
            </div>
          </div>
          <div class="panel">
            <div class="section-label">Area trajectories</div>
            <div class="screen-grid-2">
              <div class="surface-card"><strong>PF</strong><div class="meta">Trending up</div></div>
              <div class="surface-card"><strong>FT</strong><div class="meta">Trending up</div></div>
              <div class="surface-card"><strong>IM</strong><div class="meta">Early data only</div></div>
              <div class="surface-card"><strong>PI</strong><div class="meta">No data yet</div></div>
            </div>
          </div>
        </div>
        """
    )
    return page_shell("My Results", "My Results", "Trendline view with reassessment deltas and area trajectories.", content)


def assessments_landing() -> str:
    area_groups = [
        ("Professional Foundation", [
            ("PF.1 Compliance Fundamentals", "Completed", "78 · B · Competitive"),
            ("PF.2 Compliance Infrastructure", "Completed", "76 · B · Competitive"),
            ("PF.3 Compliance Structure", "Available", "~8 min"),
        ]),
        ("Firm Platform & Technology", [
            ("FT.1 Platform & Product Access", "Available", "~10 min"),
            ("FT.2 Technology Capabilities", "In Progress", "67% done"),
            ("FT.3 Support & Ops Infrastructure", "Available", "~9 min"),
        ]),
        ("Investment Strategy", [
            ("IM.1 Client Relationship Depth", "Completed", "62 · C · Needs Work"),
            ("IM.2 Practice Management", "Available", "~15 min"),
            ("IM.3 Succession & Continuity", "Available", "~12 min"),
        ]),
    ]
    group_html = []
    for title, cards in area_groups:
        cards_html = []
        for name, state, meta in cards:
            state_markup = {
                "Completed": f'<div class="band-pill comp">{meta}</div><div class="button-ghost" style="margin-top:12px;">View Results</div>',
                "In Progress": f'<div class="progress-bar" style="margin-top:12px;"><span style="width:67%;background:var(--amber);"></span></div><div class="button" style="margin-top:12px;">Continue Assessment</div>',
                "Available": f'<div class="state-pill info">{meta}</div><div class="button" style="margin-top:12px;">Open Module</div>',
            }[state]
            cards_html.append(
                f"""<div class="module-card"><strong>{name}</strong><div class="meta">{state}</div>{state_markup}</div>"""
            )
        group_html.append(
            f"""<div class="panel"><div class="section-label">{title}</div><div class="screen-grid-3">{''.join(cards_html)}</div></div>"""
        )
    content = (
        '<div class="note">All 17 modules are organized by area. Each card keeps time-first framing, state clarity, and a single primary action.</div>'
        + "".join(group_html)
    )
    return page_shell("Assessments", "Assessments", "Module list view with all modules organized by area and status.", content, 1240)


def module_home(state: str) -> str:
    if state == "not-started":
        meta = '<div class="state-pill info">Available</div><div class="button">Start Assessment</div>'
        preview = "Complete this module to unlock Essential Insight, Client Voice, and Moenio Lens scaffolding."
        details = "Returning advisors see Module Home before assessment. First-time onboarding skips this page."
    elif state == "in-progress":
        meta = '<div class="state-pill warn">In Progress · 8 of 12 answered</div><div class="progress-bar"><span style="width:67%;background:var(--amber);"></span></div><div class="button">Continue Assessment</div>'
        preview = "Progress is auto-saved after every answer. Resume at the next unanswered question."
        details = "Surface the same module information, but swap the CTA and add momentum through progress framing."
    else:
        meta = '<div class="band-pill comp">78 · B · Competitive</div><div class="cta-row"><div class="button">View Results</div><div class="button-ghost">Retake Assessment</div></div>'
        preview = "Completed advisors see score context, DP fingerprint, and the primary path back into results."
        details = "Retake is always secondary to viewing the existing results."

    content = dedent(
        f"""\
        <div class="panel">
          <div class="row" style="justify-content:space-between;align-items:start;">
            <div class="stack" style="max-width:720px;">
              <div class="section-label">Module Home</div>
              <strong style="font-size:24px;">FT.2 Technology Capabilities</strong>
              <div class="page-subtitle">Measures technology adoption, digital tools, and automation across your practice.</div>
              <div class="cluster" style="margin-top:10px;">
                <div class="state-pill info">Firm Platform & Technology</div>
                <div class="state-pill neutral">12 questions</div>
                <div class="state-pill neutral">~8 minutes</div>
              </div>
            </div>
            <div class="surface-card" style="min-width:280px;">
              <div class="section-label">Status</div>
              <div class="stack">{meta}</div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Why this matters</div>
            <div class="note">{details}</div>
          </div>
          <div class="panel">
            <div class="section-label">Results preview</div>
            <div class="note">{preview}</div>
          </div>
        </div>

        <div class="panel">
          <div class="section-label">Related modules</div>
          <div class="screen-grid-3">
            <div class="module-card"><strong>FT.1 Platform & Product Access</strong><div class="meta">Available</div></div>
            <div class="module-card"><strong>FT.3 Support & Ops Infrastructure</strong><div class="meta">Available</div></div>
            <div class="module-card"><strong>PF.2 Compliance Infrastructure</strong><div class="meta">Completed · 76</div></div>
          </div>
        </div>
        """
    )
    label = {
        "not-started": "Not Started",
        "in-progress": "In Progress",
        "completed": "Completed",
    }[state]
    return page_shell("Assessments", f"Module Home · {label}", "Gateway screen shown before module questions for returning advisors.", content, 980)


def assessment_question(kind: str) -> str:
    if kind == "likert":
        answers = """
        <div class="answer">1 · Not at all true of our practice</div>
        <div class="answer">2 · Rarely true</div>
        <div class="answer selected">3 · Sometimes true</div>
        <div class="answer">4 · Usually true</div>
        <div class="answer">5 · Consistently true</div>
        """
        title = "Question Type 1 · Likert / BARS"
        subtitle = "Behaviorally anchored primary format."
    elif kind == "multiple":
        answers = """
        <div class="answer selected">We have a documented cadence and defined owners</div>
        <div class="answer">We review this informally but inconsistently</div>
        <div class="answer">This is handled ad hoc</div>
        """
        title = "Question Type 2 · Multiple Choice / Yes-No"
        subtitle = "Binary and structured branch questions."
    elif kind == "slider":
        answers = """
        <div class="panel">
          <div class="section-label">Slider response</div>
          <div class="progress-bar"><span style="width:72%;"></span></div>
          <div class="row" style="justify-content:space-between;margin-top:8px;">
            <div class="meta">0</div><div class="band-pill comp">72 / 100</div><div class="meta">100</div>
          </div>
        </div>
        """
        title = "Question Type 3 · Slider"
        subtitle = "Continuous scale input."
    else:
        answers = """
        <div class="note success">FT.2 Technology Capabilities is complete. Your score preview is now available.</div>
        <div class="row" style="align-items:center;justify-content:center;margin-top:10px;">
          <div class="score-circle" style="border-color:var(--accent);color:var(--accent);">71</div>
        </div>
        <div class="cta-row" style="justify-content:center;margin-top:16px;">
          <div class="button">View Your Results</div>
        </div>
        """
        title = "Completion Screen"
        subtitle = "Three-Act Reveal begins after completion."

    dim_sidebar = sidebar("Assessments", in_progress=True, data_available=True).replace('class="sidebar"', 'class="sidebar" style="opacity:0.7;"')
    content = dedent(
        f"""\
        <div class="app-frame">
          <div class="desktop-shell" style="min-height:960px;">
            {dim_sidebar}
            <main class="main">
              <div class="content-width">
                <div class="meta">Assessments › FT.2 Technology Capabilities</div>
                <div class="progress-bar"><span style="width:58%;"></span></div>
                <div class="row" style="justify-content:space-between;align-items:center;">
                  <div class="meta">Question 7 of 12</div>
                  <div class="button-ghost">Save & Exit</div>
                </div>
                <div class="question-shell">
                  <div class="section-label">{title}</div>
                  <strong style="font-size:24px;">How consistently does your team use defined workflow automation across recurring client operations?</strong>
                  <div class="page-subtitle" style="margin:10px 0 18px;">Answers are auto-saved after each response. One question per screen keeps momentum intact.</div>
                  <div class="stack">{answers}</div>
                </div>
              </div>
            </main>
          </div>
        </div>
        """
    )
    return showcase(title, subtitle, content)


def module_results() -> str:
    content = dedent(
        """\
        <div class="panel">
          <div class="row" style="justify-content:space-between;">
            <div class="stack" style="max-width:720px;">
              <div class="meta">Assessments › Professional Foundation › Compliance Fundamentals</div>
              <strong style="font-size:28px;">Compliance Fundamentals</strong>
              <div class="cluster">
                <div class="band-pill comp">78 · B · Competitive</div>
                <div class="state-pill info">83rd percentile</div>
                <div class="state-pill neutral">6 data points assessed</div>
              </div>
            </div>
            <div class="score-circle" style="border-color:var(--accent);color:var(--accent);">78</div>
          </div>
        </div>

        <div class="treatment v1">
          <div class="cluster" style="justify-content:space-between;">
            <div class="voice-pill v1">V1 · Key Finding</div>
            <div class="ai-badge">AI generated</div>
          </div>
          <div class="note" style="margin-top:12px;background:white;">Your compliance baseline is structurally sound, but the distribution of scores suggests execution consistency is stronger than documentation clarity when measured against the competitive set.</div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Insight Areas</div>
            <div class="stack">
              <div class="surface-card"><strong>GP1 · Can your clients operate without calling you?</strong><div class="meta">91 · Top Tier</div></div>
              <div class="surface-card"><strong>GP2 · Is documentation quality visible across the team?</strong><div class="meta">68 · Competitive</div></div>
              <div class="surface-card"><strong>GP3 · Are filing risks surfaced early enough?</strong><div class="meta">52 · At Risk</div></div>
            </div>
          </div>
          <div class="panel">
            <div class="section-label">Data Points</div>
            <div class="dots">
              <span class="dot" style="background:var(--green);"></span>
              <span class="dot" style="background:var(--green);"></span>
              <span class="dot" style="background:var(--accent);"></span>
              <span class="dot" style="background:var(--accent);"></span>
              <span class="dot" style="background:var(--amber);"></span>
              <span class="dot" style="background:var(--rose);"></span>
            </div>
            <div class="note" style="margin-top:12px;">DP dot array stays compact here but expands fully on hover/detail views in later design passes.</div>
          </div>
        </div>

        <div class="lens-card">
          <div class="cluster" style="justify-content:space-between;">
            <div class="section-label" style="color:var(--amber);">Moenio Lens</div>
            <div class="ai-badge">AI generated</div>
          </div>
          <div class="screen-grid-2">
            <div class="surface-card"><strong>What wins meetings</strong><div class="page-subtitle">Clear governance, visible standards, and strong confidence in baseline controls.</div></div>
            <div class="surface-card"><strong>What loses meetings</strong><div class="page-subtitle">Process quality is not always translating into language clients can easily understand.</div></div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Insights unlocked</div>
            <div class="note">This module contributes to PitchPerfect stage 1 and the Dashboard Hub Verdict.</div>
          </div>
          <div class="cta-card">
            <div class="section-label">Next steps</div>
            <strong>Continue to FT.2 Technology Capabilities</strong>
            <div class="page-subtitle">Closing technology workflow gaps is the fastest way to strengthen overall platform competitiveness.</div>
            <div class="button" style="margin-top:14px;">Open next module</div>
          </div>
        </div>
        """
    )
    return page_shell("Assessments", "Module Results", "Flagship post-assessment screen with score reveal, insight areas, data points, and Moenio Lens.", content, 1200)


def areas_landing() -> str:
    cards = [
        ("Professional Foundation", "73", "A · Top Tier", "100% assessed · 3 modules"),
        ("Firm Platform & Technology", "71", "B · Competitive", "100% assessed · 3 modules"),
        ("Investment Strategy", "62", "C · Needs Work", "20% assessed · 1 of 5 modules"),
        ("Planning Process", "—", "Not assessed", "0 of 3 modules"),
        ("Client Service", "—", "Not assessed", "0 of 2 modules"),
        ("Fees, Value & Positioning", "—", "Not assessed", "0 of 1 modules"),
    ]
    card_html = []
    for title, score, band, meta in cards:
        band_markup = (
            '<div class="band-pill comp">' + band + '</div>'
            if "B" in band else
            '<div class="band-pill top">' + band + '</div>'
            if "A" in band else
            '<div class="band-pill needs">' + band + '</div>'
            if "C" in band else
            '<div class="state-pill neutral">' + band + '</div>'
        )
        card_html.append(
            f"""<div class="area-card"><div class="row" style="align-items:center;justify-content:space-between;"><strong>{title}</strong><div class="score-circle sm" style="border-color:var(--{'accent' if score == '71' else 'green' if score == '73' else 'amber' if score == '62' else 'border'});color:var(--{'accent' if score == '71' else 'green' if score == '73' else 'amber' if score == '62' else 'text-muted'});">{score}</div></div>{band_markup}<div class="meta" style="margin-top:10px;">{meta}</div><div class="button-ghost" style="margin-top:14px;">View Area</div></div>"""
        )
    content = f'<div class="screen-grid-3">{"".join(card_html)}</div>'
    return page_shell("My Areas", "My Areas", "Landing view across all six practice areas with progressive completion states.", content, 980)


def area_page(progressive: bool) -> str:
    header_meta = (
        '<div class="band-pill needs">Provisional · 62 · C · Needs Work</div><div class="meta">1 of 5 modules complete</div>'
        if progressive else
        '<div class="band-pill top">73 · A · Top Tier</div><div class="meta">All modules complete</div>'
    )
    summary = (
        "Initial area score based on Client Relationship Depth only. Complete more modules for deeper cross-module analysis."
        if progressive else
        "Professional Foundation shows consistent operational maturity across modules, with strong structural alignment between governance, documentation, and oversight."
    )
    body = (
        '<div class="note warning">Cross-module gap patterns activate after the second completed module in this area.</div>'
        if progressive else
        '<div class="note success">Cross-module synthesis is now active because all constituent modules are complete.</div>'
    )
    gallery = (
        '<div class="screen-grid-3"><div class="module-card"><strong>PF.1 Compliance Fundamentals</strong><div class="meta">78 · Competitive</div></div><div class="module-card"><strong>PF.2 Compliance Infrastructure</strong><div class="meta">76 · Competitive</div></div><div class="module-card"><strong>PF.3 Compliance Structure</strong><div class="meta">65 · Competitive</div></div></div>'
        if not progressive else
        '<div class="stack"><div class="module-card"><strong>IM.1 Client Relationship Depth</strong><div class="meta">Completed · 62</div></div><div class="module-card"><strong>IM.2 Practice Management</strong><div class="meta">In Progress · 8 of 15</div></div><div class="module-card"><strong>IM.3 Succession & Continuity</strong><div class="meta">Not started</div></div></div>'
    )
    content = dedent(
        f"""\
        <div class="panel">
          <div class="row" style="align-items:start;justify-content:space-between;">
            <div class="stack" style="max-width:760px;">
              <div class="section-label">Area page</div>
              <strong style="font-size:28px;">{"Investment Strategy, Selection & Performance" if progressive else "Professional Foundation & Team Structure"}</strong>
              <div class="cluster">{header_meta}</div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Area summary</div>
            <div class="note">{summary}</div>
          </div>
          <div class="panel">
            <div class="section-label">Strength / gap signal</div>
            {body}
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Priority assessment</div>
            <div class="surface-card"><strong>{"Next: IM.2 Practice Management" if progressive else "Focus: compliance documentation clarity"}</strong><div class="page-subtitle">{"Completing the next module unlocks cross-module synthesis in this area." if progressive else "The remaining upside sits in how rigor becomes easier for clients to see and understand."}</div></div>
          </div>
          <div class="panel">
            <div class="section-label">Module gallery</div>
            {gallery}
          </div>
        </div>
        """
    )
    return page_shell("My Areas", "Area Page", "Per-area strategic view with either progressive feedback or full cross-module synthesis.", content, 980)


def bi_landing() -> str:
    products = [
        ("PitchPerfect", "Stage 2 of 4 complete", "View Profile", True),
        ("Client Referrals", "Locked until SC.1 or Purchase", "Purchase $25", False),
        ("COI Referrals", "Locked until PI.1 or Purchase", "Purchase $25", False),
        ("Client Retention Risk", "Locked until SC.1 + SC.2", "Purchase $25", False),
        ("Discovery Quality", "Locked until PI.1", "Purchase $25", False),
        ("Head to Head", "Locked until 3+ modules", "Purchase $25", False),
        ("NextGen Ready", "Locked until IM.3", "Purchase $25", False),
    ]
    cards = []
    for name, meta, cta, active in products:
        klass = "bi-card teal-card" if active else "bi-card"
        button = "button-secondary" if active else "button"
        cards.append(f'<div class="{klass}"><strong>{name}</strong><div class="meta">{meta}</div><div class="{button}" style="margin-top:14px;">{cta}</div></div>')
    content = dedent(
        f"""\
        <div class="panel teal-card">
          <div class="section-label teal">Dual access model</div>
          <div class="screen-grid-2">
            <div class="surface-card"><strong>Earn</strong><div class="page-subtitle">Complete prerequisite modules to unlock BI stages progressively.</div></div>
            <div class="surface-card"><strong>Purchase</strong><div class="page-subtitle">Buy individual profiles or the full bundle while BI remains separate from P93 scoring.</div></div>
          </div>
        </div>
        <div class="screen-grid-3">{''.join(cards)}</div>
        <div class="cta-card teal-card">
          <div class="section-label teal">Bundle</div>
          <strong>All 7 BI Products · $125</strong>
          <div class="page-subtitle">Save against individual purchase while keeping BI separate from the assessment track.</div>
        </div>
        """
    )
    return page_shell("Business Intelligence", "Business Intelligence", "Seven BI products using dual access and stage-based progression.", content, 1040)


def bi_product() -> str:
    content = dedent(
        """\
        <div class="panel teal-card">
          <div class="row" style="justify-content:space-between;">
            <div class="stack">
              <div class="meta">Business Intelligence › PitchPerfect</div>
              <strong style="font-size:28px;" class="teal">PitchPerfect</strong>
              <div class="cluster">
                <div class="band-pill comp">68 · Competitive</div>
                <div class="state-pill info">Stage 2 of 4 complete</div>
              </div>
            </div>
            <div class="score-circle" style="border-color:var(--teal);color:var(--teal);">68</div>
          </div>
        </div>

        <div class="panel teal-card">
          <div class="section-label teal">Stage map</div>
          <div class="stepper">
            <div class="step-node complete"><div class="bubble">✓</div><div class="meta">Stage 1<br/>Foundation</div></div>
            <div class="stepper-line" style="background:var(--teal);"></div>
            <div class="step-node complete"><div class="bubble">✓</div><div class="meta">Stage 2<br/>Positioning</div></div>
            <div class="stepper-line" style="background:linear-gradient(90deg,var(--teal),rgba(209,213,222,0.9));"></div>
            <div class="step-node"><div class="bubble">▶</div><div class="meta">Stage 3<br/>Differentiation</div></div>
            <div class="stepper-line"></div>
            <div class="step-node locked"><div class="bubble">🔒</div><div class="meta">Stage 4<br/>Mastery</div></div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Prerequisites</div>
            <div class="stack">
              <div class="surface-card"><strong>Stage 1</strong><div class="meta">PF.1 Compliance Fundamentals ✓</div></div>
              <div class="surface-card"><strong>Stage 2</strong><div class="meta">FT.1 Platform Access ✓</div></div>
              <div class="surface-card"><strong>Stage 4</strong><div class="meta">Requires IM.2 Practice Management</div></div>
            </div>
          </div>
          <div class="cta-card teal-card">
            <div class="section-label teal">Current stage</div>
            <strong>Start Stage 3 · Differentiation</strong>
            <div class="page-subtitle">8 questions · ~5 minutes · builds on completed BI stages.</div>
            <div class="button-secondary" style="margin-top:14px;">Start Stage 3</div>
          </div>
        </div>

        <div class="panel">
          <div class="section-label">Completed stage results</div>
          <div class="stack">
            <div class="treatment v1"><div class="voice-pill v1">Stage 2 · Positioning</div><div class="note" style="margin-top:12px;background:white;">Positioning language is improving, but differentiation is still too dependent on process quality rather than a clear client-facing value story.</div></div>
            <div class="treatment v1"><div class="voice-pill v1">Stage 1 · Foundation</div><div class="note" style="margin-top:12px;background:white;">Operational foundations are strong enough to support a credible pitch once message discipline becomes clearer.</div></div>
          </div>
        </div>
        """
    )
    return page_shell("Business Intelligence", "BI Product Page", "Stage-based BI detail page with prerequisites, current stage CTA, and cumulative results.", content, 1120)


def coming_soon() -> str:
    content = dedent(
        """\
        <div class="panel">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div class="stack">
              <div class="section-label">What Clients Are Asking</div>
              <strong style="font-size:28px;">Coming Soon</strong>
              <div class="page-subtitle">v1 exposes the nav item and an explanatory landing page only.</div>
            </div>
            <div class="state-pill warn">Coming Soon</div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Value proposition</div>
            <div class="note">This future feature will surface current client questions and market concerns using the same one-question-per-screen assessment pattern you already know.</div>
          </div>
          <div class="panel">
            <div class="section-label">Preview format</div>
            <div class="surface-card"><strong>Periodic strategic pulse</strong><div class="page-subtitle">10–15 questions on live industry topics with profile-style output when released.</div></div>
          </div>
        </div>

        <div class="cta-card">
          <div class="section-label">Launch interest</div>
          <strong>Notify me when available</strong>
          <div class="page-subtitle">Used in v1 instead of assessment functionality.</div>
          <div class="button" style="margin-top:14px;">Join notification list</div>
        </div>
        """
    )
    return page_shell("What Clients Are Asking", "What Clients Are Asking", "Coming Soon state for the future lead-generation feature.", content, 880)


def onboarding_preview() -> str:
    return dedent(
        """\
        <div class="app-frame">
          <div class="stack" style="padding:32px;gap:24px;min-height:960px;">
            <div class="row" style="justify-content:space-between;align-items:center;">
              <strong style="font-size:24px;color:var(--accent);">Point93</strong>
              <div class="button-ghost">Sign In</div>
            </div>
            <div class="row" style="justify-content:space-between;align-items:center;">
              <div class="stack" style="max-width:560px;">
                <div class="section-label">Step 1 · Public Preview</div>
                <strong style="font-size:40px;line-height:1.05;">Measure where your practice stands before you decide what comes next.</strong>
                <div class="page-subtitle">The preview uses real product components with sample data, so first-time advisors understand the output before creating an account.</div>
                <div class="cta-row">
                  <div class="button">Get Started</div>
                  <div class="button-ghost">View sample results</div>
                </div>
              </div>
              <div class="panel" style="width:560px;">
                <div class="section-label">Sample module result</div>
                <div class="screen-grid-2">
                  <div class="surface-card"><strong>Sample score</strong><div class="band-pill comp">72 · B · Competitive</div></div>
                  <div class="surface-card"><strong>Sample treatment</strong><div class="ai-badge">AI generated</div></div>
                </div>
                <div class="lens-card" style="margin-top:16px;">
                  <div class="section-label" style="color:var(--amber);">Sample Moenio Lens</div>
                  <div class="page-subtitle">The preview clearly labels all output as sample/demo.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        """
    )


def onboarding_signup() -> str:
    return dedent(
        """\
        <div class="app-frame">
          <div class="stack" style="padding:32px;gap:24px;min-height:960px;justify-content:center;align-items:center;">
            <div class="question-shell" style="max-width:640px;width:100%;">
              <div class="section-label">Step 2 · Email Sign-Up</div>
              <strong style="font-size:28px;">Create your Point93 account</strong>
              <div class="page-subtitle">Accounts start on the Essential tier. No payment is required during onboarding.</div>
              <div class="stack" style="margin-top:18px;">
                <div class="field"><label>Full Name</label><div class="input">Adam Rotmil</div></div>
                <div class="field"><label>Email</label><div class="input">rotmila@evolve24.com</div></div>
                <div class="field"><label>Firm Association</label><div class="input">Evolve24</div></div>
              </div>
              <div class="button" style="margin-top:18px;">Create Account</div>
            </div>
          </div>
        </div>
        """
    )


def onboarding_ranking() -> str:
    cards = []
    modules = [
        "FT.2 Technology Capabilities",
        "IM.2 Practice Management",
        "PF.1 Compliance Fundamentals",
        "PI.1 Client Discovery",
        "SC.1 Client Service",
        "FV.1 Fees, Value & Positioning",
    ]
    for index, module in enumerate(modules, start=1):
        cards.append(
            f'<div class="module-card"><div class="row" style="justify-content:space-between;align-items:center;"><strong>{index}. {module}</strong><div class="state-pill neutral">Drag</div></div><div class="meta">Default order can be accepted or adjusted.</div></div>'
        )
    return dedent(
        f"""\
        <div class="app-frame">
          <div class="stack" style="padding:32px;gap:24px;min-height:960px;">
            <div>
              <div class="section-label">Step 3 · Module Ranking</div>
              <strong style="font-size:32px;">Set your starting order</strong>
              <div class="page-subtitle">Ranking determines the recommended assessment path, quick wins, and next-module suggestions.</div>
            </div>
            <div class="screen-grid-2">
              <div class="stack">{''.join(cards)}</div>
              <div class="panel">
                <div class="section-label">What this affects</div>
                <div class="stack">
                  <div class="surface-card"><strong>Assessments Landing</strong><div class="meta">Recommended order and highlighted next module</div></div>
                  <div class="surface-card"><strong>Dashboard Quick Win</strong><div class="meta">Highest-priority next step after each completion</div></div>
                  <div class="surface-card"><strong>Onboarding flow</strong><div class="meta">First-time path routes directly into the top-ranked module</div></div>
                </div>
                <div class="button" style="margin-top:16px;">Save Ranking & Start #1 Module</div>
              </div>
            </div>
          </div>
        </div>
        """
    )


def settings_screen() -> str:
    content = dedent(
        """\
        <div class="screen-grid-2">
          <div class="form-card">
            <div class="section-label">Profile information</div>
            <div class="stack">
              <div class="field"><label>Full Name</label><div class="input">Jane Doe</div></div>
              <div class="field"><label>Email (read-only)</label><div class="input">jane.doe@example.com</div></div>
              <div class="field"><label>Firm Association</label><div class="input">Merrill Lynch</div></div>
            </div>
          </div>
          <div class="form-card">
            <div class="section-label">Firm & practice details</div>
            <div class="stack">
              <div class="field"><label>Team Size</label><div class="input">12</div></div>
              <div class="field"><label>Number of Advisors</label><div class="input">4</div></div>
              <div class="field"><label>Advisor Category</label><div class="select">Senior Partner</div></div>
              <div class="field"><label>Type of Firm</label><div class="select">Wealth Management — Large</div></div>
            </div>
          </div>
        </div>

        <div class="screen-grid-2">
          <div class="panel">
            <div class="section-label">Platform preferences</div>
            <div class="toggle-row"><span>New results available</span><div class="toggle"></div></div>
            <div class="toggle-row"><span>BI stage unlocks</span><div class="toggle"></div></div>
            <div class="toggle-row"><span>Platform updates</span><div class="toggle off"></div></div>
            <div class="toggle-row"><span>Anonymous benchmarking pool</span><div class="toggle"></div></div>
            <div class="toggle-row"><span>Practice data sharing</span><div class="toggle off"></div></div>
          </div>
          <div class="panel">
            <div class="section-label">Tier management</div>
            <div class="tier-pill">Professional · $115</div>
            <div class="note" style="margin-top:14px;">Upgrade prompts remain inline and never block access to existing scores.</div>
            <div class="cta-card" style="margin-top:16px;">
              <strong>Upgrade to Comprehensive · $175</strong>
              <div class="page-subtitle">Unlock deeper voice coverage, full Moenio Lens depth, and complete treatment rendering.</div>
              <div class="button" style="margin-top:14px;">Upgrade</div>
            </div>
          </div>
        </div>
        """
    )
    return page_shell("Dashboard", "Settings & Profile", "Account management, preferences, privacy, and tier settings.", content, 1040)


def reference_page() -> str:
    body = [
        cover(
            "Point93 / Reference",
            "This page anchors the rebuild effort. It documents the frozen source archive, the governing spec documents, and the 23-screen MVP scope that the cleaned Point93 pages will preserve.",
            [
                "Frozen source archive kept separate",
                "23 MVP states in scope",
                "Blueprint, wireframes, tokens, flows, IA map",
            ],
        ),
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">Source inputs</div>
              <h2>Governed by the design archive</h2>
              <p>These are the documents used as the source of truth for layout, states, navigation, scoring, treatment hierarchy, and system scaffolding.</p>
            </div>
            <div class="count-pill">5 primary sources</div>
          </div>
          <div class="card-grid-2">
            <div class="doc-card"><h3>Blueprint v1.6.1</h3><p>Defines page architecture, state behavior, tier logic, and diagnostic rules across Dashboard, My Results, Assessments, My Areas, BI, onboarding, and settings.</p><div class="meta-line">Sections used most: §3–§10, §16–§17</div></div>
            <div class="doc-card"><h3>Wireframes v1.2</h3><p>Provides the current layout shapes and the flagship screen patterns. Useful for spatial composition even when the current capture is noisy.</p><div class="meta-line">13 panels</div></div>
            <div class="doc-card"><h3>Design Tokens v1.0</h3><p>Defines the mechanical Point93 system: colors, voice treatments, score display, motion timings, and UI chrome.</p><div class="meta-line">Foundation source for tokens</div></div>
            <div class="doc-card"><h3>Interaction Flows v1.0</h3><p>Captures the mainline product flows and edge cases needed for the FigJam diagram and cross-screen logic checks.</p><div class="meta-line">11 flow diagrams</div></div>
            <div class="doc-card"><h3>IA Map v2</h3><p>Confirms module, area, and My Results information architecture, especially where the wireframes do not provide a dedicated screen.</p><div class="meta-line">Used to synthesize My Results</div></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">Frozen source</div>
              <h2>Existing imported archive</h2>
              <p>The original HTML capture is preserved as source reference only. The rebuild effort does not edit that geometry in place.</p>
            </div>
            <div class="count-pill">Design node 4:2</div>
          </div>
          <div class="panel-card">
            <h3>Point93 MVP Clean Import</h3>
            <p>The earlier capture remains frozen so the cleaned Point93 pages can be rebuilt independently. This keeps the design file auditable and avoids continued salvage of clipped or auto-layout-flattened geometry.</p>
            <ul class="list">
              <li>Use the frozen import to compare structure, not as the final page system.</li>
              <li>All cleaned screens are recreated as new native Figma frames on dedicated Point93 pages.</li>
              <li>The unrelated <strong>UI Kit</strong> page is left untouched.</li>
            </ul>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">MVP scope</div>
              <h2>23 screens and states</h2>
              <p>The cleaned Point93 system preserves the complete MVP screen inventory used in the prior audit.</p>
            </div>
            <div class="count-pill">4 rebuild batches</div>
          </div>
          <div class="card-grid-3">
            <div class="panel-card"><h3>Batch A</h3><p>Dashboard plus My Results Score Overview, Strengths & Gaps, and Trends.</p></div>
            <div class="panel-card"><h3>Batch B</h3><p>Assessments Landing, Module Home x3, Assessment x4, and Module Results.</p></div>
            <div class="panel-card"><h3>Batch C</h3><p>My Areas Landing, Area Page x2, BI Landing, and BI Product Page.</p></div>
            <div class="panel-card"><h3>Batch D</h3><p>Onboarding x3, Settings & Profile, and What Clients Are Asking.</p></div>
            <div class="panel-card"><h3>Structural rules</h3><p>Desktop-first, 1440px canvases, 220px sidebar, 32px content padding, and explicit Fill/Hug logic for cleaned frames.</p></div>
            <div class="panel-card"><h3>System rules</h3><p>Mechanical tokens, component scaffolding, and clean state representation now. Visual mood and brand exploration later.</p></div>
          </div>
        </section>
        """,
    ]
    return document("Point93 / Reference", "".join(body))


def foundations_page() -> str:
    swatches = [
        ("UI / bg", "#f4f5f7", "Canvas background"),
        ("UI / surface", "#ffffff", "Cards and app frames"),
        ("UI / surface-2", "#eef0f4", "Sidebar and subdued containers"),
        ("UI / border", "#d1d5de", "Rules and strokes"),
        ("UI / text", "#1a1d27", "Primary text"),
        ("UI / text-muted", "#5c6478", "Secondary text"),
        ("Brand / accent", "#2563eb", "Primary action"),
        ("Brand / accent-glow", "rgba(37,99,235,0.08)", "Selection fill"),
        ("Band / top-tier", "#059669", "Top Tier"),
        ("Band / competitive", "#2563eb", "Competitive"),
        ("Band / needs-work", "#d97706", "Needs Work"),
        ("Band / at-risk", "#e11d48", "At Risk"),
        ("Voice / v1-gray", "#64748b", "Point93 analytical"),
        ("Voice / v1-teal", "#0d9488", "Point93 analytical accent"),
        ("Voice / v2-gold", "#d97706", "Client voice"),
        ("Voice / v3-green", "#059669", "External benchmark"),
        ("Tier / essential", "#64748b", "Essential"),
        ("Tier / professional", "#2563eb", "Professional"),
        ("Tier / comprehensive", "#7c3aed", "Comprehensive"),
        ("BI / teal", "#0d9488", "Business Intelligence"),
    ]
    swatch_html = []
    for name, color, usage in swatches:
        swatch_html.append(
            f'<div class="swatch"><div class="swatch-color" style="background:{color};"></div><div class="swatch-info"><strong>{name}</strong><span>{color}</span><span>{usage}</span></div></div>'
        )

    body = [
        cover(
            "Point93 / Foundations",
            "Mechanical Point93 foundations translated from the token spec: color system, typography, spacing, radii, strokes, motion, and semantic voice/tier/band cues.",
            [
                "Scoped under p93 naming",
                "Inter for temporary mechanical type",
                "Ready for later mood-board restyle",
            ],
        ),
        f"""
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">p93/color/*</div>
              <h2>Color variables</h2>
              <p>The Point93 system uses semantic color families instead of decorative color. The first pass includes UI chrome, bands, voices, tiers, BI, and support colors.</p>
            </div>
            <div class="count-pill">20 core colors</div>
          </div>
          <div class="swatch-grid">{''.join(swatch_html)}</div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">P93/Typography/*</div>
              <h2>Type system</h2>
              <p>Inter is the temporary mechanical type family. Hierarchy is kept neutral so later visual direction can swap type with minimal structural change.</p>
            </div>
            <div class="count-pill">9 text styles</div>
          </div>
          <div class="card-grid-3">
            <div class="type-sample"><div class="type-name">Screen title</div><div style="font-size:40px;font-weight:700;line-height:1.05;letter-spacing:-0.04em;">Point93 Screen</div><div class="type-meta">40 / 700 / -4%</div></div>
            <div class="type-sample"><div class="type-name">Page title</div><div style="font-size:28px;font-weight:700;line-height:1.1;letter-spacing:-0.03em;">Dashboard</div><div class="type-meta">28 / 700 / -3%</div></div>
            <div class="type-sample"><div class="type-name">Section label</div><div style="font-size:11px;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;color:#2563eb;">Executive Summary</div><div class="type-meta">11 / 800 / 8%</div></div>
            <div class="type-sample"><div class="type-name">Card title</div><div style="font-size:18px;font-weight:700;line-height:1.2;">Overall Score</div><div class="type-meta">18 / 700</div></div>
            <div class="type-sample"><div class="type-name">Body</div><div style="font-size:13px;line-height:1.75;">Advisors complete modules across six practice areas and receive scored diagnostic intelligence.</div><div class="type-meta">13 / 400 / 175% line height</div></div>
            <div class="type-sample"><div class="type-name">Small body</div><div style="font-size:12px;line-height:1.65;">Compact screen explanation and support copy.</div><div class="type-meta">12 / 400 / 165%</div></div>
            <div class="type-sample"><div class="type-name">Label</div><div style="font-size:11px;font-weight:700;">Notification Preferences</div><div class="type-meta">11 / 700</div></div>
            <div class="type-sample"><div class="type-name">Caption</div><div style="font-size:10px;font-weight:600;color:#5c6478;">AI denotation, meta tags, and helper text.</div><div class="type-meta">10 / 600</div></div>
            <div class="type-sample"><div class="type-name">Mono/meta</div><div style="font-family:ui-monospace, SFMono-Regular, Menlo, monospace;font-size:11px;color:#5c6478;">Blueprint §5.4 · IA Map §4.3</div><div class="type-meta">11 / mono</div></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">p93/space/* · p93/radius/* · p93/stroke/*</div>
              <h2>Spacing, radius, and strokes</h2>
              <p>The first pass keeps the scale intentionally small and reusable across screens, components, and future variants.</p>
            </div>
            <div class="count-pill">Mechanical layout scale</div>
          </div>
          <div class="card-grid-3">
            <div class="token-card"><h3>Spacing</h3><table class="scale-table"><tr><th>Token</th><th>Value</th><th>Use</th></tr><tr><td>p93/space/1</td><td>4</td><td>Inline icon gaps</td></tr><tr><td>p93/space/2</td><td>8</td><td>Tight stack spacing</td></tr><tr><td>p93/space/3</td><td>12</td><td>Card interior grouping</td></tr><tr><td>p93/space/4</td><td>16</td><td>Default card padding</td></tr><tr><td>p93/space/5</td><td>24</td><td>Section spacing</td></tr><tr><td>p93/space/6</td><td>32</td><td>Page padding</td></tr></table></div>
            <div class="token-card"><h3>Radii</h3><table class="scale-table"><tr><th>Token</th><th>Value</th><th>Use</th></tr><tr><td>p93/radius/sm</td><td>8</td><td>Inputs, pills, small cards</td></tr><tr><td>p93/radius/md</td><td>12</td><td>Default cards and buttons</td></tr><tr><td>p93/radius/lg</td><td>20</td><td>Hero shells and page containers</td></tr></table></div>
            <div class="token-card"><h3>Strokes</h3><table class="scale-table"><tr><th>Token</th><th>Value</th><th>Use</th></tr><tr><td>p93/stroke/1</td><td>1</td><td>Standard card and table rules</td></tr><tr><td>p93/stroke/1.5</td><td>1.5</td><td>Emphasis rows and previews</td></tr><tr><td>p93/stroke/2</td><td>2</td><td>State emphasis and shells</td></tr><tr><td>p93/stroke/3</td><td>3</td><td>Score circles and active nav</td></tr></table></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">p93/motion/*</div>
              <h2>Motion timings and semantic cues</h2>
              <p>Motion remains documented for future behavior work. This pass only records timing scaffolding so the design system is structurally complete.</p>
            </div>
            <div class="count-pill">4 timing tokens</div>
          </div>
          <div class="card-grid-2">
            <div class="token-card"><h3>Motion timings</h3><table class="scale-table"><tr><th>Token</th><th>Value</th><th>Use</th></tr><tr><td>p93/motion/hover</td><td>200ms</td><td>Card hover and button transitions</td></tr><tr><td>p93/motion/answer</td><td>700ms</td><td>Micro reward after answer submit</td></tr><tr><td>p93/motion/reveal</td><td>800ms</td><td>Score count-up reveal</td></tr><tr><td>p93/motion/celebration</td><td>2400ms</td><td>Module completion celebration sequence</td></tr></table></div>
            <div class="token-card"><h3>Voice, band, and tier cues</h3><div class="cluster"><div class="voice-pill v1">V1</div><div class="voice-pill v2">V2</div><div class="voice-pill v3">V3</div><div class="band-pill top">Top Tier</div><div class="band-pill comp">Competitive</div><div class="band-pill needs">Needs Work</div><div class="band-pill risk">At Risk</div><div class="tier-pill">Comprehensive</div></div><div class="component-meta">These semantic wrappers carry into treatments, score displays, tier prompts, and BI accents.</div></div>
          </div>
        </section>
        """,
    ]
    return document("Point93 / Foundations", "".join(body))


def components_page() -> str:
    body = [
        cover(
            "Point93 / Components",
            "Mechanical component scaffolding for the MVP. These are the canonical Point93 patterns used to rebuild screens cleanly while the visual language stays intentionally neutral.",
            [
                "Navigation, layout, scoring, assessment, areas, BI, settings",
                "Promote reusable patterns only",
                "Neutral mechanics, no mood-board polish yet",
            ],
        ),
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">P93 / Navigation + Layout</div>
              <h2>Shell components</h2>
              <p>These primitives define the overall Point93 desktop frame before product-specific content gets placed inside.</p>
            </div>
            <div class="count-pill">6 layout primitives</div>
          </div>
          <div class="card-grid-2">
            <div class="component-card"><h3>Sidebar shell</h3><div class="component-preview">""" + sidebar("Dashboard") + """</div><div class="component-meta">220px fixed sidebar, active state with 3px accent rule, account summary at the bottom.</div></div>
            <div class="component-card"><h3>Page header block</h3><div class="component-preview"><div class="stack"><div class="section-label">Page context</div><strong style="font-size:28px;">Dashboard</strong><div class="page-subtitle">Three-layer intelligence briefing with quick action and executive summary surfaces.</div></div></div><div class="component-meta">Used across all Point93 app screens.</div></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">P93 / Scoring + Intelligence</div>
              <h2>Score and intelligence patterns</h2>
              <p>Core score, band, AI, and treatment structures that recur across Dashboard, My Results, Module Results, and BI.</p>
            </div>
            <div class="count-pill">8 reusable patterns</div>
          </div>
          <div class="card-grid-3">
            <div class="component-card"><h3>Score circle</h3><div class="component-preview">""" + score_circle("78", "comp", "B · Competitive") + """</div><div class="component-meta">Module, area, BI, and overall score anchor.</div></div>
            <div class="component-card"><h3>Band and state chips</h3><div class="component-preview"><div class="cluster"><div class="band-pill top">A · Top Tier</div><div class="band-pill comp">B · Competitive</div><div class="band-pill needs">C · Needs Work</div><div class="band-pill risk">D · At Risk</div><div class="state-pill info">In Progress</div><div class="state-pill warn">Coming Soon</div></div></div><div class="component-meta">Used for scoring, states, and supporting status.</div></div>
            <div class="component-card"><h3>AI denotation</h3><div class="component-preview"><div class="stack"><div class="ai-badge">AI generated</div><div class="ai-inline">AI reference</div><div class="treatment v1"><div class="voice-pill v1">V1 · Key Finding</div><div class="note" style="margin-top:12px;background:white;">Diagnostic narration with semantic treatment structure.</div></div></div></div><div class="component-meta">Prominent badge + compact inline marker.</div></div>
            <div class="component-card"><h3>Treatment block variants</h3><div class="component-preview"><div class="stack"><div class="treatment v1"><div class="voice-pill v1">V1</div></div><div class="treatment v2"><div class="voice-pill v2">V2</div></div><div class="treatment v3"><div class="voice-pill v3">V3</div></div></div></div><div class="component-meta">Maps the three-voice system into reusable content shells.</div></div>
            <div class="component-card"><h3>Tier prompt</h3><div class="component-preview"><div class="cta-card"><strong>Upgrade to Comprehensive</strong><div class="page-subtitle">Unlock deeper treatment coverage without gating scores.</div><div class="button" style="margin-top:12px;">Upgrade</div></div></div><div class="component-meta">Inline and contextual only.</div></div>
            <div class="component-card"><h3>Moenio Lens shell</h3><div class="component-preview"><div class="lens-card"><div class="section-label" style="color:var(--amber);">Moenio Lens</div><div class="screen-grid-2"><div class="surface-card"><strong>Wins meetings</strong></div><div class="surface-card"><strong>Loses meetings</strong></div></div></div></div><div class="component-meta">Distinct gold-bordered intelligence container.</div></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">P93 / Assessments</div>
              <h2>Assessment components</h2>
              <p>Core assessment patterns used in module discovery, gateway states, question flow, and post-completion results.</p>
            </div>
            <div class="count-pill">7 assessment patterns</div>
          </div>
          <div class="card-grid-3">
            <div class="component-card"><h3>Module card</h3><div class="component-preview"><div class="module-card"><strong>FT.2 Technology Capabilities</strong><div class="meta">In Progress · 67% done</div><div class="progress-bar" style="margin-top:12px;"><span style="width:67%;background:var(--amber);"></span></div><div class="button" style="margin-top:12px;">Continue Assessment</div></div></div><div class="component-meta">Single primary CTA and time/progress-first framing.</div></div>
            <div class="component-card"><h3>DP dot array</h3><div class="component-preview"><div class="stack"><div class="dots"><span class="dot" style="background:var(--green);"></span><span class="dot" style="background:var(--green);"></span><span class="dot" style="background:var(--accent);"></span><span class="dot" style="background:var(--amber);"></span><span class="dot" style="background:var(--rose);"></span></div><div class="note">Hover detail box lives adjacent in later interaction passes.</div></div></div><div class="component-meta">Compact module fingerprint without exposing full DP detail.</div></div>
            <div class="component-card"><h3>Question shell</h3><div class="component-preview"><div class="question-shell" style="max-width:none;"><strong style="font-size:22px;">How consistently does your team use workflow automation?</strong><div class="stack" style="margin-top:16px;"><div class="answer selected">Usually true</div><div class="answer">Sometimes true</div><div class="answer">Rarely true</div></div></div></div><div class="component-meta">One question per screen with preserved answer state.</div></div>
            <div class="component-card"><h3>Progress bar</h3><div class="component-preview"><div class="stack"><div class="meta">Question 7 of 12</div><div class="progress-bar"><span style="width:58%;"></span></div></div></div><div class="component-meta">Used in question flow and gateway momentum surfaces.</div></div>
            <div class="component-card"><h3>Completion CTA block</h3><div class="component-preview"><div class="cta-card"><strong>FT.2 Technology Capabilities is complete</strong><div class="page-subtitle">Your score preview is available. Continue into Three-Act Reveal.</div><div class="button" style="margin-top:12px;">View Your Results</div></div></div><div class="component-meta">Transitions assessment completion into Module Results.</div></div>
            <div class="component-card"><h3>Module Home state</h3><div class="component-preview"><div class="panel"><div class="section-label">Module Home</div><strong>FT.2 Technology Capabilities</strong><div class="state-pill warn" style="margin-top:10px;">In Progress · 8 of 12 answered</div><div class="button" style="margin-top:12px;">Continue Assessment</div></div></div><div class="component-meta">Gateway pattern for returning visitors.</div></div>
          </div>
        </section>
        """,
        """
        <section class="section-block">
          <div class="section-header">
            <div>
              <div class="eyebrow">P93 / Areas + BI + Settings</div>
              <h2>Supporting product patterns</h2>
              <p>Core patterns that round out areas, BI, forms, navigation tabs, and empty-state utility blocks.</p>
            </div>
            <div class="count-pill">9 supporting patterns</div>
          </div>
          <div class="card-grid-3">
            <div class="component-card"><h3>Area card</h3><div class="component-preview"><div class="area-card"><strong>Professional Foundation</strong><div class="band-pill top" style="margin-top:10px;">73 · A · Top Tier</div><div class="meta" style="margin-top:10px;">100% assessed · 3 modules</div></div></div><div class="component-meta">Used on My Areas landing and previews.</div></div>
            <div class="component-card"><h3>BI product card</h3><div class="component-preview"><div class="bi-card teal-card"><strong>PitchPerfect</strong><div class="meta">Stage 2 of 4 complete</div><div class="button-secondary" style="margin-top:12px;">View Profile</div></div></div><div class="component-meta">Distinct BI palette and state model.</div></div>
            <div class="component-card"><h3>BI stage stepper</h3><div class="component-preview"><div class="stepper"><div class="step-node complete"><div class="bubble">✓</div><div class="meta">1</div></div><div class="stepper-line" style="background:var(--teal);"></div><div class="step-node"><div class="bubble">▶</div><div class="meta">2</div></div><div class="stepper-line"></div><div class="step-node locked"><div class="bubble">🔒</div><div class="meta">3</div></div></div></div><div class="component-meta">Used on BI Product Page.</div></div>
            <div class="component-card"><h3>Tabs</h3><div class="component-preview"><div class="tabs"><div class="tab active">Score Overview</div><div class="tab">Strengths & Gaps</div><div class="tab">Trends</div></div></div><div class="component-meta">Used on My Results and future tabbed surfaces.</div></div>
            <div class="component-card"><h3>Text field + select</h3><div class="component-preview"><div class="stack"><div class="field"><label>Full Name</label><div class="input">Jane Doe</div></div><div class="field"><label>Type of Firm</label><div class="select">Wealth Management — Large</div></div></div></div><div class="component-meta">Settings and onboarding structure.</div></div>
            <div class="component-card"><h3>Toggle row</h3><div class="component-preview"><div class="toggle-row"><span>Anonymous benchmarking pool</span><div class="toggle"></div></div><div class="toggle-row"><span>Practice data sharing</span><div class="toggle off"></div></div></div><div class="component-meta">Settings preference rows.</div></div>
            <div class="component-card"><h3>Comparison row</h3><div class="component-preview"><table class="table"><thead><tr><th>Metric</th><th>Your score</th><th>Peer median</th></tr></thead><tbody><tr><td>Overall</td><td>74</td><td>68</td></tr></tbody></table></div><div class="component-meta">Benchmark tables and summary rows.</div></div>
            <div class="component-card"><h3>Empty / Coming Soon block</h3><div class="component-preview"><div class="note warning">Complete a module to unlock this area of the product.</div></div><div class="component-meta">Used for pre-data and future-state messaging.</div></div>
            <div class="component-card"><h3>CTA card</h3><div class="component-preview"><div class="cta-card"><strong>Notify me when available</strong><div class="page-subtitle">Used for What Clients Are Asking in v1.</div><div class="button" style="margin-top:12px;">Join notification list</div></div></div><div class="component-meta">Flexible call-to-action shell.</div></div>
          </div>
        </section>
        """,
    ]
    return document("Point93 / Components", "".join(body))


def screens_page() -> str:
    batch_a = [
        showcase("Dashboard", "Three-layer intelligence briefing rebuilt as a clean desktop frame.", dashboard_screen()),
        showcase("My Results · Score Overview", "Tabbed results view with score, area, and benchmark structures.", my_results_overview()),
        showcase("My Results · Strengths & Gaps", "Full Edge/Exposure surface with ranking and gap analysis.", my_results_strengths()),
        showcase("My Results · Trends", "Trendline and before/after view for reassessment-aware reporting.", my_results_trends()),
    ]

    batch_b = [
        showcase("Assessments Landing", "Module list view with grouped area sections and state-aware cards.", assessments_landing()),
        showcase("Module Home · Not Started", "Gateway screen for a returning advisor before the first answer.", module_home("not-started")),
        showcase("Module Home · In Progress", "Gateway screen with preserved progress and resume affordance.", module_home("in-progress")),
        showcase("Module Home · Completed", "Gateway screen after results exist, with retake secondary to view-results.", module_home("completed")),
        assessment_question("likert"),
        assessment_question("multiple"),
        assessment_question("slider"),
        assessment_question("completion"),
        showcase("Module Results", "Flagship results page with score reveal, insights, data points, and Moenio Lens.", module_results()),
    ]

    batch_c = [
        showcase("My Areas Landing", "Landing page across all six practice areas with mixed completion states.", areas_landing()),
        showcase("Area Page · Full Cross-Module Synthesis", "Completed-area view with strong cross-module analysis.", area_page(False)),
        showcase("Area Page · Progressive Feedback", "Partial-area view with provisional score and next-module prompt.", area_page(True)),
        showcase("Business Intelligence Landing", "Seven BI products with dual access and separate scoring logic.", bi_landing()),
        showcase("BI Product Page", "Stage-based BI detail with prerequisites, stepper, and cumulative results.", bi_product()),
    ]

    batch_d = [
        showcase("Onboarding · Public Preview", "First-time landing that previews real Point93 output with sample data.", onboarding_preview()),
        showcase("Onboarding · Email Sign-Up", "Account creation step before module ranking.", onboarding_signup()),
        showcase("Onboarding · Module Ranking", "Default ranking with reordering before the first assessment begins.", onboarding_ranking()),
        showcase("Settings & Profile", "Account management, preferences, privacy, and tier management.", settings_screen()),
        showcase("What Clients Are Asking · Coming Soon", "v1 placeholder with explanatory content and notification CTA.", coming_soon()),
    ]

    sections = [
        ("Batch A", "Platform overview and My Results surfaces.", batch_a),
        ("Batch B", "Assessment discovery, gateway states, question flow, and flagship results.", batch_b),
        ("Batch C", "Area and BI views.", batch_c),
        ("Batch D", "Entry, settings, and future-state placeholder surfaces.", batch_d),
    ]

    rendered_sections = []
    for name, desc, items in sections:
        rendered_sections.append(
            f"""
            <section class="screen-section">
              <div class="section-header">
                <div>
                  <div class="eyebrow">{name}</div>
                  <h2>{name} screens</h2>
                  <p>{desc}</p>
                </div>
                <div class="count-pill">{len(items)} frames</div>
              </div>
              {''.join(items)}
            </section>
            """
        )

    body = [
        cover(
            "Point93 / Screens",
            "Cleaned Point93 MVP screen set rebuilt as separate native desktop frames. These frames preserve the original IA and state model while stripping import chrome and reducing clipping risk.",
            [
                "Desktop-first 1440px frames",
                "220px sidebar + 32px content padding",
                "23 MVP states rebuilt in batches",
            ],
        ),
        "".join(rendered_sections),
    ]
    return document("Point93 / Screens", "".join(body))


def write_outputs() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    outputs = {
        "point93-reference.html": reference_page(),
        "point93-foundations.html": foundations_page(),
        "point93-components.html": components_page(),
        "point93-screens.html": screens_page(),
    }
    for name, contents in outputs.items():
        (OUT_DIR / name).write_text(contents)
        print(f"Wrote figma_exports/{name}")


if __name__ == "__main__":
    write_outputs()
