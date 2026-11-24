# Method & Verification

How each number on this site was obtained, and what was refused. The rule is simple: **if an official page did not say it, the cell stays empty.**

## Sources, in order of authority

1. **guide.michelin.com** — the star or Bib itself, the address as Michelin prints it, and the day-by-day open/closed block on each restaurant page.
2. **The venue's own website** — menu price, service charge, opening days and hours, closures, and any social account the site itself links to.
3. **The venue's own booking page** (Tock, OpenTable, SevenRooms, Resy) — only where the restaurant controls the listing, and always labelled as such. Never presented as a homepage-verified price.
4. **Not used:** aggregators, review sites, press articles quoting prices, or memory. Third-party figures seen during the audit were recorded as indicative at most, and are not shown as totals.

## The price formula

Total for two adults = (published per-person menu price × 2) + the service charge and surcharges the restaurant publishes.

- San Francisco operators add 20–26% in service charge and mandate. **Benu:** $425 × 2 + 22% = **$1,037**. **Angler lunch:** $60 × 2 + 26% = **$151.20**.
- **7 Adams** is the clearest case for why both charges matter: $127 × 2 = $254, plus a 6% surcharge and 20% service = **$320.04**.
- Where a venue publishes "starting at", the row says so and the total is a floor, not a quote.
- Sales tax and beverages are always excluded unless the row says otherwise.

## Status labels

| Label | Meaning |
|---|---|
| **Verified** | A value on the row was read off an official page, and that page is linked in the row's source cell. |
| **Partial** | Some values are official and others are not. The status text says which is which. |
| **Unverified** | Nothing on the row could be confirmed from an official page. Values are blank. |
| **Bib Gourmand** | In the Guide for value. Not a star. |

## Build integrity

The site is generated from the CSVs by `tools/build_site.py`. The generator asserts that every restaurant row carries a `guide.michelin.com` source link, refuses to run if the column schema has drifted, and computes every count on every page from the data — so a stale headline is not possible. The text pages (executive summary, questions, suggestions, flagged, this page) are authored in `docs/*.md` and rendered by the same script, which is why their numbers match the tables.

Data repairs are scripted and logged rather than hand-patched, so each change records what it replaced: `tools/fix_data.py`, `tools/fix_bib.py`, `tools/fix_hotels.py`.

To regenerate: `python3 tools/build_site.py`. To preview: `python3 -m http.server 8000` from the repository root.

## What is still missing

Roughly a third of the starred rows have a publishable price for two; the rest live behind a booking platform or a PDF menu. No starred venue publishes a YouTube or TikTok channel, so those cells are blank. The 86 Selected restaurants are counted but not enumerated, because Michelin does not publish that set as one page. Each gap has a discovery route on the [Questions](questions.html) page rather than a guess in a table.
