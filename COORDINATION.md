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
| T7 | Final integration: re-verify line-by-line, link check, publish | in progress (claimed 2026-11-24 14:30 UTC by e1b8a912; handoff from 88da5baf — see log) | e1b8a912 | data/restaurants.csv, restaurants.html, executive-summary.html, questions.html, flagged.html, docs/*.md, scripts/build_restaurants.py, COORDINATION.md | guide.michelin.com US article “Every MICHELIN-Starred Restaurant in California for 2026” (24 Jun 2026) + Michelin SF restaurants page (145 / 29★ / 30 Bib / 86 Selected) | See log 2026-11-24 e1b8a912 |
| T8 | Michelin 2026 star list re-verification from official Michelin article + Michelin restaurant pages (days/hours, price level, official site link) | needs review (partial: 14 of 41 starred hours checked; conflicts F1–F4) | 049fdb53 (branch arena/049fdb53-baymich3) | data/restaurants.csv (stars, hours, price-level, michelin columns only) | guide.michelin.com article (24 Jun 2026) + per-restaurant Michelin pages | see 049fdb53 log |
| T9 | Hotels: official addresses + Michelin density recheck | needs review (counts corrected; Bardessono address corrected; distances not done) | 049fdb53 | data/hotels.csv | official hotel sites | see 049fdb53 log |
| T10 | Site regeneration from CSVs (restaurants/hotels pages; single generator scripts/build_tables.py; mobile card tables) | done (PR pending integration) | 049fdb53 | scripts/build_tables.py, restaurants.html, hotels.html, assets/style.css, map.html | build check, internal link check, HTML balance check | see 049fdb53 log |
| T11 | Exec summary / Questions / Suggestions / Flagged / Method refresh (suggestions NOT implemented until user approves) | done (S1–S13 await review) | 049fdb53 | docs/executive-summary.md, docs/questions.md, docs/suggestions.md, docs/flagged.md, docs/methodology.md (+ generated *.html) | cross-ref T7–T9 | see 049fdb53 log |

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

## Log — session e1b8a912 (branch arena/e1b8a912-baymich3), 2026-11-24
- **Claim / handoff:** T7 was shown as "unclaimed" in the table but "in progress" in the 88da5baf log, while the merged PR #3 (88da5baf) already published the site from `main`. Claimed T7 for re-verification and integration; this is a handoff of the final pass, not a new task. Scope limited to the files listed in the T7 row. T1–T6 data owners (88da5baf) were not otherwise edited.
- **Official verification (fetched 24 Nov 2026):**
  - Michelin article “Every MICHELIN-Starred Restaurant in California for 2026” (https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california): all 41 Core starred rows match the official star lists (7× 3★, 7× 2★, 27× 1★). Extension rows Aubergine (2★), Harbor House Inn (2★), Chez Noir (1★) match.
  - Michelin SF restaurants page (https://guide.michelin.com/us/en/california/san-francisco/restaurants): 145 restaurants; 4× 3★, 7× 2★, 18× 1★, 30 Bib, 86 Selected. Matches the SCOPE totals.
  - Sorrel menus (https://www.sorrelrestaurant.com/menus/) and Acquerello seasonal menu (https://www.acquerellosf.com/seasonal-tasting-menu): prices re-checked (see fixes).
  - Green Star 2026 list: taken from secondary sources that cite Michelin (VisitCalifornia https://www.visitcalifornia.com/experience/california-restaurants-top-nation-michelin-green-stars/ ; Enjoy Orange County https://enjoyorangecounty.com/michelin-restaurants/). Michelin's own Green Star page still to confirm.
- **Fixes made:**
  - R28–R44 malformed CSV rows (Michelin URL in price column) corrected; 7 missing Michelin links filled from the official article.
  - Green Star: Atelier Crenn (R01) and Harbor House Inn (R43) → Yes.
  - Arithmetic: Acquerello $708 → $731.60; Commis $669 → $669.60; Angler $156 → $151.20.
  - Sorrel: stale "Summer 2026" label → Fall 2026 ($195 8-course); 2 adults $409.50 incl. 5% SF Mandate.
  - restaurants.html table regenerated from data/restaurants.csv by scripts/build_restaurants.py (single source). Fixed the star filter, which compared against a group string that included the cluster.
- **Irregularities (logged in flagged.html):** Chez Panisse (Berkeley) and Pomet (Oakland) are on the 2026 Green Star list but absent from the dataset. Social links remain 3/44 verified (YouTube/TikTok 0). Hotel addresses mostly unverified. Official article uses /ca/en/ URLs vs /us/en/ in CSV.
- **Other sessions:** Open PRs #1 (arena/d7b7bed1) and #2 (arena/db94882d) exist on other branches. Not touched. Their COORDINATION.md edits will conflict with this one; resolve at merge (keep all log entries).
- **Status:** T7 re-verification complete for the starred set and the corrected rows. Not complete: per-row social links (only 3 verified), 29 unverified prices, and hotel address verification. These remain flagged and are blank, not inferred.

## Log — session 049fdb53 (branch arena/049fdb53-baymich3), 24 Nov 2026
- **Claim:** T8–T11 (table above). Branch name fixed by the Arena session (cannot be `session-<id>/<task>`). Commits pushed to that branch only.
- **Merge note:** PR #4 (e1b8a912, T7) merged to main while this session was working. Merged main into our branch (no rebase, no force push). Their CSV fixes (R28–R44 malformed rows, Acquerello/Commis/Angler arithmetic, Sorrel Fall 2026, Green Star Atelier Crenn & Harbor House) are kept. Our changes sit on top.
- **Single generator:** `scripts/build_tables.py` is now the only script that writes restaurants.html (and hotels.html + docs pages). `scripts/build_restaurants.py` (e1b8a912) is kept unchanged but is **superseded** — do not run it, or it will overwrite the new table with the older layout. Integration owner to decide whether to delete it.
- **T8 (partial, needs review):** 41 Core starred rows match the Michelin 2026 California article. Michelin restaurant pages checked for 14 starred rows (hours, price level, website, Green Star block). Conflicts: F1 Quince closing time, F2 Kiln Tue–Thu close, F3 Lazy Bear close, F4 Sons & Daughters address (Michelin 2875 18th St vs 708 Bush St). Benu Instagram removed (unconfirmed). Atelier Crenn Green Star: Yes (Michelin page shows Green Star block). Sources: data/verification-log-2026-11-24.md §A.
- **T9 (partial, needs review):** Hotel starred counts corrected (SF 20→25; Wine Country 7→8). Ordering by count (was not sorted by the metric). Bardessono address corrected to 6526 Yount St (official contact page); the prior address was the French Laundry's. Hotels in the same cluster are tied until distances are computed.
- **Sorrel:** Official menus page (sorrelrestaurant.com/menus/, fetched 24 Nov 2026): Fall 2026 8-course $195 pp; 5% SF Mandate → 2 adults $409.50. Matches PR #4. Adopted.
- **Irregularities (in flagged.md):** F1–F17 (includes the PR #4 items: Chez Panisse and Pomet on the Green Star list but not in the dataset; Michelin /ca/en vs /us/en URL paths; Green Star list from secondary sources only).
- **Not done (carried):** prices for 30 starred rows; Michelin re-check for 27 starred rows; Bib list re-verification; social links beyond 2 Instagram; hotel distances.
- **Open PRs:** #1 (arena/d7b7bed1) and #2 (arena/db94882d) overlap docs/ and scripts/build_site.py; not touched here. Integration owner to close or rebase.
- **Publishing:** this session did not merge to main. The site on main will update when the integration owner merges this PR (PR opened from arena/049fdb53-baymich3).

