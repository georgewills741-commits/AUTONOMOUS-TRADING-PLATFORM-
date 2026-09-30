# Findings Register: Conflicts, Inconsistencies and Duplicate Responsibilities

> **Status:** ACTIVE register. Last updated 2026-09-30. **All 32 findings are RESOLVED** by decision records DEC-002, DEC-003, DEC-006, and DEC-010 to DEC-016 (resolved at the owner's instruction; see each record for who decided). Entries are kept, not deleted, so the trace remains (constitution Rule 179).
>
> Specifications keep the handoff's requirements **as stated**. Findings are recorded here and are **not** silently resolved in the specifications (DEC-005). Every "proposed resolution" is **RECOMMENDED — NOT YET APPROVED** until the project owner accepts it. When one is accepted, record the decision in [`docs/decisions/`](../decisions/README.md), update the affected specifications, and mark the finding RESOLVED here with a link. Do not delete it.
>
> Open questions and technical concerns are in [`docs/open-questions/register.md`](../open-questions/register.md). Terminology normalization is in the [glossary](../glossary.md).

Summary: 10 conflicts/inconsistencies (CF) and 22 duplicate or overlapping responsibilities (DUP), all RESOLVED. "Proposed resolution" below is the builder's recommendation as first written; "Resolution" is what was decided.

## Conflicts and inconsistencies (CF)

### CF-01 — Order of the capital and risk checks
- **Sources:** §19 (opportunity → capital request → Global Capital Authority → risk check → reservation → execution); §21 (Global Capital Authority → risk/exposure/liquidity → allocation); §94 (strategy → risk → capital → execution); §70 ("capital / risk" as one step).
- **Conflict:** §19/§21 put the capital authority before the risk check; §94 puts risk before capital.
- **Impact:** high. This defines the core pre-trade sequence and the interface between the Risk Engine and the Global Capital Authority.
- **Status:** RESOLVED — [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): §19 order is the runtime order (CAP-016).
- **Proposed resolution (as first written):** treat §19 as authoritative for the detailed pre-trade sequence (it is the capital-specific flow), and read §94 as a coarse build-dependency example. Needs owner confirmation.

### CF-02 — Where AI sits in the decision flow
- **Sources:** §70 (strategy → AI reasoning → capital/risk); §08 (strategy/risk/capital → "AI only when justified"); §66 (analysis → Trading Director → Devil's Advocate → deterministic Risk Engine); §77 (latency path with no AI step).
- **Conflict:** §08 places AI after risk and capital; §70 and §66 place it before risk.
- **Impact:** medium. Affects whether AI proposals are checked by risk (§66 says risk remains authoritative).
- **Status:** RESOLVED — [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): AI, when used, sits before capital and risk; never on arbitrage paths.
- **Proposed resolution (as first written):** AI is an optional step that is always upstream of the deterministic Risk Engine (consistent with §26, §66, §70). Read §08 as "AI is invoked only for significant opportunities", not as AI coming after risk.

### CF-03 — Capital reservation missing from the latency-sensitive path
- **Sources:** §77 (market event → … → risk check → execution validation → exchange order); §19 (reservation before capital is committed).
- **Conflict:** the latency path has no capital-reservation step.
- **Impact:** medium. A literal reading of §77 would allow orders without reservation, which violates CAP-003 and CAP-004.
- **Status:** RESOLVED — [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): reservation is on the latency path (CAP-021).
- **Proposed resolution (as first written):** the latency path includes capital reservation; §77 lists stages, not every mandatory control.

### CF-04 — AI output decision values vs valid outcomes
- **Sources:** §65 (Decision: BUY / SELL / HOLD / NO_TRADE); §27 (valid outcomes include WAIT, REDUCE RISK, SUSPEND STRATEGY, SAFE MODE, ROLLBACK, UNCERTAIN, I DON'T KNOW); §07 (multi-leg routes).
- **Conflict:** the output contract cannot express uncertainty or multi-leg arbitrage decisions, yet §27 forbids manufacturing confidence.
- **Impact:** medium. A schema with no "uncertain" value pushes models toward false decisions.
- **Status:** RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): extended decision values (AIV-013); arbitrage has no AI proposals (ARB-013).
- **Proposed resolution (as first written):** extend the conceptual schema so it can express uncertainty, and add a route/leg form for arbitrage, in Part 2's interface contracts.

### CF-05 — Roadmap stage mapping: duplicates and gaps
- **Source:** §95.
- **Mapped twice:** reconciliation (CORE TRADING FOUNDATION and OPERATIONALIZATION); opportunity economics (CORE) vs "true net-profit calculation" (ARBITRAGE).
- **Mapped to one trading stage but shared:** strategy lifecycle, backtesting, and paper trading (DIRECTIONAL, but PAP-002 covers arbitrage); performance controller (ARBITRAGE, but platform-wide per §49).
- **Not mapped to any stage:** Policy System (persistent, versioned policy, §29–§30); operating modes (§31); auditability / event history (§86–§87); system health (§74); model evaluation (§61); structured AI output (§65); AI confidence calibration (§67); numerical precision (§79, cross-cutting); custody/ledger (§84–§85, unconfirmed); security beyond "security foundation" (§89).
- **Impact:** medium. §95 itself says exact sequencing is finalized after dependency analysis.
- **Status:** RESOLVED — [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md): every item placed in exactly one build stage.

### CF-06 — Policy is needed before the stage that delivers it
- **Sources:** §26 (user hard constraints rank second in risk authority); §28–§30 (policy system); §95 (only the NL Policy Interface is mapped, to AI INTELLIGENCE).
- **Conflict:** the Risk Engine (CORE TRADING FOUNDATION) enforces user hard constraints, but structured policy has no stage, and the only policy item is in a later stage.
- **Impact:** high for sequencing.
- **Status:** RESOLVED — [DEC-016](../decisions/DEC-016-roadmap-stage-placement.md): Policy System in CORE TRADING FOUNDATION.
- **Proposed resolution (as first written):** place the structured, versioned Policy System (SYS-12) no later than CORE TRADING FOUNDATION, and keep the NL interface (SYS-13) in AI INTELLIGENCE.

### CF-07 — Documentation paths in §98 vs §99
- **Sources:** §98 (`docs/systems/directional-trading.md`, `execution-engine.md`, `capital-management.md`); §99 (folders `systems/directional/`, `market-data/`, `exchanges/`, `recovery/`, `ai/agents/`, plus `implementation/`).
- **Conflict:** file vs folder for the same domain.
- **Impact:** low.
- **Status:** RESOLVED (decision accepted) by [DEC-002](../decisions/DEC-002-documentation-structure.md). §98 paths are used where given; single files are used elsewhere until content needs a folder; `implementation/` is not created before implementation is approved.

### CF-08 — Two canonical locations for policy
- **Source:** §98 lists both `docs/product/trading-policy.md` and `docs/systems/policy/` for "Policy".
- **Conflict:** two authoritative locations risk competing sources of truth (constitution Rule 44).
- **Impact:** low now; would be high if both held rules.
- **Status:** RESOLVED — [DEC-015](../decisions/DEC-015-modes-canary-and-policy-governance.md): policy lives only in the Policy System (POL-009); the product file is not created.

### CF-09 — Recovery sequence ordering
- **Source:** §71 ("load verified internal state" comes before "verify database").
- **Conflict:** state is loaded before the database it comes from is verified.
- **Impact:** low, but it matters for recovery correctness.
- **Status:** RESOLVED — [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): verify the database before loading (REC-007).
- **Proposed resolution (as first written):** confirm the intended order, or read "load verified internal state" as loading the last checkpoint that had been verified before the interruption.

### CF-10 — Two classification vocabularies
- **Sources:** handoff §96 (10 classes); constitution Rule 20 (18 types) and Rule 181 (status vocabulary).
- **Conflict:** overlapping but different vocabularies.
- **Impact:** low.
- **Status:** RESOLVED (decision accepted) by [DEC-003](../decisions/DEC-003-requirement-ids-and-classification.md). §96 classifies requirements; constitution terms describe status and findings.

## Duplicate or overlapping responsibilities (DUP)

§00 item 14 and constitution Rules 30 and 34 require these to be identified before implementation.

| ID | Responsibility | Claimed by | Proposed resolution (as first written) | Resolution |
|---|---|---|---|---|
| DUP-01 | Net-profit / opportunity economics | True Net-Profit Engine (§13); Quantitative Engine "fees, slippage, arbitrage economics" (§12); Cross-Exchange "fee calculation, slippage estimation, true net-profit calculation" (§06); Triangular "profitability calculation, fees, slippage" (§07); Arbitrage Intelligence (§43) | The Quantitative Engine computes primitive metrics. The True Net-Profit Engine alone produces the true net expected result. Arbitrage systems supply leg/route definitions and consume the result. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): TNP-017, QNT-004, ARB-012 |
| DUP-02 | Capital state (allocated, reserved, available) | Global Capital Authority (§18); Portfolio (§24) | The Global Capital Authority is authoritative; Portfolio reads and presents capital state and never holds its own copy. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): PRT-004 |
| DUP-03 | Performance controller; expected-vs-actual analysis | Performance Controller (§48–§49); Arbitrage Intelligence (§43); Cross-Exchange (§06); Triangular (§07) | One platform-wide Performance Controller. Arbitrage supplies expected values and the opportunity database. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): PFC-006 |
| DUP-04 | Kill switches, emergency shutdown, safe mode, trading halt | Risk Engine (§25); arbitrage kill switch (§47); System Health states (§74); §27 outcomes; undefined "global safety architecture" (§47) | Needs the owner's answer to OQ-06. Candidate: the Risk Engine owns kill switches and trading authorization; System Health owns platform state; the arbitrage kill switch is a Risk Engine rule set. | RESOLVED — [DEC-012](../decisions/DEC-012-safety-architecture.md): Risk Engine owns kill switches; System Health owns platform state (RSK-008, HLT-010) |
| DUP-05 | Market / exchange monitoring | Whole-universe monitoring (§08); Opportunity Detection (§09); Cross-Exchange "exchange monitoring", "exchange health" (§06); Monitoring "Exchanges" (§88) | §08 and §09 are one system (SYS-05, market monitoring). Exchange *health* belongs to operational monitoring (SYS-28), per ARCH-005. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): OPP-010 |
| DUP-06 | Rebalancing | "Capital-management decision" (§45); Arbitrage Intelligence "rebalancing intelligence" (§43) | The Global Capital Authority decides; Arbitrage Intelligence produces the rebalancing evaluation (ARB-006). | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): CAP-018 |
| DUP-07 | Dynamic allocation and capital reserve | Global Capital Authority (§20, §18); Arbitrage Intelligence "capital reserve", "dynamic capital allocation" (§43); Cross-Exchange "capital availability" (§06) | Allocation belongs to the Global Capital Authority; the arbitrage reserve is a capital category held there (ARB-009 already requires it). | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): CAP-017 |
| DUP-08 | Market regime | Market Regime Engine (§11); Market Analyst "regime interpretation" (§57); Directional "regime compatibility" (§05) | The Regime Engine is authoritative for regime state. The Analyst may add interpretation but does not set state. Directional consumes it. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): RGM-005, RGM-006 |
| DUP-09 | Arbitrage and multi-leg risk | Risk Engine (§25); Arbitrage Intelligence "arbitrage-specific risk" (§43); Triangular "multi-leg risk" (§07) | Arbitrage-specific risk rules are configured inside the shared Risk Engine (ARCH-016). | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): RSK-012 |
| DUP-10 | Opportunity discovery and ranking | Opportunity Detection (§09); Arbitrage Intelligence "opportunity discovery", "opportunity ranking" (§43); Cross-Exchange "opportunity ranking" (§06); quality dimensions (§17) | Discovery is shared (SYS-05). The ranking owner needs a decision; see also TC-03. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): Global Capital Authority ranks (CAP-017, TNP-021) |
| DUP-11 | News and market-event interpretation | Market Analyst (§57); News/Sentiment Agent (§54) | Merge, or give the News/Sentiment Agent a documented distinct scope (OQ-11). | RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): merged into Market Analyst (AGT-016) |
| DUP-12 | Strategy research vs optimization | Strategy Research Agent and Strategy Optimizer (both §59) | One agent unless a distinct scope is documented (OQ-11). | RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): one Research Agent (AGT-016) |
| DUP-13 | Research | Research Agent (§54); Quant Research Agent (§58); Strategy Research Agent (§59); "research coordination" (§51) | Define scopes, or consolidate (OQ-11). | RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): one Research Agent (AGT-016) |
| DUP-14 | Performance deterioration analysis | Performance Analyst (§60); Performance Controller (§49); strategy research "investigate deterioration" (§59) | Deterministic detection in the Performance Controller; AI interpretation and attribution in the Performance Analyst. | RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): PFC-007 |
| DUP-15 | Model cost and performance tracking | Model Evaluation (§61); AI Cost Manager (§62); Model Router (§63) | Evaluation and cost are measurement services feeding the router (see TC-02). | RESOLVED — [DEC-013](../decisions/DEC-013-ai-organization.md): deterministic services (MEV-003, COST-002, RTR-003) |
| DUP-16 | Reconciliation | Execution Engine (§39); Recovery and Reconciliation (§71); custody reconciliation (§84) | Recovery and Reconciliation owns reconciliation logic; Execution invokes it (EXE-006). | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): REC-008, EXE-007 |
| DUP-17 | Realized P&L | Portfolio (§24); ledger (§85, conditional) | Depends on OQ-02. If a ledger exists, it is authoritative for realized P&L (LED-003). | RESOLVED — [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md): ledger authoritative (LED-006) |
| DUP-18 | Strategy research and candidate creation | Strategy Factory (§35); Research (§37); AI agents (§58, §59) | Strategy Factory owns the process and lifecycle; AI agents are assistants inside it. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): STR-012 |
| DUP-19 | Position sizing | Quantitative Engine (§12); Risk Engine (§25); Directional (§05) | Quant computes; Directional proposes; Risk enforces limits. | RESOLVED — [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): RSK-011 |
| DUP-20 | Directional responsibilities that are shared capabilities | Directional §05: strategy selection, backtesting, paper trading, performance analysis, strategy improvement, strategy monitoring vs shared strategy lifecycle (§04, §34–§35), Backtesting (§33), Paper Trading (§32), Performance Controller (§49) | Directional provides the directional-specific parts and uses the shared systems (ARCH-003). | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): DIR-004 |
| DUP-21 | Record of detected and rejected opportunities | Arbitrage opportunity database (§44); event and decision history (§87) | Event history is the audit record; the opportunity database is an analytical store linked to it. They must not diverge. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): AUD-005, ARB-014 |
| DUP-22 | Histories kept in AI memory | AI memory: policy history, strategy history, model evaluations, system state (§68); Policy System (§30); Strategy Management (§36); Model Evaluation (§61) | Memory references the canonical owners (MEM-004); it is never the authority. | RESOLVED — [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md): MEM-005 |
