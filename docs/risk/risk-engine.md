# Risk Engine, Risk Hierarchy and No-Trade Outcomes

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-09 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Risk") · **Sources:** §25–§27
>
> Canonical location for risk per §98 (`docs/risk/`).

Canonical definition of deterministic risk enforcement, the authority hierarchy, and the valid decision outcomes, including declining to trade.

## Deterministic risk enforcement

- **RSK-001** Deterministic enforcement · CONFIRMED ARCHITECTURAL PRINCIPLE · §25 — Risk enforcement must be deterministic.
- **RSK-002** Risk controls · SYSTEM REQUIREMENT · §25 — Controls may include: position limits; exposure limits; leverage limits; loss limits; position sizing; slippage limits; liquidity requirements; capital reserves; strategy limits; portfolio limits; exchange limits; correlation controls; trade authorization; emergency shutdown; kill switches.
- **RSK-003** AI cannot bypass risk · CONSTRAINT · §25 — AI cannot bypass these controls.

## Authority hierarchy

- **RSK-004** Risk decision hierarchy · CONFIRMED ARCHITECTURAL PRINCIPLE · §26 — Authority, highest first: system safety → user hard constraints → portfolio / risk policy → validated strategy rules → deterministic market conditions → AI analysis / proposal.
- **RSK-005** No override from below · CONSTRAINT · §26 — Lower layers cannot override higher layers.

The platform-level priority order (capital preservation first, opportunity targets last) is PLT-006 in the [platform overview](../product/platform-overview.md).

## No-trade and uncertainty outcomes

- **RSK-006** Valid outcomes · SYSTEM REQUIREMENT · §27 — Valid outcomes include: TRADE; WAIT; NO TRADE; REDUCE RISK; SUSPEND STRATEGY; SAFE MODE; ROLLBACK; UNCERTAIN; I DON'T KNOW.
- **RSK-007** No manufactured confidence · CONSTRAINT · §27 — The system must not manufacture confidence when evidence is insufficient.

Part 1 calls §27 the "No-Trade / Uncertainty System" without naming an owner. It lives here because the Risk Engine is the authority that turns outcomes into permitted actions (RSK-008), and RSK-014 governs uncertain outcomes.

## Decisions applied (2026-09-30)

- **RSK-008** Kill switches and the global safety architecture · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-012 — The Risk Engine owns trading authorization and every kill switch: global, per venue, per instrument type, per strategy, and the arbitrage kill switch (a rule set here using the ARB-010 triggers). Together with System Health (HLT-010), this is the "global safety architecture" of §47.
- **RSK-009** Kill-switch activation and reset · CONSTRAINT · DEC-012 — Kill switches may be activated automatically by deterministic rules or by the operator. Only the operator can reset one, and only after reconciliation succeeds and system health permits trading. AI cannot activate or reset a kill switch; it may only recommend activation.
- **RSK-010** System safety rules · CONFIRMED REQUIREMENT · DEC-012 — The "system safety" layer at the top of the hierarchy (RSK-004) is: no order unless system health permits trading; no order without Risk Engine authorization and a Global Capital Authority reservation; no real order outside an authorized live mode; active kill switches are always respected; no trading on a venue or asset with unresolved reconciliation mismatches; no trading on stale market data (MKD-006); orders must satisfy exchange precision and rules; trading credentials must not allow withdrawals (SEC-003).
- **RSK-011** Final position size · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-010 — A trading system proposes a size using Quantitative Engine calculations. The Risk Engine sets the final size as the smallest of the proposal, the risk limits, and the allocated capital. It may reduce a size but never increase it.
- **RSK-012** Arbitrage risk as rule sets · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-011 — Arbitrage-specific and multi-leg risk rules are rule sets inside this engine, not a separate risk engine.
- **RSK-013** Derivatives and margin controls · CONFIRMED REQUIREMENT · DEC-007 — For perpetual futures and margin, the controls include: maximum leverage; minimum distance to liquidation; margin-ratio limits with automatic de-risking before liquidation; funding and borrow cost limits; limits on total derivatives notional.
- **RSK-014** Uncertainty means no new position · CONSTRAINT · DEC-013 — UNCERTAIN and I DON'T KNOW outcomes, including AI outputs UNCERTAIN and INSUFFICIENT_EVIDENCE, always result in no new position.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

