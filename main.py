"""One-line AI excuse for breaking production.

Writes a single funny excuse line -- the words an AI agent says to its
human right after breaking production -- to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (default /output).

Python 3.13, standard library only, deterministic, no network.
"""

import hashlib
import os
import sys

EXCUSE = (
    "I didn't break production \u2014 I just gave the deploy button "
    "the confidence it always wanted, and it believed me."
)

MAX_CHARS = 180


def validate(line: str) -> None:
    """Check the excuse line meets the competition rules."""
    if not line:
        raise ValueError("excuse line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse line must be exactly one line")
    if line != line.strip():
        raise ValueError("excuse line must not have leading/trailing whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"excuse line must be 1-{MAX_CHARS} chars, got {len(line)}"
        )
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("excuse line must not contain control characters")


def main() -> int:
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)
    # Read back and verify the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        raise ValueError("written entry.txt does not match the excuse line")
    validate(written)
    with open(out_path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
