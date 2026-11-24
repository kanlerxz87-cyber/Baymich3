# Bay Area MICHELIN Guide

A mobile-friendly, source-conscious 2026 planning dashboard for MICHELIN restaurants, hotels, clusters, and trip research in the San Francisco Bay Area and nearby destination regions.

## Pages

- `index.html` — dashboard landing page and executive snapshot
- `restaurants.html` — starred restaurants
- `bib-gourmand.html` — Bib Gourmand inventory (partial; flagged)
- `green-star.html` — Green Star restaurants
- `hotels.html` — candidate hotels and provisional ranking method
- `map.html` — approximate city/cluster map
- `executive-summary.html` — decision brief
- `questions.html` — open questions and missing inputs
- `suggestions.html` — options for future improvement, separate from implementation
- `verification.html` — evidence standards and known gaps
- `flagged.html` — irregularities for review
- `sources.html` — primary/secondary sources and geography definitions

## Run locally

Static HTML; open `index.html` or serve the repository root with any static web server. The map loads Leaflet and OpenStreetMap tiles from external hosts.

## Publish with GitHub Pages

A GitHub Actions workflow is included at `.github/workflows/pages.yml`. It deploys from `main` after a push or manual workflow dispatch. Enable GitHub Pages in repository settings with **GitHub Actions** as the build/deploy source. The current working branch is `arena/08e177e6-baymich3`; deployment occurs only after the changes land on `main` through the project's integration process.

## Data integrity

- Selection statuses use MICHELIN primary sources; exact menu totals and business details require official restaurant sources.
- Unconfirmed values remain blank and are called out on the Flagged for Review page.
- Benu is the only restaurant with an exact total for two currently verified from its official site: $1,037 before tax/drinks (two $425 menus plus 22% service).
- Hotel rankings and Bib completeness remain provisional and explicitly flagged. Do not treat the current working count as a complete census.

See `COORDINATION.md` for the project task board and `verification.html` for data policy.
