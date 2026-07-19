---
name: project-os
description: Manage an agentic software project through a durable operating system for requirements, change requests, decisions, priorities, QA, security, privacy, deployment, status history, and feedback intake. Use when starting or resuming a project, when the user sends slash-style commands such as /log, /next, /urgent, /decision, /os-status, /dashboard, /resume, or /help, or when work risks becoming scattered across chats and files.
---

# Project OS

Treat short slash-style messages as commands even when the client does not list
them in its native slash menu. Read [commands.md](references/commands.md) when a
command is used.

## Establish control

1. Read repository instructions and existing Markdown requirement/status files.
2. Select one canonical control file, preferring `PROJECT_CONTROL.md`.
3. Select one append-only history file, preferring `STATUS.md`.
4. Create missing files with `scripts/bootstrap_project_os.py`; never overwrite
   existing files.
5. Consolidate scattered requirements into the canonical file only when the user
   authorizes consolidation or implementation.

## Process every request

1. Classify it as decision, change request, defect, QA finding, security/privacy
   control, deployment/operations work, research, or deferred idea.
2. Assign a stable ID within the project's existing scheme.
3. Record source/date, outcome, priority, acceptance, dependencies, risks, and
   implementation/QA status.
4. Use impact ordering: safety, privacy, security, data integrity, billing,
   authentication, production availability, then usability and features.
5. Continue active work for `/log` and `/next`; interrupt only for `/urgent` or a
   newly discovered P0.
6. Append material changes and tests to the history file.
7. Keep live dashboards derived from the canonical control file; do not maintain a
   second conflicting backlog.

## Communicate

- Acknowledge captured feedback in one short line.
- State whether it interrupts current work.
- For `/os-status`, report done, in progress, blocked, next, and decisions needed.
- For `/help`, show the compact command table from the reference.
- Never claim a native UI slash command was installed when only text-command
  handling is available.

## Complete work

Meet acceptance criteria, run proportionate tests, update control/history, reconcile
dashboard counts, and follow the repository's Git workflow.
