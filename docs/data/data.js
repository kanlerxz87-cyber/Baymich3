/* Baymich3 — verified data registry.
 * Rules (from project brief):
 *  - Every row carries a source URL to an official site.
 *  - Values not confirmed from an official source are null and shown as "Unverified".
 *  - Nothing is inferred or estimated.
 * Last updated: 2026-11-24 (session arena/d7b7bed1-baymich3)
 */
window.BAYMICH = {
  meta: {
    updated: "2026-11-24",
    branch: "arena/d7b7bed1-baymich3",
    michelin_selection_year: 2026,
    michelin_selection_date: "2026-06-24",
    region_definition: "San Francisco Bay Area as used in this project: San Francisco, Oakland, Peninsula/South Bay (Atherton, Palo Alto, Redwood City, San Mateo, Woodside, Saratoga), Marin (San Anselmo), Napa (Calistoga, Rutherford, Saint Helena, Yountville), Sonoma (Healdsburg, Geyserville, Sonoma).",
    price_note: "Michelin lists price as $ / $$ / $$$ / $$$$ levels only. No dollar amount is shown on the official Michelin page, so no couple total is filled in."
  },

  sources: {
    michelin_ca_2026: { label: "MICHELIN Guide — Every MICHELIN-Starred Restaurant in California for 2026 (official, 24 Jun 2026)", url: "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california" },
    michelin_sf_list: { label: "MICHELIN Guide — San Francisco restaurant listing (official)", url: "https://guide.michelin.com/us/en/california/san-francisco/restaurants" },
    eater_bay_2026: { label: "Eater SF — 2026 Michelin star winners of the Bay Area (secondary, used only to cross-check)", url: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area" }
  },

  /* Star tiers are taken from the official MICHELIN 2026 California article.
   * status: "New" = new to that tier in 2026 per the article; "Promoted" = raised to 3★ in 2026.
   * Fields set to null were NOT verified on the official restaurant page yet.
   */
  starred: [
    // ---- 3 stars ----
    { name: "Californios", tier: "3★", status: "Promoted to 3★ (2026)", city: "San Francisco", area: "SF", cuisine: "Mexican, Contemporary", price: "$$$$", address: "355 11th St., San Francisco, CA 94103", hours: "Tue–Sat 5–10 PM · Sun & Mon closed", website: "https://www.californiossf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/californios", verified: "Full" },
    { name: "Enclos", tier: "3★", status: "Promoted to 3★ (2026)", city: "Sonoma", area: "Sonoma", cuisine: "Contemporary, Californian", price: "$$$$", address: "139 E. Napa St., Sonoma, CA 95476", hours: null, website: "https://enclos-sonoma.com/", michelin: "https://guide.michelin.com/us/en/california/sonoma/restaurant/enclos", verified: "Partial" },
    { name: "Atelier Crenn", tier: "3★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary, French", price: "$$$$", address: "3127 Fillmore St., San Francisco, CA 94123", hours: null, website: "https://www.ateliercrenn.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/atelier-crenn", verified: "Partial" },
    { name: "Benu", tier: "3★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Asian, Contemporary", price: "$$$$", address: "22 Hawthorne St., San Francisco, CA 94105", hours: "Wed–Thu 5–8 PM · Fri–Sat 5–8:30 PM · Mon, Tue, Sun closed", website: "https://www.benusf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/benu", verified: "Full" },
    { name: "Quince", tier: "3★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary, Californian", price: "$$$$", address: "470 Pacific Ave., San Francisco, CA 94133", hours: "Tue–Thu 5–9 PM · Fri–Sat 11:30 AM–1 PM & 5–9 PM · Mon & Sun closed", website: "https://www.quincerestaurant.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/quince", verified: "Full" },
    { name: "The French Laundry", tier: "3★", status: "Retained", city: "Yountville", area: "Napa", cuisine: "Contemporary, French", price: "$$$$", address: "6640 Washington St., Yountville, CA 94599", hours: null, website: "https://www.thomaskeller.com/tfl", michelin: "https://guide.michelin.com/us/en/california/yountville/restaurant/the-french-laundry", verified: "Partial" },
    { name: "SingleThread", tier: "3★", status: "Retained", city: "Healdsburg", area: "Sonoma", cuisine: "Contemporary, Californian", price: "$$$$", address: "131 North St., Healdsburg, CA 95448", hours: null, website: "https://www.singlethreadfarms.com/", michelin: "https://guide.michelin.com/us/en/california/healdsburg/restaurant/singlethread", verified: "Partial" },

    // ---- 2 stars ----
    { name: "Acquerello", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Italian, Contemporary", price: "$$$$", address: "1722 Sacramento St., San Francisco, CA 94109", hours: "Tue–Sat 5:30–9:45 PM · Sun & Mon closed", website: "https://www.acquerellosf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/acquerello", verified: "Full" },
    { name: "Birdsong", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary, American", price: "$$$$", address: "1085 Mission St., San Francisco, CA 94103", hours: null, website: "https://www.birdsongsf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/birdsong", verified: "Partial" },
    { name: "Kiln", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary", price: "$$$$", address: "149 Fell St., San Francisco, CA 94102", hours: "Tue–Thu 6–8 PM · Fri–Sat 5–8:30 PM · Mon & Sun closed", website: "https://www.kilnsf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/kiln-1210355", verified: "Full" },
    { name: "Lazy Bear", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary, Modern Cuisine", price: "$$$$", address: "3416 19th St., San Francisco, CA 94110", hours: "Tue–Sat 5–11 PM · Sun & Mon closed", website: "https://www.lazybearsf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/lazy-bear", verified: "Full" },
    { name: "Saison", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Californian, Contemporary", price: "$$$$", address: "178 Townsend St., San Francisco, CA 94107", hours: "Tue–Thu 5–9:30 PM · Mon closed · Fri–Sun not fully retrieved", website: "https://www.saisonsf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/saison", verified: "Partial" },
    { name: "Sons & Daughters", tier: "2★", status: "Retained", city: "San Francisco", area: "SF", cuisine: "Contemporary", price: "$$$$", address: "2875 18th St., San Francisco, CA 94110", hours: null, website: "https://www.sonsanddaughterssf.com/", michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/sons-daughters", verified: "Partial" },
    { name: "Commis", tier: "2★", status: "Retained", city: "Oakland", area: "Oakland", cuisine: "Contemporary", price: "$$$$", address: "3859 Piedmont Ave., Oakland, CA 94611", hours: "Tue–Fri 5–9:30 PM · Mon closed · Sat–Sun not fully retrieved", website: "https://www.commisrestaurant.com/", michelin: "https://guide.michelin.com/us/en/california/oakland/restaurant/commis", verified: "Partial" },

    // ---- 1 star: name/tier/city/status/Michelin link verified from official article; detail fields pending ----
    { name: "Selby's", tier: "1★", status: "Retained", city: "Atherton", area: "Peninsula", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/atherton/restaurant/selby-s", verified: "Pending" },
    { name: "Auro", tier: "1★", status: "Retained", city: "Calistoga", area: "Napa", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/calistoga/restaurant/auro", verified: "Pending" },
    { name: "Cyrus", tier: "1★", status: "Retained", city: "Geyserville", area: "Sonoma", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/geyserville/restaurant/cyrus", verified: "Pending" },
    { name: "Troubadour", tier: "1★", status: "New (2026)", city: "Healdsburg", area: "Sonoma", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/healdsburg/restaurant/troubadour", verified: "Pending" },
    { name: "Madcap", tier: "1★", status: "Retained", city: "San Anselmo", area: "Marin", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-anselmo/restaurant/madcap", verified: "Pending" },
    { name: "Press", tier: "1★", status: "Retained", city: "Saint Helena", area: "Napa", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/saint-helena/restaurant/press", verified: "Pending" },
    { name: "Protégé", tier: "1★", status: "Retained", city: "Palo Alto", area: "Peninsula", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/palo-alto/restaurant/protege", verified: "Pending" },
    { name: "Sun Moon Studio", tier: "1★", status: "Retained", city: "Oakland", area: "Oakland", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/oakland/restaurant/sun-moon-studio", verified: "Pending" },
    { name: "Auberge du Soleil", tier: "1★", status: "Retained", city: "Rutherford", area: "Napa", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/rutherford/restaurant/auberge-du-soleil", verified: "Pending" },
    { name: "7 Adams", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/7-adams", verified: "Pending" },
    { name: "Angler SF", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/angler-sf", verified: "Pending" },
    { name: "Hilda and Jesse", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/hilda-and-jesse", verified: "Pending" },
    { name: "Kin Khao", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/kin-khao", verified: "Pending" },
    { name: "Mister Jiu's", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/mister-jiu%E2%80%99s", verified: "Pending" },
    { name: "Naides", tier: "1★", status: "New (2026)", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/naides", verified: "Pending" },
    { name: "Nari", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/nari", verified: "Pending" },
    { name: "Niku Steakhouse", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/niku-steakhouse", verified: "Pending" },
    { name: "Nisei", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/nisei", verified: "Pending" },
    { name: "San Ho Won", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/san-ho-won", verified: "Pending" },
    { name: "Sorrel", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/sorrel", verified: "Pending" },
    { name: "Ssal", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/ssal", verified: "Pending" },
    { name: "State Bird Provisions", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/state-bird-provisions", verified: "Pending" },
    { name: "The Progress", tier: "1★", status: "Retained", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/the-progress", verified: "Pending" },
    { name: "Wolfsbane", tier: "1★", status: "New (2026)", city: "San Francisco", area: "SF", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-francisco/restaurant/wolfsbane", verified: "Pending" },
    { name: "Wakuriya", tier: "1★", status: "Retained", city: "San Mateo", area: "Peninsula", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/san-mateo/restaurant/wakuriya", verified: "Pending" },
    { name: "The Village Pub", tier: "1★", status: "Retained", city: "Woodside", area: "Peninsula", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/woodside/restaurant/the-village-pub", verified: "Pending" },
    { name: "Plumed Horse", tier: "1★", status: "Retained", city: "Saratoga", area: "South Bay", cuisine: null, price: null, address: null, hours: null, website: null, michelin: "https://guide.michelin.com/us/en/california/saratoga/restaurant/plumed-horse", verified: "Pending" }
  ],

  /* Removed from the starred list in 2026 per Michelin/Eater reporting. Michelin listing status not yet verified. */
  lost_stars_sf_2026: [
    { name: "Le Comptoir at Bar Crenn", note: "Not in the 2026 starred list. Chef Dominique Crenn announced in June 2026 plans to close it (Eater).", source: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area", verified: "Partial" },
    { name: "O' by Claude Le Tohic", note: "Star reported removed in 2026 (Eater). Not in the 2026 starred list.", source: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area", verified: "Partial" },
    { name: "Shota", note: "Star reported removed in 2026 (Eater). Not in the 2026 starred list.", source: "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area", verified: "Partial" }
  ]
};
