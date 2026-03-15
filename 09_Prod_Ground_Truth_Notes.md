# Point93 Prod Ground Truth Notes

Captured on 2026-03-15 from the live logged-in prod app at `https://point93.ai` using the active Chrome session cookie.

## Source artifacts

- Route manifest: `Point93/prod_snapshot_exports/manifest.json`
- HTML snapshots: `Point93/prod_snapshot_exports/*.html`
- Screenshots: `Point93/prod_snapshot_exports/*.png`
- Capture script: `Point93/scripts/capture_point93_prod_routes.cjs`

## What prod says now

- The current product has a stronger, simpler IA than the older concept archive.
- The primary user-facing navigation is:
  - Dashboard
  - Assessments
  - Insight Areas
  - Data Points
  - Scores
  - Reports
  - Business Intelligence
- Admin lives in the same shell:
  - Area Builder
  - BI Builder
  - AI Hub
  - Graph View
  - User Management
  - Analytics
  - Feedback
  - Beta

## Key route mapping

- `/dashboard`
  - Welcome/orientation shell
  - Start assessment card
  - Recommended next modules
  - Right rail with score, BI, coming soon, strengths, insight areas
- `/my-journey`
  - This is effectively the current Assessments landing page
  - Organized by 6 major areas with progress and jump links
- `/insight-areas`
  - Replaces part of the older “My Areas” thinking with a flatter, clearer inventory view
- `/data-points`
  - Dedicated inventory for granular assessment signals
- `/scores`
  - Feels like the practical replacement for much of the older “My Results” concept
  - Structured by area, then module, then linked insight areas
- `/reports`
  - Download/report surface with strong empty-state behavior
- `/business-intelligence`
  - BI landing with profile cards and descriptions
- `/business-intelligence/:id`
  - BI detail flow with stages/questions inside the same shell

## Most important product shifts vs. the older design archive

- `My Results` is no longer a single big narrative hub.
  - In prod, that idea has been split into `Scores`, `Insight Areas`, `Data Points`, and `Reports`.
- `My Areas` is no longer the dominant framing.
  - Prod uses `Insight Areas` as a clearer analytical index.
- `Assessments` is more operational than conceptual.
  - The current experience is a progress-driven journey page with areas, modules, and direct CTAs.
- `Business Intelligence` is much more concrete.
  - It exists as both a landing page and profile detail flow, not just a conceptual future state.
- The dashboard is more useful than the earlier spec version.
  - It prioritizes “start”, “recommended next”, and operational progress over abstract storytelling.

## UX implications for our redesign work

- We should use prod IA as the main structural source of truth for the user-facing app.
- The old archive is still useful for broader ambition and feature intent, but not for exact page structure.
- The cleanest path is likely:
  - keep prod routes and content hierarchy
  - restyle the current shell with the new restrained premium system
  - simplify density and card logic where prod still feels busy
  - explore aesthetics on top of live prod skeletons, not the older concept set

## Immediate design recommendation

Use these prod screens as the baseline exploration set:

- Dashboard
- Assessments (`/my-journey`)
- Scores
- Business Intelligence landing
- One BI detail page

These appear to be the highest-leverage screens for aligning the current built product with the new aesthetic direction.
