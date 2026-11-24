# SF Bay Area Michelin guide

A small, source-led static dashboard for current Michelin-starred restaurants across the nine-county San Francisco Bay Area, plus explicit verification gaps for costs, restaurant hours/social links, hotel pricing, and proximity ranking.

## Local preview

Open `index.html` directly, or run any static HTTP server from the repository root. The page is dependency-free and works as a GitHub Pages static site.

## Live site

`.github/workflows/pages.yml` publishes the static files to GitHub Pages through GitHub Actions on pushes and manual workflow dispatch. The repository must have Pages configured to use **GitHub Actions**. The live address is assigned by GitHub after the first successful deployment; check the repository's Pages settings or Actions deployment output.

## Data and verification rules

- The 37 restaurant rows are the Bay Area subset of the MICHELIN Guide California 2026 official star rollup: 7 three-star, 7 two-star, and 23 one-star restaurants.
- Each restaurant row links to an official MICHELIN Guide profile URL and to the official 2026 source rollup. The round-up is the verified source for current star distinction and city; the data file flags profile-link-by-profile-link validation as open review.
- Only official-source-confirmed values are populated. Two-adult meal totals, hours/exceptions, direct restaurant websites, and official social handles are deliberately left blank pending individual verification. Michelin's $ symbols are not converted into totals.
- Hotel entries are candidates in the official MICHELIN hotel selection. They are not ranked by nearby restaurant count because a distance/travel-time method and stay dates were not selected. A date-specific official Ritz-Carlton quote is disclosed as a single example, not a general rate.
- City clusters count only the starred records in this dataset. They are not counts of all Guide-selected or Bib Gourmand restaurants and do not imply walkable proximity to a hotel.
- This is not yet a complete inventory of all non-starred Michelin Guide listings, social accounts, schedules, or dining budgets. These gaps are clearly flagged in the dashboard.

## Primary sources

- [MICHELIN Guide California 2026 — complete star rollup](https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california)
- [MICHELIN Guide San Francisco & surroundings restaurant directory](https://guide.michelin.com/us/en/california/san-francisco/restaurants)
- [MICHELIN Guide San Francisco Bay Area hotels](https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area)
- [The Ritz-Carlton, San Francisco — date-specific MICHELIN Guide quote](https://guide.michelin.com/us/en/hotels-stays/san-francisco-bay-area/the-ritz-carlton-san-francisco-9470?arr=2026-12-22&dep=2026-12-23&nA=1&nC=0&nR=1)

Snapshot date: 2026-11-24. Recheck official sources before booking; Michelin distinctions and restaurant operations can change.
