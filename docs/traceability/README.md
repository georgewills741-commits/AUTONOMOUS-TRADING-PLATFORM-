# Traceability and Verification Records

> **Status:** ACTIVE — 2026-10-01. Lists the traceability and verification records, and sets the format every verification record follows: the format the master execution constitution asks the verification documentation to establish (§21, §22, §142 to §145), under the owner's checkpoint rule ([DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)) and [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md). The three gates themselves are defined in DEC-033, and what each covers now that code exists in [DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md).

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
| [Stage 1 record](stage-01-foundation.md) | The stage record of Stage 1 (FOUNDATION), §142: status by field, checkpoints, entry-gate re-check, dependency review, machine-check runs; later the transition checklist and completion certificate |
| [Stage 1 checkpoint A verification](stage-01-checkpoint-a-verification.md) | Checkpoint A of Stage 1: the development environment (U1) and the testing foundation and machine checks (U6) |
| [Quality audit 2026-10-06](quality-audit-2026-10-06.md) | The owner's quality, consistency, verification and correction directive adopted (DEC-039) and the audit it asks for: every area inspected, the corrections made, the non-blocking findings, and what required the owner |
| [Owner decisions 7 verification](owner-decisions-07-verification.md) | The owner's answer to OQ-29 applied: a stage's features are PROPOSED until its plan is approved (DEC-040) |
| [Stage 1 checkpoint B verification](stage-01-checkpoint-b-verification.md) | Checkpoint B of Stage 1: exact amounts (U2) and the contract kernel, outcomes, and idempotency keys (U3) |
| [Foundation convergence audit 2026-10-13](foundation-convergence-audit-2026-10-13.md) | The owner's audit of whether Stage 1's verification converges (owner decisions 13): the baseline, the history of every gate, each blocking finding classified with its provenance, check 7, convergence, and the corrections of DEC-045 |
| [Owner decisions 14 and 15 verification](owner-decisions-14-15-verification.md) | The preservation of the owner's two rule sets of 2026-10-14 (DEC-046, DEC-047): the inventory of the repository and the builder's workspace, the checks, and each Gate 3 run's findings with their fixes |
| [Stage 1 mutation checks as run](stage-01-mutation-checks.md) | Evidence: the scripts of checkpoint A's check 11 and checkpoint B's check 7, exactly as they ran, so that both checks can be repeated from the repository |
| [Owner decisions 17 verification](owner-decisions-17-verification.md) | The preservation of the owner's Rule 0 and instruction to continue (DEC-048): the record format reconciled with DEC-047's decision 4, and the owner's messages named in each record; and of the owner's messages of 2026-10-20 (DEC-049), with reviewer launches that stopped before they reported named in each record |
| Gate 3 reports of the earlier records: [Part 3](part-3-verification-gate-3-reports.md) · [integrity 2026-10-01](integrity-verification-2026-10-01-gate-3-reports.md) · [governance adoption](governance-adoption-verification-gate-3-reports.md) · [owner decisions 4](owner-decisions-04-verification-gate-3-reports.md) · [TC-08](tc-08-alternatives-verification-gate-3-reports.md) · [master knowledge-base audit](master-knowledge-base-audit-2026-10-02-gate-3-reports.md) · [owner decisions 5](owner-decisions-05-verification-gate-3-reports.md) · [Stage 1 plan](stage-01-plan-verification-gate-3-reports.md) · [final decision checkpoint](final-decision-checkpoint-2026-10-05-gate-3-reports.md) · [Stage 1 record (`5ac6799`)](stage-01-foundation-gate-3-reports.md) · [quality audit](quality-audit-2026-10-06-gate-3-reports.md) · [owner decisions 7](owner-decisions-07-verification-gate-3-reports.md) · [checkpoint B record (`813fa90`, `cb3cca1`)](stage-01-checkpoint-b-verification-gate-3-reports.md) · [convergence audit](foundation-convergence-audit-2026-10-13-gate-3-reports.md) | Evidence: the reports of the independent Gate 3 reviews of the record-only changes from Part 3 to the convergence audit, each beside its record, as its reviewer gave it apart from recorded placeholders, with the launches that stopped before reporting |
| [Earlier Gate 3 reports verification](gate-3-reports-verification.md) | The commit of those reports as evidence ("Next approved step", item 2): what they cover and what they do not, the checker's rule for code blocks that holds them, and the corrections found while matching them with the records |

