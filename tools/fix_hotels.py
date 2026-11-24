#!/usr/bin/env python3
"""Rebuild data/hotels.csv: fix wrong addresses found during audit and
re-verify each row against the hotel's own site (checked 2026-11-24).

Corrections found in this audit (all were wrong in the previous data):
  * Cavallo Point  - "601 Bridgeway" -> 601 Murray Circle, Fort Baker, Sausalito
                     (official contact page)
  * 1 Hotel SF     - "22 Battery St"  -> 8 Mission Street (official site)
  * Bardessono     - "6640 Washington St" (that is The French Laundry's
                     address) -> 6526 Yount St, Yountville (official contact page)
Everything else that could not be confirmed on the hotel's own site is
labelled Unverified rather than kept as-is.
"""
import csv
import os

COLS = ["rank", "hotel", "city", "cluster", "address", "official_url",
        "michelin_hotel_source", "starred_in_cluster", "why_ranked",
        "verification_status", "notes"]

MH = "https://guide.michelin.com/us/en/hotels"

ROWS = [
    (1, "Four Seasons Hotel San Francisco", "San Francisco", "C1 SF Core",
     "757 Market St, San Francisco, CA 94103",
     "https://www.fourseasons.com/sanfrancisco/", 25,
     "SoMa/Market - walkable to Benu, Birdsong, Californios, Saison; C1 SF Core holds 25 starred",
     "Verified - address (official site)", "MKT Restaurant on site (official)."),
    (2, "Fairmont San Francisco", "San Francisco", "C1 SF Core",
     "950 Mason St, San Francisco, CA 94108",
     "https://www.fairmont.com/en/hotels/san-francisco/fairmont-san-francisco.html", 25,
     "Nob Hill - central to Acquerello, Sons & Daughters, Quince, Atelier Crenn",
     "Verified - address (official location page)",
     "606 guestrooms (official). Parking 75 spaces, valet (official)."),
    (3, "The St. Regis San Francisco", "San Francisco", "C1 SF Core",
     "", "https://www.marriott.com/en-us/hotels/sfoxr-the-st-regis-san-francisco/overview/", 25,
     "SoMa - steps to SFMOMA and Yerba Buena; near Benu and Birdsong",
     "Partial - hotel + SoMa location verified (official site); street address Unverified",
     "Forbes Five-Star per official site. Astra restaurant on site."),
    (4, "Palace Hotel San Francisco", "San Francisco", "C1 SF Core",
     "", "https://www.marriott.com/en-us/hotels/sfodt-the-palace-a-luxury-collection-hotel-san-francisco/overview/", 25,
     "FiDi/SoMa edge - near Benu, Angler",
     "Unverified - official page did not load at check; no address published",
     "Retry official Marriott Luxury Collection page."),
    (5, "The Ritz-Carlton San Francisco", "San Francisco", "C1 SF Core",
     "", "https://www.ritzcarlton.com/en/hotels/san-francisco/", 25,
     "Nob Hill - near Acquerello, Sons & Daughters, Quince",
     "Unverified - official page did not load at check; no address published",
     "Retry ritzcarlton.com later."),
    (6, "Taj Campton Place", "San Francisco", "C1 SF Core",
     "", "https://www.tajcamptonplace.com/", 25,
     "Union Square - near Kin Khao and Quince",
     "Partial - hotel verified (official site); street address not in fetched text",
     "Campton Bar + Bistro on site (official)."),
    (7, "Hotel Kabuki", "San Francisco", "C1 SF Core",
     "", "https://www.hotelkabuki.com/", 25,
     "Japantown - same block as Nari (1 star); near 7 Adams and Nisei",
     "Unverified - official page did not load at check; no address published",
     "Nari's own FAQ confirms it is inside the Kabuki hotel (cross-source)."),
    (8, "1 Hotel San Francisco", "San Francisco", "C1 SF Core",
     "8 Mission St, San Francisco, CA",
     "https://www.1hotels.com/san-francisco", 25,
     "Embarcadero - near Angler and Benu",
     "Verified - address (official site)",
     "Previous data listed 22 Battery St - corrected to 8 Mission St."),
    (9, "Rosewood Sand Hill", "Menlo Park", "C2 Peninsula",
     "", "https://www.rosewoodhotels.com/en/sand-hill-menlo-park", 5,
     "Peninsula base - Selby's, Protege, Plumed Horse, Village Pub, Wakuriya (5 starred)",
     "Partial - hotel verified (official site); street address not in fetched text",
     "Madera restaurant + Asaya spa on site (official)."),
    (10, "The Claremont Hotel Berkeley", "Berkeley", "C3 East Bay",
     "", "https://www.theclaremontclubspa.com/", 2,
     "East Bay base - Commis and Sun Moon Studio (2 starred) + Bib cluster",
     "Unverified - official page did not load at check; no address published",
     "Retry official Claremont page."),
    (11, "Cavallo Point", "Sausalito", "C4 Marin",
     "601 Murray Circle, Fort Baker, Sausalito, CA 94965",
     "https://www.cavallopoint.com/", 1,
     "Marin gateway - Madcap (1 star) + Marin Bib cluster",
     "Verified - address (official contact page)",
     "Previous data listed 601 Bridgeway - corrected. Sula and Farley restaurants on site."),
    (12, "Auberge du Soleil", "Rutherford", "C5 Wine Country",
     "180 Rutherford Hill Rd, Rutherford, CA 94573",
     "https://auberge.com/auberge-du-soleil/", 8,
     "Wine Country - 1-star restaurant ON SITE; Napa/Sonoma cluster has 8 starred in data",
     "Verified - restaurant on site + formats (official dine page); street address Unverified",
     "Michelin 1 Star 2026 and Three Keys per official site."),
    (13, "SingleThread Inn", "Healdsburg", "C5 Wine Country",
     "131 North St, Healdsburg, CA 95448",
     "https://singlethreadfarms.com/restaurant/", 8,
     "Wine Country - 3-star restaurant + 5-room inn combined; inn stay guarantees a table",
     "Verified - address (Michelin restaurant page) + inn/restaurant combined (official site)",
     "Michelin shows Three Keys for SingleThread Inn; Green Star for the restaurant."),
    (14, "Bardessono", "Yountville", "C5 Wine Country",
     "6526 Yount St, Yountville, CA 94599",
     "https://www.bardessono.com/", 8,
     "Wine Country - walkable to The French Laundry (3 stars)",
     "Verified - address (official contact page)",
     "Previous data listed 6640 Washington St, which is The French Laundry - corrected."),
]


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "hotels.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for r in ROWS:
            (rank, hotel, city, cluster, address, url, stars, why, vs, notes) = r
            w.writerow([rank, hotel, city, cluster, address, url, MH, stars, why, vs, notes])
    print(f"wrote {len(ROWS)} hotel rows")


if __name__ == "__main__":
    main()
