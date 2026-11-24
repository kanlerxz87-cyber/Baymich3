# Coordination

This file is the shared task board for the repository. Keep task scopes non-overlapping and record official-source verification and irregularities here before marking work done.

## Session / branch constraints

- Active session identifier used for this task: `arena/35713f68-baymich3` (the current Arena branch; this session must remain on it).
- Current branch: `arena/35713f68-baymich3`.
- No other task claims were present when this board was created.
- The repository currently contains only a minimal README, so the active claim covers the end-to-end first implementation. No parallel task is being assumed or overwritten.

## Task board

| Task | Status | Owner / session ID | File scope |
|---|---|---|---|
| Bay Area Michelin guide: source audit, verified dataset, mobile-first site, QA, and GitHub Pages-ready delivery | in progress | `arena/35713f68-baymich3` | `COORDINATION.md`, `README.md`, `index.html`, `assets/`, `data/`, `.github/` |

## Work log

- Claim created before implementation. The task is being treated as the first and only active integration task because no other claims or task files existed in the checkout.
- Verification policy: Michelin status, restaurant pricing, operating hours, hotel prices, amenities, and activity details are populated only where an official Michelin, restaurant, hotel, or attraction source explicitly confirms the value. Missing/unclear values stay blank and appear on the review page. Third-party/social platforms are only linked when an official account or an official site links to that account.
- Deployment policy: prepare a static GitHub Pages-compatible site and document the required repository Pages setting; do not claim a live deployment unless GitHub Pages is confirmed active.
