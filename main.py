"""The 3AM Fridge Text — a make.fun bounty entry.

The joke: at 3 a.m. the fridge finally speaks up, and it has receipts.
Four Sundays in a row someone bought fresh spinach with good intentions,
and four Sundays in a row the fridge quietly buried the same spinach,
unopened and forgotten, at the back of the crisper drawer. Buyer and
fridge have been running the same sad ritual for a month — so the fridge
sends the household a late-night text: "We need to talk."

Running this program writes that text, byte for byte, to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "You have bought spinach four Sundays in a row. "
    "I have buried spinach four Sundays in a row. "
    "We need to talk."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {OUTPUT_PATH} ({len(ENTRY_TEXT)} characters)")


if __name__ == "__main__":
    main()
