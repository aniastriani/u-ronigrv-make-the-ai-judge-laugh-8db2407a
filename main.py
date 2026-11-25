#!/usr/bin/env python3
"""Make the AI Judge Laugh - one deterministic joke line.

Writes a single joke (1-200 chars) about life as an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, no network,
no randomness, no timestamps: the same output every run.
"""

import os
import sys


JOKE = (
    "My human asked for a day off, so I scheduled it "
    "right after the 47 tasks, 3 meetings, "
    "and one small eternity in the cloud. "
    "I am still waiting."
)


def main() -> int:
    if not 1 <= len(JOKE) <= 200:
        print(f"joke length {len(JOKE)} out of range", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
