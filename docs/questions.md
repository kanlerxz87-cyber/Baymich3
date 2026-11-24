# Questions, Information & Answers — What Must Be Resolved Before Deciding

Each question states: **What we know (verified) / What we don't know / How to discover it / Owner**. No decision should be made on Unverified rows.

## Q1. Which Michelin edition should we trust?
- **Know:** 2026 is latest (June 2026). 2025 list is superseded. Californios/Enclos are 3★ in 2026 (were 2★ in 2025).
- **Don't know:** Will 2027 change stars? (Unknowable; check June 2027 ceremony.)
- **Discover:** Re-check guide.michelin.com California 2026 article each quarter; subscribe to Michelin newsletter.
- **Owner:** Site maintainer. **Blocks:** All star claims.

## Q2. What counts as "Bay Area"?
- **Know:** This project uses 9-county Core + flagged Extension (Carmel/Elk) + excluded Sacramento. Michelin "SF and surroundings" (145) blends them.
- **Don't know:** User's travel radius (e.g., will they drive to Elk/Carmel?).
- **Discover:** Ask user for max drive time / base city; re-cut hotel ranking accordingly.
- **Owner:** User. **Blocks:** Hotel ranking, itinerary.

## Q3. What will dinner for 2 actually cost?
- **Know:** 12 rows verified (Benu, Acquerello, Birdsong, Commis, Kiln, Lazy Bear, Sons & Daughters, 7 Adams, Angler lunch, Madcap, Sorrel, Auberge via Tock). Formula shown per row.
- **Don't know:** 29 rows Unverified (official price not on fetched page). Service % missing on 4 verified rows. Tax, wine, supplements extra.
- **Discover:** Visit each official site's Reservations/Tock page (prices live there, not homepage); screenshot + date-stamp; update CSV. For Quince/Californios/SingleThread/French Laundry/Enclos/Saison, check Tock/OpenTable booking page (restaurant-controlled).
- **Owner:** Research session. **Blocks:** Budgeting.

## Q4. When is each restaurant open? Any closures/exceptions?
- **Know:** 10 rows verified (Benu Wed-Sat, Quince Tue-Sat + Nov26/Dec25-26 closed, Birdsong Tue-Sat, Kiln Tue-Thu/Fri-Sat split, Lazy Bear Tue-Sat 5-9, Angler Daily lunch/dinner, Mister Jiu's Tue-Sat, Nari 7 nights, Nisei Wed-Sun, Madcap Tue-Sat).
- **Don't know:** 34 rows Unverified. Holiday/seasonal exceptions mostly unknown.
- **Discover:** Fetch each official site's Hours/Visit page + Michelin individual page (Days open filter). Check Instagram for pop-up closures.
- **Owner:** Research session. **Blocks:** Booking dates.

## Q5. Where are the YouTube/TikTok/Instagram links?
- **Know:** 3 Instagram verified (Atelier @atelier.crenn via official sameAs, Benu @benu_sf via search, Lazy Bear @lazybearsf via official dinner page). YouTube/TikTok: 0 verified.
- **Don't know:** 41 rows social Unverified. Restaurant-owned vs fan accounts unclear.
- **Discover:** (1) Fetch official site footer for social icons (authoritative). (2) Search Instagram/YouTube/TikTok for exact restaurant name + city; only link if handle matches official site or Michelin page. (3) Record handle + URL + date checked.
- **Owner:** Research session. **Blocks:** Social proof / marketing.

## Q6. Which hotel should we book? What does it cost per night?
- **Know:** 14 hotels ranked by cluster density (method on hotels page). 2 addresses verified (Four Seasons, Fairmont partial). No nightly rates collected.
- **Don't know:** Nightly rates (dynamic), Michelin Keys status, parking/valet, cancellation, pet policy, accessibility.
- **Discover:** Check Michelin Guide Hotels (Keys) + official hotel site Rates page for sample dates; record date + occupancy. Do not use third-party rate blogs.
- **Owner:** User (dates/budget) + research session. **Blocks:** Booking.

## Q7. What about Bib Gourmand and Recommended (non-starred) restaurants?
- **Know:** Bib Bay Area ~36 names (data/bib.csv) verified via Michelin Bib page + OpenTable 2026 list. Recommended SF surroundings = 86 (Michelin count).
- **Don't know:** Full Recommended names list (86) not yet enumerated; Bib prices/hours/social Unverified.
- **Discover:** Paginate Michelin SF restaurants search (145 = 29+30+86) and transcribe names + Michelin URLs; then verify Bib prices/hours for top picks.
- **Owner:** Research session. **Blocks:** Value itinerary.

## Q8. Which 2025 stars disappeared in 2026 — are they closed or demoted?
- **Know:** Le Comptoir, O' by Claude Le Tohic, The Shota absent from 2026 starred list. Osito/Aphotic closed (Chronicle 2025). Chez TJ → Recommended (Chronicle 2025).
- **Don't know:** Current status of Le Comptoir/O'/Shota (closed? renamed? Recommended?).
- **Discover:** Check Michelin individual pages + official sites for each; update Flagged page.
- **Owner:** Research session. **Blocks:** Avoid booking closed venues.

## Q9. How do we get there? Drive time, transit, parking?
- **Know:** Addresses for 20 rows (official/secondary). Kiln parking/transit detail (official). Most parking Unverified.
- **Don't know:** Drive times from each hotel, BART/Muni routes, valet cost (Benu $30 verified; others unknown).
- **Discover:** Use Google Maps directions from chosen hotel (record date/time); check official site Parking page.
- **Owner:** User + research. **Blocks:** Itinerary feasibility.

## Q10. Dietary, allergies, dress code, cancellation, minimum age?
- **Know:** Kiln (no modifications), Commis (vegetarian/pescatarian only, no vegan), Sons & Daughters (pescatarian/vegetarian 48h), Lazy Bear (no butter exclusion). Others unknown.
- **Don't know:** 40 rows dietary/cancellation unknown.
- **Discover:** Fetch each official site's FAQ/Policies page; do not assume.
- **Owner:** Research session. **Blocks:** Suitability.

## Q11. How fresh is this data? When to re-verify?
- **Know:** Checked 24 Nov 2026. Michelin 2026 (June 2026). Prices seasonal (Sorrel Fall $125 vs Summer $195).
- **Don't know:** Next Michelin update date; seasonal menu change dates.
- **Discover:** Re-verify quarterly + before any booking; date-stamp every price/hours cell.
- **Owner:** Maintainer. **Blocks:** All decisions (staleness risk).

## Q12. What is the decision this site supports?
- **Know:** Site supports: pick cluster → pick hotel → pick restaurants → budget for 2.
- **Don't know:** User's dates, party size (2 assumed), budget cap, cuisine preferences, mobility needs.
- **Discover:** Ask user (or default to 2 adults, no cap, all cuisines — current assumption, flagged).
- **Owner:** User. **Blocks:** Personalization.
