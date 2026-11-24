# COORDINATION.md — Shared Task Board

Session IDs: `88da5baf` (branch `arena/88da5baf-baymich3`, merged PR #3), `e1b8a912` (branch `arena/e1b8a912-baymich3`, merged PR #4), `15c870c6` (branch `arena/15c870c6-baymich3`)
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
| T1 | Michelin restaurants (stars + listed) — SF Bay Area | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/restaurants.md | guide.michelin.com (official) | — |
| T2 | Pricing for 2 adults (verified only) | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/pricing.md | Official restaurant sites / Michelin | — |
| T3 | Hours/days/exceptions + official links + social links | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/restaurants.csv, data/hours-social.md | Official sites; YouTube/TikTok/Instagram search | — |
| T4 | Hotels ranked by Michelin density | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | data/hotels.csv, data/hotels.md | Hotel official sites + Michelin map distances | — |
| T5 | GitHub Pages site (landing + subpages, mobile-friendly) | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | index.html, *.html, assets/*, _config.yml | Build check, link check | — |
| T6 | Executive summary, Questions/Answers, Suggestions | done (per 88da5baf log; irregularities in flagged.html) | 88da5baf | docs/executive-summary.md, docs/questions.md, docs/suggestions.md | Cross-ref T1–T4 | — |
| T8 | Repo review: irregularity log + starred-list re-check vs Michelin 2026 article | done | 15c870c6 | COORDINATION.md, docs/flagged-review.md, flagged.html | guide.michelin.com California 2026 article (24 Jun 2026); Michelin SF restaurants list | 21 items on flagged.html (F1–F21) |
| T9 | Restaurants: verify blank rows from Michelin restaurant pages (address, website, tier, hours) | done | 15c870c6 | data/restaurants.csv | 17 Michelin restaurant pages fetched 24 Nov 2026 (linked per row) | Hours still missing for some rows; 0 YouTube/TikTok verified |
| T10 | Hotels: correct starred counts, re-rank by count, document method | done (distance method still a user decision, Q13) | 15c870c6 | data/hotels.csv, data/hotels.md | Michelin 2026 article (cluster counts) | SF 20→25, Wine Country 7→8, ranks re-sorted; Bardessono address conflict flagged; distance method not applied |
| T11 | Site: data pages from CSV/Markdown; flagged page; summary/questions/suggestions rendered from docs | done, superseded by T7 | 15c870c6 | scripts/build_site.py, scripts/build_restaurants.py (both now removed in favour of tools/build_site.py), restaurants/hotels/flagged/executive-summary/questions/suggestions .html | Internal link check: 0 missing | index/listed/map/methodology not regenerated at the time — now all 10 pages are generated |
| T7 | Final integration: re-verify line-by-line, link check, publish | done (a4fdd108) | a4fdd108 | data/restaurants.csv, restaurants.html, executive-summary.html, questions.html, flagged.html, docs/*.md, scripts/build_restaurants.py, COORDINATION.md | guide.michelin.com US article “Every MICHELIN-Starred Restaurant in California for 2026” (24 Jun 2026) + Michelin SF restaurants page (145 / 29★ / 30 Bib / 86 Selected) | See log 2026-11-24 e1b8a912 |

## Log
- 2026-11-24 (15c870c6): Session 15c870c6 on branch arena/15c870c6-baymich3 claimed T8–T11 (remediation pass) before seeing the e1b8a912 T7 claim. Note: this overlaps T7 on data/restaurants.csv, restaurants.html, executive-summary.html, questions.html, flagged.html, docs/*.md and scripts/build_restaurants.py — see the 15c870c6 merge log below.
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

## Log — session 15c870c6 (branch arena/15c870c6-baymich3), 2026-11-24 — remediation pass + merge with e1b8a912
- **Scope done:** T8 (irregularity log), T9 (17 Michelin restaurant pages), T10 (hotels), T11 (site regenerated). Branch: arena/15c870c6-baymich3.
- **Sources used:** Michelin California 2026 article https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california ; Michelin SF list https://guide.michelin.com/us/en/california/san-francisco/restaurants ; Michelin restaurant pages (linked per row in data/restaurants.csv).
- **Verification performed:** Starred list (41 Core + 3 Extension) matched name-by-name to the Michelin 2026 article's lists. Hotel cluster counts recomputed from the same lists. Two-adult totals re-computed from their stated formulas. Internal links checked. External official sites NOT re-fetched in this session (only Michelin pages).
- **Irregularities:** see flagged.html (F1–F18). Key: 2 wrong totals (fixed), 10 shifted URL cells (fixed), 2 hotel count errors (fixed), hotel ranks out of order (fixed), 2 same-address conflicts (open), Green Star list not checked (open), social coverage 3/44 (open).
- **Open decisions:** Q13 (hotel ranking method), Q14 (on-site restaurants at hotels).
- **Merge with e1b8a912 (PR #4):** PR #5 conflicted with main on the T7 files. Resolution: kept both sides. CSV: took e1b8a912's Sorrel price (409.50, SF mandate), Green Star flags (Atelier Crenn, Harbor House), and R26 status; kept 15c870c6's Michelin-page fields for R24 and R28–R44. HTML pages regenerated by scripts/build_site.py (scripts/build_restaurants.py now delegates to it). Their irregularities F19–F21 added to flagged.html. Nothing from e1b8a912 was discarded.
- **Handoff note:** Tasks T9 and T10 are "needs review" and do not block other work. Any session that picks up T9 should start with the rows whose verification_status says "Partial" or "Unverified".
- 2026-11-24 (a4fdd108) — **MERGE RESOLUTION with 15c870c6 (PR #5).** Main and this branch had both rewritten the same files. Rule applied: keep the side that could cite an official page, and take whichever value was actually fetched.
  - **restaurants.csv:** kept this branch's canonical 44×24 repair + fetched prices, and merged in 15c870c6's `michelin_price_tier` column and its Michelin-page hours/exceptions for 13 rows (Naides, Ssal, State Bird, The Progress, Wolfsbane, Sun Moon Studio, Troubadour, Press, Plumed Horse, Village Pub). Green Star: kept 15c870c6's flags for Quince, SingleThread, French Laundry, Enclos, Sons & Daughters and Harbor House Inn (all visible on Michelin pages); **Atelier Crenn set to `Unconfirmed`** because its Green Star rested on a secondary list. Took 15c870c6's more precise addresses for Aubergine, Selby's and Cyrus.
  - **hotels.csv:** kept this branch's verified addresses (Bardessono 6526 Yount St, Cavallo Point 601 Murray Circle, 1 Hotel 8 Mission St) and its per-row statuses, but adopted 15c870c6's rank order, which sorts strictly by cluster density (25 → 8 → 5 → 2 → 1).
  - **bib.csv:** no name or cluster disagreements; kept this branch's version, which cites each row's own city list and marks the 28 unconfirmed rows Unverified instead of "verified".
  - **Generator:** two competing generators existed (`tools/build_site.py` and `scripts/build_site.py`). Consolidated on `tools/build_site.py`, extended with the Markdown renderer from `scripts/build_site.py` so `docs/*.md` remains the source for the five text pages. `scripts/` removed. All 10 pages now generated, including index/listed/map/methodology.
  - **flagged:** merged both logs into one 26-item table (`docs/flagged-review.md`), keeping F1–F21 and adding F22–F26 for the hotel-address, Madcap/Sorrel/7-Adams and Bib-provenance findings.
