# Global Capital Authority (Capital Management)

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — not implemented · **System:** SYS-07 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Capital Authority", "Capital reservation"); accumulation is listed under ARBITRAGE · **Sources:** §18–§23; Part 3: P3§358–P3§366, P3§390–P3§391, P3§420, P3§442–P3§443, P3§483–P3§484, P3§517, P3§521
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
- **CAP-028** Arbitrage and reserve capital categories · DEPRECATED / REPLACED · P2§92, P2§221 — The Capital Authority may distinguish: available capital; reserved capital; arbitrage capital; directional capital; emergency reserve; venue-specific reserve. The Capital Authority should support dedicated arbitrage reserves where approved. Exact categories require architecture approval.

P2§37 (one canonical Capital Authority) is CAP-001 and CAP-017. CAP-028 was confirmed by the owner and is replaced by CAP-029 to CAP-033 ([DEC-028](../decisions/DEC-028-capital-buckets-and-progressive-activation.md)); its other categories were already in CAP-002. Pre-positioned arbitrage inventory (XAR-005) is capital held here per venue, never a hidden arbitrage state (ARB-009). "Authorized trading capital" is the capital the Policy System authorizes (NLP-002 capital authorization).

## Owner decisions applied (Part 2 findings, 2026-09-30)

From [DEC-028](../decisions/DEC-028-capital-buckets-and-progressive-activation.md) ([owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), Q6). The owner calls this system the "Capital Allocation & Treasury Engine"; it is the same system, the one capital authority (ARCH-027).

- **CAP-029** Additional capital buckets · SYSTEM REQUIREMENT · DEC-028 — In addition to the categories of CAP-002, the Global Capital Authority maintains: directional trading capital; an emergency reserve; a per-exchange reserve. These must be controlled by policy, not fixed hard-coded amounts.
- **CAP-030** Dynamic bucket sizing · CONFIRMED REQUIREMENT · DEC-028 — Allocation should dynamically scale with total available capital, risk exposure, liquidity, exchange requirements, active strategies, withdrawal/transfer constraints, and system health.
- **CAP-031** Automatic bucket rebalancing · CONFIRMED REQUIREMENT · DEC-028 — The system must automatically rebalance these capital buckets when conditions justify it, without requiring the owner to be online or manually approve routine movements. However, all transfers must remain within hard safety, risk, liquidity, and authorization policies.
- **CAP-032** Progressive capability activation · CONFIRMED REQUIREMENT · DEC-028 — Capital allocation must support progressive capability activation: smaller accounts operate safely within their available capital and do not activate capital-intensive features prematurely. As capital grows and the system proves sufficient capacity and safety, additional capabilities may become eligible automatically.
- **CAP-033** Capital movements respect the floor and the reserves · CONSTRAINT · DEC-028 — No capital movement may violate the platform's safety floor, emergency reserve requirements, exchange-specific reserves, exposure limits, or reconciliation requirements.

Notes:

