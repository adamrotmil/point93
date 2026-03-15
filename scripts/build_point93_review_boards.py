from __future__ import annotations

from textwrap import dedent

from build_point93_figma_pages import (
    BASE_CSS,
    OUT_DIR,
    assessment_question,
    assessments_landing,
    bi_product,
    coming_soon,
    cover,
    dashboard_screen,
    module_results,
    my_results_overview,
    settings_screen,
)


REVIEW_CSS = """
body.review-body {
  background:
    radial-gradient(circle at top left, rgba(140, 106, 58, 0.10), transparent 24%),
    linear-gradient(180deg, #f7f4ef 0%, #eef2f7 100%);
}

.review-root {
  width: 1920px;
  padding: 56px 72px 120px;
}

.review-stack {
  display: flex;
  flex-direction: column;
  gap: 42px;
}

.intro-grid,
.principles-grid,
.utility-grid {
  display: grid;
  gap: 16px;
}

.intro-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.principles-grid {
  grid-template-columns: repeat(5, minmax(0, 1fr));
}

.utility-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.review-card,
.principle-card,
.utility-card,
.direction-card,
.reference-card {
  border: 1px solid rgba(209, 213, 222, 0.9);
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.96);
  box-shadow: 0 14px 28px rgba(17, 24, 39, 0.08);
}

.review-card,
.principle-card,
.utility-card,
.reference-card {
  padding: 20px;
}

.review-card h3,
.principle-card h3,
.utility-card h3,
.direction-card h3,
.reference-card h3 {
  margin: 0 0 8px;
  font-size: 18px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.review-card p,
.principle-card p,
.utility-card p,
.direction-card p,
.reference-card p,
.direction-body li,
.direction-panel li {
  margin: 0;
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1.65;
}

.review-section {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.review-section-header {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 20px;
}

.review-section-header h2 {
  margin: 0 0 6px;
  font-size: 30px;
  line-height: 1.08;
  letter-spacing: -0.03em;
}

.review-section-header p {
  max-width: 980px;
  margin: 0;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.7;
}

.annotation-board {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.annotated-screen {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.annotated-meta h3 {
  margin: 0 0 4px;
  font-size: 22px;
  line-height: 1.1;
  letter-spacing: -0.03em;
}

.annotated-meta p {
  margin: 0;
  color: var(--text-muted);
  font-size: 12px;
}

.annotated-stage {
  position: relative;
  width: 1780px;
  min-height: 1080px;
  padding-right: 324px;
}

.annotated-stage.tall {
  min-height: 1280px;
}

.annotated-stage.xl {
  min-height: 1440px;
}

.screen-host {
  width: 1440px;
}

.note-column {
  position: absolute;
  top: 0;
  right: 0;
  width: 300px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ux-dot {
  position: absolute;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border: 3px solid #ffffff;
  border-radius: 999px;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  line-height: 1;
  box-shadow: 0 10px 18px rgba(15, 23, 42, 0.20);
}

.ux-note {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 14px 16px 16px;
  border-radius: 16px;
  border: 1px solid rgba(209, 213, 222, 0.9);
  background: rgba(255, 255, 255, 0.98);
  box-shadow: 0 12px 24px rgba(17, 24, 39, 0.10);
}

.ux-note-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ux-index {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 999px;
  color: #ffffff;
  font-size: 11px;
  font-weight: 800;
  line-height: 1;
}

.ux-tag {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.ux-note strong {
  display: block;
  margin: 0;
  font-size: 13px;
  line-height: 1.35;
}

.ux-note p {
  margin: 0;
}

.ux-priority,
.ux-priority .ux-index,
.ux-priority.ux-dot {
  background: #c06b2d;
}

.ux-priority .ux-tag {
  color: #9a531f;
  background: rgba(192, 107, 45, 0.12);
}

.ux-clarity,
.ux-clarity .ux-index,
.ux-clarity.ux-dot {
  background: #2563eb;
}

.ux-clarity .ux-tag {
  color: #1d4ed8;
  background: rgba(37, 99, 235, 0.12);
}

.ux-flow,
.ux-flow .ux-index,
.ux-flow.ux-dot {
  background: #0d9488;
}

.ux-flow .ux-tag {
  color: #0f766e;
  background: rgba(13, 148, 136, 0.12);
}

.ux-trust,
.ux-trust .ux-index,
.ux-trust.ux-dot {
  background: #8c6a3a;
}

.ux-trust .ux-tag {
  color: #78592f;
  background: rgba(140, 106, 58, 0.12);
}

.ux-premium,
.ux-premium .ux-index,
.ux-premium.ux-dot {
  background: #7a4d63;
}

.ux-premium .ux-tag {
  color: #6a3e56;
  background: rgba(122, 77, 99, 0.12);
}

.reference-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.direction-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.direction-card {
  padding: 24px;
}

.direction-label {
  margin-bottom: 10px;
  color: var(--text-muted);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.direction-title {
  margin: 0 0 10px;
  font-size: 28px;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

.direction-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 16px 0 20px;
}

.direction-chip {
  padding: 7px 10px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.direction-body {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.direction-preview {
  overflow: hidden;
  border-radius: 24px;
  border: 1px solid rgba(209, 213, 222, 0.8);
}

.preview-shell {
  display: grid;
  grid-template-columns: 196px minmax(0, 1fr);
  min-height: 428px;
}

.preview-sidebar {
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.preview-logo {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.preview-nav {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 14px;
}

.preview-nav-item {
  padding: 10px 12px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 700;
}

.preview-main {
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.preview-kicker {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.preview-heading {
  margin: 0;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

.preview-copy {
  max-width: 520px;
  font-size: 12px;
  line-height: 1.7;
}

.preview-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 16px;
}

.preview-card,
.preview-note,
.preview-action {
  padding: 18px;
  border-radius: 18px;
}

.preview-score {
  display: flex;
  align-items: center;
  gap: 16px;
}

.preview-ring {
  width: 82px;
  height: 82px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  font-size: 30px;
  font-weight: 800;
  line-height: 1;
}

.preview-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.preview-list-item {
  padding: 10px 12px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 700;
}

.palette-row {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 10px;
}

.palette-swatch {
  overflow: hidden;
  border-radius: 16px;
  border: 1px solid rgba(209, 213, 222, 0.8);
  background: #ffffff;
}

.palette-chip {
  height: 56px;
}

.palette-info {
  padding: 10px 12px 12px;
}

.palette-info strong {
  display: block;
  margin-bottom: 4px;
  font-size: 11px;
}

.palette-info span {
  display: block;
  color: var(--text-muted);
  font-size: 10px;
}

.direction-panel-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.direction-panel {
  padding: 16px;
  border-radius: 18px;
  border: 1px solid rgba(209, 213, 222, 0.8);
  background: rgba(248, 250, 252, 0.8);
}

.direction-panel h4 {
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.direction-panel ul {
  margin: 0;
  padding-left: 18px;
}

.editorial-preview {
  background: linear-gradient(180deg, #f7f2eb 0%, #fdfcf9 100%);
}

.editorial-preview .preview-sidebar {
  background: #efe7dc;
  border-right: 1px solid rgba(140, 106, 58, 0.18);
}

.editorial-preview .preview-logo,
.editorial-preview .preview-kicker {
  color: #78592f;
}

.editorial-preview .preview-nav-item {
  color: #3b3127;
  background: rgba(140, 106, 58, 0.08);
}

.editorial-preview .preview-nav-item.active {
  color: #14202d;
  background: rgba(140, 106, 58, 0.16);
}

.editorial-preview .preview-heading {
  color: #14202d;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 42px;
}

.editorial-preview .preview-copy {
  color: #5f584e;
}

.editorial-preview .preview-card {
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid rgba(140, 106, 58, 0.18);
}

.editorial-preview .preview-note {
  background: #f2eadf;
  border: 1px solid rgba(140, 106, 58, 0.22);
}

.editorial-preview .preview-action {
  background: linear-gradient(180deg, rgba(48, 73, 63, 0.08), rgba(255, 255, 255, 0.9));
  border: 1px solid rgba(48, 73, 63, 0.2);
}

.editorial-preview .preview-ring {
  border: 2px solid #8c6a3a;
  color: #8c6a3a;
}

.editorial-preview .preview-list-item {
  background: rgba(140, 106, 58, 0.08);
  color: #3b3127;
}

.precision-preview {
  background: linear-gradient(180deg, #f7f7f5 0%, #edf2f4 100%);
}

.precision-preview .preview-sidebar {
  background: #e8ecef;
  border-right: 1px solid rgba(31, 38, 48, 0.10);
}

.precision-preview .preview-logo,
.precision-preview .preview-kicker {
  color: #1f2630;
}

.precision-preview .preview-nav-item {
  color: #475569;
  background: rgba(31, 38, 48, 0.06);
}

.precision-preview .preview-nav-item.active {
  color: #0b4d46;
  background: rgba(30, 90, 82, 0.12);
}

.precision-preview .preview-heading {
  color: #1f2630;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 38px;
  font-weight: 700;
}

.precision-preview .preview-copy {
  color: #52606d;
}

.precision-preview .preview-card {
  background: rgba(255, 255, 255, 0.82);
  border: 1px solid rgba(31, 38, 48, 0.10);
}

.precision-preview .preview-note {
  background: linear-gradient(180deg, rgba(30, 90, 82, 0.08), rgba(255,255,255,0.92));
  border: 1px solid rgba(30, 90, 82, 0.16);
}

.precision-preview .preview-action {
  background: rgba(255, 255, 255, 0.82);
  border: 1px solid rgba(214, 178, 115, 0.26);
}

.precision-preview .preview-ring {
  border: 2px solid #1e5a52;
  color: #1e5a52;
}

.precision-preview .preview-list-item {
  background: rgba(31, 38, 48, 0.06);
  color: #1f2630;
}
"""


