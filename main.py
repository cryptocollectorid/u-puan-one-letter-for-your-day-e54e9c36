#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter W, to /output/entry.txt.
Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

LETTER = "W"


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # exactly one character, A-Z, no newline, no extra whitespace.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise SystemExit(f"entry letter must be exactly one A-Z character, got {LETTER!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(f"Wrote {len(LETTER)} character to {path}")


if __name__ == "__main__":
    main()