- **Eligibility.** Whether a capability is eligible is decided by the [Readiness System](readiness-system.md) (RDY-008), from this system's capital figures. Eligibility never exceeds the operator's authorizations (MODE-003, POL-011, PLT-020).
- **Withdrawals.** CAP-030's "withdrawal/transfer constraints" include venue withdrawal and deposit restrictions (CAP-037) and the operator's own withdrawals at venues, which the ledger detects (LED-005). "The platform itself holds no general withdrawal or custody authority" (SEC-006; custody is FUTURE, DEC-006). Rebalancing transfers between the operator's own approved venue accounts use the separate rebalancing transfer authority, which "must not become a general-purpose withdrawal mechanism" (SEC-006, SEC-007; OC-1 item 4; [glossary](../glossary.md)). PLT-010 says the same since CF-21 was decided ([DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md)).
- **Values.** The sizing rules and eligibility thresholds are V-34 and V-35 in the [values register](../requirements/values-register.md).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **CAP-034** Capital growth does not create exposure · CONSTRAINT · P3§358 — When capital increases, do not automatically increase: leverage; trade frequency; position size; risk per trade; market exposure; unless explicitly authorized and validated. Capital growth should instead allow the system to evaluate additional opportunities.
- **CAP-035** Allocation reassessed as capital changes · SYSTEM REQUIREMENT · P3§359 — As capital changes, the Capital Authority should reevaluate: strategy allocations; reserve requirements; arbitrage reserves; venue allocations; emergency reserves; maximum exposure; position sizing; opportunity participation; capital efficiency. The system should continuously determine whether the existing allocation remains appropriate.
- **CAP-036** Capital efficiency without forced utilization · CONFIRMED REQUIREMENT · P3§360, P3§420 — The system should consider not only "Can I afford this trade?" but "Is allocating this capital here the best authorized use of capital given current opportunities and risk?" Capital should not remain unnecessarily trapped in low-value allocations. However, capital should not be constantly moved merely to optimize theoretical utilization. Unused capital is not automatically a problem: if no sufficiently attractive opportunity exists, capital remains available. Capital should be deployed because the economics justify deployment.
- **CAP-037** Additional rebalancing factors · SYSTEM REQUIREMENT · P3§361 — The Rebalancing Engine must be autonomous: the user should not need to manually tell the system "Now move funds from Exchange A to Exchange B", and the system must determine when rebalancing is economically and operationally justified. In addition to the factors of CAP-023 and CAP-024, it should evaluate: historical opportunity frequency; withdrawal/deposit restrictions; transfer reliability; opportunity urgency; expected return on transferred capital.
- **CAP-038** Rebalancing decision model · SYSTEM REQUIREMENT · P3§362 — Conceptually: current inventory → forecast capital requirements → expected opportunity distribution → transfer economics → risk → liquidity → venue health → reserve requirements → rebalancing decision. Possible decisions: NO ACTION; REBALANCE NOW; REBALANCE LATER; PARTIAL REBALANCE; PRE-POSITION; WAIT FOR BETTER NETWORK CONDITIONS; WAIT FOR BETTER ECONOMICS; EMERGENCY REBALANCE.
- **CAP-039** Forward-looking rebalancing · CONFIRMED REQUIREMENT · P3§363 — The system should not wait until an opportunity is discovered and then discover that the required capital is on the wrong exchange. Where economically justified, it should anticipate future capital needs. Example: Exchange A has excess USDT, Exchange B has insufficient USDT, and historical opportunity data indicates that Exchange B frequently produces executable opportunities; the system may determine that moving a portion of capital now is economically justified. This must be based on measured economics, not arbitrary movement.
- **CAP-040** No rebalancing churn · CONSTRAINT · P3§364 — The system must avoid: move funds → move them back → move again → pay fees → lose time → reduce capital efficiency. The Rebalancing Engine must use: minimum meaningful imbalance thresholds; expected opportunity value; transfer costs; transfer latency; reserve requirements; hysteresis / anti-churn logic; cooldowns where appropriate; confidence requirements.
- **CAP-041** Emergency rebalancing · CONFIRMED REQUIREMENT · P3§365 — Emergency rebalancing may occur when required to protect operational continuity or satisfy critical risk constraints. Examples: venue outage; unexpected liquidity deterioration; critical inventory imbalance; capital stranded at an unavailable venue; risk exposure requiring reduction; operational failover; critical reserve deficiency. Emergency rebalancing must still pass deterministic authorization and risk controls.
- **CAP-042** Rebalancing is not a second capital authority · CONSTRAINT · P3§366 — The Rebalancing Engine proposes or executes capital movement through the canonical Capital Authority. It must not create a competing capital ledger or independent authority.
- **CAP-043** Opportunity-set allocation · SYSTEM REQUIREMENT · P3§390, P3§391 — The system should not evaluate opportunities only one at a time in isolation. It should maintain an opportunity set and evaluate: expected net return; risk; capital requirement; capital efficiency; correlation; execution probability; liquidity; time sensitivity; strategy priority; existing exposure; and then determine which opportunities are worth capital allocation. Capital should be treated as a constrained resource, and multiple opportunities may compete for the same capital: opportunity set → capital requirements → risk interactions → correlation → expected net economics → capital allocation. The system should avoid blindly executing every positive-looking opportunity.
- **CAP-044** Additional capital states · SYSTEM REQUIREMENT · P3§442 — Do not confuse available capital with free capital. In addition to the categories of CAP-002 and CAP-029, the Capital Authority must distinguish capital that is: at risk; pending settlement; unavailable.
- **CAP-045** Dynamic reserve requirements · SYSTEM REQUIREMENT · P3§443 — Capital reserves are dynamic. In addition to the factors of CAP-030, reserve requirements may change according to: volatility; open positions; arbitrage requirements; venue health; emergency conditions.
- **CAP-046** Capital change events · CONFIRMED REQUIREMENT · P3§483, P3§484, P3§517, P3§521 — When capital changes materially: capital change → capability reassessment → strategy eligibility → risk reassessment → capital allocation → rebalancing assessment → opportunity universe update. The same intelligence must operate in reverse: if capital decreases, the system should automatically reassess: strategy eligibility; position sizing; reserves; arbitrage participation; feature availability; risk; capital allocation. The system should reduce capabilities safely rather than continuing as though nothing changed.

