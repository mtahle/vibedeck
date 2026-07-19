# VibeDeck

**A control deck for agentic software projects.**

VibeDeck gives coding agents a durable way to manage product decisions,
requirements, change requests, priorities, QA, security, privacy, deployments, and
status across many chat sessions.

It uses two deliberately boring Markdown files:

- `PROJECT_CONTROL.md` is the canonical register.
- `STATUS.md` is the append-only delivery history.

The included `project-os` Codex skill teaches agents how to keep those files useful,
while a small command language makes project intake fast:

| Command | What it does |
| --- | --- |
| `/log <idea>` | Capture an idea without interrupting active work |
| `/next <feedback>` | Capture feedback for the next safe checkpoint |
| `/urgent <issue>` | Interrupt and triage material risk |
| `/decision <choice>` | Record an explicit owner decision |
| `/os-status` | Report done, active, blocked, next, and decisions needed |
| `/dashboard` | Reconcile the canonical register/dashboard |
| `/resume` | Resume the highest-priority authorized work |
| `/help` | Show the commands |

## Why VibeDeck?

Agentic projects tend to scatter their truth across prompts, plans, issues, and
half-updated specs. VibeDeck keeps one source of truth, one audit trail, stable IDs,
explicit acceptance criteria, and risk-aware priority ordering.

It is intentionally:

- plain Markdown and Git friendly;
- independent of your application stack;
- safe to add to an existing repository;
- strict about decisions, scope, and completion evidence;
- compatible with Codex repository instructions.

## Install

Clone the repository and run:

```bash
python3 scripts/install.py
```

This installs the skill at `~/.codex/skills/project-os`. Existing installations are
left untouched unless you pass `--force`.

Then add the contents of [`templates/AGENTS.snippet.md`](templates/AGENTS.snippet.md)
to your project's `AGENTS.md`.

## Start a project

From the target repository:

```bash
python3 ~/.codex/skills/project-os/scripts/bootstrap_project_os.py .
```

The bootstrapper creates only missing control files and never overwrites existing
project data.

Ask Codex to use the `project-os` skill, or start with:

```text
/decision Ship the smallest safe vertical slice first.
/log Add an operator dashboard.
/os-status
```

## Repository layout

```text
skills/project-os/          Installable Codex skill
templates/                  Drop-in project instructions and examples
scripts/install.py          Safe local installer
tests/                      Portable behavior checks
.github/workflows/          Continuous validation
```

## Validate

```bash
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/install.py skills/project-os/scripts/bootstrap_project_os.py
```

## Design principles

1. One canonical control register; no competing backlogs.
2. One append-only status history; delivery claims need evidence.
3. Every material request gets a stable ID, priority, acceptance criteria, risks,
   dependencies, and status.
4. Safety, privacy, security, data integrity, billing, authentication, and
   availability outrank convenience.
5. Capture does not silently authorize implementation.
6. A change is done only after acceptance, verification, and reconciliation.

## License

MIT
