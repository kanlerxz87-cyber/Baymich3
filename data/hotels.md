# Hotel candidates — scope and verification

The 14 properties in `data/hotels.csv` are **unranked candidates**, not hotel recommendations or Michelin Key ratings. The `starred_in_cluster` field is an area-level count from the official 2026 starred set; it does not indicate how many starred restaurants are close to an individual hotel.

## Cluster totals (context only)

| Cluster | 3★ | 2★ | 1★ | Core starred total | Source |
|---|---:|---:|---:|---:|---|
| C1 SF Core | 4 | 6 | 15 | 25 | [MICHELIN Guide California 2026](https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california) |
| C2 Peninsula | 0 | 0 | 5 | 5 | same |
| C3 East Bay | 0 | 1 | 1 | 2 | same |
| C4 Marin | 0 | 0 | 1 | 1 | same |
| C5 Wine Country | 3 | 0 | 5 | 8 | same |

These sum to 41 Core stars. They are not proximity scores. The candidate table does not publish a rank, distance, or walkability claim.

## Why there is no ranking

- Verified official street addresses and coordinates are incomplete for the full hotel list.
- No measurement rule has been chosen: straight-line radius, walking, transit, or driving distance produce different results.
- Stay-date room rates and Michelin Key status are not verified consistently.
- Whether a hotel's on-site starred restaurant should count separately remains unresolved (Questions Q13–Q14).

Keep properties unranked until addresses, a coordinate source, a distance method, and on-site scoring rules are explicitly documented. Do not infer addresses from nearby restaurants or landmarks. Keep an unsupported value blank and flag it.

## Data-source policy

Every listed address is retained only with its row-level verification status and official property source. Michelin's hotel directory link is a directory, not proof that a specific property has a Michelin Key or individual listing. See `data/hotels.csv`, [Flagged for Review](../docs/flagged-review.md), and [Questions](../docs/questions.md).
