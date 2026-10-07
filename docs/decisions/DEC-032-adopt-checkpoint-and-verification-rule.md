# DEC-032 — Adopt the owner's checkpoint, version-control, and three-stage verification rule

- **Status:** ACCEPTED
- **Later changes:** Code exists since Stage 1's checkpoint A (2026-10-06), so the reading of "tests where applicable" below now includes the code's tests and checks; what each gate covers is stated in [DEC-039](DEC-039-adopt-quality-and-correction-directive.md), decision 2.
- **Date:** 2026-09-30
- **Decided by:** project owner (rule sent with Handoff Part 3); the reading notes below are the builder's
- **Rule text:** [`docs/builder/checkpoint-and-verification-rule.md`](../builder/checkpoint-and-verification-rule.md) (verbatim, ACTIVE)

## Decision

The owner's rule becomes an active builder rule, loaded in every session by `CLAUDE.md` next to the [builder constitution](../builder/claude-code-builder-constitution.md). Both apply. Where the rule is stricter, it wins:

- **Scope of the three passes.** The constitution requires three passes for every *major stage* (Rules 118–122). The owner's rule requires all three gates for *everything* built, modified, or approved, documentation changes included.
- **Checkpoints.** Work → verify → audit → checkpoint commit → push. Commits are made only after the three gates pass, never file by file.
- **Completion report.** Every stage ends with the owner's 11-point report: what was done, files, requirements, the three verification results, checks, remaining issues, commit hash, push status, and the next stage.
- **No silent dropping.** It restates constitution Rules 56, 177, and 220, and adds nothing that conflicts with them.

## Reading notes (builder)

| Phrase in the rule | Reading |
|---|---|
| "Global Game Constitution equivalent / platform constitution and system rules" | For this project: the platform principles index (ARCH-028, in the [platform overview](../product/platform-overview.md)) and the [System Rules Register](../requirements/system-rules-register.md) (P3§468) |
| "tests where applicable" | Until code exists, the tests are the documentation checks: `tools/docs/build_index.py`, the requirement comparison against the previous commit (`tools/docs/compare_requirements.py`), and the round-trip checks for preserved sources |
| "use an independent reviewer/checker or a separate verification pass" | Verification 3 uses an independent reviewer (a separate review agent that did not write the change) where possible, plus the builder's own separate pass |
| "accidentally ignored files" | `git status --ignored` is part of the repository completeness check |
| "checkpoint documentation" | [Project state](../project-state.md) keeps a checkpoint log: commit, what it contains, and its verification record |

## Alternatives considered

None on the decision itself: the rule is the owner's instruction. For the reading notes, the builder considered running Verification 3 only as its own separate pass; the rule asks for an independent reviewer where possible, so both are used.

## Consequences

- Every checkpoint from now on is recorded with its three gate results in a verification record under `docs/traceability/` and in the project state's checkpoint log.
- The rule governs Claude's work only. It does not change any platform requirement.
