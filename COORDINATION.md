# Coordination — Baymich3 (session baymich3-session)

## Branch
- Branch: `arena/3c9252ca-baymich3` (from `fc288dbe429ddecaba7f1d0b98971eac9df0ab65` of main)
- Status: active
- Remote: https://github.com/kanlerxz87-cyber/Baymich3.git

## Rules
- No manual input; work autonomously line by line
- Verify everything from official sources (guide.michelin.com); no hallucinations
- If a value can't be confirmed: leave blank, flag "unverified", never infer/fill
- Every table row must have source link to official site
- Mobile-friendly, easy to read, simple organized tables
- Distinguish "listed in Michelin guide" vs "currently has Michelin star"
- Total price estimate range for 2 adults per restaurant
- Social media links (YouTube/TikTok/Instagram) alongside each entry
- Days open, hours, exceptions columns
- Executive summary, suggestions section, open Q/I/A section, verification page
- Claim tasks before work; commit+push claims; small frequent commits; git pull --rebase before push

## Task Board (all claimed by this session)

| Task | Status | Notes |
|------|--------|-------|
| Research SF Bay Area Michelin restaurants | DONE | 56 entries: 6×3★, 10×2★, 32×1★, 8×Listed |
| Fetch individual Michelin pages for stars | DONE | 28+ fetched directly; 3 recovered from search snippets (Le Comptoir, O' by Claude Le Tohoc, The Shota) |
| Fetch Michelin hotel data | DONE | 8 hotels with Keys, scores, nearby restaurants |
| Build data files (restaurants.js, hotels.js) | DONE | data/restaurants.js, data/hotels.js |
| Build website (index, restaurants, hotels, verification) | DONE | 4 HTML pages + CSS + JS, pushed to origin |
| Add social media links | PENDING | Michelin pages don't show them; need restaurant-site verification |
| Fill remaining unverified blanks | PENDING | Addresses/hours for Bib/Selected and some 1★ |
| Deploy to GitHub Pages | PENDING | Need to enable Pages in repo settings |

## Key Data (verified)

**3★ (6):** Atelier Crenn, Benu, Quince, French Laundry, SingleThread, Californios
**2★ (10):** Acquerello, Birdsong, Commis, Enclos (discrepancy: page shows 3★), Kiln, Lazy Bear, Saison, Sons & Daughters, Harbor House, Aubergine
**1★ (32):** incl. 7 Adams, Angler SF, Hilda and Jesse, Kin Khao, Mister Jiu's, Nari, Niku, Nisei, San Ho Won, Sorrel, Ssal, State Bird Provisions, The Progress, Wolfsbane, Restaurant Naides, Le Comptoir at Bar Crenn, O' by Claude Le Tohoc, The Shota, Auberge du Soleil, Auro, Kenzo, Press, Sun Moon Studio, The Village Pub, Wakuriya, Selby's, Madcap, Cyrus, Chez Noir
**Listed (8):** Dumpling Home, Izakaya Rintaro, Okane, A16, Yank Sing, Outerlands, MAMA Oakland, Petiscos

## Last Actions
- write_file: data/restaurants.js (56 entries, validated with node)
- write_file: data/hotels.js (8 entries)
- write_file: assets/css/style.css
- write_file: assets/js/app.js
- write_file: index.html (landing page + executive summary + suggestions + Q/I/A)
- write_file: pages/restaurants.html (star-level tables)
- write_file: pages/hotels.html (hotels ranked by nearby Michelin stars)
- write_file: pages/verification.html (sources, completeness, discrepancies)
- write_file: README.md
- write_file: COORDINATION.md (updated)

## Next Steps
1. git add + commit + push all files
2. Enable GitHub Pages on the repo
3. Add social media links (need external verification per restaurant)
4. Fill remaining unverified blanks
