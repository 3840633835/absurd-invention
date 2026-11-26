#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — entry program for make.fun.

Writes the one-sentence pitch for Typo Insurance (139 characters,
under the 220-character gate) to ``<output>/entry.txt`` and prints it.
Standard library only, no network, no randomness, no clock: the same
bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# Typo Insurance: a phone keyboard that turns your typos into
# compliments, so the furious text you sent your boss now calls them
# a visionary. The fix IS the joke: autocorrect already rewrites
# words, so a keyboard that rewrites them into flattery is silly yet
# weirdly plausible, and the disaster (a furious text to your boss)
# arrives as a promotion.
ENTRY = "Typo Insurance: a phone keyboard that turns your typos into compliments, so the furious text you sent your boss now calls them a visionary."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 220):
        raise SystemExit("entry must be 1 to 220 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
