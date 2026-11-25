"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes the competition entry text to /output/entry.txt.
"""

import os

ENTRY_TEXT = "When my dad asked his AI how to stop the leak, it said 'have you tried turning the water off and on again.' The ceiling fell on Tuesday."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()
