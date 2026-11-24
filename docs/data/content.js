/* Narrative content for the Baymich3 site. Every factual claim cites a source URL.
 * Items marked decision:true are suggestions awaiting the user's choice; nothing is implemented until chosen.
 */
window.BAYMICH_CONTENT = {

  executive_summary: [
    { k: "Starred restaurants (Bay Area, 2026)", v: "41 total: 7 three-star, 7 two-star, 27 one-star.", src: "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california" },
    { k: "Changes in 2026", v: "New to 3★: Californios (SF) and Enclos (Sonoma). New to 2★ from SF list: none in the Bay Area (Kato is Los Angeles). New 1★ in the Bay Area: Troubadour (Healdsburg), Naides (SF), Wolfsbane (SF).", src: "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california" },
    { k: "Reported star losses (SF)", v: "Le Comptoir at Bar Crenn, O' by Claude Le Tohic and Shota are reported removed from one-star status. Official listing status still to be confirmed.", src: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area" },
    { k: "Verification level", v: "14 of 41 starred restaurants have address, price level, hours and website (or partial hours) verified on the official Michelin page. 27 one-star entries are verified for name, city, star and Michelin link only.", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurants" },
    { k: "Price for 2 adults", v: "Michelin lists only $–$$$$ price levels. No dollar total is listed, so none is entered on this site.", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios" },
    { k: "Not yet covered", v: "Bib Gourmand list, hotel ranking by nearby Michelin restaurants, YouTube/TikTok/Instagram links, and per-restaurant couple prices. These are open tasks (see COORDINATION.md T3–T7).", src: "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/d7b7bed1-baymich3/COORDINATION.md" }
  ],

  /* Questions that must be answered before any decision can reasonably be made */
  questions: [
    { q: "Which definition of 'Bay Area' should the guide use?", status: "Answered (proposed)", a: "This project uses: SF, Oakland, Peninsula/South Bay, Marin, Napa, Sonoma. Michelin's own regional grouping should be confirmed.", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurants", decision: true },
    { q: "Which Michelin tiers should appear? (3★, 2★, 1★, Bib Gourmand, Recommended)", status: "Partly answered", a: "Stars: answered from the official 2026 California article. Bib Gourmand and Recommended: not yet gathered.", src: "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california" },
    { q: "What is the exact couple price (2 adults) at each restaurant?", status: "Unanswered", a: "Michelin gives only $ levels. Exact menu prices must come from each restaurant's own official site or booking page, which is not yet done.", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios" },
    { q: "Which hours and days are open for each restaurant, including exceptions?", status: "Partly answered", a: "14 restaurants have hours from the official Michelin page; some are partial. The other 27 one-stars and several others are pending.", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/benu" },
    { q: "How should hotels be ranked (count of starred restaurants within a radius, or by star weight)?", status: "Unanswered — decision needed", a: "Not yet gathered. The ranking method must be chosen by you (see Suggestions).", src: "https://guide.michelin.com/us/en/hotels", decision: true },
    { q: "Should social links (YouTube / TikTok / Instagram) be official-channel only, or any creator?", status: "Unanswered — decision needed", a: "Choice affects how links are verified. Suggest official-only as the default.", src: "", decision: true },
    { q: "Should lost-star restaurants (Le Comptoir at Bar Crenn, O' by Claude Le Tohic, Shota) stay in the list as 'former star'?", status: "Unanswered — decision needed", a: "Michelin's official listing status for each is not yet verified.", src: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area", decision: true },
    { q: "Who is the site audience (personal planning, group trip, or public)?", status: "Unanswered — decision needed", a: "Affects how much detail and how many pages are needed.", src: "", decision: true },
    { q: "Is a LICENSE needed for the repository?", status: "Unanswered — decision needed", a: "Repo has no LICENSE file. Choice is a legal decision for you.", src: "https://github.com/kanlerxz87-cyber/Baymich3", decision: true }
  ],

  /* Suggestions. Nothing here is implemented until the user picks an option. */
  suggestions: [
    { id: "S1", title: "Finish the 27 one-star restaurant detail rows", detail: "Visit each official Michelin page to fill address, cuisine, price level, hours and website. Estimated effort: about 27 page checks.", benefit: "Full coverage of starred list.", decision: true },
    { id: "S2", title: "Add a 'Lost stars' sub-page", detail: "Track restaurants that lost stars in 2026 with their official listing status.", benefit: "Avoids stale recommendations.", decision: true },
    { id: "S3", title: "Hotel ranking by starred restaurants within a set radius", detail: "Use official Michelin hotel pages and the restaurant addresses above. Ranking method (radius, weighting) needs your choice.", benefit: "Answers the hotel question directly.", decision: true },
    { id: "S4", title: "Couple price from official menus only", detail: "Record the exact tasting-menu price where the restaurant publishes it. Otherwise leave blank and flag.", benefit: "Real verified pricing with no guesses.", decision: true },
    { id: "S5", title: "Social links from official channels only", detail: "Only link a restaurant's own verified YouTube, TikTok or Instagram account.", benefit: "Avoids unverified creator content.", decision: true },
    { id: "S6", title: "Map view by neighborhood", detail: "Add an interactive map once addresses are verified for every row. Requires a map provider decision.", benefit: "Visual clustering of starred restaurants.", decision: true },
    { id: "S7", title: "Add a LICENSE and a real README", detail: "Currently the README is a title only and there is no LICENSE.", benefit: "Clear reuse rules and onboarding.", decision: true }
  ],

  /* Flagged items shown on the Flagged for review page */
  flags: [
    { id: "F1", type: "Unverified", item: "27 one-star restaurants: address, cuisine, price, hours, website", status: "needs review", src: "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california" },
    { id: "F2", type: "Unverified", item: "Couple totals for 2 adults (no dollar figures on Michelin)", status: "needs review", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios" },
    { id: "F3", type: "Partial", item: "Hours truncated for Saison (Fri–Sun), Commis (Sat–Sun), Enclos, Atelier Crenn, French Laundry, SingleThread, Birdsong, Sons & Daughters", status: "needs review", src: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/saison" },
    { id: "F4", type: "Conflict check", item: "Lost-star restaurants (Le Comptoir at Bar Crenn, O' by Claude Le Tohic, Shota) — Eater reports removal; Michelin listing not yet checked", status: "needs review", src: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area" },
    { id: "F5", type: "Repo irregularity", item: "README.md contains only the title", status: "needs review", src: "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/d7b7bed1-baymich3/README.md" },
    { id: "F6", type: "Repo irregularity", item: "No LICENSE file in the repository", status: "needs review", src: "https://github.com/kanlerxz87-cyber/Baymich3" },
    { id: "F7", type: "Scope gap", item: "Bib Gourmand, hotels, social links and couple prices not yet collected", status: "needs review", src: "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/d7b7bed1-baymich3/COORDINATION.md" }
  ]
};
