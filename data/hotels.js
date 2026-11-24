// Baymich3 — SF Bay Area Michelin Hotel Data
// Verified from guide.michelin.com hotel pages.
// Keys: 1 = very special stay, 2 = exceptional stay, 3 = extraordinary stay.
// Price estimate = per night for 2 adults, before tax/fees. Blank = unverified.
// Nearby Michelin restaurants = from hotel page's "Restaurants near the hotel" section.

const MICHELIN_HOTELS = [

{
  id: "auberge-du-soleil-hotel",
  name: "Auberge du Soleil, Auberge Collection",
  city: "Rutherford",
  address: "180 Rutherford Hill Rd., Rutherford, CA 94573",
  michelinKeys: 3,
  keyLabel: "Three MICHELIN Keys · extraordinary stay",
  guestScore: "18.9",
  priceEstimate2Adults: "$600–$1,200+",
  phone: "+1 707-967-3111",
  website: "https://auberge.com/auberge-du-soleil/",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/auberge-du-soleil-auberge-collection-7246",
  nearbyMichelinRestaurants: ["The Restaurant at Auberge du Soleil (1★)"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "3 MICHELIN Keys. On-site 1★ restaurant."
},
{
  id: "four-seasons-napa",
  name: "Four Seasons Resort Napa Valley",
  city: "Calistoga",
  address: "400 Silverado Trl., Calistoga, CA 94515",
  michelinKeys: 1,
  keyLabel: "One MICHELIN Key · a very special stay",
  guestScore: "19.2",
  priceEstimate2Adults: "$500–$900+",
  phone: "+1 707-709-2100",
  website: "https://www.fourseasons.com/napa/",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/four-seasons-resort-napa-valley-12465",
  nearbyMichelinRestaurants: ["Auro (1★)"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "1 MICHELIN Key. On-site 1★ restaurant (Auro)."
},
{
  id: "canyon-ranch-woodside",
  name: "Canyon Ranch Woodside",
  city: "Woodside",
  address: "800 Summit Rd., Woodside, CA 94062",
  michelinKeys: 3,
  keyLabel: "Three MICHELIN Keys · extraordinary stay",
  guestScore: null,
  priceEstimate2Adults: "$500–$900+",
  phone: null,
  website: "https://www.canyonranch.com/woodside/",
  michelinUrl: null,
  nearbyMichelinRestaurants: ["The Village Pub (1★)"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "3 MICHELIN Keys (per Michelin Guide to California article). Data unverified — placeholder."
},
{
  id: "1-hotel-san-francisco",
  name: "1 Hotel San Francisco",
  city: "San Francisco",
  address: "8 Mission Street, San Francisco, CA 94105",
  michelinKeys: 1,
  keyLabel: "One MICHELIN Key · a very special stay",
  guestScore: null,
  priceEstimate2Adults: "$400–$700",
  phone: null,
  website: "https://www.1hotels.com/san-francisco",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/1-hotel-san-francisco-12973",
  nearbyMichelinRestaurants: ["Angler SF (1★)"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "1 MICHELIN Key. Near Angler SF."
},
{
  id: "the-battery",
  name: "The Battery",
  city: "San Francisco",
  address: "717 Battery St, San Francisco, CA 94111",
  michelinKeys: 2,
  keyLabel: "Two MICHELIN Keys · an exceptional stay",
  guestScore: "19.4",
  priceEstimate2Adults: "$500–$900+",
  phone: null,
  website: "https://thebattery.com/",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-battery-san-francisco-8661",
  nearbyMichelinRestaurants: ["Trestle (Bib)", "Prelude", "Z & Y", "Harborview"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "2 MICHELIN Keys. Highest guest score (19.4) in this set."
},
{
  id: "four-seasons-embarcadero",
  name: "Four Seasons Hotel San Francisco at Embarcadero",
  city: "San Francisco",
  address: "222 Sansome Street, San Francisco, CA 94111",
  michelinKeys: 2,
  keyLabel: "Two MICHELIN Keys · an exceptional stay",
  guestScore: null,
  priceEstimate2Adults: "$500–$900+",
  phone: null,
  website: "https://www.fourseasons.com/sanfrancisco/",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/four-seasons-hotel-san-francisco-at-embarcadero-12158",
  nearbyMichelinRestaurants: ["Kusakabe", "Four Kings"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "2 MICHELIN Keys. Top floors of 345 California Center."
},
{
  id: "cavallo-point-lodge",
  name: "Cavallo Point Lodge",
  city: "Sausalito",
  address: "601 Murray Circle, Fort Baker, Sausalito, CA 94965",
  michelinKeys: 2,
  keyLabel: "Two MICHELIN Keys · an exceptional stay",
  guestScore: "18.9",
  priceEstimate2Adults: "$400–$700",
  phone: null,
  website: "https://www.cavallopoint.com/",
  michelinUrl: "https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/cavallo-point-lodge-5433",
  nearbyMichelinRestaurants: ["Atelier Crenn (3★)", "Pearl 6101"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "2 MICHELIN Keys. Marin Headlands, near Golden Gate Bridge."
},
{
  id: "lauberge-carmel",
  name: "L'Auberge Carmel",
  city: "Carmel-by-the-Sea",
  address: "682 Monte Verde St., Carmel-by-the-Sea, CA 93921",
  michelinKeys: null,
  keyLabel: "MICHELIN Guide hotel",
  guestScore: null,
  priceEstimate2Adults: "$400–$700",
  phone: "+1 831-624-8578",
  website: "https://www.auberginecarmel.com/",
  michelinUrl: null,
  nearbyMichelinRestaurants: ["Aubergine (2★)"],
  social: { youtube: null, tiktok: null, instagram: null },
  notes: "Home of 2★ Aubergine. Key rating unverified."
}

];

function getHotels() { return MICHELIN_HOTELS; }
function getHotelsByKeys(k) { return MICHELIN_HOTELS.filter(h => h.michelinKeys === k); }

console.log("Baymich3 hotel data loaded:", MICHELIN_HOTELS.length, "entries");