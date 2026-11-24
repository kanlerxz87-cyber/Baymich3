# Bay Michelin field guide

A responsive, source-first Michelin dining and hotel planning site for the San Francisco Bay Area. Static site files are in `site/`; no build framework or runtime dependencies are required.

## Preview locally

From the repository root, run `python3 -m http.server 8000 --directory site`, then open `http://localhost:8000`.

## Publish with GitHub Pages

The workflow in `.github/workflows/pages.yml` deploys the `site/` folder on pushes to this task branch or `main`. In repository Settings → Pages, select **GitHub Actions** as the build and deployment source. Repository permissions and Pages settings are controlled outside this checkout; deployment status must be checked in Actions after push.

## Data integrity

The 2026 restaurant distinction list and hotel data cite official MICHELIN pages; restaurant costs and schedules cite venue-owned pages where verified. Unknown values remain blank or explicitly unverified. The current directory count is a dated snapshot and must be refreshed before treating it as current. Read the Review & methods page for unresolved issues and ranking methodology.
