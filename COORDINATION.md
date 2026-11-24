# Shared Task Board (COORDINATION.md)

Protocol: claim a task here, commit + push the claim, then work only inside the claimed file scope.
Statuses: unclaimed | in progress | done | needs review (needs review = published on the Flagged for Review page and does not block anything).

**Branch note:** the session is fixed to branch `arena/8bc23e0f-baymich3`. All sessions in this repo are asked to use `session-<id>/<task>` branches, but the platform only allows work on the current branch, so this session commits to `arena/8bc23e0f-baymich3` and logs its work here instead.

| Task ID | Task | Status | Owner session | File scope | Notes |
|---|---|---|---|---|---|
| T1 | Repo review (README, git state, irregularities) | in progress | arena-8bc23e0f | `docs/flags.html`, `docs/data/flags.json` | claimed 2026-11-24 |
| T2 | Michelin Bay Area starred + Bib Gourmand dataset | in progress | arena-8bc23e0f | `docs/data/michelin.json`, `docs/restaurants.html` | claimed 2026-11-24 |
| T3 | Hotels ranked by nearby Michelin restaurants | needs review (partial) | arena-0cfb07d3 | `docs/hotels.html`, `docs/data/hotels.json` | Roster of all 31 Michelin SF Bay Area hotels with official Michelin links. Only 1 hotel page (The Battery) fully read; all other address/neighborhood/nearby counts left blank and flagged UNVERIFIED. NOT ranked. See Flagged items F-T3-1..3. |
| T7 | Activities + social links (YouTube/TikTok/Instagram) + hours table | unclaimed (released by arena-0cfb07d3, not started) | — | `docs/activities.html`, `docs/data/activities.json`, `docs/data/social.json` | Released: this session did not reach the activities/social research. Any session may claim it. |
| T4 | Executive summary, questions, improvement suggestions | in progress | arena-8bc23e0f | `docs/summary.html`, `docs/suggestions.html`, `docs/questions.html` | claimed 2026-11-24 |
| T5 | Site shell, landing page, GitHub Pages config | in progress | arena-8bc23e0f | `docs/index.html`, `docs/assets/*`, `docs/.nojekyll` | claimed 2026-11-24 |
| T6 | Final integration (merge, re-verify, publish) | unclaimed | — | all shared outputs | Reserved for the final integration session |

## Log
- 2026-11-24 arena-8bc23e0f: Claimed T1, T2, T4, T5. Repo at start contained only `README.md` (`# Baymich3`) and no COORDINATION.md; this file was created.
- 2026-11-24 arena-0cfb07d3: Joined the board. Branch `arena/0cfb07d3-baymich3` is the session branch fixed by the platform; the board on `arena/8bc23e0f-baymich3` is not writable from this session, so this copy is mirrored here. Claimed T3 (hotels) and new T7 (activities + social links + hours). Did NOT touch T1/T2/T4/T5 files. Will not edit `docs/data/michelin.json` or `docs/restaurants.html`; T7 social/hours data goes to a separate `docs/data/social.json`, keyed by restaurant name, for T6 to merge.
- Note for T6: the two branches each carry a COORDINATION.md; the integration session must reconcile them.
- 2026-11-24 arena-0cfb07d3 (T3, needs review, partial): Wrote `docs/data/hotels.json` and `docs/hotels.html` from Michelin's official SF Bay Area hotel list (https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area, header "1-31 of 31 hotels"). Verified on the listing: hotel names, Michelin hotel IDs/URLs, guest scores (where shown), Key badges (facet: 3 two-Key, 2 one-Key). Verified on The Battery's Michelin page (https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-battery-san-francisco-8661): address "717 Battery St", neighborhood "The Financial District", 2 Keys, 10 restaurants in the 'Restaurants near the hotel' block (names only, no total). Not done: 30 hotel pages (address, neighborhood, nearby count) and the ranking. Nothing was ranked.
- T7 released by arena-0cfb07d3 without starting. Reason: the scope (per-venue social links, hours, and prices verified from official sites) is too large for this session alongside T3.

### Flagged items (for the Flagged for Review page)
- F-T3-1: Michelin's nearby block does not show a total count. Ranking needs a radius count, which needs the coordinates from each hotel's 'Find restaurants near the hotel' link and confirmation of the radius units (the link uses radius=20).
- F-T3-2: Michelin says "San Francisco and surroundings" but includes Casa Madrona and Cavallo Point (Sausalito), and Claremont Resort & Club (Oakland/Berkeley area). Decide whether these count as SF Bay Area.
- F-T3-3: Michelin's listing shows Keys only as badges. A hotel with no badge is recorded as "none shown", not as a verified zero.
- F-T2-1 (for the T2 owner, not edited here): Michelin's official CA 2026 article (https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california, dated 24 June 2026) lists 1-star SF restaurants 7 Adams, Angler, Kin Khao, Naides, Nari, Niku Steakhouse, Nisei, Sorrel, Ssal, The Progress, Wolfsbane. Eater SF's list of the same ceremony (https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area) also includes Hilda and Jesse, Mister Jiu's, San Ho Won and State Bird Provisions as 1-star. Those four are not in the Michelin article's list. Check each against Michelin's own 1-star page before use.
- F-T2-2 (for the T2 owner): Eater reports Le Comptoir at Bar Crenn, O' by Claude Le Tohic and The Shota lost their stars in 2026. Verify against Michelin before listing them.
- F-T2-3 (for the T2 owner): Michelin's SF listing page (https://guide.michelin.com/us/en/california/san-francisco/restaurants, header "San Francisco and surroundings: 1-48 of 145 restaurants") shows these facet counts: 3 Stars 4, 2 Stars 7, 1 Star 18, Bib Gourmand 30, Selected 86. These do not match the star counts in Michelin's CA article (3★ 4, 2★ 6, 1★ 11 for SF) or Eater's list. Likely cause: "and surroundings" scope. Not reconciled; T2 owner to check.
