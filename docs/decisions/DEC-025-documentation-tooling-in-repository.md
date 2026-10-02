# DEC-025 — Keep the documentation generator and checker in the repository

- **Status:** ACCEPTED (builder decision; the owner may override)
- **Date:** 2026-09-30
- **Relates to:** ARCH-030, ARCH-032, ARCH-033 (Part 2 §173, §175, §179); constitution Rules 3, 53, 71, 227

## Context

The [requirements registry](../requirements/registry.md) and the handoff coverage tables are generated from the specifications. Until now the script that generates and checks them existed only in the builder's temporary workspace. The registry itself says it must be rebuilt with the specifications, so a new session could not rebuild or check it. That is a project-continuity gap (constitution Rules 53 and 227). Part 2 also asks for an eventual consistency system (ARCH-032) and change-impact identification (ARCH-033).

## Decision

The generator and checker live in [`tools/docs/`](../../tools/docs/README.md):

- It uses Python's standard library only (Python is the project language, [DEC-009](DEC-009-technology-stack.md)), so it adds no new dependency.
- It is documentation tooling, not platform code. It reads Markdown under `docs/` and writes three generated files:
  - the registry;
  - the Part 1 coverage;
  - the Part 2 reconciliation's generated part.
- Its checks:
  - requirement line format, known classes and prefixes, unique and sequential IDs;
  - every requirement, finding, decision, and system ID referenced anywhere is defined;
  - every relative link resolves;
  - every Part 1 section and every Part 2 section is accounted for;
  - every ID in the Part 2 mapping exists.

`tools/` holds project tooling only. It is not the product's source tree, which is not created until implementation is approved.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **Keeping the generator and checker outside the repository,** in the builder's temporary workspace, as until then: not taken. A new session could not rebuild or check the generated files, which is a continuity gap (constitution Rules 53 and 227; Context). The [Part 1 verification record](../traceability/part-1-verification.md) gives why the checks were first kept out: adding the tooling "would introduce Python as a project dependency without approval (constitution Rule 104)", and committing it was RECOMMENDED — NOT YET APPROVED. By this decision, DEC-009 had chosen Python, so the tooling adds no new dependency (Decision above).

## Consequences

- The first increment of ARCH-032 exists, for documentation only. It does not check code, schemas, interfaces, or tests, because none exist yet.
- After any change to a specification, run `python3 tools/docs/build_index.py` and commit the regenerated files with the change.
