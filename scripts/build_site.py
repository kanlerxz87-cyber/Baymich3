#!/usr/bin/env python3
"""Build data/restaurants.json and the static GitHub Pages site in docs/.

Inputs (all verified sources live in data/source/):
  - michelin_sf_listing_page1.tsv   : rows copied from the official Michelin SF listing (page 1 of 4)
  - michelin_detail_verified.json   : fields copied from official Michelin detail pages

Rule: a value that is not in an official source is left EMPTY and shown as UNVERIFIED.
Stdlib only, no network access.
"""
import csv
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "source"
DATA = ROOT / "data"
DOCS = ROOT / "docs"
LISTING_URL = "https://guide.michelin.com/us/en/california/san-francisco/restaurants"
DETAIL_BASE = "https://guide.michelin.com/us/en/california/san-francisco/restaurant/"
VERIFIED_ON = "2026-11-24"

STAR_MAP = {"3 Stars": 3, "2 Stars": 2, "1 Star": 1}


def load_rows():
    detail = json.loads((SRC / "michelin_detail_verified.json").read_text())
    detail.pop("_note", None)
    rows = []
    with open(SRC / "michelin_sf_listing_page1.tsv", newline="", encoding="utf-8") as fh:
        for i, r in enumerate(csv.DictReader(fh, delimiter="\t"), start=1):
            dist = r["distinction"]
            stars = STAR_MAP.get(dist, 0)
            d = detail.get(r["slug"])
            rows.append({
                "rank": i,
                "name": r["name"],
                "michelin_distinction": dist,
                "has_michelin_star": stars > 0,
                "michelin_stars": stars,
                "cuisine": r["cuisine"],
                "michelin_price_band": r["michelin_price"],
                "couple_total_2_adults": "",  # not published by Michelin; unverified
                "address": d["address"] if d else "",
                "hours": d["hours"] if d else "",
                "phone": d["phone"] if d else "",
                "website": d["website"] if d else "",
                "social_links": "",  # not yet searched; unverified
                "michelin_url": DETAIL_BASE + r["slug"],
                "detail_verified": bool(d),
                "verification": (
                    "Listing + detail page verified" if d and d.get("hours")
                    else "Detail page verified (hours not captured)" if d
                    else "Listing verified · details unverified"
                ),
                "sources": [LISTING_URL, DETAIL_BASE + r["slug"]] if d else [LISTING_URL],
            })
    return rows


def esc(v):
    return html.escape(str(v)) if v else ""


def unv(v, label="unverified"):
    if v:
        return esc(v)
    return f'<span class="flag">⚠ {label}</span>'


def status_badge(r):
    d = r["michelin_distinction"]
    if r["michelin_stars"]:
        return f'<span class="badge star">{"★" * r["michelin_stars"]} {esc(d)}</span>'
    if d.startswith("Bib"):
        return f'<span class="badge bib">Bib Gourmand (no star)</span>'
    return '<span class="badge listed">Listed only (no star)</span>'


def table_rows(rows):
    out = []
    for r in rows:
        src_links = " · ".join(
            f'<a href="{esc(u)}" target="_blank" rel="noopener">source {i+1}</a>'
            for i, u in enumerate(r["sources"]))
        website = (f'<a href="{esc(r["website"])}" target="_blank" rel="noopener">site</a>'
                   if r["website"] else unv(""))
        out.append(f"""
        <tr>
          <td>{r['rank']}</td>
          <td class="name"><a href="{esc(r['michelin_url'])}" target="_blank" rel="noopener">{esc(r['name'])}</a><div class="sub">{esc(r['cuisine'])}</div></td>
          <td>{status_badge(r)}</td>
          <td>{esc(r['michelin_price_band'])}</td>
          <td>{unv(r['couple_total_2_adults'], 'no verified price')}</td>
          <td>{unv(r['address'], 'address not captured')}</td>
          <td class="hours">{unv(r['hours'], 'hours not captured')}</td>
          <td>{unv(r['phone'], 'n/a')}</td>
          <td>{website}</td>
          <td>{unv(r['social_links'], 'not searched')}</td>
          <td class="ver">{esc(r['verification'])}<div class="sub">{src_links}</div></td>
        </tr>""")
    return "\n".join(out)


