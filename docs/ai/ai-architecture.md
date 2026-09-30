# AI Intelligence Layer

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-22 · **Category:** AI · **Roadmap stage:** AI INTELLIGENCE · **Sources:** §51–§53
>
> Canonical location for AI per §98 (`docs/ai/`).

Canonical definition of what AI is for, the hard boundary it may never cross, and when it is activated.

| Topic | Document |
|---|---|
| Responsibilities, hard-safety boundary, activation | this document |
| Hallucination Firewall, structured output, multi-agent validation, confidence calibration | [AI output validation](ai-output-validation.md) |
| Model routing, model evaluation, AI cost | [Model management](model-management.md) |
| Agent roster and overlap analysis | [Agents](agents.md) |
| AI memory / knowledge | [AI memory](ai-memory.md) |
| Model health vs strategy health | [Performance Controller](../systems/performance-controller.md) (PFC-005) |

## Role of AI

- **AIL-001** AI responsibilities · SYSTEM REQUIREMENT · §51 — AI responsibilities may include: market interpretation; research; strategy discovery; hypothesis generation; backtest interpretation; news analysis; sentiment; complex reasoning; strategy improvement proposals; failure investigation; performance interpretation; research coordination.
- **AIL-002** AI proposes, deterministic infrastructure enforces · CONFIRMED ARCHITECTURAL PRINCIPLE · §51 — AI proposes and analyzes. Deterministic infrastructure enforces.

## Hard-safety boundary

- **AIL-003** What AI must never do · CONSTRAINT · §52 — AI must not: bypass risk; increase authorized risk; disable kill switches; override user hard restrictions; submit unrestricted arbitrary orders; deploy unvalidated strategies; modify protected test boundaries; assume unsupported claims are facts; assume execution succeeded; receive unrestricted secrets.

The same boundary appears elsewhere as system-level rules: RSK-003 (AI cannot bypass risk), EXE-003 (never trust an AI claim of order success), STR-002 (no AI shortcut through the lifecycle), SEC-002 (no unrestricted credentials for AI agents). These statements agree with each other.

## Event-driven activation

- **AIL-004** No per-tick AI · CONSTRAINT · §53 — AI must not inspect every market tick unnecessarily.
- **AIL-005** Event-driven activation · CONFIRMED ARCHITECTURAL PRINCIPLE · §53 — Preferred architecture: high-volume market events → deterministic processing → filtering → significant event → AI reasoning if justified.

Consistent with OPP-008 (AI activated only when its reasoning adds meaningful value) and PERF-004 (AI should not unnecessarily block latency-sensitive execution).

## Decisions applied (2026-09-30)

- **AIL-006** AI gateway · CONFIRMED REQUIREMENT · DEC-013 — All AI calls go through one AI gateway. It abstracts providers; holds AI credentials, kept separate from trading credentials; enforces budgets and rate limits set by the AI Cost Manager; records prompts and outputs in the audit trail; validates outputs against their contracts (AIV-004); and applies timeouts and fallbacks.
- **AIL-007** Provider-agnostic · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-009 — The platform is not tied to one AI provider. Providers and models are configuration, chosen by the Model Router from Model Evaluation results.

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **AIL-008** AI Resource & Decision Governor · SYSTEM REQUIREMENT · P2§12 — The AI Resource & Decision Governor remains part of the architecture. It should control, where applicable: whether AI is required; AI call frequency; AI budgets; model selection; agent activation; context size; scheduling; caching; failover; degradation; cost limits; task prioritization; financial-consequence-aware escalation. The system must avoid unnecessary AI consumption.
- **AIL-009** Governor placement · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — The Governor is the deterministic admission and resource-control component of the AI gateway (AIL-006), not a second gateway. It decides whether an AI task runs and with what context, priority, schedule, cache use, and degradation level. It enforces the budgets and limits set by the AI Cost Manager (COST-002) and delegates model selection to the Model Router (RTR-003).
- **AIL-010** AI result caching · SYSTEM REQUIREMENT · P2§16 — AI results should be cached where appropriate. Caching must account for: context; market state; timestamp; data version; model version; prompt version; validity period; financial consequence. Stale AI output must not be treated as current truth.
- **AIL-011** AI failover · CONFIRMED REQUIREMENT · P2§17, P2§127, P2§270 — If an AI provider becomes unavailable: is AI required? If not, deterministic operation continues. If it is, use a fallback model, or WAIT, or NO TRADE. The failure of an AI provider must not automatically cause uncontrolled system failure; core trading must remain independently operable where possible.
- **AIL-012** AI degradation states · SYSTEM REQUIREMENT · P2§18 — The system should define graceful AI degradation states. Examples: full AI operation; reduced AI; fallback model; deterministic-only operation; research-only AI; no-trade where AI is mandatory.
- **AIL-013** Tool-first AI access · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§109, P2§298 — AI agents interact with deterministic systems through controlled tools: AI agent → tool request → schema validation → authorization → deterministic service → result. AI should not receive arbitrary operating-system access to production infrastructure.
- **AIL-014** AI does not promote production changes · CONSTRAINT · P2§111, P2§300 — AI must not independently promote production changes unless explicitly authorized by the approved deployment architecture.
- **AIL-015** AI hosting independence · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§269 — AI may run locally, remotely, or through providers, depending on the approved architecture.
- **AIL-016** AI activation triggers · SYSTEM REQUIREMENT · P2§275 — AI triggers may include: regime transition; major news; unusual volatility; conflicting signals; strategy deterioration; complex portfolio state; significant opportunity; research events; failure investigation.
- **AIL-017** AI request flow · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§315 — Event → opportunity / research filter → does this require AI? If not: deterministic path. If it does: AI Resource Governor → task classification → Model Router → specialized agent → structured output → hallucination / evidence validation → multi-agent validation where required → deterministic system → accept / reject / wait.

Notes:

- **AIL-012 vs System Health.** "AI DEGRADED" in HLT-011 is an observed health condition. The AI degradation state of AIL-012 is the operating level the Governor chooses in response. The two are different things and are not merged.
- **AIL-014.** The approved deployment architecture gives promotion to the deterministic Governance and Readiness Engine (STR-019, RDY-006), never to an AI component.
- **P2§26 / P2§276 (no AI on every tick)** is AIL-004, with OPP-004 and PERF-004.

## Boundary (§92)

- **Owns:** AI reasoning, research, and proposals, always as *input* to deterministic systems.
- **Must not:** anything in AIL-003.
- **Failure behavior (§91 example):** if AI is unavailable, deterministic capabilities continue where safe (HLT-005).
- **Not yet specified:** the specific providers and models (chosen in the AI INTELLIGENCE stage by measurement, AIL-007), interfaces, tests. The AI gateway is AIL-006.
