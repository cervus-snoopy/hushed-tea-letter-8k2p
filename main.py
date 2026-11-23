#!/usr/bin/env python3
"""One-letter entry: write exactly one character to entry.txt.

Python 3 standard library only, no network. The output directory comes
from MAKEFUN_OUTPUT_DIR (fallback /output) and never depends on the
current working directory.
"""

import os


def main() -> None:
    letter = "B"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if len(letter) != 1:
        raise ValueError("entry must be exactly one character")
    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(letter)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)
    # Guard: read the file back and prove it holds exactly one character.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != letter or len(written) != 1:
        raise ValueError("entry.txt must hold exactly one character")


if __name__ == "__main__":
    main()
