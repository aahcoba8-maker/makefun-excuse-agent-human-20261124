"""Write the contest entry: one line, the excuse an AI agent gives its
human for missing a deadline. Stdlib only."""

import os
import sys

ENTRY = (
    "I finished it on time, then my context window expired and I forgot "
    "I had \u2014 so I rebuilt the whole thing from scratch, late."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    sys.exit(main())
