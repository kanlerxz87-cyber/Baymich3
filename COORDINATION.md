# Shared Task Board (COORDINATION.md)

Protocol: claim a task here, commit + push the claim, then work only inside the claimed file scope.
Statuses: unclaimed | in progress | done | needs review (needs review = published on the Flagged for Review page and does not block anything).

**Branch note:** the session is fixed to branch `arena/8bc23e0f-baymich3`. All sessions in this repo are asked to use `session-<id>/<task>` branches, but the platform only allows work on the current branch, so this session commits to `arena/8bc23e0f-baymich3` and logs its work here instead.

| Task ID | Task | Status | Owner session | File scope | Notes |
|---|---|---|---|---|---|
| T1 | Repo review (README, git state, irregularities) | needs review | arena-8bc23e0f | `docs/flags.html`, `docs/data/flags.json` | claimed 2026-11-24 |
| T2 | Michelin Bay Area starred + Bib Gourmand dataset | needs review | arena-8bc23e0f | `docs/data/michelin.json`, `docs/stars.html`, `docs/bib.html`, `scripts/build_site.py` | claimed 2026-11-24 |
| T3 | Hotels ranked by nearby Michelin restaurants | unclaimed | — | `docs/hotels.html`, `docs/data/hotels.json` | Not done this pass; blocked on verified hotel addresses (see Flagged R12) |
| T4 | Executive summary, questions, improvement suggestions | needs review | arena-8bc23e0f | `docs/summary.html`, `docs/suggestions.html`, `docs/questions.html` | claimed 2026-11-24 |
| T5 | Site shell, landing page, GitHub Pages config | needs review | arena-8bc23e0f | `docs/index.html`, `docs/assets/*`, `docs/.nojekyll`, `scripts/build_site.py` | claimed 2026-11-24 |
| T6 | Final integration (merge, re-verify, publish) | unclaimed | — | all shared outputs | Reserved for the final integration session |

## Log
- 2026-11-24 arena-8bc23e0f: Claimed T1, T2, T4, T5. Repo at start contained only `README.md` (`# Baymich3`) and no COORDINATION.md; this file was created.

### T1 Repo review: sources, verification, irregularities
- Sources: repo tree and git log (`git log`, `git status`); README.md read line by line (`# Baymich3`, one line).
- Irregularities (all on `docs/flags.html`, R1-R4): repo has no code/license/CI; COORDINATION.md missing at start; branch naming rule conflicts with the fixed branch; escaped placeholders in the brief's branch name.

### T2 Michelin dataset: sources, verification, irregularities
- Official sources: Michelin 2026 California article https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california ; Michelin press release https://www.michelin.com/en/publications/products-and-services/the-michelin-guide-california-2026 ; Michelin Bib article https://guide.michelin.com/us/en/article/michelin-guide-ceremony/california-s-most-affordable-restaurants-in-2026
- Michelin restaurant pages fetched (address, price tier, hours where shown): Californios, Enclos, SingleThread, Atelier Crenn, Benu, Quince.
- Verified: 41 Bay Area starred restaurants (7 three-star, 7 two-star, 27 one-star); 25 in San Francisco. Counted per county.
- NOT verified (left blank and flagged): exact 2-adult prices (Michelin gives tiers only); hours for 35 starred restaurants; social links for all rows; Bib rows without Michelin address.
- Irregularities: Selby's city conflict (R5); three star losses only from secondary press (R6); Michelin Bib article count inconsistent (R7); 8 Bib rows only in OpenTable reproduction (R8); French Laundry page URL attempt failed (R9).

### T4 / T5 site
- Pages built by `scripts/build_site.py` from `docs/data/michelin.json`. Internal links checked (none broken). External links point to the sources above.

## Log (continued)
- 2026-11-24 arena-8bc23e0f: T1, T2, T4, T5 completed to "needs review". Published to `docs/` on this branch. T3 (hotels) not started: blocked on verified hotel addresses. T6 (integration) left for the integration session.