CSS = """
:root{--ink:#1d2430;--mut:#5b6474;--bg:#f6f7f9;--card:#fff;--line:#e3e6ec;--acc:#8a1c2b;--ok:#1d7a4a;--warn:#b35c00}
*{box-sizing:border-box}body{margin:0;font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
header{background:var(--acc);color:#fff;padding:18px 16px}header h1{margin:0;font-size:1.4rem}header p{margin:4px 0 0;opacity:.9;font-size:.9rem}
nav{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:2}nav ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 14px;padding:10px 16px}
nav a{color:var(--acc);text-decoration:none;font-weight:600;font-size:.92rem}
main{max-width:1200px;margin:0 auto;padding:16px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:12px 0 20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
.card b{display:block;font-size:1.6rem;color:var(--acc)}.card a{color:var(--ink);font-weight:600;text-decoration:none}
h2{font-size:1.2rem;margin:24px 0 8px}h3{font-size:1rem;margin:16px 0 6px}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:10px 0}
.tablewrap{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;min-width:1100px;font-size:.88rem}
th,td{padding:8px 9px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:#f0f2f6;position:sticky;top:0;font-size:.82rem;text-transform:uppercase;letter-spacing:.03em;color:var(--mut)}
td.name a{font-weight:700;color:var(--ink)}.sub{color:var(--mut);font-size:.8rem;margin-top:2px}
.hours{min-width:200px}.ver{min-width:200px;font-size:.8rem}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:.78rem;font-weight:600;white-space:nowrap}
.badge.star{background:#fbe9ec;color:var(--acc)}.badge.bib{background:#e7f4ec;color:var(--ok)}.badge.listed{background:#eef0f4;color:var(--mut)}
.flag{color:var(--warn);font-size:.8rem;font-style:italic;white-space:nowrap}
.search{width:100%;max-width:360px;padding:9px 12px;border:1px solid var(--line);border-radius:8px;font-size:1rem;margin:6px 0 10px}
.pill{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:999px;padding:3px 10px;margin:2px;font-size:.85rem}
ul.plain{padding-left:20px}ul.plain li{margin:4px 0}
footer{color:var(--mut);font-size:.82rem;text-align:center;padding:24px 16px}
.qa{display:grid;gap:8px}.qa .q{font-weight:700}.qa .ans{color:var(--mut)}
@media (max-width:640px){main{padding:10px}header h1{font-size:1.2rem}}
"""

NAV = """<nav><ul>
<li><a href="index.html">Dashboard</a></li>
<li><a href="restaurants.html">Michelin restaurants</a></li>
<li><a href="hotels.html">Hotels</a></li>
<li><a href="flagged.html">Flagged &amp; decisions</a></li>
</ul></nav>"""


def page(title, body, active=""):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · SF Bay Area Michelin</title>
<link rel="stylesheet" href="style.css"></head><body>
<header><h1>SF Bay Area Michelin · Dashboard</h1><p>Verified against official Michelin pages · last checked {VERIFIED_ON}</p></header>
{NAV}<main>{body}</main>
<footer>Unverified values are left blank and marked ⚠. No value is inferred. Repo: github.com/kanlerxz87-cyber/Baymich3</footer>
</body></html>"""


def build_index(rows):
    c = {}
    for r in rows:
        k = r["michelin_distinction"]
        c[k] = c.get(k, 0) + 1
    verified = sum(1 for r in rows if r["detail_verified"])
    body = f"""
<h2>Executive summary</h2>
<div class="box">
<ul class="plain">
<li>Official Michelin source used: <a href="{LISTING_URL}" target="_blank" rel="noopener">San Francisco and surroundings listing</a> — it reports <b>145</b> restaurants across 4 pages. <b>This build covers page 1 only (48 entries).</b></li>
<li>Page 1 breakdown: <b>4</b> three-star · <b>6</b> two-star · <b>15</b> one-star · <b>8</b> Bib Gourmand · <b>15</b> listed with no star or Bib.</li>
<li>Detail pages checked on Michelin for <b>{verified}</b> of 48 entries (address, hours, phone, website). Other rows show listing data only.</li>
<li><b>Couple prices (2 adults):</b> not published on Michelin pages. Only the Michelin price band ($–$$$$) is shown. No total price is filled in.</li>
<li><b>Social links (YouTube / TikTok / Instagram):</b> not collected yet.</li>
<li><b>Hotels ranking:</b> not started. See the Hotels page.</li>
<li>Several press reports conflict with each other or with the official listing. See the Flagged page.</li>
</ul></div>

<h2>Snapshot</h2>
<div class="cards">
<div class="card"><b>{c.get('3 Stars',0)}</b><a href="restaurants.html">Three-star</a></div>
<div class="card"><b>{c.get('2 Stars',0)}</b><a href="restaurants.html">Two-star</a></div>
<div class="card"><b>{c.get('1 Star',0)}</b><a href="restaurants.html">One-star</a></div>
<div class="card"><b>{c.get('Bib Gourmand',0)}</b><a href="restaurants.html">Bib Gourmand</a></div>
<div class="card"><b>{c.get('Selected (no star)',0)}</b><a href="restaurants.html">Listed, no star</a></div>
<div class="card"><b>0</b><a href="hotels.html">Hotels ranked</a></div>
</div>

