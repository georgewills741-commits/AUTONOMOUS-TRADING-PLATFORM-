# CLAUDE.md

Instructions for Claude Code sessions working in this repository.

## Governing rules

All work in this repository is governed by the Claude Code Builder Constitution. It is imported below so it loads in full at the start of every session. That file is the single canonical copy: do not restate or summarize its rules anywhere else.

@docs/builder/claude-code-builder-constitution.md

The owner's checkpoint, version-control, and three-stage verification rule is also imported. It applies together with the constitution, and wins where it is stricter ([DEC-032](docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)). Every change passes all three verification gates before its checkpoint commit.

@docs/builder/checkpoint-and-verification-rule.md

## Where to start

The current stage, blockers, and next approved step are recorded in [`docs/project-state.md`](docs/project-state.md). Read it first (Constitution Rule 51) and update it after any major piece of work (Rule 174).

Every document is listed in [`docs/README.md`](docs/README.md). Requirement text lives only in its owning specification; see [`docs/requirements/README.md`](docs/requirements/README.md) before adding or changing one.

After changing any document under `docs/`, run `python3 tools/docs/build_index.py`. It regenerates the requirements registry and the coverage tables and checks every reference and link ([`tools/docs/README.md`](tools/docs/README.md)). Commit the regenerated files with the change.
