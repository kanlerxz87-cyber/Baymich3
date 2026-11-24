/* Shared renderer. All facts come from docs/data/data.js (official sources only). */
(function () {
  var S = window.SITE;
  var PAGES = [
    ["index.html", "Dashboard"],
    ["restaurants.html", "Restaurants"],
    ["bib-gourmand.html", "Bib Gourmand"],
    ["hotels.html", "Hotels"],
    ["summary.html", "Executive summary"],
    ["questions.html", "Questions"],
    ["suggestions.html", "Suggestions"],
    ["verification.html", "Verification"],
    ["flagged.html", "Flagged"]
  ];

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c];
    });
  }
  function unv(text) { return text ? esc(text) : '<span class="unv">Unverified</span>'; }
  function link(url, label) { return url ? '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(label) + "</a>" : '<span class="unv">Unverified</span>'; }

  function nav() {
    var here = (location.pathname.split("/").pop() || "index.html");
    var html = '<header class="top"><div class="row"><a class="brand" href="index.html">SF Bay Area MICHELIN Dashboard</a><nav class="menu">';
    PAGES.forEach(function (p) {
      html += '<a href="' + p[0] + '"' + (p[0] === here ? ' class="on"' : "") + ">" + p[1] + "</a>";
    });
    html += "</nav></div></header>";
    var slot = document.getElementById("nav");
    if (slot) slot.outerHTML = html;
  }

  function statusTag(st) {
    var cls = {"3 Stars": "t3", "2 Stars": "t2", "1 Star": "t1", "Bib Gourmand": "tbib", "Selected": "tsel"}[st] || "tsel";
    var label = st === "Selected" ? "Listed (Selected, no star or Bib)" : st;
    return '<span class="tag ' + cls + '">' + esc(label) + "</span>";
  }

  function searchLinks(name) {
    var q = encodeURIComponent(name + " San Francisco restaurant");
    return '<div class="links"><a href="https://www.youtube.com/results?search_query=' + q + '" target="_blank" rel="noopener">YouTube search</a>' +
      '<a href="https://www.tiktok.com/search?q=' + q + '" target="_blank" rel="noopener">TikTok search</a>' +
      '<span class="small">Search helper, not verified</span></div>';
  }

  /* ---------- Restaurants ---------- */
  var filter = "all";
  function renderRestaurants() {
    var box = document.getElementById("rest-body");
    if (!box) return;
    var q = (document.getElementById("rest-q").value || "").toLowerCase();
    var rows = S.restaurants.filter(function (r) {
      var okF = filter === "all" ||
        (filter === "stars" && /Stars?$/.test(r.status)) ||
        (filter === "bib" && r.status === "Bib Gourmand") ||
        (filter === "sel" && r.status === "Selected");
      var okQ = !q || (r.name + " " + r.cuisine + " " + r.status).toLowerCase().indexOf(q) > -1;
      return okF && okQ;
    });
    document.getElementById("rest-count").textContent = rows.length + " of " + S.restaurants.length + " rows shown";
    box.innerHTML = rows.map(function (r) {
      var hours = r.detail_checked ? esc(r.hours) + (r.exceptions ? '<div class="small">' + esc(r.exceptions) + "</div>" : "") : '<span class="unv">Hours not verified</span>';
      var days = r.detail_checked ? esc(r.days_closed ? "Closed: " + r.days_closed : "") : '<span class="unv">Not verified</span>';
      var addr = r.address ? esc(r.address) : '<span class="unv">Unverified</span>';
      var web = r.website ? link(r.website, "Website") : '<span class="unv">Unverified</span>';
      var michelin = r.michelin ? link(r.michelin, "Michelin page") : '<span class="unv">No official page captured</span>';
      var ver = r.detail_checked
        ? '<span class="tag vok">Detail page checked</span>'
        : '<span class="tag vpart">Listing only</span>';
      var news = r.new2026 ? '<div class="small">' + esc(r.new2026) + "</div>" : "";
      var srcLabel = r.src === "release_2026" ? "Official 2026 press release" : (r.src === "listing_p2" ? "Official listing p.2" : "Official listing p.1");
      return "<tr>" +
        '<td class="num" data-label="#">' + r.n + "</td>" +
        '<td class="title" data-label="Restaurant">' + esc(r.name) + news + "</td>" +
        '<td data-label="Michelin status">' + statusTag(r.status) + "</td>" +
        '<td data-label="Cuisine">' + esc(r.cuisine) + "</td>" +
        '<td data-label="Price tier (official)">' + (r.price ? esc(r.price) + '<div class="small">Michelin tier, not a 2-adult total</div>' : '<span class="unv">Unverified</span>') + "</td>" +
        '<td data-label="2-adult total price">' + '<span class="unv">Unverified (not published on official pages checked)</span>' + "</td>" +
        '<td data-label="Address">' + addr + "</td>" +
        '<td data-label="Hours">' + hours + "</td>" +
        '<td data-label="Days closed">' + days + "</td>" +
        '<td data-label="Links">' + michelin + " · " + web + "</td>" +
        '<td data-label="Social (YouTube / TikTok)">' + searchLinks(r.name) + "</td>" +
        '<td data-label="Verification">' + ver + '<div class="small">' + esc(srcLabel) + "</div></td>" +
        "</tr>";
    }).join("");
  }

  function wireRestaurants() {
    var q = document.getElementById("rest-q");
    if (!q) return;
    q.addEventListener("input", renderRestaurants);
    document.querySelectorAll("[data-filter]").forEach(function (b) {
      b.addEventListener("click", function () {
        filter = b.getAttribute("data-filter");
        document.querySelectorAll("[data-filter]").forEach(function (x) { x.classList.toggle("on", x === b); });
        renderRestaurants();
      });
    });
    renderRestaurants();
  }

  /* ---------- Bib ---------- */
  function renderBib() {
    var box = document.getElementById("bib-body");
    if (!box) return;
    var city = (document.getElementById("bib-city") || {}).value || "";
    var rows = S.bib.filter(function (b) { return !city || b.county === city; });
    document.getElementById("bib-count").textContent = rows.length + " of " + S.bib.length + " Bay Area Bib Gourmands shown";
    box.innerHTML = rows.map(function (b, i) {
      return "<tr>" +
        '<td class="num" data-label="#">' + (i + 1) + "</td>" +
        '<td class="title" data-label="Restaurant">' + esc(b.name) + "</td>" +
        '<td data-label="City">' + esc(b.city) + "</td>" +
        '<td data-label="County">' + esc(b.county) + "</td>" +
        '<td data-label="Address (official)">' + esc(b.address) + "</td>" +
        '<td data-label="Source">' + link(S.sources.release_2026.url, "Official 2026 release") + '</td>' +
        '<td data-label="Social">' + searchLinks(b.name.replace(" (new)", "")) + "</td>" +
        "</tr>";
    }).join("");
  }
  function wireBib() {
    var sel = document.getElementById("bib-city");
    if (!sel) return;
    sel.addEventListener("change", renderBib);
    renderBib();
  }

  /* ---------- Hotels ---------- */
  function renderHotels() {
    var box = document.getElementById("hotel-body");
    if (!box) return;
    var rank = S.hotels.slice().sort(function (a, b) {
      var ka = a.keys.indexOf("Two") > -1 ? 2 : a.keys ? 1 : 0;
      var kb = b.keys.indexOf("Two") > -1 ? 2 : b.keys ? 1 : 0;
      if (ka !== kb) return kb - ka;
      return (parseFloat(b.guest_score) || 0) - (parseFloat(a.guest_score) || 0);
    });
    box.innerHTML = rank.map(function (h, i) {
      return "<tr>" +
        '<td class="num" data-label="Rank (keys, then guest score)">' + (i + 1) + "</td>" +
        '<td class="title" data-label="Hotel">' + esc(h.name) + (h.note ? '<div class="small">' + esc(h.note) + "</div>" : "") + "</td>" +
        '<td data-label="MICHELIN Keys">' + (h.keys ? '<span class="tag t2">' + esc(h.keys) + "</span>" : '<span class="small">No key icon on index</span>') + "</td>" +
        '<td data-label="Guest score (official)">' + (h.guest_score ? esc(h.guest_score) : '<span class="unv">Not shown</span>') + "</td>" +
        '<td data-label="Restaurants nearby">' + '<span class="unv">Not computed (no verified coordinates)</span>' + "</td>" +
        '<td data-label="Link">' + link(h.url, "Michelin hotel page") + "</td>" +
        "</tr>";
    }).join("");
  }

  /* ---------- Dashboard counts ---------- */
  function fillCounts() {
    var set = function (id, v) { var el = document.getElementById(id); if (el) el.textContent = v; };
    var stars = S.restaurants.filter(function (r) { return /Stars?$/.test(r.status); }).length;
    var bibs = S.restaurants.filter(function (r) { return r.status === "Bib Gourmand"; }).length;
    var sel = S.restaurants.filter(function (r) { return r.status === "Selected"; }).length;
    var det = S.restaurants.filter(function (r) { return r.detail_checked; }).length;
    set("k-rest", S.restaurants.length);
    set("k-total", S.listing_facets.total);
    set("k-stars", stars);
    set("k-bib", S.bib.length);
    set("k-sel", sel);
    set("k-det", det);
    set("k-hotels", S.hotels.length);
    set("k-hotels-total", 31);
    set("k-bibs-sf", bibs);
    set("k-stars-sf", stars);
  }

  document.addEventListener("DOMContentLoaded", function () {
    nav();
    fillCounts();
    wireRestaurants();
    wireBib();
    renderHotels();
  });
})();
