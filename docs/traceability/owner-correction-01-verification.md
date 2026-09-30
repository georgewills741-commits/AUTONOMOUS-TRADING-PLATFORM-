# Verification Record — Owner Correction 1 (Company-Grade Autonomous Operating Model)

> **Date:** 2026-09-30 · **Scope:** applying [OC-1](../handoffs/owner-correction-01-autonomous-operating-defaults.md) through [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md) and [DEC-020](../decisions/DEC-020-value-classification.md). Documentation only; nothing was implemented.
>
> **Result: VERIFIED.** OC-1 is fully applied. Three conflicts with established requirements (CF-11 to CF-13) are recorded and surfaced for owner review, as OC-1 item 33 requires; the requirements they concern were **not** changed.

## Pass 1 — Was the correction captured correctly?

| Check | Result |
|---|---|
| Historical copy matches the received text | PASS: 725 content lines identical; items 1–33 in sequence |
| Every OC-1 item mapped to a result | PASS: DEC-019's table maps items 1–33; every requirement ID it names exists (41) |
| Every bullet and flow step of OC-1 reached the documentation | PASS: 311 elements from items 1–29 and 32 checked. 248 appear verbatim in the new requirement text; 24 elsewhere in the canonical documents. The remaining 39 were reviewed by hand: 38 are the same content in different grammar or notation (e.g. "Stop allocation increases" → "stops allocation increases"; `→` flows written as sentences). One was a real loss and was fixed (below). Items 30, 31, and 33 are realized as the supersession table, DEC-020 with the values register, and the conflict records |
| Superseded defaults no longer described as current | PASS: text search for 5%, 14 days, 50 trades, 50 ms, 500 ms, and "operator confirmation" outside historical records, decision records, registers, and the values register finds only supersession notes, the Part 1 illustrative examples, and still-valid policy-change governance (POL-005, consistent with OC-1 item 29) |
| Earlier requirements unchanged except by explicit supersession | PASS: compared with a snapshot taken before this work. Of 337 prior requirement lines, exactly 19 changed, and only in the class field: 9 superseded (CAP-022, SEC-003, HLT-007, HLT-008, HLT-009, REC-009, STR-011, MODE-004, PERF-007) and 10 reclassified as IMPLEMENTATION CHOICE (TEC-001, TEC-004 to TEC-012). No title, source, or text changed; no ID missing |

**Defect found and fixed:** PERF-010 had shortened "SLO / SLA-like internal targets" to "SLO-like", dropping "SLA". The wording was restored.

## Pass 2 — Is it in the right place?

| Check | Result |
|---|---|
| Each new requirement lives in the owning system's specification, cites DEC-019 or DEC-020, and is indexed | PASS: 378 requirements (228 from Part 1, 150 from decisions); IDs unique and sequential; all references and links resolve |
| No requirement text outside its owning specification | PASS |
| Every DEPRECATED / REPLACED requirement names its replacement in the same document | PASS |
| Every value-bearing requirement is covered by the values register (ARCH-018) | PASS: 23 entries; none approved as a permanent hard-coded value |
| No new system invented | PASS: the emergency controller is part of the Risk Engine (SYS-09); transfer execution is in the Execution Engine (SYS-10); the execution lease is in Recovery and Reconciliation (SYS-11) |
| Every document reachable from the index or decision log | PASS: 77 documents |

## Pass 3 — Does everything still fit together?

| Check | Result |
|---|---|
| Constitution, Part 1 handoff, and OC-1 historical copy unchanged | PASS |
| `CLAUDE.md` import resolves | PASS |
| Part 1 fidelity unaffected | PASS: 1,023 Part 1 items still in requirement text; no new drops |
| Project-state figures match the repository | PASS after fix: a draft said 44 new requirements; the count is **41**. Corrected |
| Stage placement consistent (roadmap, system registry, index) | PASS |
| Only Markdown in the repository | PASS |

## Conflicts surfaced (not resolved)

| ID | Topic | Established requirement kept in force |
|---|---|---|
| CF-11 | Kill-switch reset: operator-only vs exception-based human intervention | RSK-009 |
| CF-12 | Recovery ordering: verify the database before or after loading | REC-007 (alongside REC-002, REC-011) |
| CF-13 | Lifecycle APPROVAL stage vs automatic canary | STR-001, STR-009; STR-014 applied as the owner wrote it |

Proposed resolutions are in the [findings register](../conflicts/register.md), marked RECOMMENDED — NOT YET APPROVED.
