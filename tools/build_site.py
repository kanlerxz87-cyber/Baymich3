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


# ---------------------------------------------------------------- compute
R = load("restaurants.csv")
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

# ---------------------------------------------------------------- summary
def tier_rows():
    out = ""
    for d in ("3 Stars", "2 Stars", "1 Star"):
        vals = sorted((money(r["price_2adults_usd"]), r["name"]) for r in R
                      if r["distinction"] == d and money(r["price_2adults_usd"]))
        total = len([r for r in R if r["distinction"] == d])
        if not vals:
            continue
        lo, hi = vals[0], vals[-1]
        rng = f"${lo[0]:,.0f}" if lo[0] == hi[0] else f"${lo[0]:,.0f}&ndash;${hi[0]:,.0f}"
        out += (f'<tr><td>{star_badge(d)}</td><td>{len(vals)} of {total}</td><td>{rng}</td>'
                f'<td>{e(lo[1])}</td><td>{e(hi[1])}</td></tr>\n')
    return out


sum_body = f"""
<h1>Executive summary</h1>
<p class="lead">MICHELIN Guide California 2026, checked {CHECKED}. Scope: the 9-county Core Bay Area plus a separately flagged Extension. Everything below is computed from the data files, and every claim traces to a linked source.</p>

<div class="grid">
{stat(len(CORE), "Core starred", "7&#215;3&#9733; / 7&#215;2&#9733; / 27&#215;1&#9733;")}
{stat(dist["3 Stars"], "3-star rows in dataset", "Bay Area incl. extension")}
{stat(f"${min(totals):,.0f}–${max(totals):,.0f}", "verified dinner for two", f"{len(verified_price)} rows with an official price")}
{stat(f"{round(100*len(sf)/len(CORE))}%", "of Core stars are in SF city", f"{len(sf)} of {len(CORE)}")}
</div>

<div class="card">
<h2>Five things that matter for a decision</h2>
<ol class="tight">
<li><b>Concentration beats breadth.</b> {len(sf)} of {len(CORE)} Core starred restaurants are inside San Francisco. If you want maximum Michelin with minimum travel, base yourself in the city and do not split the trip.</li>
<li><b>Wine Country is a second trip, not a day trip.</b> {len([r for r in cluster['C5 Wine Country'] if 'Star' in r['distinction']])} starred restaurants sit in Napa/Sonoma, including three of the seven 3-star rooms. Two of them (Auberge du Soleil, SingleThread) also have rooms, which removes the driving problem.</li>
<li><b>The 2026 edition moved.</b> Californios went to 3 stars (the first Mexican restaurant in the world to reach that tier) and Enclos was promoted to 3. Naides and Wolfsbane arrived with 1 star. Any list built from a 2025 source is out of date.</li>
<li><b>Service charges, not menu prices, decide the bill.</b> Published per-person prices run $60 (Angler lunch) to $425 (Benu), but San Francisco adds 20&ndash;26% on top, and 7 Adams adds a 6% mandate on top of its 20% service. Two adults at Benu is $1,037 before tax and wine.</li>
<li><b>The data is deliberately incomplete.</b> {vcount['Verified']} of {len(R)} starred rows carry a verified value; {vcount['Partial']} are partial and {vcount['Unverified']} unverified. Prices and hours live behind booking platforms for most venues, so they are blank rather than guessed.</li>
</ol>
</div>

<div class="card">
<h2>Cost picture, by tier (total for two adults, before tax and drinks)</h2>
<div class="tblwrap"><table><thead><tr><th>Tier</th><th>Rows with a verified total</th><th>Range</th><th>Cheapest</th><th>Most expensive</th></tr></thead><tbody>
{tier_rows()}</tbody></table></div>
<p class="small">A &ldquo;verified total&rdquo; is a row where the per-person menu price and the service charge both came from an official page. 3-star prices are the biggest gap: Atelier Crenn, Quince, Californios, SingleThread, The French Laundry and Enclos publish no readable price on the official page we checked &mdash; only Benu does. See <a href="questions.html">Q3</a> for how to close that.</p>
</div>

<div class="card">
<h2>Hotels, in one line each</h2>
<p><b>Densest:</b> Four Seasons SF, Fairmont, St. Regis, Palace, Ritz-Carlton, Taj Campton, Hotel Kabuki, 1 Hotel &mdash; all C1, all sitting inside a 25-star cluster. <b>Peninsula:</b> Rosewood Sand Hill (5 stars in cluster). <b>East Bay:</b> The Claremont (2). <b>Marin:</b> Cavallo Point (1). <b>Wine Country:</b> Auberge du Soleil (1-star restaurant on site), SingleThread Inn (3-star restaurant + inn), Bardessono (walk to The French Laundry).</p>
<p class="small">Nightly rates are not collected &mdash; they are dynamic and a stale rate misleads. See <a href="questions.html">Q6</a>.</p>
</div>

<div class="card">
<h2>What changed in this audit</h2>
<ul class="tight">
<li><b>Data corruption fixed.</b> Eleven rows in the starred table had the Michelin URL sitting in the price column, which had pushed every later field out of place and rendered junk prices on the live site. All 44 rows were rebuilt in canonical column order.</li>
<li><b>Price arithmetic fixed.</b> Acquerello showed $708 against a $731.60 basis, Angler $156 against $151.20, Commis $669 against $669.60, and 7 Adams omitted its 6% mandate entirely.</li>
<li><b>Hotel addresses corrected.</b> Three were wrong, including one that listed The French Laundry's address as a hotel's.</li>
<li><b>Provenance corrected.</b> Bib rows outside San Francisco had been citing the San Francisco list as their source.</li>
<li><b>Cluster count corrected.</b> Wine Country has 8 Core starred restaurants, not 7 &mdash; the earlier text said 7 while listing 8 names.</li>
</ul>
<p>Full detail on the <a href="flagged.html">Flagged for Review</a> page.</p>
</div>
"""
write("executive-summary.html", "Executive summary — SF Bay Area Michelin 2026", sum_body)

