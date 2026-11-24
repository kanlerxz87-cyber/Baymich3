# COORDINATION — shared task board

Repo: `kanlerxz87-cyber/Baymich3` · Live site (GitHub Pages, from this branch's `docs/`): see the Pages link in the Log.

## Rules used in this file

- Status values: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).
- Every table row must link an official source. Anything that can't be confirmed from an official source is left blank and flagged `unverified`. Values are never inferred.
- **Branch note:** this session is bound to branch `arena/d7b7bed1-baymich3` (fixed by the session harness). The `session-<id>/<task>` branch naming in the original brief is not used, because the harness requires work to stay on this one branch. Scopes are still kept non-overlapping by file, as listed below.
- Before pushing: `git pull --rebase`, then `git push origin arena/d7b7bed1-baymich3`.

## Task board

| ID | Task | Status | Owner (session) | Files in scope | Notes |
|---|---|---|---|---|---|
| T1 | Repo review (README, git state, repo hygiene) | done | arena/d7b7bed1 | `README.md`, `COORDINATION.md` | See *Repo review* below |
| T2 | Michelin Bay Area starred list (3★/2★/1★) | done for star status · detail fields partial | arena/d7b7bed1 | `docs/data/data.js` (starred) | 41 starred restaurants; 14 fully/partly verified (hours/address), 27 one-star pending detail |
| T3 | Michelin Bib Gourmand & Recommended, Bay Area | **unclaimed** | — | `docs/data/data.js` (bib) | Not gathered in this session |
| T4 | Hotels ranked by nearby Michelin restaurants | **unclaimed** | — | `docs/data/data.js` (hotels) | Not gathered in this session |
| T5 | Couple price (2 adults) from official restaurant menus | **unclaimed** | — | `docs/data/data.js` (price fields) | Michelin shows $ levels only; no dollar figure is inferred |
| T6 | YouTube / TikTok / Instagram links per listing | **unclaimed** | — | `docs/data/data.js` (social fields) | Not gathered in this session |
| T7 | Detail fields for 27 one-star restaurants (address, cuisine, price, hours, website) | **unclaimed** | — | `docs/data/data.js` (starred 1★ rows) | Michelin page link already verified per row |
| T8 | Website: landing + category subpages + GitHub Pages | done (first version) | arena/d7b7bed1 | `docs/**` | Built as static HTML/JS, no build step |
| T9 | Executive summary, questions/answers, suggestions | done (first version) | arena/d7b7bed1 | `docs/questions.html`, `docs/suggestions.html`, `docs/index.html` | Suggestions await user choice before any change |
| T10 | Integration: merge, re-verify combined data, link check, publish | pending | arena/d7b7bed1 (no other sessions active) | all | Only one session exists, so integration is done here |

## Log

- **2026-11-24 · arena/d7b7bed1** — Claimed T1–T10 (single active session). Read official Michelin California 2026 article (`guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california`, 24 Jun 2026) and 14 official Michelin restaurant pages. Built the first version of the site and the data file.

## Repo review (T1)

Checked: `git status`, `git log`, branch list, remote, `README.md`.

| Item | Result | Source / check |
|---|---|---|
| Repo state | Clean. One commit (`fc288db Initial commit`) on `main`. Working branch `arena/d7b7bed1-baymich3` | `git log`, `git branch -a` |
| README.md | Contains only `# Baymich3` (10 bytes). No description, license, or setup steps. **Irregularity: flag** | `README.md` |
| LICENSE | Missing. **Flag for review** (licensing decision needed before reuse) | file listing |
| CI / build config | None present. Site is plain static HTML so no build is required | file listing |
| Coordination file | `COORDINATION.md` was missing and has been created by this session | brief |
| Git identity | `kanlerxz87-cyber` / noreply address configured locally | `git config` |
| GitHub auth | `gh auth status` reports logged in as `kanlerxz87-cyber`. Token not shown or stored in repo | `gh auth status` |

## Flagged for review

Items below are published on the site's *Flagged for review* page.

1. **Partial Michelin coverage.** 27 one-star restaurants have only name, city, star and Michelin link verified. Other fields are blank and marked `Pending`.
2. **No Michelin dollar prices.** Michelin shows $/$$/$$$/$$$$ levels only. Couple totals are not filled in.
3. **Hours gaps.** Some restaurants show partial hours because the official page output was truncated. Those rows are marked `Partial`.
4. **Lost stars.** Le Comptoir at Bar Crenn, O' by Claude Le Tohic and Shota are reported removed in 2026 (Eater). Their official Michelin listing status is not verified.
5. **Region definition.** "Bay Area" is defined in `docs/data/data.js` (`region_definition`). Michelin's own regional grouping may differ.
6. **Repo irregularities.** README has no content and the repo has no LICENSE. Both flagged above.
