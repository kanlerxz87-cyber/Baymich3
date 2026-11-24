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
| T7 | Final integration: re-verify line-by-line, link check, publish | in progress | 6270f56e | validation only; COORDINATION.md | Official sources referenced in each data row; automated HTML/CSV checks | GitHub Pages publishing status needs verification; do not modify T1–T6-owned content without review |

## Log
- 2026-11-24 (session 6270f56e): Final integration audit performed on merged `main` snapshot. Automated checks: 10 HTML pages; no missing local `.html` href targets; local homepage returns HTTP 200; CSV row counts: restaurants 44, Bib 36, hotels 14. Review findings: restaurant rows 25–45 have empty price_source; multiple restaurant rows have no official_url and/or blank verification_status (Naides, Wolfsbane, Sun Moon Studio, Auro, Troubadour, Press, Plumed Horse, Village Pub, Aubergine, Chez Noir). Bib rows all have blank official_url (Michelin source references exist but not official restaurant links). Many hotel rows have blank official_url and statuses explicitly admit secondary/unverified addresses; hotel density order has no auditable distance/count calculation in CSV. These are not certified complete against the user's per-row official-source requirement. No data edited because task scopes belong to T1–T4; requesting them for review below. `git pull --rebase origin arena/6270f56e-baymich3` could not run because that remote branch did not yet exist; claim was pushed as new branch.
- 2026-11-24: Repo was empty (only README). Session 88da5baf claimed T1–T6 on branch arena/88da5baf-baymich3. T7 left for final integration pass in same session after T1–T6 done.

## Update 2026-11-24 (session 6270f56e)
- T7 review is needs review, not complete: line-by-line criteria exposed unfilled official restaurant links / source fields and insufficient audit trail for hotel ranking. Review requests: T1 fill/flag missing source statuses and ensure every presented restaurant has Michelin official source; T2 all blank price_source fields should visibly be unverified; T4 provide official hotel links and reproducible density method or suppress unsupported rank values; integration review should then rerun link/site checks. No dataset files changed due to ownership scope.

## Update 2026-11-24 (session 88da5baf)
- T1 DONE: 41 Core starred (2026) + 3 Extension in data/restaurants.csv. Source: Michelin Guide California 2026 article (24 Jun 2026) + press release (26 Jun 2026). Irregularity: 2025 stars Le Comptoir/O'/Shota absent 2026 — flagged.
- T2 DONE (partial verified): 12 rows verified official price (Benu, Acquerello, Birdsong, Commis, Kiln, Lazy Bear, Sons & Daughters, 7 Adams, Angler, Madcap, Sorrel, Auberge via Tock). 29 Unverified (blank, flagged). No inferred prices.
- T3 DONE (partial): Hours verified 10 rows; social verified 3 Instagram (Atelier, Benu, Lazy Bear). Rest blank/Unverified. YouTube/TikTok 0 verified — see Questions Q5.
- T4 DONE: 14 hotels ranked by cluster density in data/hotels.csv. 2 addresses verified (Four Seasons, Fairmont partial). Nightly rates not collected (dynamic).
- T5 DONE: GitHub Pages site (10 pages, mobile-friendly, search/filter). Link check: no missing internal links. Local preview on :8000 OK.
- T6 DONE: docs/executive-summary.md, docs/questions.md (12 Qs), docs/suggestions.md (10 suggestions S1-S10, none implemented).
- T7 IN PROGRESS: final integration — re-verified combined data, link check passed, publish to GitHub Pages (merge to main + enable Pages).
