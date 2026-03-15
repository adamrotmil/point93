from __future__ import annotations

from copy import deepcopy
from html import escape
from pathlib import Path
from textwrap import dedent

from lxml import etree, html


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HTML = ROOT / "01_Design_Specs/03_Point93_Screen_Wireframes_v1.2.html"
OUTPUT_HTML = ROOT / "07_Point93_MVP_Clean_Import.html"


def class_xpath(name: str) -> str:
    return f"contains(concat(' ', normalize-space(@class), ' '), ' {name} ')"


def first_text(node: html.HtmlElement, class_name: str) -> str:
    matches = node.xpath(f".//*[ {class_xpath(class_name)} ]")
    if not matches:
        return ""
    return " ".join(matches[0].itertext()).strip()


def extract_base_css(document: html.HtmlElement) -> str:
    styles = [text for text in document.xpath("//style/text()") if text.strip()]
    return "\n\n".join(styles)


def extract_panel_canvases(document: html.HtmlElement, panel_id: str) -> list[dict[str, str]]:
    panels = {
        panel.get("id"): panel
        for panel in document.xpath(f"//div[{class_xpath('wf-panel')}]")
    }
    panel = panels[panel_id]
    panel_title = first_text(panel, "panel-title")
    panel_ref = first_text(panel, "panel-ref")

    screens: list[dict[str, str]] = []
    for canvas in panel.xpath(f"./div[{class_xpath('wf-canvas')}]"):
        label = first_text(canvas, "wf-canvas-label") or panel_title
        canvas_copy = deepcopy(canvas)
        for label_node in canvas_copy.xpath(f".//*[ {class_xpath('wf-canvas-label')} ]"):
            parent = label_node.getparent()
            if parent is not None:
                parent.remove(label_node)

        body_html = "".join(
            etree.tostring(child, encoding="unicode") for child in canvas_copy.getchildren()
        )
        screens.append(
            {
                "panel_title": panel_title,
                "screen_title": label,
                "source": panel_ref,
                "body_html": body_html,
            }
        )

    return screens


def render_sidebar(active_key: str) -> str:
    items = [
        ("dashboard", "◫", "Dashboard", ""),
        ("results", "★", "My Results", '<span style="margin-left:auto;width:6px;height:6px;border-radius:50%;background:var(--green);"></span>'),
        ("assessments", "✎", "Assessments", '<span style="margin-left:auto;font-size:9px;color:var(--amber);font-weight:600;">1 in progress</span>'),
        ("areas", "◧", "My Areas", ""),
        ("bi", "◈", "Business Intelligence", ""),
        ("clients", "◇", "What Clients Are Asking", '<span style="font-size:8px;background:var(--amber-bg);color:var(--amber);padding:1px 6px;border-radius:8px;font-weight:600;margin-left:auto;">Soon</span>'),
    ]

    item_html = []
    for key, icon, label, suffix in items:
        active = " active" if key == active_key else ""
        item_html.append(
            f'<div class="wf-sidebar-item{active}"><span class="nav-icon">{icon}</span> {label}{suffix}</div>'
        )

    return dedent(
        f"""
        <div class="wf-sidebar">
          <div class="wf-sidebar-logo">Point93</div>
          {''.join(item_html)}
          <div style="border-top:1px solid var(--border);margin:12px 16px;"></div>
          <div style="padding:0 16px;">
            <div style="font-size:9px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;">Account</div>
            <div style="font-size:11px;font-weight:600;color:var(--purple);margin-bottom:4px;">Comprehensive</div>
            <div style="font-size:10px;color:var(--text-muted);">5/17 modules · 29%</div>
            <div style="height:3px;background:var(--surface);border-radius:2px;margin-top:4px;">
              <div style="height:3px;background:var(--accent);border-radius:2px;width:29%;"></div>
            </div>
          </div>
        </div>
        """
    ).strip()


