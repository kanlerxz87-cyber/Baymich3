/*
 * Source data. Star levels and city assignments come from the official MICHELIN
 * Guide California 2026 rollup (source linked on every restaurant row).
 * Pricing, schedules, restaurant social handles and direct restaurant URLs are
 * intentionally empty unless independently confirmed from an official source.
 */
const MICHELIN_SOURCE = 'https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california';
const MICHELIN_PROFILE_ROOT = 'https://guide.michelin.com/us/en/california';

const restaurants = [
  // 3 stars
  ['Atelier Crenn','San Francisco',3,'san-francisco','atelier-crenn'],
  ['Benu','San Francisco',3,'san-francisco','benu'],
  ['Californios','San Francisco',3,'san-francisco','californios'],
  ['Quince','San Francisco',3,'san-francisco','quince'],
  ['SingleThread','Healdsburg',3,'healdsburg','singlethread'],
  ['Enclos','Sonoma',3,'sonoma','enclos'],
  ['The French Laundry','Yountville',3,'yountville','the-french-laundry'],
  // 2 stars
  ['Acquerello','San Francisco',2,'san-francisco','acquerello'],
  ['Birdsong','San Francisco',2,'san-francisco','birdsong'],
  ['Kiln','San Francisco',2,'san-francisco','kiln-1210355'],
  ['Lazy Bear','San Francisco',2,'san-francisco','lazy-bear'],
  ['Saison','San Francisco',2,'san-francisco','saison'],
  ['Sons & Daughters','San Francisco',2,'san-francisco','sons-daughters'],
  ['Commis','Oakland',2,'oakland','commis'],
  // 1 star
  ['7 Adams','San Francisco',1,'san-francisco','7-adams'],
  ['Angler SF','San Francisco',1,'san-francisco','angler-sf'],
  ['Kin Khao','San Francisco',1,'san-francisco','kin-khao'],
  ['Restaurant Naides','San Francisco',1,'san-francisco','naides'],
  ['Nari','San Francisco',1,'san-francisco','nari'],
  ['Niku Steakhouse','San Francisco',1,'san-francisco','niku-steakhouse'],
  ['Nisei','San Francisco',1,'san-francisco','nisei'],
  ['Sorrel','San Francisco',1,'san-francisco','sorrel'],
  ['Ssal','San Francisco',1,'san-francisco','ssal'],
  ['The Progress','San Francisco',1,'san-francisco','the-progress'],
  ['Wolfsbane','San Francisco',1,'san-francisco','wolfsbane'],
  ['Troubadour','Healdsburg',1,'healdsburg','troubadour'],
  ['Sun Moon Studio','Oakland',1,'oakland','sun-moon-studio'],
  ["Selby's",'Atherton',1,'atherton','selby-s'],
  ['Auro','Calistoga',1,'calistoga','auro'],
  ['Cyrus','Geyserville',1,'geyserville','cyrus'],
  ['Protégé','Palo Alto',1,'palo-alto','protege'],
  ['Auberge du Soleil','Rutherford',1,'rutherford','auberge-du-soleil'],
  ['Press','Saint Helena',1,'saint-helena','press'],
  ['Madcap','San Anselmo',1,'san-anselmo','madcap'],
  ['Wakuriya','San Mateo',1,'san-mateo','wakuriya'],
  ['Plumed Horse','Saratoga',1,'saratoga','plumed-horse'],
  ['The Village Pub','Woodside',1,'woodside','the-village-pub']
].map(([name,city,stars,place,slug]) => ({
  name,
  city,
  stars,
  distinction: `${stars} ${stars === 1 ? 'Star' : 'Stars'}`,
  profile: `${MICHELIN_PROFILE_ROOT}/${place}/restaurant/${slug}`,
  source: MICHELIN_SOURCE,
  sourceLabel: 'MICHELIN 2026',
  // No current official menu total or restaurant schedule was verified in this research pass.
  coupleTotal: '',
  hours: '',
  officialWebsite: '',
  social: ''
}));

