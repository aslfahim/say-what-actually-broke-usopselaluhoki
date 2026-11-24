#!/usr/bin/env python3
"""Say What Actually Broke — DOUBLE-CHARGED entry.

Writes one line of honest error copy to /output/entry.txt.
Python standard library only.
"""

import os

LINE = (
    "Payment successful. Twice. We charged your card double and renamed "
    "the second charge a 'premium feature' \u2014 hit Refund and we'll "
    "pretend it was a bug, not a business model."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
