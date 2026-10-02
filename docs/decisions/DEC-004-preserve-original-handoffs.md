# DEC-004 — Keep each received handoff verbatim as a HISTORICAL record

- **Status:** ACCEPTED (delegated, 2026-09-30: accepted under the owner's instruction to resolve all open items; first recorded as PROPOSED)
- **Date:** 2026-09-30
- **Affects:** `docs/handoffs/`

## Context

Constitution Rule 27: preserve the original handoff as a clearly labelled historical source, not a competing source of truth. Handoff §00 item 7: do not simply put the whole handoff into one giant Markdown file, meaning as the working specification.

## Decision

- Each handoff part is stored once in `docs/handoffs/`, converted to Markdown with its wording unchanged. A script checks that the text matches the received text line for line.
- Each file starts with a HISTORICAL banner stating that it is not an active source of truth and linking to [handoff coverage](../traceability/handoff-coverage.md), which shows where each section's content now lives.
- The handoff's section numbers (§00–§103 for Part 1) are the source references used in every requirement line.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **The received handoff itself as the working specification, kept as one large Markdown file:** ruled out by handoff §00 item 7 (Context) and constitution Rule 22. The handoff is kept only as a HISTORICAL record; the owning specifications are the working knowledge base.

## Consequences

- Traceability runs from every requirement back to handoff text.
- If the canonical documents and the historical handoff ever disagree, the canonical documents win. The disagreement must be explained by a decision record.
