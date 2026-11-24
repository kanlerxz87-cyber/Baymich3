# Shared Task Board (COORDINATION.md)

Protocol: claim a task here, commit + push the claim, then work only inside the claimed file scope.
Statuses: unclaimed | in progress | done | needs review (needs review = published on the Flagged for Review page and does not block anything).

**Branch note:** the session is fixed to branch `arena/8bc23e0f-baymich3`. All sessions in this repo are asked to use `session-<id>/<task>` branches, but the platform only allows work on the current branch, so this session commits to `arena/8bc23e0f-baymich3` and logs its work here instead.

| Task ID | Task | Status | Owner session | File scope | Notes |
|---|---|---|---|---|---|
| T1 | Repo review (README, git state, irregularities) | in progress | arena-8bc23e0f | `docs/flags.html`, `docs/data/flags.json` | claimed 2026-11-24 |
| T2 | Michelin Bay Area starred + Bib Gourmand dataset | in progress | arena-8bc23e0f | `docs/data/michelin.json`, `docs/restaurants.html` | claimed 2026-11-24 |
| T3 | Hotels ranked by nearby Michelin restaurants | unclaimed | — | `docs/hotels.html`, `docs/data/hotels.json` | Not done this pass; blocked on verified hotel addresses |
| T4 | Executive summary, questions, improvement suggestions | in progress | arena-8bc23e0f | `docs/summary.html`, `docs/suggestions.html`, `docs/questions.html` | claimed 2026-11-24 |
| T5 | Site shell, landing page, GitHub Pages config | in progress | arena-8bc23e0f | `docs/index.html`, `docs/assets/*`, `docs/.nojekyll` | claimed 2026-11-24 |
| T6 | Final integration (merge, re-verify, publish) | unclaimed | — | all shared outputs | Reserved for the final integration session |

## Log
- 2026-11-24 arena-8bc23e0f: Claimed T1, T2, T4, T5. Repo at start contained only `README.md` (`# Baymich3`) and no COORDINATION.md; this file was created.