<h2>Pages</h2>
<div class="cards">
<div class="card"><a href="restaurants.html">Michelin restaurants →</a><div class="sub">Table: status, price band, hours, links, sources</div></div>
<div class="card"><a href="hotels.html">Hotels →</a><div class="sub">Status: not started</div></div>
<div class="card"><a href="flagged.html">Flagged, questions &amp; suggestions →</a><div class="sub">Irregularities, open questions, options to approve</div></div>
</div>
"""
    return page("Dashboard", body)


def build_restaurants(rows):
    body = f"""
<h2>Michelin restaurants · San Francisco and surroundings · page 1 of 4</h2>
<p>Star status and price bands come from the official Michelin listing. Hours, address, phone and website come from the official Michelin detail page only where the detail page was checked. Couple totals are blank: no official source was found for them.</p>
<input class="search" id="q" type="search" placeholder="Search name or cuisine…" aria-label="Search">
<div class="tablewrap"><table id="t">
<thead><tr>
<th>#</th><th>Restaurant</th><th>Michelin status</th><th>Price band</th><th>Total for 2 adults</th>
<th>Address</th><th>Hours (days &amp; exceptions)</th><th>Phone</th><th>Website</th><th>Social (YT/TT/IG)</th><th>Verification &amp; sources</th>
</tr></thead>
<tbody>{table_rows(rows)}</tbody>
</table></div>
<script>
document.getElementById('q').addEventListener('input',function(e){{
 var v=e.target.value.toLowerCase();
 document.querySelectorAll('#t tbody tr').forEach(function(r){{
  r.style.display = r.textContent.toLowerCase().indexOf(v)>-1 ? '' : 'none';
 }});
}});
</script>
"""
    return page("Michelin restaurants", body)


def build_hotels():
    body = """
<h2>Hotels ranked by Michelin density</h2>
<div class="box"><b>Status: not started.</b> No hotel data has been collected or verified in this session, so no ranking is shown.
Planned method (needs your decision, see <a href="flagged.html">Flagged &amp; decisions</a>):
use official Michelin hotel pages, count Michelin restaurants within a defined radius, and rank.</div>
"""
    return page("Hotels", body)


def build_flagged():
    irregularities = [
        ("Repo", "README.md is only the title line (10 bytes). No description, license, .gitignore, or build config existed at base commit fc288db.", "https://github.com/kanlerxz87-cyber/Baymich3/blob/main/README.md"),
        ("Repo", "COORDINATION.md was missing. It was created by this session as the task board.", "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/26f06e9a-baymich3/COORDINATION.md"),
        ("Process", "The coordination rules name per-task branches `session-<id>/<task>`. This session is restricted to one branch, so claims are logged on the current branch instead.", "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/26f06e9a-baymich3/COORDINATION.md"),
        ("Source", "The URL for the official listing “San Francisco Bay Area” returned an error. The official “San Francisco and surroundings” listing (145 entries, 4 pages) was used instead. Only page 1 was captured.", LISTING_URL),
        ("Source", "Press reports say Le Comptoir at Bar Crenn, O' by Claude Le Tohic, and Shota lost their stars in 2026. None of them appears on page 1 of the official listing. Not verified here.", "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area"),
        ("Source", "Press reports describe Green Stars returning after Michelin said it would retire the designation. Not verified against Michelin; not used in this table.", "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area"),
        ("Source", "Press lists disagree on which Bay Area restaurants are Bib Gourmand (for example Joodooboo and Kitchen Istanbul). Only the official listing icons were used for this table.", "https://www.sacbee.com/news/california/article316268654.html"),
        ("Data", "Michelin shows price bands ($–$$$$), not couple totals. The couple-total column is left blank for every row.", LISTING_URL),
        ("Data", "Atelier Crenn detail page: address, phone and website were captured, but the hours section was cut off in the copy, so hours are blank.", "https://guide.michelin.com/us/en/california/san-francisco/restaurant/atelier-crenn"),
        ("Data", "Michelin hours and restaurant websites may differ. Confirm hours on the restaurant site or booking platform before visiting.", LISTING_URL),
    ]
    questions = [
        ("Geographic scope", "Do you want San Francisco only, or the whole Bay Area (Oakland, Berkeley, Peninsula, Napa, Sonoma)?", "Michelin's SF page covers “San Francisco and surroundings” (145 entries). Only page 1 is captured.", "Your answer. Options: SF only · Bay Area core (SF, Oakland, Berkeley, Peninsula) · Full region."),
        ("Couple price source", "Which price should the 2-adult total use? Michelin only gives price bands.", "Michelin price bands are verified. No couple total is published by Michelin.", "Your answer. Options: restaurant's official menu page · booking platform (OpenTable/Resy/Tock) · price band only."),
        ("Hotel ranking radius", "How should ‘around’ be measured for hotels: walking distance, driving time, or a fixed radius?", "Unknown.", "Your answer. Options: 1 mile · 3 miles · 15-min drive · custom."),
        ("Visit dates & party", "Which dates are you planning? Open days and hours change by date (holidays, closures).", "Only that the party is 2 adults.", "Your answer (dates or “flexible”)."),
        ("Social links policy", "Accept only restaurant-owned accounts, or also creator videos?", "Nothing collected yet. No link has been verified.", "Your answer. Options: owned accounts only · owned + creator videos · skip social."),
        ("Map provider", "Which map should the site use?", "Michelin provides coordinates in its map view, not in the text we captured. Coordinates are not verified.", "Your answer. Options: OpenStreetMap (no key) · Google Maps embed (needs key) · link out only."),
    ]
    suggestions = [
        ("S1", "Capture pages 2–4 of the official listing (97 more entries) using the same line-by-line method.", "Completes the list of 145.", "Pending approval"),
        ("S2", "For each restaurant, read its official website menu or booking page to get a dated 2-adult price range.", "Gives real verified totals. Adds a dated source column.", "Pending approval"),
        ("S3", "Check each restaurant's own website for Instagram, TikTok, or YouTube links, and record only links found there.", "Fills the social column with official links only.", "Pending approval"),
        ("S4", "Hotels: take Michelin hotel pages, get their restaurant coordinates, and rank by count of Michelin restaurants within the radius chosen in Q3.", "Delivers the hotel ranking.", "Pending approval"),
        ("S5", "Add a GitHub Actions link checker and a per-row ‘last verified’ date so the site fails when a source link breaks.", "Keeps the ‘no broken links’ rule enforceable.", "Pending approval"),
        ("S6", "Add filters (star, Bib, price band, neighborhood) and sorting to the restaurant table.", "Easier decisions on mobile.", "Pending approval"),
        ("S7", "Add a press-vs-official reconciliation table so each press claim is marked confirmed, conflicting, or not found.", "Makes the conflicts above reviewable.", "Pending approval"),
    ]

    irr_html = "\n".join(
        f'<li><b>{esc(k)}:</b> {esc(t)} <a href="{esc(u)}" target="_blank" rel="noopener">source</a></li>'
        for k, t, u in irregularities)
    q_html = "\n".join(
        f'<div class="box qa"><div class="q">{i+1}. {esc(q)}</div><div>{esc(qq)}</div>'
        f'<div class="ans"><b>What we know:</b> {esc(k)}</div><div class="ans"><b>Answer needed:</b> {esc(a)}</div></div>'
        for i, (q, qq, k, a) in enumerate(questions))
    s_html = "\n".join(
        f'<tr><td>{esc(i)}</td><td>{esc(t)}</td><td>{esc(b)}</td><td>{esc(s)}</td></tr>'
        for i, t, b, s in suggestions)

    body = f"""