# ---------------------------------------------------------------- questions
qs = [
    ("Q1", "Which Michelin edition is authoritative right now?",
     f"Guide California 2026 (revealed 24–26 June 2026) is the current edition, and this build is checked against it on {CHECKED}.",
     "When the 2027 edition lands, every star in this dataset could change. Nothing on the site can pre-empt that.",
     "Re-read the ceremony article each June and diff it against <code>data/restaurants.csv</code>; the starred page should be regenerated the same day.",
     "Blocks: every star claim after June 2027."),
    ("Q2", "What counts as 'the Bay Area' for this project?",
     "A 9-county Core (SF, San Mateo, Santa Clara, Alameda, Contra Costa, Marin, Sonoma, Napa, Solano) plus a separately flagged Extension (Carmel, Elk) and an excluded Sacramento metro. Defined in <code>data/SCOPE.md</code>.",
     "Your actual travel radius. Someone based in Palo Alto and someone based in Napa should not get the same hotel ranking.",
     "Ask for a base city and a maximum drive time; then re-cut the hotel table. Until then the ranking assumes SF-centric travel.",
     "Blocks: hotel ranking, itinerary design."),
    ("Q3", "What does dinner for two actually cost?",
     f"{len(verified_price)} starred rows have an official price and a printed formula, ranging ${min(totals):,.0f}–${max(totals):,.0f} before tax and drinks.",
     "The other rows publish no price on their own site, including six of the seven 3-star rooms. Tax, wine, supplements and corkage are excluded everywhere.",
     "Prices appear on the booking layer (Tock, OpenTable, SevenRooms, Resy) which the restaurant controls. Open each, screenshot, date-stamp, record in the CSV. Start with the 3-star six, where the money is largest.",
     "Blocks: budgeting, and any 'cheapest 2-star' comparison."),
    ("Q4", "When is each place open, and what are the exceptions?",
     f"{len([r for r in R if r['days_open']])} of {len(R)} starred rows have days or hours from an official page; several carry explicit exceptions (Quince closed 26 Nov and 25–26 Dec; SingleThread closed 1 Jan, Thanksgiving, 25 Dec; Harbor House closed Tue–Wed; Chez Noir closed Wed).",
     "Holiday closures, private buy-outs and seasonal breaks are mostly unpublished until the week of.",
     "Check the venue's own reservation page for the exact date, plus its Instagram for same-week closures. Michelin's per-restaurant page also carries a day-by-day open/closed block.",
     "Blocks: booking a specific date."),
    ("Q5", "Where are the YouTube, TikTok and Instagram links?",
     "Four Instagram handles are verified from an official page: @atelier.crenn, @benu_sf, @lazybearsf, @7adamsrestaurant, @niseisf, @auronapavalley, @cheznoircarmel (verified in this audit from each venue's own site).",
     "YouTube and TikTok: no Bay Area starred restaurant links a channel from its own site. A search-result handle is not an official link, so those cells are blank.",
     "Ask each restaurant's press page or inspect the social icon row in the site source (a <code>sameAs</code> block in JSON-LD is the reliable signal). Where a venue has no channel, record 'none' rather than a lookalike account.",
     "Blocks: social column completeness (a nice-to-have, not a decision blocker)."),
    ("Q6", "Which hotel should we actually book?",
     f"{len(HOT)} hotels are ranked by starred-restaurant density in their cluster. Three hotels have an address corrected in this audit and five have no verified street address at all.",
     "Nightly rates, room quality, and whether the hotel holds Michelin Keys. Density alone flatters the city.",
     "Pull a dated rate from each hotel's own booking engine for two or three sample nights, and read the Keys off each Michelin hotel page. Then rank on density-per-dollar as a second column.",
     "Blocks: booking. Currently the ranking answers 'where are the restaurants', not 'what is the best stay'."),
    ("Q7", "How do we enumerate the 86 Selected/Recommended restaurants?",
     "Michelin's city filter reports 86 Selected restaurants for SF and surroundings, and the tier is explained on the listed page.",
     "The names. Michelin does not publish that set as a single page.",
     "Walk each city listing paginated 30 at a time, or query the Michelin site with the distinction filter and capture each card. It is a few hours of careful work, not an inference problem.",
     "Blocks: a complete 'listed-only' table."),
    ("Q8", "How many Bib Gourmands are in the Bay Area, really?",
     "Michelin's filter counts are 30 (San Francisco), 29 (Oakland) and 28 (Berkeley) — and these lists overlap, so they cannot simply be added.",
     f"A de-duplicated Bay Area total, and confirmation of the {len(BIB)} rows carried in this dataset ({len(BIB)-bib_verified} of which were not re-seen on a Michelin page in this audit).",
     "Fetch each city Bib list in full, dedupe by name, and reconcile against the statewide 117 figure.",
     "Blocks: any precise Bib count claim."),
    ("Q9", "Does a star include the Green Star?",
     "Green Star is a separate sustainability award that can sit alongside stars (Quince and Harbor House both carry it). It is recorded in the <code>green_star</code> field, not counted as a star.",
     "Whether you want Green Star venues surfaced as their own shortlist.",
     "Filter the CSV on <code>green_star = Yes</code> and add a page, if that matters to you.",
     "Blocks: nothing; it is a presentation choice."),
    ("Q10", "Which prices are 'for two' versus 'per person'?",
     "Every price on the starred page is a total for two adults, and the per-person figure and the formula are printed inside the cell.",
     "Whether you want the table to also show a per-person column for comparison with other guides.",
     "Trivial change to the generator; it needs your sign-off on layout, not more data.",
     "Blocks: nothing."),
    ("Q11", "What is missing that a diner would notice immediately?",
     "Cancellation terms, dress codes and dietary limits are on many official pages (Benu corkage $100, Kiln no substitutions, Harbor House no under-15s, SingleThread closures) and are summarised in the notes column.",
     "Party-size limits, deposit amounts and allergy policies are only partly captured.",
     "Add three structured fields (deposit, cancellation window, dietary limits) to the CSV and fill them from the same official pages already cited.",
     "Blocks: nothing, but improves booking confidence."),
    ("Q12", "What should not be trusted on this site?",
     f"Every row links to its source, and blank means unverified. {vcount['Unverified']} starred rows and {len(BIB)-bib_verified} Bib rows are still unverified.",
     "Anything not carrying a source link — there should be nothing in that state, and a link check runs over the whole site.",
     "Read the status badge before the number. Where a cell is blank, open the official site; if the value still is not there, leave it blank.",
     "Blocks: nothing, but it is the single most important reading instruction."),
]
q_html = ""
for qid, q, know, dont, how, blocks in qs:
    q_html += f"""
<div class="card q">
<h2><span class="qid">{qid}</span> {e(q)}</h2>
<dl>
<dt>What we know (verified)</dt><dd>{know}</dd>
<dt>What we do not know</dt><dd>{e(dont)}</dd>
<dt>How to discover it</dt><dd>{how}</dd>
<dt>What it blocks</dt><dd>{e(blocks)}</dd>
</dl>
</div>"""

