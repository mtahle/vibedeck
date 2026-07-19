#!/usr/bin/env python3
"""Install VibeDeck's project-os skill into a Codex skills directory."""

import argparse
import os
from pathlib import Path
import shutil


def install(source: Path, destination: Path, force: bool = False) -> Path:
    if destination.exists():
        if not force:
            raise FileExistsError(
                f"{destination} already exists; use --force to replace it"
            )
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    default_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=default_home,
        help="Codex home directory (default: CODEX_HOME or ~/.codex)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing project-os skill",
    )
    args = parser.parse_args()

    repository = Path(__file__).resolve().parents[1]
    source = repository / "skills" / "project-os"
    destination = args.codex_home.expanduser().resolve() / "skills" / "project-os"
    installed = install(source, destination, force=args.force)
    print(f"Installed VibeDeck Project OS to {installed}")
    print(
        "Next: add templates/AGENTS.snippet.md to the target repository's AGENTS.md"
    )


if __name__ == "__main__":
    main()
