# Verification log — 24 Nov 2026 (session 049fdb53, branch arena/049fdb53-baymich3)

Every check below was run on 24 Nov 2026 (UTC) using the fetch tool. "Result" is what the page said at the time. Items not listed here were NOT re-checked this session; their values are the prior session's (88da5baf) and are labelled as such in data/restaurants.csv.

## A. Michelin official pages (guide.michelin.com)
| # | URL | Used for | Result |
|---|---|---|---|
| A1 | https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california | Statewide + Bay Area star list (2026 edition, 24 Jun 2026) | 83 starred: 10×3★, 13×2★, 60×1★. Bay Area 3★: Atelier Crenn, Benu, Californios (NEW), Quince, Enclos (NEW, Sonoma), The French Laundry (Yountville), SingleThread (Healdsburg). 2★ (Core): Acquerello, Birdsong, Kiln, Lazy Bear, Saison, Sons & Daughters, Commis (Oakland). 1★ (Core): 27 names (see restaurants.csv). Extension 2★: Aubergine (Carmel), Harbor House Inn (Elk). 1★ Extension: Chez Noir (Carmel). |
| A2 | https://guide.michelin.com/us/en/california/san-francisco/restaurants | Michelin count for "San Francisco and surroundings" | 145 restaurants: 4 × 3★, 7 × 2★, 18 × 1★, 30 Bib Gourmand, 86 Selected. (Different geography from our 9-county Core — see Flagged F9.) |
| A3 | …/san-francisco/restaurant/quince | Hours, price level, website | Tue–Thu 5–9 PM; Fri–Sat 11:30 AM–1 PM and 5–9 PM; Mon & Sun closed. $$$$. Green-Star block present. Website quincerestaurant.com. |
| A4 | …/san-francisco/restaurant/californios | Hours, price level | Tue–Sat 5–10 PM; Mon & Sun closed. $$$$. |
| A5 | …/san-francisco/restaurant/benu | Hours, price level | Wed–Thu 5–8 PM; Fri–Sat 5–8:30 PM; Mon, Tue, Sun closed. $$$$. |
| A6 | …/san-francisco/restaurant/atelier-crenn | Hours, price level, Green Star | Tue–Sat 4:45–8:45 PM; Mon & Sun closed. $$$$. Green-Star block present. |
| A7 | …/healdsburg/restaurant/singlethread | Price level, Green Star | $$$$. Green-Star block present. Hours cut off in fetched chunk. |
| A8 | …/yountville/restaurant/the-french-laundry | Price level, Green Star, website | $$$$. Green-Star block present. Website link thomaskeller.com/tfl. Hours cut off. |
| A9 | …/sonoma/restaurant/enclos | Hours, price level, Green Star | Wed–Sat 5:30–8 PM; Sun–Tue closed. $$$$. Green-Star block present. |
| A10 | …/san-francisco/restaurant/acquerello | Hours, price level | Tue–Sat 5:30–9:45 PM; Sun & Mon closed. $$$$. |
| A11 | …/san-francisco/restaurant/birdsong | Price level; hours | $$$$. Tue 5:30–8 PM; Wed–Sat cut off. |
| A12 | …/oakland/restaurant/commis | Price level, hours | $$$$. Tue–Fri 5–9:30 PM; Mon closed; Sat cut off. |
| A13 | …/san-francisco/restaurant/kiln-1210355 | Price level, hours | $$$$. Tue–Thu 6–8 PM; Fri–Sat 5–8:30 PM; Sun & Mon closed. |
| A14 | …/san-francisco/restaurant/lazy-bear | Price level, hours | $$$$. Tue–Sat 5–11 PM; Sun & Mon closed. |
| A15 | …/san-francisco/restaurant/saison | Price level, hours | $$$$. Tue–Thu 5–9:30 PM; Fri onward cut off. |
| A16 | …/san-francisco/restaurant/sons-daughters | Address, hours, price level, Green Star | Address 2875 18th St SF CA 94110. Tue–Sat 5:30–8:30 PM; Sun & Mon closed. $$$$. Green-Star block present. |

## B. Restaurant official sites (checked this session)
| # | URL | Result |
|---|---|---|
| B1 | https://www.californiossf.com/ | Homepage: address 355 11th St; OpenTable booking. No price or hours text. |
| B2 | https://www.frenchlaundry.com/ | HTTP 500 (failed again). Michelin links thomaskeller.com/tfl instead. |
| B3 | https://enclos-sonoma.com/ | Video landing page only; no price or hours text. |
| B4 | https://singlethreadfarms.com/restaurant/ | "3 Michelin-Star Restaurant"; ten-course tasting menu; bookings released 1st of month 9 AM PST via OpenTable. No price on page. |
| B5 | https://saisonsf.com/ | "two-Michelin star open woodfire restaurant" (matches Michelin 2★). No price/hours on homepage. |
| B6 | https://www.bardessono.com/ | Instagram https://www.instagram.com/bardessonohotelspa (footer). |
| B7 | https://www.bardessono.com/contact.htm | Address: 6526 Yount St., Yountville, CA 94599. Phone +1 707-204-6000. |

## C. Not re-checked this session (values carried from prior session 88da5baf)
Prices for 2 (Benu, Acquerello, Birdsong, Commis, Kiln, Lazy Bear, Sons & Daughters, 7 Adams, Angler, Madcap, Sorrel), Instagram handles (Atelier Crenn, Lazy Bear), Bib Gourmand list (data/bib.csv), 1★ restaurants not in section A, all hotel addresses except Bardessono.

## D. Corrections made this session
- Bardessono address: 6640 Washington St (French Laundry's) → 6526 Yount St (official). 
- Hotel starred counts: SF 20 → 25; Wine Country 7 → 8 (recount from restaurants.csv).
- Hotel ordering: prior order was not by the stated metric; now sorted by cluster count (ties noted).
- Price for 2: Acquerello $708 → $731.60 (formula in row); Angler $156 → $151.20 (formula in row); Commis $669 → $669.60; Sorrel $409.50 for 2 (Fall 2026 menu, official menus page sorrelrestaurant.com/menus/, fetched 24 Nov 2026; matches PR #4).
- Green Star: Atelier Crenn No → Yes (Michelin page shows Green Star block). Others confirmed or left.
- Benu Instagram https://www.instagram.com/benu_sf/ removed (not confirmed on official site).
- Restaurant hours updated from Michelin pages (14 rows); conflicts with prior official-page hours flagged (Quince, Kiln, Lazy Bear) — see flagged.md.
- Sons & Daughters address conflict flagged (Michelin 2875 18th St vs prior 708 Bush St).
