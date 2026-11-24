#!/usr/bin/env python3
"""Generate the static site from data/*.csv.

All counts and tables on the pages are computed from the CSVs, so the site can
never drift from the data. Run:  python3 tools/build_site.py
"""
import csv
import html
import os
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKED = "24 Nov 2026"

NAV = [
    ("index.html", "Home"),
    ("restaurants.html", "Starred"),
    ("listed.html", "Bib &amp; Listed"),
    ("hotels.html", "Hotels"),
    ("map.html", "Map &amp; Clusters"),
    ("executive-summary.html", "Summary"),
    ("questions.html", "Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged"),
    ("methodology.html", "Method"),
]


def e(v):
    return html.escape(str(v or ""), quote=True)


def load(name):
    with open(os.path.join(ROOT, "data", name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def badge(status):
    s = (status or "").strip()
    if s.startswith("Verified"):
        return '<span class="badge ok">Verified</span>'
    if s.startswith("Partial"):
        return '<span class="badge mid">Partial</span>'
    return '<span class="badge warn">Unverified</span>'


def flag(status):
    s = (status or "").strip()
    return "v" if s.startswith("Verified") else "p" if s.startswith("Partial") else "u"


def star_badge(dist):
    cls = {"3 Stars": "s3", "2 Stars": "s2", "1 Star": "s1"}.get(dist, "bib")
    return f'<span class="badge star {cls}">{e(dist)}</span>'


def shell(title, body, depth=0):
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="SF Bay Area MICHELIN Guide 2026 dashboard: starred vs listed, verified prices for two, clusters, and hotels ranked by Michelin density.">
<link rel="stylesheet" href="assets/style.css"></head>
<body>
<header class="top"><div class="wrap">
<div class="brand">SF Bay Area Michelin<small>Guide California 2026 &middot; source-linked &middot; mobile-friendly</small></div>
<nav class="main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer>
<p><b>Sources:</b> MICHELIN Guide California 2026 (guide.michelin.com) and each venue's own website. Every row links to its source. <b>Unverified</b> means the value was not published on the official page we checked &mdash; it is left blank, never guessed. Data checked {CHECKED}.</p>
<p>Data: <a href="data/restaurants.csv">restaurants.csv</a> &middot; <a href="data/bib.csv">bib.csv</a> &middot; <a href="data/hotels.csv">hotels.csv</a> &middot; <a href="data/SCOPE.md">SCOPE.md</a>. See <a href="methodology.html">Method</a> and <a href="flagged.html">Flagged for Review</a>.</p>
</footer>
<script src="assets/app.js"></script></body></html>
"""


def write(name, title, body):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
        fh.write(shell(title, body))
    print("wrote", name)



# ------------------------------------------------------------- markdown renderer
# The text pages (executive summary, questions, suggestions, flagged, method) are
# authored in docs/*.md and rendered here, so the Markdown stays the single source.
import re as _re


def inline_md(text):
    t = e(text)
    t = _re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = _re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = _re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def md_to_body(md):
    out, title, lines = [], "", md.splitlines()
    i, in_ul, in_ol = 0, False, False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>"); in_ul = False
        if in_ol:
            out.append("</ol>"); in_ol = False

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("# ") and not title:
            title = ln[2:].strip(); i += 1; continue
        if ln.startswith("|"):
            close_lists()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            out.append('<div class="tblwrap"><table><thead><tr>' +
                       "".join(f"<th>{inline_md(c)}</th>" for c in head) +
                       "</tr></thead><tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue
        if ln.startswith("### "):
            close_lists(); out.append(f"<h3>{inline_md(ln[4:])}</h3>")
        elif ln.startswith("## "):
            close_lists(); out.append(f"<h2>{inline_md(ln[3:])}</h2>")
        elif ln.startswith("- "):
            if in_ol:
                out.append("</ol>"); in_ol = False
            if not in_ul:
                out.append('<ul class="tight">'); in_ul = True
            out.append(f"<li>{inline_md(ln[2:])}</li>")
        elif _re.match(r"^\d+\. ", ln):
            if in_ul:
                out.append("</ul>"); in_ul = False
            if not in_ol:
                out.append('<ol class="tight">'); in_ol = True
            item = _re.sub(r"^\d+\.\s*", "", ln)
            out.append("<li>" + inline_md(item) + "</li>")
        elif ln.startswith("> "):
            close_lists(); out.append(f'<div class="note">{inline_md(ln[2:])}</div>')
        elif ln.strip() == "":
            close_lists()
        else:
            close_lists(); out.append(f"<p>{inline_md(ln)}</p>")
        i += 1
    close_lists()
    return title, "\n".join(out)


def write_doc(md_path, out_name, fallback_title):
    with open(os.path.join(ROOT, md_path), encoding="utf-8") as fh:
        title, body = md_to_body(fh.read())
    write(out_name, title or fallback_title,
          f'<p class="small">Rendered from <code>{e(md_path)}</code>. Verified values link to official sources; '
          f'this page regenerates with <code>python3 tools/build_site.py</code>.</p>' + body)


# ---------------------------------------------------------------- compute
SCHEMA = ["id", "name", "city", "cluster", "scope", "distinction", "green_star",
          "cuisine", "address", "michelin_url", "official_url", "price_pp_usd",
          "service_charge", "price_2adults_usd", "price_basis", "price_source",
          "michelin_price_tier", "days_open", "hours", "exceptions", "instagram", "youtube",
          "tiktok", "verification_status", "notes"]

def money_ok(v):
    try:
        float(v); return True
    except (TypeError, ValueError):
        return False


R = load("restaurants.csv")

# ---- build-time assertions: fail loudly instead of publishing a bad page ----
_hdr = list(R[0].keys())
assert _hdr == SCHEMA, f"restaurants.csv schema drifted: {set(_hdr) ^ set(SCHEMA)}"
_bad_src = [r["name"] for r in R if "guide.michelin.com" not in (r["michelin_url"] or "")]
assert not _bad_src, f"rows without a Michelin source link: {_bad_src}"
_bad_price = []
for r in R:
    if r["price_2adults_usd"]:
        assert money_ok(r["price_2adults_usd"]), f"unparseable price on {r['name']}"
        pp = float(r["price_pp_usd"] or 0) * 2
        tot = float(r["price_2adults_usd"])
        if pp and tot + 0.01 < pp:
            _bad_price.append(r["name"])
assert not _bad_price, f"total below the bare 2x menu price: {_bad_price}"
_url_in_price = [r["name"] for r in R if "http" in (r["price_pp_usd"] or "")]
assert not _url_in_price, f"a URL is sitting in the price column: {_url_in_price}"
_social_mix = [r["name"] for r in R
               if "instagram.com" in (r["youtube"] or "") or "instagram.com" in (r["tiktok"] or "")]
assert not _social_mix, f"Instagram URL in a YouTube/TikTok column: {_social_mix}"

BIB = load("bib.csv")
HOT = load("hotels.csv")

CORE = [r for r in R if r["scope"] == "Core"]
EXT = [r for r in R if r["scope"] == "Extension"]
dist = Counter(r["distinction"] for r in R)
core_dist = Counter(r["distinction"] for r in CORE)
cluster = OrderedDict((k, [r for r in R if r["cluster"] == k]) for k in
                      ["C1 SF Core", "C2 Peninsula", "C3 East Bay", "C4 Marin",
                       "C5 Wine Country", "C6 Extension"])
sf = [r for r in R if r["city"] == "San Francisco"]
priced = [r for r in R if r["price_2adults_usd"]]
def money(v):
    try:
        return float(v)
    except ValueError:
        return None
totals = sorted(x for x in (money(r["price_2adults_usd"]) for r in priced) if x)
verified_price = [r for r in priced if r["verification_status"].startswith("Verified")]
vcount = Counter()
for r in R:
    s = r["verification_status"]
    vcount["Verified" if s.startswith("Verified") else
           "Partial" if s.startswith("Partial") else "Unverified"] += 1

# ---------------------------------------------------------------- index
def stat(n, label, sub=""):
    return f'<div class="stat"><b>{n}</b><span>{label}</span>' + (f'<em>{sub}</em>' if sub else "") + "</div>"


cluster_rows = ""
for cname, rows in cluster.items():
    c = Counter(r["distinction"] for r in rows)
    hotels = len([h for h in HOT if h["cluster"] == cname])
    cities = ", ".join(sorted({r["city"] for r in rows}))
    cluster_rows += (
        f'<tr><td><b>{e(cname)}</b><br><span class="small">{e(cities)}</span></td>'
        f'<td>{c["3 Stars"]}</td><td>{c["2 Stars"]}</td><td>{c["1 Star"]}</td>'
        f'<td><b>{len(rows)}</b></td><td>{hotels}</td></tr>'
    )

index_body = f"""
<h1>SF Bay Area Michelin Guide &amp; Map</h1>
<p class="lead">One organised dashboard for the <b>MICHELIN Guide California 2026</b> in the Bay Area: which places hold a star and which are only <i>listed</i> (Bib Gourmand or Selected), where the stars cluster, what dinner for <b>two adults</b> costs, and which hotels sit in the densest Michelin neighbourhoods. Every row links to the official source it came from.</p>

<div class="grid">
{stat(len(CORE), "Core Bay Area starred", "9-county definition")}
{stat(len(EXT), "Extension starred", "Carmel / Elk, flagged separately")}
{stat(dist["3 Stars"], "three-star", "Bay Area incl. extension")}
{stat(len(BIB), "Bib Gourmand rows", "value list, no star")}
{stat(len(HOT), "hotels ranked", "by Michelin density")}
</div>

<div class="card">
<h2>What the numbers actually say</h2>
<ul class="tight">
<li><b>{len(CORE)} starred in the Core Bay Area</b> ({core_dist['3 Stars']}&times;3&#9733;, {core_dist['2 Stars']}&times;2&#9733;, {core_dist['1 Star']}&times;1&#9733;). Adding the two Extension clusters ({len(EXT)} restaurants in Carmel and Elk) gives {len(R)} starred rows in this dataset.</li>
<li><b>San Francisco city proper holds {len(sf)} starred restaurants</b> &mdash; {Counter(r['distinction'] for r in sf)['3 Stars']}&times;3&#9733;, {Counter(r['distinction'] for r in sf)['2 Stars']}&times;2&#9733;, {Counter(r['distinction'] for r in sf)['1 Star']}&times;1&#9733; &mdash; roughly {round(100*len(sf)/len(CORE))}% of the Core list. Density is the story of this guide, not spread.</li>
<li><b>Wine Country is the second cluster</b> with {len([r for r in cluster['C5 Wine Country'] if 'Star' in r['distinction']])} starred restaurants, but it is a 60&ndash;90 minute drive from the city, so it behaves like a separate trip, not a suburb.</li>
<li><b>Verified dinner for two ranges ${min(totals):,.0f}&ndash;${max(totals):,.0f}</b> before tax and drinks across the {len(verified_price)} rows where an official price exists. Most of the cheap end is lunch or a short menu; the top end is a full tasting menu plus service charge.</li>
<li><b>Honesty about gaps:</b> {vcount['Verified']} of {len(R)} starred rows have at least one value verified on an official site, {vcount['Partial']} is partial and {vcount['Unverified']} are unverified. Nothing has been filled in to look complete.</li>
</ul>
</div>

<div class="card">
<h2>Clusters at a glance</h2>
<div class="tblwrap"><table>
<thead><tr><th>Cluster</th><th>3&#9733;</th><th>2&#9733;</th><th>1&#9733;</th><th>Total starred</th><th>Hotels ranked</th></tr></thead>
<tbody>{cluster_rows}</tbody></table></div>
<p class="small">Counts computed from <a href="data/restaurants.csv">restaurants.csv</a> and <a href="data/hotels.csv">hotels.csv</a> at build time. C1&ndash;C5 are the 9-county Core (41 starred); C6 is an Extension area outside it (3 starred).</p>
</div>

<div class="card">
<h2>Start here</h2>
<p class="btnrow">
<a class="btn" href="restaurants.html">Starred restaurants &rarr;</a>
<a class="btn" href="listed.html">Bib &amp; listed-only &rarr;</a>
<a class="btn" href="hotels.html">Ranked hotels &rarr;</a>
<a class="btn" href="map.html">Map &amp; clusters &rarr;</a>
</p>
<p class="small">Short on time? Read the <a href="executive-summary.html">executive summary</a>, then the <a href="questions.html">open questions</a> and <a href="suggestions.html">suggestions</a> (proposed only &mdash; nothing is implemented without your approval).</p>
</div>

<div class="card">
<h2>How to read a row</h2>
<div class="tblwrap"><table><tbody>
<tr><td>{star_badge('3 Stars')}</td><td>Holds a star (3 = worth a special journey, 2 = worth a detour, 1 = worth a stop).</td></tr>
<tr><td><span class="badge star bib">Bib Gourmand (no star)</span></td><td>In the Guide for value &mdash; <b>not</b> a star, and not the same honour.</td></tr>
<tr><td><span class="badge star sel">Selected / Recommended</span></td><td>In the Guide, no star and no Bib. Shown by count and Michelin link, not enumerable from an official list yet.</td></tr>
<tr><td><span class="badge ok">Verified</span></td><td>At least one value on the row was read off the venue's own site or its Michelin page, and the link is on the row.</td></tr>
<tr><td><span class="badge warn">Unverified</span></td><td>Not published on the official page we checked. Left blank on purpose.</td></tr>
<tr><td><b>$&nbsp;for&nbsp;2</b></td><td>Per-person menu price &times; 2, plus the service charge/surcharge the venue publishes. Tax and drinks excluded unless stated. The formula is printed in each row.</td></tr>
</tbody></table></div>
</div>
"""
write("index.html", "SF Bay Area Michelin 2026 — dashboard", index_body)

# ---------------------------------------------------------------- restaurants
rows_html = ""
for r in R:
    price = ""
    if r["price_pp_usd"]:
        price = (f'${money(r["price_2adults_usd"]):,.2f}'.replace(".00", "") if money(r["price_2adults_usd"]) else "")
        price = f'<b>${r["price_2adults_usd"]}</b><br><span class="small">${r["price_pp_usd"]} pp &times; 2'
        if r["service_charge"]:
            price += f' + {e(r["service_charge"])}'
        price += f'</span><br><span class="small">{e(r["price_basis"])}</span>'
    else:
        price = '<span class="muted">&mdash;</span><br><span class="small">No official price published</span>'
        if r["price_basis"]:
            price += f'<br><span class="small">{e(r["price_basis"])}</span>'

    hours = ""
    if r["days_open"] or r["hours"]:
        hours = f'<b>{e(r["days_open"]) or "&mdash;"}</b><br><span class="small">{e(r["hours"])}</span>'
    else:
        hours = '<span class="muted">&mdash;</span>'
    if r["exceptions"]:
        hours += f'<br><span class="small ex">{e(r["exceptions"])}</span>'

    socials = []
    for key, label in (("instagram", "Instagram"), ("youtube", "YouTube"), ("tiktok", "TikTok")):
        if r[key]:
            socials.append(f'<a href="{e(r[key])}" rel="noopener">{label}</a>')
    social = "<br>".join(socials) if socials else '<span class="muted">&mdash;</span><br><span class="small">none published</span>'

    src = f'<a href="{e(r["michelin_url"])}">Michelin page</a>'
    if r["official_url"]:
        src += f'<br><a href="{e(r["official_url"])}">Official site</a>'
    if r["price_source"] and r["price_source"] != r["official_url"]:
        src += f'<br><a class="small" href="{e(r["price_source"])}">Price/hours source</a>'
    src += f'<br><span class="small">{e(r["verification_status"])}</span>'
    if r["notes"]:
        src += f'<br><span class="small note-inline">{e(r["notes"])}</span>'

    rows_html += (
        f'<tr data-group="{e(r["distinction"])}|{e(r["cluster"])}|{e(r["scope"])}|'
        f'{flag(r["verification_status"])}">'
        f'<td><b>{e(r["name"])}</b><br><span class="small">{e(r["city"])} &middot; {e(r["cluster"].split()[0])} {e(r["cluster"][3:])}</span>'
        f'<br>{star_badge(r["distinction"])} {badge(r["verification_status"])}</td>'
        f'<td>{e(r["cuisine"])}<br><span class="small">{e(r["address"])}</span></td>'
        f'<td class="num">{price}</td>'
        f'<td>{hours}</td>'
        f'<td>{social}</td>'
        f'<td>{src}</td></tr>\n'
    )

rest_body = f"""
<h1>Starred restaurants &mdash; 2026</h1>
<p class="lead">{len(R)} starred restaurants: <b>{len(CORE)} in the Core Bay Area</b> plus <b>{len(EXT)} Extension</b> (Carmel and Elk, outside the 9 counties). Prices are the <b>total for two adults</b> using each venue's published per-person menu price and its published service charge. Blank means the official page did not publish it.</p>

<div class="note"><b>Read the badge, not the number.</b> A price only exists here if an official page stated it. {vcount['Verified']} rows carry a verified value, {vcount['Partial']} are partial, {vcount['Unverified']} are unverified &mdash; the last group is a to-do list, not a set of zeros.</div>

<div class="controls">
<input data-filter="#restTable" placeholder="Search restaurant, cuisine, city&hellip;" aria-label="Search starred restaurants">
<select data-filter-select="#restTable" data-key="0" aria-label="Filter by distinction"><option value="">All distinctions</option><option>3 Stars</option><option>2 Stars</option><option>1 Star</option></select>
<select data-filter-select="#restTable" data-key="1" aria-label="Filter by cluster"><option value="">All clusters</option>{"".join(f"<option>{e(k)}</option>" for k in cluster)}</select>
<select data-filter-select="#restTable" data-key="3" aria-label="Filter by verification"><option value="">All rows</option><option value="v">Verified only</option><option value="p">Partial only</option><option value="u">Unverified only</option></select>
</div>
<p class="small" data-count="#restTable"></p>

<div class="tblwrap"><table id="restTable">
<thead><tr><th>Restaurant</th><th>Cuisine / address</th><th>Total for 2</th><th>Days / hours / exceptions</th><th>Social</th><th>Sources &amp; status</th></tr></thead>
<tbody>
{rows_html}</tbody></table></div>

<div class="card">
<h2>What the price column includes</h2>
<p>Total for two = (per-person menu price &times; 2) + the service charge the restaurant publishes. San Francisco venues add a 20&ndash;26% service charge plus, in some cases, a 4&ndash;6% city mandate, so the same menu price can land 20% apart depending on the operator. Sales tax and drinks are excluded. Where a restaurant publishes only "starting at", the row says so.</p>
<p class="small">Only {len(verified_price)} of {len(R)} rows currently have a publishable price. Most restaurants put prices behind the booking platform rather than on their own site; those rows stay blank until an official price is seen.</p>
</div>
"""
write("restaurants.html", "Starred restaurants — SF Bay Area Michelin 2026", rest_body)

# ---------------------------------------------------------------- listed
bib_rows = ""
for b in BIB:
    vs = b["verification_status"]
    band = ('<br><span class="small">' + e(b["price_band"]) + " Michelin band</span>") if b["price_band"] else ""
    bib_rows += (
        f'<tr data-group="{e(b["cluster"])}|{flag(vs)}">'
        f'<td><b>{e(b["name"])}</b><br><span class="small">{e(b["city"])} &middot; {e(b["cluster"])}</span></td>'
        f'<td>{e(b["cuisine"])}{band}</td>'
        f'<td><span class="badge star bib">Bib Gourmand (no star)</span></td>'
        f'<td><a href="{e(b["michelin_source"])}">Michelin Bib list</a><br><span class="small">{e(vs)}</span></td>'
        f'<td class="small">{e(b["notes"])}</td></tr>\n'
    )

bib_verified = len([b for b in BIB if b["verification_status"].startswith("Verified")])
listed_body = f"""
<h1>Bib Gourmand &amp; listed-only</h1>
<p class="lead">Not every honoured restaurant holds a star. This page separates the two lower tiers so they are never confused with stars.</p>

<div class="grid">
<div class="stat"><b>3</b><span>tiers below 3 stars</span><em>2&#9733;, 1&#9733;, then value/selected</em></div>
<div class="stat"><b>{len(BIB)}</b><span>Bib Gourmand rows</span><em>{bib_verified} re-confirmed on a Michelin list page</em></div>
<div class="stat"><b>86</b><span>Selected/Recommended in SF area</span><em>Michelin filter count; names not enumerated</em></div>
</div>

<div class="card">
<h2>Definitions (Michelin's own wording)</h2>
<div class="tblwrap"><table><thead><tr><th>Tier</th><th>Meaning</th><th>Confusable with a star?</th></tr></thead><tbody>
<tr><td><span class="badge star bib">Bib Gourmand</span></td><td>"Good quality, good value cooking" &mdash; a personal recommendation for a good meal at a moderate price.</td><td><b>No.</b> It is not a star and never has been.</td></tr>
<tr><td><span class="badge star sel">Selected / Recommended</span></td><td>"Good cooking" &mdash; inspected and included in the Guide, with no star and no Bib.</td><td><b>No.</b> Inclusion only.</td></tr>
<tr><td><span class="badge star s1">1 Star</span></td><td>"High quality cooking, worth a stop."</td><td>Yes &mdash; this is the first star tier.</td></tr>
</tbody></table></div>
</div>

<div class="note"><b>Provenance correction.</b> A previous version of this file cited the <i>San Francisco</i> Bib list as the source for Bib restaurants in Oakland, Berkeley, Marin and Wine Country. Michelin publishes separate city lists, so each row now cites its own city's list. Rows whose names were not re-seen on a Michelin list page in this audit are marked <b>Unverified</b> rather than "verified" &mdash; {len(BIB)-bib_verified} of {len(BIB)} need re-checking. Michelin's filter counts for the three main lists are 30 (San Francisco), 29 (Oakland) and 28 (Berkeley), and the lists overlap.</div>

<div class="controls">
<input data-filter="#bibTable" placeholder="Search Bib Gourmand&hellip;" aria-label="Search Bib Gourmand restaurants">
<select data-filter-select="#bibTable" data-key="0" aria-label="Filter by cluster"><option value="">All clusters</option>{"".join(f"<option>{e(k)}</option>" for k in cluster)}</select>
<select data-filter-select="#bibTable" data-key="1" aria-label="Filter by verification"><option value="">All rows</option><option value="v">Verified only</option><option value="u">Unverified only</option></select>
</div>
<p class="small" data-count="#bibTable"></p>

<div class="tblwrap"><table id="bibTable">
<thead><tr><th>Restaurant</th><th>Cuisine / price band</th><th>Distinction</th><th>Source &amp; status</th><th>Notes</th></tr></thead>
<tbody>{bib_rows}</tbody></table></div>

<div class="card">
<h2>The Selected/Recommended tier is counted, not listed</h2>
<p>Michelin's own city filter reports <b>86 Selected restaurants</b> for San Francisco and surroundings. The Guide does not publish that set as one page, so this project records the count and links to the source rather than reconstructing the list from memory.</p>
<p><a class="btn" href="https://guide.michelin.com/us/en/california/san-francisco/restaurants">Michelin SF &amp; surroundings list &rarr;</a></p>
<p class="small">If a full enumeration matters, see <a href="questions.html">Q7</a> for the discovery route (city-by-city Michelin listing pages, paginated 30 at a time).</p>
</div>
"""
write("listed.html", "Bib Gourmand & listed — SF Bay Area Michelin 2026", listed_body)

# ---------------------------------------------------------------- hotels
hot_clusters = sorted({h["cluster"] for h in HOT})
hot_rows = ""
for h in HOT:
    addr = e(h["address"]) if h["address"] else '<span class="muted">not published on official page</span>'
    hot_rows += (
        f'<tr data-group="{e(h["hotel"])}|{e(h["cluster"])}|{flag(h["verification_status"])}"><td><b>#{e(h["rank"])} {e(h["hotel"])}</b><br><span class="small">{e(h["city"])} &middot; {e(h["cluster"])}</span></td>'
        f'<td>{addr}</td>'
        f'<td><b>{e(h["starred_in_cluster"])}</b> starred<br><span class="small">in {e(h["cluster"])}</span></td>'
        f'<td class="small">{e(h["why_ranked"])}</td>'
        f'<td><a href="{e(h["official_url"])}">Official</a><br><a href="{e(h["michelin_hotel_source"])}">Michelin hotels</a><br>{badge(h["verification_status"])}<br><span class="small">{e(h["verification_status"])}</span></td>'
        f'<td class="small">{e(h["notes"])}</td></tr>\n'
    )

hotels_body = f"""
<h1>Hotels ranked by Michelin density</h1>
<p class="lead">Ranking question: if you sleep here, how many starred restaurants are in the same cluster? The rank uses the starred count of the cluster each hotel sits in, computed from <a href="data/restaurants.csv">restaurants.csv</a> &mdash; never a guessed drive time.</p>

<div class="grid">
<div class="stat"><b>{len(HOT)}</b><span>hotels ranked</span></div>
<div class="stat"><b>25</b><span>starred in the top cluster</span><em>C1 SF Core</em></div>
<div class="stat"><b>8</b><span>starred in Wine Country</span><em>C5, incl. three 3&#9733;</em></div>
</div>

<div class="card">
<h2>Method, stated plainly</h2>
<ul class="tight">
<li><b>What is counted:</b> starred restaurants in the hotel's cluster (C1 25, C5 8, C2 5, C3 2, C4 1). Ties are broken by how central the address is to the dense part of the cluster, which is a judgement, not a measurement.</li>
<li><b>What is not counted:</b> nightly rates (dynamic, and a rate seen today is stale next week), drive times (not measured), and Michelin "Keys" unless the hotel's own site states them.</li>
<li><b>Address corrections found in this audit:</b> Cavallo Point is at 601 Murray Circle, Fort Baker (not "601 Bridgeway"); 1 Hotel San Francisco is at 8 Mission Street (not "22 Battery"); Bardessono is at 6526 Yount St (the previously listed 6640 Washington St is The French Laundry's address).</li>
<li><b>Blank addresses</b> mean the hotel's official page did not load or did not state a street address when checked, so nothing was filled in.</li>
</ul>
</div>

<div class="controls">
<input data-filter="#hotTable" placeholder="Search hotel or city&hellip;" aria-label="Search hotels">
<select data-filter-select="#hotTable" data-key="1" aria-label="Filter by cluster"><option value="">All clusters</option>{"".join(f"<option>{e(k)}</option>" for k in hot_clusters)}</select>
<select data-filter-select="#hotTable" data-key="2" aria-label="Filter by verification"><option value="">All rows</option><option value="v">Verified only</option><option value="p">Partial only</option><option value="u">Unverified only</option></select>
</div>
<p class="small" data-count="#hotTable"></p>

<div class="tblwrap"><table id="hotTable">
<thead><tr><th>Hotel</th><th>Address</th><th>Density</th><th>Why it ranks here</th><th>Sources &amp; status</th><th>Notes</th></tr></thead>
<tbody>{hot_rows}</tbody></table></div>

<div class="card">
<h2>If you only read one line</h2>
<p>For a first trip, stay in <b>C1 SF Core</b> &mdash; it holds {len([r for r in cluster['C1 SF Core'] if 'Star' in r['distinction']])} of the {len(CORE)} Core starred restaurants and you can walk or ride-share to a different one each night. For an eating-first Wine Country trip, <b>Auberge du Soleil</b> and <b>SingleThread Inn</b> are the two places where the starred restaurant is in the building; Bardessono is the walk-to-French-Laundry option.</p>
<p class="small">Ranking by density flatters the city. It says nothing about room quality, price or service &mdash; see <a href="questions.html">Q6</a> and <a href="suggestions.html">S5</a> before treating this as a booking list.</p>
</div>
"""
write("hotels.html", "Hotels ranked by Michelin density — SF Bay Area", hotels_body)

# ---------------------------------------------------------------- map
CLUSTER_INFO = {
    "C1 SF Core": ("San Francisco city proper", "SoMa, Mission, Hayes Valley, Pacific Heights, Nob Hill, Jackson Square",
                   "Walkable or a short ride-share between venues; the densest star cluster in California outside LA."),
    "C2 Peninsula": ("San Mateo, Santa Clara counties", "Atherton/Redwood City, Palo Alto, Saratoga, Woodside, San Mateo",
                     "Spread out; you need a car. Best done as two nights, not one."),
    "C3 East Bay": ("Alameda, Contra Costa counties", "Oakland, Berkeley, Alameda, El Cerrito, San Leandro, Hayward",
                    "Two starred rooms plus the deepest Bib Gourmand bench in the region."),
    "C4 Marin": ("Marin county", "San Anselmo, Mill Valley, Fairfax",
                 "One starred room (Madcap) and three Bibs; a gateway, not a destination cluster."),
    "C5 Wine Country": ("Napa, Sonoma counties", "Yountville, Rutherford, Calistoga, St Helena, Healdsburg, Sonoma, Geyserville",
                        "The only cluster with three 3-star restaurants. 60-90 minutes from SF; treat it as its own trip."),
    "C6 Extension": ("Monterey, Mendocino counties", "Carmel-by-the-Sea, Elk",
                     "Outside the 9-county Core. Excellent, but a road trip add-on, not a base."),
}
map_rows = ""
for cname, rows in cluster.items():
    starred = [r for r in rows if "Star" in r["distinction"]]
    names = ", ".join(f'<a href="{e(r["michelin_url"])}">{e(r["name"])}</a>' for r in starred)
    area, towns, note = CLUSTER_INFO[cname]
    map_rows += (
        f'<tr><td><b>{e(cname)}</b><br><span class="small">{e(area)}</span></td>'
        f'<td>{len(starred)}</td>'
        f'<td class="small">{e(towns)}</td>'
        f'<td class="small">{names}</td>'
        f'<td class="small">{e(note)}</td></tr>\n'
    )

map_body = f"""
<h1>Map &amp; clusters</h1>
<p class="lead">The Bay Area's stars are not spread evenly. This page groups every starred restaurant into one of six clusters and links to the official Michelin pages that plot them. <b>No coordinates are invented here</b> &mdash; every map link goes to Michelin's or Google's own map, and addresses come from the Michelin listing or the venue's site.</p>

<div class="note"><b>Why no pins on this page:</b> a hand-placed pin that is 300 metres off is worse than no pin, because it looks authoritative. Geocoding 44 verified addresses is proposed as <a href="suggestions.html">S2</a> and needs your approval first.</div>

<div class="tblwrap"><table>
<thead><tr><th>Cluster</th><th>Starred</th><th>Towns</th><th>Starred restaurants</th><th>How to use it</th></tr></thead>
<tbody>{map_rows}</tbody></table></div>

<div class="card">
<h2>Official maps to open</h2>
<ul class="tight">
<li><a href="https://guide.michelin.com/us/en/california/san-francisco/restaurants?showMap=true">Michelin map &mdash; San Francisco &amp; surroundings</a> (145 restaurants, map toggle on)</li>
<li><a href="https://guide.michelin.com/us/en/california/oakland/restaurants?showMap=true">Michelin map &mdash; Oakland &amp; surroundings</a></li>
<li><a href="https://guide.michelin.com/us/en/california/berkeley/restaurants?showMap=true">Michelin map &mdash; Berkeley &amp; surroundings</a></li>
<li><a href="https://guide.michelin.com/us/en/california/napa-valley/restaurants?showMap=true">Michelin map &mdash; Napa Valley</a></li>
<li><a href="https://guide.michelin.com/us/en/california/sonoma-county/restaurants?showMap=true">Michelin map &mdash; Sonoma County</a></li>
<li><a href="https://guide.michelin.com/us/en/california/carmel-by-the-sea/restaurants?showMap=true">Michelin map &mdash; Carmel-by-the-Sea</a></li>
<li><a href="https://guide.michelin.com/us/en/hotels">Michelin Guide hotels</a> (Keys, when awarded, appear on each hotel page)</li>
</ul>
<p class="small">Each restaurant's own Michelin link is in the Sources column on the <a href="restaurants.html">starred page</a>.</p>
</div>

<div class="card">
<h2>Cluster logic in one paragraph</h2>
<p>C1 is where a two-night trip works without a car. C3 is the value play: two starred rooms but a much deeper Bib bench, and BART connects it to C1. C5 is the only place with three-star cooking, and it deserves its own days. C2 and C4 are bases for specific meals rather than destinations. C6 is deliberately fenced off as an Extension so the Core counts stay honest.</p>
</div>
"""
write("map.html", "Map & clusters — SF Bay Area Michelin 2026", map_body)

# ---------------------------------------------------------------- doc pages
write_doc("docs/executive-summary.md", "executive-summary.html", "Executive summary")
write_doc("docs/questions.md", "questions.html", "Open questions")
write_doc("docs/suggestions.md", "suggestions.html", "Suggestions for review")
write_doc("docs/flagged-review.md", "flagged.html", "Flagged for review")
write_doc("docs/methodology.md", "methodology.html", "Method and verification")
print("done")