// Official links and weekly schedules visible on the linked MICHELIN profiles during this pass.
// Exceptional closures/holiday overrides were not provided and still require rechecking.
const verifiedRestaurantDetails = {
  '7 Adams': { officialWebsite: 'https://www.7adamsrestaurant.com/', hours: 'Mon–Thu 5:30–9 PM; Fri–Sat 5–10 PM; Sun 5–9 PM.' },
  'Kiln': { officialWebsite: 'https://www.kilnsf.com/', hours: 'Mon/Sun closed; Tue–Thu 6–8 PM; Fri–Sat 5–8:30 PM.' },
  'Enclos': { officialWebsite: 'https://enclos-sonoma.com/', hours: 'Mon/Tue/Sun closed; Wed–Sat 5:30–8 PM.' },
  'Troubadour': { officialWebsite: 'https://www.troubadourhbg.com/', hours: 'Mon–Wed closed; Thu–Sun 5:30–8:30 PM.' },
  "Selby's": { officialWebsite: 'https://www.selbysrestaurant.com/', hours: 'Daily 5–9 PM.' },
  'Restaurant Naides': { officialWebsite: 'https://www.restaurantnaides.com/', hours: 'Mon–Wed closed; Thu–Sun 5:30–8:30 PM.' },
  'Auberge du Soleil': { officialWebsite: 'https://auberge.com/auberge-du-soleil/dine/the-restaurant-at-auberge-du-soleil/' },
  'Auro': { officialWebsite: 'https://www.auronapavalley.com/', hours: 'Mon/Tue/Sun closed; Wed–Sat 5–9 PM.' },
  'Press': { officialWebsite: 'https://www.pressnapavalley.com/', hours: 'Mon–Thu 5–9 PM; Fri–Sat 5–10 PM; Sun 5–9 PM.' },
  'Madcap': { officialWebsite: 'https://www.madcapmarin.com/', hours: 'Mon/Sun closed; Tue–Thu 5:30–8:30 PM; Fri–Sat 5:30–9 PM.' },
  'Protégé': { officialWebsite: 'https://www.protegepaloalto.com/' },
  'Wakuriya': { officialWebsite: 'https://www.wakuriya.com/' },
  'Plumed Horse': { officialWebsite: 'https://plumedhorse.com/', hours: 'Mon closed; Tue–Sun 5–10 PM.' },
  'The Village Pub': { officialWebsite: 'https://www.thevillagepub.net/' },
  'Sun Moon Studio': { officialWebsite: 'https://www.sunmoonstudio.com/', hours: 'Mon–Wed closed; Thu–Sat 5–9 PM; Sun 5–8 PM.' },
  'Cyrus': { officialWebsite: 'https://www.cyrusrestaurant.com/' }
};
restaurants.forEach((restaurant) => Object.assign(restaurant, verifiedRestaurantDetails[restaurant.name] || {}));

