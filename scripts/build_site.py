#!/usr/bin/env python3
"""Build the static GitHub Pages site in docs/ from docs/data/michelin.json.

Standard library only. Run: python3 scripts/build_site.py
"""
import html
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(DOCS, "data", "michelin.json")

with open(DATA, encoding="utf-8") as f:
    D = json.load(f)

SOURCES = D["sources"]


def e(s):
    return html.escape(str(s)) if s not in (None, "") else ""


def src_links(keys):
    out = []
    for k in keys:
        s = SOURCES[k]
        tag = "official" if s["type"] == "official" else "secondary"
        out.append(f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["label"])}</a> <span class="tag {tag}">{tag}</span>')
    return "<br>".join(out)


def cell(v, flag_word="Not verified"):
    """Blank values are shown as flagged, never inferred."""
    if v in (None, ""):
        return f'<span class="unv">{flag_word}</span>'
    return e(v)


def layout(title, active, body, sub=""):
    nav = [
        ("index.html", "Home"),
        ("summary.html", "Executive summary"),
        ("stars.html", "Michelin stars"),
        ("bib.html", "Bib &amp; Recommended"),
        ("hotels.html", "Hotels"),
        ("questions.html", "Questions"),
        ("suggestions.html", "Suggestions"),
        ("flags.html", "Flagged for review"),
    ]
    links = "".join(
        f'<a href="{href}"{" class=on" if href == active else ""}>{label}</a>' for href, label in nav
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | SF Bay Area Michelin Guide</title>
<meta name="description" content="Verified Michelin Guide data for the San Francisco Bay Area, 2026 edition. Every row links to an official source.">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top">
  <div class="brand"><a href="index.html">SF Bay Area Michelin Dashboard</a></div>
  <nav class="nav">{links}</nav>
</header>
<main>
{body}
</main>
<footer>
  <p>Data snapshot: 2026-11-24. Sources are linked on every row. Blank cells are unverified and flagged, never inferred.
  Repository: <a href="https://github.com/kanlerxz87-cyber/Baymich3">kanlerxz87-cyber/Baymich3</a> · Branch <code>arena/8bc23e0f-baymich3</code></p>
</footer>
<script src="assets/filter.js"></script>
</body>
</html>
"""


def table(headers, rows, table_id=None, filter_box=False):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = []
    for r in rows:
        tds = "".join(f'<td data-label="{e(h)}">{c}</td>' for h, c in zip(headers, r))
        trs.append(f"<tr>{tds}</tr>")
    box = ""
    if filter_box:
        box = f'<input class="filter" type="search" placeholder="Filter rows (name, city, status)…" data-target="{table_id}" aria-label="Filter table">'
    return f'{box}<div class="tablewrap"><table id="{table_id}" class="data"><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'


stars = D["stars"]
bib = D["bib"]
lost = D["lost_star_reported"]
rec = D["recommended"]

n3 = [s for s in stars if s["stars"] == 3]
n2 = [s for s in stars if s["stars"] == 2]
n1 = [s for s in stars if s["stars"] == 1]
county_counts = Counter(s["county"] for s in stars)
sf_stars = [s for s in stars if s["county"] == "San Francisco"]
bib_sf = [b for b in bib if b["county"] == "San Francisco"]
bib_official = [b for b in bib if "michelin_bib_list" in b["sources"] or "michelin_bib_article" in b["sources"]]
verified_detail = [s for s in stars if s["michelin_url"]]
new_names = [s["name"] for s in stars if "NEW" in s["status"]]
promoted = [s["name"] for s in stars if "Promoted" in s["status"]]
total_rows = len(stars) + len(bib) + len(rec)
unverified_price = len([s for s in stars if not s["price_2_adults"]])
unverified_social = len([s for s in stars if not s["social"]])

N_FLAGGED = len([1 for s in stars if "FLAG" in s["verified"]]) + len([1 for b in bib if "FLAG" in b["verified"]])
N_QUESTIONS = 11  # keep in sync with questions table below

# ---------------------------------------------------------------- index
index_body = f"""
<section class="hero">
  <h1>San Francisco Bay Area · Michelin Guide 2026</h1>
  <p class="lead">A verified, organized view of Michelin-starred and Bib Gourmand restaurants in the Bay Area, built from official Michelin sources. Every row links to its source. Anything I could not confirm is left blank and flagged.</p>
</section>
<section class="cards">
  <a class="card" href="stars.html"><b>{len(stars)}</b><span>Michelin-starred restaurants</span><small>{len(n3)} three-star · {len(n2)} two-star · {len(n1)} one-star</small></a>
  <a class="card" href="bib.html"><b>{len(bib)}</b><span>Bib Gourmand &amp; Recommended listings</span><small>{len(bib_sf)} in San Francisco</small></a>
  <a class="card" href="summary.html"><b>{len(sf_stars)}</b><span>Starred restaurants in San Francisco</span><small>Largest cluster in the Bay Area</small></a>
  <a class="card warn" href="hotels.html"><b>0</b><span>Hotels ranked</span><small>Not completed. Blocked on verified hotel addresses.</small></a>
  <a class="card warn" href="flags.html"><b>{N_FLAGGED}</b><span>Rows flagged for review</span><small>Secondary-source or conflicting data</small></a>
  <a class="card" href="questions.html"><b>{N_QUESTIONS}</b><span>Questions still open</span><small>What we know vs. what is missing</small></a>
  <a class="card" href="suggestions.html"><b>8</b><span>Suggestions awaiting your choice</span><small>Nothing is changed until you choose</small></a>
</section>
<section>
  <h2>How to use this site</h2>
  <ul class="steps">
    <li><b>Michelin stars</b> lists each starred restaurant, its star level, whether it is new or promoted, and its source.</li>
    <li><b>Bib &amp; Recommended</b> lists the value-focused Bib Gourmand and other Michelin recommendations.</li>
    <li><b>Executive summary</b> has the key takeaways.</li>
    <li><b>Questions</b> lists what must be answered before a decision can be made.</li>
    <li><b>Suggestions</b> lists improvements for you to approve or reject.</li>
    <li><b>Flagged for review</b> lists repo irregularities and conflicting data.</li>
  </ul>
</section>
"""

# ---------------------------------------------------------------- summary
summary_body = f"""
<h1>Executive summary</h1>
<p class="lead">Snapshot as of 2026-11-24. Michelin's 2026 California selection was revealed on June 24, 2026.</p>
<div class="kpis">
  <div><b>{len(stars)}</b> starred restaurants in the Bay Area</div>
  <div><b>{len(n3)}</b> three-star</div>
  <div><b>{len(n2)}</b> two-star</div>
  <div><b>{len(n1)}</b> one-star</div>
  <div><b>{len(sf_stars)}</b> starred in San Francisco</div>
  <div><b>{len(bib)}</b> Bib Gourmand listings</div>
</div>
<h2>Key findings</h2>
<ol class="findings">
  <li><b>San Francisco is the cluster.</b> {len(sf_stars)} of {len(stars)} Bay Area starred restaurants are in San Francisco ({len(sf_stars)*100//len(stars)}%). Other counties: {", ".join(f"{k} {v}" for k, v in county_counts.most_common() if k != "San Francisco")}.</li>
  <li><b>Star changes in 2026.</b> Three-star promotions: {e(", ".join(promoted))}. New one-star entries: {e(", ".join(new_names))}.</li>
  <li><b>Star losses reported (secondary source only):</b> {e(", ".join(l["name"] for l in lost))}. Needs review against Michelin before use.</li>
  <li><b>Hotels are not ranked yet.</b> Ranking hotels by nearby stars needs verified hotel addresses and a distance method. See the Hotels page.</li>
  <li><b>Prices and social links are not yet verified.</b> Michelin pages give only price tiers ($ to $$$$) for the restaurants checked so far, not exact prices for two adults. Exact prices and social links must come from restaurant menus and official accounts.</li>
  <li><b>Detail coverage is partial.</b> Full Michelin detail (address, price tier, hours) was captured for {len(verified_detail)} of {len(stars)} starred restaurants. The rest show only star status (from the official Michelin list).</li>
</ol>
<h2>Scope and method</h2>
<ul>
  <li>Bay Area = nine Bay Area counties. Carmel-by-the-Sea (Monterey County) and Elk (Mendocino County) are excluded.</li>
  <li>Star status comes from Michelin's official 2026 California article. Detail fields come from Michelin restaurant pages where fetched.</li>
  <li>Bib and Recommended rows are from Michelin's official 2026 publication and article. Some Bib rows appear only in a secondary reproduction and are flagged.</li>
</ul>
<h2>What is still missing</h2>
<p>Hours, exact two-adult prices, social links, and hotels remain open. See <a href="questions.html">Questions</a> for what is needed to close each gap, and <a href="suggestions.html">Suggestions</a> for how to get it.</p>
"""

# ---------------------------------------------------------------- stars
star_rows = []
for s in stars:
    name = f'<b>{e(s["name"])}</b>'
    if s["michelin_url"]:
        name += f'<br><a href="{e(s["michelin_url"])}" target="_blank" rel="noopener">Michelin page</a>'
    star_glyph = "★" * s["stars"]
    star_rows.append([
        name,
        e(s["city"]) + (f'<br><small>{e(s["county"])} Co.</small>' if s["county"] and "/" not in s["city"] else ""),
        f'<span class="stars">{star_glyph}</span> {e(s["stars"])}★',
        e(s["status"]),
        cell(s["cuisine"]),
        cell(s["price_tier"]),
        cell(s["address"]),
        cell(s["hours"], "Hours not captured"),
        cell(s["price_2_adults"], "Not verified"),
        cell(s["website"]) if not s["website"] else f'<a href="{e(s["website"])}" target="_blank" rel="noopener">Official site</a>',
        cell(s["social"], "Not found / not verified"),
        src_links(s["sources"]),
        e(s["verified"]),
    ])
stars_headers = ["Restaurant", "City", "Michelin stars", "2026 status", "Cuisine", "Price tier", "Address", "Hours (Michelin page)", "Price for 2 adults", "Website", "Social (YT/TikTok/IG)", "Source(s)", "Verification note"]
stars_body = f"""
<h1>Michelin-starred restaurants · Bay Area 2026</h1>
<p class="lead">{len(stars)} starred restaurants: {len(n3)} three-star, {len(n2)} two-star, {len(n1)} one-star. Sorted by star level. Blank cells are not verified.</p>
<p class="note"><b>Price for 2 adults:</b> left blank. Michelin price tiers are shown only when the Michelin page was captured. An exact total needs a verified menu price from the restaurant.</p>
<p class="note"><b>Social links:</b> none were verified in this pass. Each restaurant's official site and social accounts still need to be searched and confirmed.</p>
{table(stars_headers, star_rows, "stars-table", True)}
<h2>Reported star losses (secondary source, needs review)</h2>
{table(["Restaurant", "City", "Note", "Verification", "Source"], [[e(l["name"]), e(l["city"]), e(l["note"]), e(l["verified"]), src_links(l["sources"])] for l in lost], "lost-table")}
"""

# ---------------------------------------------------------------- bib
bib_rows = []
for b in bib:
    bib_rows.append([
        f'<b>{e(b["name"])}</b>',
        e(b["city"]) + (f'<br><small>{e(b["county"])} Co.</small>' if b["county"] else ""),
        e(b["status"]),
        cell(b["cuisine"]),
        cell(b["address"]),
        cell("", "Not verified"),
        cell("", "Not verified"),
        cell("", "Not found / not verified"),
        src_links(b["sources"]),
        e(b["verified"]),
    ])
for r in rec:
    bib_rows.append([
        f'<b>{e(r["name"])}</b>',
        e(r["city"]) + f'<br><small>{e(r["county"])} Co.</small>',
        e(r["status"]),
        cell(""), cell(""), cell(""), cell(""), cell(""),
        src_links(r["sources"]),
        e(r["verified"]),
    ])
bib_headers = ["Restaurant", "City", "2026 status", "Cuisine", "Address", "Price tier", "Price for 2 adults", "Social (YT/TikTok/IG)", "Source(s)", "Verification note"]
bib_body = f"""
<h1>Bib Gourmand &amp; Recommended · Bay Area 2026</h1>
<p class="lead">{len(bib)} Bib Gourmand listings plus one Recommended restaurant. Bib Gourmands are Michelin's value-focused selections; they are listed, not starred.</p>
<p class="note">Rows marked <span class="tag secondary">secondary</span> or with FLAG appear only in a non-Michelin reproduction and need review before use. Trestle, Z &amp; Y, and the other city-only entries have no street address yet.</p>
{table(bib_headers, bib_rows, "bib-table", True)}
"""

# ---------------------------------------------------------------- hotels
hotels_body = """
<h1>Hotels ranked by nearby Michelin restaurants</h1>
<div class="banner warn"><b>Status: not completed.</b> No hotel was ranked in this pass, because I could not verify hotel addresses from official sources. Ranking hotels from guesses would break the verification rule.</div>
<h2>Method (planned)</h2>
<ol>
  <li>Take the verified starred and Bib addresses from the <a href="stars.html">Michelin stars</a> and <a href="bib.html">Bib</a> tables.</li>
  <li>Take candidate hotel addresses from official hotel sites or Michelin hotel pages (Michelin lists hotels on its own site, e.g. the SingleThread Inn page linked from its restaurant page).</li>
  <li>Count starred and Bib restaurants within a set walking radius (for example 1 km and 3 km), and record the method and distance used.</li>
  <li>Rank hotels by count, then tie-break by distance to the nearest starred restaurant.</li>
</ol>
<h2>Blockers</h2>
<ul>
  <li>Hotel addresses are not yet captured from official pages.</li>
  <li>The radius and tie-break rule need your decision (see <a href="questions.html">Questions</a>).</li>
  <li>Coordinates for each restaurant are not yet captured (Michelin pages show maps, not coordinates in text).</li>
</ul>
"""

# ---------------------------------------------------------------- questions
questions = [
    ["Q1", "Which counties count as the 'Bay Area'?", "Partly answered: this site uses nine Bay Area counties and excludes Carmel and Elk.", "Your confirmation of the boundary.", "Choose the boundary in Suggestions S8."],
    ["Q2", "What is the exact price for two adults at each restaurant?", "Not answered. Michelin gives only price tiers ($$$$).", "Verified menu prices from each restaurant's official site or booking page, with date and tax/tip rules.", "Collect menus from official sites (Suggestions S3)."],
    ["Q3", "What are the current hours and exceptions per restaurant?", "Partly answered for 6 starred restaurants (Michelin pages).", "Hours for the other restaurants, plus holiday and seasonal exceptions.", "Capture official hours (Suggestions S3)."],
    ["Q4", "Which social accounts (YouTube, TikTok, Instagram) are official for each place?", "Not answered. None verified yet.", "Official links from each restaurant's website or Michelin page.", "Search official sites for social links (Suggestions S3)."],
    ["Q5", "Is each star status current?", "Answered as of the June 2026 announcement. Star status can change.", "A re-check date, and the rule for updating after new guide releases.", "Set a re-check schedule (Suggestions S5)."],
    ["Q6", "Which hotels should be ranked, and by which radius?", "Not answered.", "A hotel list with verified addresses, and a radius and tie-break rule.", "Decide the rule (Suggestions S6)."],
    ["Q7", "Should Selby's be listed in Atherton or Redwood City?", "Conflict: Michelin says Atherton; Eater says Redwood City.", "Michelin page for Selby's (not yet fetched).", "Fetch and check the Michelin page (Suggestions S7)."],
    ["Q8", "Are the three reported star losses (Le Comptoir at Bar Crenn, O' by Claude Le Tohic, Shota) confirmed?", "Partly answered: secondary source only.", "Confirmation on Michelin's own site.", "Check Michelin's pages for each (Suggestions S7)."],
    ["Q9", "Which Bib Gourmand rows are confirmed on Michelin's own list?", "Partly answered: 15 addresses confirmed; 8 rows are secondary only; 10 are city-only.", "Michelin's full California Bib list with addresses.", "Pull the full Michelin Bib list (Suggestions S7)."],
    ["Q10", "What is the purpose of the site (booking, planning, or analysis)?", "Not answered.", "Your goal decides which columns matter most.", "Your answer decides what to build next."],
    ["Q11", "How often should data be refreshed?", "Not answered.", "A refresh cadence.", "Pick one (Suggestions S5)."],
]
questions_body = f"""
<h1>Questions to answer before deciding</h1>
<p class="lead">What we know, what we do not know, and how to close each gap. Nothing here is inferred.</p>
{table(["ID", "Question", "Answer so far", "Missing information", "How to get it"], questions, "questions-table", True)}
"""

# ---------------------------------------------------------------- suggestions
suggestions = [
    ["S1", "Add a single master table with every restaurant and hotel, and filters by city, stars, and price.", "Faster decisions; fewer copies of the same data.", "Medium", "Awaiting your choice"],
    ["S2", "Add a map view using the verified addresses (Leaflet with OpenStreetMap tiles).", "Shows clusters visually, as requested in the brief.", "Medium", "Awaiting your choice"],
    ["S3", "Run a second verification pass on each starred restaurant: official site for hours, menu price for 2 adults, and social links.", "Closes the largest data gap (Q2 to Q4).", "High (many pages)", "Awaiting your choice"],
    ["S4", "Add a 'Last verified' date and a source status per row.", "Makes stale data obvious.", "Low", "Awaiting your choice"],
    ["S5", "Set a re-check schedule (for example, each Michelin release and monthly for hours).", "Keeps star and hour data current.", "Low", "Awaiting your choice"],
    ["S6", "Define the hotel-ranking rule (radius, weighting, tie-break) and capture hotel addresses from official sites.", "Enables the hotel ranking that is not done yet.", "Medium", "Awaiting your choice"],
    ["S7", "Resolve the flagged conflicts: Selby's city, the three star losses, and the secondary-only Bib rows.", "Removes the most visible risks before publishing.", "Low", "Awaiting your choice"],
    ["S8", "Confirm the Bay Area boundary (nine counties vs. the broader Michelin 'San Francisco and surroundings' area).", "Changes the total count (for example Carmel, Elk, Healdsburg).", "Low", "Awaiting your choice"],
]
suggestions_body = f"""
<h1>Suggestions · your decision needed</h1>
<p class="lead">Nothing here has been implemented. Reply with the IDs you want (for example "S1, S3, S7"), or with "all", "none", or your own changes.</p>
{table(["ID", "Suggestion", "Benefit", "Effort", "Decision"], suggestions, "suggestions-table")}
"""

# ---------------------------------------------------------------- flags
flags = [
    ["R1", "Repo contains only README.md ('# Baymich3'); no code, license, or CI.", "Information", "https://github.com/kanlerxz87-cyber/Baymich3", "Repo review"],
    ["R2", "COORDINATION.md did not exist; it was created this session with the task board.", "Process", "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/8bc23e0f-baymich3/COORDINATION.md", "Repo review"],
    ["R3", "Branch rule conflict: the coordination spec asks for session-<id>/<task> branches, while this session is locked to arena/8bc23e0f-baymich3. Work logged here instead of on new branches.", "Process", "https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/8bc23e0f-baymich3/COORDINATION.md", "Repo review"],
    ["R4", "Spec text in the brief contains HTML-escaped placeholders ('&amp;amp;lt;id&amp;amp;gt;') in the branch name. Read as session-<id>/<task>.", "Formatting", "", "Repo review"],
    ["R5", "Selby's city conflict: Michelin 'Atherton' vs Eater 'Redwood City'.", "Data conflict", "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/guide-michelin-california", "Stars table"],
    ["R6", "Three star losses (Le Comptoir at Bar Crenn, O' by Claude Le Tohic, Shota) come only from Eater SF / press, not Michelin.", "Unverified", "https://sf.eater.com/restaurant-news/212958/2026-michelin-star-winners-california-guide-san-francisco-bay-area", "Stars table"],
    ["R7", "Michelin's 'most affordable' article says 'seven new' Bibs but lists about 20 cities/restaurants. Count is unclear.", "Source inconsistency", "https://guide.michelin.com/us/en/article/michelin-guide-ceremony/california-s-most-affordable-restaurants-in-2026", "Bib table"],
    ["R8", "Eight Bib rows are only in the OpenTable reproduction, not on Michelin's own pages.", "Unverified", "https://www.opentable.com/blog/michelin-bib-gourmand-california/", "Bib table"],
    ["R9", "The French Laundry Michelin page URL attempt failed; detail not captured.", "Gap", "https://guide.michelin.com/us/en/california/restaurants", "Stars table"],
    ["R10", "Michelin's listing pages show the SF list as '145 restaurants' (all tiers), so the Bay Area count is not the same as the 'San Francisco and surroundings' count.", "Scope", "https://guide.michelin.com/us/en/california/san-francisco/restaurants", "Scope"],
    ["R11", "Michelin's Bay Area restaurant pages were fetched as text; hours and prices were read only where they appeared in the captured text.", "Method", "", "All tables"],
    ["R12", "Hotels not ranked: no verified hotel addresses captured.", "Gap", "https://guide.michelin.com/us/en/hotels", "Hotels"],
]
flags_body = f"""
<h1>Flagged for review</h1>
<p class="lead">Repo irregularities, conflicting sources, and gaps. Each has a link for manual review.</p>
{table(["ID", "Issue", "Type", "Link for review", "Where"], [[r[0], e(r[1]), e(r[2]), (f'<a href="{e(r[3])}" target="_blank" rel="noopener">{e(r[3])}</a>' if r[3] else "-"), e(r[4])] for r in flags], "flags-table", True)}
<h2>Verification log</h2>
<ul>
  <li>Michelin's official 2026 California article: star lists for Bay Area counted per county ({", ".join(f"{k} {v}" for k, v in county_counts.most_common())}).</li>
  <li>Michelin restaurant pages captured for {len(verified_detail)} starred restaurants: {", ".join(e(s["name"]) for s in verified_detail)}.</li>
  <li>Michelin's Bib list (publication excerpt) confirmed {len(bib_official)} Bib rows. The rest are flagged.</li>
  <li>Total rows in the dataset: {total_rows}. Unverified exact prices: {unverified_price} of {len(stars)} starred rows. Unverified social links: {unverified_social} of {len(stars)}.</li>
</ul>
"""

pages = {
    "index.html": ("Home", "index.html", index_body),
    "summary.html": ("Executive summary", "summary.html", summary_body),
    "stars.html": ("Michelin stars", "stars.html", stars_body),
    "bib.html": ("Bib & Recommended", "bib.html", bib_body),
    "hotels.html": ("Hotels", "hotels.html", hotels_body),
    "questions.html": ("Questions", "questions.html", questions_body),
    "suggestions.html": ("Suggestions", "suggestions.html", suggestions_body),
    "flags.html": ("Flagged for review", "flags.html", flags_body),
}

for fname, (title, active, body) in pages.items():
    with open(os.path.join(DOCS, fname), "w", encoding="utf-8") as f:
        f.write(layout(title, active, body))

print("built", len(pages), "pages;", len(stars), "stars;", len(bib), "bib;", "county counts:", dict(county_counts))
