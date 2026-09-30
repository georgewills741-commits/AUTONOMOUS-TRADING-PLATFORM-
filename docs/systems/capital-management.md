# Global Capital Authority (Capital Management)

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-07 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Capital Authority", "Capital reservation"); accumulation is listed under ARBITRAGE · **Sources:** §18–§23
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

## Decisions applied (2026-09-30)

- **CAP-016** Runtime order of capital and risk · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-010 — The runtime order is: capital request → this system checks availability and allocation → the Risk Engine authorizes and sets the final size → this system reserves → execution → commit / release. §94's order is a build-dependency chain, not the runtime order. A risk rejection means nothing is reserved.
- **CAP-017** Allocation and ranking authority · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This system alone allocates capital and ranks competing opportunities for allocation, using the comparable measure in TNP-021. Arbitrage allocation and the arbitrage reserve are capital categories held here.
- **CAP-018** Rebalancing decisions · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — This system decides whether to rebalance. Arbitrage Intelligence supplies the evaluation (ARB-006).
- **CAP-019** Capital derived from the ledger · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-006 — Available capital is derived from ledger-confirmed balances minus reservations and commitments (LED-006).
- **CAP-020** Collateral and margin categories · SYSTEM REQUIREMENT · DEC-007 — The capital state also distinguishes collateral posted for margin and derivatives positions, borrowed funds, and margin required to keep positions open.
- **CAP-021** Reservation on the latency-sensitive path · CONFIRMED REQUIREMENT · DEC-010 — The latency-sensitive path includes capital reservation (§77 lists stages, not every control). Reservation must meet the latency targets in PERF-007.
- **CAP-022** Rebalancing transfers need confirmation by default · DEPRECATED / REPLACED · DEC-012 — Rebalancing transfers are proposed by the platform and executed after operator confirmation. Automated transfers can be enabled only by an important policy change (POL-005) and must use the restricted transfer key described in SEC-003.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

CAP-022 (transfers need operator confirmation by default) is replaced by CAP-023 to CAP-025. CAP-021 still names the latency targets of PERF-007, which is replaced; reservation must now meet the path-specific latency budgets of PERF-008 to PERF-012.

- **CAP-023** Autonomous rebalancing decision · CONFIRMED REQUIREMENT · DEC-019 — The platform must be capable of making autonomous rebalancing decisions when doing so is authorized by policy and economically justified. The decision considers: venue inventory state; capital requirements; current reserves; expected opportunity distribution; liquidity requirements; future opportunity forecast / expected value; transfer cost; transfer time; network conditions; venue health; risk; capital policy; rebalancing policy; true economic benefit. The outcome is one of NO TRANSFER, WAIT, SCHEDULE, or EXECUTE TRANSFER. The platform should not move funds simply because balances are unequal, and it should not refuse to move funds merely because a human is unavailable.
- **CAP-024** Economic justification · CONFIRMED REQUIREMENT · DEC-019 — Before transferring, the system should calculate whether expected benefit exceeds transfer cost + risk cost + opportunity cost. It should consider: current inventory; required reserve; available capital; reserved capital; expected opportunity flow; venue-specific capital requirements; transfer fees; network fees; transfer latency; blockchain/network conditions; venue liquidity; expected future opportunity value; risk; capital efficiency; minimum reserve requirements; maximum transfer limits; transfer frequency limits; operational health; exchange availability. A transfer should not occur merely because the balance between exchanges is uneven.
- **CAP-025** Bounded rebalancing · CONSTRAINT · DEC-019 — Autonomous rebalancing operates within explicit controls: maximum transfer amount; maximum daily transfer amount; minimum venue reserve; maximum venue exposure; approved destination venues; approved source venues; approved assets; transfer frequency limits; emergency restrictions; risk restrictions; capital restrictions; user policy restrictions. If rebalancing is required but outside the authorized boundary, the system does not execute; it waits, alerts, and requests authorization. It must never invent authorization.

The Execution Engine carries out the transfer (EXE-009). Transfer authority and security are SEC-006 and SEC-007. The control values are V-10 in the [values register](../requirements/values-register.md).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **CAP-026** Capital distinctions for compounding · SYSTEM REQUIREMENT · P2§36, P2§227 — The system must distinguish: realized P&L; available capital; authorized trading capital; reserved capital. Realized gains may become available for future trading if authorized. Compounding follows realized capital and policy authorization; it is a capital-management consequence, not a guaranteed strategy outcome.
- **CAP-027** Atomic capital reservation · CONSTRAINT · P2§38 — Capital reservation must be safe under concurrency. Two strategies must not simultaneously reserve the same capital. Reservation should be atomic or otherwise protected against race conditions.
- **CAP-028** Arbitrage and reserve capital categories · PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION · P2§92, P2§221 — The Capital Authority may distinguish: available capital; reserved capital; arbitrage capital; directional capital; emergency reserve; venue-specific reserve. The Capital Authority should support dedicated arbitrage reserves where approved. Exact categories require architecture approval.

P2§37 (one canonical Capital Authority) is CAP-001 and CAP-017. CAP-002 already distinguishes capital allocated to arbitrage, capital held in reserve, and capital by exchange; CAP-028's new categories (directional capital, emergency reserve, venue-specific reserve) wait for the owner's confirmation. Pre-positioned arbitrage inventory (XAR-005) is capital held here per venue, never a hidden arbitrage state (ARB-009). "Authorized trading capital" is the capital the Policy System authorizes (NLP-002 capital authorization).

## Boundary (§92)

- **Owns:** the authoritative capital state (CAP-001, CAP-002), reservations (CAP-004, CAP-005), and allocation decisions (CAP-006 to CAP-009).
- **Consumes:** capital requests from trading systems; risk-check results from the [Risk Engine](../risk/risk-engine.md); user policy from the [Policy System](policy/policy-system.md); realized results via accounting (CAP-012).
- **Must not:** let any strategy assume capital (CAP-003) or hold capital state outside this system (ARB-009).
- **Not yet specified in Part 1:** failure behavior, reservation timeouts, interfaces, tests.

## Findings (all resolved)

CF-01 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-016). CF-03 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-021). DUP-02 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PRT-004). DUP-06 and DUP-07 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (CAP-017, CAP-018). OQ-02 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (CAP-019). OQ-04 → [DEC-007](../decisions/DEC-007-instrument-scope.md) (CAP-020).
