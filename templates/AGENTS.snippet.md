# Shared Project OS

Use the `project-os` skill for project intake, requirements, change requests,
decisions, priorities, QA, security, privacy, deployment status, and progress
dashboards.

Recognize these text commands in every project:

- `/log <idea>`: capture without interrupting active work.
- `/next <feedback>`: capture and review after the current safe step.
- `/urgent <issue>`: interrupt and triage material risk immediately.
- `/decision <choice>`: record an explicit owner decision.
- `/os-status`: report done, active, blocked, next, and decisions needed.
- `/dashboard`: reconcile the canonical register/dashboard.
- `/resume`: resume the highest-priority authorized work.
- `/help`: show the commands.

Treat `LOG ONLY:`, `NEXT:`, `REVIEW NEXT:`, `URGENT:`, `DECISION:`, and
`STATUS:` as aliases.

Prefer one canonical project-control file and one append-only status history.
Project-specific instructions should define scope, architecture, verification
commands, safety boundaries, and deferred features below this shared section.
