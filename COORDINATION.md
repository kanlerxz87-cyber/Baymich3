# Coordination Board — Baymich3 (SF Bay Area Michelin Guide & Map)

**Branch:** `arena/3c9252ca-baymich3` (branched from `main` @ `fc288db`)
**Session:** `baymich3-session` (single session; no other sessions active)
**Convention:** claim a task by writing this session ID + file scope; mark status; commit + push the claim before starting work. Never start a task another session has claimed.

## Tasks

| # | Task | Status | Session | Files touched | Sources / verification |
|---|------|--------|---------|---------------|------------------------|
| 1 | Research SF Bay Area Michelin restaurants (official guide.michelin.com): names, star vs listed, cuisine, district, address, official URL | in progress | baymich3-session | `data/restaurants.json`, `docs/restaurants.md` | guide.michelin.com |
| 2 | Research hotels near Michelin clusters; rank by number of Michelin restaurants nearby | unclaimed | baymich3-session | `data/hotels.json`, `docs/hotels.md` | hotel official sites, michelin.com |
| 3 | Build GitHub Pages site: landing page + category subpages, dashboard-style tables, executive summary | unclaimed | baymich3-session | `docs/index.html`, `docs/*.html`, `assets/*` | — |
| 4 | Add per-row source links; flag unverified values; leave blanks where unconfirmed | unclaimed | baymich3-session | all data/docs files | official sources per row |
| 5 | Executive summary, suggestions section, open questions/information/answers section | unclaimed | baymich3-session | `docs/executive-summary.md`, `docs/suggestions.md`, `docs/questions.md` | — |
| 6 | Verify every table row line by line against official sources; fix irregularities | unclaimed | baymich3-session | all | official sources |
| 7 | Integrate branches, re-verify combined data, confirm build with no broken links, publish to GitHub Pages | unclaimed | baymich3-session | all | — |

## Rules
- No manual input from the user; work autonomously line by line.
- No hallucinations: if a value cannot be confirmed from an official source, leave blank + flag "unverified".
- Every table row must carry a source link to an official site.
- Small, frequent commits; `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding other session's work, log it here.

## Log
- 2026-11-24: COORDINATION.md created; session `baymich3-session` claiming all tasks on branch `arena/3c9252ca-baymich3`. Repo initially empty (README only).