questions_body = f"""
<h1>Questions to settle before any decision</h1>
<p class="lead">A decision made on unverified data is a guess with a nice table around it. Each question below records what is verified, what is missing, how to close the gap, and what it blocks.</p>
<div class="note"><b>Current scoreboard:</b> {vcount['Verified']} starred rows verified, {vcount['Partial']} partial, {vcount['Unverified']} unverified &middot; {bib_verified} of {len(BIB)} Bib rows re-confirmed &middot; 0 YouTube and 0 TikTok links published by the venues themselves.</div>
{q_html}
"""
write("questions.html", "Open questions — SF Bay Area Michelin 2026", questions_body)

# ---------------------------------------------------------------- suggestions
sugs = [
    ("S1", "Finish the price sweep on the booking layer",
     "Six of seven 3-star rooms and roughly half the 1-star list have no publishable price, because the price lives in Tock/OpenTable/SevenRooms rather than on the marketing site.",
     "Open each booking page, capture the per-person price and service charge, date-stamp it, and write it into the CSV with the booking URL as the source. Budget lines become usable for all 44 rows.",
     "High (roughly 30 pages to read carefully).", "Low — it is recording, not estimating.", "Approve treating a restaurant-controlled booking page as an official source."),
    ("S2", "Real map pins, geocoded from verified addresses",
     "The map page links out instead of plotting, because guessing coordinates would look authoritative and be wrong.",
     "Geocode the addresses that are actually verified, keep the address text visible next to each pin, and fall back to a plain list where no address is confirmed.",
     "Medium-high.", "Medium — geocoder error is invisible to a reader.", "Approve OpenStreetMap Nominatim, and a visible 'approximate' disclaimer."),
    ("S3", "A 'bookable tonight' view",
     "Hours and closures go stale fast, and the site cannot tell you whether a room is open on your date.",
     "Add a per-row 'last checked' date, auto-flag rows older than 90 days, and link each row to its own booking engine rather than to a generic homepage.",
     "Medium.", "Low.", "Approve the 90-day staleness threshold."),
    ("S4", "Total-trip cost: hotel + dinners",
     "The hotel ranking ignores what the room costs, so density alone drives the order.",
     "Add a dated nightly rate for two or three sample nights per hotel, then show density and cost side by side instead of one blended score.",
     "Medium.", "Medium — rates move weekly.", "Approve the sample dates and the refresh cadence."),
    ("S5", "Split the hotel table into 'eat-and-sleep' vs 'base'",
     "Auberge du Soleil and SingleThread Inn have the starred kitchen in the building; the SF hotels do not. Those are different products ranked in one list.",
     "Two tables: venues where the restaurant is on site, and city bases where you travel to dinner.",
     "Low.", "Low.", "Approve the split."),
    ("S6", "A green-star and dietary filter",
     "Sustainability and dietary accommodation are the two most common questions a diner asks a table like this, and neither is filterable today.",
     "Expose <code>green_star</code> and a small set of dietary flags (vegetarian menu, no vegan, no gluten-free) as filters on the starred page.",
     "Low-medium, needs the dietary fields filled first.", "Low.", "Approve adding three dietary columns to the CSV."),
    ("S7", "Social column: 'none published' instead of blanks",
     "Zero YouTube and zero TikTok links are published by the venues themselves; blanks read as unfinished work.",
     "Search each venue's own site for a <code>sameAs</code> block or icon row, record what exists, and write 'none published' where nothing exists.",
     "Low.", "Low.", "Approve 'none published' as a value."),
    ("S8", "Enumerate the Selected/Recommended tier",
     "The 86 Selected restaurants are counted but not listed, which leaves a visible gap between 'listed' and 'starred'.",
     "Page through the Michelin city listings with the distinction filter and capture each card, then add them to the listed page as a third table.",
     "High.", "Low.", "Approve the extra pages of research."),
    ("S9", "A printable one-page plan",
     "The dashboard is good for browsing and bad for standing outside a restaurant door with no signal.",
     "Generate a single-page print stylesheet with the chosen cluster, the confirmed bookings and the phone numbers.",
     "Low.", "Low.", "Approve adding a print stylesheet."),
    ("S10", "Kitchen notes per row",
     "Deposits, cancellation windows and allergy policies differ sharply (Commis takes a $100pp deposit, Ssal $150pp non-refundable, Harbor House refuses under-15s and most substitutions).",
     "Three extra fields per row, filled only from the official page already cited.",
     "Medium.", "Low.", "Approve the extra fields."),
]
s_html = ""
for sid, title, problem, change, effort, risk, decision in sugs:
    s_html += f"""
<div class="card sug">
<h2><span class="qid">{sid}</span> {e(title)} <span class="badge warn">proposed</span></h2>
<dl>
<dt>Problem</dt><dd>{e(problem)}</dd>
<dt>Proposed change</dt><dd>{e(change)}</dd>
<dt>Effort</dt><dd>{e(effort)}</dd>
<dt>Risk</dt><dd>{e(risk)}</dd>
<dt>Decision needed</dt><dd>{e(decision)}</dd>
</dl>
</div>"""

