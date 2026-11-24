# Coordination board

| Task | Status | Owner session | File scope |
|---|---|---|---|
| Integrated Bay Area Michelin guide site: source audit, data, dashboard, verification and deployment config | needs review | 46b28920 | all project files |

## Log
- 2026-11-24 — Claimed integrated build as the only listed task. Repository was otherwise empty except for README.md; no other task claims or concurrent changes found. Scope is this branch only, consistent with the session branch restriction.
- 2026-11-24 — Implemented static dashboard, restaurant roster, hotel-cluster method, activity placeholder, decision questions, review flags, and Pages workflow. Official Michelin 2026 selection article fetched and used for the star roster; its 3-star, 2-star and 1-star lists were checked against the official text. The Michelin individual Benu listing was opened and confirms three stars, city, venue URL, Michelin price tier and posted hours; the restaurant-price-for-two field remains blank because Michelin's tier is not an exact total. Other roster entries link to individual official Michelin listings, while hours/prices/social fields remain blank pending entry-by-entry checks. Verified internal page references with an HTML parser and `git diff --check`; no broken local references found. Status is needs review because restaurant-by-restaurant price/hours/social checks, complete non-star Guide coverage, definitive regional boundary, hotel rates/rankings and activity research remain unresolved and are documented on Review Flags / Open Questions. Sources: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california and https://guide.michelin.com/ca/en/california/san-francisco/restaurant/benu .
