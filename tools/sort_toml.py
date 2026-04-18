#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["tomlkit"]
# ///
"""Sort `[[providers]]` and `[[systems]]` entries by `name` (case-insensitive).

Uses tomlkit so comments, blank-line separators between entries, and inline
field order are all preserved across a sort. Run with `--check` to fail
(exit 1) when entries are out of order without rewriting; run without
arguments to sort the files in place. Closes #61.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import tomlkit
from tomlkit.items import AoT

REPO_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ("Hosting Providers.toml", "providers"),
    ("Content Management Systems.toml", "systems"),
]


def _name(table) -> str:
    return str(table.get("name", "")).lower()


def _names_in_order(path: Path, aot_key: str) -> list[str]:
    doc = tomlkit.parse(path.read_text(encoding="utf-8"))
    aot = doc.get(aot_key)
    if not isinstance(aot, AoT):
        return []
    return [_name(t) for t in aot]


def _is_sorted(names: list[str]) -> bool:
    return names == sorted(names)


def sort_file(path: Path, aot_key: str) -> bool:
    """Return True if already sorted, False if the file was rewritten."""
    text = path.read_text(encoding="utf-8")
    doc = tomlkit.parse(text)
    aot = doc.get(aot_key)
    if not isinstance(aot, AoT) or len(aot) < 2:
        return True

    if _is_sorted([_name(t) for t in aot]):
        return True

    sorted_tables = sorted(aot, key=_name)
    doc[aot_key] = AoT(sorted_tables, parsed=True)
    path.write_text(tomlkit.dumps(doc), encoding="utf-8")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any TOML file is unsorted (without rewriting).",
    )
    args = parser.parse_args()

    unsorted: list[str] = []
    for filename, aot_key in FILES:
        path = REPO_ROOT / filename
        if not path.exists():
            print(f"warning: {filename} not found", file=sys.stderr)
            continue
        if args.check:
            if not _is_sorted(_names_in_order(path, aot_key)):
                unsorted.append(filename)
        else:
            already = sort_file(path, aot_key)
            print(f"{filename}: {'already sorted' if already else 'sorted in place'}")

    if args.check and unsorted:
        print("Unsorted files (run `just sort-toml`):", file=sys.stderr)
        for f in unsorted:
            print(f"  {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