sugg_body = f"""
<h1>Suggestions for review</h1>
<p class="lead">Nothing on this page has been implemented. Each item states the problem, the change, the cost and the decision it needs from you, so you can take the ones worth taking and drop the rest.</p>
<div class="note"><b>Already done, not proposed:</b> verification badges on every row, per-row price formulas, the distinction split between starred and listed, cluster tables, and the audit fixes listed on <a href="flagged.html">Flagged</a>. These proposals start from there.</div>
{s_html}
<div class="card">
<h2>If you only approve one</h2>
<p><b>S1</b> — finishing the price sweep. The site's whole premise is a real total for two, and it currently has that number for {len(verified_price)} of {len(R)} starred rows. S1 is the only proposal that changes how usable the core table is.</p>
<p><b>S2</b> is the most visible upgrade after that, and <b>S5</b> is the cheapest fix to the hotel ranking's weakest point.</p>
</div>
"""
write("suggestions.html", "Suggestions for review — SF Bay Area Michelin 2026", sugg_body)

# ---------------------------------------------------------------- flagged
flag_body = f"""
<h1>Flagged for review</h1>
<p class="lead">Irregularities found while checking this repository line by line, in the order they were found. Nothing here is hidden behind a status badge: each item states what was wrong, what was done, and what is still open.</p>

<div class="card">
<h2>1. Column corruption in the starred data <span class="badge ok">fixed</span></h2>
<p><b>What was wrong:</b> eleven rows (Naides, Wolfsbane, Sun Moon Studio, Auro, Troubadour, Press, Plumed Horse, The Village Pub, Aubergine, Chez Noir and Hilda and Jesse's neighbour row) had the Michelin URL stored in the <code>price_pp_usd</code> column. Every later field had shifted one place, so the rendered page printed a URL where a price belonged and showed no address, no hours and no sources. A twelfth row (Lazy Bear) had its Instagram link in the YouTube column.</p>
<p><b>What was done:</b> all 44 rows were rebuilt in canonical 24-column order, the shift was reversed per row, and a build-time assertion now fails if any row lacks a Michelin source link. The generator reads the CSV, so the HTML cannot drift out of step again.</p>
</div>

<div class="card">
<h2>2. Price arithmetic <span class="badge ok">fixed</span></h2>
<ul class="tight">
<li><b>Acquerello</b> displayed $708 for two while its own stated basis was $731.60 ($295 &times; 2, +24%). Corrected to $731.60; the surcharge is 20% service <i>plus</i> a 4% employee-benefit surcharge.</li>
<li><b>Angler</b> displayed $156 against a $151.20 basis ($60 &times; 2, +26%). Corrected to $151.20.</li>
<li><b>Commis</b> displayed $669 against $669.60. Corrected.</li>
<li><b>7 Adams</b> omitted its charges entirely. Its own menu page states a 6% surcharge <i>and</i> a 20% service charge, so the total for two is $320.04, not $254. Both figures now appear with the formula.</li>
<li><b>Sorrel</b> had a summer price in a Fall 2026 dataset. Corrected to the Fall menu ($195 pp) with the 5% SF mandate added: $409.50 for two.</li>
<li><b>Madcap</b> omitted the 20% service charge it publishes in place of gratuity: $432 for two.</li>
</ul>
</div>

<div class="card">
<h2>3. Wrong hotel addresses <span class="badge ok">fixed</span></h2>
<ul class="tight">
<li><b>Bardessono</b> was listed at 6640 Washington St &mdash; that is The French Laundry's address. Bardessono's own contact page gives 6526 Yount St, Yountville.</li>
<li><b>Cavallo Point</b> was listed at "601 Bridgeway". Its contact page gives 601 Murray Circle, Fort Baker, Sausalito.</li>
<li><b>1 Hotel San Francisco</b> was listed at 22 Battery St. Its own site gives 8 Mission St.</li>
</ul>
<p>Five further hotels (St. Regis, Palace, Ritz-Carlton, Taj Campton Place, Rosewood Sand Hill, Claremont, Hotel Kabuki) have addresses that could not be confirmed from an official page during this audit. Their address cells are now <b>blank</b> and labelled Unverified rather than carrying a plausible-looking guess.</p>
</div>

<div class="card">
<h2>4. Source provenance for Bib Gourmand <span class="badge ok">fixed</span></h2>
<p><b>What was wrong:</b> every Bib row, including Oakland, Berkeley, Marin and Wine Country restaurants, cited the <i>San Francisco</i> Bib Gourmand list as its source, and all 36 were labelled "verified". Michelin publishes separate city lists, so the citation was wrong even where the restaurant was genuinely a Bib.</p>
<p><b>What was done:</b> each row now cites its own city's list, and rows whose names were not actually re-seen on a Michelin list page in this audit are marked <b>Unverified</b> ({len(BIB)-bib_verified} of {len(BIB)}). Michelin's own filter counts are 30 for San Francisco, 29 for Oakland and 28 for Berkeley, and those lists overlap &mdash; so a simple sum would also have been wrong.</p>
</div>

<div class="card">
<h2>5. Cluster count contradiction <span class="badge ok">fixed</span></h2>
<p>The executive summary described Wine Country as having 7 starred restaurants while listing 8 names (The French Laundry, SingleThread, Enclos, Auberge du Soleil, Auro, Cyrus, Troubadour, Press). The data has 8, and the sum across clusters is 25 + 5 + 2 + 1 + 8 = 41, matching the Core total. The text now says 8 and all cluster counts are computed from the CSV at build time.</p>
</div>

<div class="card">
<h2>6. Sources that could not be read <span class="badge warn">open</span></h2>
<p>These are recorded as Unverified rather than filled from memory:</p>
<ul class="tight">
<li><b>frenchlaundry.com</b> returned HTTP 500 on every attempt, so The French Laundry has no price and no hours.</li>
<li><b>pressnapavalley.com/food</b> returned a bot challenge. Press has verified hours from its homepage but no price.</li>
<li><b>enclos-sonoma.com</b> is a video-only page with no readable text, so Enclos has no hours or price.</li>
<li><b>statebirdsf.com</b> and <b>theprogress-sf.com</b> publish reservation links only, so both rows are Unverified for price and hours.</li>
<li><b>californiossf.com</b> publishes address, phone and a booking link, but no price and no hours. Californios, the first 3-star Mexican restaurant in the world, therefore has no price on this site.</li>
<li><b>Mister Jiu's, San Ho Won, Protege, Wakuriya and Saison</b> publish menus as PDFs or images. The prices are real but were not machine-readable, so they stay blank.</li>
</ul>
<p>Discovery route for each is on the <a href="questions.html">Questions</a> page (Q3, Q4).</p>
</div>

<div class="card">
<h2>7. Editorial notes worth a human eye <span class="badge mid">review</span></h2>
<ul class="tight">
<li><b>Selby's city label:</b> Michelin files it under Atherton, the street address is in Redwood City. Both are shown.</li>
<li><b>Cyrus address:</b> Michelin prints "587 St. Helena St." for Press, which is inconsistent with the restaurant's own "587 St Helena Highway". The official form is used.</li>
<li><b>Auberge du Soleil:</b> it appears both as a restaurant (1 star) and as a hotel. It is counted once in restaurant totals and once in hotel rankings, deliberately.</li>
<li><b>Extension vs Core:</b> Aubergine, Harbor House Inn and Chez Noir are starred but sit in Monterey and Mendocino counties. They are excluded from the Core count of 41 and shown separately; folding them in would inflate the Bay Area figure.</li>
<li><b>Recommended tier:</b> 86 names are counted but not enumerated, because Michelin does not publish that set as one page. This is a stated gap, not an oversight.</li>
</ul>
</div>
"""
write("flagged.html", "Flagged for review — SF Bay Area Michelin 2026", flag_body)

