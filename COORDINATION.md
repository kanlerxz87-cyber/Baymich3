# COORDINATION.md — Shared Task Board

Session ID: `a4fdd108` (branch: `arena/a4fdd108-baymich3`) — audit/verification pass. Prior session 88da5baf work merged to main (b047b5d).
Last updated: 2026-11-24 (session a4fdd108)

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
| T7 | Final integration: re-verify line-by-line, link check, publish | unclaimed | — | all | — | — |

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

## Session a4fdd108 (2026-11-24) — Audit & Verification Pass

| ID | Task | Status | Owner | Files | Notes |
|----|------|--------|-------|-------|-------|
| A1 | Line-by-line audit: CSV column shifts, price math, HTML↔CSV sync, counts | in progress | a4fdd108 | data/restaurants.csv, data/bib.csv, data/hotels.csv, *.html | Found: 11 rows michelin_url in price_pp column (R28,R33,R34,R36,R38-R42,R44), R26 verification in notes, R12 instagram in youtube col, Acquerello $708 vs $731.60 basis, Angler $156 vs $151.20 basis. Fixing. |
| A2 | Re-verify prices/hours/social from official sites (fetch, no inference) | in progress | a4fdd108 | data/restaurants.csv | Fetch official_url per row; blank stays Unverified if not on official page. |
| A3 | Fix site: regenerate tables from fixed CSV, mobile, broken-link check, Pages check | in progress | a4fdd108 | *.html, assets/*, _config.yml | Pages already built on main (legacy). This branch needs merge to main to go live. |
| A4 | Update executive summary / questions / suggestions / flagged with audit findings | in progress | a4fdd108 | docs/*.md, *.html | Correct C5 count error (8 names listed as 7), update unverified counts. |
| A5 | Final integration: re-verify, link check, commit/push | unclaimed | — | all | — |

### Audit log a4fdd108
- Michelin 2026 star list re-verified line-by-line vs official article https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california (24 Jun 2026): 3★ Bay Area 7, 2★ 9 (7 Core+2 Ext), 1★ 28 (27 Core+1 Ext) = 44 total. Matches CSV counts. Californios + Enclos NEW 3★, Naides/Wolfsbane/Troubadour NEW 1★ confirmed.
- Irregularities found (see A1): column-shift corruption in 12 rows, 2 price-math mismatches, C5 cluster count text error in executive summary, 7 Adams/Angler "verified via search snippet" does not meet strict official-fetch rule — re-fetching.
