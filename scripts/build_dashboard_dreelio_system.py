from __future__ import annotations

from textwrap import dedent

from build_point93_figma_pages import OUT_DIR


CSS = """
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/3exmuO07FP19gMM08TQrpXl3BGQ.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/HJY4SY2JywrSZ2l1AEW9Tm9cO8.woff2") format("woff2"); font-weight: 500; }
@font-face { font-family: "Open Runde"; src: url("https://framerusercontent.com/assets/hG3wmGmFwadB6X5XPVXkMlmLr8o.woff2") format("woff2"); font-weight: 600; }

:root {
  --sky-500: #84b9ef;
  --sky-200: #d7e7f8;
  --sand-300: #f4e6da;
  --vellum-300: #f4f1ee;
  --paper-0: rgba(255,255,255,0.74);
  --paper-strong: rgba(255,255,255,0.92);
  --ink-900: #1a1615;
  --text-700: #453f3d;
  --text-500: #757170;
  --line-200: rgba(69,63,61,0.10);
  --gold-500: #cf8d13;
  --navy-950: #141311;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  color: var(--text-700);
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at top center, rgba(255,255,255,0.45), transparent 24%),
    radial-gradient(circle at 15% 12%, rgba(255,255,255,0.22), transparent 16%),
    radial-gradient(circle at 85% 14%, rgba(255,255,255,0.22), transparent 16%),
    linear-gradient(180deg, #a7c9ef 0%, #dbe9f8 40%, #efe8df 72%, #f4e6da 100%);
}

.capture-root { width: 1920px; padding: 56px 72px 92px; }
.board {
  border-radius: 38px;
  border: 5px solid rgba(255,255,255,0.95);
  overflow: hidden;
  box-shadow: 0 40px 90px rgba(41, 33, 29, 0.12);
  background:
    radial-gradient(circle at top center, rgba(255,255,255,0.42), transparent 22%),
    linear-gradient(180deg, rgba(141,186,233,0.95) 0%, rgba(214,231,248,0.94) 28%, rgba(247,242,236,0.94) 100%);
}

.section, .cover {
  margin: 28px;
  padding: 28px;
  border-radius: 30px;
  background: rgba(255,255,255,0.60);
  border: 1px solid rgba(255,255,255,0.78);
  box-shadow: 0 24px 50px rgba(41, 33, 29, 0.10);
  backdrop-filter: blur(18px);
}

.cover { margin-bottom: 22px; }
.eyebrow, .token-name, .component-name, .meta {
  color: rgba(69,63,61,0.62);
  font: 600 11px/1.2 "Open Runde", Inter, sans-serif;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

h1, h2, h3, h4, strong, .brand { color: var(--ink-900); font-family: "Open Runde", "Saans TRIAL", "Helvetica Neue", Inter, sans-serif; }
h1 { max-width: 1120px; margin: 0 0 12px; font-size: 46px; line-height: 1.02; letter-spacing: -0.055em; }
h2 { margin: 0 0 6px; font-size: 28px; line-height: 1.05; letter-spacing: -0.04em; }
h3 { margin: 0 0 10px; font-size: 18px; line-height: 1.12; }
p { margin: 0; color: var(--text-500); font-size: 13px; line-height: 1.72; }

.chips, .section-head, .pill-row, .status-row, .utility-right { display: flex; flex-wrap: wrap; gap: 10px; }
.chips { margin-top: 20px; }

.chip, .pill, .status {
  padding: 9px 13px;
  border-radius: 999px;
  background: rgba(255,255,255,0.64);
  border: 1px solid rgba(255,255,255,0.78);
  font-size: 11px;
  font-weight: 600;
}

.section-head { justify-content: space-between; align-items: end; margin-bottom: 18px; }
.grid-3, .grid-4, .grid-5, .comp-grid, .mini-grid { display: grid; gap: 12px; }
.grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }
.mini-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.comp-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }

.card, .swatch, .type-card, .mini-card, .comp-card {
  padding: 18px;
  border-radius: 22px;
  background: rgba(255,255,255,0.62);
  border: 1px solid rgba(255,255,255,0.78);
  box-shadow: 0 18px 34px rgba(41, 33, 29, 0.08);
}

.swatch { padding: 0; overflow: hidden; }
.swatch-color { height: 64px; }
.swatch-copy { padding: 14px; }
.swatch-copy span { display: block; color: var(--text-500); font-size: 11px; line-height: 1.45; }

.type-sample { color: var(--ink-900); font-family: "Open Runde", Inter, sans-serif; letter-spacing: -0.03em; }
.type-display { font-size: 56px; line-height: 0.98; }
.type-title { font-size: 42px; line-height: 1.02; }
.type-section { font-size: 24px; line-height: 1.06; }
.type-body { font: 13px/1.72 Inter, sans-serif; }
.type-meta { font: 600 11px/1.2 "Open Runde", Inter, sans-serif; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(69,63,61,0.62); }

.shape {
  display: flex; align-items: center; justify-content: center; color: rgba(69,63,61,0.7); font-size: 11px; font-weight: 600;
  background: linear-gradient(180deg, rgba(255,255,255,0.88), rgba(247,242,236,0.84));
  border: 1px solid rgba(255,255,255,0.78);
  box-shadow: 0 18px 34px rgba(41, 33, 29, 0.08);
}

.r14 { height: 56px; border-radius: 14px; }
.r18 { height: 72px; border-radius: 18px; }
.r24 { height: 88px; border-radius: 24px; }
.r28 { height: 104px; border-radius: 28px; }
.r38 { height: 120px; border-radius: 38px; }

.comp-name { margin-bottom: 10px; }
.comp-preview {
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,0.78);
  overflow: hidden;
  background: linear-gradient(180deg, rgba(255,255,255,0.80), rgba(247,242,236,0.84));
}

.pillbar {
  display: flex; align-items: center; gap: 12px; padding: 10px 14px;
  border-radius: 999px; background: rgba(255,255,255,0.46); border: 1px solid rgba(255,255,255,0.74);
}

.brand { font-size: 14px; font-weight: 600; }
.cta-dark, .btn-dark {
  display: inline-flex; align-items: center; justify-content: center; padding: 10px 14px;
  border-radius: 999px; background: var(--navy-950); color: white; font-size: 12px; font-weight: 600;
}

.side-shell {
  padding: 14px; border-radius: 24px; background: linear-gradient(180deg, rgba(247,241,233,0.96), rgba(242,236,230,0.90));
}

.side-item { padding: 10px 12px; border-radius: 14px; font-size: 12px; }
.side-item.active { background: rgba(255,255,255,0.56); }

.hero {
  padding: 18px;
  border-radius: 24px;
  background: radial-gradient(circle at top left, rgba(255,255,255,0.42), transparent 24%), linear-gradient(180deg, rgba(169,202,238,0.86), rgba(223,236,248,0.72));
}

.metric-card, .verdict-card, .module-card, .utility-card {
  padding: 18px; border-radius: 22px;
}

.metric-card, .module-card, .utility-card {
  background: rgba(255,255,255,0.72); border: 1px solid rgba(255,255,255,0.78);
}

.verdict-card {
  color: rgba(255,255,255,0.88);
  background: linear-gradient(180deg, rgba(28,31,36,0.98), rgba(40,48,60,0.96));
  border: 1px solid rgba(255,255,255,0.10);
}

.ring {
  width: 64px; height: 64px; border-radius: 999px; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(245,238,230,0.92)); border: 2px solid rgba(255,255,255,0.76);
  color: var(--ink-900); font: 600 24px/1 "Open Runde", Inter, sans-serif;
}

.token-table { display: grid; grid-template-columns: 1.25fr 0.7fr 1.45fr; gap: 1px; border-radius: 18px; overflow: hidden; background: rgba(69,63,61,0.08); }
.cell { padding: 12px; background: rgba(255,255,255,0.74); font-size: 12px; }
.cell.head { font: 600 11px/1.2 "Open Runde", Inter, sans-serif; letter-spacing: 0.16em; text-transform: uppercase; color: rgba(69,63,61,0.62); }
"""


