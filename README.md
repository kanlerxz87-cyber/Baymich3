# SF Bay Area Michelin Guide & Map (2026)

Verified, mobile-friendly dashboard of Michelin-starred, Bib Gourmand, and Recommended restaurants in the San Francisco Bay Area, plus an unranked hotel-candidate directory grouped by restaurant cluster.

**Live site (GitHub Pages):** https://kanlerxz87-cyber.github.io/Baymich3/ (deployed from `main`; see COORDINATION.md for verification)

## Regenerate the site
All HTML is generated from the CSVs, so it can never drift from the data:
`python3 tools/build_site.py` (data repairs: `tools/fix_data.py`, `tools/fix_bib.py`, `tools/fix_hotels.py`).

## What's here
- `index.html` — landing dashboard (all counts computed from the CSVs)
- `restaurants.html` — 41 Core starred + 3 Extension (stars, price for 2, hours, social, sources, per-row verification badge)
- `listed.html` — Bib Gourmand (36 rows, per-city Michelin citation) + Recommended (86 count + link)
- `hotels.html` — 14 unranked hotel candidates grouped by broad restaurant cluster; not proximity scores
- `map.html` — cluster guide + Michelin map links (no guessed coordinates)
- `executive-summary.html` / `questions.html` / `suggestions.html` / `flagged.html` (irregularity log) / `methodology.html`
- `data/restaurants.csv`, `data/bib.csv`, `data/hotels.csv`, `data/SCOPE.md`
- `tools/` — `build_site.py` (generator) and the three data-repair scripts
- `docs/` — markdown sources for the text pages (summary, questions, suggestions, flagged, method)
- `COORDINATION.md` — shared task board (parallel sessions)

## Rules
- Edition: MICHELIN Guide California 2026. Scope: 9-county Core + flagged Extension.
- Every row has an official source link. Blank = Unverified (never guessed).
- Price for 2 = per-person × 2 + service charge (formula per row, excl. tax/bev).

## Contributing
Edit the CSV or the Markdown, never the HTML — the HTML is output. There is exactly one generator (`tools/build_site.py`); run it and commit both the data and the regenerated pages.

## Run locally
`python3 -m http.server 8000` then open http://localhost:8000/
