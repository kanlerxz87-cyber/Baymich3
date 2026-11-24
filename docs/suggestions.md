# Suggestions — Site Improvements for Better Decision-Making (Review Before Implementing)

> **Status:** Suggestions only. Nothing here is implemented until reviewed and chosen. Each suggestion lists: Problem → Change → Effort → Risk → Decision needed.

## S1. Verified-price badge + "Budget for 2" calculator
- **Problem:** Users can't tell verified vs indicative prices at a glance.
- **Change:** Add green "Verified" / amber "Unverified" badge per row; calculator: enter party size + wine pairing toggle → total incl. service %. Pulls from CSV.
- **Effort:** Medium (JS + CSV). **Risk:** Low. **Decision:** Approve badge colors + tax inclusion (currently excl. tax).

## S2. Cluster map with real pins (Leaflet + geocoded addresses)
- **Problem:** Map page currently links to Michelin/Google search (no pins). Users can't see density.
- **Change:** Geocode each verified address (Nominatim/OSM, date-stamped) → Leaflet pins colored by stars; hotel pins; 5/10/25 mi circles. Fallback to list if geocode fails.
- **Effort:** High (geocoding 44 addresses + QA). **Risk:** Medium (coordinate accuracy). **Decision:** Approve OSM vs Google (ToS) + accuracy disclaimer.

## S3. "Bookable now?" checker
- **Problem:** Hours/prices stale; users book closed venues (e.g., dropped 2025 stars).
- **Change:** Per-row "Last checked" date; auto-flag rows >90 days old; link to Tock/OpenTable/Resy booking page (from official site).
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve staleness threshold (90 days?) + booking links policy.

## S4. Hotel total-trip cost estimator
- **Problem:** Hotel ranking ignores nightly rate; restaurant cost dominates.
- **Change:** Add sample-date nightly rate (official site, date-stamped) + 3-night total + dinner total = trip total. Rank by value (stars per $) as secondary sort.
- **Effort:** High (rates change daily). **Risk:** Medium (stale rates mislead). **Decision:** Approve sample dates + refresh cadence.

## S5. Social proof wall (verified handles only)
- **Problem:** Social links sparse (3/44). Users want video previews.
- **Change:** Collect official Instagram/YouTube/TikTok via official-site footers; embed Instagram grid (official embed) + YouTube playlist per cluster. Mark fan accounts separately.
- **Effort:** High (44×3 searches). **Risk:** Low. **Decision:** Approve platforms priority (Instagram first?) + embed vs link.

## S6. Bib vs Star value comparison
- **Problem:** Bib (value) buried; users overpay for stars.
- **Change:** "Value picks" view: Bib + 1★ under $200pp for 2, sorted by price. Show $/star metric.
- **Effort:** Low (filter on existing data). **Risk:** Low. **Decision:** Approve price threshold.

## S7. Itinerary builder (cluster → hotel → 3 dinners)
- **Problem:** Tables don't make an itinerary.
- **Change:** Pick hotel → auto-suggest 3 restaurants in same cluster (1×3★/2★ + 1×1★ + 1×Bib) with total cost + days-open check. Export/print.
- **Effort:** High. **Risk:** Medium (availability not real-time). **Decision:** Approve scope (print-only vs save).

## S8. Accessibility & mobile polish
- **Problem:** Tables hard on mobile; color-only badges fail WCAG.
- **Change:** Card view <640px (already planned), text labels on badges, keyboard nav, contrast AA, reduced-motion.
- **Effort:** Medium. **Risk:** Low. **Decision:** Approve WCAG AA target.

## S9. Data freshness + changelog
- **Problem:** No audit trail.
- **Change:** CHANGELOG.md + per-row source URL + checked date; GitHub Actions link checker (weekly).
- **Effort:** Low-Medium. **Risk:** Low. **Decision:** Approve checker (broken-link PRs?).

## S10. Recommended (86) full enumeration
- **Problem:** 86 Recommended names missing; value dining incomplete.
- **Change:** Transcribe Michelin SF search pagination → data/recommended.csv → Listed page table.
- **Effort:** Medium (manual transcription + QA). **Risk:** Low. **Decision:** Approve (full 86 vs top 30?).

## Decision log (fill after review)
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