def review_document(title: str, body: str) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{title}</title>
          <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
          <style>{BASE_CSS}{REVIEW_CSS}</style>
        </head>
        <body class="review-body">
          <div class="review-root">
            {body}
          </div>
        </body>
        </html>
        """
    )


def note_card(index: int, category: str, title: str, body: str) -> str:
    return dedent(
        f"""\
        <div class="ux-note ux-{category}">
          <div class="ux-note-header">
            <div class="ux-index">{index}</div>
            <div class="ux-tag">{category}</div>
          </div>
          <strong>{title}</strong>
          <p>{body}</p>
        </div>
        """
    )


def note_dot(index: int, category: str, x: int, y: int) -> str:
    return f'<div class="ux-dot ux-{category}" style="left:{x}px;top:{y}px;">{index}</div>'


def annotated_screen(
    title: str,
    summary: str,
    screen_html: str,
    notes: list[dict[str, object]],
    stage_class: str = "",
) -> str:
    dots = "".join(note_dot(note["index"], note["category"], note["x"], note["y"]) for note in notes)
    cards = "".join(
        note_card(note["index"], note["category"], note["title"], note["body"]) for note in notes
    )
    stage_class_attr = f"annotated-stage {stage_class}".strip()
    return dedent(
        f"""\
        <div class="annotated-screen">
          <div class="annotated-meta">
            <h3>{title}</h3>
            <p>{summary}</p>
          </div>
          <div class="{stage_class_attr}">
            <div class="screen-host">{screen_html}</div>
            {dots}
            <div class="note-column">{cards}</div>
          </div>
        </div>
        """
    )


def palette_card(name: str, hex_value: str, use: str) -> str:
    return dedent(
        f"""\
        <div class="palette-swatch">
          <div class="palette-chip" style="background:{hex_value};"></div>
          <div class="palette-info">
            <strong>{name}</strong>
            <span>{hex_value}</span>
            <span>{use}</span>
          </div>
        </div>
        """
    )


def direction_preview(direction: str) -> str:
    if direction == "editorial":
        return dedent(
            """\
            <div class="direction-preview editorial-preview">
              <div class="preview-shell">
                <div class="preview-sidebar">
                  <div class="preview-logo">Point93</div>
                  <div class="preview-nav">
                    <div class="preview-nav-item active">Practice Standing</div>
                    <div class="preview-nav-item">My Results</div>
                    <div class="preview-nav-item">Assessments</div>
                    <div class="preview-nav-item">Intelligence</div>
                  </div>
                </div>
                <div class="preview-main">
                  <div class="preview-kicker">Private Wealth Editorial</div>
                  <h4 class="preview-heading">Practice standing, rendered with discretion.</h4>
                  <div class="preview-copy">The UI feels less like software chrome and more like a tailored briefing prepared for a senior advisor before a client-facing day.</div>
                  <div class="preview-grid">
                    <div class="preview-card">
                      <div class="preview-score">
                        <div class="preview-ring">74</div>
                        <div>
                          <strong style="display:block;font-size:15px;">Competitive position</strong>
                          <div class="preview-copy">Operational discipline is strong; narrative confidence is the next lift.</div>
                        </div>
                      </div>
                    </div>
                    <div class="preview-note">
                      <div class="preview-kicker">Advisor Note</div>
                      <div class="preview-copy">Translate your strongest internal systems into clearer outward confidence in meetings.</div>
                    </div>
                  </div>
                  <div class="preview-action">
                    <div class="preview-kicker">Focus next</div>
                    <div class="preview-list">
                      <div class="preview-list-item">Complete IM.2 Practice Management</div>
                      <div class="preview-list-item">Unlock cross-module synthesis</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            """
        )

    return dedent(
        """\
        <div class="direction-preview precision-preview">
          <div class="preview-shell">
            <div class="preview-sidebar">
              <div class="preview-logo">Point93</div>
              <div class="preview-nav">
                <div class="preview-nav-item active">Dashboard</div>
                <div class="preview-nav-item">Results</div>
                <div class="preview-nav-item">Assessments</div>
                <div class="preview-nav-item">BI</div>
              </div>
            </div>
            <div class="preview-main">
              <div class="preview-kicker">Precision Concierge</div>
              <h4 class="preview-heading">An intelligence system with composure.</h4>
              <div class="preview-copy">The interface reads as expert, tailored, and high-conviction. Data feels curated, not dumped, with premium restraint replacing generic fintech energy.</div>
              <div class="preview-grid">
                <div class="preview-card">
                  <div class="preview-score">
                    <div class="preview-ring">74</div>
                    <div>
                      <strong style="display:block;font-size:15px;">Standing</strong>
                      <div class="preview-copy">83rd percentile against a clearly defined peer cohort.</div>
                    </div>
                  </div>
                </div>
                <div class="preview-note">
                  <div class="preview-kicker">Interpretation</div>
                  <div class="preview-copy">Your strongest gains now come from client-facing articulation, not internal control.</div>
                </div>
              </div>
              <div class="preview-action">
                <div class="preview-kicker">Next milestone</div>
                <div class="preview-list">
                  <div class="preview-list-item">Resume FT.2 Technology Capabilities</div>
                  <div class="preview-list-item">6 minutes to unlock BI stage progress</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        """
    )


def ux_review_page() -> str:
    intro = """
      <div class="intro-grid">
        <div class="review-card">
          <h3>What this pass is for</h3>
          <p>These notes mark the highest-leverage UX questions, not pixel issues. The goal is to improve clarity, momentum, trust, and the feeling of tailored guidance before we restyle the full system.</p>
        </div>
        <div class="review-card">
          <h3>How to read the dots</h3>
          <p>Each dot marks a location where the current interface is asking too much, explaining too little, or missing an opportunity to feel more confidence-building and premium.</p>
        </div>
        <div class="review-card">
          <h3>What we are optimizing for</h3>
          <p>UHNW-facing advisors need the product to feel expert, discreet, and high-conviction. It should guide them like a trusted strategic briefing, not a generic SaaS dashboard.</p>
        </div>
      </div>
    """

    principles = """
      <div class="principles-grid">
        <div class="principle-card"><h3>One clear next step</h3><p>Every major screen should signal what the advisor should do now, not just what the system knows.</p></div>
        <div class="principle-card"><h3>Interpret before detail</h3><p>Scores and comparisons need plain-language meaning before they branch into charts, tabs, or rankings.</p></div>
        <div class="principle-card"><h3>Trust through explanation</h3><p>Benchmark logic, AI narration, and BI gating should feel explicit and credible, especially for a skeptical high-income audience.</p></div>
        <div class="principle-card"><h3>Progress should motivate</h3><p>Assessment flow should reduce effort anxiety and create a stronger sense of pace, reward, and payoff.</p></div>
        <div class="principle-card"><h3>Premium means restraint</h3><p>Less badge noise, fewer equal-weight panels, and more curated hierarchy will do more than decorative polish.</p></div>
      </div>
    """

    screens = [
        annotated_screen(
            "Dashboard",
            "The highest-stakes arrival surface. It currently carries orientation, score interpretation, status, and action selection all at once.",
            dashboard_screen(),
            [
                {
                    "index": 1,
                    "category": "priority",
                    "x": 248,
                    "y": 186,
                    "title": "Clarify the hero action",
                    "body": "Arrival currently asks the advisor to orient, resume work, evaluate score, scan areas, and read AI. We should define the one action that makes a first visit feel successful.",
                },
                {
                    "index": 2,
                    "category": "clarity",
                    "x": 520,
                    "y": 402,
                    "title": "Translate score into business meaning",
                    "body": "Percentile and band are efficient, but they need a stronger explanation of what this means for the practice and what changes when the score moves.",
                },
                {
                    "index": 3,
                    "category": "trust",
                    "x": 958,
                    "y": 402,
                    "title": "Make the area map worth reading",
                    "body": "Abbreviations and completion percentages are compact, but they do not yet tell the advisor which area deserves attention next or why it matters.",
                },
            ],
            "xl",
        ),
        annotated_screen(
            "My Results · Score Overview",
            "The results hub should feel like an executive readout, but it still makes the user assemble the story themselves.",
            my_results_overview(),
            [
                {
                    "index": 1,
                    "category": "clarity",
                    "x": 132,
                    "y": 120,
                    "title": "Tabs need stronger narrative framing",
                    "body": "Score Overview, Strengths & Gaps, and Trends are valid views, but the product should explain how they differ and which one to start with.",
                },
                {
                    "index": 2,
                    "category": "trust",
                    "x": 302,
                    "y": 335,
                    "title": "Benchmark trust needs better scaffolding",
                    "body": "A premium audience will want to understand peer-set logic, percentile quality, and the confidence of the comparison before trusting the conclusion.",
                },
                {
                    "index": 3,
                    "category": "priority",
                    "x": 865,
                    "y": 608,
                    "title": "Surface action over raw inventory",
                    "body": "Results currently reward scanning. We should decide how to elevate the top two or three follow-up actions without losing the reference detail.",
                },
            ],
            "tall",
        ),
        annotated_screen(
            "Assessments Landing",
            "This is where the product needs to convert intention into commitment. The list is clear, but the decision support is still light.",
            assessments_landing(),
            [
                {
                    "index": 1,
                    "category": "priority",
                    "x": 250,
                    "y": 250,
                    "title": "Make prioritization more opinionated",
                    "body": "Module ordering is visible, but the screen should say why a module is next and what the expected business payoff is if the advisor completes it.",
                },
                {
                    "index": 2,
                    "category": "flow",
                    "x": 495,
                    "y": 650,
                    "title": "Reduce assessment-start anxiety",
                    "body": "Before people begin, we should communicate time, auto-save confidence, and what completing a module will unlock elsewhere in the experience.",
                },
                {
                    "index": 3,
                    "category": "premium",
                    "x": 1020,
                    "y": 650,
                    "title": "Turn recommendations into concierge guidance",
                    "body": "Recommended modules can feel more bespoke if they read as a tailored plan rather than a generic task list.",
                },
            ],
            "xl",
        ),
        annotated_screen(
            "Assessment Question",
            "Question flow is functionally clear. The opportunity is emotional pacing, confidence, and reduction of ambiguity.",
            assessment_question("likert"),
            [
                {
                    "index": 1,
                    "category": "flow",
                    "x": 315,
                    "y": 182,
                    "title": "Use progress to build confidence",
                    "body": "Progress should feel more like momentum than bookkeeping. The advisor should feel the assessment is moving quickly and safely toward value.",
                },
                {
                    "index": 2,
                    "category": "clarity",
                    "x": 480,
                    "y": 360,
                    "title": "Strengthen answer anchors",
                    "body": "When questions touch behavior and process maturity, stronger examples or endpoint descriptions can reduce interpretation drift.",
                },
                {
                    "index": 3,
                    "category": "trust",
                    "x": 950,
                    "y": 825,
                    "title": "Reassure the user about how answers are used",
                    "body": "For affluent advisors, credibility goes up when the system feels transparent about how responses become scores, insights, and future BI guidance.",
                },
            ],
            "tall",
        ),
        annotated_screen(
            "Module Results",
            "This is one of the best opportunities to make Point93 feel premium and distinctive, because it combines result, interpretation, and next-step guidance.",
            module_results(),
            [
                {
                    "index": 1,
                    "category": "priority",
                    "x": 300,
                    "y": 230,
                    "title": "Separate reveal from diagnosis",
                    "body": "The first read should clearly answer: what was the result, is it good, and what does it mean before the screen asks the user to parse deeper layers.",
                },
                {
                    "index": 2,
                    "category": "clarity",
                    "x": 715,
                    "y": 615,
                    "title": "Route from insight into action",
                    "body": "Insight blocks are useful, but the handoff into the next module, next area, or next business action should feel more explicit and sequential.",
                },
                {
                    "index": 3,
                    "category": "premium",
                    "x": 1025,
                    "y": 920,
                    "title": "Make Moenio Lens feel like concierge interpretation",
                    "body": "This section is a chance to feel signature and proprietary. It should read like a reserved advisory memo, not just one more card in the stack.",
                },
            ],
            "xl",
        ),
        annotated_screen(
            "BI Product Page",
            "The BI stage model is promising, but the current structure still feels more gated than guided.",
            bi_product(),
            [
                {
                    "index": 1,
                    "category": "flow",
                    "x": 900,
                    "y": 308,
                    "title": "Emphasize the next milestone",
                    "body": "The stage stepper should help the advisor understand what the immediate next unlock is, how close it is, and why it is valuable.",
                },
                {
                    "index": 2,
                    "category": "clarity",
                    "x": 375,
                    "y": 560,
                    "title": "Clarify prerequisite logic",
                    "body": "Locked prerequisites are understandable, but the product should frame them as a guided path rather than a constraint or feature gate.",
                },
                {
                    "index": 3,
                    "category": "trust",
                    "x": 985,
                    "y": 620,
                    "title": "Tie BI effort to business benefit",
                    "body": "The advisor should quickly see what insight or practice advantage each BI stage creates, not just that a stage exists.",
                },
            ],
            "tall",
        ),
        annotated_screen(
            "Settings & Profile",
            "Settings is structurally fine; the main opportunity is how account value and service relationships are framed.",
            settings_screen(),
            [
                {
                    "index": 1,
                    "category": "premium",
                    "x": 935,
                    "y": 650,
                    "title": "Shift tier management toward white-glove service",
                    "body": "Pricing and upgrade language can feel more considered if it positions the tier as a level of support and depth, not a software upsell.",
                },
                {
                    "index": 2,
                    "category": "clarity",
                    "x": 425,
                    "y": 705,
                    "title": "Group settings by user outcome",
                    "body": "Preference rows can feel lighter if they are organized by what the advisor is trying to control, rather than by an internal settings taxonomy.",
                },
            ],
        ),
    ]

    body = review_document(
        "Point93 / UX Opportunity Review",
        "".join(
            [
                '<div class="review-stack">',
                cover(
                    "Point93 / UX Opportunity Review",
                    "A design-thinking overlay that marks the most promising UX opportunities across the MVP. The emphasis is on decision quality, confidence, and premium guidance rather than cosmetic polish.",
                    [
                        "Dots mark high-leverage friction or opportunity",
                        "Bias toward clarity, trust, and momentum",
                        "Built for the UHNW advisor audience",
                    ],
                ),
                intro,
                principles,
                '<section class="review-section"><div class="review-section-header"><div><div class="eyebrow">Wave 1 critique</div><h2>Annotated opportunity pass</h2><p>These are the screens where product hierarchy, interpretation, and perceived value matter most. Each note is phrased as a design question we should answer in future iterations.</p></div><div class="count-pill">7 screens reviewed</div></div><div class="annotation-board">',
                "".join(screens),
                "</div></section></div>",
            ]
        ),
    )
    return body


def visual_review_page() -> str:
    audience = """
      <div class="utility-grid">
        <div class="utility-card"><h3>Audience reality</h3><p>This is software for advisors serving ultra-high-net-worth clients. The product should feel composed, expensive in taste, and quietly authoritative.</p></div>
        <div class="utility-card"><h3>What to borrow from Mobbin</h3><p>Borrow compositional confidence, restrained chrome, and a more art-directed approach to data surfaces. Keep the calm, not the consumer-fintech energy.</p></div>
        <div class="utility-card"><h3>What to avoid</h3><p>Avoid generic SaaS blue, crypto aesthetics, loud dark mode, playful badges, or overt “luxury” signals that feel performative instead of credible.</p></div>
        <div class="utility-card"><h3>Immediate goal</h3><p>Find a visual language that makes Point93 feel less generic and more like a strategic briefing system for a high-trust wealth audience.</p></div>
      </div>
    """

    references = """
      <div class="reference-grid">
        <div class="reference-card">
          <h3>Reference synthesis</h3>
          <p>The mood board leans toward premium finance products: high whitespace, clear hierarchy, disciplined cards, and selective moments of rich contrast. The strongest signal is composure, not ornament.</p>
        </div>
        <div class="reference-card">
          <h3>Translation for Point93</h3>
          <p>Point93 needs to go one step further toward advisory discretion. The UI should feel like a custom practice-intelligence environment, with more gravitas and fewer generic product conventions.</p>
        </div>
      </div>
    """

    editorial_direction = dedent(
        """\
        <div class="direction-card">
          <div class="direction-label">Direction A</div>
          <h3 class="direction-title">Quiet Wealth Editorial</h3>
          <p>A restrained, warm, literate direction. It treats the interface like an executive dossier with curated emphasis, elegant spacing, and a softer palette.</p>
          <div class="direction-chips">
            <div class="direction-chip" style="background:rgba(140,106,58,0.10);color:#78592f;">Discreet</div>
            <div class="direction-chip" style="background:rgba(48,73,63,0.10);color:#30493f;">Tailored</div>
            <div class="direction-chip" style="background:rgba(20,32,45,0.08);color:#14202d;">Editorial</div>
          </div>
          <div class="direction-body">
            """ + direction_preview("editorial") + """
            <div class="palette-row">
              """ + "".join(
            [
                palette_card("Warm Ivory", "#f7f2eb", "Base surface"),
                palette_card("Ink", "#14202d", "Primary text"),
                palette_card("Bronze", "#8c6a3a", "Premium accent"),
                palette_card("Moss", "#30493f", "Insight emphasis"),
                palette_card("Fog", "#e6dfd2", "Soft secondary surface"),
            ]
        ) + """
            </div>
            <div class="direction-panel-grid">
              <div class="direction-panel">
                <h4>System moves</h4>
                <ul>
                  <li>Replace generic blue dominance with warmer, rarer accent moments.</li>
                  <li>Use serif-led display moments only where authority matters most.</li>
                  <li>Give scores and insights more breathing room and narrative framing.</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>Best test screens</h4>
                <ul>
                  <li>Dashboard</li>
                  <li>My Results</li>
                  <li>Module Results</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>What it says</h4>
                <ul>
                  <li>This platform is bespoke.</li>
                  <li>The intelligence is considered, not automated noise.</li>
                  <li>Your practice is being reviewed with taste and care.</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>Anti-goals</h4>
                <ul>
                  <li>No flashy gold-and-black wealth cliches.</li>
                  <li>No luxury-for-luxury’s-sake ornament.</li>
                  <li>No heavy-handed dark mode.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        """
    )

    precision_direction = dedent(
        """\
        <div class="direction-card">
          <div class="direction-label">Direction B</div>
          <h3 class="direction-title">Precision Concierge</h3>
          <p>A sharper and more modern direction. It keeps the interface light, but makes it feel more exacting, bespoke, and confidence-building than a typical fintech dashboard.</p>
          <div class="direction-chips">
            <div class="direction-chip" style="background:rgba(31,38,48,0.08);color:#1f2630;">Exacting</div>
            <div class="direction-chip" style="background:rgba(30,90,82,0.10);color:#1e5a52;">Composed</div>
            <div class="direction-chip" style="background:rgba(214,178,115,0.16);color:#8c6a3a;">Premium</div>
          </div>
          <div class="direction-body">
            """ + direction_preview("precision") + """
            <div class="palette-row">
              """ + "".join(
            [
                palette_card("Pearl", "#f7f7f5", "Base surface"),
                palette_card("Slate", "#1f2630", "Primary text"),
                palette_card("Evergreen", "#1e5a52", "Trust accent"),
                palette_card("Champagne", "#d6b273", "Selective highlight"),
                palette_card("Smoke", "#d9dde3", "Structure and lines"),
            ]
        ) + """
            </div>
            <div class="direction-panel-grid">
              <div class="direction-panel">
                <h4>System moves</h4>
                <ul>
                  <li>Reduce pill clutter and rely more on hierarchy, spacing, and tonal separation.</li>
                  <li>Treat charts, scores, and progress surfaces as prestige objects.</li>
                  <li>Make AI blocks feel credentialed and editorial, not playful.</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>Best test screens</h4>
                <ul>
                  <li>Dashboard</li>
                  <li>Assessment flow</li>
                  <li>BI Product</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>What it says</h4>
                <ul>
                  <li>This system is disciplined and expert.</li>
                  <li>The recommendations are curated, not generic.</li>
                  <li>The product belongs in a premium advisory workflow.</li>
                </ul>
              </div>
              <div class="direction-panel">
                <h4>Anti-goals</h4>
                <ul>
                  <li>No consumer-banking friendliness.</li>
                  <li>No crypto-style gradients and neon.</li>
                  <li>No crowded control bars and badge stacks.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        """
    )

    body = review_document(
        "Point93 / Visual Direction Review",
        "".join(
            [
                '<div class="review-stack">',
                cover(
                    "Point93 / Visual Direction Review",
                    "A first-pass exploration of how Point93 could feel more affluent, tailored, and high-trust without losing the clean structural system. These are directional studies, not final UI comps.",
                    [
                        "Built from the Mobbin reference set",
                        "Bias toward discretion over flash",
                        "Two viable premium directions",
                    ],
                ),
                audience,
                references,
                '<section class="review-section"><div class="review-section-header"><div><div class="eyebrow">Exploration</div><h2>Two premium visual directions</h2><p>Both directions keep the current product architecture intact while changing the emotional register. The choice is less about “luxury styling” and more about what kind of high-trust intelligence product Point93 should become.</p></div><div class="count-pill">2 directions</div></div><div class="direction-grid">',
                editorial_direction,
                precision_direction,
                "</div></section></div>",
            ]
        ),
    )
    return body


def write_outputs() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    outputs = {
        "point93-ux-review.html": ux_review_page(),
        "point93-visual-review.html": visual_review_page(),
    }
    for name, contents in outputs.items():
        (OUT_DIR / name).write_text(contents)
        print(f"Wrote figma_exports/{name}")


if __name__ == "__main__":
    write_outputs()
