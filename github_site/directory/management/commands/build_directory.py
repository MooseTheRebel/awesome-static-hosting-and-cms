"""
Management command: build_directory

Reads the TOML data files and writes them as JSON into the `data/` directory
so that coltrane can load them into template context as `{{ data }}`.

Run this before `coltrane record` (or `coltrane play`) whenever TOML data changes:

    python app.py build_directory
"""

import json
import tomllib
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Convert TOML directory data files to JSON for coltrane."

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR).resolve()
        repo_root = base_dir.parent
        data_dir = base_dir / "data"
        data_dir.mkdir(exist_ok=True)

        self._convert(
            toml_path=repo_root / "Hosting Providers.toml",
            json_path=data_dir / "hosting_providers.json",
        )

        self._convert(
            toml_path=repo_root / "Content Management Systems.toml",
            json_path=data_dir / "content_management_systems.json",
        )

    def _convert(self, toml_path: Path, json_path: Path) -> None:
        if not toml_path.exists():
            from django.core.management.base import CommandError
            raise CommandError(f"Source TOML file not found: {toml_path}")

        with toml_path.open("rb") as f:
            data = tomllib.load(f)

        json_path.write_text(json.dumps(data, indent=2) + "\n")
        self.stdout.write(self.style.SUCCESS(f"Wrote {json_path.relative_to(Path(settings.BASE_DIR).resolve())}"))
