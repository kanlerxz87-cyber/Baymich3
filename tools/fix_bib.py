#!/usr/bin/env python3
"""Rewrite data/bib.csv with honest provenance.

Audit finding: every non-SF row previously cited the *San Francisco* Bib
Gourmand list as its source, and all rows were labelled "Bib verified".
Michelin's own filter counts (checked 2026-11-24) are:
  San Francisco and surroundings .... 30 Bib Gourmand
  Oakland and surroundings .......... 29 Bib Gourmand
  Berkeley and surroundings ......... 28 Bib Gourmand   (lists overlap)
This file therefore cites the city-specific Bib list per row, and marks a row
"Verified" only where the name was actually seen on a Michelin list page in
this audit; everything else is explicitly Unverified and flagged for re-check.
"""
import csv
import os

COLS = ["name", "city", "cluster", "distinction", "cuisine", "price_band",
        "michelin_source", "official_url", "price_note", "verification_status",
        "notes"]

BIB = {
    "San Francisco": "https://guide.michelin.com/us/en/california/san-francisco/restaurants/bib-gourmand",
    "Oakland": "https://guide.michelin.com/us/en/california/oakland/restaurants/bib-gourmand",
    "Berkeley": "https://guide.michelin.com/us/en/california/berkeley/restaurants/bib-gourmand",
    "San Mateo": "https://guide.michelin.com/us/en/california/san-mateo/restaurants/bib-gourmand",
    "Menlo Park": "https://guide.michelin.com/us/en/california/menlo-park/restaurants/bib-gourmand",
    "San Jose": "https://guide.michelin.com/us/en/california/san-jose/restaurants/bib-gourmand",
    "San Anselmo": "https://guide.michelin.com/us/en/california/san-anselmo/restaurants/bib-gourmand",
    "Mill Valley": "https://guide.michelin.com/us/en/california/mill-valley/restaurants/bib-gourmand",
    "Fairfax": "https://guide.michelin.com/us/en/california/fairfax/restaurants/bib-gourmand",
    "Sonoma": "https://guide.michelin.com/us/en/california/sonoma/restaurants/bib-gourmand",
    "Glen Ellen": "https://guide.michelin.com/us/en/california/glen-ellen/restaurants/bib-gourmand",
    "Sebastopol": "https://guide.michelin.com/us/en/california/sebastopol/restaurants/bib-gourmand",
    "Petaluma": "https://guide.michelin.com/us/en/california/petaluma/restaurants/bib-gourmand",
    "San Leandro": "https://guide.michelin.com/us/en/california/san-leandro/restaurants/bib-gourmand",
    "El Cerrito": "https://guide.michelin.com/us/en/california/el-cerrito/restaurants/bib-gourmand",
    "Alameda": "https://guide.michelin.com/us/en/california/alameda/restaurants/bib-gourmand",
    "Hayward": "https://guide.michelin.com/us/en/california/hayward/restaurants/bib-gourmand",
}

# name -> (city, cluster, cuisine, price_band, seen_on_michelin_page_this_audit)
ROWS = [
    ("A16", "San Francisco", "C1 SF Core", "Pizza", "$$", True),
    ("Anchor Oyster Bar", "San Francisco", "C1 SF Core", "Seafood", "$$", False),
    ("Bansang", "San Francisco", "C1 SF Core", "Korean", "$$", False),
    ("Dumpling Home", "San Francisco", "C1 SF Core", "Dumplings", "$$", False),
    ("Good Good Culture Club", "San Francisco", "C1 SF Core", "South East Asian", "$$", False),
    ("Izakaya Rintaro", "San Francisco", "C1 SF Core", "Japanese", "$$", True),
    ("Kitchen Istanbul", "San Francisco", "C1 SF Core", "Turkish", "$$", False),
    ("Okane", "San Francisco", "C1 SF Core", "Japanese", "$$$", False),
    ("Outerlands", "San Francisco", "C1 SF Core", "Californian", "$$", False),
    ("Trestle", "San Francisco", "C1 SF Core", "Contemporary", "$$", False),
    ("Yank Sing", "San Francisco", "C1 SF Core", "Chinese", "$$", False),
    ("Z & Y", "San Francisco", "C1 SF Core", "Sichuan", "$$", True),
    ("Bombera", "Oakland", "C3 East Bay", "Mexican", "$$", False),
    ("FOB Kitchen", "Oakland", "C3 East Bay", "Filipino", "$$", False),
    ("Horn Barbecue", "Oakland", "C3 East Bay", "Contemporary", "$$", False),
    ("Joodooboo", "Oakland", "C3 East Bay", "Korean", "$$", False),
    ("Jo's Modern Thai", "Oakland", "C3 East Bay", "Thai", "$$", False),
    ("Soba Ichi", "Oakland", "C3 East Bay", "Japanese", "$$", True),
    ("Comal", "Berkeley", "C3 East Bay", "Mexican", "$$", True),
    ("Great China", "Berkeley", "C3 East Bay", "Chinese", "$$", True),
    ("Ippuku", "Berkeley", "C3 East Bay", "Japanese", "$$", True),
    ("Top Hatters Kitchen", "San Leandro", "C3 East Bay", "Contemporary", "", False),
    ("New Dumpling", "El Cerrito", "C3 East Bay", "Dumplings", "", False),
    ("Spinning Bones", "Alameda", "C3 East Bay", "Contemporary", "", False),
    ("Los Carnalitos", "Hayward", "C3 East Bay", "Mexican", "", False),
    ("Eylan", "Menlo Park", "C2 Peninsula", "Regional Cuisine", "", False),
    ("Pausa", "San Mateo", "C2 Peninsula", "Italian", "", False),
    ("Petiscos", "San Jose", "C2 Peninsula", "Mediterranean Cuisine", "", False),
    ("Insalata's", "San Anselmo", "C4 Marin", "Mediterranean Cuisine", "", False),
    ("Playa", "Mill Valley", "C4 Marin", "Mexican", "", False),
    ("Village Sake", "Fairfax", "C4 Marin", "Japanese", "", False),
    ("El Molino Central", "Sonoma", "C5 Wine Country", "Mexican", "", False),
    ("Glen Ellen Star", "Glen Ellen", "C5 Wine Country", "Californian", "$$", True),
    ("Khom Loi", "Sebastopol", "C5 Wine Country", "South East Asian", "", False),
    ("Stockhome", "Petaluma", "C5 Wine Country", "Contemporary", "", False),
    ("Valley", "Sonoma", "C5 Wine Country", "Californian", "", False),
]


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "bib.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for (name, city, cluster, cuisine, band, seen) in ROWS:
            src = BIB.get(city) or BIB["San Francisco"]
            if seen:
                vs = "Verified - name seen on this city's Michelin Bib Gourmand list page (24 Nov 2026)"
                notes = "Bib Gourmand = good quality, good value; NOT a star."
            else:
                vs = "Unverified - name carried over from an earlier pass; not re-confirmed on a Michelin list page in this audit"
                notes = "Re-check against the city Bib list page before relying on this row."
            w.writerow([name, city, cluster, "Bib Gourmand (no star)", cuisine,
                        band, src, "", "Official price/hours not collected", vs, notes])
    print(f"wrote {len(ROWS)} Bib rows")


if __name__ == "__main__":
    main()