def render_results_tabs(active_tab: str) -> str:
    tabs = [
        ("overview", "Score Overview"),
        ("strengths", "Strengths & Gaps"),
        ("trends", "Trends"),
    ]

    chips = []
    for key, label in tabs:
        selected = key == active_tab
        chips.append(
            dedent(
                f"""
                <div style="padding:8px 14px;border-radius:999px;border:1px solid {'var(--accent)' if selected else 'var(--border)'};background:{'var(--accent-glow)' if selected else 'white'};color:{'var(--accent)' if selected else 'var(--text-muted)'};font-size:11px;font-weight:{'700' if selected else '600'};">
                  {label}
                </div>
                """
            ).strip()
        )

    return (
        '<div style="display:flex;gap:10px;align-items:center;margin-bottom:20px;">'
        + "".join(chips)
        + "</div>"
    )


def render_results_page(active_tab: str, body: str) -> str:
    return dedent(
        f"""
        <div class="wf-page">
          {render_sidebar("results")}
          <div class="wf-main">
            <div style="margin-bottom:24px;">
              <div style="font-size:22px;font-weight:700;margin-bottom:4px;">My Results</div>
              <div style="font-size:13px;color:var(--text-muted);">All scores, benchmarks, and analytical views across completed modules.</div>
            </div>
            {render_results_tabs(active_tab)}
            {body}
          </div>
        </div>
        """
    ).strip()


