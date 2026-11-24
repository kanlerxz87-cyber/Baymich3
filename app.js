(() => {
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const escapeHTML = (value) => String(value ?? '').replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]);
  const distinction = (stars) => `${'★'.repeat(stars)}${'☆'.repeat(3 - stars)} <span>${stars} ${stars === 1 ? 'star' : 'stars'}</span>`;
  const blank = (label = 'Not verified') => `<span class="missing-value"><span class="missing-dot"></span>${label}</span>`;
  const pages = ['overview', 'restaurants', 'clusters', 'hotels', 'decisions', 'review'];

  function setPage(page, updateHistory = false) {
    if (!pages.includes(page)) page = 'overview';
    $$('.page').forEach((section) => section.classList.toggle('active', section.dataset.page === page));
    $$('[data-page-link]').forEach((link) => {
      const active = link.dataset.pageLink === page;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current');
    });
    const crumbs = { overview: 'OVERVIEW', restaurants: 'RESTAURANTS', clusters: 'CLUSTERS & MAP', hotels: 'HOTELS', decisions: 'DECISIONS', review: 'REVIEW QUEUE' };
    $('#current-crumb').textContent = crumbs[page];
    document.title = `${crumbs[page]} | Bay Area Michelin Guide`;
    if (updateHistory) history.pushState({ page }, '', `?page=${page}`);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function initNavigation() {
    document.addEventListener('click', (event) => {
      const link = event.target.closest('[data-page-link], a[href^="?page="]');
      if (!link) return;
      const page = link.dataset.pageLink || new URL(link.href).searchParams.get('page');
      if (!page) return;
      event.preventDefault();
      setPage(page, true);
    });
    window.addEventListener('popstate', () => setPage(new URLSearchParams(location.search).get('page') || 'overview'));
    setPage(new URLSearchParams(location.search).get('page') || 'overview');
  }

  function renderSummary() {
    const counts = restaurants.reduce((result, item) => (result[item.stars] = (result[item.stars] || 0) + 1, result), {});
    const stats = [
      { number: restaurants.length, label: 'Bay Area starred restaurants', sub: '2026 MICHELIN Guide rollup' },
      { number: counts[3] || 0, label: 'Three-star restaurants', sub: 'Exceptional cuisine' },
      { number: counts[2] || 0, label: 'Two-star restaurants', sub: 'Excellent cooking' },
      { number: counts[1] || 0, label: 'One-star restaurants', sub: 'High-quality cooking' }
    ];
    $('#summary-stats').innerHTML = stats.map((item, index) => `<article class="stat-card"><span class="stat-icon stat-icon-${index}">${['✳', '★★★', '★★', '★'][index]}</span><strong>${item.number}</strong><span class="stat-label">${escapeHTML(item.label)}</span><small>${escapeHTML(item.sub)}</small></article>`).join('');
    $('#flag-count').textContent = reviewItems.length;
  }

  function renderRestaurantFilters() {
    const cities = [...new Set(allRestaurantRecords.map((item) => item.city))].sort((a, b) => a.localeCompare(b));
    $('#city-filter').innerHTML = '<option value="all">All Bay Area cities</option>' + cities.map((city) => `<option value="${escapeHTML(city)}">${escapeHTML(city)}</option>`).join('');
    ['#restaurant-search', '#star-filter', '#city-filter'].forEach((selector) => $(selector).addEventListener('input', renderRestaurants));
    renderRestaurants();
  }

  function renderRestaurants() {
    const query = $('#restaurant-search').value.trim().toLocaleLowerCase();
    const star = $('#star-filter').value;
    const city = $('#city-filter').value;
    const filtered = allRestaurantRecords.filter((item) => {
      const matchesDistinction = star === 'all' || (star === 'listed' ? item.stars === 0 : String(item.stars) === star);
      return (!query || `${item.name} ${item.city}`.toLocaleLowerCase().includes(query)) && matchesDistinction && (city === 'all' || item.city === city);
    });
    $('#restaurant-count').textContent = `${filtered.length} of ${allRestaurantRecords.length} entries`;
    $('#restaurant-rows').innerHTML = filtered.map((item) => `<tr>
      <td data-label="Restaurant"><a class="restaurant-name" href="${escapeHTML(item.profile)}" target="_blank" rel="noreferrer">${escapeHTML(item.name)} <span aria-hidden="true">↗</span></a><small class="mobile-subtitle">${escapeHTML(item.city)}</small></td>
      <td data-label="MICHELIN distinction">${item.stars ? `<span class="star-rating" aria-label="${item.stars} Michelin ${item.stars === 1 ? 'star' : 'stars'}">${distinction(item.stars)}</span>` : `<span class="listed-distinction">${escapeHTML(item.distinction)}</span>`}</td>
      <td data-label="City">${escapeHTML(item.city)}</td>
      <td data-label="Total for 2 adults">${item.coupleTotal ? escapeHTML(item.coupleTotal) : blank('Unverified')}</td>
      <td data-label="Days, hours & exceptions">${item.hours ? escapeHTML(item.hours) : blank('Unverified')}</td>
      <td data-label="Venue’s official website">${item.officialWebsite ? `<a class="table-link" href="${escapeHTML(item.officialWebsite)}" target="_blank" rel="noreferrer">Restaurant site ↗</a>` : blank('Unverified')}</td>
      <td data-label="Social">${item.social ? `<a class="table-link" href="${escapeHTML(item.social)}" target="_blank" rel="noreferrer">Official social ↗</a>` : blank('Unverified')}</td>
      <td data-label="Source"><a class="source-chip" href="${escapeHTML(item.source)}" target="_blank" rel="noreferrer">${escapeHTML(item.sourceLabel)} ↗</a></td>
    </tr>`).join('') || '<tr><td colspan="8" class="empty-state">No matching restaurants. Adjust the filters.</td></tr>';
  }

  function renderClusters() {
    const counts = restaurants.reduce((result, item) => (result[item.city] = (result[item.city] || 0) + 1, result), {});
    const areas = Object.entries(counts).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
    $('#cluster-grid').innerHTML = areas.map(([city, count], index) => {
      const mapURL = `https://www.google.com/maps/search/${encodeURIComponent(`Michelin starred restaurants ${city} California`)}`;
      return `<article class="cluster-card"><div class="cluster-top"><span class="cluster-index">${String(index + 1).padStart(2, '0')}</span><span class="cluster-pin">⌖</span></div><h3>${escapeHTML(city)}</h3><p>${count} current starred ${count === 1 ? 'restaurant' : 'restaurants'} in this dataset</p><div class="cluster-bottom"><span>City-level count · stars only</span><a href="${mapURL}" target="_blank" rel="noreferrer" aria-label="Open map search for ${escapeHTML(city)}">Map ↗</a></div></article>`;
    }).join('');
  }

  function renderHotels() {
    $('#hotel-rows').innerHTML = hotels.map((hotel) => `<tr>
      <td data-label="Candidate property"><a class="restaurant-name" href="${escapeHTML(hotel.source)}" target="_blank" rel="noreferrer">${escapeHTML(hotel.name)} ↗</a></td>
      <td data-label="Destination / neighborhood">${escapeHTML(hotel.area)}</td>
      <td data-label="Nearby starred count">${hotel.nearbyCount === null ? blank('Not scored') : escapeHTML(hotel.nearbyCount)}</td>
      <td data-label="Rate for stay">${hotel.rate ? escapeHTML(hotel.rate) : blank('Dates needed')}</td>
      <td data-label="Why included / caveat">${escapeHTML(hotel.note)}</td>
      <td data-label="Official hotel source"><a class="source-chip" href="${escapeHTML(hotel.source)}" target="_blank" rel="noreferrer">MICHELIN hotel ↗</a></td>
    </tr>`).join('');
  }

  function renderDecisions() {
    $('#decision-list').innerHTML = decisions.map((item, index) => `<article class="decision-card"><span class="decision-number">${String(index + 1).padStart(2, '0')}</span><div><h3>${escapeHTML(item.question)}</h3><p>${escapeHTML(item.why)}</p><div class="decision-missing"><strong>Information to discover</strong><span>${escapeHTML(item.missing)}</span></div></div></article>`).join('');
    const saved = new Set(JSON.parse(localStorage.getItem('baymichelinSuggestions') || '[]'));
    $('#suggestion-list').innerHTML = suggestions.map((item) => `<label class="suggestion-card"><input type="checkbox" value="${escapeHTML(item.id)}" ${saved.has(item.id) ? 'checked' : ''}><span class="suggestion-check" aria-hidden="true">✓</span><span class="suggestion-copy"><span class="suggestion-meta">${escapeHTML(item.effort)}</span><strong>${escapeHTML(item.title)}</strong><small>${escapeHTML(item.detail)}</small></span><span class="suggestion-arrow" aria-hidden="true">↗</span></label>`).join('');
    $('#suggestion-list').addEventListener('change', (event) => {
      if (event.target.type !== 'checkbox') return;
      const selected = $$('#suggestion-list input:checked').map((input) => input.value);
      localStorage.setItem('baymichelinSuggestions', JSON.stringify(selected));
      renderSuggestionSummary(selected);
    });
    renderSuggestionSummary([...saved]);
  }

  function renderSuggestionSummary(selected) {
    const chosen = suggestions.filter((item) => selected.includes(item.id));
    $('#selection-summary').innerHTML = chosen.length ? `<strong>${chosen.length} suggestion${chosen.length === 1 ? '' : 's'} saved in this browser:</strong> ${chosen.map((item) => escapeHTML(item.title)).join(' · ')}` : 'No suggestions selected yet.';
  }

  function renderReview() {
    $('#review-count').textContent = `${reviewItems.length} items`;
    $('#review-list').innerHTML = reviewItems.map((item) => `<article class="review-card"><div class="review-level level-${item.severity.toLowerCase()}">${escapeHTML(item.severity)}</div><div class="review-copy"><h3>${escapeHTML(item.title)}</h3><p>${escapeHTML(item.detail)}</p><a href="${escapeHTML(item.source)}" target="_blank" rel="noreferrer">Open official reference ↗</a></div></article>`).join('');
  }

  initNavigation();
  renderSummary();
  renderRestaurantFilters();
  renderClusters();
  renderHotels();
  renderDecisions();
  renderReview();
})();
