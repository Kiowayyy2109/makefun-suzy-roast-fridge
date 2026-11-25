#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — a single-line fridge roast."""
import os

LINE = "My fridge has a light that turns on every time I open it, just so I can watch my life choices expire in high definition."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
