# Flagged for Review

Flagged items do not block publication. Each one lists both sources so you can check them yourself. "Fix" = what was changed in the data.

| ID | Item | Source A | Source B | Status / Fix |
|---|---|---|---|---|
| F1 | Quince closing time | Michelin page: Tue–Thu 5–9 PM; Fri–Sat 5–9 PM [guide.michelin.com/…/quince](https://guide.michelin.com/us/en/california/san-francisco/restaurant/quince) | Official homepage (prior session): main dining 5–8 PM [quincerestaurant.com](https://www.quincerestaurant.com/) | Conflict. Both shown. Confirm on Tock/OpenTable before booking. |
| F2 | Kiln Tue–Thu hours | Michelin: 6–8 PM [kiln page](https://guide.michelin.com/us/en/california/san-francisco/restaurant/kiln-1210355) | Official info page (prior): 6–8:30 PM [kilnsf.com/information](https://www.kilnsf.com/information) | Conflict. Both shown. |
| F3 | Lazy Bear hours | Michelin: Tue–Sat 5–11 PM [lazy-bear page](https://guide.michelin.com/us/en/california/san-francisco/restaurant/lazy-bear) | Official tickets page (prior): 5–9 PM [lazybearsf.com/tickets](https://www.lazybearsf.com/tickets) | Conflict. Both shown. |
| F4 | Sons & Daughters address | Michelin: 2875 18th St SF 94110 [page](https://guide.michelin.com/us/en/california/san-francisco/restaurant/sons-daughters) | Prior record: 708 Bush St SF 94108 | Conflict. Michelin address used; confirm on sonsanddaughterssf.com. |
| F5 | Benu Instagram | Prior record: instagram.com/benu_sf (found by search) | Not on official site per prior session | Removed to Unverified. |
| F6 | Bardessono address | Prior record: 6640 Washington St (= French Laundry's address) | Official contact page: 6526 Yount St [bardessono.com/contact.htm](https://www.bardessono.com/contact.htm) | Fixed to official address. |
| F7 | Hotel star counts + order | Prior: SF 20 starred; Wine Country 7; list not sorted by count | Recount from restaurants.csv: SF 25, Wine Country 8 | Fixed. Ordering now by count (see F13). |
| F8 | Atelier Crenn Green Star | Prior record: No | Michelin page: Green Star sustainability block present [page](https://guide.michelin.com/us/en/california/san-francisco/restaurant/atelier-crenn) | Set to Yes. Prior Yes/No values for other rows not re-checked unless listed in verification-log. |
| F9 | Geography | Michelin "San Francisco and surroundings": 145 restaurants; 4/7/18 starred [SF list](https://guide.michelin.com/us/en/california/san-francisco/restaurants) | Our 9-county Core: 41 starred (25 SF) | Both shown. Explained in Methodology. |
| F10 | French Laundry official site | Prior: frenchlaundry.com | HTTP 500 on 24 Nov 2026 (twice) | Michelin links thomaskeller.com/tfl; used as official link. Hours/price for 2 Unverified. |
| F11 | 2025 stars not in 2026 list | Prior: Le Comptoir, O' by Claude Le Tohic, The Shota (2025) | Not in Michelin 2026 California starred list [article](https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california) | Status (closed / demoted / renamed) still unknown. Not added to the table. |
| F12 | Price arithmetic | Acquerello prior total $708; Angler prior total $156 | Their own formulas: $731.60; $151.20 | Fixed. Sorrel: prior "Summer 2026" label replaced by Fall 2026 menu, $409.50 for 2 (official menus page). |
| F13 | Hotel ranking ties | Within each cluster every hotel has the same count | No distance data yet | Open. Needs coordinates (see Suggestions S11). |
| F14 | Michelin pages cut off | Birdsong (Wed–Sat), Commis (Sat), SingleThread, French Laundry, Saison (Fri+) hours not in fetched part | — | Left blank. Re-check Michelin page. |
| F15 | Official sites with no price/hours | Californios, Enclos (video), Saison, SingleThread (no price) | — | Left Unverified; booking links are the official source. |
| F16 | Stale open PRs in this repo | PR #1 (arena/d7b7bed1) and PR #2 (arena/db94882d), opened 08:53 UTC on 24 Nov | Both touch docs/ and scripts/build_site.py | Not merged by this session. Integration owner to close or rebase. |
| F17 | Prior-session values not re-checked | Benu/Acquerello/Birdsong/Commis/Kiln/Lazy Bear/Sons prices; Bib list; hotel addresses | — | Carried over and labelled "prior session". |
| F18 | Green Star list not checked on Michelin itself | Green Star 2026 list used from secondary sources that cite Michelin: VisitCalifornia [page](https://www.visitcalifornia.com/experience/california-restaurants-top-nation-michelin-green-stars/) and Enjoy Orange County [page](https://enjoyorangecounty.com/michelin-restaurants/) (added by PR #4) | Michelin's own Green Star listing still to confirm | Open. Green Star "Yes" for rows with the Michelin page's green sustainability block is confirmed (see verification log §A). |
| F19 | Green-Star-only Bay Area restaurants not in dataset | Chez Panisse (Berkeley) and Pomet (Oakland) on the 2026 Green Star list (secondary sources, PR #4) | No row in the starred or Bib tables | Open. Needs Michelin listing check; not added. |
| F20 | Michelin URL path | Official article links use guide.michelin.com/ca/en/… | CSV uses /us/en/… for the same pages | Both resolve to the same restaurant pages (checked for 14 rows); seven rows filled from the article (PR #4). |
| F21 | Two generators for restaurants.html | scripts/build_restaurants.py (PR #4) | scripts/build_tables.py (this session) | `build_tables.py` is the single generator. `build_restaurants.py` is superseded and must not be run. Integration owner to decide on removal. |

