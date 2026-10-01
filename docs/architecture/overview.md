# Architecture Overview

> **Status:** DOCUMENTED (Handoff Parts 1, 2, and 3) — conceptual architecture; no implementation exists · **Owner:** platform architecture (cross-cutting) · **Sources:** §03, §04, §08, §69, §70, §79, §92–§94, §96–§98; Part 3: P3§444, P3§467–P3§470, P3§540
>
> Canonical home for the structural principles that apply to every system. System-specific rules live in each system's own specification; this document links to them rather than restating them.

## Shape of the platform

The platform has three trading systems on top of shared infrastructure (§03):

```text
                 AUTONOMOUS TRADING PLATFORM
                           |
          +----------------+----------------+
          |                |                |
     DIRECTIONAL     CROSS-EXCHANGE    TRIANGULAR
       TRADING        ARBITRAGE         ARBITRAGE
          |                |                |
          +----------------+----------------+
                           |
                  SHARED INFRASTRUCTURE
                           |
 DATA / QUANT / STRATEGY / CAPITAL / RISK /
 PORTFOLIO / EXECUTION / AI / STORAGE /
 MONITORING / RECOVERY / SECURITY
```

Every system and capability named in Part 1, with its category, owner, and canonical document, is listed in the [system registry](system-registry.md). How they depend on each other is in the [dependency map](dependency-map.md).

- **ARCH-001** Multiple trading systems · CONFIRMED ARCHITECTURAL PRINCIPLE · §03 — The platform contains multiple trading systems: A. Directional Trading (trades based on validated directional opportunities); B. Cross-Exchange Arbitrage (trades executable discrepancies between venues); C. Triangular Arbitrage (trades executable multi-leg opportunities within a venue/market graph).
- **ARCH-002** One platform, not three applications · CONSTRAINT · §03 — These systems share infrastructure. They must not become three unrelated applications.
- **ARCH-003** Reuse of common infrastructure · CONFIRMED ARCHITECTURAL PRINCIPLE · §04 — Trading systems must reuse common infrastructure. They must not independently recreate: market-data ingestion; data normalization; quantitative calculations; risk enforcement; capital accounting; portfolio accounting; exchange connectivity; execution; logging; monitoring; storage; recovery; reconciliation; security; strategy lifecycle; AI infrastructure.
- **ARCH-004** Ownership split · CONFIRMED ARCHITECTURAL PRINCIPLE · §04 — A trading system owns its trading behavior. Shared infrastructure owns common platform capabilities.
- **ARCH-016** Duplication control · CONFIRMED ARCHITECTURAL PRINCIPLE · §97 — Shared capability must be implemented once where appropriate. Directional Trading and Arbitrage both consume the shared Risk Engine. Likewise capital; execution; portfolio; market data; quantitative calculations; monitoring; storage; recovery must not be unnecessarily duplicated.

## Layer separation

- **ARCH-008** Canonical conceptual flow · CONFIRMED ARCHITECTURAL PRINCIPLE · §70 — Data → quantitative computation → opportunity → strategy → AI reasoning → capital / risk → execution → external venue → reconciliation → portfolio state.
- **ARCH-009** Explicit layer authority · CONSTRAINT · §70 — Each layer must have explicit responsibility. No layer silently assumes another layer's authority.

Part 1 describes this flow in five places that did not fully agree (CF-01, CF-02, CF-03). They are reconciled into one canonical runtime order in [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md).

## What is deterministic and what belongs to AI

This summarizes rules defined in the linked documents. It adds no new rules.

