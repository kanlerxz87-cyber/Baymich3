# COORDINATION — Shared Task Board

Repo: `kanlerxz87-cyber/Baymich3` · Project: SF Bay Area Michelin guide, map, hotels, and review site.

## Session rules used in this repo

- **Branch rule:** this session works only on its assigned branch `arena/401d224f-baymich3` (branched from `main` @ `fc288db`). Work is not split into `session-<id>/<task>` branches, because the session is locked to one branch. Task claims are recorded here instead.
- Status values: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).
- Verification standard: every table row needs a source link to an official site. A value that cannot be confirmed from an official source is left blank and flagged `UNVERIFIED`. Nothing is inferred or filled in.
- Shared outputs (site index and navigation, combined data) are finalized in the integration step at the end of this session.

## Task board

| ID | Task | Status | Owner (session) | Files in scope | Notes |
|----|------|--------|-----------------|----------------|-------|
| T0 | Create coordination board | done | `401d224f` | `COORDINATION.md` | Created in this session. |
| T1 | Repo review (line by line) + irregularities | in progress | `401d224f` | `docs/review.html`, `data/flags.json` | See Irregularities log. |
| T2 | Michelin Bay Area starred restaurants (detail-page verification) | in progress | `401d224f` | `data/restaurants_starred.json` | Source: guide.michelin.com detail pages. |
| T3 | Michelin Bib Gourmand + Selected restaurants (Bay Area) | unclaimed | — | `data/restaurants_bib.json` | Official listing: `/restaurants/bib-gourmand` (30 SF & surroundings). Not started. |
| T4 | Hotels in Bay Area + Michelin Keys + ranking | unclaimed | — | `data/hotels.json` | Needs official hotel listing + coordinates. Not started. |
| T5 | Social links (YouTube / TikTok / Instagram) per row | unclaimed | — | `data/social_links.json` | Must come from the venue's official website or verified account. |
| T6 | Exact menu pricing per restaurant (couple of 2 adults) | unclaimed | — | `data/prices.json` | Michelin shows price *category* only; exact prices need the venue website. |
| T7 | Questions, missing information, and suggestions | in progress | `401d224f` | `docs/questions.html`, `docs/suggestions.html` | Suggestions need owner approval before any implementation. |
| T8 | GitHub Pages site (landing + category subpages) | in progress | `401d224f` | `docs/` | Integration step. |

## Claims log

- 2026-11-24 · `401d224f` · claimed T0–T2, T7, T8 (and T1). Scope listed above. Commit: see git log.

## Handoff rule

If a claim is older than 60 minutes with no commits, any other session may take over and must note the handoff below.

## Handoffs

_None yet._

## Irregularities log

Logged in `docs/review.html` and `data/flags.json`. Summary:

1. Michelin press releases give different totals for the 2026 California selection: michelin.com says **523** eateries; michelinmedia.com says **521**. Unresolved; flagged.
2. Michelin's guide lists the Bay Area under **"San Francisco and surroundings"** (145 entries). That grouping does not match the 9-county Bay Area, so counts from the two sources differ.
3. Michelin press pages are dated June 24 (ceremony) and June 26 (michelin.com page), 2026. Both are recorded.
4. Michelin price levels ($–$$$$) are categories, not dollar amounts. Exact prices are therefore not verified.
5. The SFist "michelin-guide" tag page carries a 2018 date in its metadata, so it was not used as a source.
6. The repository contains only `README.md` (`# Baymich3`). It has no license, no `.gitignore`, and no description.

## Sources

Primary (official):
- Michelin Guide California 2026 press release: https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026
- Michelin North America newsroom (June 24, 2026): https://michelinmedia.com/pages/blog/detail/article/c0/a1474/
- Michelin Guide, San Francisco & surroundings listing: https://guide.michelin.com/us/en/california/san-francisco/restaurants
- Michelin Guide, Bib Gourmand (SF & surroundings): https://guide.michelin.com/us/en/california/san-francisco/restaurants/bib-gourmand
- Michelin Guide, California listing: https://guide.michelin.com/us/en/california/restaurants

Secondary (cross-check only, not used as the source for any row):
- San Francisco Chronicle, June 25, 2026 star list: https://www.sfchronicle.com/food/restaurants/article/2026-michelin-stars-of-bay-area-22317064.php
- SFist, June 25, 2026: https://sfist.com/2026/06/25/californios-elevated-to-three-michelin-stars-wolfsbane-and-naides/
