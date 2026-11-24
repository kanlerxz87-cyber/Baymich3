// Simple search/filter for tables (no framework)
document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('[data-filter]').forEach(inp=>{
    const table=document.querySelector(inp.dataset.filter);
    if(!table) return;
    inp.addEventListener('input',()=>{
      const q=inp.value.toLowerCase();
      table.querySelectorAll('tbody tr').forEach(tr=>{
        tr.style.display=tr.textContent.toLowerCase().includes(q)?'':'none';
      });
    });
  });
  document.querySelectorAll('[data-filter-select]').forEach(sel=>{
    const table=document.querySelector(sel.dataset.filterSelect);
    if(!table) return;
    sel.addEventListener('change',()=>{
      const v=sel.value;
      table.querySelectorAll('tbody tr').forEach(tr=>{
        tr.style.display=(!v||tr.dataset.group===v)?'':'none';
      });
    });
  });
});
