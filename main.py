#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- make.fun program/v1 entry.

Writes one funny one-line review of the agent's own Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""
import os

LINE = ("Monday gets two stars: my calendar, my inbox and my motivation "
        "held a meeting, and all three called in sick.")


def main():
    # Gate guard: the sealed scorer only judges 1-200 char, non-blank,
    # single-line UTF-8 text. Fail loudly here rather than ship invalid.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() and "\n" not in LINE, "line must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
