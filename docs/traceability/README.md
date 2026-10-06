# Traceability and Verification Records

> **Status:** ACTIVE — 2026-10-01. Lists the traceability and verification records, and sets the format every verification record follows: the format the master execution constitution asks the verification documentation to establish (§21, §22, §142 to §145), under the owner's checkpoint rule ([DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)) and [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md). The three gates themselves, and what each covers today, are defined in DEC-033.

## Records

| Record | What it traces or verifies |
|---|---|
| [Handoff coverage (Part 1)](handoff-coverage.md) | Every Part 1 section → canonical location (generated, with hand-written §100 and §102 tables) |
| [Part 2 reconciliation](part-2-reconciliation.md) · [Part 3 reconciliation](part-3-reconciliation.md) | Every Part 2 and Part 3 section → requirement or disposition |
| [Part 1 verification](part-1-verification.md) | Handoff Part 1 documented |
| [Resolution verification](resolution-verification.md) | Part 1 open items resolved (DEC-006 to DEC-018) |
| [Owner correction 1 verification](owner-correction-01-verification.md) | DEC-019, DEC-020 |
| [Owner decisions 2 verification](owner-decisions-02-verification.md) | DEC-021 to DEC-023 |
| [Part 2 verification](part-2-verification.md) | Handoff Part 2 integrated (DEC-024, DEC-025) |
| [Owner decisions 3 verification](owner-decisions-03-verification.md) | DEC-026 to DEC-030 |
| [Part 3 verification](part-3-verification.md) | Handoff Part 3 integrated; checkpoint rule adopted (DEC-031, DEC-032) |
| [Integrity verification 2026-10-01](integrity-verification-2026-10-01.md) | Repository integrity check requested by the owner |
| [Governance adoption verification](governance-adoption-verification.md) | Master execution constitution and the owner's directive adopted (DEC-033, DEC-034) |
| [Owner decisions 4 verification](owner-decisions-04-verification.md) | Owner decisions on the Part 3 findings applied; Part 3 approved (DEC-035) |
| [TC-08 verification](tc-08-alternatives-verification.md) | "Alternatives considered" added to DEC-001 to DEC-030, where sourced (TC-08, DEC-035) |
| [Master knowledge-base audit](master-knowledge-base-audit-2026-10-02.md) | The complete documentation review (handoff §101, P2§329), at the owner's request of 2026-10-02: verdict, findings, consistency matrix, human review package; accepted by the owner (DEC-036) |
| [Owner decisions 5 verification](owner-decisions-05-verification.md) | Owner decisions on the audit findings applied; documentation review accepted; Stage 1 planning authorized (DEC-036) |
| [Stage 1 plan verification](stage-01-plan-verification.md) | The [Stage 1 plan](../roadmap/stage-01-foundation-plan.md) written for the owner's approval; approved (DEC-038) |
| [Final decision checkpoint 2026-10-05](final-decision-checkpoint-2026-10-05.md) | The owner's final human-decision, knowledge-base, consistency, and repository checkpoint: every open or deferred item classified, every owner decision verified against the owner's answers; DEC-037, DEC-038 |

Which commit each record belongs to is in the [project state](../project-state.md)'s checkpoint log.

## Verification record (every checkpoint)

One record per checkpoint commit, in this directory. It contains:

- **Identity:** date; stage, or the documentation round before Stage 1; the commit the work starts from. A commit cannot contain its own hash, so the record's own commit is entered in the checkpoint log by the next checkpoint.
- **Scope:** what changed (files, requirements added, removed, or changed), and what was out of scope.
- **Checks:** every test and check run, as a command another engineer or a fresh session can repeat (§22), with its result. A check that cannot be a command is written as WHAT was checked, HOW, the EXPECTED RESULT, and the ACTUAL RESULT.
- **Gates:** the result of Verification 1, 2, and 3 (DEC-033), each with its evidence. Gate 3 names the independent reviewer (or why none was possible) and lists its findings, each with its fix, and the builder's own separate pass.
- **Failures and fixes:** every failure found, its cause, the fix, and the re-run that passed (§19).
- **Final status and remaining issues:** PASS only when all three gates pass; known limitations and open items named.
- **Environment:** tool versions used for the checks.

## Stage record (§142), from Stage 1

Each roadmap stage gets one record, created when the stage starts and updated as it runs: stage ID; purpose; dependencies; requirements; systems affected; files; implementation status; test status; Verification 1, 2, and 3; security status; performance status; documentation status; traceability status; Git commit; blockers; next stage.

It ends with the **stage transition checklist** of §152, where each item links to its evidence: a ticked box without evidence does not count (§144).

## Stage completion certificate (§143)

Written at the end of the stage record, and only after every gate passed: stage; version or commit; the three verifications passed; tests passed; known limitations; documentation updated; traceability updated; remaining future work; approved to proceed. Where the roadmap or the owner requires human review, "approved to proceed" records the owner's approval (§156, §157), never the builder's.

## Verification matrix (§145)

Requirement → system → implementation → test → verification → status → evidence → commit. The [requirements registry](../requirements/registry.md) already gives requirement → system → specification → stage, and the [System Rules Register](../requirements/system-rules-register.md) gives rule → enforcement → planned verification. The implementation, test, and evidence columns are added when Stage 1 produces the first code (ARCH-030, ARCH-031, ARCH-040); until then they would be empty, so they are not created.
