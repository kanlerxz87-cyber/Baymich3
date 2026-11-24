# COORDINATION.md — Shared Task Board

Session ID: `88da5baf` (branch: `arena/88da5baf-baymich3`)
Last updated: 2026-11-24

## Rules
- Claim a task by writing session ID + file scope, commit + push immediately.
- Never start a task another session has claimed.
- Keep scopes non-overlapping.
- Small frequent commits, `git pull --rebase` before push.
- Never mark verified without official source link.
- Shared outputs (data + site index/nav) changed only by final integration session.
- If claim >60 min old with no commits, may be taken over with handoff note.

## Tasks

| ID | Task | Status | Owner Session | Files Touched | Sources / Verification | Irregularities |
|----|------|--------|---------------|---------------|------------------------|----------------|
| T1 | Michelin restaurants (stars + listed) — SF Bay Area | in progress | 88da5baf | data/restaurants.csv, data/restaurants.md | guide.michelin.com (official) | — |
| T2 | Pricing for 2 adults (verified only) | in progress | 88da5baf | data/restaurants.csv, data/pricing.md | Official restaurant sites / Michelin | — |
| T3 | Hours/days/exceptions + official links + social links | in progress | 88da5baf | data/restaurants.csv, data/hours-social.md | Official sites; YouTube/TikTok/Instagram search | — |
| T4 | Hotels ranked by Michelin density | in progress | 88da5baf | data/hotels.csv, data/hotels.md | Hotel official sites + Michelin map distances | — |
| T5 | GitHub Pages site (landing + subpages, mobile-friendly) | in progress | 88da5baf | index.html, *.html, assets/*, _config.yml | Build check, link check | — |
| T6 | Executive summary, Questions/Answers, Suggestions | in progress | 88da5baf | docs/executive-summary.md, docs/questions.md, docs/suggestions.md | Cross-ref T1–T4 | — |
| T7 | Final integration: re-verify line-by-line, link check, publish | in progress (88da5baf; merged PR #3 at 14:27Z) | 88da5baf | all | — | — |
| T8 | Michelin 2026 star list re-verification from official Michelin article + Michelin restaurant pages (days/hours, price level, official site link) | needs review (partial: 14 of 41 starred hours checked; conflicts F1–F4) | 049fdb53 (branch arena/049fdb53-baymich3) | data/restaurants.csv (stars, hours, price-level, michelin columns only) | guide.michelin.com article (24 Jun 2026) + per-restaurant Michelin pages | see Log |
| T9 | Hotels: official addresses + Michelin density recheck | needs review (counts corrected; 1 address corrected; distances not done) | 049fdb53 | data/hotels.csv | official hotel sites | see Log |
| T10 | Site regeneration from CSVs (restaurants/hotels pages, Verified / Unverified badges, mobile tables) | done (PR pending integration) | 049fdb53 | scripts/build_tables.py, restaurants.html, hotels.html, listed.html, map.html, index.html | build check, link check | see Log |
| T11 | Exec summary / Questions / Suggestions refresh (suggestions NOT implemented until user approves) | done (suggestions S1–S13 await review) | 049fdb53 | docs/executive-summary.md, docs/questions.md, docs/suggestions.md, executive-summary.html, questions.html, suggestions.html | cross-ref T8–T10 | see Log |

## Log
- 2026-11-24: Repo was empty (only README). Session 88da5baf claimed T1–T6 on branch arena/88da5baf-baymich3. T7 left for final integration pass in same session after T1–T6 done.

## Update 2026-11-24 (session 88da5baf)
- T1 DONE: 41 Core starred (2026) + 3 Extension in data/restaurants.csv. Source: Michelin Guide California 2026 article (24 Jun 2026) + press release (26 Jun 2026). Irregularity: 2025 stars Le Comptoir/O'/Shota absent 2026 — flagged.
- T2 DONE (partial verified): 12 rows verified official price (Benu, Acquerello, Birdsong, Commis, Kiln, Lazy Bear, Sons & Daughters, 7 Adams, Angler, Madcap, Sorrel, Auberge via Tock). 29 Unverified (blank, flagged). No inferred prices.
- T3 DONE (partial): Hours verified 10 rows; social verified 3 Instagram (Atelier, Benu, Lazy Bear). Rest blank/Unverified. YouTube/TikTok 0 verified — see Questions Q5.
- T4 DONE: 14 hotels ranked by cluster density in data/hotels.csv. 2 addresses verified (Four Seasons, Fairmont partial). Nightly rates not collected (dynamic).
- T5 DONE: GitHub Pages site (10 pages, mobile-friendly, search/filter). Link check: no missing internal links. Local preview on :8000 OK.
- T6 DONE: docs/executive-summary.md, docs/questions.md (12 Qs), docs/suggestions.md (10 suggestions S1-S10, none implemented).
- T7 IN PROGRESS: final integration — re-verified combined data, link check passed, publish to GitHub Pages (merge to main + enable Pages).

## Session 049fdb53 — claim (2026-11-24, 14:3x UTC)
- Branch: `arena/049fdb53-baymich3` (fixed by Arena session; the `session-<id>/<task>` naming in the rules above could not be used because the session is bound to this branch). All claimed work is committed here and opened as a PR to `main`.
- Claimed T8–T11 above. T7 remains with 88da5baf (PR #3 already merged to main).
- Open PRs #1 (arena/d7b7bed1) and #2 (arena/db94882d) from earlier sessions touch docs/ and scripts/build_site.py; not merged by this session. Flagged for integration owner.
- Non-overlap: this session edits only the files listed in T8–T11. Shared index/navigation changes are limited to restaurants/hotels/listed/map/index pages (T10) and must be re-verified by the integration session.

## Session 049fdb53 — log (24 Nov 2026)
- **T8 (partial, needs review).** Stars: all 41 Core starred rows match the Michelin 2026 California article (A1). Michelin restaurant pages checked for 14 starred rows (hours, price level, website, Green Star block). Sources: data/verification-log-2026-11-24.md §A. Irregularities: F1 Quince hours (Michelin 9 PM vs official 8 PM); F2 Kiln Tue–Thu close; F3 Lazy Bear close; F4 Sons & Daughters address (Michelin 2875 18th St vs prior 708 Bush St); F8 Atelier Crenn Green Star corrected No→Yes; F9 Michelin "SF & surroundings" (145) is a different geography than our 9-county Core.
- **T9 (partial, needs review).** Hotel starred counts corrected (SF 20→25; Wine Country 7→8); list re-sorted by the metric; Bardessono address corrected to 6526 Yount St (official contact page) — prior address was the French Laundry's. Hotels within a cluster are tied (F13). Nightly rates not collected.
- **T10 (done).** `scripts/build_tables.py` generates restaurants.html and hotels.html (and the docs pages) from CSV/Markdown. Mobile card layout (<640 px). Internal link check: 0 broken. Structural HTML check: all 10 pages balanced.
- **T11 (done).** docs/executive-summary.md, questions.md (14 Qs), suggestions.md (S1–S13, none implemented), flagged.md (F1–F17), methodology.md rewritten; verification-log added.
- **Price-for-2 corrections:** Acquerello $708→$731.60; Angler $156→$151.20; Commis $669→$669.60; Sorrel set Unverified (season).
- **Not done (carried):** prices for 31 starred rows; Michelin re-check for 27 starred rows; Bib list re-verification; social links beyond 2 Instagram; hotel distances.
- **Integration note for 88da5baf / integration owner:** open PRs #1 (arena/d7b7bed1) and #2 (arena/db94882d) from the morning overlap docs/ and scripts/build_site.py; not merged here. The new PR from arena/049fdb53-baymich3 touches restaurants.html, hotels.html, docs/*.md, data/*.csv, scripts/build_tables.py, assets/style.css, map.html, README.md, COORDINATION.md. Integration owner to re-verify and publish; this session did not merge to main.

