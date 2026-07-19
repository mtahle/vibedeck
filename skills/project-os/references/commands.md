# Project OS commands

| Command | Meaning | Interrupt current work? |
| --- | --- | --- |
| `/log <idea>` | Capture as an unreviewed change request or note with a stable ID. | No |
| `/next <feedback>` | Capture and review immediately after the current safe step. | No |
| `/urgent <issue>` | Triage now for material safety, security, privacy, data, financial, authentication, or production impact. | Yes |
| `/decision <choice>` | Record an explicit owner decision; reconcile conflicts. | Only if it changes active work |
| `/os-status` | Summarize done, active, blocked, next, and decisions needed. | No |
| `/dashboard` | Reconcile the canonical register and report or open its dashboard. | No |
| `/resume` | Resume the highest-priority unfinished authorized work. | No |
| `/help` | Show this command list. | No |

Uppercase phrases remain aliases:

- `LOG ONLY:` → `/log`
- `NEXT:` or `REVIEW NEXT:` → `/next`
- `URGENT:` → `/urgent`
- `DECISION:` → `/decision`
- `STATUS:` → `/os-status`

If a project has no control files, initialize them before recording the first
command. Do not overwrite established project naming or ID conventions.
