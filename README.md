# SF Bay Area Michelin Guide & Map (2026)

Verified, mobile-friendly dashboard of Michelin-starred, Bib Gourmand, and Recommended restaurants in the San Francisco Bay Area, plus hotels ranked by Michelin density.

**Live site (GitHub Pages):** https://kanlerxz87-cyber.github.io/Baymich3/ (enable Pages → Deploy from branch `main` if not yet enabled; see COORDINATION.md)

## What's here
- `index.html` — landing dashboard
- `restaurants.html` — 41 Core starred + 3 Extension (stars, price for 2, hours, social, sources)
- `listed.html` — Bib Gourmand (~36) + Recommended (86 count + link)
- `hotels.html` — 14 hotels ranked by cluster density
- `map.html` — cluster guide + Michelin map links (no guessed coordinates)
- `executive-summary.html` / `questions.html` / `suggestions.html` / `flagged.html` (irregularity log) / `methodology.html`
- `data/restaurants.csv`, `data/bib.csv`, `data/hotels.csv`, `data/SCOPE.md`
- `docs/` — markdown sources for summary/questions/suggestions
- `COORDINATION.md` — shared task board (parallel sessions)

## Rules
- Edition: MICHELIN Guide California 2026. Scope: 9-county Core + flagged Extension.
- Every row has an official source link. Blank = Unverified (never guessed).
- Price for 2 = per-person × 2 + service charge (formula per row, excl. tax/bev).

## Rebuild data pages
`python3 scripts/build_site.py` regenerates `restaurants.html`, `hotels.html`, `flagged.html`, and the summary/questions/suggestions pages from `data/*.csv` and `docs/*.md`. Edit the CSV or Markdown, then rerun the script. Other pages are hand-maintained.

## Run locally
`python3 -m http.server 8000` then open http://localhost:8000/