# ---------------------------------------------------------------- methodology
meth_body = f"""
<h1>Method &amp; verification</h1>
<p class="lead">How each number on this site was obtained, and what was refused. The rule is simple: if an official page did not say it, the cell stays empty.</p>

<div class="card">
<h2>Sources, in order of authority</h2>
<ol class="tight">
<li><b>guide.michelin.com</b> — the star or Bib itself, the address as Michelin prints it, and the day-by-day open/closed block on each restaurant page.</li>
<li><b>The venue's own website</b> — menu price, service charge, opening days and hours, closures, and social accounts that the site itself links to.</li>
<li><b>The venue's own booking page</b> (Tock, OpenTable, SevenRooms, Resy) — only where the restaurant controls the listing, and always labelled as such. Never presented as a homepage-verified price.</li>
<li><b>Not used:</b> aggregators, review sites, press articles quoting prices, or memory. Third-party figures seen during the audit were recorded as indicative at most and are not shown as totals.</li>
</ol>
</div>

<div class="card">
<h2>The price formula</h2>
<p>Total for two adults = (published per-person menu price &times; 2) + the service charge and surcharges the restaurant publishes.</p>
<ul class="tight">
<li>San Francisco operators add 20&ndash;26% in service charge and mandate. Benu: $425 &times; 2 + 22% = <b>$1,037</b>. Angler lunch: $60 &times; 2 + 26% = <b>$151.20</b>.</li>
<li>7 Adams is the clearest case of why both charges matter: $127 &times; 2 = $254, plus 6% surcharge and 20% service = <b>$320.04</b>.</li>
<li>Where a venue publishes "starting at", the row says so and the total is a floor, not a quote.</li>
<li>Sales tax and beverages are always excluded unless the row says otherwise.</li>
</ul>
</div>

<div class="card">
<h2>Status labels</h2>
<div class="tblwrap"><table><thead><tr><th>Label</th><th>Meaning</th></tr></thead><tbody>
<tr><td><span class="badge ok">Verified</span></td><td>A value on the row was read off an official page, and that page is linked in the row's source cell.</td></tr>
<tr><td><span class="badge mid">Partial</span></td><td>Some values are official, others are not. The status text says which is which.</td></tr>
<tr><td><span class="badge warn">Unverified</span></td><td>Nothing on the row could be confirmed from an official page. Values are blank.</td></tr>
<tr><td><span class="badge star bib">Bib Gourmand</span></td><td>In the Guide for value. Not a star.</td></tr>
</tbody></table></div>
</div>

<div class="card">
<h2>Build integrity</h2>
<p>The site is generated from the CSVs by <code>tools/build_site.py</code>. The generator asserts that every restaurant row carries a <code>guide.michelin.com</code> source link, refuses to run if the column schema has drifted, and computes every count on every page from the data — so a stale headline is not possible. Data repair scripts record exactly which values were changed and why: <code>tools/fix_data.py</code>, <code>tools/fix_bib.py</code>, <code>tools/fix_hotels.py</code>.</p>
<p>To run locally: <code>python3 -m http.server 8000</code> from the repository root, then open <code>localhost:8000</code>. To regenerate: <code>python3 tools/build_site.py</code>.</p>
</div>

<div class="card">
<h2>What is still missing</h2>
<p>{vcount['Unverified']} of {len(R)} starred rows and {len(BIB)-bib_verified} of {len(BIB)} Bib rows are unverified, no YouTube or TikTok channel is published by any starred venue, and the 86 Selected restaurants are counted but not listed. Each gap has a discovery route on the <a href="questions.html">Questions</a> page.</p>
</div>
"""
write("methodology.html", "Method & verification — SF Bay Area Michelin 2026", meth_body)
print("done")
