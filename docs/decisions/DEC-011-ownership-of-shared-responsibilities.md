# DEC-011 — Ownership of overlapping responsibilities

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Date:** 2026-09-30
- **Resolves:** DUP-01, DUP-02, DUP-03, DUP-05, DUP-06, DUP-07, DUP-08, DUP-09, DUP-10, DUP-16, DUP-18, DUP-20, DUP-21, DUP-22, TC-03, OQ-10

## Principle

Each responsibility has exactly one owner (ARCH-016, constitution Rule 92). Handoff requirements that list an overlapping item are **kept as written** and read as "uses", not "owns"; each affected specification carries a note pointing here. Nothing was removed.

## Decisions

| Finding | Owner | Everyone else | New requirement |
|---|---|---|---|
| DUP-01 net-profit calculation | True Net-Profit Engine alone produces the true net expected result | Quantitative Engine computes primitive metrics; arbitrage and directional systems supply legs, routes, and sizes, and consume the result | TNP-017, QNT-004, ARB-012 |
| DUP-02 capital state | Global Capital Authority | Portfolio shows capital figures read-only | PRT-004 |
| DUP-03 performance controller / expected vs actual | One platform-wide Performance Controller | Arbitrage systems supply expected values and the opportunity database | PFC-006 |
| DUP-05 market / exchange monitoring | Opportunity Detection Engine (§08 and §09 are one system) | Exchange *health* belongs to operational monitoring | OPP-010 |
| DUP-06 rebalancing | Global Capital Authority decides | Arbitrage Intelligence evaluates | CAP-018 |
| DUP-07 allocation and reserve | Global Capital Authority | Arbitrage requests capital; the arbitrage reserve is a category held there | CAP-017 |
| DUP-08 market regime (+ OQ-10) | Market Regime Engine: deterministic, versioned, explicit UNCERTAIN / UNKNOWN thresholds, no LLM | Market Analyst interprets but never sets regime state | RGM-005, RGM-006 |
| DUP-09 arbitrage risk | Risk Engine (arbitrage rule sets inside it) | — | RSK-012 |
| DUP-10 ranking (+ TC-03) | Global Capital Authority ranks for allocation, using a common risk-adjusted expected net return per unit of capital per unit of time, produced by the True Net-Profit Engine | Opportunity Detection detects and filters only | CAP-017, TNP-021, OPP-011 |
| DUP-16 reconciliation | Recovery and Reconciliation | Execution invokes it | REC-008, EXE-007 |
| DUP-18 strategy research | Strategy Factory owns and coordinates the process | AI agents assist inside it | STR-012 |
| DUP-20 directional vs shared | Directional owns directional-specific logic | Uses shared backtesting, paper trading, performance, improvement, monitoring | DIR-004 |
| DUP-21 opportunity records | Event history is the authoritative record | The arbitrage opportunity database is an analytical store, linked by event IDs and rebuildable from events | AUD-005, ARB-014 |
| DUP-22 AI memory | Each canonical owner keeps its own history | Memory references versioned records, never copies them | MEM-005 |

## Consequences

The dependency map marks these edges DECIDED. Part 2 interfaces must follow this ownership.
