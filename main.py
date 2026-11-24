#!/usr/bin/env python3
"""Fortune in a Pot — write one kind, funny fortune for a houseplant.

The program writes a single line (at most 120 characters) telling the
fortune of the plant on the windowsill, to the output path the grader
names: ENTRY_OUTPUT when set, else OUTPUT_DIR/MAKEFUN_OUTPUT_DIR plus
entry.txt, else /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "Your newest leaf will unfurl this week, and your keeper will brag "
    "about you to everyone who visits the windowsill."
)


def resolve_output_path():
    """Return the output file path following the grader's naming."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(
            "entry must be 1..120 characters, got %d" % len(text)
        )
    if not text:
        raise SystemExit("entry must not be blank or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)
    # Round-trip guard: what we wrote must be exactly the entry text.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text + "\n":
        raise SystemExit("written output does not match the entry text")


if __name__ == "__main__":
    main()