- **RSK-015** Graduated safety levels · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — The platform supports multiple deterministic safety levels instead of one universal emergency action. The owner's example set, adopted as the initial design, is:
  - NORMAL: normal authorized operation.
  - CAUTION: degradation detected; execution may continue under tighter controls (e.g. reduce new exposure, increase validation, restrict affected venues, reduce capital allocation, increase monitoring).
  - RESTRICTED: new risk-taking significantly restricted (e.g. stop new positions for affected strategies, cancel selected pending orders, reduce exposure, disable affected strategies, preserve existing positions according to strategy-specific rules).
  - SAFE MODE: the platform stops initiating new risk unless explicitly permitted by the safety policy; existing positions are managed by deterministic position-protection rules.
  - EMERGENCY: critical system condition (e.g. cancel appropriate open orders, prevent new positions, disable affected strategies, isolate affected venues, preserve capital, reconcile all external state, activate emergency monitoring, apply predefined position-management rules).
  - CRITICAL RECOVERY: the system is uncertain about financial/external state: stop new risk → reconcile → restore state certainty → validate → resume.
- **RSK-016** Response by emergency type · CONFIRMED REQUIREMENT · DEC-019 — An emergency is not treated as one universal action. Different emergency types require different responses, mapped by deterministic rules in policy to a safety level and actions.
- **RSK-017** Policy-driven position handling · CONFIRMED REQUIREMENT · DEC-019 — The system must not blindly close every position during an emergency, nor blindly leave every position untouched. Handling is decided from: emergency type; position exposure; market conditions; liquidity; strategy; risk policy; position-protection policy. Possible actions: hold; reduce; hedge; close; cancel associated orders; freeze strategy; move to protected state; wait for liquidity; escalate.
- **RSK-018** No AI in emergency position handling · CONSTRAINT · DEC-019 — These decisions must be deterministic and policy-controlled. AI must not independently decide how to handle emergency positions.
- **RSK-019** Idempotent emergency actions · CONSTRAINT · DEC-019 — Emergency handling must be safe if triggered multiple times: a repeated trigger must not create duplicate actions or unintended orders. Emergency operations are idempotent, auditable, deterministic, retry-safe, and reconciliation-aware.
- **RSK-020** Safety-level ownership and de-escalation · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-019 — The Risk Engine's emergency controller owns the current safety level. The level is global; its actions are scoped to the affected venues, strategies, and instrument types. It escalates automatically when a deterministic rule fires. It de-escalates automatically when the triggering condition has cleared and the required checks pass (REC-011), except where PLT-014 reserves the condition for a human. Kill-switch reset stays governed by RSK-009 until CF-11 is decided.

## Boundary (§92)

- **Owns:** deterministic risk decisions and the controls in RSK-002.
- **Consumes:** user hard constraints from the [Policy System](../systems/policy/policy-system.md); portfolio and exposure state from [Portfolio Management](../systems/portfolio-management.md); strategy output and AI proposals (validated first, AIV-004).
- **Must not:** be bypassed or overridden by AI (RSK-003, AIL-003), by research (STR-008), or by lower layers (RSK-005).
- **Not yet specified:** limit values (operator policy), interfaces, tests. System safety is defined in RSK-010; failure and state behavior in [System Health](../operations/system-health.md) (HLT-007 to HLT-009).

## Findings

DUP-04 and OQ-06 → [DEC-012](../decisions/DEC-012-safety-architecture.md) (RSK-008, RSK-009). OQ-20 → [DEC-012](../decisions/DEC-012-safety-architecture.md) (RSK-010). DUP-09 → [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md) (RSK-012). DUP-19 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (RSK-011). CF-01 → [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md) (CAP-016). CF-06 → [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md) (the Policy System is in CORE TRADING FOUNDATION). OQ-04 → [DEC-007](../decisions/DEC-007-instrument-scope.md) (RSK-013). CF-04 → [DEC-013](../decisions/DEC-013-ai-organization.md) (RSK-014).

Open: CF-11 (kill-switch reset): RSK-009 allows only the operator to reset a kill switch, while OC-1 makes human intervention exception-based. RSK-009 stays in force until the owner decides; see the [findings register](../conflicts/register.md).