| Deterministic (no LLM required) | AI (proposes and analyses; never enforces) |
|---|---|
| Market data pipeline — [market-data](../systems/market-data.md) | Market interpretation, research, hypothesis generation, news/sentiment — [AI architecture](../ai/ai-architecture.md) |
| Quantitative calculations — [quantitative engine](../systems/quantitative-engine.md) (QNT-003: if deterministic is possible, do not ask an LLM) | Trade proposals (Trading Director) and challenges (Devil's Advocate) — [agents](../ai/agents.md) |
| High-volume opportunity screening — [opportunity detection](../systems/opportunity-detection.md) | Strategy research and improvement proposals, always through the formal lifecycle — [strategy management](../systems/strategy/strategy-management.md) |
| Risk enforcement — [risk engine](../risk/risk-engine.md) | Interpreting natural-language instructions into proposed policy — [NL policy interface](../systems/policy/natural-language-policy-interface.md) |
| Execution — [execution engine](../systems/execution-engine.md) | Performance interpretation — [agents](../ai/agents.md) |
| Policy enforcement — [policy system](../systems/policy/policy-system.md) | |

AI output crosses into the deterministic side only through validated, structured contracts ([AI output validation](../ai/ai-output-validation.md)), and the deterministic Risk Engine keeps final authority ([risk hierarchy](../risk/risk-engine.md)). The Market Regime Engine is deterministic (RGM-005, [DEC-011](../decisions/DEC-011-ownership-of-shared-responsibilities.md)). The technology used for all of this is in the [technology stack](technology-stack.md).

## Deterministic core and AI intelligence layer (Handoff Part 2)

- **ARCH-019** Deterministic core and AI layer are distinct · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§2, P2§196 — The distinction between the deterministic trading core and the AI intelligence layer is a foundational architectural principle and must remain explicit throughout the repository. The deterministic core owns functions where correctness, repeatability, financial accuracy, timing, enforcement, and safety are critical. Where applicable these include: market-data ingestion; WebSocket management; market-data normalization; data validation; data-quality scoring; data quarantine; data lineage; timestamp validation; time synchronization; market-data storage; quantitative calculations; indicators; feature calculations; regime classification; opportunity calculations; true net profitability; fee calculations; slippage calculations; liquidity calculations; market-impact calculations; funding calculations; position sizing; exposure calculations; capital availability; capital reservation; portfolio state; order validation; order execution; exchange communication; order reconciliation; position reconciliation; balance reconciliation; risk limits; capital limits; kill switches; safe modes; no-new-position mode; policy enforcement; audit logging; persistent financial state; backtesting; paper trading; deterministic monitoring; recovery; reconciliation; failure handling. The AI layer provides intelligence where interpretation, research, reasoning, synthesis, or hypothesis generation is useful. Where applicable this includes: market interpretation; research; strategy discovery; hypothesis generation; strategy analysis; news analysis; sentiment/context analysis; complex event interpretation; failure analysis; strategy improvement proposals; research prioritization; model evaluation; opportunity interpretation; portfolio contextual reasoning; Devil's Advocate analysis; trading proposals. AI must not replace deterministic authorities.
- **ARCH-020** AI is never the financial source of truth · CONSTRAINT · P2§3, P2§197 — AI must never become authoritative for: account balance; available capital; reserved capital; position size; position state; order state; fill state; fees; slippage; P&L; exposure; risk limits; capital reservations; net profitability; ledger balances; reconciliation state; policy enforcement; kill-switch state. AI may interpret these values and may propose actions based on them. It cannot redefine them.
- **ARCH-021** Deterministic operation without AI · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§4, P2§198 — The core platform should remain capable of performing functions that do not genuinely require intelligence. The normal path is market data → validation → normalization → quant → regime → opportunity → net economics → risk → capital → execution, not market tick → LLM → calculate spread → LLM → calculate fees → LLM → trade. AI is introduced only when interpretation or reasoning is genuinely useful.
- **ARCH-022** Deterministic/AI responsibility table · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§339 — Responsibilities are divided between the deterministic core and the AI layer as in the table below.

| Responsibility | Deterministic core | AI layer |
|---|---|---|
| Market data | Authoritative | Interpret |
| Indicators | Calculate | Interpret |
| Fees | Calculate | Explain |
| Slippage | Calculate | Analyze |
| Net profitability | Calculate | Interpret |
| Risk limits | Enforce | Propose/analyze |
| Capital | Authoritative | Consume information |
| Position state | Authoritative | Interpret |
| Order state | Authoritative | Interpret |
| Execution | Execute | Propose |
| Policy enforcement | Enforce | Interpret user intent |
| Strategy research | Support data | Primary intelligence role |
| Strategy proposal | Validate | Generate |
| Strategy deployment | Control | Propose |
| News analysis | Provide source/data | Analyze |
| Market interpretation | Provide facts | Interpret |
| Reconciliation | Authoritative | Diagnose |
| Ledger | Authoritative | Read/analyze |
| Audit | Authoritative | Contribute metadata |
| Kill switch | Deterministic | Cannot override |
| Safe mode | Deterministic | Cannot override |
| AI selection | N/A | Router/Governor |
| Model evaluation | Deterministic metrics + AI analysis | Analyze |
| Research | Infrastructure | Intelligence |
| Live execution | Deterministic | Advisory/proposal |
| Self-improvement | Controlled pipeline | Generate candidates |
| Paper execution | Deterministic simulator | Analyze |
| Readiness | Authoritative gate | Provide analysis |
| Dashboard | Deterministic aggregation | Summarize/interpret |

**How the table was read.** In the received handoff the table's cell boundaries were lost (for example "Market dataAuthoritativeInterpret"; see the [historical copy](../handoffs/part-2-consolidated-additional-systems.md), §339). The rows above restore the boundaries at the joins between words; no word was added, removed, or changed. "Router/Governor" in the AI column names the deterministic Model Router and AI Resource & Decision Governor that belong to the AI layer (RTR-003, AIL-009). The "AI analysis" of model evaluation is done by the Performance Analyst (model contribution, AGT-014) on the deterministic metrics of Model Evaluation (MEV-003).

- **ARCH-023** Event-driven architecture · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§126, P2§273 — The system should be event-driven, using events instead of unnecessary polling. Examples: market update → opportunity evaluation; risk state change → strategy evaluation; exchange degradation → venue eligibility change; policy change → policy recompilation; strategy degradation → strategy review.
- **ARCH-024** End-to-end platform architecture · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§314 — The complete high-level architecture is: user → natural-language policy → policy compiler / validation → structured policy → global platform controller → whole-market universe → market data → data validation → quantitative engine → regime engine → opportunity engine → opportunity filter → strategy engine → AI intelligence when justified → trade / opportunity proposal → deterministic validation → risk authority → capital authority → execution engine → exchange adapter → venue → reconciliation → portfolio / ledger → monitoring → performance analysis → controlled improvement → validation → paper → canary → production.

ARCH-021 and ARCH-024 are conceptual flows, like ARCH-008. The runtime order of the pre-trade steps stays the one in [DEC-010](../decisions/DEC-010-pre-trade-decision-flow.md): the Global Capital Authority checks availability, the Risk Engine authorizes and sizes, and only then is capital reserved. Part 2's "risk → capital" matches that order, since risk authorizes before capital is reserved (DEC-024). The "global platform controller" is defined by ARCH-035 (OQ-24, decided by the owner).

## Market monitoring vs operational monitoring

- **ARCH-005** Two kinds of monitoring · CONFIRMED ARCHITECTURAL PRINCIPLE · §08 — The system must distinguish Market Monitoring ("What is happening across the trading universe?") from Operational Monitoring ("Is the platform itself functioning correctly?"). These must remain separate.

Market monitoring is owned by the [Opportunity Detection Engine](../systems/opportunity-detection.md). Operational monitoring is owned by [Monitoring and Observability](../operations/monitoring-and-observability.md) and [System Health](../operations/system-health.md).

## Cross-cutting engineering rules

- **ARCH-010** Numerical precision · CONFIRMED REQUIREMENT · §79 — Financial calculations must be deterministic and precise. Includes: prices; quantities; fees; slippage; P&L; position sizing; exposure; leverage; risk; reservations; arbitrage economics; portfolio accounting.
- **ARCH-011** Exchange-specific precision · CONSTRAINT · §79 — Exchange-specific precision must be respected.
- **ARCH-006** Consistency and anti-drift · CONFIRMED REQUIREMENT · §69 — The platform must preserve consistency as the project grows. The architecture should maintain: canonical definitions; versioned requirements; explicit ownership; traceability; dependency mapping; conflict detection; decision records; strategy versions; policy versions; model versions; interface contracts.
- **ARCH-007** Changes checked against architecture · CONSTRAINT · §69 — Changes must be checked against existing architecture before acceptance.

Failure handling and controlled degradation are defined in [System Health](../operations/system-health.md). Performance and latency are defined in [Performance, Latency and Continuous Operation](performance-and-latency.md). Security is defined in [Security Architecture](../security/security-architecture.md).

## Ownership and traceability rules

- **ARCH-012** System boundary definition · CONFIRMED ARCHITECTURAL PRINCIPLE · §92 — Every system must define: purpose; responsibility; inputs; outputs; dependencies; interfaces; data owned; data consumed; data produced; allowed actions; forbidden actions; failure behavior; tests; roadmap stage.
- **ARCH-013** Feature ownership chain · CONFIRMED ARCHITECTURAL PRINCIPLE · §93 — For every feature: what responsibility → which system owns it → which document defines it → which module implements it → which requirement tracks it → which roadmap stage → which test verifies it. This prevents duplicate implementation.
- **ARCH-014** Dependencies respected · CONFIRMED ARCHITECTURAL PRINCIPLE · §94 — Dependencies must be respected.
- **ARCH-015** Feature classification · CONFIRMED REQUIREMENT · §96 — Every feature must be classified as one of: CONFIRMED REQUIREMENT; CONFIRMED ARCHITECTURAL PRINCIPLE; CONSTRAINT; SYSTEM REQUIREMENT; PROPOSED; FUTURE; PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION; OPEN QUESTION; TECHNICAL CONCERN; DEPRECATED / REPLACED. No silent classification changes.
- **ARCH-017** Canonical source of truth · CONFIRMED ARCHITECTURAL PRINCIPLE · §98 — Major domains require authoritative locations. Other documents should reference the authoritative source.

Where these are applied: the §94 example chain and every recorded dependency are in the [dependency map](dependency-map.md) (ARCH-014); classification rules are in the [requirements README](../requirements/README.md) (ARCH-015); the canonical location of every concept is in the [source-of-truth map](source-of-truth-map.md) (ARCH-017).

Every system specification in `docs/systems/`, `docs/risk/`, `docs/ai/`, `docs/security/` and `docs/operations/` records the §92 fields that Part 1 supplies and lists the rest as not yet specified. Part 2 did not provide interfaces or contracts; they are defined contract-first when each stage is planned (ARCH-025).

- **ARCH-035** Global platform controller · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-027 — The "global platform controller" of ARCH-024 and RMP-009 is not a separate system. It names three existing parts working together: the Policy System, which applies the operator's policy (POL-008, POL-011); the Risk Engine's emergency controller, which sets the safety level (RSK-020); and System Health, which tracks the platform's state (HLT-010).

ARCH-035 is the owner's answer to OQ-24 ([DEC-027](../decisions/DEC-027-part-2-open-questions.md)).

## Contracts, governance, and consistency (Handoff Part 2)

- **ARCH-025** Contract-first development · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§120 — Core interfaces should be defined before implementations where practical. Examples: market-data contract; order contract; position contract; risk contract; capital contract; opportunity contract; strategy contract; AI tool contract; exchange adapter contract.
- **ARCH-026** Interface versioning · CONSTRAINT · P2§121 — Important interfaces should support versioning. Breaking changes must be explicit. Historical data and strategies must not silently break because an interface changed.
- **ARCH-027** Canonical authorities · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§184, P2§293 — Fundamental authorities are centralized. There is one each of: Capital Authority; Risk Authority; Portfolio Authority; Policy Authority; Fee Engine; Slippage Engine; exchange abstraction; audit system; market-data normalization layer; Strategy Registry; Readiness System; Opportunity Registry. Specialized systems may operate above these authorities.
- **ARCH-028** Central non-negotiable principles · CONFIRMED REQUIREMENT · P2§174, P2§295 — Central non-negotiable principles should be documented. Part 2 names: deterministic core; AI boundary; capital preservation; risk precedence; no fixed returns; true net profitability; unknown-state safety; controlled self-improvement; auditability; reconciliation; no duplicate authorities. Final naming is an architecture decision.
- **ARCH-029** No silent requirement promotion · CONSTRAINT · P2§181, P2§290 — A previously discussed idea must not automatically become an approved production requirement; ideas remain ideas until approved. For example, platform-managed accounts remain an architectural option unless formally approved.
- **ARCH-030** Requirements registry fields · CONFIRMED REQUIREMENT · P2§179, P2§288, P2§336 — There is one canonical requirements registry, and all approved requirements eventually enter it. Each requirement should contain: requirement ID; description; source; classification; owner; system; dependencies; status; priority; roadmap stage; verification method; related documents; approval state.
- **ARCH-031** Master traceability chain · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§187, P2§337 — One traceability system should connect: source → requirement → architecture → system → implementation → test → verification → roadmap → approval.
- **ARCH-032** Consistency system · CONFIRMED REQUIREMENT · P2§173, P2§294 — The project should eventually have a mechanism for detecting contradictions between: requirements; architecture; interfaces; schemas; strategies; policies; roadmap; tests; documentation. Exact implementation remains an architecture decision.
- **ARCH-033** Change-impact identification · CONFIRMED REQUIREMENT · P2§175, P2§296 — When a requirement changes, the affected architecture, interfaces, schemas, tests, roadmap, and documentation should be identified.
- **ARCH-034** Domain command language · PROPOSED · P2§176, P2§297 — A compact structured command language may eventually reduce repetitive orchestration. It must never bypass validation, authorization, audit, policy, risk, or schema validation. It remains a proposal until formally approved.

Where these stand today:

- **ARCH-027:** the one owner of each authority is listed in the [source-of-truth map](source-of-truth-map.md#canonical-authorities-arch-027).
- **ARCH-028:** the principles index is in the [platform overview](../product/platform-overview.md#non-negotiable-platform-principles-p2174-p2295-arch-028).
- **ARCH-030:** the [registry](../requirements/registry.md) holds ID, title, source, class, owner/system, specification, stage, status, and approval state. Dependencies are recorded between systems in the [dependency map](dependency-map.md); they will be recorded per requirement when interfaces are designed. The verification method is assigned when each stage is planned (constitution Rule 140). No priority is invented: order comes from the roadmap's dependency sequence (RMP-002, RMP-011).
- **ARCH-034:** the owner decided to keep it as an idea; it stays PROPOSED and nothing is built ([DEC-027](../decisions/DEC-027-part-2-open-questions.md)).
- **ARCH-032, ARCH-033:** the documentation checker in [`tools/docs/`](../../tools/docs/README.md) ([DEC-025](../decisions/DEC-025-documentation-tooling-in-repository.md)) is the first increment. It checks the documentation only, not code, schemas, or tests.

## Handoff Part 3 applied (2026-09-30)

New requirements from [Handoff Part 3](../handoffs/part-3-consolidated-autonomy-capital-scaling.md), cited as P3§N. Part 3 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 3 reconciliation](../traceability/part-3-reconciliation.md). Placement, duplicate, and conflict resolutions: [DEC-031](../decisions/DEC-031-part-3-reconciliation.md).

- **ARCH-036** Reversible where possible · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§444 — Execution must be reversible where possible. Architecture should support, where technically possible: cancellation; rollback; recovery; strategy suspension; deployment rollback; configuration rollback. Irreversible financial actions require stronger authorization boundaries.
- **ARCH-037** Additional canonical authorities · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§467 — In addition to the authorities of ARCH-027, the system should maintain one canonical authority for: execution state; the financial ledger where applicable.
- **ARCH-038** System Rules Register · CONFIRMED REQUIREMENT · P3§468 — The repository should contain a canonical System Rules Register. Each rule should have: rule ID; rule statement; classification; source; owner; related systems; dependencies; enforcement location; verification method; status.
- **ARCH-039** Rules are enforceable · CONFIRMED REQUIREMENT · P3§469, P3§470 — A rule should not exist only as prose. Where a rule is approved and machine-enforceable, the architecture should identify where, how, and when it is enforced, and what happens if it is violated. A violation may trigger: reject; block; safe mode; alert; suspend; rollback; human review; depending on severity.
- **ARCH-040** Traceability includes rules and interfaces · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§540 — In addition to the chain of ARCH-031, the final traceability system must connect the rule and the interface: source → requirement → rule → architecture → system → interface → implementation → test → verification → roadmap → approval.

Where these stand today:

- **ARCH-037:** execution state is owned by the Execution Engine (EXE-002, "execution-state management"); the financial ledger is the Trading Ledger (LED-004, LED-006). Both are added to the [source-of-truth map](source-of-truth-map.md#canonical-authorities-arch-027).
- **ARCH-038, ARCH-039:** the register is [`docs/requirements/system-rules-register.md`](../requirements/system-rules-register.md). It is an index: each rule's full wording stays in its canonical requirement, so the register never becomes a second copy (DUP-38). Enforcement location and violation handling are recorded per rule; the verification method is assigned when the owning stage is planned, as for every requirement (ARCH-030).
- **ARCH-040:** requirement → rule is the register's "canonical requirements" column. Rule → interface → implementation → test are filled in as each stage is built.
- **Rule precedence (P3§471)** is kept with the risk hierarchy it extends: RSK-048 in the [Risk Engine](../risk/risk-engine.md) (CF-17).
- **Feature extensibility (P3§401–P3§410, P3§462–P3§466, P3§472–P3§475, P3§508–P3§512)** is in [Architecture Governance](architecture-governance.md) (GOV).
- P3§514 (system boundary principle) is ARCH-012. P3§515 (final consolidated operating model) is ARCH-024, with ARCH-035 as its global controller and CAP-016 as its runtime order.

## Operating values ([DEC-020](../decisions/DEC-020-value-classification.md))

- **ARCH-018** Values are classified and configurable · CONSTRAINT · DEC-020 — Every concrete operating value in a requirement (percentages, durations, counts, latencies, thresholds, versions) is recorded in the values register with one classification: DEFAULT, DESIGN TARGET, POLICY-CONTROLLED PARAMETER, HARD LIMIT, IMPLEMENTATION CHOICE, or OBSERVED. No value becomes a permanent hard-coded requirement unless the owner explicitly approves it as such; the architecture supports configurable, evidence-driven values. Illustrative examples quoted from a source are not operating values.

The register is the [values register](../requirements/values-register.md).
