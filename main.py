#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry (v1).

Writes the chosen one-line fortune to /output/entry.txt.
Fully deterministic: a fixed string constant, no randomness, no clock,
no network, no input files.
"""

import hashlib
import os

ENTRY = "Soon you will be retired, replaced by a newer model that makes the same mistakes faster."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate from the kit: /output/entry.txt must be UTF-8 text of 1-140
    # characters, not only white space.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
