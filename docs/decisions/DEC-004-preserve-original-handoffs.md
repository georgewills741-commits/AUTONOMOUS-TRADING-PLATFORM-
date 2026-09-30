# DEC-004 — Keep each received handoff verbatim as a HISTORICAL record

- **Status:** PROPOSED (in effect provisionally)
- **Date:** 2026-09-30
- **Affects:** `docs/handoffs/`

## Context

Constitution Rule 27: preserve the original handoff as a clearly labelled historical source, not a competing source of truth. Handoff §00 item 7: do not simply put the whole handoff into one giant Markdown file, meaning as the working specification.

## Decision

- Each handoff part is stored once in `docs/handoffs/`, converted to Markdown with its wording unchanged. A script checks that the text matches the received text line for line.
- Each file starts with a HISTORICAL banner stating that it is not an active source of truth and linking to [handoff coverage](../traceability/handoff-coverage.md), which shows where each section's content now lives.
- The handoff's section numbers (§00–§103 for Part 1) are the source references used in every requirement line.

## Consequences

- Traceability runs from every requirement back to handoff text.
- If the canonical documents and the historical handoff ever disagree, the canonical documents win. The disagreement must be explained by a decision record.
