# Baymich3 — Bay Area Michelin dashboard

A static dashboard (GitHub Pages, served from `docs/`) for planning Michelin-starred dining, hotels and activities in the San Francisco Bay Area.

- **Live site:** https://kanlerxz87-cyber.github.io/Baymich3/
- **Starred restaurants:** `docs/starred.html` (41 entries, 2026 Michelin California selection)
- **Questions, suggestions, flags, sources:** see the site navigation.

## Rules used
- Every table row links to an official source (Michelin guide pages or the restaurant's own site).
- If a value cannot be confirmed from an official source, it is left blank and marked **Unverified**. Nothing is inferred.
- Michelin lists price as $ levels only, so no couple total is entered without a published figure.

## Files
- `docs/data/data.js` — verified data registry (edit here)
- `docs/data/content.js` — summary, questions, suggestions, flags
- `docs/assets/` — stylesheet and renderer (no build step)
- `COORDINATION.md` — task board, verification log, repo review, flagged items

## Local preview
`cd docs && python3 -m http.server 8080`, then open http://localhost:8080.
