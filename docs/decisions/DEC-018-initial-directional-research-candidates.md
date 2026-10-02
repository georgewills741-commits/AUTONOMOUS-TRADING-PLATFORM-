# DEC-018 — Initial directional strategy research candidates

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Date:** 2026-09-30
- **Resolves:** OQ-21

## Decision

The first directional strategies to **research** are:
- trend following, using moving-average and breakout entries with ATR-based stops;
- momentum.

Both run on liquid markets, on 1-hour and 4-hour timeframes (DIR-005).

These are research candidates, not approved strategies. Each must pass the full lifecycle (STR-001): specification, backtest, out-of-sample and walk-forward validation, robustness, paper, approval, canary.

## Why these

They use only Quantitative Engine metrics that Part 1 already lists (moving averages, ATR, momentum, volatility; QNT-002). They are well understood and testable, and they exercise the whole directional path before more complex strategies are added.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)): records with no sourced alternatives say so. Nothing is reconstructed from memory (constitution Rule 181)._

None recorded. OQ-21 listed no options, and the record names no other candidate strategies, so none are listed here.
