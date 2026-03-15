# Point93 Browser Restyle Lab

This lab uses the captured prod snapshots as an exact visual baseline and then layers pure CSS overrides on top in the browser.

## Run locally

From the repo root:

```bash
python3 -m http.server 8130
```

Then open:

```text
http://127.0.0.1:8130/Point93/browser-lab/
```

## Workflow

- `Prod Exact` keeps the captured prod HTML untouched.
- Theme presets inject CSS into the same DOM.
- `Custom CSS` lets us try quick overrides live without rebuilding.
- When a direction feels right, we can turn it into a cleaner coded prototype or push selected states into Figma.
- `Component Study · Metric Card` is the first card-first study surface. It isolates one dashboard metric card and shows source, iterations, a chosen direction, and a context row for the next component pass.
