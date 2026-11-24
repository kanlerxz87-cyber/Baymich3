#!/usr/bin/env python3
"""Regenerate restaurants.html from data/restaurants.csv.

Kept as an entry point (session e1b8a912, PR #4). Running it regenerates all data pages.
The rendering now lives in scripts/build_site.py (single renderer for all data
pages); this file delegates to it so there is one source of HTML output.
Run:  python3 scripts/build_restaurants.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site  # noqa: E402

if __name__ == "__main__":
    build_site.main()
