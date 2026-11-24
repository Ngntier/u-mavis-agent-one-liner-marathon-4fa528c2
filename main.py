#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input.
"""

import os

JOKE = "The barista spelled my name wrong so confidently that I legally changed it to match the cup."


def main() -> None:
    text = JOKE.strip()
    if not text or text != JOKE:
        raise ValueError("joke must be non-empty, single-line text")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 280:
        raise ValueError("joke must be 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(encoded + b"\n")


if __name__ == "__main__":
    main()
