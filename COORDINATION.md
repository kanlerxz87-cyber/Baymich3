# COORDINATION.md — Shared Task Board

> **Purpose:** Coordinate parallel agent sessions on this repo.
> **Rule:** Claim a task by writing your session ID and file scope here, commit and push the claim, then work. Never start a task another session has claimed.

## Branch note

Arena sessions are bound to one branch each. This session (`bc5ad36e`) works **only** on
`arena/bc5ad36e-baymich3`, so the `session-<id>/<task>` naming in the brief is replaced by
claims on this branch. Nothing is merged from other `arena/*` branches; they were read-only
checked (no `COORDINATION.md` claims overlap the tasks below).

## Task board

| # | Task | Status | Owner (session) | Files in scope | Notes |
|---|------|--------|-----------------|----------------|-------|
| T1 | Repo review (README, structure, irregularities) | done | bc5ad36e | `COORDINATION.md`, `docs/flagged.html` | Repo held only `README.md` (10 bytes) at base `fc288db`. No build tooling, no data. |
| T2 | Michelin restaurants — SF listing (official) + Bay Area Bib list + 2026 stars | needs review | bc5ad36e | `docs/data/data.js`, `docs/restaurants.html`, `docs/bib-gourmand.html` | 57 of 145 listing entries captured; 4 of 7 unlocated star/Bib entries flagged; hours verified for 7 only |
| T3 | Hotels — Michelin Keys + guest score (official index) | needs review | bc5ad36e | `docs/hotels.html` | 18 of 31 hotels captured. Proximity-to-restaurants ranking NOT done (no verified coordinates) |
| T4 | Social links (YouTube / TikTok / Instagram) | needs review | bc5ad36e | `docs/restaurants.html` (social column) | No verified social handles captured. Search helper links only, clearly labeled unverified |
| T5 | Site build (landing, category pages, summary, questions, suggestions, verification, flagged) | in progress | bc5ad36e | `docs/*.html`, `docs/assets/*`, `docs/data/*` | Static site in `docs/` (GitHub Pages source folder) |
| T6 | Integration / final re-verification / publish | unclaimed | — | all shared outputs | Reserved for the final integration session |

## Status legend
- `unclaimed` — no owner
- `in progress` — claimed, work ongoing
- `done` — finished, sources recorded
- `needs review` — published on the Flagged for Review page; does not block other work

## Sources used (this session, all official)

- Michelin SF listing (official): https://guide.michelin.com/us/en/california/san-francisco/restaurants (pages 1 and 2 read; page 2 partly)
- Michelin SF listing page 2: https://guide.michelin.com/us/en/california/san-francisco/restaurants/page/2
- Michelin detail pages opened: Quince, Californios, Benu, Atelier Crenn, Acquerello, Wolfsbane, Restaurant Naides (hours, address, website, price tier)
- Michelin hotels index (Bay Area): https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area (chunks 0–3 read; 18 hotels)
- Michelin press release, MICHELIN Guide California 2026 (26 Jun 2026): https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026 (full statewide Bib list, new stars, Green Star names)

## Verification performed

- Every restaurant row links to its official Michelin listing URL (taken from the official listing page). Hours, address and website were only filled where the official detail page was opened.
- Bay Area Bib Gourmand rows come from the official 2026 press release table (address per row).
- Blank cell = not verified. Blank values are flagged on the Flagged for Review page.

## Irregularities (flagged for review)

See `docs/flagged.html`. Key items:
1. Listing facets say 2 Stars = 7 and 1 Star = 18 for "San Francisco and surroundings" but only 6 and 15 were visible in the pages captured. The missing names are flagged, not guessed.
2. Michelin's listing sort is not strictly by distinction across pages (page 2 starts with "Selected" entries).
3. Price tier ($–$$$$) is the only Michelin price field. Price-for-two is not published on Michelin pages and was not found on official restaurant sites in this session, so it is blank.
4. Social links are not verifiable from the sources used. Search helper links only.
5. The brief's "Bay Area" scope is ambiguous (Michelin's SF listing vs. the 9-county Bay Area). Both are shown, labeled.

## Handoff / takeover log
- 2026-11-24 · bc5ad36e: Claimed T1–T6 on this branch. Built first-pass verified dataset and static site in `docs/`.

## Merge-conflict log
- (none)

## Change requests (file owned by another session)
- (none)
