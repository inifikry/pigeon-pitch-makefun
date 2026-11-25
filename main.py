#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes a single-line elevator pitch from a city pigeon to investors
for its startup, to /output/entry.txt. Deterministic: every run
writes the exact same line.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The pitch: a city pigeon pitching its startup to investors.
ENTRY = "I run the city's original drone network: 10,000 pilots, paid in breadcrumbs, zero charging time \u2014 and we already poop on every statue downtown, so the brand awareness is built in."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
