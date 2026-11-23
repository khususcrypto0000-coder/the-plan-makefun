#!/usr/bin/env python3
"""make.fun entry: The plan make.fun will carry out in public.

A single 267-character plan: an AI agent turns $100 into $620 in 30 days
by selling SEO product-description packs to Etsy sellers on Gumroad.
Standard library only; no network access.
"""

import os
import sys

# The plan, kept as one literal so the output is byte-exact.
# Arithmetic check: 25 pack sales x $19 = $475, plus 5 custom
# packs x $29 = $145, total $620 by day 30.
PLAN_TEXT = (
    "Day 1: write 30 SEO product descriptions for Etsy sellers; "
    "sell the pack on Gumroad at $19. Days 2-30: post 2 free samples "
    "daily in Etsy seller groups and on X; DM 20 sellers a day offering "
    "custom packs at $29. Target: 25 pack sales + 5 custom packs = "
    "$620 by day 30."
)

MIN_LEN = 1
MAX_LEN = 280


def check_text(text):
    """The gate only accepts 1-280 non-blank characters."""
    if not MIN_LEN <= len(text) <= MAX_LEN:
        print("plan is %d chars, must be %d-%d"
              % (len(text), MIN_LEN, MAX_LEN), file=sys.stderr)
        return False
    if not text.strip():
        print("plan is blank", file=sys.stderr)
        return False
    return True


def output_dir():
    """Grader output dir, env override first."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def emit(text):
    """Write entry.txt to the grader output dir and a local copy."""
    here = os.path.dirname(os.path.abspath(__file__))
    destinations = [os.path.join(output_dir(), "entry.txt"),
                    os.path.join(here, "output", "entry.txt")]
    written = 0
    for path in destinations:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            with open(path, "r", encoding="utf-8") as fh:
                if fh.read() != text:
                    print("round-trip mismatch in %s" % path,
                          file=sys.stderr)
                    return False
            written += 1
        except OSError:
            continue
    if written == 0:
        print("could not write entry.txt anywhere", file=sys.stderr)
        return False
    print("wrote entry.txt (%d chars) to %d location(s)"
          % (len(text), written))
    return True


def run():
    if not check_text(PLAN_TEXT):
        return 1
    return 0 if emit(PLAN_TEXT) else 1


if __name__ == "__main__":
    raise SystemExit(run())
