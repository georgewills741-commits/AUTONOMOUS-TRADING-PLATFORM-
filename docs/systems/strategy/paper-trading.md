# Paper Trading

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-16 · **Category:** shared infrastructure · **Roadmap stage:** DIRECTIONAL TRADING, although it covers arbitrage too (PAP-002, CF-05) · **Sources:** §32

Canonical definition of paper trading. PAPER is both a platform [operating mode](../../product/operating-modes.md) (MODE-001) and a [strategy lifecycle](strategy-management.md) stage (STR-001). This document defines the paper-trading capability used by both.

## Requirements

- **PAP-001** Production architecture, realistically · CONFIRMED REQUIREMENT · §32 — Paper trading should use the production architecture as realistically as practical.
- **PAP-002** What paper trading accounts for · SYSTEM REQUIREMENT · §32 — It should account for: fees; spread; slippage; liquidity; latency; partial fills; rejections; position management; risk; capital reservation; portfolio interaction; opportunity competition; directional trading; cross-exchange arbitrage; triangular arbitrage.

## Boundary (§92)

- **Uses:** the production Risk Engine, Global Capital Authority, Portfolio, and Execution paths with simulated capital (PAP-001, MODE-001).
- **Not yet specified in Part 1:** how simulated fills, latency, and partial fills are modelled; how paper and live state are kept technically separate (constitution Rule 111); interfaces; tests.

## Findings

- TC-04: at small margins, simulated execution that is optimistic about fills or slippage would overstate results. Paper results need comparison with live expected-vs-actual data (PFC-001) before being trusted.
- OQ-08: operating-mode ownership and transitions.