def synthesize_my_results_screens() -> list[dict[str, str]]:
    overview_body = dedent(
        """
        <div class="wf-block" style="margin-bottom:16px;">
          <div class="wf-block-label"><span class="wf-block-num">1</span> OVERALL SCORE + BAND</div>
          <div class="wf-flex" style="align-items:center;">
            <div class="wf-score-circle">74</div>
            <div style="margin-left:16px;">
              <div style="font-size:18px;font-weight:700;">Overall Point93 Position</div>
              <div style="font-size:13px;color:var(--accent);font-weight:600;"><span class="band-shape band-shape-comp"></span> B · Competitive</div>
              <div style="font-size:11px;color:var(--text-muted);margin-top:4px;">83rd percentile · 5 completed modules · updated after latest module completion</div>
            </div>
          </div>
        </div>

        <div class="wf-section-label">Area Scores</div>
        <div class="wf-grid-2" style="margin-bottom:16px;">
          <div class="wf-block">
            <div style="display:flex;align-items:center;gap:12px;">
              <div class="wf-score-sm" style="border-color:var(--green);color:var(--green);">73</div>
              <div>
                <div style="font-size:13px;font-weight:700;">Professional Foundation</div>
                <div style="font-size:10px;color:var(--green);font-weight:600;"><span class="band-shape band-shape-top"></span> A · Top Tier</div>
              </div>
            </div>
          </div>
          <div class="wf-block">
            <div style="display:flex;align-items:center;gap:12px;">
              <div class="wf-score-sm" style="border-color:var(--accent);color:var(--accent);">71</div>
              <div>
                <div style="font-size:13px;font-weight:700;">Firm Platform &amp; Technology</div>
                <div style="font-size:10px;color:var(--accent);font-weight:600;"><span class="band-shape band-shape-comp"></span> B · Competitive</div>
              </div>
            </div>
          </div>
          <div class="wf-block">
            <div style="display:flex;align-items:center;gap:12px;">
              <div class="wf-score-sm" style="border-color:var(--amber);color:var(--amber);">62</div>
              <div>
                <div style="font-size:13px;font-weight:700;">Investment Strategy</div>
                <div style="font-size:10px;color:var(--amber);font-weight:600;"><span class="band-shape band-shape-needs"></span> C · Needs Work</div>
              </div>
            </div>
          </div>
          <div class="wf-block">
            <div style="display:flex;align-items:center;gap:12px;">
              <div class="wf-score-sm" style="border-color:var(--border);color:var(--text-muted);">—</div>
              <div>
                <div style="font-size:13px;font-weight:700;">Planning Process</div>
                <div style="font-size:10px;color:var(--text-muted);">Not assessed</div>
              </div>
            </div>
          </div>
        </div>

        <div class="wf-section-label">Module Score Grid</div>
        <div class="wf-block" style="margin-bottom:16px;">
          <table class="token-table" style="font-size:11px;">
            <thead>
              <tr><th>Module</th><th>Your Score</th><th>Average</th><th>Top 5%</th><th>Band</th></tr>
            </thead>
            <tbody>
              <tr><td>PF.1 Compliance Fundamentals</td><td>78</td><td>66</td><td>88</td><td style="color:var(--accent);font-weight:600;">B · Competitive</td></tr>
              <tr><td>PF.2 Compliance Infrastructure</td><td>76</td><td>69</td><td>91</td><td style="color:var(--accent);font-weight:600;">B · Competitive</td></tr>
              <tr><td>FT.2 Technology Capabilities</td><td>71</td><td>64</td><td>86</td><td style="color:var(--accent);font-weight:600;">B · Competitive</td></tr>
              <tr><td>IM.1 Client Relationship Depth</td><td>62</td><td>67</td><td>85</td><td style="color:var(--amber);font-weight:600;">C · Needs Work</td></tr>
            </tbody>
          </table>
        </div>

        <div class="wf-block">
          <div class="wf-block-label"><span class="wf-block-num">4</span> BENCHMARK SNAPSHOT</div>
          <div style="font-size:12px;color:var(--text-muted);line-height:1.6;">Sortable comparison rows for overall score, each completed area, and each completed module. The clean MVP import keeps the structure simple: your score, average, top 5%, percentile, and band in one comparison surface.</div>
        </div>
        """
    ).strip()

    strengths_body = dedent(
        """
        <div class="wf-grid-2" style="margin-bottom:16px;">
          <div class="wf-block" style="border-left:3px solid var(--green);">
            <div class="wf-block-label"><span class="wf-block-num">1</span> EDGE LIST</div>
            <div style="display:flex;flex-direction:column;gap:10px;font-size:12px;">
              <div><strong>1.</strong> Can Your Clients Operate Without Calling You? <span style="color:var(--green);font-weight:600;">91</span><br><span style="color:var(--text-muted);font-size:10px;">PF.2 Compliance Infrastructure</span></div>
              <div><strong>2.</strong> Are Your Processes Repeatable Across Advisors? <span style="color:var(--green);font-weight:600;">88</span><br><span style="color:var(--text-muted);font-size:10px;">FT.2 Technology Capabilities</span></div>
              <div><strong>3.</strong> Is Your Oversight Framework Durable? <span style="color:var(--accent);font-weight:600;">84</span><br><span style="color:var(--text-muted);font-size:10px;">PF.1 Compliance Fundamentals</span></div>
            </div>
          </div>
          <div class="wf-block" style="border-left:3px solid var(--rose);">
            <div class="wf-block-label"><span class="wf-block-num">2</span> EXPOSURE LIST</div>
            <div style="display:flex;flex-direction:column;gap:10px;font-size:12px;">
              <div><strong>1.</strong> Are Investment Decisions Consistently Framed for Clients? <span style="color:var(--rose);font-weight:600;">49</span><br><span style="color:var(--text-muted);font-size:10px;">IM.1 Client Relationship Depth</span></div>
              <div><strong>2.</strong> Is Your Practice Management Cadence Visible to the Team? <span style="color:var(--amber);font-weight:600;">56</span><br><span style="color:var(--text-muted);font-size:10px;">IM.2 Practice Management</span></div>
              <div><strong>3.</strong> Do Prospects Hear a Clear Value Story? <span style="color:var(--amber);font-weight:600;">59</span><br><span style="color:var(--text-muted);font-size:10px;">PitchPerfect</span></div>
            </div>
          </div>
        </div>

        <div class="wf-grid-2" style="margin-bottom:16px;">
          <div class="wf-block">
            <div class="wf-block-label"><span class="wf-block-num">3</span> YOUR POSITION DETAIL</div>
            <div style="font-size:12px;line-height:1.6;color:var(--text-muted);">You are sitting in the upper Competitive band, closer to Top Tier than to Needs Work. Two more points on platform technology would move that area into Top Tier, while investment communication remains the most likely factor to pull the overall position down.</div>
          </div>
          <div class="wf-block">
            <div class="wf-block-label"><span class="wf-block-num">4</span> PRIORITY GAP ANALYSIS</div>
            <table class="token-table" style="font-size:11px;">
              <thead>
                <tr><th>IA</th><th>Current</th><th>Competitive Floor</th><th>Gap</th></tr>
              </thead>
              <tbody>
                <tr><td>Investment Communication</td><td>49</td><td>70</td><td>21</td></tr>
                <tr><td>Practice Management Cadence</td><td>56</td><td>70</td><td>14</td></tr>
                <tr><td>Value Story Clarity</td><td>59</td><td>70</td><td>11</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="wf-block" style="background:var(--surface2);">
          <div style="font-size:12px;color:var(--text-muted);line-height:1.6;">The blueprint calls this view the full Edge/Exposure ranking surface: all strongest IAs, all weakest IAs, position detail, and the top five gaps by distance to the competitive floor.</div>
        </div>
        """
    ).strip()

    trends_body = dedent(
        """
        <div class="wf-block" style="margin-bottom:16px;">
          <div class="wf-block-label"><span class="wf-block-num">1</span> SCORE PROGRESSION</div>
          <div style="padding:12px 8px 4px;">
            <svg viewBox="0 0 760 220" width="100%" height="220" aria-label="Score progression chart">
              <line x1="40" y1="180" x2="720" y2="180" stroke="var(--border)" stroke-width="1" />
              <line x1="40" y1="140" x2="720" y2="140" stroke="rgba(37,99,235,0.15)" stroke-width="1" />
              <line x1="40" y1="100" x2="720" y2="100" stroke="rgba(5,150,105,0.15)" stroke-width="1" />
              <line x1="40" y1="60" x2="720" y2="60" stroke="rgba(217,119,6,0.15)" stroke-width="1" />
              <polyline fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" points="80,165 220,150 360,136 500,110 640,100" />
              <circle cx="80" cy="165" r="6" fill="white" stroke="var(--accent)" stroke-width="3" />
              <circle cx="220" cy="150" r="6" fill="white" stroke="var(--accent)" stroke-width="3" />
              <circle cx="360" cy="136" r="6" fill="white" stroke="var(--accent)" stroke-width="3" />
              <circle cx="500" cy="110" r="6" fill="white" stroke="var(--accent)" stroke-width="3" />
              <circle cx="640" cy="100" r="6" fill="white" stroke="var(--accent)" stroke-width="3" />
              <text x="40" y="185" font-size="10" fill="var(--text-muted)">50</text>
              <text x="40" y="145" font-size="10" fill="var(--text-muted)">65</text>
              <text x="40" y="105" font-size="10" fill="var(--text-muted)">80</text>
              <text x="60" y="205" font-size="10" fill="var(--text-muted)">Jan 9</text>
              <text x="200" y="205" font-size="10" fill="var(--text-muted)">Jan 22</text>
              <text x="340" y="205" font-size="10" fill="var(--text-muted)">Feb 1</text>
              <text x="480" y="205" font-size="10" fill="var(--text-muted)">Feb 19</text>
              <text x="620" y="205" font-size="10" fill="var(--text-muted)">Mar 8</text>
            </svg>
          </div>
        </div>

        <div class="wf-grid-2" style="margin-bottom:16px;">
          <div class="wf-block">
            <div class="wf-block-label"><span class="wf-block-num">2</span> BEFORE / AFTER</div>
            <div style="display:flex;flex-direction:column;gap:10px;font-size:12px;">
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;">FT.2 Technology Capabilities: <strong>68</strong> → <strong style="color:var(--green);">71</strong> <span style="color:var(--green);">↑ +3</span></div>
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;">PF.1 Compliance Fundamentals: <strong>74</strong> → <strong style="color:var(--green);">78</strong> <span style="color:var(--green);">↑ +4</span></div>
            </div>
          </div>
          <div class="wf-block">
            <div class="wf-block-label"><span class="wf-block-num">3</span> AREA TRAJECTORIES</div>
            <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;">
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;font-size:11px;">PF <span class="sparkline-trend"><svg viewBox="0 0 48 16"><polyline points="2,14 12,11 24,8 36,6 46,4" fill="none" stroke="var(--green)" stroke-width="1.5" stroke-linecap="round"/></svg></span></div>
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;font-size:11px;">FT <span class="sparkline-trend"><svg viewBox="0 0 48 16"><polyline points="2,13 12,12 24,10 36,8 46,6" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round"/></svg></span></div>
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;font-size:11px;">IM <span class="sparkline-trend"><svg viewBox="0 0 48 16"><polyline points="2,10 12,12 24,11 36,9 46,8" fill="none" stroke="var(--amber)" stroke-width="1.5" stroke-linecap="round"/></svg></span></div>
              <div style="padding:10px 12px;background:var(--surface2);border-radius:8px;font-size:11px;">PI <span style="color:var(--text-muted);">No data yet</span></div>
            </div>
          </div>
        </div>

        <div class="wf-block" style="background:var(--surface2);">
          <div style="font-size:12px;color:var(--text-muted);line-height:1.6;">The blueprint specifies single-point behavior for new accounts and before/after cards when reassessments happen. This synthesized screen shows the richer post-MVP state to anchor future visual design in Figma.</div>
        </div>
        """
    ).strip()

    return [
        {
            "category": "Platform Core",
            "panel_title": "My Results",
            "screen_title": "My Results · Score Overview",
            "source": "Blueprint §4.1–§4.2 · IA Map §4.2 · Flow 7",
            "tag": "Synthesized from spec",
            "body_html": render_results_page("overview", overview_body),
            "note": "The source repo does not include a dedicated My Results wireframe panel, so this screen is synthesized from the blueprint, IA map, and interaction flow definitions.",
        },
        {
            "category": "Platform Core",
            "panel_title": "My Results",
            "screen_title": "My Results · Strengths & Gaps",
            "source": "Blueprint §4.3 · IA Map §4.3 · Flow 7",
            "tag": "Synthesized from spec",
            "body_html": render_results_page("strengths", strengths_body),
            "note": "This variant covers the full Edge/Exposure view that is specified architecturally but not drawn in the shipped wireframe HTML.",
        },
        {
            "category": "Platform Core",
            "panel_title": "My Results",
            "screen_title": "My Results · Trends",
            "source": "Blueprint §4.4 · IA Map §4.4 · Flow 7",
            "tag": "Synthesized from spec",
            "body_html": render_results_page("trends", trends_body),
            "note": "This trend layout combines the blueprint's score progression, before/after comparison, and area trajectories into one clean screen state.",
        },
    ]


