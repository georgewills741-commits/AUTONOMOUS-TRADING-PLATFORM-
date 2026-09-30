# Verification Record — Owner Decisions 2 (CF-11, CF-12, CF-13)

> **Date:** 2026-09-30 · **Scope:** applying the owner's answers ([owner decisions 2](../handoffs/owner-decisions-02-cf-11-to-cf-13.md)) through [DEC-021](../decisions/DEC-021-kill-switch-recovery.md), [DEC-022](../decisions/DEC-022-restart-recovery-sequence.md), and [DEC-023](../decisions/DEC-023-autonomous-canary-approval.md). Documentation only.
>
> **Result: VERIFIED.** All three conflicts are resolved as the owner decided. No open questions or findings remain.

## Pass 1 — Were the answers captured correctly?

| Check | Result |
|---|---|
| Answers stored verbatim | PASS: the three text blocks in the historical record compared equal to the answers as received |
| Answers reached requirement text | PASS: 124 units checked (sentences, list items, flow steps). 106 appear verbatim in the new requirement text. The rest were reviewed by hand: grammatical person ("verify" → "the platform must verify"), answer titles and rationale kept in the decision records, and "every recovery step" made specific as "every restart recovery step" |
| Modal strength kept | PASS after fix (below) |
| Nothing silently removed from replaced requirements | PASS: RSK-009's activation rule and AI limits carried into RSK-025; REC-011's "partially safe → restricted operation" carried into REC-016 |
| Existing requirements unchanged except by explicit replacement | PASS: of 378 prior lines, exactly 3 changed, class field only (RSK-009, REC-007, REC-011 → DEPRECATED / REPLACED); no ID missing; no wording changed |

**Defect found and fixed:** in the first draft, three of the owner's "must" statements were weakened to plain statements ("recovery is progressive", "remains in SAFE MODE", "enters NO-TRADE / SAFE MODE"). "Must" was restored in RSK-023, RSK-024, and REC-016 before commit.

## Pass 2 — Is it in the right place?

| Check | Result |
|---|---|
| New requirements in their owners' specifications | PASS: RSK-021 to RSK-025 (Risk Engine), REC-014 to REC-018 (Recovery and Reconciliation), AUD-008 and AUD-009 (Audit), STR-019 to STR-022 (Strategy Management) |
| No new system invented | PASS: the owner-named Governance and Readiness Engine is registered as a component of Strategy Management (SYS-14), which already owns promotion and canary readiness |
| IDs, references, links, index | PASS: 394 requirements, 23 decisions, 33 systems, 64 register entries (all resolved) |
| Active requirements that cite a replaced ID have a note resolving it | PASS after fix: RSK-020, REC-013, HLT-012 had notes; a note was added for PFC-008 |
| Values register | PASS: V-24 to V-29 added (policy parameters for recovery and approval); 29 entries |

## Pass 3 — Does everything still fit together?

| Check | Result |
|---|---|
| Earlier historical records (constitution, Part 1, OC-1) unchanged | PASS |
| Recovery requirements consistent with each other | PASS: REC-002 (§71), REC-012 (failure handling), REC-013 (lease acquired first, re-verified before authorizing resumption), REC-015 to REC-018, RSK-023 |
| Project-state figures match the repository | PASS after fix: a draft said 15 new requirements; the count is **16** |
| Only Markdown in the repository | PASS |
