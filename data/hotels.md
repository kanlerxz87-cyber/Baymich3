# Hotel ranking — method and corrections (T10, session 15c870c6)

## Method actually used in `data/hotels.csv`
- **Rank key:** number of MICHELIN-starred restaurants (2026, Core scope) in the hotel's **cluster** (C1–C5). Within a tie, the original editorial order is kept.
- **Not used (yet):** straight-line distance counts (5/10/25 mi) from verified coordinates. `data/SCOPE.md` describes this method, but no coordinates source has been verified, so it has not been applied. See Questions (Q-H1) in the flagged page.
- Consequence: all 8 SF hotels tie at 25; their order is editorial, not evidence-based.

## Starred counts used (2026, from Michelin California 2026 article, 24 Jun 2026)
| Cluster | 3★ | 2★ | 1★ | Total Core starred | Source |
|---|---|---|---|---|---|
| C1 SF Core | 4 | 6 | 15 | **25** | guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california |
| C2 Peninsula | 0 | 0 | 5 | **5** | same |
| C3 East Bay | 0 | 1 | 1 | **2** | same |
| C4 Marin | 0 | 0 | 1 | **1** | same |
| C5 Wine Country | 3 | 0 | 5 | **8** | same |

Corrections made in this session: C1 was recorded as 20 (now 25); C5 was recorded as 7 (now 8). Hotel ranks were re-sorted so that the order follows the count.

## Address status
- Carried over from the prior session (NOT re-checked this session): Four Seasons SF address (official site), Fairmont (partial), SingleThread (official page), Auberge du Soleil (partial).
- Unverified: all others. Do not use until checked against the hotel's official site.
- **Flag:** Bardessono address on file (6640 Washington St, Yountville) is the same address Michelin gives for The French Laundry. Treat as wrong until checked.

## Candidates not yet in the ranking
- **Four Seasons Resort Napa Valley (Calistoga)** — Michelin lists AURO (1★) as inside the resort (Michelin Calistoga page, fetched 24 Nov 2026). Not added; needs a decision on whether on-site restaurants count.
