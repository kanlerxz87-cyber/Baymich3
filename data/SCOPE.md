# Scope Definition — SF Bay Area Michelin Project

## Geographic scope (verified definition)
**Core Bay Area (9-county):** San Francisco, San Mateo, Santa Clara, Alameda, Contra Costa, Marin, Sonoma, Napa, Solano counties.
This is the standard U.S. Census / OMB definition of the San Francisco Bay Area. All "Core" rows in this project fall inside these 9 counties.

**Extension (flagged separately, NOT core):**
- Carmel-by-the-Sea / Monterey County (Aubergine 2★, Chez Noir 1★) — ~90 mi south of SF, Central Coast.
- Elk / Mendocino County (Harbor House Inn 2★) — ~150 mi north, Mendocino Coast.
- Sacramento (The Kitchen 1★, Localis 1★) — separate metro, excluded from core counts; listed in appendix for reference only.

Rationale: Michelin markets "San Francisco and surroundings" (145 restaurants) which blends core + nearby. This project separates Core vs Extension so hotel-density math is honest. Every row carries a `scope` flag: Core / Extension / Excluded-metro.

## Michelin edition used
**MICHELIN Guide California 2026**, revealed 24–26 June 2026.
- Official source 1: https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california (24 June 2026)
- Official source 2: https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026 (26 June 2026)
- Statewide totals (2026): 83 starred (10×3★, 13×2★, 60×1★), 18 Green Star, 117 Bib Gourmand, 323 Recommended = 523 total.
- San Francisco and surroundings (Michelin search): 145 restaurants = 29 starred + 30 Bib Gourmand + 86 Selected/Recommended. (guide.michelin.com/us/en/california/san-francisco/restaurants)

## Distinction definitions (per Michelin)
- 3 Stars: "Exceptional cuisine, worth a special journey"
- 2 Stars: "Excellent cooking, worth a detour"
- 1 Star: "High quality cooking, worth a stop"
- Green Star: sustainability leader (can co-exist with Stars)
- Bib Gourmand: "Good quality, good value cooking" — NOT a star
- Selected / Recommended: in Guide, no star, no Bib

## Verification rule (strict)
- Every row must have a source link to an official site (Michelin Guide or restaurant's own site).
- If a value (price, hours, social) cannot be confirmed from an official source, leave BLANK and flag `Unverified`.
- Never infer, estimate from third-party blogs, or fill from memory. Third-party prices (Tock/OpenTable/press) are recorded separately as "Indicative (non-official)" and never presented as verified.
- Pricing for 2 adults = (per-person tasting price × 2) + service charge where official site states it. Tax excluded unless official site includes it. Show formula.

## Clusters (for hotel ranking)
- C1 SF Core (SF city: SoMa, Mission, Hayes Valley, Pacific Heights, etc.)
- C2 Peninsula / South Bay (San Mateo, Palo Alto, Saratoga, Woodside, Atherton)
- C3 East Bay (Oakland, Berkeley, Alameda)
- C4 Marin / North Bay gateway (San Anselmo, Mill Valley, Fairfax)
- C5 Wine Country — Napa / Sonoma (Yountville, Rutherford, Calistoga, St Helena, Healdsburg, Sonoma, Geyserville)
- C6 Extension coast (Carmel, Elk) — flagged, not used for core hotel ranking

Hotel ranking method: count of Core starred restaurants within 5 mi / 10 mi / 25 mi straight-line from hotel address (computed from published addresses), plus cluster total. See data/hotels.md for method + caveats. Distances are indicative (address-to-address), not drive-time.
