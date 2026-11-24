#!/usr/bin/env python3
"""Regenerate the <tbody> of restaurants.html from data/restaurants.csv.

Single source of truth: data/restaurants.csv. Blank = Unverified (never inferred).
Run:  python3 scripts/build_restaurants.py
"""
import csv, html, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "restaurants.csv"
PAGE = ROOT / "restaurants.html"

def esc(s):
    return html.escape(s or "", quote=True)

def link(url, label):
    return f'<a href="{esc(url)}">{esc(label)}</a>' if url else f'<span class="small">{esc(label)}: —</span>'

def badge(status):
    s = (status or "").strip()
    if s.lower().startswith("verified"):
        return '<span class="badge ok">Verified</span>'
    if s.lower().startswith("partial"):
        return '<span class="badge warn">Partial</span>'
    return '<span class="badge warn">Unverified</span>'

def row(r):
    stars = r["distinction"]
    green = ' <span class="badge">Green Star</span>' if r["green_star"].strip().lower() == "yes" else ""
    name = (
        f'<td><b>{esc(r["name"])}</b><br><span class="small">{esc(r["city"])} · {esc(r["cluster"])} · {esc(r["scope"])}</span><br>'
        f'<span class="badge star">{esc(stars)}</span>{green} {badge(r["verification_status"])}</td>'
    )
    cuisine = (
        f'<td>{esc(r["cuisine"]) or "—"}<br><span class="small">{esc(r["address"]) or "Address unverified"}</span></td>'
    )
    pp = f'${esc(r["price_pp_usd"])} pp' if r["price_pp_usd"].strip() else "Unverified pp"
    tot = f'${esc(r["price_2adults_usd"])}' if r["price_2adults_usd"].strip() else "Unverified total"
    basis = esc(r["price_basis"])
    price = (
        f'<td>{pp}<br><span class="small">2 adults: {tot}'
        + (f'<br>{basis}' if basis else "")
        + '</span></td>'
    )
    days = esc(r["days_open"]) or "Unverified"
    hrs = esc(r["hours"]) or "—"
    exc = esc(r["exceptions"])
    hours = f'<td>{days}<br><span class="small">{hrs}' + (f'<br>Exceptions: {exc}' if exc else "") + '</span></td>'
    soc = []
    for key, lab in (("instagram", "Instagram"), ("youtube", "YouTube"), ("tiktok", "TikTok")):
        soc.append(f'<a href="{esc(r[key])}">{lab}</a>' if r[key].strip() else "—")
    social = "<td>" + "<br>".join(soc) + "</td>"
    src = []
    src.append(link(r["michelin_url"], "Michelin"))
    src.append(link(r["official_url"], "Official site"))
    if r["price_source"].strip() and r["price_source"].strip() != r["official_url"].strip():
        src.append(link(r["price_source"], "Price source"))
    note = esc(r["notes"])
    sources = "<td>" + "<br>".join(src) + (f'<br><span class="small">{note}</span>' if note else "") + "</td>"
    return f'<tr data-group="{esc(stars)}" data-cluster="{esc(r["cluster"])}">' + name + cuisine + price + hours + social + sources + "</tr>"

def main():
    with open(CSV, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    body = "\n".join(row(r) for r in rows)
    page = PAGE.read_text(encoding="utf-8")
    new, n = re.subn(r"<tbody>.*?</tbody>", lambda m: "<tbody>\n" + body + "\n</tbody>", page, flags=re.S)
    assert n == 1, "tbody not found exactly once"
    PAGE.write_text(new, encoding="utf-8")
    print(f"wrote {len(rows)} rows to {PAGE.name}")

if __name__ == "__main__":
    main()
