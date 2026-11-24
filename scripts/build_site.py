#!/usr/bin/env python3
"""Build the static GitHub Pages site in docs/ from data/*.json.

No third-party dependencies. Run:  python3 scripts/build_site.py
Every data row is rendered with its source link; blank fields are shown as
"Unverified" so nothing is inferred.
"""
import html
import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")

with open(os.path.join(DATA, "restaurants.json"), encoding="utf-8") as f:
    R = json.load(f)
with open(os.path.join(DATA, "analysis.json"), encoding="utf-8") as f:
    A = json.load(f)

ASOF = R["as_of"]
starred = R["restaurants"]
bibs = R["bib_gourmand"]
core_starred = [r for r in starred if r["region"] == "Core Bay Area"]
wine_starred = [r for r in starred if r["region"] != "Core Bay Area"]
sf_starred = [r for r in core_starred if r["city"] == "San Francisco"]
full_verified = [r for r in starred if r["verification"].startswith("Full")]

NAV = [
    ("index.html", "Home"),
    ("stars.html", "Starred"),
    ("bib.html", "Bib Gourmand"),
    ("clusters.html", "Clusters"),
    ("hotels.html", "Hotels"),
    ("questions.html", "Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged"),
    ("sources.html", "Sources"),
]

CSS = """
:root{--ink:#1d1d1f;--mut:#5b5f66;--line:#e3e5e8;--bg:#f7f7f9;--acc:#b3121c;--ok:#1f7a3d;--warn:#8a5a00}
*{box-sizing:border-box}body{margin:0;font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.wrap{max-width:1200px;margin:0 auto;padding:0 14px}
.brand{padding:12px 0 6px;font-weight:700;font-size:17px}.brand span{color:var(--acc)}
nav{display:flex;flex-wrap:wrap;gap:6px;padding-bottom:10px}
nav a{font-size:13px;color:var(--ink);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:4px 11px;background:#fff}
nav a.on,nav a:hover{background:var(--ink);color:#fff}
h1{font-size:22px;margin:18px 0 4px}h2{font-size:17px;margin:22px 0 8px}
p.lead{color:var(--mut);margin:0 0 12px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px}
.card b{display:block;font-size:24px}.card small{color:var(--mut)}
.tblwrap{overflow-x:auto;background:#fff;border:1px solid var(--line);border-radius:10px;margin:8px 0 14px;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;min-width:720px;font-size:13.5px}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:#fafafa;font-size:12px;text-transform:uppercase;letter-spacing:.03em;color:var(--mut);position:sticky;top:0}
td.name{font-weight:600;min-width:150px}
.tag{display:inline-block;font-size:11.5px;border-radius:6px;padding:1px 7px;margin:1px 2px 1px 0;background:#eef0f3}
.t3{background:#111;color:#fff}.t2{background:#444;color:#fff}.t1{background:#8a8f98;color:#fff}.bib{background:#e7f3ea;color:var(--ok)}
.new{background:#fff3d6;color:var(--warn)}.unv{color:var(--warn);font-style:italic}
.ok{color:var(--ok)}
a{color:#0b57d0}
ul.plain{padding-left:18px}ul.plain li{margin:4px 0}
.note{background:#fff8e6;border:1px solid #f0dda0;border-radius:10px;padding:10px 12px;margin:10px 0;font-size:13.5px}
footer{color:var(--mut);font-size:12.5px;padding:24px 0 40px}
.qa{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:8px 0}
.qa b{display:block}
@media (max-width:640px){body{font-size:14px}h1{font-size:19px}}
"""


def e(s):
    return html.escape(str(s or ""), quote=True)


