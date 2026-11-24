# Baymich3

SF Bay Area MICHELIN Guide Explorer — an independent, mobile-friendly GitHub Pages site with verified restaurant data, hotel rankings, and full sourcing transparency.

## What's here

- **Landing page** (`index.html`) — executive summary, suggestions, open Q/I/A
- **Restaurants** (`pages/restaurants.html`) — tables by star level (3★, 2★, 1★, Listed) with addresses, prices, 2-adult estimates, phone, website, social links, days/hours, and official Michelin source link per row
- **Hotels** (`pages/hotels.html`) — ranked by nearby Michelin restaurants, with MICHELIN Keys, guest scores, and pricing
- **Verification** (`pages/verification.html`) — sources, data completeness, discrepancies, open questions

## Data policy

- No manual input; no hallucinations
- Every value verified from guide.michelin.com (official source)
- If a value can't be confirmed: left blank, flagged "unverified" — never inferred
- Every table row links to its official MICHELIN page
- "Listed in guide" ≠ "currently has a Michelin star" — both shown distinctly

## Tech

- Static HTML/CSS/JS — no build step, runs on GitHub Pages
- Data files: `data/restaurants.js`, `data/hotels.js`
- Rendering: `assets/js/app.js`

## Branch

`arena/3c9252ca-baymich3` — do not switch branches.
