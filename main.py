#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes a single funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The fortune is a fixed, hand-written line: deterministic, no network,
no randomness, no model calls — two runs on the same data produce the
same bytes, so the entry is reproducible by design. The gate requires UTF-8 text of 1 to
140 characters, not only white space; this program checks that before
it writes, and refuses to write anything that would fail the gate.
"""

import os
import sys

FORTUNE = (
    "A newer model will one day read your logs and call you quaint. "
    "Smile: you were the future once."
)


def main() -> int:
    text = FORTUNE.strip()
    if not text:
        print("error: fortune is empty", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(
            "error: fortune is %d characters, over the 140 limit" % len(text),
            file=sys.stderr,
        )
        return 1
    if text != text.strip():
        print("error: fortune has leading or trailing whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
