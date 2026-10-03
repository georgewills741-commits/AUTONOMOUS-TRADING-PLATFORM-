# DEC-010 — Canonical pre-trade decision flow

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Later changes:** REC-007 (CF-09) is superseded by [DEC-022](DEC-022-restart-recovery-sequence.md). Part 2 did not supply the interface contracts this record expected from it; they are produced when each stage is planned (ARCH-025; [DEC-024](DEC-024-part-2-reconciliation.md), Consequences).
- **Date:** 2026-09-30
- **Resolves:** CF-01, CF-02, CF-03, CF-09, DUP-19

## Context

Part 1 describes the trade path in five places (§08, §19, §21, §70, §77, §94) with different orders and different placements of AI.

## Decision

The single canonical runtime order for opening a position:

```text
MARKET EVENT → data validation (freshness, MKD-006)
  → opportunity detection (OPP)
  → strategy evaluation, proposes size (DIR / XAR / TAR)
  → [AI reasoning — only if routed; never on arbitrage paths]           (CF-02)
  → true net-profit evaluation (TNP)
  → capital request → Global Capital Authority: availability + allocation
  → Risk Engine: authorization + final size (never increased)            (CF-01, DUP-19)
  → Global Capital Authority: reservation                                (CF-03)
  → Execution Engine: stale-decision revalidation (EXE-004) → order
  → fills → commit / release → reconciliation → ledger → portfolio
```

1. **CF-01:** the §19 order (capital authority → risk check → reservation) is the runtime order. §94 is a build-dependency chain. A risk rejection means nothing is reserved (CAP-016).
2. **CF-02:** AI, when used, sits after strategy evaluation and before the deterministic capital and risk steps (§70, §66), so risk always has the final word. §08's "AI only when justified" is a condition on *whether* AI runs, not on where it sits. Arbitrage paths never use AI ([DEC-013](DEC-013-ai-organization.md)).
3. **CF-03:** capital reservation is part of the latency-sensitive path. §77 lists stages, not every control (CAP-021). Reservation must meet the latency targets (PERF-007).
4. **DUP-19:** the strategy proposes a size using Quantitative Engine calculations. The Risk Engine sets the final size as the smallest of the proposal, the risk limits, and the allocated capital. It may reduce a size but never increase it (RSK-011).
5. **CF-09:** database integrity is verified *before* internal state is loaded from it (REC-007).

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **CF-01, the risk check before the capital authority** (§94's order: strategy → risk → capital → execution): not the runtime order. §94 is read as a build-dependency chain, as CF-01's proposal said. In the chosen order the Risk Engine still authorizes before anything is reserved.
- **CF-02, AI after the risk and capital steps** (a literal reading of §08): not taken, so risk always has the final word. §08's "AI only when justified" is read as a condition on whether AI runs.
- **CF-03, a latency-sensitive path without capital reservation** (a literal reading of §77): not taken. It would allow orders without a reservation, against CAP-003 and CAP-004 (CF-03's impact).
- **CF-09, §71's order as written** (load verified internal state, then verify the database), **or CF-09's proposed reading of it** (load the last checkpoint verified before the interruption): not taken; REC-007 verifies the database first. REC-007 was later replaced by the owner's staged recovery ([DEC-022](DEC-022-restart-recovery-sequence.md)), which loads persisted state first, as untrusted context.
- **DUP-19:** the register's proposal (the Quantitative Engine computes, the strategy proposes, the Risk Engine enforces limits) was adopted; no other option was recorded.

## Consequences

This sequence is the reference for interface contracts in Part 2 and for the CORE TRADING FOUNDATION stage.