Which commit each record belongs to is in the [project state](../project-state.md)'s checkpoint log.

## Verification record (every checkpoint)

One record per checkpoint commit, in this directory. It contains:

- **Identity:** date; stage, or the documentation round before Stage 1; the commit the work starts from. A commit cannot contain its own hash, so the record's own commit is entered in the checkpoint log by the next checkpoint.
- **Scope:** what changed (files, requirements added, removed, or changed), and what was out of scope; and the owner's messages received after the last one the previous record names, up to the making of the copy that its last Gate 3 run reviews (or, where no copy is reviewed, its commit), each with where it is preserved, or that it is procedural; the next record names any received later ([DEC-048](../decisions/DEC-048-preserve-and-apply-rule-0.md), decision 3).
- **Checks:** every test and check run, as a command another engineer or a fresh session can repeat (§22), with its result. A check that cannot be a command is written as WHAT was checked, HOW, the EXPECTED RESULT, and the ACTUAL RESULT.
- **Gates:** the result of Verification 1, 2, and 3 (DEC-033), each with its evidence. Gate 3 names the independent reviewer (or why none was possible), the copy each run reviewed, identified by its base commit and the hash of its change, and any launch that stopped before it reported ([DEC-049](../decisions/DEC-049-preserve-owner-messages-of-2026-10-20.md), decision 3), and lists, in the record itself and for documentation changes too, each run's findings, each with an identity, its class, its severity, the provenance of a blocking one, the evidence, the fix, and its status ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 4), and the builder's own separate pass. From Stage 1's checkpoint C on ([DEC-045](../decisions/DEC-045-apply-foundation-convergence-audit.md)), each Gate 3 run also records the baseline and the severity its brief gave the reviewer; findings are numbered once per checkpoint, across runs, each saying how it stands to earlier ones; and each run counts its blocking findings and how many were reopened or caused by fixes.
- **Failures and fixes:** every failure found, its cause, the fix, and the re-run that passed (§19).
- **Final status and remaining issues:** each gate PASS or FAIL; the record's status in precise words such as those of §10 of the owner's [quality directive](../builder/quality-consistency-and-correction-directive.md) ([DEC-039](../decisions/DEC-039-adopt-quality-and-correction-directive.md)), backed by the evidence above, and never better than the gates allow: a checkpoint is complete only when all three gates pass; known limitations, non-blocking findings, and open items named.
- **Environment:** tool versions used for the checks.

## Stage record (§142), from Stage 1

Each roadmap stage gets one record, created when the stage starts and updated as it runs: stage ID; purpose; dependencies; requirements; systems affected; files; implementation status; test status; Verification 1, 2, and 3; security status; performance status; documentation status; traceability status; Git commit; blockers; next stage.

It ends with the **stage transition checklist** of §152, where each item links to its evidence: a ticked box without evidence does not count (§144).

## Stage completion certificate (§143)

Written at the end of the stage record, and only after every gate passed: stage; version or commit; the three verifications passed; tests passed; known limitations; documentation updated; traceability updated; remaining future work; approved to proceed. Where the roadmap or the owner requires human review, "approved to proceed" records the owner's approval (§156, §157), never the builder's.

## Verification matrix (§145)

Requirement → system → implementation → test → verification → status → evidence → commit. The [requirements registry](../requirements/registry.md) already gives requirement → system → specification → stage, and the [System Rules Register](../requirements/system-rules-register.md) gives rule → enforcement → planned verification. The implementation, test, and evidence columns are added by Stage 1's U7 at checkpoint D, in the generated verification matrix (ARCH-030, ARCH-031, ARCH-040; the [Stage 1 plan](../roadmap/stage-01-foundation-plan.md), D10); until then what each checkpoint delivers is recorded in the [stage record](stage-01-foundation.md).
