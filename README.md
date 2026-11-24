# Bay Area Michelin Field Guide

A lightweight, mobile-friendly, source-first dashboard for Michelin dining, hotel-cluster planning, activities and unresolved decisions in the San Francisco Bay Area.

## Pages
- `index.html` — executive summary and navigation
- `restaurants.html` — 2026-starred shortlist; unsupported price, hour and social fields intentionally remain blank
- `stays.html` — hotel-cluster comparison framework; no unsupported price/ranking claims
- `activities.html` — empty pending verified activities
- `questions.html` — decision inputs and suggested paths
- `review.html` — audit flags and source limitations

## Run locally
Open `index.html` in a browser or serve this directory with any static HTTP server.

## Publish
`.github/workflows/pages.yml` deploys the repository root to GitHub Pages on pushes to the current Arena branch and supports manual dispatch. The repository's GitHub Pages setting must allow GitHub Actions deployment. A workflow file alone does not guarantee that Pages is enabled or the deployment succeeded; check the repository Actions/Pages settings and workflow run.

## Source and limitations
Current star claims in the table are based on Michelin's official 2026 California selection: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california. Michelin states the selection was revealed June 24, 2026. The source is an edition-specific announcement, not a live feed and not a substitute for each venue's menu, hours, booking terms or social pages. No price, opening schedule, hotel rate, distance count or social account has been inferred. See `review.html` before using this as a booking itinerary.