def build_screen_inventory(document: html.HtmlElement) -> list[dict[str, str]]:
    ordered_panels = [
        ("Platform Core", "panel-dashboard"),
        ("Assessments", "panel-assessments-landing"),
        ("Assessments", "panel-module-home"),
        ("Assessments", "panel-assessment"),
        ("Assessments", "panel-module-results"),
        ("Areas & BI", "panel-areas-landing"),
        ("Areas & BI", "panel-area-page"),
        ("Areas & BI", "panel-bi-landing"),
        ("Areas & BI", "panel-bi-product"),
        ("Supporting Screens", "panel-coming-soon"),
        ("Onboarding & Settings", "panel-onboarding"),
        ("Onboarding & Settings", "panel-settings"),
    ]

    screens: list[dict[str, str]] = []
    for category, panel_id in ordered_panels:
        for screen in extract_panel_canvases(document, panel_id):
            screens.append(
                {
                    "category": category,
                    "panel_title": screen["panel_title"],
                    "screen_title": screen["screen_title"],
                    "source": screen["source"],
                    "tag": "Wireframe source",
                    "body_html": screen["body_html"],
                    "note": "",
                }
            )

        if panel_id == "panel-dashboard":
            screens.extend(synthesize_my_results_screens())

    return screens


def render_screen_card(screen: dict[str, str]) -> str:
    note_html = ""
    if screen["note"]:
        note_html = f'<div class="import-card-note">{escape(screen["note"])}</div>'

    synthesized_class = " import-card-synthesized" if screen["tag"] == "Synthesized from spec" else ""
    return dedent(
        f"""
        <article class="import-card{synthesized_class}">
          <div class="import-card-header">
            <div>
              <div class="import-card-kicker">{escape(screen["panel_title"])}</div>
              <h3>{escape(screen["screen_title"])}</h3>
            </div>
            <div class="import-card-meta">
              <span class="import-pill">{escape(screen["tag"])}</span>
              <span>{escape(screen["source"])}</span>
            </div>
          </div>
          {note_html}
          <div class="import-card-canvas">
            {screen["body_html"]}
          </div>
        </article>
        """
    ).strip()


