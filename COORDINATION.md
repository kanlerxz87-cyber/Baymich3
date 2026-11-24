# COORDINATION.md — Shared Task Board

> **Purpose:** Coordinate parallel agent sessions working on this repo to avoid conflicts and duplicate work.
> **Rule:** Claim a task by writing your session ID and file scope below, then commit and push that claim immediately. Never start a task another session has claimed. Keep scopes non-overlapping. If a task requires changing a file owned by another session, log the request here instead of editing it.

## Sessions

| Session ID | Branch | Status | Scope (files owned) | Last commit |
|---|---|---|---|---|
| `arena/08e177e6-baymich3` | `arena/08e177e6-baymich3` | **in progress** | `COORDINATION.md`, `README.md`, `index.html`, `restaurants.html`, `bib-gourmand.html`, `green-star.html`, `hotels.html`, `map.html`, `executive-summary.html`, `questions.html`, `suggestions.html`, `verification.html`, `flagged.html`, `sources.html`, `assets/*`, `data/*`, `.github/workflows/pages.yml` | — (claim commit) |

## Task Board

| # | Task | Status | Owner | Files touched | Sources / verification | Irregularities |
|---|---|---|---|---|---|---|
| 1 | Repo review + coordination setup | done | arena/08e177e6-baymich3 | COORDINATION.md, README.md | Repo had only README.md (10 bytes) at fc288db | None |
| 2 | Michelin starred restaurants (2026) — verified table | in progress | arena/08e177e6-baymich3 | restaurants.html, data/restaurants.json | MICHELIN Guide California 2026 official ceremony page (guide.michelin.com) + michelin.com 2026 release | Sacramento inclusion flagged — see Flagged page |
| 3 | Bib Gourmand + Green Star (2026) — verified tables | in progress | arena/08e177e6-baymich3 | bib-gourmand.html, green-star.html, data/restaurants.json | guide.michelin.com affordable list 2026; michelin.com 2026 Bib list; guide.michelin.com Green Star filter | Green Star phase-out in 2026 flagged |
| 4 | Hotel ranking by Michelin proximity (methodology + table) | in progress | arena/08e177e6-baymich3 | hotels.html, data/hotels.json | MICHELIN Key hotels 2024/2025 official guide.michelin.com; cluster counts from Task 2 | Distances are cluster-based estimates, not surveyed — flagged |
| 5 | Cluster map (Leaflet / OSM, no API key) | in progress | arena/08e177e6-baymich3 | map.html, assets/app.js | Coordinates are city-level centroids for clustering, not exact addresses — flagged | Exact addresses require per-restaurant verification |
| 6 | Pricing (2 adults, total) — verified only | in progress | arena/08e177e6-baymich3 | restaurants.html (pricing column), verification.html | Official restaurant sites only (e.g. benusf.com/info for Benu). Blank = unverified | Most prices not published on official sites — left blank per no-hallucination rule |
| 7 | Hours / days open / exceptions + official links + social search links | in progress | arena/08e177e6-baymich3 | restaurants.html, bib-gourmand.html | Official site links from MICHELIN Guide listings; hours blank unless verified | Social links are search links, not direct video IDs — flagged |
| 8 | Executive summary | in progress | arena/08e177e6-baymich3 | executive-summary.html | Derived from Tasks 2–4 counts | — |
| 9 | Open questions / missing info + discovery suggestions | in progress | arena/08e177e6-baymich3 | questions.html | — | — |
| 10 | Site improvement suggestions + decision matrix | in progress | arena/08e177e6-baymich3 | suggestions.html | — | No changes implemented without review per brief |
| 11 | Verification log (line-by-line) + Flagged for Review | in progress | arena/08e177e6-baymich3 | verification.html, flagged.html, sources.html | Every row links to official source or is flagged unverified | — |
| 12 | GitHub Pages publish + link check | pending | arena/08e177e6-baymich3 | .github/workflows/pages.yml, all html | — | Requires Pages enabled in repo settings |

## Status legend
- `unclaimed` — no owner
- `in progress` — claimed, work ongoing
- `done` — finished, sources recorded
- `needs review` — published on Flagged for Review page; does not block other work

## Handoff / takeover log
- (none yet)

## Merge-conflict log
- (none yet)

## Change requests (file owned by another session)
- (none yet)
