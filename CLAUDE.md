# CLAUDE.md

Instructions for Claude Code sessions working in this repository.

## Governing rules

Six builder texts govern all work in this repository. Each is imported below so it loads in full at the start of every session, and each file is the single canonical copy of its text: do not restate or summarize their rules anywhere else. They apply together; where they differ, the stricter applies. Everything built, modified, or approved, documentation included, passes all three gates of the one verification procedure of [DEC-033](docs/decisions/DEC-033-adopt-master-execution-constitution.md) before its checkpoint commit (the owner's rule, DEC-032); what each gate covers now that code exists is in [DEC-039](docs/decisions/DEC-039-adopt-quality-and-correction-directive.md).

The Claude Code Builder Constitution ([DEC-001](docs/decisions/DEC-001-adopt-builder-constitution.md)):

@docs/builder/claude-code-builder-constitution.md

The owner's checkpoint, version-control, and three-stage verification rule ([DEC-032](docs/decisions/DEC-032-adopt-checkpoint-and-verification-rule.md)):

@docs/builder/checkpoint-and-verification-rule.md

The master execution, consistency, verification and continuity constitution ([DEC-033](docs/decisions/DEC-033-adopt-master-execution-constitution.md)):

@docs/builder/master-execution-constitution.md

The owner's directive on three-level verification and platform independence ([DEC-034](docs/decisions/DEC-034-verification-and-platform-independence.md)):

@docs/builder/verification-and-platform-independence-directive.md

The owner's master quality, consistency, verification and correction directive ([DEC-039](docs/decisions/DEC-039-adopt-quality-and-correction-directive.md)):

@docs/builder/quality-consistency-and-correction-directive.md

The owner's canonical requirement drafting and anti-drift rules, loaded from the copy preserved under `docs/handoffs/` ([DEC-051](docs/decisions/DEC-051-adopt-requirement-drafting-and-anti-drift-rules.md)):

@docs/handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md

The owner's later rule sets are not loaded here; each stays in force through its decision record: owner decisions 10's lifecycle for temporary backups ([DEC-042](docs/decisions/DEC-042-preserve-anti-drift-rules-and-backup-instructions.md)), the lasting rules of owner decisions 13 ([DEC-045](docs/decisions/DEC-045-apply-foundation-convergence-audit.md)), owner decisions 14 ([DEC-046](docs/decisions/DEC-046-preserve-company-grade-order-and-traceability-rules.md)), owner decisions 15 ([DEC-047](docs/decisions/DEC-047-preserve-stage-transition-persistence-rules.md)), and owner decisions 17, Rule 0 ([DEC-048](docs/decisions/DEC-048-preserve-and-apply-rule-0.md)). The [owner rule sets reconciliation](docs/traceability/owner-rule-sets-reconciliation.md) shows where each of their rules is stated or applied.

## Where to start

The current stage, blockers, next approved step, and continuation contract are recorded in [`docs/project-state.md`](docs/project-state.md). Read it first (Constitution Rule 51), compare it with `git status` and `git log` before continuing, and update it after any major piece of work and before a session ends (Rule 174). Verification records follow [`docs/traceability/README.md`](docs/traceability/README.md).

How to install, check, and test the code, and the checks every code change passes, are in the [developer guide](docs/development.md).

Every document is listed in [`docs/README.md`](docs/README.md). Requirement text lives only in its owning specification; see [`docs/requirements/README.md`](docs/requirements/README.md) before adding or changing one.

After changing any document under `docs/`, run `python3 tools/docs/build_index.py`. It regenerates the requirements registry and the coverage tables and checks every reference and link ([`tools/docs/README.md`](tools/docs/README.md)). Commit the regenerated files with the change.
