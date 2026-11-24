# COORDINATION.md — Shared task board

Repo: `kanlerxz87-cyber/Baymich3` · Scope: SF Bay Area MICHELIN restaurants, hotels, and a verified GitHub Pages site.

**Session ID:** `15830ac4` (branch `arena/15830ac4-baymich3`).
This session works on its single assigned branch, as its instructions require. The `session-<id>/<task>` naming in the parallel-session protocol was not used, because the session is pinned to its branch name.

**Status values:** `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block other work).

**Rule:** Every table row needs a source link to an official site. If a value cannot be confirmed from an official source, leave it blank and flag it as unverified. Never infer or fill in values.

---

## Task board

| ID | Task | Status | Owner (session) | Files / scope | Notes |
|----|------|--------|-----------------|---------------|-------|
| T0 | Repo review (README, structure, git state, irregularities) | done | 15830ac4 | `README.md`, `COORDINATION.md` | See Log, entry 2026-11-24 (T0). |
| T1 | Verify SF city MICHELIN starred restaurants (1★–3★) on official guide.michelin.com pages | done | 15830ac4 | `docs/data/starred-sf.json` | 25 of 25 verified. See Log. |
| T2 | Verify Bay Area starred restaurants **outside** SF city proper on official Michelin pages | unclaimed | — | `docs/data/starred-bay-area-other.json` | 16 names identified from press only; official pages not yet fetched. |
| T3 | Bib Gourmand and Michelin "Selected" lists for SF Bay Area | unclaimed | — | `docs/data/bib-*.json` (new) | Not started. |
| T4 | Hotels: list Michelin hotels and rank by Michelin restaurants nearby | unclaimed | — | `docs/data/hotels*.json` (new) | Not started. |
| T5 | Real verified pricing for two adults (restaurant's own official menu/prices) | unclaimed | — | `docs/data/starred-sf.json` (cost fields only) | Official Michelin pages show a price tier only, not menu prices. |
| T6 | YouTube / TikTok / Instagram links per restaurant or activity | unclaimed | — | new `docs/data/social-*.json` | Not started. |
| T7 | Activities list (things to do) with official links and hours | unclaimed | — | new `docs/data/activities*.json` | Not started. |
| T8 | Site build: landing page, category subpages, flagged-for-review page, GitHub Pages publish | released | — (15830ac4 released its claim) | `docs/**` | Released 2026-11-24 after finding the same task claimed on other branches (see "Cross-branch overlap"). Not built on this branch. |
| T9 | Final integration: merge branches, re-verify combined data, check links, publish Pages | unclaimed | — | `docs/**`, `COORDINATION.md` | Reserved for a final integration session once T2–T7 are done. |

Scope notes: `docs/**` is shared output. Only the integration session (T9) may change the site index and navigation after other tasks finish. This session is currently making the initial version of it because it owns T8.

---

## Log

### 2026-11-24 · T0 Repo review · session 15830ac4
- Repo state on arrival: branch `arena/15830ac4-baymich3` from `main` commit `fc288db` ("Initial commit"). Working tree clean.
- Files present: `README.md` only (content: `# Baymich3`). No license, no code, no data, no CI config, no existing `COORDINATION.md`.
- Remote: `origin` = `https://github.com/kanlerxz87-cyber/Baymich3.git`. `gh` authenticated as `kanlerxz87-cyber`.
- **Irregularities flagged:**
  1. README has no description, scope, or how-to; nothing in the repo yet explains the project.
  2. No `COORDINATION.md` existed; created by this session.
  3. The protocol's `session-<id>/<task>` branch naming conflicts with the session branch rule (`arena/<session>`); the session branch rule was followed.
  4. No GitHub Pages configuration exists yet in the repo.
- Verification sources for this review: `https://github.com/kanlerxz87-cyber/Baymich3` (repo), `git log` output in the sandbox.

### 2026-11-24 · T1 SF starred restaurants · session 15830ac4
- Star list cross-checked against: Eater SF "2026 Michelin Star Winners of the Bay Area" (https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area) and SF Standard (https://sfstandard.com/2026/06/25/californios-three-star-michelin-restaurant/). Ceremony date: June 24, 2026 (SF Standard).
- Each of the 25 San Francisco entries was then checked on its official Michelin page (`guide.michelin.com/us/en/california/san-francisco/restaurant/<slug>`), which shows star count, address, cuisine, price tier, and weekly hours.
- **Irregularities flagged:**
  1. Kiln: the default slug `/kiln` resolves to a **London** restaurant. The SF Kiln is `/kiln-1210355` (149 Fell St.). Anyone using the default slug gets the wrong restaurant.
  2. Mister Jiu's: the live slug (`/mister-jius`) did not load in this session. Official data came from a different-locale Michelin page indexed by search (`guide.michelin.com/vn/en/...`, 2025-era data) plus Eater/SF Standard for 2026 status. Hours and address reconfirmation pending.
  3. Nisei: the official page shows no hours block. Left blank.
  4. Press lists disagree with each other (the europesays.com copy of the 2026 list omits Angler, 7 Adams, Kin Khao, Nari, Nisei, Sorrel and Ssal). Official pages were used for every row.
  5. Eater's Bay Area list includes Harbor House Inn (Elk) and Aubergine / Chez Noir (Carmel-by-the-Sea), and Sacramento restaurants, which fall outside the SF Bay Area. Excluded from the Bay Area table.
  6. Removed from SF 1★ in 2026 per press (not yet verified officially): Le Comptoir at Bar Crenn, O' by Claude Le Tohic, Shota.
- Verification: 25/25 SF rows have an official Michelin page link. Cost for two is left blank because official pages do not show menu prices.

### 2026-11-24 · Cross-branch overlap · session 15830ac4
- Reading the other `arena/*` branches on origin showed at least seven sessions with overlapping claims on this same repo: `arena/0cfb07d3`, `arena/26f06e9a`, `arena/401d224f`, `arena/612cf61c`, `arena/8bc23e0f`, `arena/db94882d`, plus `arena/08e177e6`, `arena/230df0ee`, `arena/35713f68`, `arena/3c9252ca`, `arena/401d224f`.
- Overlap by task:
  - **Repo review (T0):** claimed or done on `26f06e9a`, `401d224f`, `8bc23e0f`, `db94882d`.
  - **Michelin SF / Bay Area dataset (T1–T2):** claimed on `8bc23e0f`, `26f06e9a`, `401d224f`, `612cf61c`, `db94882d`.
  - **Site shell (T8):** `26f06e9a` reports done; `8bc23e0f`, `612cf61c`, `db94882d`, `401d224f` in progress.
  - **Hotels (T4 here):** `0cfb07d3` partial (31-hotel roster); others unclaimed.
  - **Social links / activities:** `401d224f` and `0cfb07d3` (released) and others.
- Action taken by 15830ac4: the site-shell claim (T8) was released. The verified San Francisco dataset (T1) is kept. T2–T7 were not started here.
- Recommendation to the user and integration session: pick one branch as the integration owner. Merge the verified rows from each branch, and resolve any conflicts on `docs/data/` vs `data/` paths. Re-verify every row against the official URL before publishing.
- Path note: this session's data lives at `docs/data/starred-sf.json`. Other branches use `data/` or `docs/data/` with different schemas. The integration session should choose one schema.

### Claims (current)
- 2026-11-24 · 15830ac4: **T1 done** (SF starred, 25 rows verified). **T8 released.** T2–T7 unclaimed on this branch.
