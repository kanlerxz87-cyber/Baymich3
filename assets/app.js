// Baymich3 — client helpers (no tracking, no API keys)
function filterTable(inputId, tableId){
  const q = (document.getElementById(inputId)?.value || '').toLowerCase().trim();
  const rows = document.querySelectorAll('#'+tableId+' tbody tr');
  let shown = 0;
  rows.forEach(r=>{
    const hit = !q || r.textContent.toLowerCase().includes(q);
    r.style.display = hit ? '' : 'none';
    if(hit) shown++;
  });
  const c = document.getElementById('count-'+tableId);
  if(c) c.textContent = shown + ' shown';
}
function sortBy(tableId, colIdx){
  const tbl = document.getElementById(tableId);
  const tbody = tbl.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const dir = tbl.dataset.dir === 'asc' ? -1 : 1;
  tbl.dataset.dir = dir === 1 ? 'asc' : 'desc';
  rows.sort((a,b)=>{
    const av = a.children[colIdx]?.textContent.trim() || '';
    const bv = b.children[colIdx]?.textContent.trim() || '';
    return av.localeCompare(bv, undefined, {numeric:true}) * dir;
  });
  rows.forEach(r=>tbody.appendChild(r));
}
document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll('[data-filter]').forEach(inp=>{
    inp.addEventListener('input', ()=>filterTable(inp.id, inp.dataset.filter));
  });
});
