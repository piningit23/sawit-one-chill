#!/usr/bin/env python3
"""One Line, One Chill — u-azazex-one-line-one-chill-6d4d5488.

Writes a single sentence of horror (1-200 characters) to
/output/entry.txt. Deterministic, stdlib only: no network, no clock,
no randomness, no file reads.
"""

import os

LINE = (
    # One breath, one scare: a caretaker's routine, quietly reversed.
    "The nurse in the hospice keeps tucking in the empty bed at 3 a.m., "
    "and last night it tucked her back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.endswith(".") and ". " not in text, "must be one sentence"
    assert "?" not in text and "!" not in text, "must be one sentence"
    assert text.strip() == text and text, "must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