def page(title, active, body):
    nav = "".join(
        f'<a href="{href}" class="{"on" if href == active else ""}">{label}</a>'
        for href, label in NAV
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · SF Bay Area Michelin Dashboard</title>
<style>{CSS}</style></head><body>
<header><div class="wrap"><div class="brand">SF Bay Area <span>Michelin</span> Dashboard</div><nav>{nav}</nav></div></header>
<main class="wrap">{body}</main>
<footer class="wrap">Data as of {ASOF}. Star and Bib status: MICHELIN Guide California 2026 (official). Blank or “Unverified” means the value was not confirmed from an official source. Repo: <a href="https://github.com/kanlerxz87-cyber/Baymich3">Baymich3</a>.</footer>
</body></html>"""


def tier_tag(tier):
    cls = {"Three Stars": "t3", "Two Stars": "t2", "One Star": "t1"}.get(tier, "bib")
    short = {"Three Stars": "3★", "Two Stars": "2★", "One Star": "1★"}.get(tier, tier)
    return f'<span class="tag {cls}">{short}</span>'


def unv(val, label="Unverified"):
    return e(val) if val else f'<span class="unv">{label}</span>'


def starred_rows(rows):
    out = []
    for r in rows:
        new = ' <span class="tag new">NEW 2026</span>' if r["name"] in ("Californios", "Naides", "Wolfsbane", "Troubadour", "Enclos") else ""
        status = "Starred (" + {"Three Stars": "3", "Two Stars": "2", "One Star": "1"}[r["tier"]] + " MICHELIN Star" + ("s" if r["tier"] != "One Star" else "") + ")"
        website = f'<a href="{e(r["website"])}">Official site</a>' if r["website"] else '<span class="unv">Unverified</span>'
        out.append(
            "<tr>"
            f'<td class="name">{e(r["name"])}{new}</td>'
            f"<td>{tier_tag(r['tier'])}<br><small>{e(status)}</small></td>"
            f"<td>{e(r['region'])}<br><small>{e(r['city'])}</small></td>"
            f"<td>{unv(r['address'])}</td>"
            f"<td>{unv(r['cuisine'])}</td>"
            f"<td>{unv(r['michelin_price'])}</td>"
            f"<td>{unv(r['hours'])}<br><small>{e(r['hours_status'])}</small></td>"
            '<td class="unv">Unverified<br><small>Needs official menu price</small></td>'
            '<td class="unv">Unverified<br><small>Not yet researched</small></td>'
            f"<td>{website}</td>"
            f'<td><a href="{e(r["michelin_url"])}">Michelin page</a><br><small>{e(r["verification"])}</small></td>'
            "</tr>"
        )
    return "\n".join(out)


def stars_page():
    head = ("<tr><th>Restaurant</th><th>Michelin status 2026</th><th>Region / city</th>"
            "<th>Address</th><th>Cuisine</th><th>Michelin price tier</th><th>Hours &amp; days</th>"
            "<th>Price for 2 adults</th><th>Social (IG/TikTok/YouTube)</th><th>Official link</th>"
            "<th>Source &amp; verification</th></tr>")
    body = f"""<h1>Michelin starred restaurants</h1>
<p class="lead">Core SF Bay Area first (SF, Oakland, Peninsula). Wine Country starred restaurants are listed last. "Unverified" = not confirmed from an official source yet.</p>
<div class="note"><b>Price for 2 adults</b> is blank for every row: no official menu prices have been collected yet. Michelin shows only a $ to $$$$ price tier, which is not a dollar amount. <b>Social links</b> have not been researched yet.</div>
<h2>Core Bay Area ({len(core_starred)})</h2>
<div class="tblwrap"><table>{head}{starred_rows(core_starred)}</table></div>
<h2>Wine Country, outside core ({len(wine_starred)})</h2>
<div class="tblwrap"><table>{head}{starred_rows(wine_starred)}</table></div>"""
    return page("Starred restaurants", "stars.html", body)


def bib_page():
    rows = []
    for b in bibs:
        new = ' <span class="tag new">NEW 2026</span>' if b["new_2026"] else ""
        rows.append(
            "<tr>"
            f'<td class="name">{e(b["name"])}{new}</td>'
            f'<td>{e(b["city"])}</td>'
            f'<td>{e(b["address"])}</td>'
            '<td><span class="tag bib">Bib Gourmand 2026</span></td>'
            '<td class="unv">Unverified</td>'
            '<td class="unv">Unverified</td>'
            '<td class="unv">Unverified<br><small>Needs official menu price</small></td>'
            '<td class="unv">Unverified</td>'
            f'<td><a href="{R["michelin_sources"]["official_press_release"]}">Michelin 2026 Bib list</a></td>'
            "</tr>"
        )
    head = ("<tr><th>Restaurant</th><th>City</th><th>Address</th><th>Michelin status</th>"
            "<th>Hours &amp; days</th><th>Official website</th><th>Price for 2 adults</th>"
            "<th>Social</th><th>Source</th></tr>")
    body = f"""<h1>Bib Gourmand restaurants (core Bay Area)</h1>
<p class="lead">{len(bibs)} restaurants on Michelin's official 2026 Bib Gourmand list for the core Bay Area. Bib Gourmand = good food at a moderate price (Michelin definition). Addresses are from Michelin's list; the other columns are not yet verified.</p>
<div class="tblwrap"><table>{head}{''.join(rows)}</table></div>"""
    return page("Bib Gourmand", "bib.html", body)


def cluster_page():
    # Only rows with a full address count (ZIP parsed from the address text).
    zips = defaultdict(lambda: {"starred": 0, "bib": 0, "names": []})
    unparsed = []
    rows_all = [("star", r["name"], r["address"], r["tier"]) for r in core_starred] + [
        ("bib", b["name"], b["address"], "Bib") for b in bibs]
    for kind, name, addr, tier in rows_all:
        m = re.search(r"CA (\d{5})", addr or "")
        if not m:
            unparsed.append(name)
            continue
        z = m.group(1)
        if kind == "star":
            zips[z]["starred"] += 1
        else:
            zips[z]["bib"] += 1
        zips[z]["names"].append(name)
    tbl = []
    for z in sorted(zips, key=lambda k: (-(zips[k]["starred"] * 2 + zips[k]["bib"]), k)):
        d = zips[z]
        tbl.append(
            f"<tr><td class='name'>{z}</td><td>{d['starred']}</td><td>{d['bib']}</td>"
            f"<td>{e(', '.join(sorted(d['names'])))}</td></tr>")
    city = Counter()
    for r in core_starred:
        city[r["city"]] += 1
    city_tbl = "".join(
        f"<tr><td class='name'>{e(c)}</td><td>{n}</td><td>{sum(1 for b in bibs if b['city']==c)}</td></tr>"
        for c, n in sorted(city.items(), key=lambda x: (-x[1], x[0])))
    bib_city = Counter(b["city"] for b in bibs)
    for c, n in bib_city.items():
        if c not in city:
            city_tbl += f"<tr><td class='name'>{e(c)}</td><td>0</td><td>{n}</td></tr>"
    body = f"""<h1>Restaurant clusters</h1>
<p class="lead">Counts of Michelin-listed restaurants by city and by ZIP code. This is the input for the hotel ranking, which is not finished yet. ZIP codes come from the official addresses; ZIP-only grouping does not claim neighborhood boundaries.</p>
<h2>By city</h2>
<div class="tblwrap"><table style="min-width:420px"><tr><th>City</th><th>Starred (core)</th><th>Bib (core)</th></tr>{city_tbl}</table></div>
<h2>By ZIP code (rows with a full address)</h2>
<div class="tblwrap"><table><tr><th>ZIP</th><th>Starred</th><th>Bib</th><th>Restaurants</th></tr>{''.join(tbl)}</table></div>
<div class="note">Not counted here because no official address was captured yet: {e(', '.join(sorted(set(unparsed))))}.</div>"""
    return page("Clusters", "clusters.html", body)


def hotels_page():
    body = """<h1>Hotels ranked by nearby Michelin restaurants</h1>
<div class="note"><b>Status: not started.</b> No hotel list has been collected from an official source, so no ranking is shown. Ranking needs a rule first (see Suggestions S4) and then official hotel data.</div>
<h2>Facts already verified from Michelin's official article</h2>
<ul class="plain">
<li>SingleThread Inn (Healdsburg, Wine Country): Three MICHELIN Keys. Link: <a href="https://guide.michelin.com/us/en/hotels-stays/napa-sonoma-valleys/singlethread-inn-13698">Michelin hotel page</a> (source: <a href="https://guide.michelin.com/en/article/michelin-guide-ceremony/guide-michelin-california">official article</a>).</li>
<li>Bernardus Lodge &amp; Spa (Carmel Valley, outside core): Two MICHELIN Keys. Link: <a href="https://guide.michelin.com/us/en/hotels-stays/carmel-monterey/bernardus-lodge-spa-5909">Michelin hotel page</a>.</li>
</ul>
<h2>Method (proposed, not applied)</h2>
<ul class="plain">
<li>Hotel list: Michelin hotel selection for the Bay Area plus official hotel websites.</li>
<li>Count: starred and Bib restaurants within a fixed straight-line radius (e.g., 1.6 km / 1 mile) of the hotel, using official coordinates.</li>
<li>Score: 3★ = 3, 2★ = 2, 1★ = 1, Bib = 0.5 (weights not yet approved).</li>
</ul>"""
    return page("Hotels", "hotels.html", body)


def qa_page():
    ans = "".join(
        f'<div class="qa"><b>{e(q["q"])}</b>{e(q["a"])}<br><small>Source: <a href="{e(q["source"])}">{e(q["source"])}</a></small></div>'
        for q in A["questions"]["answered"])
    opn = "".join(
        f'<div class="qa"><b>{e(q["q"])}</b>Why it matters: {e(q["why"])}<br><small>How to find it: {e(q["how_to_find"])}</small></div>'
        for q in A["questions"]["open"])
    body = f"""<h1>Questions, answers and gaps</h1>
<p class="lead">What we know (with sources), and what must be answered before a decision.</p>
<h2>Answered from official sources</h2>{ans}
<h2>Still open (needed before a decision)</h2>{opn}"""
    return page("Questions", "questions.html", body)


def sug_page():
    items = "".join(
        f'<div class="qa"><b>{e(s["id"])} · {e(s["title"])}</b>{e(s["detail"])}<br>'
        f'<small>Effort: {e(s["effort"])} · Impact: {e(s["impact"])} · <span class="unv">{e(s["status"])}</span></small></div>'
        for s in A["suggestions"])
    body = f"""<h1>Suggestions for review</h1>
<div class="note"><b>Nothing here has been implemented.</b> Choose the suggestions you want (e.g., “do S1, S2, S7”). Only chosen items will be built.</div>
{items}"""
    return page("Suggestions", "suggestions.html", body)


def flagged_page():
    rr = "".join(
        f'<tr><td class="name">{e(x["item"])}</td><td>{e(x["finding"])}</td><td>{e(x["flag"])}</td>'
        f'<td><a href="{e(x["source"])}">link</a></td></tr>' for x in A["repo_review"])
    di = "".join(
        f'<tr><td class="name">{e(x["item"])}</td><td>{e(x["conflict"])}</td><td>{e(x["used"])}</td>'
        f'<td><a href="{e(x["source"])}">link</a></td></tr>' for x in A["data_irregularities"])
    unv_rows = [r["name"] for r in starred if not r["verification"].startswith("Full")]
    body = f"""<h1>Flagged for review</h1>
<p class="lead">Items to review by hand. Nothing here is marked verified unless it is linked to an official source.</p>
<h2>Repo review</h2>
<div class="tblwrap"><table><tr><th>Item</th><th>Finding</th><th>Flag</th><th>Source</th></tr>{rr}</table></div>
<h2>Data irregularities and conflicts</h2>
<div class="tblwrap"><table><tr><th>Item</th><th>Conflict</th><th>Used</th><th>Source</th></tr>{di}</table></div>
<h2>Starred rows verified only at list level ({len(unv_rows)})</h2>
<p>{e(', '.join(unv_rows))}. Their address, hours, and price tier must be checked on the Michelin page.</p>"""
    return page("Flagged", "flagged.html", body)


def sources_page():
    srcs = [
        ("Michelin press release: MICHELIN Guide California 2026 (Bib list, addresses, star changes)", R["michelin_sources"]["official_press_release"]),
        ("Michelin press release PDF (26 June 2026)", R["michelin_sources"]["official_press_release_pdf"]),
        ("Michelin Guide article: every starred restaurant in California 2026", R["michelin_sources"]["official_article"]),
        ("Michelin restaurant page: Benu", "https://guide.michelin.com/us/en/california/san-francisco/restaurant/benu"),
        ("Michelin restaurant page: Atelier Crenn", "https://guide.michelin.com/us/en/california/san-francisco/restaurant/atelier-crenn"),
        ("Third-party cross-check (not used for counts): SF Chronicle, Bay Area stars", "https://www.sfchronicle.com/food/restaurants/article/2026-michelin-stars-of-bay-area-22317064.php"),
        ("Third-party cross-check: Eastbay Times full NorCal list", "https://www.eastbaytimes.com/2026/06/25/full-list-of-norcals-2026-michelin-star-restaurants/"),
    ]
    rows = "".join(f'<tr><td>{e(t)}</td><td><a href="{e(u)}">{e(u)}</a></td></tr>' for t, u in srcs)
    body = f"""<h1>Sources</h1>
<p class="lead">Official sources are Michelin's own pages. Third-party pages were used only to cross-check.</p>
<div class="tblwrap"><table><tr><th>Source</th><th>Link</th></tr>{rows}</table></div>"""
    return page("Sources", "sources.html", body)


def index_page():
    cards = [
        (len(core_starred), "Starred, core Bay Area"),
        (len(sf_starred), "Starred, San Francisco"),
        (sum(1 for r in sf_starred if r["tier"] == "Three Stars"), "3-star, San Francisco"),
        (len(bibs), "Bib Gourmand, core Bay Area"),
        (len(full_verified), "Rows fully verified (Michelin page)"),
        (len(A["questions"]["open"]), "Open questions"),
    ]
    card_html = "".join(f'<div class="card"><b>{n}</b><small>{e(l)}</small></div>' for n, l in cards)
    summ = "".join(f"<li>{e(s)}</li>" for s in A["executive_summary"])
    nav_cards = "".join(
        f'<a class="card" href="{h}" style="text-decoration:none;color:inherit"><b style="font-size:16px">{e(l)}</b></a>'
        for h, l in NAV[1:])
    body = f"""<h1>Executive summary</h1>
<p class="lead">Michelin restaurants in the San Francisco Bay Area, as of {ASOF}. Built from official sources; gaps are flagged, not filled in.</p>
<div class="cards">{card_html}</div>
<div class="cards">{nav_cards}</div>
<h2>Key points</h2>
<ul class="plain">{summ}</ul>
<div class="note"><b>Not yet delivered:</b> exact 2-adult prices, social links, hotel ranking, and hours for some rows. See <a href="questions.html">Questions</a> and <a href="suggestions.html">Suggestions</a> to choose the next step.</div>"""
    return page("Home", "index.html", body)


PAGES = {
    "index.html": index_page,
    "stars.html": stars_page,
    "bib.html": bib_page,
    "clusters.html": cluster_page,
    "hotels.html": hotels_page,
    "questions.html": qa_page,
    "suggestions.html": sug_page,
    "flagged.html": flagged_page,
    "sources.html": sources_page,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in PAGES.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(fn())
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")
    print(f"Built {len(PAGES)} pages into {OUT}")
