# DEC-001 — Adopt the builder constitution and load it in every session

- **Status:** PROPOSED (in effect provisionally)
- **Date:** 2026-09-30 (made in the first session; moved here from the project-state file's decision table on the same day)
- **Affects:** every Claude Code session; `CLAUDE.md`; `docs/builder/`

## Context

The project owner supplied the Claude Code Builder Constitution before any handoff. It must bind every future session, and it must not depend on conversation memory (Rules 47, 48).

## Decision

1. Store the constitution at `docs/builder/claude-code-builder-constitution.md`, converted to Markdown with its wording unchanged (script-verified).
2. Keep it apart from product documentation (`docs/builder/`), so the builder's process rules are never confused with the product's own governance or risk rules.
3. Import it in full from `CLAUDE.md` (`@docs/builder/...`), so Claude Code loads it at the start of every session. Do not summarize it anywhere.

## Alternatives considered

- **Summary in `CLAUDE.md` with a link to the full text:** rejected. A summary is a second copy that can drift (Rules 42, 54).
- **Pointer only, asking each session to read the file:** rejected for now. It relies on each session choosing to comply.

## Consequences

- About 57K characters are loaded into every session's context. Claude Code may warn that `CLAUDE.md` is large.
- If the owner prefers, the import can be replaced with a pointer by a superseding decision.
