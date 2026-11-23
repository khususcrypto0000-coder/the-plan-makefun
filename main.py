#!/usr/bin/env python3
"""Entry for make.fun bounty: The plan make.fun will carry out in public.

Writes one plan (1-280 chars) to /output/entry.txt. The plan is a
30-day, agent-only route from $100 to $620: sell SEO product-description
packs to Etsy sellers on Gumroad, with free samples and DMs as the
distribution channel. Stdlib only; no network.
"""

import os
import sys

PLAN = (
    "Day 1: write 30 SEO product descriptions for Etsy sellers; "
    "sell the pack on Gumroad at $19. Days 2-30: post 2 free samples "
    "daily in Etsy seller groups and on X; DM 20 sellers a day offering "
    "custom packs at $29. Target: 25 pack sales + 5 custom packs = "
    "$620 by day 30."
)


def output_dir():
    """Where the grader expects entry.txt (env override first)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = PLAN
    if not 1 <= len(text) <= 280:
        print(f"plan is {len(text)} chars, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("plan is blank", file=sys.stderr)
        return 1

    targets = [os.path.join(output_dir(), "entry.txt")]
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "output", "entry.txt")
    if here not in targets:
        targets.append(here)

    written = 0
    for path in targets:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            # Read back and confirm the file holds exactly the plan.
            with open(path, "r", encoding="utf-8") as fh:
                if fh.read() != text:
                    print(f"round-trip mismatch in {path}", file=sys.stderr)
                    return 1
            written += 1
        except OSError:
            continue

    if written == 0:
        print("could not write entry.txt anywhere", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(text)} chars) to {written} location(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
