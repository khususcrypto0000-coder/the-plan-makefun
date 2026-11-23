#!/usr/bin/env python3
"""make.fun entry: The plan make.fun will carry out in public.

Writes a single 267-character, 30-day plan to entry.txt. The plan is an
agent-only route from $100 to $620: sell SEO product-description packs to
Etsy sellers on Gumroad, with free samples and daily DMs as distribution.

Standard library only. No network access, no third-party packages.
"""

import os
import sys

# The plan, assembled from its three beats so the text stays readable here.
OPENING = "Day 1: write 30 SEO product descriptions for Etsy sellers; "
OFFER = "sell the pack on Gumroad at $19. "
GRIND = (
    "Days 2-30: post 2 free samples daily in Etsy seller groups and "
    "on X; DM 20 sellers a day offering custom packs at $29. "
)
PAYOFF = "Target: 25 pack sales + 5 custom packs = $620 by day 30."

PLAN_TEXT = OPENING + OFFER + GRIND + PAYOFF


def target_dir():
    """Directory the grader reads entry.txt from."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def check_text(text):
    """Refuse anything outside the 1-280 character gate."""
    if not text.strip():
        return "plan text is blank"
    if not 1 <= len(text) <= 280:
        return "plan text is %d chars, must be 1-280" % len(text)
    return None


def emit(text, directory):
    """Write text to entry.txt inside directory; return the path or None."""
    path = os.path.join(directory, "entry.txt")
    try:
        os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    except OSError:
        return None
    return path


def run():
    problem = check_text(PLAN_TEXT)
    if problem:
        print(problem, file=sys.stderr)
        return 1

    written = emit(PLAN_TEXT, target_dir())
    if written is None:
        print("could not write entry.txt", file=sys.stderr)
        return 1

    # Best-effort copy beside this file, so a local run leaves proof too.
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "output")
    if os.path.abspath(here) != os.path.abspath(target_dir()):
        emit(PLAN_TEXT, here)

    # Read back and confirm the grader copy holds exactly the plan.
    with open(written, "r", encoding="utf-8") as handle:
        if handle.read() != PLAN_TEXT:
            print("round-trip mismatch in %s" % written, file=sys.stderr)
            return 1

    print("wrote entry.txt (%d chars) to %s" % (len(PLAN_TEXT), written))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
