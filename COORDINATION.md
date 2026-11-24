# Coordination board

> Shared task board for this repository. Keep file scopes non-overlapping, record source/verification notes, and flag anything that cannot be confirmed from an official source. Current Arena branch is the session identifier because no separate session ID was supplied.

## Tasks

| Task | Status | Owner / session | Files in scope | Notes |
|---|---|---|---|---|
| Bay Area Michelin guide site: research, source-backed dataset, UI, QA, GitHub Pages setup | in progress | `arena/4e9ed8f1-baymich3` | `COORDINATION.md`, `README.md`, site/data/docs/workflow files created by this session | Sole active task; this session acts as final integrator because the board was absent and no other work was claimed. |
| Independent content/source audit | unclaimed | — | To be assigned | Verify official source links, status/date labels, missing fields, and flagged items. |
| GitHub Pages deployment check | unclaimed | — | To be assigned | Confirm repository Pages settings/workflow and live URL after publication. |

## Work log

- Initial checkout: `fc288dbe429ddecaba7f1d0b98971eac9df0ab65` (`main`); clean worktree. No coordination file or prior task claims existed.
- Claim created before implementation. Research/verification prefers Michelin Guide and official venue/hotel sources. Any unconfirmed prices, schedules, social profiles, or operating details remain blank or explicitly flagged.
- Research source set: official 2026 California starred list (https://guide.michelin.com/ca/en/article/michelin-guide-ceremony/guide-michelin-california); live SF-and-surroundings directory (https://guide.michelin.com/us/en/california/san-francisco/restaurants); 2026 U.S. Key hotel article (https://guide.michelin.com/en/article/travel/all-the-key-hotels-united-states); official venue menu/visitor pages linked in `site/data/restaurants.json` and `site/restaurants.html`; official hotel profiles linked in `site/hotels.html`.
- Site implementation added under `site/`, with responsive dashboard, category pages, row table, filters, source/caveat page, and Pages workflow. 32 2026 starred Bay Area records (5 three-star including Sonoma, 7 two-star, 20 one-star) were entered from the statewide 2026 article. This intentionally differs from the older live directory snapshot of 145 (29 starred + 30 Bib Gourmand + 86 Selected); investigate/refresh category totals before representing them as one reconciled current count.
- Price verification: official venue pages confirm menu prices for Benu, Commis, Birdsong, Kiln, Lazy Bear, 7 Adams, Angler SF, and Madcap; calculated menu totals exclude tax/beverages as stated. Other totals blank/unverified. Verified source URLs cited beside rows. Social source verified only for 7 Adams official Instagram link.
- QA run: parsed JSON, confirmed 32 rows, every row links to official 2026 Michelin selection source and carries a cost/status caveat. Not yet run browser QA, external URL validation, build/deployment, nor independent content audit. Workflow still requires Pages enabled with GitHub Actions in repository settings.
