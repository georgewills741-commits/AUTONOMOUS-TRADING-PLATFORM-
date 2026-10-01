# IMPORTANT — MANDATORY CHECKPOINT, VERSION CONTROL & 3-STAGE VERIFICATION RULE

> **Status:** ACTIVE — builder operating rule set by the project owner on 2026-09-30, sent together with Handoff Part 3. Adopted by [DEC-032](../decisions/DEC-032-adopt-checkpoint-and-verification-rule.md) and loaded into every Claude Code session through `CLAUDE.md`, alongside the [builder constitution](claude-code-builder-constitution.md). Where this rule is stricter than the constitution, this rule applies.
>
> **Formatting note:** converted from plain text to Markdown (headings, paragraph breaks). No wording was added, removed, or changed; the `====` separator lines around headings were rendered as Markdown headings. The two empty code blocks near the end are reproduced as received.

Before you begin implementing anything, treat the repository as the single source of truth for the entire Autonomous Trading Platform.

EVERYTHING MUST BE PRESERVED IN THE REPOSITORY.

Do not allow architecture decisions, requirements, system rules, safety rules, specifications, workflows, roadmaps, implementation decisions, or other approved project knowledge to exist only in chat/context.

For every completed piece of work:

1. Make sure the actual implementation is saved in the correct repository files.
2. Make sure all relevant documentation/specifications are updated.
3. Make sure no approved requirement or decision has been silently dropped.
4. Check for duplicate, conflicting, obsolete, or contradictory definitions.
5. Check git status for untracked, modified, or accidentally ignored files that should be part of the project.
6. Make sure the repository is internally consistent.
7. Run the required tests/checks.
8. Commit the completed checkpoint with a clear commit message.
9. Push the commit to the remote repository when the remote is configured and available.
10. Never describe work as “completed” if important work exists only in the conversation and has not been captured in the repository.

## MANDATORY 3-STAGE VERIFICATION GATE

This rule applies to EVERYTHING you build, modify, or approve — not only major milestones.

Every stage, feature, subsystem, architectural change, migration, integration, safety mechanism, trading component, AI component, infrastructure component, and documentation change must pass ALL THREE verification stages before it is considered complete.

### VERIFICATION 1 — IMPLEMENTATION / FUNCTIONAL VERIFICATION

Verify that the thing actually works as intended.

Check:

- implementation correctness
- unit/integration tests where applicable
- expected inputs and outputs
- failure handling
- edge cases
- persistence/state behavior
- interfaces and dependencies
- no obvious runtime errors
- no placeholder or fake implementation presented as complete

### VERIFICATION 2 — ARCHITECTURE / CONSISTENCY VERIFICATION

Verify that the new work fits the entire platform.

Check:

- Global architecture
- existing system boundaries
- Global Game Constitution equivalent / platform constitution and system rules
- deterministic-vs-AI separation
- risk controls
- capital controls
- execution controls
- state/reconciliation rules
- exchange adapter rules
- data integrity rules
- opportunity pipeline
- strategy lifecycle
- monitoring
- recovery
- security
- existing decisions and approved requirements
- no duplicated systems
- no conflicting implementations
- no accidental changes to previously approved architecture

A feature must not be considered correct merely because its own tests pass. It must also fit the larger system.

### VERIFICATION 3 — INDEPENDENT FINAL AUDIT / REGRESSION VERIFICATION

Perform a fresh verification pass as if reviewing someone else's work.

Do not simply repeat the first two checks.

Look specifically for:

- missing requirements
- regressions
- hidden assumptions
- contradictory rules
- unsafe failure modes
- race conditions
- duplicate responsibilities
- incorrect state transitions
- security weaknesses
- risk-control bypasses
- incomplete error handling
- missing documentation
- uncommitted files
- untracked files
- accidental deletions
- incorrect configuration
- tests that pass without actually proving the required behavior

If possible, use an independent reviewer/checker or a separate verification pass rather than relying only on the same reasoning that produced the implementation.

## STRICT GATE RULE

A stage is NOT COMPLETE unless:

VERIFICATION 1 = PASS

AND

VERIFICATION 2 = PASS

AND

VERIFICATION 3 = PASS

If any verification fails:

STOP the completion process.

Record the failure.

Fix the problem.

Run the affected verification again.

Then rerun the complete three-stage gate where appropriate.

Do NOT mark the stage complete merely because the implementation exists.

Do NOT proceed to the next dependent stage while a blocking verification failure remains.

## COMMIT / CHECKPOINT RULE

Only after the required verification gate passes:

- save all changes
- update the relevant documentation
- review git diff
- review git status
- confirm no required files are missing
- commit the checkpoint
- push it to the remote repository when available

Each meaningful completed stage should have a clear, traceable commit.

Use meaningful commit messages that identify what was completed.

Never use a commit as proof that the work is correct. The three verification gates are the proof; the commit is the durable checkpoint.

## NO LOSS / NO SILENT DROPPING RULE

During consolidation, refactoring, implementation, or cleanup:

DO NOT silently remove an existing requirement, architectural decision, safety rule, feature, subsystem, or documented concept.

If something appears duplicated, contradictory, obsolete, unsafe, or unclear:

1. identify it,
2. document the conflict,
3. determine the authoritative version according to the project's governing rules,
4. preserve the decision and rationale in the repository.

Do not resolve important architectural conflicts by silently choosing one.

## RECOVERY / CONTINUITY RULE

The repository must always remain recoverable.

At every major checkpoint, another engineer/agent should be able to clone the repository and understand:

- what has been built
- what is currently working
- what has been verified
- what remains
- what architectural decisions are authoritative
- what known limitations remain
- how to continue safely

Maintain appropriate checkpoint documentation so work can resume after a crash, context loss, machine change, or agent change.

## FINAL COMPLETION REQUIREMENT

At the end of every stage, report:

1. What was implemented.
2. What files were changed.
3. What requirements/decisions were satisfied.
4. Verification 1 result.
5. Verification 2 result.
6. Verification 3 result.
7. Tests/checks performed.
8. Any remaining issues or limitations.
9. Commit hash.
10. Push status.
11. The exact next stage.

Never report “complete” when any of the three verification gates is unresolved.

This is a production-grade autonomous trading platform. Optimize for correctness, traceability, recoverability, safety, and architectural consistency — not merely speed of implementation.

One important addition

I would also tell Claude not to commit every tiny file change blindly. The rule should be:

work → verify → audit → checkpoint commit → continue.

That gives you a clean chain such as:

```

```

```
Stage 01
   ↓
Implementation
   ↓
Verification 1
   ↓
Verification 2
   ↓
Verification 3
   ↓
Repository completeness check
   ↓
Commit
   ↓
Push
   ↓
Stage 02
```

And if something fails:

```

```

```
FAIL
 ↓
Fix
 ↓
Re-verify
 ↓
3 gates PASS
 ↓
Commit
```
