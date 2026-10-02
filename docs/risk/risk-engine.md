# Risk Engine, Risk Hierarchy and No-Trade Outcomes

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — not implemented · **System:** SYS-09 · **Category:** shared infrastructure · **Roadmap stage:** CORE TRADING FOUNDATION ("Risk") · **Sources:** §25–§27; Part 3: P3§371, P3§373–P3§375, P3§417–P3§418, P3§435–P3§438
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
- **RSK-009** Kill-switch activation and reset · DEPRECATED / REPLACED · DEC-012 — Kill switches may be activated automatically by deterministic rules or by the operator. Only the operator can reset one, and only after reconciliation succeeds and system health permits trading. AI cannot activate or reset a kill switch; it may only recommend activation.
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

CF-11 was decided by [DEC-021](../decisions/DEC-021-kill-switch-recovery.md): kill-switch reset now follows RSK-021 to RSK-025, and references to RSK-009 resolve there. The recovery checks referred to as REC-011 are now REC-015 and REC-016 ([DEC-022](../decisions/DEC-022-restart-recovery-sequence.md)). RSK-010's last rule refers to SEC-003, which is replaced; its no-withdrawal rule for trading credentials is carried into SEC-006 ([DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md)).

## Owner decisions applied (CF-11 to CF-13, 2026-09-30)

RSK-009 is replaced by RSK-021 to RSK-025 ([DEC-021](../decisions/DEC-021-kill-switch-recovery.md)). Its activation rule and its AI limits are carried into RSK-025.

- **RSK-021** Automatic recovery from transient conditions · CONFIRMED REQUIREMENT · DEC-021 — The platform must automatically recover from known, transient, and measurable infrastructure conditions, such as temporary exchange/API instability, connectivity interruptions, stale market data, rate-limit conditions, or temporary performance degradation, but only after the triggering condition has cleared and deterministic recovery checks pass.
- **RSK-022** Latched kill switches · CONSTRAINT · DEC-021 — Kill switches triggered by security events, unknown financial state, unexplained or abnormal losses, data-integrity failures, suspected duplicate execution, reconciliation failures, custody/withdrawal issues, repeated abnormal behavior, or any other high-risk or uncertain condition must remain latched and require explicit authorization before reset. A trigger not classified as a transient infrastructure condition under RSK-021, including a kill switch the operator activated, stays latched.
- **RSK-023** Progressive, scoped recovery · CONFIRMED REQUIREMENT · DEC-021 — Recovery must be progressive and scoped: tripped → diagnose → wait for the condition to clear → health checks → reconciliation → SAFE/RESTRICTED mode → limited recovery → full operation. Before resuming affected trading, the platform must verify exchange connectivity, market-data freshness, balances, positions, open orders, capital reservations, risk state, policy state, and execution state. The system must not automatically resume full trading merely because the original error appears to have disappeared.
- **RSK-024** Recovery failure escalation · CONSTRAINT · DEC-021 — If recovery fails, trips repeatedly, or the system cannot establish a known-safe state, the platform must remain in SAFE MODE / NO-TRADE and escalate to the operator.
- **RSK-025** Activation, AI limits, and precedence · CONSTRAINT · DEC-021 — Kill switches may be activated automatically by deterministic rules or by the operator. AI cannot activate or reset a kill switch; it may only recommend activation. Automatic recovery must never override higher-level safety, security, policy, financial-integrity, or reconciliation requirements.

