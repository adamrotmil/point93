# Point93 Shadcn Lab

This app rebuilds the Point93 dashboard with real `shadcn/ui` components instead
of the static browser-lab HTML snapshots.

## Run locally

```bash
npm install
npm run dev
```

Then open the local Vite URL, typically:

```text
http://127.0.0.1:5173/
```

## Purpose

- keep the same broad product structure as the current prod dashboard
- swap raw page markup for reusable component building blocks
- make future visual iteration happen through tokens and components rather than
  one-off CSS overrides
- give us a path to expand from `Dashboard` into other screens using the same
  system
