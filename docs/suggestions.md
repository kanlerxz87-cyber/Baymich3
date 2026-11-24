# Suggestions — Review Before Anything Is Implemented

> **Status: proposals only.** Nothing below is implemented unless you choose it. Each item lists the problem, the change, effort, risk, and the decision needed from you.
> (Exception: the table layout and mobile card view were built to meet the "mobile friendly" requirement, and corrections to data are listed in the Flagged page.)

## S1. Verified-price badge and "budget for 2" calculator
- **Problem:** Hard to tell verified prices from blanks at a glance.
- **Change:** Green/amber badge per row; a calculator with party size and wine-pairing toggle that shows the total including the service charge.
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve badge colors; whether to include tax.

## S2. Map with real pins
- **Problem:** The map page links to Michelin and Google search; it has no pins.
- **Change:** Geocode each verified address (OpenStreetMap, date-stamped); Leaflet pins colored by star count; hotel pins; 5/10/25-mile rings.
- **Effort:** High. **Risk:** Medium (coordinate accuracy). **Decision:** Approve the map provider and an accuracy note.

## S3. "Last checked" dates and staleness warnings
- **Problem:** Hours and prices go stale; users may book a closed venue.
- **Change:** Show the checked date on each row; flag rows older than 90 days; link to the official booking page.
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve the 90-day threshold.

## S4. Hotel trip-cost estimator
- **Problem:** Ranking ignores nightly rates; restaurant costs dominate the budget.
- **Change:** Add official nightly rates for sample dates, then a trip total (nights + dinners).
- **Effort:** High (rates change daily). **Risk:** Medium (stale rates). **Decision:** Approve sample dates and refresh cadence.

## S5. Social links (verified handles only)
- **Problem:** Only 2 Instagram handles are verified; no YouTube or TikTok.
- **Change:** Collect handles from official-site footers; show them per row; keep fan accounts separate.
- **Effort:** High (about 41 restaurants × 3 platforms). **Risk:** Low. **Decision:** Approve platform priority (Instagram first?) and whether to embed or link.

## S6. Value view: Bib and 1★ under a price cap
- **Problem:** Good-value restaurants are hard to find.
- **Change:** A filtered view (Bib + 1★ under a set price for two), sorted by price.
- **Effort:** Low. **Risk:** Low. **Decision:** Approve the price cap.

## S7. Itinerary builder
- **Problem:** Tables do not turn into a plan.
- **Change:** Pick a hotel → suggest three restaurants in the same cluster (one 2★/3★, one 1★, one Bib) with a total cost and days-open check. Printable.
- **Effort:** High. **Risk:** Medium (no live availability). **Decision:** Approve scope (print-only or saved).

## S8. Accessibility polish
- **Problem:** Colour-only badges; keyboard and contrast not audited.
- **Change:** Text labels on all badges (done for status), keyboard navigation, WCAG AA contrast check.
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve WCAG AA as the target.

## S9. Data change log and link checker
- **Problem:** No audit trail; links can break silently.
- **Change:** CHANGELOG.md; per-row source URL and checked date; weekly link-check job.
- **Effort:** Low–medium. **Risk:** Low. **Decision:** Approve the weekly check and whether it opens PRs.

## S10. Full Recommended list (86)
- **Problem:** The 86 Selected restaurants are not listed; value dining is incomplete.
- **Change:** Transcribe Michelin's SF list into data/recommended.csv and show it on the Bib & Listed page.
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve full list or the top 30.

## S11. Distance-based hotel ranking
- **Problem:** Hotels in the same cluster are tied (Flagged F13).
- **Change:** Verify coordinates from each official address; rank by the number of starred restaurants within 5, 10 and 25 miles.
- **Effort:** Medium. **Risk:** Low–medium (geocoder accuracy). **Decision:** Approve the radius bands.

## S12. Automated Michelin re-check
- **Problem:** The Michelin hours check was done by hand, page by page (about 9k tokens each).
- **Change:** A scheduled job fetches each Michelin restaurant page, extracts hours and price level, and opens a PR when a value changes.
- **Effort:** Medium–high. **Risk:** Medium (page structure may change; Michelin terms of use). **Decision:** Approve, or keep manual checks.

## S13. Resolve the repository's open PRs
- **Problem:** PR #1 and PR #2 (from earlier sessions) conflict with this branch's files.
- **Change:** Close them or rebase onto the current site.
- **Effort:** Low. **Risk:** Low. **Decision:** Approve closing or rebasing.

## Decision log (fill in after review)
| Suggestion | Chosen? | Date | Notes |
|---|---|---|---|
| S1 | — | — | — |
| S2 | — | — | — |
| S3 | — | — | — |
| S4 | — | — | — |
| S5 | — | — | — |
| S6 | — | — | — |
| S7 | — | — | — |
| S8 | — | — | — |
| S9 | — | — | — |
| S10 | — | — | — |
| S11 | — | — | — |
| S12 | — | — | — |
| S13 | — | — | — |