The cause classification (transient vs latched), the cleared-condition period, the repeated-trip limit, and the limited-recovery stages are policy values V-24 to V-27 in the [values register](../requirements/values-register.md).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **RSK-026** Loss-streak protection · SYSTEM REQUIREMENT · P2§40 — The system should support configurable protection against repeated losses. Possible responses: reduce exposure; pause strategy; require review; enter cooldown; suspend strategy. Exact thresholds must be policy/configuration driven.
- **RSK-027** Excessive-trading protection · SYSTEM REQUIREMENT · P2§41 — The platform should detect abnormal trade frequency. Possible triggers: excessive order rate; repeated failed opportunities; strategy loop; execution churn; unexpected activity. Responses may include: throttle; pause; review; kill switch.
- **RSK-028** Additional kill-switch scopes · SYSTEM REQUIREMENT · P2§78 — Kill switches must be deterministic. In addition to the scopes in RSK-008, potential levels include: new positions; a specific execution path.
- **RSK-029** No-new-position mode · CONFIRMED REQUIREMENT · P2§79 — The platform should support NO NEW POSITIONS while still allowing controlled management of existing positions where policy permits. This is distinct from a full shutdown.
- **RSK-030** Safe Mode triggers · SYSTEM REQUIREMENT · P2§80 — Safe Mode must be a first-class state. Possible triggers: critical state uncertainty; reconciliation failure; risk engine failure; capital integrity issue; security incident; exchange state uncertainty; data corruption; migration failure.
- **RSK-031** NO TRADE is a valid decision · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§81, P2§310 — "No trade" is not inherently a failure. Examples: opportunity insufficient; risk too high; data stale; unknown regime; capital unavailable; exchange degraded; AI unavailable when required; policy restriction; execution uncertain.
- **RSK-032** WAIT is first-class · CONSTRAINT · P2§82, P2§311 — WAIT means the system needs more information. The system should not be forced to generate a trade merely because the opportunity engine was activated.
- **RSK-033** Arbitrage risk scope · SYSTEM REQUIREMENT · P2§93, P2§222 — Arbitrage-specific risks include: leg failure; execution delay; liquidity collapse; exchange outage; inventory imbalance; transfer risk; venue risk; correlated execution failure. They integrate with the global Risk Authority as rule sets (RSK-012).

Notes:

- **One Risk Authority (P2§39, §229)** is RSK-001 and RSK-012. **The independent arbitrage kill switch (P2§94, §223)** is the arbitrage scope of RSK-008; actions are scoped (RSK-020), so directional strategies may continue while arbitrage is disabled if policy permits.
- **RSK-029 and RSK-015.** NO NEW POSITIONS is the "new positions" kill-switch scope of RSK-028, and it is also what RESTRICTED and SAFE MODE do for the affected scope.
- **RSK-030 and RSK-016.** Each Safe Mode trigger is mapped by policy to SAFE MODE or a higher safety level (RSK-016; values register V-14).
- **Thresholds.** Loss-streak and excessive-trading thresholds are policy values V-30 and V-31 in the [values register](../requirements/values-register.md).
- **CF-14 (decided).** Part 2's user policy hierarchy (P2§101, §279) put user hard policy above system safety. The owner decided on an immutable safety floor instead (RSK-034 to RSK-039, [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)); RSK-004 is unchanged.

## Owner decisions applied (Part 2 findings, 2026-09-30)

CF-14 is decided by the owner ([DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md), [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md), Q1): a layered control model with an immutable safety floor. RSK-004 is unchanged: system safety stays at the top.

- **RSK-034** Immutable safety invariants · CONSTRAINT · DEC-026 — The platform's immutable system-safety invariants must never be disabled or bypassed by an AI agent, strategy, policy, administrator, or automatic process. The safety floor must not be confused with ordinary operational limits or configurable policies. These invariants cannot be overridden: never trade on stale or invalid market data; never execute against an unreconciled exchange state; never exceed the platform's absolute risk boundaries; never send an invalid, duplicated, unauthorized, or unsafe order; never trade when required exchange connectivity/integrity checks fail; never allow an AI agent to directly bypass deterministic safety enforcement.
- **RSK-035** Configurable policy layer · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-026 — The platform uses a layered control model. Capital allocation, strategy limits, exposure limits, execution parameters, opportunity thresholds, and other operational policies may be changed automatically or administratively, but only within the immutable safety envelope.
- **RSK-036** Adaptive operation · CONFIRMED REQUIREMENT · DEC-026 — The platform may automatically adjust operational limits, execution methods, capital allocation, strategy availability, and opportunity thresholds according to available capital, liquidity, market conditions, system health, historical performance, and verified risk conditions, provided that no immutable safety invariant is violated.
- **RSK-037** Recovery and fail-safe behavior · CONFIRMED REQUIREMENT · DEC-026 — If a safety condition temporarily blocks an operation, the platform should automatically diagnose the cause, attempt safe recovery where possible, revalidate all required conditions, and resume only when the safety requirements are satisfied.
- **RSK-038** No deadlock by safety · CONSTRAINT · DEC-026 — A safety rule must prevent unsafe activity, not permanently disable unrelated healthy parts of the platform. The system should isolate the affected component, preserve unaffected operations where safe, and recover automatically when possible.
- **RSK-039** Explicit change control for invariants · CONSTRAINT · DEC-026 — Any proposed change to an immutable safety invariant must require a formal, versioned, audited human-controlled policy change. AI may analyze and propose such changes, but may never authorize or silently implement them.