def render_output(document: html.HtmlElement) -> str:
    base_css = extract_base_css(document)
    screens = build_screen_inventory(document)

    category_descriptions = {
        "Platform Core": "Platform-level briefing surfaces plus the missing My Results tabbed page synthesized from the blueprint and IA map.",
        "Assessments": "The core diagnostic journey from module discovery through completion and the flagship results screen.",
        "Areas & BI": "Cross-module area intelligence and the separate Business Intelligence track.",
        "Supporting Screens": "Visible but limited v1 surfaces that still need to live in the MVP app shell.",
        "Onboarding & Settings": "Entry flow, account setup, and persistent account management screens.",
    }

    grouped: dict[str, list[dict[str, str]]] = {}
    for screen in screens:
        grouped.setdefault(screen["category"], []).append(screen)

    section_html = []
    for category, category_screens in grouped.items():
        cards = "\n".join(render_screen_card(screen) for screen in category_screens)
        section_html.append(
            dedent(
                f"""
                <section class="import-section">
                  <div class="import-section-header">
                    <div>
                      <div class="import-section-kicker">Point93 MVP</div>
                      <h2>{escape(category)}</h2>
                      <p>{escape(category_descriptions[category])}</p>
                    </div>
                    <div class="import-section-count">{len(category_screens)} screens</div>
                  </div>
                  <div class="import-screen-stack">
                    {cards}
                  </div>
                </section>
                """
            ).strip()
        )

    return dedent(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Point93 MVP Clean Import</title>
          <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
          <style>
          {base_css}

          body {{
            background:
              radial-gradient(circle at top left, rgba(37, 99, 235, 0.07), transparent 32%),
              linear-gradient(180deg, #f7f9fc 0%, #eef2f7 100%);
            padding: 48px 32px 80px;
          }}

          .import-header {{
            max-width: 1600px;
            margin: 0 auto 40px;
            padding: 28px 32px;
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(146, 153, 170, 0.24);
            border-radius: 28px;
            box-shadow: 0 20px 40px rgba(19, 28, 54, 0.08);
          }}

          .import-header h1 {{
            margin: 0 0 8px;
            font-size: 34px;
            letter-spacing: -0.04em;
          }}

          .import-header p {{
            margin: 0;
            max-width: 980px;
            font-size: 14px;
            line-height: 1.7;
            color: var(--text-muted);
          }}

          .import-meta-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 18px;
          }}

          .import-chip {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            border-radius: 999px;
            background: var(--surface2);
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
          }}

          .import-section {{
            max-width: 1600px;
            margin: 0 auto 44px;
          }}

          .import-section-header {{
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 24px;
            margin-bottom: 18px;
          }}

          .import-section-kicker {{
            font-size: 11px;
            font-weight: 700;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 8px;
          }}

          .import-section-header h2 {{
            margin: 0 0 6px;
            font-size: 28px;
            letter-spacing: -0.03em;
          }}

          .import-section-header p {{
            margin: 0;
            max-width: 980px;
            font-size: 13px;
            line-height: 1.6;
            color: var(--text-muted);
          }}

          .import-section-count {{
            padding: 10px 14px;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.08);
            color: var(--accent);
            font-size: 11px;
            font-weight: 700;
            white-space: nowrap;
          }}

          .import-screen-stack {{
            display: flex;
            flex-direction: column;
            gap: 24px;
          }}

          .import-card {{
            padding: 20px;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(146, 153, 170, 0.24);
            border-radius: 24px;
            box-shadow: 0 18px 40px rgba(19, 28, 54, 0.08);
          }}

          .import-card-synthesized {{
            border-color: rgba(5, 150, 105, 0.28);
            box-shadow: 0 18px 40px rgba(5, 150, 105, 0.08);
          }}

          .import-card-header {{
            display: flex;
            align-items: start;
            justify-content: space-between;
            gap: 18px;
            margin-bottom: 14px;
          }}

          .import-card-header h3 {{
            margin: 0;
            font-size: 20px;
            letter-spacing: -0.03em;
          }}

          .import-card-kicker {{
            margin-bottom: 6px;
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
          }}

          .import-card-meta {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            align-items: end;
            font-size: 11px;
            color: var(--text-muted);
            text-align: right;
            min-width: 220px;
          }}

          .import-pill {{
            display: inline-flex;
            align-self: end;
            padding: 6px 10px;
            border-radius: 999px;
            background: var(--surface2);
            color: var(--text-muted);
            font-weight: 700;
          }}

          .import-card-note {{
            margin-bottom: 14px;
            padding: 10px 12px;
            border-radius: 12px;
            background: rgba(5, 150, 105, 0.08);
            color: #065f46;
            font-size: 12px;
            line-height: 1.6;
          }}

          .import-card-canvas {{
            padding: 12px;
            overflow-x: auto;
            background:
              radial-gradient(circle at top left, rgba(37, 99, 235, 0.08), transparent 34%),
              linear-gradient(180deg, #f9fbfe 0%, #eef2f7 100%);
            border-radius: 18px;
          }}

          .import-card-canvas > * {{
            min-width: fit-content;
          }}

          .wf-page {{
            margin: 0;
          }}

          @media (max-width: 1200px) {{
            body {{
              padding: 24px 16px 64px;
            }}

            .import-header,
            .import-section {{
              max-width: none;
            }}

            .import-card-header,
            .import-section-header {{
              flex-direction: column;
              align-items: start;
            }}

            .import-card-meta {{
              min-width: 0;
              align-items: start;
              text-align: left;
            }}

            .import-pill {{
              align-self: start;
            }}
          }}
          </style>
        </head>
        <body>
          <header class="import-header">
            <h1>Point93 MVP Clean Import</h1>
            <p>This page strips the original spec chrome away and keeps the actual MVP screen canvases ready for Figma import. It includes 20 wireframed states pulled directly from the HTML archive, plus 3 synthesized My Results screens derived from the blueprint, IA map, and interaction flows because that page exists in the product architecture but was never turned into a dedicated wireframe panel.</p>
            <div class="import-meta-row">
              <div class="import-chip">23 import-ready screens</div>
              <div class="import-chip">12 wireframe panels + 1 synthesized screen family</div>
              <div class="import-chip">Primary sources: Blueprint v1.6.1, Wireframes v1.2, IA Map v2, Flows v1.0</div>
            </div>
          </header>
          {' '.join(section_html)}
        </body>
        </html>
        """
    ).strip() + "\n"


def main() -> None:
    document = html.fromstring(SOURCE_HTML.read_text())
    OUTPUT_HTML.write_text(render_output(document))
    print(f"Wrote {OUTPUT_HTML.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