// A small, separately labelled sample of current non-star MICHELIN Guide listings.
// This is not a complete inventory of all non-starred selections in the region.
const guideSelections = [
  { name: 'MAMA Oakland', city: 'Oakland', distinction: 'Bib Gourmand', stars: 0, profile: 'https://guide.michelin.com/us/en/california/oakland/restaurant/mama-oakland', source: 'https://guide.michelin.com/us/en/california/oakland/restaurant/mama-oakland', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Bombera', city: 'Oakland', distinction: 'Bib Gourmand', stars: 0, profile: 'https://guide.michelin.com/us/en/california/oakland/restaurant/bombera', source: 'https://guide.michelin.com/us/en/california/oakland/restaurant/bombera', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Snail Bar', city: 'Oakland', distinction: 'Bib Gourmand', stars: 0, profile: 'https://guide.michelin.com/us/en/california/oakland/restaurant/snail-bar', source: 'https://guide.michelin.com/us/en/california/oakland/restaurant/snail-bar', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Soba Ichi', city: 'Oakland', distinction: 'Guide Selected', stars: 0, profile: 'https://guide.michelin.com/us/en/california/oakland/restaurant/soba-ichi', source: 'https://guide.michelin.com/us/en/california/oakland/restaurant/soba-ichi', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Teni East Kitchen', city: 'Oakland', distinction: 'Guide Selected', stars: 0, profile: 'https://guide.michelin.com/us/en/california/oakland/restaurant/teni-east-kitchen', source: 'https://guide.michelin.com/us/en/california/oakland/restaurant/teni-east-kitchen', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Pausa', city: 'San Mateo', distinction: 'Guide Selected', stars: 0, profile: 'https://guide.michelin.com/us/en/california/san-mateo/restaurant/pausa', source: 'https://guide.michelin.com/us/en/california/san-mateo/restaurant/pausa', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Zola', city: 'Palo Alto', distinction: 'Guide Selected', stars: 0, profile: 'https://guide.michelin.com/us/en/california/palo-alto/restaurant/zola', source: 'https://guide.michelin.com/us/en/california/palo-alto/restaurant/zola', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'El Molino Central', city: 'Sonoma', distinction: 'Bib Gourmand', stars: 0, profile: 'https://guide.michelin.com/us/en/california/sonoma/restaurant/el-molino-central', source: 'https://guide.michelin.com/us/en/california/sonoma/restaurant/el-molino-central', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' },
  { name: 'Valley', city: 'Sonoma', distinction: 'Bib Gourmand', stars: 0, profile: 'https://guide.michelin.com/us/en/california/sonoma/restaurant/valley', source: 'https://guide.michelin.com/us/en/california/sonoma/restaurant/valley', sourceLabel: 'MICHELIN profile', coupleTotal: '', hours: '', officialWebsite: '', social: '' }
];

const allRestaurantRecords = [...restaurants, ...guideSelections];

const hotels = [
  {
    name: 'Four Seasons Hotel San Francisco at Embarcadero',
    area: 'Embarcadero · San Francisco',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/four-seasons-hotel-san-francisco-at-embarcadero-12158',
    note: 'MICHELIN Guide hotel selection; Embarcadero location. Exact nearby-restaurant radius/count not audited.',
    rank: null,
    nearbyCount: null,
    rate: ''
  },
  {
    name: 'The Ritz-Carlton, San Francisco',
    area: 'Nob Hill · San Francisco',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-ritz-carlton-san-francisco-9470',
    note: 'MICHELIN Guide hotel selection. A Dec 22–23, 2026 quote is separately documented; it is not a general rate.',
    rank: null,
    nearbyCount: null,
    rate: ''
  },
  {
    name: 'Hotel G San Francisco',
    area: 'Union Square · San Francisco',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/hotel-g-san-francisco-8562',
    note: 'MICHELIN Guide hotel selection; Union Square location. Exact nearby-restaurant radius/count not audited.',
    rank: null,
    nearbyCount: null,
    rate: ''
  },
  {
    name: 'The St. Regis Hotel San Francisco',
    area: 'SoMa · San Francisco',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/st-regis-hotel-san-francisco-7468',
    note: 'MICHELIN Guide hotel selection; SoMa location. Exact nearby-restaurant radius/count not audited.',
    rank: null,
    nearbyCount: null,
    rate: ''
  },
  {
    name: 'Graduate by Hilton Berkeley',
    area: 'Berkeley · East Bay',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/graduate-by-hilton-berkeley-8914',
    note: 'MICHELIN Guide hotel selection. The current star rollup has no starred restaurant entry under Berkeley; this is not a claim that Berkeley has no Guide restaurants.',
    rank: null,
    nearbyCount: null,
    rate: ''
  },
  {
    name: 'Casa Madrona Hotel & Spa',
    area: 'Sausalito · Marin County',
    source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/casa-madrona-hotel-spa-6946',
    note: 'MICHELIN Guide hotel selection; Sausalito location. Exact nearby-restaurant radius/count not audited.',
    rank: null,
    nearbyCount: null,
    rate: ''
  }
];

const decisions = [
  { question: 'What is the exact Bay Area boundary for this trip?', why: 'This dataset uses cities in the official 2026 California star list across the nine-county Bay Area plus Yountville. Michelin’s “San Francisco and surroundings” directory is not identical to every possible regional definition.', missing: 'Confirm the counties/cities to include, and whether Yountville/Napa wine-country stops belong in the trip.' },
  { question: 'What dates and meal periods are being considered?', why: 'Menus, hours, closures, hotel rates and reservation availability are date-specific. An all-year hours summary can be misleading around holidays and special events.', missing: 'Choose dates, weekdays, lunch/dinner preference, and any date flexibility.' },
  { question: 'What should “cost for two adults” include?', why: 'An entree/menu total can exclude beverage pairing, supplements, tax, service charge, gratuity, and optional upgrades.', missing: 'Set a per-meal ceiling and decide whether to include drinks, tax, service, tip, and supplements.' },
  { question: 'How should restaurant proximity be measured for hotels?', why: 'Straight-line distance, walk time, transit time, driving time, and “same neighborhood” produce different rankings.', missing: 'Pick a radius or max walk/transit time; set whether to count starred restaurants only or all Michelin Guide selections.' },
  { question: 'What hotel constraints matter most?', why: 'A ranking by restaurant density alone ignores stay cost, accessibility, parking, cancellation, and desired hotel class.', missing: 'Set nightly budget, party/room count, accessibility needs, parking needs, and hotel preferences.' },
  { question: 'Which non-starred Michelin Guide entries should be covered?', why: 'The 2026 statewide star rollup does not represent every selected restaurant or Bib Gourmand. The live San Francisco directory has a much wider selection.', missing: 'Decide whether to include all guide-selected restaurants, Bib Gourmand, Green Star, or only starred restaurants.' },
  { question: 'Which social platforms count as an acceptable official link?', why: 'Unverified fan pages, user posts, and impersonators are not reliable source links; availability varies by venue.', missing: 'Include official Instagram/TikTok/YouTube only, or allow a venue’s own video/media page when a verified account is absent.' }
];

const suggestions = [
  { id: 'scope', title: 'Lock the trip boundary and dates first', detail: 'Then freeze the research scope and rebuild schedules, rates, booking windows, and seasonal hours against those dates.', effort: 'Recommended first' },
  { id: 'restaurant-cost', title: 'Add itemized two-person cost ranges', detail: 'Use restaurant-owned menus or booking pages; include mandatory supplements, tax, service, and label optional beverage pairings separately.', effort: 'High impact' },
  { id: 'hotel-radius', title: 'Score hotels with explicit walk/transit bands', detail: 'Geocode official restaurant and hotel addresses, count current Michelin selections within a defined travel-time band, and show the sources and date used.', effort: 'High impact' },
  { id: 'social-hours', title: 'Verify schedules and official social channels', detail: 'Check each restaurant’s own website for weekly hours, holiday notices, closure dates, booking link, and linked social profiles; leave absent fields blank.', effort: 'Completeness' },
  { id: 'guide-list', title: 'Expand beyond starred venues', detail: 'Add all current MICHELIN-selected and Bib Gourmand restaurants in the chosen area, with explicit “Guide Selected” versus “Bib Gourmand” labels.', effort: 'Broader discovery' },
  { id: 'activities', title: 'Add food-focused activities as a separate category', detail: 'Only add market tours, wineries, cooking classes, and attractions after checking the operator’s official page and official social channel.', effort: 'Optional scope' }
];

const reviewItems = [
  { severity: 'High', title: 'Current star list needs link-by-link restaurant-profile validation', detail: 'Star distinctions and cities are taken from the official 2026 roundup. Direct profile URLs are generated using MICHELIN Guide URL conventions and should be opened and checked before publication as individual profile links.', source: MICHELIN_SOURCE },
  { severity: 'High', title: 'No two-adult restaurant totals are confirmed', detail: 'A total requires a current official menu or booking price, plus a consistent rule for tax, service, beverages, and supplements. Cells remain blank; Michelin price symbols are not converted to dollar totals.', source: MICHELIN_SOURCE },
  { severity: 'High', title: 'Restaurant schedules, holiday exceptions, and social links are incomplete', detail: 'Weekly hours and official website links are populated only where visible on a checked MICHELIN profile. Remaining cells are blank; holiday exceptions and all official Instagram/TikTok/YouTube accounts still need venue-by-venue verification.', source: MICHELIN_SOURCE },
  { severity: 'High', title: 'Hotel scores and live rates remain unranked', detail: 'No user dates or proximity rule were provided. The documented Ritz-Carlton example is $673 total including taxes for one night, one adult, one room, Dec 22–23, 2026; it is not comparable to other properties or dates.', source: 'https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-ritz-carlton-san-francisco-9470?arr=2026-12-22&dep=2026-12-23&nA=1&nC=0&nR=1' },
  { severity: 'Medium', title: 'The regional directory is not the same as the complete star rollup', detail: 'The restaurant table includes starred restaurants only. Non-starred Guide-selected, Bib Gourmand, and Green Star distinctions need separate complete records and labels.', source: 'https://guide.michelin.com/us/en/california/san-francisco/restaurants' },
  { severity: 'Medium', title: 'City-level clusters are not neighborhood density', detail: 'Counts group entries by the city named in the MICHELIN 2026 star rollup. They do not establish walking distance to any candidate hotel and do not count all Guide-listed restaurants.', source: MICHELIN_SOURCE },
  { severity: 'Medium', title: 'Map locations are city searches, not verified venue pins', detail: 'No coordinates are invented. Individual address geocoding and routing should be added only after restaurant profiles and hotel locations are verified.', source: 'https://guide.michelin.com/us/en/california/san-francisco/restaurants' },
  { severity: 'Medium', title: 'No activities are currently listed', detail: 'No food tours, winery visits, attractions, or other activity rows are included in this verified starter dataset. Add an activity only after checking its official operator page and official social links.', source: 'https://guide.michelin.com/us/en/travel-guides' },
  { severity: 'Low', title: 'The official compilation is a snapshot, not a permanence guarantee', detail: 'MICHELIN can update distinctions and its selection. Recheck the current restaurant profile and the restaurant’s own booking page before reserving.', source: MICHELIN_SOURCE }
];
