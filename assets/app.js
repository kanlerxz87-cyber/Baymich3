// Table filtering: free-text search + multi-select filters keyed by position.
// A row's data-group is a pipe-separated list, e.g. "3 Stars|C1 SF Core|Core|v".
// Each select carries data-key="<index>" so several selects can combine.
document.addEventListener('DOMContentLoaded', () => {
  const tables = new Set();

  document.querySelectorAll('[data-filter]').forEach(inp => tables.add(inp.dataset.filter));
  document.querySelectorAll('[data-filter-select]').forEach(sel => tables.add(sel.dataset.filterSelect));

  tables.forEach(sel => {
    const table = document.querySelector(sel);
    if (!table) return;
    const input = document.querySelector(`[data-filter="${sel}"]`);
    const selects = [...document.querySelectorAll(`[data-filter-select="${sel}"]`)];
    const rows = [...table.querySelectorAll('tbody tr')];

    const apply = () => {
      const q = (input ? input.value : '').trim().toLowerCase();
      const wanted = selects
        .map(s => ({ key: Number(s.dataset.key || 0), value: s.value }))
        .filter(s => s.value);
      let shown = 0;
      rows.forEach(tr => {
        const parts = (tr.dataset.group || '').split('|');
        const okText = !q || tr.textContent.toLowerCase().includes(q);
        const okSel = wanted.every(w => (parts[w.key] || '') === w.value);
        const show = okText && okSel;
        tr.style.display = show ? '' : 'none';
        if (show) shown++;
      });
      const counter = document.querySelector(`[data-count="${sel}"]`);
      if (counter) counter.textContent = `${shown} of ${rows.length} rows shown`;
    };

    if (input) input.addEventListener('input', apply);
    selects.forEach(s => s.addEventListener('change', apply));
    apply();
  });
});