How these fit is set out in [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md):

- The safety floor is RSK-034 together with the system safety rules of RSK-010.
- The HARD LIMIT values in the [values register](../requirements/values-register.md) are the numbers inside the invariants, so changing one is an RSK-039 change.
- RSK-036's automatic adjustments are operating decisions inside the bounds the operator sets in policy. Widening a bound or an authorization still needs the operator (POL-005).

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **RSK-040** Critical subsystem failure · CONFIRMED REQUIREMENT · P3§371 — If a critical subsystem fails (risk; capital; execution; reconciliation; market-data integrity; security), the system may transition to: SAFE MODE; NO NEW POSITIONS; WAIT; or another explicitly defined safety state. Existing positions must continue to be managed according to the safest validated behavior.
- **RSK-041** Emergencies without chaos · CONSTRAINT · P3§373 — An emergency must not trigger uncontrolled simultaneous actions. For example, emergency → all services panic → everything sells → everything transfers → system collapses is unacceptable. Instead: emergency → classify failure → protect capital → stop prohibited actions → preserve valid state → reconcile → execute approved recovery policy.
- **RSK-042** Emergency priority · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§374 — Conceptually: 1. protect financial state; 2. prevent unauthorized execution; 3. preserve external state; 4. determine actual state; 5. reduce uncontrolled exposure; 6. restore critical services; 7. reconcile; 8. resume only when safe.
- **RSK-043** Safe Mode permissions · CONFIRMED REQUIREMENT · P3§375 — Safe Mode is a deliberate operating state. It may disable: new positions; new strategies; new deployments; unvalidated AI decisions; high-risk execution; while preserving: monitoring; reconciliation; risk evaluation; position management; emergency controls; data collection; recovery. The exact Safe Mode permissions must be formally defined.
- **RSK-044** No chasing and no forced trading · CONSTRAINT · P3§417, P3§418 — The system should not enter a trade merely because an opportunity disappeared or because another opportunity was profitable. A missed opportunity does not justify lowering safety standards. The platform must never trade merely to: increase activity; hit a daily target; keep AI busy; use available capital; recover losses; compensate for missed opportunities; satisfy a trade-count target. NO TRADE is valid.
- **RSK-045** Additional loss-streak responses · SYSTEM REQUIREMENT · P3§435 — In addition to the responses of RSK-026, possible responses to abnormal loss sequences include: throttle; enter safe state. The exact thresholds must be validated rather than arbitrarily fixed.
- **RSK-046** Additional excessive-trading signals · SYSTEM REQUIREMENT · P3§436 — In addition to the triggers of RSK-027, the system should detect abnormal increases in: order cancellations; re-entry; churn; capital turnover; and determine whether the behavior is legitimate or pathological.
- **RSK-047** No revenge trading, no martingale by default · CONSTRAINT · P3§437, P3§438 — Losses must not automatically increase: position size; trade frequency; risk; leverage. The system must not automatically increase exposure after losses unless an explicitly validated strategy and policy authorize such behavior.
- **RSK-048** Where Part 3's layers sit in the hierarchy · DEPRECATED / REPLACED · DEC-031 — P3§471's precedence layers are placed within RSK-004's hierarchy, highest first: system safety (the safety floor: RSK-034 with RSK-010) → user hard constraints (Part 3's "user hard policy") → security → portfolio / risk policy → capital → execution → validated strategy rules → deterministic market conditions → AI analysis / proposal (Part 3's "AI preference"). No lower layer may override a higher-level hard constraint (RSK-005).

How these fit what already exists:

- **Precedence (CF-17; decided by the owner on 2026-10-02: RSK-048 is replaced by RSK-049, below).** P3§471 puts user hard policy above system safety, as P2§101 did. The owner already decided this question for P2§101: the safety floor stays on top and can only be changed through RSK-039 ([DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)). RSK-048 applies that decision and adds Part 3's security, capital, and execution layers in Part 3's own order. RSK-004 is unchanged. As a result, RSK-048 ranked security controls outside the safety floor (for example SEC-006 to SEC-008) below the user's hard constraints. The owner decided otherwise: security ranks above them (RSK-049).
- **Emergency state names (DUP-35; builder reading, confirmed by the owner on 2026-10-02, [DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md)).** P3§372's possible states map onto existing states without merging different meanings: NORMAL = safety level NORMAL; DEGRADED = the health state DEGRADED (HLT-011), which feeds the safety level (typically CAUTION) and is not itself a safety level; PROTECTIVE = safety level RESTRICTED; EMERGENCY = EMERGENCY; SAFE MODE = SAFE MODE; RECOVERY = recovery in progress, either recovery from a transient condition (RSK-021 to RSK-023) or CRITICAL RECOVERY when financial or external state is uncertain, with health state RECOVERING; RESUMING = the limited-recovery step of RSK-023. P3§372 itself leaves the final state machine to architecture, as HLT-002 does.
- **RSK-040:** adds execution failure and the NO NEW POSITIONS and WAIT outcomes to the Safe Mode triggers of RSK-030; position handling stays policy-driven and deterministic (RSK-017, RSK-018).
- **RSK-043:** makes formal definition of Safe Mode's permissions a requirement; OPS-006 already keeps recovery and monitoring running in SAFE MODE.
- **RSK-044:** extends RSK-031 and RSK-032. P3§419 (quality over trade count) is PLT-019. P3§376 (no-new-position mode) is RSK-029. P3§422 (unknown means unknown) is PLT-018, RSK-007, and RSK-014.
- **RSK-045, RSK-046** thresholds are values V-30 and V-31. RSK-045's loss-streak thresholds (V-30) must now also be validated, not only configured (P3§435); RSK-046 adds signals to V-31 and requires deciding whether abnormal activity is legitimate or pathological (P3§436).

## Owner decisions applied (Part 3 findings, 2026-10-02)

CF-17 is decided by the owner ([DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md), [owner decisions 4](../handoffs/owner-decisions-04-part-3-findings.md), Q1): security controls rank above the user's hard policy, below the safety floor. RSK-048, which placed them below it, is replaced; its wording is kept above as the record.

- **RSK-049** Security ranks above the user's hard constraints · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-035 — The precedence layers, highest first: system safety (the safety floor: RSK-034 with RSK-010) → security → user hard constraints → portfolio / risk policy → capital → execution → validated strategy rules → deterministic market conditions → AI analysis / proposal. No lower layer may override a higher-level hard constraint (RSK-005). The user's hard policy cannot override a security control, for example the transfer-authority restrictions (SEC-006, SEC-007) or AI least privilege (SEC-008); changing a security control needs a formal, audited security change.

RSK-049 keeps RSK-004's layers in their order and places Part 3's security, capital, and execution layers within it (P3§471), with security moved above the user's hard constraints by the owner. How a formal, audited security change is made is specified with the security and policy design. Indexed in SR-02 of the [System Rules Register](../requirements/system-rules-register.md).

## Boundary (§92)

- **Owns:** deterministic risk decisions and the controls in RSK-002.
- **Consumes:** user hard constraints from the [Policy System](../systems/policy/policy-system.md); portfolio and exposure state from [Portfolio Management](../systems/portfolio-management.md); strategy output and AI proposals (validated first, AIV-004).
- **Must not:** be bypassed or overridden by AI (RSK-003, AIL-003), by research (STR-008), or by lower layers (RSK-005).
- **Not yet specified:** limit values (operator policy), interfaces, tests. System safety is defined in RSK-010; health state in [System Health](../operations/system-health.md) (HLT-011, HLT-012), and the safety levels in RSK-015 to RSK-020.

## Findings

All resolved. CF-14 → [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md) (RSK-034 to RSK-039). DUP-04 and OQ-06 → DEC-012 (RSK-008). OQ-20 → DEC-012 (RSK-010). DUP-09 → DEC-011 (RSK-012). DUP-19 → DEC-010 (RSK-011). CF-01 → DEC-010 (CAP-016). CF-06 → DEC-016. OQ-04 → DEC-007 (RSK-013). CF-04 → DEC-013 (RSK-014). CF-11 → [DEC-021](../decisions/DEC-021-kill-switch-recovery.md) (RSK-021 to RSK-025).
