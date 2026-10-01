# CLAUDE.md

Instructions for Claude Code sessions working in this repository.

## Governing rules

Four builder texts govern all work in this repository. Each is imported below so it loads in full at the start of every session, and each file is the single canonical copy of its text: do not restate or summarize their rules anywhere else. They apply together; where they differ, the stricter applies. Everything built, modified, or approved, documentation included, passes all three gates of the one verification procedure of [DEC-033](docs/decisions/DEC-033-adopt-master-execution-constitution.md) before its checkpoint commit (the owner's rule, DEC-032).

The Claude Code Builder Constitution ([DEC-001](docs/decisions/DEC-001-adopt-builder-constitution.md)):

@docs/builder/claude-code-builder-constitution.md

The owner's checkpoint, version-control, and three-stage verification rule ([DEC-032](docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)):

@docs/builder/checkpoint-and-verification-rule.md

The master execution, consistency, verification and continuity constitution ([DEC-033](docs/decisions/DEC-033-adopt-master-execution-constitution.md)):

@docs/builder/master-execution-constitution.md

The owner's directive on three-level verification and platform independence ([DEC-034](docs/decisions/DEC-034-verification-and-platform-independence.md)):

@docs/builder/verification-and-platform-independence-directive.md

## Where to start

The current stage, blockers, next approved step, and continuation contract are recorded in [`docs/project-state.md`](docs/project-state.md). Read it first (Constitution Rule 51), compare it with `git status` and `git log` before continuing, and update it after any major piece of work and before a session ends (Rule 174). Verification records follow [`docs/traceability/README.md`](docs/traceability/README.md).

Every document is listed in [`docs/README.md`](docs/README.md). Requirement text lives only in its owning specification; see [`docs/requirements/README.md`](docs/requirements/README.md) before adding or changing one.

After changing any document under `docs/`, run `python3 tools/docs/build_index.py`. It regenerates the requirements registry and the coverage tables and checks every reference and link ([`tools/docs/README.md`](tools/docs/README.md)). Commit the regenerated files with the change.
