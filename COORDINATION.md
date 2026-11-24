# Coordination board

Session branch: `arena/f4837132-baymich3` (Arena-managed; do not create/switch branches).

| Task | Status | Owner session ID | File scope |
|---|---|---|---|
| Full project integration: verified Bay Area Michelin guide, decision-support content, responsive site, and Pages setup | needs review | arena/f4837132-baymich3 | all project files except `.git/` |

## Log and verification
- 2026-11-24 — Claim recorded by `arena/f4837132-baymich3`. Repository initially contained only a 10-byte README and no coordination board, data, or app. No other remote task claims were present. This session owns full integration.
- Primary official source checked: [Michelin Guide California 2025 selection](https://www.michelin.com/en/publications/products-and-services/michelin-guide-california-2025-selection), published June 27, 2025. Its text explicitly confirms Enclos (Sonoma) entered the selection with two stars and Kiln (San Francisco) was promoted from one star to two. Both populated restaurant rows link to this source. This source is dated 2025 and does not verify 2026 status.
- Verification performed: fetched and read the official Michelin release; checked site HTML parses; checked all internal navigation anchors resolve and IDs are unique; `git diff --check` passes. No guessed prices, hours, social profiles, coordinates, hotels, or rankings were added. Such omissions are explicitly flagged in the UI.
- Irregularities / open verification: this is a partial sample, not the complete Bay Area selection. Official prices, hours, current selection, hotel/date quotes, official social accounts, addresses, and full guide listings remain unverified. Hotel ranking and map density require more primary-source data and a defined travel radius.
- Pages deployment workflow added, but publication is not confirmed. The repository needs GitHub Pages set to GitHub Actions and a successful workflow run. The current branch did not exist on `origin` at start; `git pull --rebase origin arena/f4837132-baymich3` therefore failed with “couldn't find remote ref” after the initial claim commit. No branch was switched.
