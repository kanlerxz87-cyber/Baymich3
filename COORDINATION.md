# Coordination

| Task | Status | Owning session | File scope |
|---|---|---|---|
| Bay Area Michelin guide site: research framework, official-source-backed dataset, responsive dashboard, decision questions, and review flags | done | arena/1a2441ec-baymich3 | `index.html`, `styles.css`, `app.js`, `data.js`, `README.md`, `.github/workflows/pages.yml`, `COORDINATION.md` |

## Handoff / environment note

The repository started with only `README.md`; no other task was claimed. Arena requires this work to remain on the current branch, so this task is being handled on `arena/1a2441ec-baymich3` rather than creating or switching to a `session-*` branch. Shared data and navigation will be integrated only after source checks for this task. No separate agent sessions are visible in this workspace.

## Verification log

- Primary official restaurant source checked: [MICHELIN Guide California 2026 starred restaurant rollup](https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california). It lists all current California stars; the Bay Area rows in `data.js` were counted line by line against the rollup: 7 three-star, 7 two-star, 23 one-star (37 total). The city assigned to each row matches the locality printed in that source.
- Official profile pages opened in this pass (per prior fetch record): 7 Adams, Kiln, Enclos, Troubadour, Selby's, Auberge du Soleil, Restaurant Naides, Press, Protégé, Auro, Cyrus, Madcap, Wakuriya, Plumed Horse, The Village Pub, Sun Moon Studio. Star distinction and profile links were checked against these pages; profile-published hours and official websites were added only where they appeared in fetched content. Every other generated profile link remains open for link-by-link validation.
- Non-star sample (MAMA Oakland, Bombera, Snail Bar, Soba Ichi, Teni East Kitchen, Pausa, Zola, El Molino Central, Valley) is included with profile links only; these records were NOT individually fetched and verified in this pass, so they remain open for verification. Bib Gourmand is kept distinct from stars. This is explicitly a sample, not a complete regional non-star list.
- Hotel candidates (Four Seasons SF Embarcadero, Ritz-Carlton SF, Hotel G SF, St. Regis SF, Graduate Berkeley, Casa Madrona) are listed as candidates with profile links only; their profiles were NOT all fetched in this pass. Ritz-Carlton SF: the official Michelin hotel profile was fetched for Dec 22–23, 2026, 1 adult, 1 room and showed a total of $673 including taxes. This is a single date-specific example, not a comparable rate or a hotel ranking.
- Repository checks: `node --check app.js`, `node --check data.js`, runtime count check (37 starred, 9 non-star samples, 6 hotels, 7 decision questions, 6 suggestions, 8 review flags), HTTP smoke check on the static site, and `git diff --check` passed. No build dependencies are required.

## Flagged for review / irregularities

- Meal totals for two adults are blank: current official menus and consistent treatment of tax, service, drinks, and supplements were not audited for every venue.
- Weekly schedules and holiday/special closure exceptions are populated only on profiles checked in this pass. Social-media links have not been confirmed for any venue; fields remain blank rather than guessed.
- Hotel list is a candidate shortlist, not a restaurant-density ranking. Distance/time threshold, stay dates, group size, comparable rate basis, and geocoded address inventory are missing.
- City counts and map searches are star-only, municipality-level approximations; not walking-radius counts, venue pins, or counts of all Michelin Guide selections.
- The full 2026 Guide-selected/Bib Gourmand inventory is not represented; nine verified non-star examples are included to demonstrate distinct labels.
- GitHub Pages currently reports `build_type: legacy`, sourced from `main`. Attempting to switch to GitHub Actions with `gh api` returned HTTP 403 (`Resource not accessible by integration`). The workflow is ready, but publishing this branch to the live Pages URL requires an owner/admin to enable Actions as the Pages source; no permission workaround or credential request was attempted.

## Deployment status (checked 2026-11-24)

- Pages API: `build_type: legacy`, source `main`, URL `https://kanlerxz87-cyber.github.io/Baymich3/`. Not yet switched to the Actions workflow (HTTP 403 on change attempt).
- Actions history shows a failed run "Build source-first Bay Area Michelin planning dashboard" (`Deploy static site to GitHub Pages`) on branch `arena/46b28920-baymich3`, a different session's branch. Not investigated or modified here; flagged for the integration session.
- Live site is therefore NOT yet showing this branch's dashboard.
