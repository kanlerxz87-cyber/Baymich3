# COORDINATION.md — Shared Task Board

Session IDs: `88da5baf` (branch `arena/88da5baf-baymich3`, merged to main via PR #3) and `15c870c6` (branch `arena/15c870c6-baymich3`, current)
Last updated: 2026-11-24 (session 15c870c6)

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
| T1 | Michelin restaurants (stars + listed) — SF Bay Area | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/restaurants.md | guide.michelin.com (official) | — |
| T2 | Pricing for 2 adults (verified only) | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/pricing.md | Official restaurant sites / Michelin | — |
| T3 | Hours/days/exceptions + official links + social links | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/hours-social.md | Official sites; YouTube/TikTok/Instagram search | — |
| T4 | Hotels ranked by Michelin density | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/hotels.csv, data/hotels.md | Hotel official sites + Michelin map distances | — |
| T5 | GitHub Pages site (landing + subpages, mobile-friendly) | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | index.html, *.html, assets/*, _config.yml | Build check, link check | — |
| T6 | Executive summary, Questions/Answers, Suggestions | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | docs/executive-summary.md, docs/questions.md, docs/suggestions.md | Cross-ref T1–T4 | — |
| T10 | Hotels: correct starred counts, re-rank by count, document method | needs review (method decision Q13) | 15c870c6 | data/hotels.csv, data/hotels.md | Michelin 2026 article (cluster counts) | SF 20→25, Wine Country 7→8, ranks re-sorted; Bardessono address = French Laundry address (flag); distance method not applied |
| T11 | Site: data pages regenerated from CSVs (scripts/build_site.py); flagged page; summary/questions/suggestions rendered from docs/*.md | done | 15c870c6 | scripts/build_site.py, restaurants.html, hotels.html, flagged.html, executive-summary.html, questions.html, suggestions.html | Internal link check: 0 missing; external links not checked (sandbox allows only GitHub/npm/PyPI) | Hand-written pages index/listed/map/methodology not regenerated |
| T7 | Final integration: re-verify line-by-line, link check, publish | done (88da5baf, merged PR #3; Pages built from main) | 88da5baf | all | — | — |
| T8 | Repo review: irregularity log + starred-list re-check vs Michelin 2026 article | done | 15c870c6 | COORDINATION.md, docs/flagged-review.md, flagged.html | guide.michelin.com California 2026 article (24 Jun 2026); Michelin SF restaurants list | 18 items (F1–F18) on flagged.html: 9 fixed, 9 open |
| T9 | Restaurants: fill/verify blank rows from Michelin restaurant pages (address, website, tier, hours) | needs review | 15c870c6 | data/restaurants.csv | 17 Michelin restaurant pages fetched 24 Nov 2026 (links in each row) | 27 rows still lack a verified hours/price; 0 YouTube/TikTok verified; Naides/Sons & Daughters same address; 10 shifted-URL rows fixed; Acquerello, Commis, Angler totals corrected |

## Log
- 2026-11-24 (15c870c6): Session 15c870c6 starts on branch arena/15c870c6-baymich3 (the only active branch per session rules; session-<id>/<task> naming not used — branch name fixed by Arena). Prior tasks T1–T6 are complete per the 88da5baf log and merged. Claimed T8–T11 as the remediation pass. No other session holds a claim on any file listed above.
- 2026-11-24: Repo was empty (only README). Session 88da5baf claimed T1–T6 on branch arena/88da5baf-baymich3. T7 left for final integration pass in same session after T1–T6 done.

## Update 2026-11-24 (session 88da5baf)
- T1 DONE: 41 Core starred (2026) + 3 Extension in data/restaurants.csv. Source: Michelin Guide California 2026 article (24 Jun 2026) + press release (26 Jun 2026). Irregularity: 2025 stars Le Comptoir/O'/Shota absent 2026 — flagged.
- T2 DONE (partial verified): 12 rows verified official price (Benu, Acquerello, Birdsong, Commis, Kiln, Lazy Bear, Sons & Daughters, 7 Adams, Angler, Madcap, Sorrel, Auberge via Tock). 29 Unverified (blank, flagged). No inferred prices.
- T3 DONE (partial): Hours verified 10 rows; social verified 3 Instagram (Atelier, Benu, Lazy Bear). Rest blank/Unverified. YouTube/TikTok 0 verified — see Questions Q5.
- T4 DONE: 14 hotels ranked by cluster density in data/hotels.csv. 2 addresses verified (Four Seasons, Fairmont partial). Nightly rates not collected (dynamic).
- T5 DONE: GitHub Pages site (10 pages, mobile-friendly, search/filter). Link check: no missing internal links. Local preview on :8000 OK.
- T6 DONE: docs/executive-summary.md, docs/questions.md (12 Qs), docs/suggestions.md (10 suggestions S1-S10, none implemented).
- T7 IN PROGRESS: final integration — re-verified combined data, link check passed, publish to GitHub Pages (merge to main + enable Pages).

## Update 2026-11-24 (session 15c870c6) — remediation pass
- **Scope done:** T8 (irregularity log), T9 (17 Michelin restaurant pages), T10 (hotels), T11 (site regenerated). Branch: arena/15c870c6-baymich3.
- **Sources used:** Michelin California 2026 article https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california ; Michelin SF list https://guide.michelin.com/us/en/california/san-francisco/restaurants ; Michelin restaurant pages (linked per row in data/restaurants.csv).
- **Verification performed:** Starred list (41 Core + 3 Extension) matched name-by-name to the Michelin 2026 article's lists. Hotel cluster counts recomputed from the same lists. Two-adult totals re-computed from their stated formulas. Internal links checked. External official sites NOT re-fetched in this session (only Michelin pages).
- **Irregularities:** see flagged.html (F1–F18). Key: 2 wrong totals (fixed), 10 shifted URL cells (fixed), 2 hotel count errors (fixed), hotel ranks out of order (fixed), 2 same-address conflicts (open), Green Star list not checked (open), social coverage 3/44 (open).
- **Open decisions:** Q13 (hotel ranking method), Q14 (on-site restaurants at hotels).
- **Handoff note:** Tasks T9 and T10 are "needs review" and do not block other work. Any session that picks up T9 should start with the rows whose verification_status says "Partial" or "Unverified".

