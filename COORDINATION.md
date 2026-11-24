# COORDINATION — shared task board

Created by session `26f06e9a` (branch `arena/26f06e9a-baymich3`, base `fc288db`).
Note: this session works on one branch only (`arena/26f06e9a-baymich3`), so the
`session-<id>/<task>` branch naming is replaced by claims on this branch.

Status values: `unclaimed` · `in progress` · `done` · `needs review`
(`needs review` = published on the Flagged for Review page; does not block other work.)

## Task board

| # | Task | Status | Owner (session) | Files in scope | Notes |
|---|------|--------|-----------------|----------------|-------|
| T1 | Repo review (README, structure, irregularities) | done | 26f06e9a | `docs/flagged.html`, `COORDINATION.md` (this log) | Repo contains only `README.md` (10 bytes) at base commit |
| T2 | Michelin restaurants — SF listing, page 1 of 4 (48 entries) + detail checks | in progress (pages 2–4 open) | 26f06e9a | `data/restaurants.json`, `docs/restaurants.html` | Source: official guide.michelin.com SF listing |
| T3 | Hotels ranked by Michelin density | unclaimed | — | `data/hotels.json`, `docs/hotels.html` | Not started in this session |
| T4 | Social links (YouTube / TikTok / Instagram) | unclaimed | — | `data/social.json` | Not started in this session |
| T5 | Site build (landing + category pages) | done | 26f06e9a | `docs/index.html`, `docs/*.html`, `docs/assets/*` | GitHub Pages from `docs/` |
| T6 | Integration / final re-verification / publish | unclaimed | — | all shared outputs | Reserved for final integration session |

## Log

- **2026-11-24 · 26f06e9a** — Claimed T1, T2, T5 (single-session run). Reason for claim: repo had no coordination file and no other session activity on this branch.
  - Note: "claim is more than 60 minutes old with no commits" rule applies to other sessions; none seen.

- **2026-11-24 · 26f06e9a** — T1 done. T5 built (`scripts/build_site.py` → `docs/`). T2 partial: page 1 of 4 captured (48 entries); 7 detail pages checked (Quince, Californios, Benu, Atelier Crenn, Acquerello, Kiln, Izakaya Rintaro). T3/T4 not started.

## Sources used (T2, verified in this session)

- Official Michelin SF listing: https://guide.michelin.com/us/en/california/san-francisco/restaurants (page 1 of 4, read in full, 48 entries)
- Official Michelin detail pages checked line by line: see `data/restaurants.json` field `verified_detail_url`.

## Irregularities (flagged for review)

See the Flagged for Review page: `docs/flagged.html`.
