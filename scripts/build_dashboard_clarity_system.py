from __future__ import annotations

from textwrap import dedent

from build_point93_figma_pages import OUT_DIR


CSS = """
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/3exmuO07FP19gMM08TQrpXl3BGQ.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/HJY4SY2JywrSZ2l1AEW9Tm9cO8.woff2") format("woff2"); font-weight: 500; }
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/hG3wmGmFwadB6X5XPVXkMlmLr8o.woff2") format("woff2"); font-weight: 600; }

:root {
  --canvas-top: #bcd2ea;
  --canvas-bottom: #efe3d6;
  --shell: rgba(255,255,255,0.92);
  --panel: rgba(255,255,255,0.96);
  --panel-soft: #f7f2ea;
  --line: #e9e1d8;
  --line-soft: rgba(32,29,26,0.08);
  --ink: #1f1b19;
  --copy: #5d5750;
  --muted: #81796f;
  --action: #121110;
  --sky: #9ebde2;
  --sky-soft: #dbe7f4;
  --sand: #f0e4d8;
  --moss: #7d9160;
  --amber: #c59a52;
  --rose: #bf6c55;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  color: var(--copy);
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: linear-gradient(180deg, var(--canvas-top) 0%, #e8eef5 32%, #f7f2ec 68%, var(--canvas-bottom) 100%);
}

.capture-root { width: 1920px; padding: 56px 72px 96px; }
.board {
  border-radius: 34px;
  border: 3px solid rgba(255,255,255,0.92);
  overflow: hidden;
  box-shadow: 0 30px 72px rgba(39, 32, 28, 0.10);
  background: linear-gradient(180deg, rgba(158,189,226,0.38) 0%, rgba(255,255,255,0.28) 18%, rgba(247,242,234,0.68) 100%);
}

.cover, .section {
  margin: 24px;
  padding: 28px;
  border-radius: 28px;
  border: 1px solid rgba(255,255,255,0.78);
  background: var(--shell);
  box-shadow: 0 16px 34px rgba(39, 32, 28, 0.06);
}

.eyebrow, .token-name, .component-name, .meta {
  color: var(--muted);
  font: 600 11px/1.2 "Open Runde", Inter, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

h1, h2, h3, h4, .brand {
  color: var(--ink);
  font-family: "Saans TRIAL", "Open Runde", Inter, sans-serif;
}

h1 {
  max-width: 1120px;
  margin: 0 0 12px;
  font-size: 42px;
  line-height: 1.02;
  letter-spacing: -0.05em;
}

h2 {
  margin: 0 0 6px;
  font-size: 28px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

h3 {
  margin: 0 0 8px;
  font-size: 18px;
  line-height: 1.18;
}

p {
  margin: 0;
  color: var(--copy);
  font-size: 13px;
  line-height: 1.68;
}

.chips, .section-head, .pill-row, .header-bar, .row-between {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.chips { margin-top: 18px; }

.chip, .pill, .tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.72);
  color: var(--copy);
  font-size: 11px;
  font-weight: 600;
}

.pill.dark {
  background: var(--action);
  border-color: var(--action);
  color: #fff;
}

.section-head {
  justify-content: space-between;
  align-items: end;
  margin-bottom: 18px;
}

.grid-2, .grid-3, .grid-4, .mini-grid, .component-grid {
  display: grid;
  gap: 14px;
}

.grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.mini-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.component-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }

.card, .swatch, .type-card, .token-card, .component-card {
  padding: 18px;
  border-radius: 22px;
  border: 1px solid var(--line);
  background: var(--panel);
  box-shadow: 0 10px 22px rgba(39, 32, 28, 0.04);
}

.card.soft, .component-preview.soft {
  background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(247,242,234,0.86));
}

.swatch {
  padding: 0;
  overflow: hidden;
}

.swatch-color { height: 66px; }
.swatch-copy { padding: 14px; }
.swatch-copy span {
  display: block;
  color: var(--muted);
  font-size: 11px;
  line-height: 1.45;
}

.type-sample {
  color: var(--ink);
  font-family: "Saans TRIAL", "Open Runde", Inter, sans-serif;
  letter-spacing: -0.035em;
}

.type-display { font-size: 44px; line-height: 1.02; }
.type-title { font-size: 30px; line-height: 1.06; }
.type-card-title { font-size: 18px; line-height: 1.18; }
.type-body { font: 14px/1.65 Inter, sans-serif; letter-spacing: 0; }
.type-meta { font: 600 12px/1.25 Inter, sans-serif; letter-spacing: 0; }

.token-table {
  display: grid;
  grid-template-columns: 1.35fr 0.75fr 1.35fr;
  gap: 1px;
  overflow: hidden;
  border-radius: 18px;
  background: var(--line-soft);
}

.cell {
  padding: 12px;
  background: rgba(255,255,255,0.96);
  font-size: 12px;
}

.cell.head {
  color: var(--muted);
  font: 600 11px/1.2 "Open Runde", Inter, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.component-name { margin-bottom: 10px; }
.component-preview {
  border-radius: 24px;
  border: 1px solid var(--line);
  overflow: hidden;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(247,242,234,0.90));
}

.stage-preview {
  padding: 18px;
  background: linear-gradient(180deg, rgba(158,189,226,0.30), rgba(255,255,255,0.24) 22%, rgba(247,242,234,0.66) 100%);
}

.app-shell {
  border-radius: 24px;
  border: 2px solid rgba(255,255,255,0.92);
  background: rgba(255,255,255,0.78);
  box-shadow: 0 12px 28px rgba(39, 32, 28, 0.06);
  padding: 14px;
}

.dashboard-layout {
  display: grid;
  grid-template-columns: 170px 1fr;
  gap: 14px;
}

.sidebar {
  padding: 14px;
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(247,242,234,0.84));
  border: 1px solid var(--line);
}

.brand {
  margin-bottom: 12px;
  font-size: 14px;
  font-weight: 600;
}

.nav-item {
  padding: 10px 12px;
  border-radius: 14px;
  font-size: 12px;
}

.nav-item.active { background: rgba(16,17,16,0.05); color: var(--ink); }

.surface {
  padding: 14px;
  border-radius: 20px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.92);
}

.search {
  min-width: 160px;
  padding: 10px 12px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.86);
  color: var(--muted);
  font-size: 12px;
}

.metric-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}

.metric-card {
  padding: 16px;
  border-radius: 18px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.94);
}

.metric-label {
  margin-bottom: 14px;
  color: var(--copy);
  font-size: 11px;
  font-weight: 600;
}

.metric-value {
  color: var(--ink);
  font: 600 22px/1 "Saans TRIAL", "Open Runde", Inter, sans-serif;
  letter-spacing: -0.03em;
}

.metric-delta {
  font-size: 11px;
  font-weight: 600;
}

.metric-delta.good { color: var(--moss); }
.metric-delta.warn { color: var(--rose); }

.chart-shell, .table-shell, .budget-shell {
  padding: 18px;
  border-radius: 20px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.95);
}

.chart-area {
  height: 148px;
  margin-top: 12px;
  border-radius: 14px;
  background:
    linear-gradient(180deg, rgba(158,189,226,0.14), rgba(158,189,226,0.04)),
    repeating-linear-gradient(180deg, transparent 0, transparent 27px, rgba(32,29,26,0.05) 27px, rgba(32,29,26,0.05) 28px);
  position: relative;
  overflow: hidden;
}

.bar {
  position: absolute;
  bottom: 0;
  width: 34px;
  border-radius: 10px 10px 0 0;
  background: linear-gradient(180deg, rgba(158,189,226,0.88), rgba(158,189,226,0.42));
}

.line {
  position: absolute;
  left: 12px;
  right: 12px;
  top: 76px;
  height: 2px;
  background: linear-gradient(90deg, rgba(125,145,96,0.12), rgba(125,145,96,0.78));
}

.table-row {
  display: grid;
  grid-template-columns: 1.4fr 0.9fr 0.9fr 0.9fr;
  gap: 10px;
  align-items: center;
  padding: 14px 0;
  border-top: 1px solid var(--line);
  font-size: 12px;
}

.priority {
  display: inline-flex;
  align-items: center;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  background: rgba(125,145,96,0.12);
  color: var(--moss);
}

.priority.medium {
  background: rgba(197,154,82,0.14);
  color: #9f7a40;
}

.priority.low {
  background: rgba(191,108,85,0.12);
  color: var(--rose);
}

.stack {
  display: inline-flex;
  align-items: center;
}

.avatar {
  width: 22px;
  height: 22px;
  margin-left: -6px;
  border-radius: 999px;
  border: 2px solid #fff;
  background: linear-gradient(180deg, #c9aa86, #7f5d44);
}

.button-dark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 14px;
  border-radius: 999px;
  background: var(--action);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
}

.button-soft {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 14px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.9);
  color: var(--copy);
  font-size: 12px;
  font-weight: 600;
}

.insight {
  padding: 16px;
  border-radius: 18px;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(247,242,234,0.94), rgba(255,255,255,0.98));
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
          <title>Point93 Quiet Clarity Foundations and Components</title>
          <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
          <style>{CSS}</style>
        </head>
        <body>
          <div class="capture-root">{body}</div>
        </body>
        </html>
        """
    )