How these fit what already exists ([DEC-031](../decisions/DEC-031-part-3-reconciliation.md)):

- **The Rebalancing Engine (DUP-34)** is this system's rebalancing-decision component, the one that already decides whether to rebalance (CAP-018, CAP-023) and rebalances the capital buckets (CAP-031). It uses Arbitrage Intelligence's evaluation (ARB-006). It holds no capital state of its own: every movement goes through this system's reservation and the ledger (CAP-001, LED-006), which is what CAP-042 requires.
- **CAP-038's decisions refine CAP-023's four outcomes:** NO ACTION is NO TRANSFER; REBALANCE NOW is EXECUTE TRANSFER; REBALANCE LATER is SCHEDULE; the two WAIT decisions are WAIT with its reason; PARTIAL REBALANCE and PRE-POSITION execute or schedule a transfer for part of an imbalance or ahead of forecast need (CAP-039, XAR-005); EMERGENCY REBALANCE is CAP-041. Every decision stays inside the controls of CAP-025 and CAP-033.
- **Capital growth and limits (CF-18; builder reading, confirmed by the owner on 2026-10-02, [DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)).** CAP-034 is read together with CAP-030, CAP-032, and RSK-036: growth updates available capital and the capability assessment automatically. It raises leverage, trade frequency, position size, risk per trade, market exposure, or authorized capital only when the operator's policy already authorizes that scaling (for example a limit expressed relative to capital, or an explicit reinvestment rule under CAP-011) and the Readiness System has validated it. Any other increase is a policy change under POL-005.
- **P3§441 (compounding is accounting-driven)** is CAP-011, CAP-012, CAP-013, and CAP-026. Its chain "realized P&L → available capital → authorized capital → capability assessment" follows the same CF-18 reading: authorized capital rises only as the capital policy already authorizes.
- **Anti-churn controls** in CAP-040 are policy values (V-38). P3§400 (atomic capital reservation) is CAP-027. P3§391's opportunity competition extends CAP-008 and CAP-017, ranked by TNP-021.
- **Capability eligibility** after a capital change is decided by the [Readiness System](readiness-system.md) (RDY-008, RDY-024); this system publishes the change event.

## Boundary (§92)

- **Owns:** the authoritative capital state (CAP-001, CAP-002), reservations (CAP-004, CAP-005), and allocation decisions (CAP-006 to CAP-009).
- **Consumes:** capital requests from trading systems; risk-check results from the [Risk Engine](../risk/risk-engine.md); user policy from the [Policy System](policy/policy-system.md); realized results via accounting (CAP-012).
- **Must not:** let any strategy assume capital (CAP-003) or hold capital state outside this system (ARB-009).
- **Not yet specified in Part 1:** failure behavior, reservation timeouts, interfaces, tests.

## Findings

**Resolved:** OQ-28 → [DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md): the owner confirmed the instrument scope of PLT-011 ([DEC-007](../decisions/DEC-007-instrument-scope.md)): spot, perpetual futures, and margin, no other derivatives ([open-question register](../open-questions/register.md); raised by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md)). CAP-020 tracks collateral, borrowed funds, and margin.

Resolved:

CF-01 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-016). CF-03 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-021). DUP-02 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (PRT-004). DUP-06 and DUP-07 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (CAP-017, CAP-018). OQ-02 → [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md) (CAP-019). OQ-04 → [DEC-007](../decisions/DEC-007-instrument-scope.md) (CAP-020).
