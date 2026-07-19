#!/usr/bin/env python3
"""Create minimal VibeDeck control files without overwriting project data."""

import argparse
from datetime import date
from pathlib import Path


CONTROL = """# Project control

Last reconciled: {today}

## Decisions

| ID | Source/date | Decision | Status |
| --- | --- | --- | --- |

## Change requests

| ID | Priority | Outcome | Acceptance | Dependencies/risks | Status |
| --- | --- | --- | --- | --- | --- |

## QA, security, and privacy

| ID | Priority | Control or finding | Acceptance | Status |
| --- | --- | --- | --- | --- |

## Operations and deployment

| ID | Priority | Requirement | Acceptance | Status |
| --- | --- | --- | --- | --- |

## Deferred ideas

| ID | Idea | Why deferred | Revisit trigger |
| --- | --- | --- | --- |
"""

STATUS = """# Status history

- `{today}` — Initialized VibeDeck control and append-only status history.
"""


def bootstrap(root: Path, today: date | None = None) -> list[str]:
    root = root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    current_date = today or date.today()
    created = []
    for name, content in (
        ("PROJECT_CONTROL.md", CONTROL),
        ("STATUS.md", STATUS),
    ):
        target = root / name
        if target.exists():
            continue
        target.write_text(
            content.format(today=current_date.isoformat()),
            encoding="utf-8",
        )
        created.append(name)
    return created


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    created = bootstrap(Path(args.path))
    if created:
        print("Created: " + ", ".join(created))
    else:
        print("VibeDeck files already exist.")


if __name__ == "__main__":
    main()