def page() -> str:
    return document(
        dedent(
            """\
            <div class="board">
              <div class="cover">
                <div class="eyebrow">Point93 quiet clarity system</div>
                <h1>The stronger luxury move is restraint: simpler cards, calmer type, and less visual talking.</h1>
                <p>The newer references are valuable because they remove visual negotiation. Cards do one job. Headers are short and quiet. Color is structural instead of decorative. Type creates hierarchy without shouting. For Point93, that means we should keep the premium poise from Dreelio, but dial down the atmosphere and let spacing, typography, and single-purpose surfaces carry the experience.</p>
                <div class="chips">
                  <div class="chip">Type leads, not effects</div>
                  <div class="chip">One card, one job</div>
                  <div class="chip">Color only for status and action</div>
                  <div class="chip">Quiet borders, not loud shells</div>
                  <div class="chip">Soft canvas, plain surfaces</div>
                  <div class="chip">Reduce decisions per row</div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">Language principles</div>
                    <h2>What to keep and what to dial down</h2>
                  </div>
                  <div class="pill">Simpler than the Dreelio pass</div>
                </div>
                <div class="grid-3">
                  <div class="card"><h3>Keep the calm stage</h3><p>A soft sky-to-sand canvas still helps the product feel elevated, but it should sit behind the interface. The cards themselves stay plain, bright, and easy to parse.</p></div>
                  <div class="card"><h3>Let type do more work</h3><p>Use a more branded headline voice, but keep sizes disciplined. Clear typography should replace decorative hero treatments and heavy label chrome.</p></div>
                  <div class="card"><h3>Reduce component personality</h3><p>Not every card needs its own style. Metric cards, chart cards, and table cards should feel like siblings with one visual grammar.</p></div>
                  <div class="card"><h3>Use color with intent</h3><p>Black anchors action. Sky tints support the stage. Green, amber, and rose only appear when they signal status, movement, or priority.</p></div>
                  <div class="card"><h3>Keep rows easier to scan</h3><p>Rows should have fewer badges, fewer competing alignments, and wider breathing room. The user should understand a surface in one pass.</p></div>
                  <div class="card"><h3>Premium through composure</h3><p>For this audience, the luxurious signal is confidence and editorial restraint, not more layers, glass, or flourish.</p></div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">p93-calm/*</div>
                    <h2>Revised token system</h2>
                  </div>
                  <div class="pill">Fewer tokens, clearer jobs</div>
                </div>

                <div class="grid-4" style="margin-bottom:14px;">
                  <div class="swatch"><div class="swatch-color" style="background:#bcd2ea;"></div><div class="swatch-copy"><strong>p93-calm/color/canvas/top</strong><span>#bcd2ea</span><span>Soft atmospheric stage</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#efe3d6;"></div><div class="swatch-copy"><strong>p93-calm/color/canvas/bottom</strong><span>#efe3d6</span><span>Warm lower wash</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#ffffff;"></div><div class="swatch-copy"><strong>p93-calm/color/surface/base</strong><span>#ffffff</span><span>Primary card and table surface</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#f7f2ea;"></div><div class="swatch-copy"><strong>p93-calm/color/surface/soft</strong><span>#f7f2ea</span><span>Subtle alternate fill</span></div></div>
                </div>

                <div class="grid-4" style="margin-bottom:18px;">
                  <div class="swatch"><div class="swatch-color" style="background:#e9e1d8;"></div><div class="swatch-copy"><strong>p93-calm/color/line/default</strong><span>#e9e1d8</span><span>Hairline borders only</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#1f1b19;"></div><div class="swatch-copy"><strong>p93-calm/color/text/strong</strong><span>#1f1b19</span><span>Headlines and anchors</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#5d5750;"></div><div class="swatch-copy"><strong>p93-calm/color/text/default</strong><span>#5d5750</span><span>Primary copy</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#121110;"></div><div class="swatch-copy"><strong>p93-calm/color/action/primary</strong><span>#121110</span><span>Near-black CTA</span></div></div>
                </div>

                <div class="grid-4" style="margin-bottom:18px;">
                  <div class="swatch"><div class="swatch-color" style="background:#9ebde2;"></div><div class="swatch-copy"><strong>p93-calm/color/accent/sky</strong><span>#9ebde2</span><span>Stage and chart tint</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#7d9160;"></div><div class="swatch-copy"><strong>p93-calm/color/status/positive</strong><span>#7d9160</span><span>Healthy movement</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#c59a52;"></div><div class="swatch-copy"><strong>p93-calm/color/status/warning</strong><span>#c59a52</span><span>Moderate caution</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#bf6c55;"></div><div class="swatch-copy"><strong>p93-calm/color/status/risk</strong><span>#bf6c55</span><span>Needs attention</span></div></div>
                </div>

                <div class="mini-grid" style="margin-bottom:18px;">
                  <div class="type-card">
                    <div class="eyebrow">p93-calm/type/*</div>
                    <div class="type-sample type-display">Quiet display</div>
                    <div class="type-sample type-title">Page title</div>
                    <div class="type-sample type-card-title">Card title</div>
                    <div class="type-sample type-body">Body copy should stay plain, readable, and slightly generous in line height.</div>
                    <div class="type-sample type-meta" style="margin-top:8px;">Meta labels should feel quiet, not branded.</div>
                  </div>
                  <div class="type-card">
                    <div class="eyebrow">Scale and rhythm</div>
                    <div class="token-table">
                      <div class="cell head">Token</div><div class="cell head">Value</div><div class="cell head">Use</div>
                      <div class="cell">p93-calm/type/display</div><div class="cell">42 / 1.02</div><div class="cell">Single hero moment only</div>
                      <div class="cell">p93-calm/type/title</div><div class="cell">30 / 1.06</div><div class="cell">Page titles</div>
                      <div class="cell">p93-calm/type/card-title</div><div class="cell">18 / 1.18</div><div class="cell">Card headers and table sections</div>
                      <div class="cell">p93-calm/type/body</div><div class="cell">14 / 1.65</div><div class="cell">Primary copy</div>
                      <div class="cell">p93-calm/type/meta</div><div class="cell">12 / 1.25</div><div class="cell">Labels and support text</div>
                    </div>
                  </div>
                </div>

                <div class="token-table">
                  <div class="cell head">Token</div><div class="cell head">Value</div><div class="cell head">Use</div>
                  <div class="cell">p93-calm/space/xs</div><div class="cell">8</div><div class="cell">Compact status and chip spacing</div>
                  <div class="cell">p93-calm/space/sm</div><div class="cell">12</div><div class="cell">Dense card internals</div>
                  <div class="cell">p93-calm/space/md</div><div class="cell">16</div><div class="cell">Default card and row padding</div>
                  <div class="cell">p93-calm/space/lg</div><div class="cell">24</div><div class="cell">Major sections and panels</div>
                  <div class="cell">p93-calm/space/xl</div><div class="cell">32</div><div class="cell">Page gutters and shell spacing</div>
                  <div class="cell">p93-calm/radius/input</div><div class="cell">14</div><div class="cell">Inputs and pills</div>
                  <div class="cell">p93-calm/radius/card</div><div class="cell">18</div><div class="cell">Metric cards and utility panels</div>
                  <div class="cell">p93-calm/radius/surface</div><div class="cell">20</div><div class="cell">Charts, tables, and major content blocks</div>
                  <div class="cell">p93-calm/radius/shell</div><div class="cell">24</div><div class="cell">App shell and staged previews</div>
                  <div class="cell">p93-calm/stroke/hairline</div><div class="cell">1</div><div class="cell">Default border weight everywhere</div>
                  <div class="cell">p93-calm/shadow/lift</div><div class="cell">0 10 22 / 4%</div><div class="cell">Subtle lift only, never dramatic glass</div>
                  <div class="cell">p93-calm/motion/settle</div><div class="cell">180-240ms</div><div class="cell">Short, confident movement</div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">P93-Calm/*</div>
                    <h2>Component library</h2>
                  </div>
                  <div class="pill dark">Build from quiet surfaces</div>
                </div>

                <div class="component-grid">
                  <div class="component-card">
                    <div class="component-name">P93-Calm/Shell/AppStage</div>
                    <div class="component-preview stage-preview">
                      <div class="app-shell">
                        <div class="dashboard-layout">
                          <div class="sidebar">
                            <div class="brand">Point93</div>
                            <div class="nav-item active">Dashboard</div>
                            <div class="nav-item">My Results</div>
                            <div class="nav-item">Assessments</div>
                            <div class="nav-item">Business Intelligence</div>
                          </div>
                          <div class="surface">
                            <div class="header-bar" style="justify-content:space-between;align-items:center;">
                              <div>
                                <div class="meta" style="margin-bottom:4px;">Hello, Adam</div>
                                <h3>Today’s financial clarity</h3>
                              </div>
                              <div class="search">Search</div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Soft app shell with clean internal surfaces. The stage is present, but not busy.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Header/PageHeader</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="row-between" style="justify-content:space-between;align-items:center;">
                        <div>
                          <div class="meta" style="margin-bottom:6px;">Dashboard</div>
                          <h3 style="margin-bottom:4px;">A clear picture of your positioning</h3>
                          <p>One sentence of guidance, not three.</p>
                        </div>
                        <div class="pill dark">Continue assessment</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Short title, short explanation, one action. This replaces heavier hero treatments.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Control/SearchFilterRow</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="header-bar" style="justify-content:space-between;">
                        <div class="search" style="min-width:200px;">Find an assessment...</div>
                        <div class="pill">Filter</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Utility rows should be plain and spacious so they disappear into the workflow.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Card/Metric</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="metric-card">
                        <div class="metric-label">Overall P93 Score</div>
                        <div class="row-between" style="justify-content:space-between;align-items:end;">
                          <div class="metric-value">74</div>
                          <div class="metric-delta good">+8.4%</div>
                        </div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Simple metrics use one value, one label, one status cue.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Card/ChartPanel</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="chart-shell">
                        <div class="row-between" style="justify-content:space-between;align-items:center;">
                          <strong style="color:var(--ink);">Earning over time</strong>
                          <div class="pill">Month</div>
                        </div>
                        <div class="chart-area">
                          <div class="line"></div>
                          <div class="bar" style="left:14px;height:74px;"></div>
                          <div class="bar" style="left:56px;height:122px;"></div>
                          <div class="bar" style="left:98px;height:84px;"></div>
                          <div class="bar" style="left:140px;height:96px;"></div>
                          <div class="bar" style="left:182px;height:62px;"></div>
                          <div class="bar" style="left:224px;height:115px;"></div>
                        </div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Charts should feel explanatory, not ornamental. Keep surrounding chrome minimal.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Card/WorklistTable</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="table-shell">
                        <div class="row-between" style="justify-content:space-between;align-items:center;">
                          <strong style="color:var(--ink);">Projects</strong>
                          <div class="tag">Ongoing 5</div>
                        </div>
                        <div class="table-row">
                          <div>Estate readiness review</div><div class="priority">High</div><div>Broker team</div><div class="stack"><div class="avatar"></div><div class="avatar"></div><div class="avatar"></div></div>
                        </div>
                        <div class="table-row">
                          <div>Tax positioning workshop</div><div class="priority medium">Medium</div><div>Planner</div><div class="stack"><div class="avatar"></div><div class="avatar"></div></div>
                        </div>
                        <div class="table-row">
                          <div>Liquidity scenario prep</div><div class="priority low">Low</div><div>Client</div><div class="stack"><div class="avatar"></div></div>
                        </div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Tables should feel quieter and more legible than card grids when density rises.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Card/BudgetInsight</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="budget-shell">
                        <h3 style="margin-bottom:14px;">Project budget</h3>
                        <div class="grid-2" style="gap:12px;margin-bottom:14px;">
                          <div class="insight"><div class="metric-value" style="font-size:18px;">$18,090</div><p>Billable total</p></div>
                          <div class="insight"><div class="metric-value" style="font-size:18px;">89.3</div><p>Margin</p></div>
                        </div>
                        <div class="chart-area" style="height:124px;"></div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Summary and analytics can coexist when each layer stays quiet and evenly spaced.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Status/PriorityChip</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="pill-row">
                        <div class="priority">High</div>
                        <div class="priority medium">Medium</div>
                        <div class="priority low">Low</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Status chips are compact and secondary. They support scanability without taking over the row.</p>
                  </div>

                  <div class="component-card">
                    <div class="component-name">P93-Calm/Action/PrimaryButton</div>
                    <div class="component-preview soft" style="padding:18px;">
                      <div class="pill-row">
                        <div class="button-dark">Continue assessment</div>
                        <div class="button-soft">View details</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">The near-black button becomes the main premium anchor throughout the product.</p>
                  </div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">Applied pattern</div>
                    <h2>How this should change Point93 screens</h2>
                  </div>
                  <div class="pill">Lower cognitive load</div>
                </div>
                <div class="grid-3">
                  <div class="card"><h3>Dashboard</h3><p>Fewer bespoke card treatments. Use one page header, a metric strip, one chart surface, and one worklist/table surface.</p></div>
                  <div class="card"><h3>My Results</h3><p>Move away from decorative insight cards and use simple ranked sections, quiet comparisons, and clearer action framing.</p></div>
                  <div class="card"><h3>Assessments</h3><p>Keep progress and completion states highly legible with more whitespace and fewer tertiary chips competing with the next action.</p></div>
                </div>
              </div>
            </div>
            """
        )
    )


def write_outputs() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / "dashboard-clarity-system.html"
    path.write_text(page())
    print(f"Wrote {path.relative_to(OUT_DIR.parent)}")


if __name__ == "__main__":
    write_outputs()
