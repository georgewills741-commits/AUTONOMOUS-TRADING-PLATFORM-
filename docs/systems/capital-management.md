# Global Capital Authority (Capital Management)

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-07 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Capital Authority", "Capital reservation"); accumulation is listed under ARBITRAGE · **Sources:** §18–§23
>
> File path follows §98 (`docs/systems/capital-management.md`). The system's name in the handoff is **Global Capital Authority**.

Canonical definition of the platform's single capital state, capital reservation, allocation, competition between strategies, compounding, and protection of active trades. The arbitrage capital reserve is defined in [Arbitrage Intelligence](arbitrage/arbitrage-intelligence.md) (ARB-008, ARB-009) and must integrate with this system.

## One authoritative capital state

- **CAP-001** Single authoritative capital state · CONFIRMED ARCHITECTURAL PRINCIPLE · §18 — All trading systems must use one authoritative capital state.
- **CAP-002** Capital categories · SYSTEM REQUIREMENT · §18 — It must distinguish: available capital; reserved capital; capital committed to positions; capital committed to pending orders; capital allocated to arbitrage; capital held in reserve; capital by exchange; capital by strategy; capital pending release; capital involved in partial fills.
- **CAP-003** No assumed capital · CONSTRAINT · §18 — A strategy must never independently assume that capital is available.

## Reservation

- **CAP-004** Reservation flow · CONFIRMED ARCHITECTURAL PRINCIPLE · §19 — Before capital is committed: opportunity → capital request → Global Capital Authority → risk check → reservation → execution → commit / release.
- **CAP-005** Reservation release · CONFIRMED REQUIREMENT · §19 — Reservations must be correctly released after: rejection; cancellation; completion; failure; partial execution; recovery.

## Allocation and competition

- **CAP-006** Dynamic capital allocation · SYSTEM REQUIREMENT · §20 — The system should determine how available capital can be used most effectively while respecting risk. It should evaluate: net economics; risk; liquidity; existing exposure; capital reserve; strategy health; correlation; user policy; execution constraints; opportunity duration.
- **CAP-007** Efficiency, not exposure · CONSTRAINT · §20 — Capital allocation must optimize capital efficiency under constraints, not maximize exposure.
- **CAP-008** Opportunity competition · CONFIRMED ARCHITECTURAL PRINCIPLE · §21 — Different strategies may discover opportunities simultaneously: directional + cross-exchange + triangular → Global Capital Authority → risk / exposure / liquidity → allocation.
- **CAP-009** Not profitability alone · CONSTRAINT · §21 — Theoretical profitability alone must not determine allocation.

## Accumulation and compounding

- **CAP-010** Accumulating realized results · SYSTEM REQUIREMENT · §22 — The arbitrage system should be capable of accumulating realized positive results over time.
- **CAP-011** Reinvesting realized profits · CONFIRMED REQUIREMENT · §22 — The system may use realized profits to increase future available trading capital when permitted by: user policy; capital-management rules; risk limits; reserve requirements; strategy constraints; operational safety.
- **CAP-012** Compounding flow · CONFIRMED ARCHITECTURAL PRINCIPLE · §22 — Valid opportunity → net profit → realized result → accounting / ledger → available capital → future capital allocation → new opportunities. This creates the possibility of compounding.
- **CAP-013** Compounding is not a promise · CONSTRAINT · §22 — Compounding is an accounting/capital-allocation mechanism, not a promise of compound returns.

## Active trade protection

- **CAP-014** Respect existing commitments · CONSTRAINT · §23 — A new opportunity must not automatically interrupt an existing position merely because it appears theoretically better. Existing commitments must be respected.
- **CAP-015** Grounds for rejecting a new opportunity · SYSTEM REQUIREMENT · §23 — A new opportunity may be rejected because: capital is committed; risk budget is committed; exposure limits are reached; execution resources are constrained; existing positions require management; the opportunity is no longer executable.

## Boundary (§92)

- **Owns:** the authoritative capital state (CAP-001, CAP-002), reservations (CAP-004, CAP-005), and allocation decisions (CAP-006 to CAP-009).
- **Consumes:** capital requests from trading systems; risk-check results from the [Risk Engine](../risk/risk-engine.md); user policy from the [Policy System](policy/policy-system.md); realized results via accounting (CAP-012).
- **Must not:** let any strategy assume capital (CAP-003) or hold capital state outside this system (ARB-009).
- **Not yet specified in Part 1:** failure behavior, reservation timeouts, interfaces, tests.

## Findings

- CF-01: §19 and §21 place the capital authority before the risk check; §94 places risk before capital.
- CF-03: capital reservation does not appear on the latency-sensitive path (PERF-003).
- DUP-02: the Portfolio also tracks allocated, reserved, and available capital (PRT-002).
- DUP-06 and DUP-07: rebalancing, dynamic allocation, and the capital reserve are also listed by Arbitrage Intelligence (ARB-001).
- OQ-02: CAP-012 routes realized results through "accounting / ledger", but the ledger is only required if the platform becomes user-facing (LED-001).
