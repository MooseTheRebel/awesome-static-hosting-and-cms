#!/usr/bin/env python3
"""Sort `[[providers]]` and `[[systems]]` entries by `name` (case-insensitive).

Run with `--check` to fail (exit 1) when entries are out of order without
rewriting; run without arguments to sort the files in place. Closes #61.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ("Hosting Providers.toml", "[[providers]]"),
    ("Content Management Systems.toml", "[[systems]]"),
]


def split_entries(text: str, marker: str) -> tuple[str, list[str]]:
    """Split a TOML file into (header, [entry, ...]) where each entry begins with `marker`."""
    idx = text.find(marker)
    if idx == -1:
        return text, []
    header = text[:idx]
    body = text[idx:]
    parts = body.split(marker)
    entries = [(marker + p).rstrip() for p in parts[1:] if p.strip()]
    return header, entries


def get_name(entry: str) -> str:
    match = re.search(r'name\s*=\s*"([^"]+)"', entry)
    return match.group(1).lower() if match else ""


def sort_file(path: Path, marker: str) -> bool:
    """Return True if the file was already sorted, False if it changed (or would change)."""
    text = path.read_text()
    trailing = "\n" if text.endswith("\n") else ""
    header, entries = split_entries(text.rstrip(), marker)
    sorted_entries = sorted(entries, key=get_name)
    if entries == sorted_entries:
        return True
    new_text = header + "\n\n".join(sorted_entries) + trailing
    path.write_text(new_text)
    return False


def check_file(path: Path, marker: str) -> bool:
    """Return True if sorted, False if not."""
    text = path.read_text()
    _, entries = split_entries(text.rstrip(), marker)
    return entries == sorted(entries, key=get_name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any TOML file is unsorted (without rewriting).",
    )
    args = parser.parse_args()

    unsorted: list[str] = []
    for filename, marker in FILES:
        path = REPO_ROOT / filename
        if not path.exists():
            print(f"warning: {filename} not found", file=sys.stderr)
            continue
        if args.check:
            if not check_file(path, marker):
                unsorted.append(filename)
        else:
            already = sort_file(path, marker)
            print(f"{filename}: {'already sorted' if already else 'sorted in place'}")

    if args.check and unsorted:
        print("Unsorted files (run `just sort-toml`):", file=sys.stderr)
        for f in unsorted:
            print(f"  {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
