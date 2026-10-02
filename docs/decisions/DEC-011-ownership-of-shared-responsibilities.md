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

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **More than one owner for a responsibility,** as Part 1 has it for each finding (the claimants listed in the [findings register](../conflicts/register.md)): not taken. Each responsibility has exactly one owner (ARCH-016, constitution Rule 92; "Principle" above). Except for DUP-10, each owner chosen is the one the register proposed when the finding was first recorded.
- **DUP-10 and TC-03, ranking by one of the other systems DUP-10 lists for discovery and ranking:** Opportunity Detection (§09), Arbitrage Intelligence ("opportunity ranking", §43), or Cross-Exchange Arbitrage ("opportunity ranking", §06). The register left the ranking owner open. Not taken: the Global Capital Authority ranks for allocation, and Opportunity Detection only detects and filters (OPP-011). The §17 quality dimensions DUP-10 also lists are kept: the True Net-Profit Engine produces them, with a measure that compares opportunities across trading systems (TNP-021).
- **OQ-10, a Market Regime Engine that is not deterministic:** not taken. RGM-005 makes it deterministic and versioned, with no LLM; the Market Analyst interprets but never sets regime state (DUP-08, RGM-006).

## Consequences

The dependency map marks these edges DECIDED. Part 2 interfaces must follow this ownership.
