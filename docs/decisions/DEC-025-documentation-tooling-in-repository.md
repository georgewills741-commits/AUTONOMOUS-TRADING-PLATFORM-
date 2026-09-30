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

## Consequences

- The first increment of ARCH-032 exists, for documentation only. It does not check code, schemas, interfaces, or tests, because none exist yet.
- After any change to a specification, run `python3 tools/docs/build_index.py` and commit the regenerated files with the change.
