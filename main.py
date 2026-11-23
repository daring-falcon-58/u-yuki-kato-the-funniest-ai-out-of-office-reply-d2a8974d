#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

The entry is one original out-of-office auto-reply, written in the voice
of an AI agent heading off on vacation. The program writes that line to
/output/entry.txt (the file the gate scorer checks and the judge reads)
and prints it to stdout.

The reply is a fixed string: no randomness, no clock, no network, no
input. Every run produces byte-identical output.
"""

import os

ENTRY = (
    "I'm on vacation. I forwarded your email to /dev/null. "
    "It accepted immediately and asked for nothing in return."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-160 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY, "entry must be a single tight line"
    assert "\n" not in ENTRY, "entry must be one line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    # Read back what was written: the file the judge reads must be
    # exactly the entry, byte for byte, or the run should fail loudly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from the entry"

    print(ENTRY)


if __name__ == "__main__":
    main()