<h2>Flagged for review</h2>
<div class="box"><ul class="plain">{irr_html}</ul></div>

<h2>Questions to answer before deciding</h2>
<p>Each question lists what we already know and what is missing. Nothing below is decided.</p>
{q_html}

<h2>Suggestions · choose before anything changes</h2>
<p>None of these have been implemented. Reply with the IDs you approve (for example “S1, S2”).</p>
<div class="tablewrap"><table style="min-width:700px">
<thead><tr><th>ID</th><th>Suggestion</th><th>Benefit</th><th>Status</th></tr></thead>
<tbody>{s_html}</tbody></table></div>

<h2>Sources used</h2>
<div class="box"><ul class="plain">
<li><a href="{LISTING_URL}" target="_blank" rel="noopener">Official Michelin Guide — San Francisco listing (guide.michelin.com)</a></li>
<li>Official Michelin detail pages used: Quince, Californios, Benu, Atelier Crenn (address/phone/website only), Acquerello, Kiln, Izakaya Rintaro.</li>
<li>Press (for conflicts only, not for table values): <a href="https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area" target="_blank" rel="noopener">Eater SF</a>, <a href="https://www.sacbee.com/news/california/article316268654.html" target="_blank" rel="noopener">SacBee</a>.</li>
</ul></div>
"""
    return page("Flagged & decisions", body)


def main():
    rows = load_rows()
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (DATA / "restaurants.json").write_text(json.dumps({
        "generated_for": "San Francisco and surroundings, Michelin listing page 1 of 4",
        "verified_on": VERIFIED_ON,
        "listing_source": LISTING_URL,
        "count": len(rows),
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DOCS / "style.css").write_text(CSS, encoding="utf-8")
    (DOCS / "index.html").write_text(build_index(rows), encoding="utf-8")
    (DOCS / "restaurants.html").write_text(build_restaurants(rows), encoding="utf-8")
    (DOCS / "hotels.html").write_text(build_hotels(), encoding="utf-8")
    (DOCS / "flagged.html").write_text(build_flagged(), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print(f"built {len(rows)} rows")


if __name__ == "__main__":
    main()
