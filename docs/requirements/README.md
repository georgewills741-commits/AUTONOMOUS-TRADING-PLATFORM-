# Requirements: Conventions

> Rules for how requirements are written, identified, classified, and indexed. The reasoning is in [DEC-003](../decisions/DEC-003-requirement-ids-and-classification.md).

## Where requirements live

- **Requirement text** lives in exactly one place: the specification that owns it. Specifications are listed in the [system registry](../architecture/system-registry.md).
- **The [registry](registry.md)** is an index: ID, title, class, handoff source, owner, canonical document, and default stage (the [roadmap](../roadmap/roadmap.md) is authoritative for individual placement). It never restates requirement text.
- **Coverage** (which handoff sections produced which requirements) is in [handoff coverage](../traceability/handoff-coverage.md) for Part 1, the [Part 2 reconciliation](../traceability/part-2-reconciliation.md) for Part 2, and the [Part 3 reconciliation](../traceability/part-3-reconciliation.md) for Part 3.
- **System rules** are indexed in the [System Rules Register](system-rules-register.md) (SR-nn). It points to requirements and never restates them.
- **Generation:** the registry and the coverage tables are generated and checked by [`tools/docs/build_index.py`](../../tools/docs/README.md) ([DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md)).

## Line format

Every requirement in a specification is one Markdown list item:

```text
- **XYZ-001** Short title · CLASS · §NN — Requirement text, keeping the handoff's own wording and modal verbs.
```

The parts are: ID · short title · class · source — requirement text. The source is a Part 1 handoff section (`§NN`), a Part 2 handoff section (`P2§N`), a Part 3 handoff section (`P3§N`), or a decision record (`DEC-NNN`) for requirements created by a decision. Several sections may be cited, separated by commas. Requirements from a decision sit under a "Decisions applied" heading in the owning specification.

## IDs

`PREFIX-NNN`. The prefix identifies the owner ([system registry](../architecture/system-registry.md) lists every prefix). IDs are permanent: never reused or renumbered. A replaced requirement is marked DEPRECATED / REPLACED and points to its replacement.

## Classes (handoff §96, ARCH-015)

| Class | Used for |
|---|---|
| CONFIRMED REQUIREMENT | A required capability or behavior stated by the handoff |
| CONFIRMED ARCHITECTURAL PRINCIPLE | A rule about structure, ownership, separation, or flow |
| CONSTRAINT | A prohibition or limit |
| SYSTEM REQUIREMENT | Responsibilities or capabilities of a named system |
| PROPOSED | Something offered as potential, not yet approved |
| FUTURE | Deliberately deferred; recorded but not built (e.g. CUS-001, CUS-002) |
| PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION | Discussed before; not a production requirement until confirmed |
| OPEN QUESTION | Kept in the [open-question register](../open-questions/register.md) as OQ-nn |
| TECHNICAL CONCERN | Kept in the [open-question register](../open-questions/register.md) as TC-nn |
| DEPRECATED / REPLACED | Superseded; kept for traceability. The replacing requirement is named next to it (e.g. EXA-002 → EXA-005, AGT-001 → AGT-016, STR-011 → STR-013 to STR-018) |
| IMPLEMENTATION CHOICE | A technology or mechanism choice rather than a platform behavior (added by [DEC-020](../decisions/DEC-020-value-classification.md), OC-1 item 31) |

The interpretation of CONFIRMED REQUIREMENT vs SYSTEM REQUIREMENT in DEC-003 was accepted (OQ-23 resolved).

**Values** such as percentages, durations, counts, latencies, and versions are classified separately in the [values register](values-register.md): DEFAULT, DESIGN TARGET, POLICY-CONTROLLED PARAMETER, HARD LIMIT, IMPLEMENTATION CHOICE, or OBSERVED (ARCH-018). None is a permanent hard-coded requirement unless the owner explicitly approves it.

Two rules always apply:

- Requirement text keeps the handoff's modal verb. "Should" stays "should", and "may include" lists stay indicative.
- A classification never changes silently (§96). A change needs a decision record.

## Status

All requirements are **DOCUMENTED**: recorded, not implemented, not verified. When implementation is approved, the registry gains implementation, test, and verification columns (constitution Rule 184).

## Adding or changing a requirement

1. Add or edit the line in the owning specification. Search first for an existing equivalent (constitution Rule 37).
2. Do not edit the [registry](registry.md) by hand; it is generated.
3. Run `python3 tools/docs/build_index.py`: it rebuilds the registry and coverage. For a Part 2 or Part 3 source, also fill the hand-written column of the [Part 2 reconciliation](../traceability/part-2-reconciliation.md) or the [Part 3 reconciliation](../traceability/part-3-reconciliation.md) if the section's disposition changes. `python3 tools/docs/compare_requirements.py` then lists every requirement added, removed, reclassified, or reworded since the last commit; check that each one was intended. Cite the decision record if the source is a decision.
4. Record any decision, conflict, or open question in the matching register.
5. Add any concrete value to the [values register](values-register.md) with its classification.
