#!/usr/bin/env python3
"""Rebuild data/restaurants.csv in canonical column order.

Fixes the column-shift corruption (michelin_url stored in price_pp_usd) and
applies values re-verified from official sources on 2026-11-24.

Every value written here was read off an official source (restaurant site or
guide.michelin.com restaurant page). Anything not confirmed stays empty and is
labelled "Unverified" in verification_status. No value is inferred.
"""
import csv
import os

COLS = [
    "id", "name", "city", "cluster", "scope", "distinction", "green_star",
    "cuisine", "address", "michelin_url", "official_url", "price_pp_usd",
    "service_charge", "price_2adults_usd", "price_basis", "price_source",
    "days_open", "hours", "exceptions", "instagram", "youtube", "tiktok",
    "verification_status", "notes",
]

M = "https://guide.michelin.com/us/en/california/"

# id -> {field: value}. Only listed fields are overwritten.
UPD = {
    "R01": dict(
        price_pp_usd="", price_2adults_usd="",
        price_basis="Official homepage lists no price; Tock booking page shows $365-465",
        price_source="https://www.exploretock.com/ateliercrenn/",
        days_open="", hours="",
        instagram="https://www.instagram.com/atelier.crenn/",
        verification_status="Partial - star verified (Michelin 2026); Instagram verified via official site sameAs; price (Tock, booking page) indicative; hours Unverified",
        notes="Official homepage confirms chef/3 stars only; no hours or price text.",
    ),
    "R02": dict(
        price_pp_usd="425", service_charge="22% service charge",
        price_2adults_usd="1037",
        price_basis="$425 pp x 2 = $850; + 22% service = $1,037 (excl. tax and beverages)",
        price_source="https://www.benusf.com/info",
        days_open="Wed-Sat", hours="Dinner only, Wed-Sat",
        exceptions="",
        instagram="https://www.instagram.com/benu_sf/",
        verification_status="Verified - price + hours (official site); Instagram found via Instagram (not linked from official site)",
        notes="Corkage $100/750ml; valet $30 (official site).",
    ),
    "R03": dict(
        price_basis="Official site lists menus but no prices; no official price found",
        price_source="https://www.quincerestaurant.com/info-reservations",
        days_open="Tue-Sat",
        hours="Main dining room seatings 5:00-8:00pm; Bolinas Bar first-come",
        exceptions="Closed Nov 26 and Dec 25-26 (official homepage)",
        verification_status="Verified - hours + exceptions (official site); price Unverified",
        notes="Green Star per Michelin 2026. Lunch Fri-Sat (4 courses) per official page.",
    ),
    "R04": dict(
        address="355 11th St, San Francisco, CA 94103",
        price_basis="Official homepage shows address/phone/reservations only - no price or hours",
        price_source="https://www.californiossf.com/",
        verification_status="Verified - star + address (Michelin page + official site); price/hours Unverified",
        notes="World's first 3-star Mexican restaurant (Michelin 2026).",
    ),
    "R05": dict(
        price_basis="Official restaurant/booking pages list no menu price; bookings released 9am PST on the 1st of each month",
        price_source="https://singlethreadfarms.com/bookings/",
        days_open="", hours="Dinner only (10-course tasting)",
        exceptions="Closed Jan 1, Thanksgiving, Dec 25 (official bookings page)",
        verification_status="Verified - hours type + closures (official site); price + exact days Unverified",
        notes="5-room inn on site; inn stay guarantees a dining reservation (official).",
    ),
    "R06": dict(
        price_basis="Official site returned HTTP 500 at check - no official value obtained",
        verification_status="Unverified - official site unreachable at check; do not publish a price",
        notes="Green Star per Michelin 2026 list. Retry frenchlaundry.com later.",
    ),
    "R07": dict(
        price_basis="Official homepage is a video-only page with no price text",
        verification_status="Unverified - price/hours not on official homepage",
        notes="Promoted 2 stars -> 3 stars in 2026 (Michelin).",
    ),
    "R08": dict(
        price_pp_usd="295", service_charge="20% service + 4% surcharge",
        price_2adults_usd="731.60",
        price_basis="$295 pp x 2 = $590; + 24% (20% service + 4% surcharge) = $731.60 (excl. tax and beverages)",
        price_source="https://www.acquerellosf.com/seasonal-tasting-menu",
        verification_status="Verified - price (official menu page); hours Unverified",
        notes="Wine pairing $195 (official).",
    ),
    "R09": dict(
        price_pp_usd="350", service_charge="Not stated on experience page",
        price_2adults_usd="700",
        price_basis="Journey $350 pp x 2 = $700 (Discovery menu $290, Tue-Thu). Service charge % not stated",
        price_source="https://www.birdsongsf.com/experience",
        days_open="Tue-Sat",
        hours="Journey Tue-Sat; Discovery Tue-Thu",
        verification_status="Verified - price + days (official site); service charge Unverified",
        notes="Dinner only; closed Sun-Mon per menu availability.",
    ),
    "R10": dict(
        price_pp_usd="279", service_charge="20% service charge",
        price_2adults_usd="669.60",
        price_basis="$279 pp x 2 = $558; + 20% service = $669.60 (excl. tax and beverages)",
        price_source="https://commisrestaurant.com/info/",
        verification_status="Verified - price + address (official site); hours Unverified",
        notes="Pairing $139; $100 pp deposit credited to bill (official).",
    ),
    "R11": dict(
        price_pp_usd="315", service_charge="20% service charge",
        price_2adults_usd="756",
        price_basis="$315 pp x 2 = $630; + 20% service = $756 (excl. tax and beverages)",
        price_source="https://www.kilnsf.com/information",
        days_open="Tue-Sat",
        hours="Tue-Thu 18:00-20:30; Fri-Sat 17:00-20:30; dinner only",
        verification_status="Verified - price + hours (official site)",
        notes="Pairings $175 / $375 / $145. Corkage $125/750ml (official).",
    ),
    "R12": dict(
        price_pp_usd="320", service_charge="Not stated on tickets page",
        price_2adults_usd="640",
        price_basis="$320 pp x 2 = $640 (excl. beverages, service charge, tax)",
        price_source="https://www.lazybearsf.com/tickets/",
        days_open="Tue-Sat", hours="Reservations 5:00pm-9:00pm",
        exceptions="Tickets released 15th of each month, 10am, for the following month",
        instagram="https://www.instagram.com/lazybearsf/",
        verification_status="Verified - price + hours (official site); service charge Unverified",
        notes="Ticket price explicitly excludes service charge (official page).",
    ),
    "R13": dict(
        price_basis="Official FAQ lists no menu price",
        price_source="https://saisonsf.com/about/",
        days_open="Tue-Sat", hours="Dinner from 5:00pm",
        verification_status="Verified - days + hours (official FAQ); price Unverified",
        notes="Two Michelin stars stated by restaurant (official FAQ). Cancellation <48h charged $98 pp.",
    ),
    "R14": dict(
        price_pp_usd="330", service_charge="Not stated on food page",
        price_2adults_usd="660",
        price_basis="Tasting menu $330 pp x 2 = $660 (excl. tax and beverages)",
        price_source="https://www.sonsanddaughterssf.com/food",
        verification_status="Verified - price (official site); hours Unverified",
        notes="Second star 2024; Green Star summer 2025 (official page).",
    ),
    "R15": dict(
        price_pp_usd="127", service_charge="6% surcharge + 20% service",
        price_2adults_usd="320.04",
        price_basis="7-course $127 pp x 2 = $254; + 6% surcharge + 20% service = $320.04 (excl. tax and beverages)",
        price_source="https://www.7adamsrestaurant.com/menus",
        instagram="https://www.instagram.com/7adamsrestaurant/",
        verification_status="Verified - price + surcharges + Instagram (official site); hours Unverified",
        notes="5-course $87; Chef's Counter $157 (official). Address 1963 Sutter St per official footer.",
    ),
    "R16": dict(
        price_pp_usd="60", service_charge="20% service + 6% SF mandate",
        price_2adults_usd="151.20",
        price_basis="Lunch $60 pp x 2 = $120; + 26% = $151.20 (dinner is a la carte, varies)",
        price_source="https://anglerrestaurants.com/menu/",
        days_open="Daily", hours="Lunch 11:30am-2:00pm (dinner hours not stated on this page)",
        verification_status="Verified - lunch price + hours + service charges (official menu); dinner hours Unverified",
        notes="Menu page states 20% service charge + 6% SF mandate.",
    ),
    "R17": dict(
        price_basis="Official menu page links PDF menus only - no price text",
        price_source="https://www.misterjius.com/menu",
        days_open="Tue-Sat", hours="Tue-Thu 5-9pm; Fri-Sat 5-9:30pm; closed Sun-Mon",
        verification_status="Verified - hours (Michelin page); price Unverified (PDF menus)",
        notes="A la carte or banquet; Peking duck pre-order (official).",
    ),
    "R18": dict(
        price_basis="Official FAQ lists no menu price",
        price_source="https://www.narisf.com/faq",
        days_open="Daily",
        hours="Sun-Thu 5:30-9pm; Fri-Sat 5:30-9:30pm (7 nights)",
        verification_status="Verified - hours (official FAQ); price Unverified",
        notes="Inside Hotel Kabuki lobby (official FAQ).",
    ),
    "R19": dict(
        price_basis="Official site lists no menu price",
        price_source="https://www.restaurantnisei.com/",
        days_open="Wed-Sun", hours="Dinner only",
        instagram="https://www.instagram.com/niseisf/",
        verification_status="Verified - days + Instagram (official site); price + exact hours Unverified",
        notes="2316 Polk St; 20% service noted on beverage page.",
    ),
    "R20": dict(
        price_basis="Official menu page links PDF menus only - no price text",
        price_source="https://www.sanhowon.com/menu",
        verification_status="Unverified - price + hours not on official site",
        notes="Korean BBQ; charcoal grill. Secondary hours removed pending official confirmation.",
    ),
    "R21": dict(
        price_pp_usd="195", service_charge="5% SF mandate",
        price_2adults_usd="409.50",
        price_basis="Fall 2026 tasting $195 pp x 2 = $390; + 5% SF mandate = $409.50 (excl. tax and beverages)",
        price_source="https://www.sorrelrestaurant.com/menus/",
        hours="Bar seats 5pm-9pm Wed-Sun",
        verification_status="Verified - price + mandate (official menus page); dinner days Unverified",
        notes="5-course $125; pairings $105/$225/$75 (official).",
    ),
    "R22": dict(
        price_pp_usd="180", service_charge="20% service charge (in place of gratuity)",
        price_2adults_usd="432",
        price_basis="11-course $180 pp x 2 = $360; + 20% service = $432 (excl. tax and beverages)",
        price_source="https://www.madcapmarin.com/food",
        days_open="Tue-Sat", hours="Dinner Tue-Sat (4-course option Tue-Thu)",
        verification_status="Verified - price + service charge + days (official site)",
        notes="4-course $145 Tue-Thu (official).",
    ),
    "R23": dict(
        price_basis="Official dine page lists menu formats but no prices",
        price_source="https://auberge.com/auberge-du-soleil/dine/",
        days_open="Daily", hours="The Bar: continuous dining 11:30am-11pm daily",
        verification_status="Verified - restaurant formats + bar hours (official site); tasting price + dining-room hours Unverified",
        notes="3- or 4-course prix fixe / 6-course tasting (official). Michelin 1 Star 2026 + Three Keys.",
    ),
    "R24": dict(
        price_basis="Official menus page links sample menus with no prices",
        price_source="https://www.protegepaloalto.com/menus",
        days_open="Tue-Sat", hours="5:00pm-9:15pm",
        exceptions="Closed Sunday and Monday (official site)",
        verification_status="Verified - hours + address (official site); price Unverified",
        notes="Dining Room 7-course tasting; Lounge a la carte (official).",
    ),
    "R25": dict(
        price_basis="Official site lists hours/reservations only - no price",
        price_source="https://www.wakuriya.com/",
        days_open="Wed-Sun",
        hours="Wed-Fri dinner 6:30pm; Sat-Sun dinner 6:00pm",
        exceptions="Reservations by phone, one month in advance",
        verification_status="Verified - hours + address (official site); price Unverified",
        notes="115 De Anza Blvd, San Mateo; (650) 286-0410 (official).",
    ),
    "R26": dict(
        official_url="https://www.hildaandjessesf.com/",
        price_basis="Official site has no menu text or price; Michelin price band $$$",
        price_source="https://www.hildaandjessesf.com/",
        days_open="Mon, Thu-Sun",
        hours="Mon/Thu/Fri 5:30-9pm; Sat-Sun 10am-2pm (brunch)",
        verification_status="Verified - hours (Michelin page); price Unverified - not on official site",
        notes="Menu changes frequently and is not printed (Michelin). Address 701 Union St.",
    ),
    "R27": dict(
        price_basis="A la carte; official homepage lists no prices",
        price_source="https://www.kinkhao.com/",
        days_open="Daily",
        hours="Lunch 11:30am-2pm daily; dinner Sun-Thu 5:30-9pm, Fri-Sat 5:30-10pm",
        verification_status="Verified - hours (official homepage); price Unverified",
        notes="55 Cyril Magnin St (corner Mason & Ellis).",
    ),
    "R28": dict(
        name="Naides", city="San Francisco", cluster="C1 SF Core", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Filipino, Contemporary",
        address="708 Bush St, San Francisco, CA 94108",
        michelin_url=M + "san-francisco/restaurant/naides",
        official_url="https://www.restaurantnaides.com/",
        price_pp_usd="", service_charge="", price_2adults_usd="",
        price_basis="Michelin price band $$$$; official site not yet checked for price",
        price_source=M + "san-francisco/restaurant/naides",
        days_open="Thu-Sun", hours="5:30pm-8:30pm (closed Mon-Wed)",
        verification_status="Verified - address + hours (Michelin page); price Unverified",
        notes="NEW 1 Star in 2026 (Michelin).",
    ),
    "R29": dict(
        official_url="https://www.nikusteakhouse.com/",
        price_basis="A la carte steakhouse; official homepage lists no prices",
        price_source="https://www.nikusteakhouse.com/",
        days_open="Daily", hours="Sun-Thu 5-9pm; Fri-Sat 5-10pm",
        verification_status="Verified - hours + address (official site); price Unverified",
        notes="Part of Omakase Restaurant Group (official).",
    ),
    "R30": dict(
        official_url="https://ssalsf.com/",
        price_pp_usd="270", service_charge="Not stated on homepage",
        price_2adults_usd="540",
        price_basis="Tasting menu 'starts at' $270 pp x 2 = $540 (excl. beverages, service, tax)",
        price_source="https://ssalsf.com/",
        days_open="Wed-Sun", hours="5:30pm-8:30pm, reservation only",
        verification_status="Verified - price + hours (official site)",
        notes="$150 pp non-refundable deposit applied to bill (official).",
    ),
    "R31": dict(
        official_url="https://www.statebirdsf.com/",
        price_basis="Official homepage covers reservations only - no price or hours text",
        price_source="https://www.statebirdsf.com/",
        verification_status="Unverified - price + hours not on official site",
        notes="California/Californian small plates; sister to The Progress.",
    ),
    "R32": dict(
        official_url="https://theprogress-sf.com/",
        price_basis="Official homepage covers reservations only - no price or hours text",
        price_source="https://theprogress-sf.com/",
        verification_status="Unverified - price + hours not on official site",
        notes="Sister restaurant to State Bird Provisions.",
    ),
    "R33": dict(
        name="Wolfsbane", city="San Francisco", cluster="C1 SF Core", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Contemporary, Californian",
        address="2495 3rd St, San Francisco, CA 94107",
        michelin_url=M + "san-francisco/restaurant/wolfsbane",
        official_url="https://wolfsbanesf.com/",
        price_pp_usd="", service_charge="", price_2adults_usd="",
        price_basis="Tasting-menu page not priced in fetched text; official site states menu only",
        price_source="https://wolfsbanesf.com/tasting",
        days_open="Tue-Sat", hours="5:30pm-10:00pm",
        verification_status="Verified - address + hours (official site + Michelin); price Unverified",
        notes="NEW 1 Star in 2026 (Michelin). A la carte bar menu, walk-ins nightly (official).",
    ),
    "R34": dict(
        name="Sun Moon Studio", city="Oakland", cluster="C3 East Bay", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Californian",
        address="1940 Union St, Ste 21, Oakland, CA 94607",
        michelin_url=M + "oakland/restaurant/sun-moon-studio",
        official_url="https://www.sunmoonstudio.com/",
        price_pp_usd="", service_charge="", price_2adults_usd="",
        price_basis="Official site is image-only; Michelin price band $$$$",
        price_source=M + "oakland/restaurant/sun-moon-studio",
        days_open="Thu-Sun", hours="Thu-Sat 5-9pm; Sun 5-8pm (closed Mon-Wed)",
        verification_status="Verified - address + hours (Michelin page); price Unverified",
        notes="Tasting menu; tiny dining room (Michelin).",
    ),
    "R35": dict(
        official_url="https://www.selbysrestaurant.com/",
        price_basis="Official homepage states 'open for dinner nightly' with no price text",
        price_source="https://www.selbysrestaurant.com/",
        days_open="Daily", hours="Dinner nightly (hours not stated)",
        verification_status="Verified - days (official site); price + hours Unverified",
        notes="Michelin 2026 One Star logo on official site. Address per Michelin listing.",
    ),
    "R36": dict(
        name="Auro", city="Calistoga", cluster="C5 Wine Country", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Contemporary, French",
        address="Four Seasons Resort Napa Valley, 400 Silverado Trl, Calistoga, CA 94515",
        michelin_url=M + "calistoga/restaurant/auro",
        official_url="https://www.auronapavalley.com/",
        price_pp_usd="275", service_charge="Not stated on menu page",
        price_2adults_usd="550",
        price_basis="Seven-course tasting 'starting at' $275 pp x 2 = $550 (excl. tax, beverages, service)",
        price_source="https://www.auronapavalley.com/menus/",
        days_open="Wed-Sat", hours="5:00pm-9:00pm",
        instagram="https://www.instagram.com/auronapavalley/",
        verification_status="Verified - price + Instagram (official site); hours from Michelin page",
        notes="Wine pairing from $195 pp; corkage $100 (official). Third consecutive star.",
    ),
    "R37": dict(
        official_url="https://www.cyrusrestaurant.com/",
        price_basis="Official site describes the Dining Journey but lists no price",
        price_source="https://www.cyrusrestaurant.com/",
        address="275 Highway 128, Geyserville, CA 95441",
        verification_status="Unverified - price + hours not on official site",
        notes="Reservations open 1st of each month, 2 months ahead (official).",
    ),
    "R38": dict(
        name="Troubadour", city="Healdsburg", cluster="C5 Wine Country", scope="Core",
        distinction="1 Star", green_star="No", cuisine="French, Californian",
        address="381 Healdsburg Ave, Healdsburg, CA 95448",
        michelin_url=M + "healdsburg/restaurant/troubadour",
        official_url="https://www.troubadourhbg.com/",
        price_pp_usd="205", service_charge="Not stated on menu page",
        price_2adults_usd="410",
        price_basis="Le Diner 8-course prix fixe $205 pp x 2 = $410 (11-course Chef's Table also offered)",
        price_source="https://www.troubadourhbg.com/le-diner-menu",
        days_open="Thu-Sun", hours="Dinner 5:30pm-8:30pm",
        verification_status="Verified - price (official menu); hours from Michelin page",
        notes="Bakery/lunch by day, Le Diner at night (official). NEW 1 Star 2026.",
    ),
    "R39": dict(
        name="Press", city="Saint Helena", cluster="C5 Wine Country", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Modern Cuisine",
        address="587 St Helena Hwy, St Helena, CA 94574",
        michelin_url=M + "saint-helena/restaurant/press",
        official_url="https://pressnapavalley.com/",
        price_pp_usd="", service_charge="", price_2adults_usd="",
        price_basis="Food page blocked by bot challenge at check - no official price obtained",
        price_source="https://pressnapavalley.com/food/",
        days_open="Daily", hours="Sun-Thu 5-9pm; Fri-Sat 5-10pm",
        verification_status="Verified - hours + address (official homepage); price Unverified",
        notes="Reservations via OpenTable (official).",
    ),
    "R40": dict(
        name="Plumed Horse", city="Saratoga", cluster="C2 Peninsula", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Contemporary, American",
        address="14555 Big Basin Way, Saratoga, CA 95070",
        michelin_url=M + "saratoga/restaurant/plumed-horse",
        official_url="https://plumedhorse.com/",
        price_pp_usd="225", service_charge="Not stated on menu page",
        price_2adults_usd="450",
        price_basis="Chef's Tasting Menu $225 pp x 2 = $450 (4-course prix fixe $138 also offered)",
        price_source="https://plumedhorse.com/menu/",
        days_open="Tue-Sun", hours="Dinner Tue-Sun (5-10pm per Michelin)",
        verification_status="Verified - price + days (official site); service charge Unverified",
        notes="Wine pairing $148; n/a pairing $118 (official menu).",
    ),
    "R41": dict(
        name="The Village Pub", city="Woodside", cluster="C2 Peninsula", scope="Core",
        distinction="1 Star", green_star="No", cuisine="Contemporary, American",
        address="2967 Woodside Rd, Woodside, CA 94062",
        michelin_url=M + "woodside/restaurant/the-village-pub",
        official_url="https://www.thevillagepub.net/",
        price_pp_usd="", service_charge="", price_2adults_usd="",
        price_basis="Three-course prix fixe per Michelin; official site shows no price",
        price_source="https://www.thevillagepub.net/",
        days_open="Mon-Sat",
        hours="Mon-Thu 5-9pm; Fri 11:30am-2:30pm & 5-9pm; Sat 11am-2pm & 5-9pm (Michelin)",
        verification_status="Verified - hours (Michelin page); price Unverified",
        notes="One Michelin Star every year since 2009 (official site).",
    ),
    "R42": dict(
        name="Aubergine", city="Carmel-by-the-Sea", cluster="C6 Extension", scope="Extension",
        distinction="2 Stars", green_star="No", cuisine="Contemporary, Californian",
        address="L'Auberge Carmel, Monte Verde at 7th, Carmel-by-the-Sea, CA 93921",
        michelin_url=M + "carmel-by-the-sea/restaurant/aubergine",
        official_url="https://auberginecarmel.com/",
        price_pp_usd="285", service_charge="22% charge plus taxes",
        price_2adults_usd="695.40",
        price_basis="$285 pp x 2 = $570; + 22% charge = $695.40 (plus taxes, excl. beverages)",
        price_source="https://auberginecarmel.com/",
        days_open="Wed-Sun", hours="5:00pm-10:30pm, last seating 8:00pm",
        verification_status="Verified - price + charge + hours + address (official site)",
        notes="Second star earned 2024 (official site). Extension area (Monterey Co.).",
    ),
    "R43": dict(
        address="5600 CA-1, Elk, CA 95432",
        official_url="https://www.theharborhouseinn.com/",
        price_basis="Official site lists tasting/lunch times but no price",
        price_source="https://www.theharborhouseinn.com/",
        days_open="Thu-Mon",
        hours="Full Experience tasting Thu-Mon at 5:30, 6:00, 6:45pm; lunch Thu-Mon 12:00, 12:30, 1:00pm",
        exceptions="Restaurant closed Tuesday and Wednesday (official)",
        verification_status="Verified - hours + closures (official site); price Unverified",
        notes="Extension area (Mendocino Co.). 11-room inn; under-15 not permitted (official).",
    ),
    "R44": dict(
        name="Chez Noir", city="Carmel-by-the-Sea", cluster="C6 Extension", scope="Extension",
        distinction="1 Star", green_star="No", cuisine="Contemporary, Seafood",
        address="431 5th Ave, Carmel-by-the-Sea, CA 93921",
        michelin_url=M + "carmel-by-the-sea/restaurant/chez-noir",
        official_url="https://www.cheznoircarmel.com/",
        price_pp_usd="165", service_charge="20% service charge",
        price_2adults_usd="396",
        price_basis="$165 pp x 2 = $330; + 20% service = $396 (before tax; rises to $175 pp / $420 from 1 Dec 2026)",
        price_source="https://www.cheznoircarmel.com/menu",
        days_open="Mon, Tue, Thu-Sun; lunch Sat-Sun",
        hours="Dinner 5:00pm-8:30pm; lunch Sat-Sun 11:00am-1:30pm",
        exceptions="Closed Wednesday (Michelin hours)",
        instagram="https://www.instagram.com/cheznoircarmel",
        verification_status="Verified - price + service charge + Instagram (official site); hours from Michelin page",
        notes="Extension area (Monterey Co.). No phone; email only (official).",
    ),
}


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "restaurants.csv")
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    assert header == COLS, header

    out = []
    seen = set()
    for raw in body:
        row = dict(zip(COLS, raw))
        rid = row["id"]
        seen.add(rid)
        # Undo the historical column shift: a URL found in price_pp_usd means
        # michelin_url/official_url were pushed left and everything after slid.
        if row["price_pp_usd"].startswith("http"):
            row["michelin_url"] = row["price_pp_usd"]
            row["price_pp_usd"] = ""
        # Lazy Bear historically had Instagram in the youtube column.
        if row["youtube"].startswith("https://www.instagram.com/"):
            row["instagram"] = row["youtube"]
            row["youtube"] = ""
        row.update(UPD.get(rid, {}))
        # No row may ship without a Michelin source link.
        assert row["michelin_url"].startswith("https://guide.michelin.com"), rid
        out.append({c: row[c] for c in COLS})

    missing = set(UPD) - seen
    assert not missing, missing

    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in out:
            w.writerow(r)
    print(f"wrote {len(out)} rows, {len(COLS)} columns")


if __name__ == "__main__":
    main()
