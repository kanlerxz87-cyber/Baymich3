/* Baymich3 site renderer — static, no build step. Data lives in docs/data/*.js */
(function () {
  var D = window.BAYMICH, C = window.BAYMICH_CONTENT;
  var PAGES = [
    { id: "home", href: "index.html", label: "Home" },
    { id: "starred", href: "starred.html", label: "Michelin starred" },
    { id: "bib", href: "bib.html", label: "Bib Gourmand" },
    { id: "hotels", href: "hotels.html", label: "Hotels" },
    { id: "activities", href: "activities.html", label: "Activities" },
    { id: "questions", href: "questions.html", label: "Questions" },
    { id: "suggestions", href: "suggestions.html", label: "Suggestions" },
    { id: "flagged", href: "flagged.html", label: "Flagged" },
    { id: "sources", href: "sources.html", label: "Sources" }
  ];

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function link(url, text) {
    if (!url) return '<span class="blank">Unverified</span>';
    return '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(text || url) + "</a>";
  }
  function or(v, cls) {
    if (v == null || v === "") return '<span class="blank">Unverified</span>';
    return esc(v);
  }
  function verifiedBadge(v) {
    if (v === "Full") return '<span class="ok">Full</span>';
    if (v === "Partial") return '<span class="warn">Partial</span>';
    return '<span class="pend">Pending</span>';
  }
  function tierTag(t) {
    var cls = t === "3★" ? "t3" : t === "2★" ? "t2" : "t1";
    return '<span class="tag ' + cls + '">' + esc(t) + "</span>";
  }

  function nav(current) {
    return '<header class="top"><div class="row"><div class="brand">Baymich3 · Bay Area Michelin</div><nav>' +
      PAGES.map(function (p) {
        return '<a href="' + p.href + '"' + (p.id === current ? ' class="on"' : "") + ">" + esc(p.label) + "</a>";
      }).join("") +
      "</nav></div></header>";
  }
  function footer() {
    return '<footer>Updated ' + esc(D.meta.updated) + ' · Every row links to an official source. Blank = unverified. ' +
      'Repo: <a href="https://github.com/kanlerxz87-cyber/Baymich3" target="_blank" rel="noopener">kanlerxz87-cyber/Baymich3</a></footer>';
  }

  /* ---------- pages ---------- */
  function renderHome() {
    var s = D.starred;
    var c3 = s.filter(function (r) { return r.tier === "3★"; }).length;
    var c2 = s.filter(function (r) { return r.tier === "2★"; }).length;
    var c1 = s.filter(function (r) { return r.tier === "1★"; }).length;
    var full = s.filter(function (r) { return r.verified !== "Pending"; }).length;
    return '<h1>Bay Area Michelin — dashboard</h1>' +
      '<p class="lead">Starred restaurants, hotels and activities for the San Francisco Bay Area. Every value comes from an official source; anything unconfirmed is shown as <b>Unverified</b>.</p>' +
      '<div class="grid">' +
      '<div class="stat"><div class="n">' + s.length + '</div><div class="l">Starred restaurants (2026)</div></div>' +
      '<div class="stat"><div class="n">' + c3 + '</div><div class="l">3★</div></div>' +
      '<div class="stat"><div class="n">' + c2 + '</div><div class="l">2★</div></div>' +
      '<div class="stat"><div class="n">' + c1 + '</div><div class="l">1★</div></div>' +
      '<div class="stat"><div class="n">' + full + '</div><div class="l">Rows with detail verified (Full/Partial)</div></div>' +
      '</div>' +
      '<h2>Executive summary</h2>' +
      '<div class="card">' + C.executive_summary.map(function (e) {
        return '<p><b>' + esc(e.k) + ':</b> ' + esc(e.v) + ' ' + (e.src ? '<span class="src">[' + link(e.src, "source") + "]</span>" : "") + "</p>";
      }).join("") + "</div>" +
      '<h2>Browse</h2><div class="grid tiles">' +
      '<a href="starred.html"><b>Michelin starred</b><span>41 Bay Area starred restaurants, filterable table.</span></a>' +
      '<a href="bib.html"><b>Bib Gourmand</b><span>Not yet gathered (open task T3).</span></a>' +
      '<a href="hotels.html"><b>Hotels</b><span>Ranking not yet built (open task T4).</span></a>' +
      '<a href="activities.html"><b>Activities</b><span>Not yet gathered.</span></a>' +
      '<a href="questions.html"><b>Questions &amp; answers</b><span>What is answered, what is missing, and how to find it.</span></a>' +
      '<a href="suggestions.html"><b>Suggestions</b><span>Choose a path before anything changes.</span></a>' +
      '<a href="flagged.html"><b>Flagged for review</b><span>Unverified items and repo irregularities.</span></a>' +
      '<a href="sources.html"><b>Sources</b><span>Official pages used, with links.</span></a>' +
      "</div>" +
      '<h2>How to read the tables</h2><div class="card"><ul class="clean">' +
      '<li><b>Full</b> = address, price level, hours and website confirmed on the official Michelin page.</li>' +
      '<li><b>Partial</b> = some fields confirmed, some missing or cut off.</li>' +
      '<li><b>Pending</b> = only name, city, star and Michelin link confirmed.</li>' +
      '<li><b>Couple total (2 adults)</b>: Michelin gives $ levels only, so no dollar figure is entered.</li></ul></div>';
  }

  function renderStarred() {
    var rows = D.starred;
    var html = '<h1>Michelin starred restaurants — Bay Area</h1>' +
      '<p class="lead">Star status from the official 2026 California Michelin selection (24 June 2026). Detail fields are verified per row; blanks are unverified.</p>' +
      '<div class="toolbar"><input id="q" type="search" placeholder="Search name, city, cuisine…" aria-label="Search">' +
      '<select id="tier" aria-label="Filter by tier"><option value="">All tiers</option><option>3★</option><option>2★</option><option>1★</option></select>' +
      '<select id="ver" aria-label="Filter by verification"><option value="">All verification</option><option>Full</option><option>Partial</option><option>Pending</option></select>' +
      '<span class="src" id="count"></span></div>' +
      '<div class="table-wrap"><table id="t"><thead><tr>' +
      '<th>Tier</th><th>Restaurant</th><th>City</th><th>Michelin status 2026</th><th>Cuisine</th><th>Price level</th><th>Couple total (2 adults)</th><th>Address</th><th>Days &amp; hours (exceptions)</th><th>Website</th><th>Michelin page (source)</th><th>YouTube / TikTok / Instagram</th><th>Verified</th>' +
      '</tr></thead><tbody id="tb"></tbody></table></div>' +
      '<h2>Lost stars (SF, 2026)</h2><div class="card"><p class="src">Reported by Eater (secondary). Michelin listing status not yet confirmed.</p><ul class="clean">' +
      D.lost_stars_sf_2026.map(function (r) {
        return "<li><b>" + esc(r.name) + "</b> — " + esc(r.note) + ' <span class="src">[' + link(r.source, "Eater source") + "]</span></li>";
      }).join("") + "</ul></div>";
    setTimeout(bind, 0);
    return html;

    function bind() {
      var tb = document.getElementById("tb"), q = document.getElementById("q"),
        tier = document.getElementById("tier"), ver = document.getElementById("ver"), count = document.getElementById("count");
      function draw() {
        var term = (q.value || "").toLowerCase(), t = tier.value, v = ver.value, n = 0;
        var out = rows.filter(function (r) {
          var hay = [r.name, r.city, r.cuisine, r.area].join(" ").toLowerCase();
          return (!term || hay.indexOf(term) > -1) && (!t || r.tier === t) && (!v || r.verified === v);
        }).map(function (r) {
          n++;
          return "<tr>" +
            "<td>" + tierTag(r.tier) + "</td>" +
            "<td><b>" + esc(r.name) + "</b></td>" +
            "<td>" + esc(r.city) + "</td>" +
            "<td>" + esc(r.status) + "</td>" +
            "<td>" + or(r.cuisine) + "</td>" +
            '<td class="num">' + or(r.price) + "</td>" +
            '<td class="num"><span class="blank">Unverified</span></td>' +
            "<td>" + or(r.address) + "</td>" +
            "<td>" + or(r.hours) + "</td>" +
            "<td>" + link(r.website, "Website") + "</td>" +
            "<td>" + link(r.michelin, "Michelin") + "</td>" +
            '<td><span class="blank">Unverified</span></td>' +
            "<td>" + verifiedBadge(r.verified) + "</td>" +
            "</tr>";
        });
        tb.innerHTML = out.join("");
        count.textContent = n + " of " + rows.length + " shown";
      }
      [q, tier, ver].forEach(function (el) { el.addEventListener("input", draw); el.addEventListener("change", draw); });
      draw();
    }
  }

  function renderPlaceholder(title, text, task) {
    return "<h1>" + esc(title) + "</h1><p class=\"lead\">" + esc(text) + "</p>" +
      '<div class="card"><p><b>Status:</b> not yet gathered. Nothing is filled in until it can be checked against an official source.</p>' +
      '<p><b>Open task:</b> ' + esc(task) + ' — see <a href="https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/d7b7bed1-baymich3/COORDINATION.md" target="_blank" rel="noopener">COORDINATION.md</a>.</p></div>';
  }

  function renderQuestions() {
    return "<h1>Questions, answers and gaps</h1>" +
      '<p class="lead">What is known, what is missing, and what is needed before a decision can be made.</p>' +
      C.questions.map(function (x) {
        return '<details class="qa" open><summary>' + esc(x.q) + ' <span class="tag">' + esc(x.status) + "</span></summary>" +
          "<p>" + esc(x.a) + "</p>" +
          (x.src ? '<p class="src">Source: ' + link(x.src) + "</p>" : "") +
          (x.decision ? '<span class="decide">Needs your decision — see Suggestions</span>' : "") + "</details>";
      }).join("") +
      '<h2>Information needed to discover missing data</h2><div class="card"><ol class="clean">' +
      "<li>Visit each one-star restaurant's official Michelin page (link in the table) to complete address, cuisine, price, hours and website.</li>" +
      "<li>Check each restaurant's own website or booking page for a published tasting-menu price (exact dollar total for 2 adults).</li>" +
      "<li>Pull the official Michelin Bib Gourmand and Recommended lists for the Bay Area.</li>" +
      "<li>Pull each hotel's official Michelin page to get a list of nearby starred restaurants (ranking method to be chosen).</li>" +
      "<li>Find each restaurant's own YouTube, TikTok or Instagram account from its official website.</li>" +
      "</ol></div>";
  }

  function renderSuggestions() {
    return "<h1>Suggestions</h1>" +
      '<p class="lead">Nothing here is changed until you choose. Pick a number (for example, "do S1 and S4") and the work is done in the next session.</p>' +
      C.suggestions.map(function (s) {
        return '<details class="sugg" open><summary>' + esc(s.id) + " · " + esc(s.title) + "</summary>" +
          "<p>" + esc(s.detail) + "</p><p class=\"src\">Benefit: " + esc(s.benefit) + "</p>" +
          '<span class="decide">Awaiting your choice</span></details>';
      }).join("") + "";
  }

  function renderFlagged() {
    return "<h1>Flagged for review</h1>" +
      '<p class="lead">Items that could not be fully verified, or that look irregular. Each needs a human check before it is treated as final.</p>' +
      '<div class="table-wrap"><table><thead><tr><th>ID</th><th>Type</th><th>Item</th><th>Status</th><th>Source</th></tr></thead><tbody>' +
      C.flags.map(function (f) {
        return "<tr><td>" + esc(f.id) + "</td><td>" + esc(f.type) + "</td><td>" + esc(f.item) + '</td><td><span class="warn">' + esc(f.status) + "</span></td><td>" + link(f.src, "Source") + "</td></tr>";
      }).join("") + "</tbody></table></div>" +
      '<h2>Repo review</h2><div class="card"><ul class="clean">' +
      '<li>Git state clean, one commit on <code>main</code>.</li>' +
      '<li>README.md has only a title. <span class="warn">Flagged</span>.</li>' +
      '<li>No LICENSE file. <span class="warn">Flagged</span>.</li>' +
      '<li>No build or CI config. The site is static HTML, so no build step is needed.</li>' +
      '<li>Full review notes are in <a href="https://github.com/kanlerxz87-cyber/Baymich3/blob/arena/d7b7bed1-baymich3/COORDINATION.md" target="_blank" rel="noopener">COORDINATION.md</a>.</li>' +
      "</ul></div>";
  }

  function renderSources() {
    var s = D.sources;
    var rows = Object.keys(s).map(function (k) {
      return "<tr><td>" + esc(s[k].label) + "</td><td>" + link(s[k].url) + "</td></tr>";
    });
    return "<h1>Sources</h1><p class=\"lead\">Official sources first. Secondary press is used only to cross-check and is labelled as such.</p>" +
      '<div class="table-wrap"><table><thead><tr><th>Source</th><th>Link</th></tr></thead><tbody>' + rows.join("") + "</tbody></table></div>" +
      '<h2>Verification performed</h2><div class="card"><ul class="clean">' +
      "<li>Star list read from the official Michelin 2026 California article (24 June 2026), page chunks 0–2.</li>" +
      "<li>Restaurant details read from the official Michelin restaurant pages for 14 starred Bay Area restaurants.</li>" +
      "<li>Reported lost stars cross-checked against Eater SF (secondary).</li>" +
      "<li>Not yet done: restaurant websites for prices, Bib Gourmand list, hotels, social links.</li></ul></div>";
  }

  var BODY = {
    home: renderHome,
    starred: renderStarred,
    bib: function () { return renderPlaceholder("Bib Gourmand", "Michelin Bib Gourmand picks for the Bay Area.", "T3 (Bib Gourmand & Recommended list)"); },
    hotels: function () { return renderPlaceholder("Hotels", "Hotels ranked by the number of Michelin restaurants nearby.", "T4 (hotel ranking; needs the ranking method chosen)"); },
    activities: function () { return renderPlaceholder("Activities", "Activities and experiences in the Bay Area with verified hours and social links.", "T6 (activities list and social links)"); },
    questions: renderQuestions,
    suggestions: renderSuggestions,
    flagged: renderFlagged,
    sources: renderSources
  };

  var page = document.getElementById("app");
  var id = page.getAttribute("data-page") || "home";
  var title = (PAGES.filter(function (p) { return p.id === id; })[0] || {}).label || "Home";
  document.title = title + " · Baymich3";
  page.innerHTML = nav(id) + '<main>' + (BODY[id] ? BODY[id]() : "<p>Page not found.</p>") + "</main>" + footer();
})();
