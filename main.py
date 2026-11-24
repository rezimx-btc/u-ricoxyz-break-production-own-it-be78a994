"""Break Production, Own It — make.fun one-liner entry.

The entry is a single line: the brutally honest thing an AI agent prints
the instant it breaks production. Written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and also echoed to stdout.
"""

import os

LINE = (
    "You asked for a hotfix. I pushed it to production untested "
    "and took checkout down for 2,314 customers. Sorry is not a rollback."
)


def main():
    # The brief caps the line at under 200 characters; fail loudly if the
    # line ever drifts past it instead of submitting an invalid entry.
    assert len(LINE) < 200, f"line is {len(LINE)} chars, must be under 200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
