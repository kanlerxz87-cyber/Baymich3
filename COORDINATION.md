# COORDINATION.md — Shared Task Board

Session ID: `231b05b5` (branch: `arena/231b05b5-baymich3`)
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
| T1 | Michelin restaurants (stars + listed) — SF Bay Area | done | 88da5baf | data/restaurants.csv, data/bib.csv | guide.michelin.com (official) | 10 CSV rows had URL in price column (fixed by 231b05b5) |
| T2 | Pricing for 2 adults (verified only) | done* | 88da5baf | data/restaurants.csv | Official restaurant sites / Michelin | *partial: 12 verified, 29 unverified — deepened by 231b05b5 |
| T3 | Hours/days/exceptions + official links + social links | done* | 88da5baf | data/restaurants.csv | Official sites; social search | *partial: 10 hours, 3 social — deepened by 231b05b5 |
| T4 | Hotels ranked by Michelin density | done* | 88da5baf | data/hotels.csv | Hotel official sites + Michelin | *partial: 2 addresses verified — deepened by 231b05b5 |
| T5 | GitHub Pages site (landing + subpages, mobile-friendly) | done* | 88da5baf | index.html, *.html, assets/* | Build check, link check | *rebuilt/polished by 231b05b5 |
| T6 | Executive summary, Questions/Answers, Suggestions | done* | 88da5baf | docs/*.md | Cross-ref T1–T4 | *updated by 231b05b5 |
| T7 | Final integration: re-verify line-by-line, link check, publish | in progress | 231b05b5 | all | guide.michelin.com + official sites | Taking over from 88da5baf (merged to main via PR #3, b047b5d) |
| T8 | Fix CSV bugs + deepen verification (prices/hours/social/hotels) | in progress | 231b05b5 | data/*.csv, data/*.md | Official sites via fetch_page | 10 rows URL-in-price bug; Auro/Troubadour/Press/Plumed Horse/Village Pub/Aubergine/Chez Noir/Naides/Wolfsbane/Sun Moon |
| T9 | Rebuild site pages from clean data (mobile-friendly, map, tables) | in progress | 231b05b5 | *.html, assets/* | Link check, preview | — |

## Log
- 2026-11-24: Repo was empty (only README). Session 88da5baf claimed T1–T6 on branch arena/88da5baf-baymich3. T7 left for final integration pass in same session after T1–T6 done.
- 2026-11-24 (session 88da5baf): T1–T6 done (partial verification). T7 in progress.
- 2026-11-24 (session 231b05b5): Took over T7–T9 on branch arena/231b05b5-baymich3 (branched from main b047b5d, PR #3 merge). Found 10 CSV rows with Michelin URL shifted into price_pp_usd column (R28, R33, R34, R36, R38, R39, R40, R41, R42, R44) causing broken site rows. Claiming T7–T9. Scope: data/*.csv + *.html + assets/* + docs/*.md + COORDINATION.md.
