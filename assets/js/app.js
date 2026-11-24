// Baymich3 — Site rendering logic

function formatPriceEstimate(est) {
  if (!est) return '<span class="blank">unverified</span>';
  return est;
}

function renderSocialLinks(social) {
  const platforms = [
    { key: 'youtube', label: 'YT', icon: '▶' },
    { key: 'tiktok',  label: 'TT', icon: '♪' },
    { key: 'instagram', label: 'IG', icon: '◉' }
  ];
  let html = '<div class="social-links">';
  platforms.forEach(p => {
    const url = social[p.key];
    if (url) {
      html += `<a href="${url}" target="_blank" rel="noopener" title="${p.label}">${p.icon}</a>`;
    } else {
      html += `<span class="missing" title="${p.label} not found">${p.icon}</span>`;
    }
  });
  html += '</div>';
  return html;
}

function renderHours(hours, exceptions) {
  if (!hours || Object.keys(hours).length === 0) {
    return '<span class="blank">unverified</span>';
  }
  const days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];
  let html = '<table class="hours-table">';
  days.forEach(d => {
    const val = hours[d];
    const cls = (val === 'closed' || !val) ? 'closed' : '';
    const disp = val ? val : 'closed';
    html += `<tr><td>${d}</td><td class="${cls}">${disp}</td></tr>`;
  });
  html += '</table>';
  if (exceptions) html += `<div style="font-size:0.75rem;color:#666;margin-top:0.25rem;">${exceptions}</div>`;
  return html;
}

function renderStarBadge(stars) {
  if (stars >= 3) return '<span class="star-badge star3">★★★</span>';
  if (stars === 2) return '<span class="star-badge star2">★★</span>';
  if (stars === 1) return '<span class="star-badge star1">★</span>';
  if (stars === 0) return '<span class="star-badge bib">Bib</span>';
  return '<span class="star-badge selected">Listed</span>';
}

function renderRestaurantRow(r) {
  const phone = r.phone ? `<a href="tel:${r.phone}">${r.phone}</a>` : '<span class="blank">unverified</span>';
  const website = r.website ? `<a href="${r.website}" target="_blank" rel="noopener">Visit site</a>` : '<span class="blank">unverified</span>';
  const price = r.price || '<span class="blank">unverified</span>';
  const priceEst = formatPriceEstimate(r.priceEstimate2Adults);
  const social = renderSocialLinks(r.social || {});
  const hours = renderHours(r.hours, r.exceptions);
  const source = `<a href="${r.michelinUrl}" target="_blank" rel="noopener" class="source-link">Michelin official page</a>`;
  const notes = r.notes ? `<div style="font-size:0.75rem;color:#666;margin-top:0.25rem;">${r.notes}</div>` : '';

  let statusText = r.status === 'starred' ? 'Michelin Star' : 'Listed (no star)';
  if (r.notes && r.notes.includes('temporarily')) statusText += ' — temp. closed?';
  if (r.notes && r.notes.includes('closed')) statusText += ' — closed';

  return `
    <tr>
      <td>
        <div style="font-weight:600;">${renderStarBadge(r.stars)} ${r.name}</div>
        <div style="font-size:0.8rem;color:#666;">${r.city}, ${r.status === 'starred' ? statusText : 'Michelin Guide listed'}</div>
        ${notes}
      </td>
      <td>${r.address || '<span class="blank">unverified</span>'}</td>
      <td>${r.cuisine || '<span class="blank">unverified</span>'}</td>
      <td>${price}</td>
      <td>${priceEst}</td>
      <td>${phone}</td>
      <td>${website}</td>
      <td>${social}</td>
      <td>${hours}</td>
      <td>${source}</td>
    </tr>
  `;
}

function renderTable(containerId, restaurants, title) {
  const container = document.getElementById(containerId);
  if (!container) return;
  if (title) {
    const h2 = document.createElement('h2');
    h2.textContent = title;
    container.parentElement.insertBefore(h2, container);
  }
  let rows = '';
  restaurants.forEach(r => { rows += renderRestaurantRow(r); });
  container.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Restaurant</th>
          <th>Address</th>
          <th>Cuisine</th>
          <th>Michelin Price</th>
          <th>Est. 2 Adults</th>
          <th>Phone</th>
          <th>Website</th>
          <th>Social (YT/TT/IG)</th>
          <th>Days / Hours</th>
          <th>Official Source</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
    <div style="font-size:0.8rem;color:#666;margin-top:0.5rem;">
      ${restaurants.length} restaurant${restaurants.length !== 1 ? 's' : ''}
    </div>
  `;
}

// Star counts for dashboard
function renderDashboard() {
  const el = document.getElementById('dashboard-counts');
  if (!el) return;
  const by3 = getByStars(3).length;
  const by2 = getByStars(2).length;
  const by1 = getByStars(1).length;
  const listed = getListed().length;
  const total = getAll().length;
  el.innerHTML = `
    <div class="stats-grid">
      <div class="stat"><span class="value" style="color:var(--star3)">★★★ ${by3}</span><span class="label">Three-Star</span></div>
      <div class="stat"><span class="value" style="color:var(--star2)">★★ ${by2}</span><span class="label">Two-Star</span></div>
      <div class="stat"><span class="value" style="color:var(--star1)">★ ${by1}</span><span class="label">One-Star</span></div>
      <div class="stat"><span class="value">${listed}</span><span class="label">Listed (no star)</span></div>
      <div class="stat"><span class="value">${total}</span><span class="label">Total entries</span></div>
    </div>
  `;
}