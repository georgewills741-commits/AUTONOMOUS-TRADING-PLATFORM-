# Project State

The single record of where this project currently stands (Constitution Rules 50, 172). Update it after every major piece of work. If it disagrees with the repository, the repository wins and this file gets corrected (Rule 52).

**Last updated:** 2026-09-30

## Current stage

**Pre-initialization.** The builder constitution has been adopted. The master handoff has not been received, so no requirements, architecture, system registry, or roadmap exist yet.

| Gate | Status |
|---|---|
| Builder constitution | ADOPTED — [`docs/builder/claude-code-builder-constitution.md`](builder/claude-code-builder-constitution.md) |
| Master handoff | NOT RECEIVED |
| Handoff initialization (Constitution Part XXII, Phases A–N) | NOT STARTED |
| Product implementation | NOT STARTED — requires explicit user approval after initialization is verified (Part XXIII) |

## Current objective

Receive the master handoff and carry out the initial handoff procedure (Constitution Part XXII).

## Completed work

- Repository inspected: a single prior commit ("Initial commit") containing only `README.md` with the repository name. Treated as an empty repository (Rule 5).
- Builder constitution persisted at `docs/builder/claude-code-builder-constitution.md`. Converted from plain text to Markdown; a script check confirmed the wording matches the received text line for line, with 56 parts, rules 1–235, and 50 non-negotiable rules all present in sequence.
- `CLAUDE.md` created so every Claude Code session loads the constitution.
- This project-state file created.
- `README.md` extended with pointers to the above.

## In-progress work

None.

## Blockers

| Problem | Impact | Required resolution |
|---|---|---|
| Master handoff not yet provided | Requirements, architecture, repository structure, and roadmap cannot be derived (Rule 16) | Project owner supplies the master handoff |

## Open questions

None recorded yet. A dedicated open-question register will be set up during handoff initialization.

## Recent decisions

Builder decisions made while persisting the constitution. Status: PROPOSED — the project owner may change any of them.

| Decision | Reason |
|---|---|
| Constitution stored under `docs/builder/`, apart from future product documentation | Builder process rules must not be confused with the product's own governance and risk rules, which will come from the handoff |
| `CLAUDE.md` imports the full constitution rather than summarizing it | One source of truth (Rule 42); a summary would be a second copy that drifts |
| Project state kept in `docs/project-state.md` | Rule 50 requires persistent state whatever the architecture turns out to be; kept out of the repository root (Rule 219) |
| No other directories created | Structure must be derived from the handoff, not pre-scaffolded (Rules 9, 16) |

## Recent changes

- 2026-09-30 — Adopted the builder constitution; created `CLAUDE.md` and this file; updated `README.md`.

## Next approved step

Receive the master handoff, then perform Constitution Part XXII Phases A–N, ending at the stop gate (Phase M) and waiting for explicit approval (Phase N).