def document(body: str) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Point93 Luxury Foundations and Components</title>
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
                <div class="eyebrow">Point93 luxury system</div>
                <h1>Dreelio gave us the shell language. Point93 turns it into a premium advisory system.</h1>
                <p>The new language is not "blue gradients" or "soft glass" by itself. The real shift is structural: atmosphere replaces decorative polish, containment is handled by thick shells and translucent pills instead of hard cards, headlines feel rounded and editorial, and dark anchors create confidence inside a mostly light field. For Point93, that means the product can feel more expensive without feeling fashion-driven.</p>
                <div class="chips">
                  <div class="chip">Atmosphere before ornament</div>
                  <div class="chip">Soft containment over hard chrome</div>
                  <div class="chip">Rounded editorial clarity</div>
                  <div class="chip">Dark anchors in a light field</div>
                  <div class="chip">Gold used selectively, never broadly</div>
                  <div class="chip">Roomier hierarchy and lower friction</div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">Language principles</div>
                    <h2>What changed from the earlier Point93 pass</h2>
                  </div>
                  <div class="pill">Translate, do not imitate</div>
                </div>
                <div class="grid-3">
                  <div class="card"><h3>Atmosphere Before Ornament</h3><p>The interface feels premium because the whole stage has climate and air. We use a sky-to-vellum field, soft mist, and framed shells instead of relying on decorative patterns or loud gradients inside every card.</p></div>
                  <div class="card"><h3>Soft Containment</h3><p>Panels no longer need heavy outlines to feel separate. Thick white shells, translucent pills, and low-contrast card borders make the product feel more frictionless and modern.</p></div>
                  <div class="card"><h3>Rounded Editorial Clarity</h3><p>Headlines feel more human and more designed through a rounded grotesk voice. Body copy stays pragmatic, but key moments feel more intentional and less enterprise-generic.</p></div>
                  <div class="card"><h3>Dark Anchors</h3><p>Near-black buttons and dark insight surfaces create trust and seriousness. They keep the system from drifting into playful startup softness.</p></div>
                  <div class="card"><h3>Selective Prestige</h3><p>Gold is a precision accent, not a theme. It appears in score chips, emphasis moments, and subtle hierarchy markers, which keeps the product feeling expensive rather than gaudy.</p></div>
                  <div class="card"><h3>Fast Through Calm</h3><p>Utility actions become pills, card spacing gets roomier, and micro-content is quieter. The product feels easier and faster because the interface argues with the user less.</p></div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">p93-lux/color/*</div>
                    <h2>Token system</h2>
                  </div>
                  <div class="pill">New luxury namespace</div>
                </div>
                <div class="grid-5" style="margin-bottom:12px;">
                  <div class="swatch"><div class="swatch-color" style="background:#84b9ef;"></div><div class="swatch-copy"><strong>p93-lux/color/sky/500</strong><span>#84b9ef</span><span>Primary atmosphere</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#d7e7f8;"></div><div class="swatch-copy"><strong>p93-lux/color/sky/200</strong><span>#d7e7f8</span><span>Soft hero wash</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#f4e6da;"></div><div class="swatch-copy"><strong>p93-lux/color/sand/300</strong><span>#f4e6da</span><span>Warm lower glow</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#f4f1ee;"></div><div class="swatch-copy"><strong>p93-lux/color/vellum/300</strong><span>#f4f1ee</span><span>Shell and panel base</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#1a1615;"></div><div class="swatch-copy"><strong>p93-lux/color/ink/900</strong><span>#1a1615</span><span>Display and CTA anchor</span></div></div>
                </div>
                <div class="grid-5" style="margin-bottom:20px;">
                  <div class="swatch"><div class="swatch-color" style="background:#453f3d;"></div><div class="swatch-copy"><strong>p93-lux/color/text/700</strong><span>#453f3d</span><span>Primary copy</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#757170;"></div><div class="swatch-copy"><strong>p93-lux/color/text/500</strong><span>#757170</span><span>Quiet support copy</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#ffffff;"></div><div class="swatch-copy"><strong>p93-lux/color/paper/0</strong><span>rgba(255,255,255,0.74)</span><span>Default card fill</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#ffffff;"></div><div class="swatch-copy"><strong>p93-lux/color/paper/strong</strong><span>rgba(255,255,255,0.92)</span><span>Primary shell surface</span></div></div>
                  <div class="swatch"><div class="swatch-color" style="background:#cf8d13;"></div><div class="swatch-copy"><strong>p93-lux/color/gold/500</strong><span>#cf8d13</span><span>Selective prestige accent</span></div></div>
                </div>

                <div class="mini-grid" style="margin-bottom:20px;">
                  <div class="type-card">
                    <div class="eyebrow">p93-lux/type/*</div>
                    <div class="type-sample type-display">Display</div>
                    <div class="type-sample type-title">Dashboard</div>
                    <div class="type-sample type-section">Overall P93 Score</div>
                    <div class="type-meta">Rounded grotesk for all headline moments</div>
                  </div>
                  <div class="type-card">
                    <div class="eyebrow">Type scale</div>
                    <div class="type-sample type-display">56 / 0.98</div>
                    <div class="type-sample type-title">42 / 1.02</div>
                    <div class="type-sample type-section">24 / 1.06</div>
                    <div class="type-sample type-body">13 / 1.72 body and 11 / 1.2 meta</div>
                  </div>
                </div>

                <div class="grid-4" style="margin-bottom:18px;">
                  <div class="mini-card"><div class="eyebrow">p93-lux/radius/pill</div><div class="shape r14">14</div></div>
                  <div class="mini-card"><div class="eyebrow">p93-lux/radius/card-sm</div><div class="shape r18">18</div></div>
                  <div class="mini-card"><div class="eyebrow">p93-lux/radius/card</div><div class="shape r24">24</div></div>
                  <div class="mini-card"><div class="eyebrow">p93-lux/radius/shell</div><div class="shape r28">28</div></div>
                </div>

                <div class="token-table">
                  <div class="cell head">Token</div><div class="cell head">Value</div><div class="cell head">Use</div>
                  <div class="cell">p93-lux/radius/stage</div><div class="cell">38</div><div class="cell">Outer framed atmosphere board</div>
                  <div class="cell">p93-lux/stroke/hairline</div><div class="cell">1</div><div class="cell">Interior pills and cards</div>
                  <div class="cell">p93-lux/stroke/frame</div><div class="cell">5</div><div class="cell">Primary shell border</div>
                  <div class="cell">p93-lux/shadow/float-sm</div><div class="cell">0 18 34 / 8%</div><div class="cell">Cards and controls</div>
                  <div class="cell">p93-lux/shadow/float-lg</div><div class="cell">0 40 90 / 12%</div><div class="cell">Stage and system boards</div>
                  <div class="cell">p93-lux/space/compact</div><div class="cell">12</div><div class="cell">Tight grouped controls</div>
                  <div class="cell">p93-lux/space/default</div><div class="cell">18</div><div class="cell">Card interiors</div>
                  <div class="cell">p93-lux/space/roomy</div><div class="cell">24</div><div class="cell">Major containers and hero cards</div>
                  <div class="cell">p93-lux/motion/fade-rise</div><div class="cell">400-700ms</div><div class="cell">Soft reveal for shell and cards</div>
                </div>
              </div>

              <div class="section">
                <div class="section-head">
                  <div>
                    <div class="eyebrow">P93-Lux/*</div>
                    <h2>Component library</h2>
                  </div>
                  <div class="pill">Build from shell first</div>
                </div>

                <div class="comp-grid">
                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Shell/AtmosphereStage</div>
                    <div class="comp-preview" style="padding:18px;background:linear-gradient(180deg, rgba(141,186,233,0.95), rgba(247,242,236,0.92));">
                      <div class="pillbar">
                        <div class="brand">Point93</div><div>Dashboard</div><div>Results</div><div>Assessments</div><div class="cta-dark">Continue assessment</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">The core premium frame: atmosphere, white shell border, and floating navigation.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Nav/FloatingPillBar</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="pillbar"><div class="brand">Point93</div><div>Dashboard</div><div>Results</div><div>Assessments</div><div class="cta-dark">View tour</div></div>
                    </div>
                    <p style="margin-top:10px;">For top-level navigation or high-level utility context, not for dense in-app routing.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Nav/Sidebar</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="side-shell">
                        <div class="brand" style="margin-bottom:12px;">Point93</div>
                        <div class="side-item active">Dashboard</div>
                        <div class="side-item">My Results</div>
                        <div class="side-item">Assessments</div>
                        <div class="side-item">Business Intelligence</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Still the primary app navigation, but softer and more furniture-like.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Card/HeroBriefing</div>
                    <div class="comp-preview" style="padding:18px;"><div class="hero"><div class="eyebrow" style="margin-bottom:8px;">Layer 1</div><h3 style="margin-bottom:8px;">Welcome back, Adam</h3><p>Curated, atmospheric briefing surface with one primary action.</p><div class="pill-row" style="margin-top:14px;"><div class="btn-dark">Continue assessment</div><div class="pill">View tour</div></div></div></div>
                    <p style="margin-top:10px;">Use for welcome, orientation, or strategic summary moments.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Card/Metric</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="metric-card">
                        <div class="eyebrow" style="margin-bottom:10px;">Progress</div>
                        <div style="display:flex;justify-content:space-between;align-items:center;"><div><h3 style="margin-bottom:6px;">Overall P93 Score</h3><p>83rd percentile among peers</p></div><div class="ring">74</div></div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Metric cards should feel light and quiet, with the number as the anchor.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Card/DarkVerdict</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="verdict-card">
                        <div class="eyebrow" style="margin-bottom:12px;color:rgba(255,255,255,0.6);">Hub verdict</div>
                        <div class="status" style="display:inline-flex;margin-bottom:12px;background:rgba(255,255,255,0.10);color:rgba(255,255,255,0.72);border-color:rgba(255,255,255,0.12);">AI generated</div>
                        <p style="color:rgba(255,255,255,0.84);">Dark anchors are reserved for conviction and intelligence surfaces.</p>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Use sparingly for strategic synthesis, not as a general card style.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Control/UtilityPillGroup</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="utility-card">
                        <div class="pill-row"><div class="pill">Comprehensive tier</div><div class="pill">Concierge view</div><div class="pill">29% complete</div></div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Replaces harder utility rows with quieter, faster controls.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Status/ScoreChip</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="status-row"><div class="status">B · Competitive</div><div class="status gold">5 modules complete</div><div class="status blue">2 BI profiles active</div></div>
                    </div>
                    <p style="margin-top:10px;">Status chips are supportive. They should never become the loudest thing on the screen.</p>
                  </div>

                  <div class="comp-card">
                    <div class="comp-name">P93-Lux/Module/AssessmentCard</div>
                    <div class="comp-preview" style="padding:18px;">
                      <div class="module-card">
                        <strong>FT.2 Technology Capabilities</strong>
                        <p>In Progress · 67% done</p>
                        <div style="margin-top:12px;height:6px;border-radius:999px;background:rgba(20,19,17,0.06);overflow:hidden;"><div style="width:67%;height:100%;background:linear-gradient(90deg,#89bced,#c0d9f2);"></div></div>
                        <div class="btn-dark" style="margin-top:14px;">Continue assessment</div>
                      </div>
                    </div>
                    <p style="margin-top:10px;">Assessment cards stay practical, but inherit the softer shell and type language.</p>
                  </div>
                </div>
              </div>
            </div>
            """
        )
    )


def write_outputs() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    path = OUT_DIR / "dashboard-dreelio-system.html"
    path.write_text(page())
    print(f"Wrote {path.relative_to(OUT_DIR.parent)}")


if __name__ == "__main__":
    write_outputs()
