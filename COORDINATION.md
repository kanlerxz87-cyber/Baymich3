# COORDINATION.md — Shared task board

Branch used by this session: `arena/db94882d-baymich3` (the session's assigned branch; all work stays on it).

Status legend: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block other tasks)

## Tasks

| ID | Task | Status | Owner (session) | Claimed (UTC) | File scope |
|----|------|--------|-----------------|---------------|------------|
| T1 | Repo review: verify README and repo state, flag irregularities | in progress | db94882d (this session) | 2026-11-24 | `README.md`, `COORDINATION.md`, `data/repo_review.json` |
| T2 | Michelin SF Bay Area data: starred + Bib Gourmand restaurants (official Michelin sources) | in progress | db94882d | 2026-11-24 | `data/restaurants.json` |
| T3 | Hotel ranking by Michelin density | unclaimed | — | — | `data/hotels.json` (not started; needs hotel source data) |
| T4 | Executive summary, questions/answers, suggestions | in progress | db94882d | 2026-11-24 | `data/questions.json`, `data/suggestions.json`, `docs/` |
| T5 | GitHub Pages static site (landing + category subpages) | in progress | db94882d | 2026-11-24 | `docs/`, `scripts/build_site.py` |

No other session has claimed any task at the time of writing. The integration step (merging branches, final re-verification, publishing) is owned by the final integration session; this session currently holds all tasks because it is the only active session on this branch.

## Activity log

- 2026-11-24 — db94882d: Created this board. Repo state at start: only `README.md` ("# Baymich3"), no site, no data, no prior coordination file. Branch `arena/db94882d-baymich3` from `fc288db` ("Initial commit").
- 2026-11-24 — db94882d: Sources identified (see "Sources" below). Note: the instruction referenced `session-<id>/<task>` branch names; the session's assigned branch is used instead, per the session's branch rules.

## Sources (official unless marked)

- Michelin press release, California 2026 — https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026 (Bib Gourmand list with addresses; new stars)
- Michelin Guide article, "Every MICHELIN-Starred Restaurant in California for 2026" — https://guide.michelin.com/en/article/michelin-guide-ceremony/guide-michelin-california (full star list, counts)
- Michelin Guide restaurant pages — `https://guide.michelin.com/us/en/california/<town>/restaurant/<slug>` (address, cuisine, price tier, official website link, hours)

## Irregularities flagged (see `data/repo_review.json` and the Flagged page)

- Third-party lists disagree with Michelin's own list on some one-star names (e.g., State Bird Provisions, San Francisco). Michelin's official list was used; third-party disagreements are logged.
- A third-party page states 3 three-star restaurants in San Francisco; Michelin's official list shows 4 (Atelier Crenn, Benu, Californios, Quince). Michelin list used.
- The instruction asked for branches named `session-<id>/<task>`; the session's assigned branch name is used instead.
