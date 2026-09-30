# AI Agents

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented. **Final roster decided: AGT-016 ([DEC-013](../decisions/DEC-013-ai-organization.md)).** · **System:** SYS-23 · **Roadmap stage:** AI INTELLIGENCE ("Agents", "Trading Director", "Devil's Advocate") · **Sources:** §54–§60
>
> §99 sketches `docs/ai/agents/` as a folder. One file is enough for Part 1's content; the split can happen when agent specifications grow (DEC-002).

Canonical definition of the AI agents and the overlap analysis that §54 requires before implementation.

## Roster

- **AGT-001** Previously discussed roster · DEPRECATED / REPLACED · §54 — Previously discussed AI responsibilities include: 1. Market Analyst; 2. Quant Research Agent; 3. Strategy Research Agent; 4. Trading Director; 5. Devil's Advocate; 6. Performance Analyst; 7. Strategy Optimizer; 8. Model Evaluation Agent; 9. Research Agent; 10. AI Cost Manager; 11. News/Sentiment Agent.
- **AGT-002** Find overlaps before implementation · CONFIRMED REQUIREMENT · §54 — Claude must identify overlapping responsibilities before implementation.
- **AGT-003** No duplicate agents · CONSTRAINT · §54 — The project must not create multiple agents doing essentially the same job without an explicit architectural reason.

## Overlap analysis (AGT-002)

Only six of the eleven agents have their own section in Part 1. The rest are names only, or map onto a capability section that does not say "agent".

| # | Agent | Defined in | Overlaps with | Finding |
|---|---|---|---|---|
| 1 | Market Analyst | §57 (AGT-008) | News/Sentiment Agent (news, event interpretation); Market Regime Engine (regime) | DUP-11, DUP-08 |
| 2 | Quant Research Agent | §58 (AGT-010) | Research Agent; Strategy Research Agent (hypothesis generation, strategy research, backtest interpretation) | DUP-13 |
| 3 | Strategy Research Agent | §59 (AGT-012, shared with #7) | Strategy Optimizer (same section); Quant Research Agent; Strategy Factory (STR-003) | DUP-12, DUP-13, DUP-18 |
| 4 | Trading Director | §55 (AGT-004) | — | — |
| 5 | Devil's Advocate | §56 (AGT-006) | — | — |
| 6 | Performance Analyst | §60 (AGT-014) | Performance Controller (deterioration, expected vs actual); Model Evaluation ("model contribution") | DUP-14 |
| 7 | Strategy Optimizer | §59 only, shared with #3 | Strategy Research Agent | DUP-12 |
| 8 | Model Evaluation Agent | §61 (MEV-001, not framed as an agent) | AI Cost Manager (cost); Model Router (model performance) | DUP-15, TC-02 |
| 9 | Research Agent | name only; §51 lists "research", "research coordination" | Quant Research Agent; Strategy Research Agent | DUP-13 |
| 10 | AI Cost Manager | §62 (COST-001, not framed as an agent) | Model Router (routing); Model Evaluation (cost) | DUP-15, TC-02 |
| 11 | News/Sentiment Agent | name only; §51 lists "news analysis", "sentiment" | Market Analyst ("relevant news", "event interpretation") | DUP-11 |

Every overlap above is resolved by [DEC-013](../decisions/DEC-013-ai-organization.md):

- **AGT-016** Final agent roster · CONFIRMED REQUIREMENT · DEC-013 — The platform has five AI agents. Market Analyst (including news and sentiment). Research Agent (quantitative research and strategy research/optimization, routed by task type). Trading Director. Devil's Advocate. Performance Analyst. Model Evaluation and the AI Cost Manager are deterministic services, not agents.

AGT-001 is replaced by AGT-016. The sections below keep the handoff's definitions as written. The Market Analyst section now also covers news and sentiment; the Quant Research Agent and strategy research/optimization sections both describe task types of the one Research Agent.

## Trading Director

- **AGT-004** Trading Director · SYSTEM REQUIREMENT · §55 — The Trading Director generates structured trade proposals. It may receive: market state; quantitative features; regime; liquidity; volatility; news; strategy state; portfolio state; existing positions; policy; risk state. It may propose: asset; action; strategy; strategy version; entry; stop; target; size; confidence; evidence; invalidation conditions; risk observations.
- **AGT-005** Proposals are validated deterministically · CONFIRMED ARCHITECTURAL PRINCIPLE · §55 — The deterministic system validates the proposal.

## Devil's Advocate

- **AGT-006** Devil's Advocate · SYSTEM REQUIREMENT · §56 — The Devil's Advocate challenges proposals. It should examine: false signals; weak volume; conflicting evidence; liquidity; spread; volatility; news risk; manipulation risk; regime mismatch; risk/reward; invalid assumptions; strategy deterioration.
- **AGT-007** Power to reject · CONFIRMED REQUIREMENT · §56 — It must be able to reject a proposal.

## Market Analyst

- **AGT-008** Market Analyst · SYSTEM REQUIREMENT · §57 — The Market Analyst interprets relevant market context. Responsibilities may include: market context; regime interpretation; event interpretation; cross-market relationships; relevant news; higher-level reasoning.
- **AGT-009** Does not replace quantitative calculation · CONSTRAINT · §57 — It must not replace deterministic quantitative calculations.

## Quant Research Agent

- **AGT-010** Quant Research Agent · SYSTEM REQUIREMENT · §58 — Assists with: quantitative research; hypothesis generation; feature exploration; backtest interpretation; statistical investigation; strategy research.
- **AGT-011** Does not replace the Quantitative Engine · CONSTRAINT · §58 — It does not replace the deterministic Quantitative Engine.

## Strategy research / optimization

- **AGT-012** AI strategy research and optimization · SYSTEM REQUIREMENT · §59 — AI may: generate candidates; analyze historical behavior; suggest improvements; compare variants; investigate deterioration; propose hypotheses.
- **AGT-013** Formal lifecycle required · CONSTRAINT · §59 — Every resulting strategy must pass the formal lifecycle.

The formal lifecycle is STR-001 in [Strategy Management](../systems/strategy/strategy-management.md).

## Performance Analyst

- **AGT-014** Performance Analyst · SYSTEM REQUIREMENT · §60 — Evaluates: strategy performance; trade outcomes; drawdown; execution quality; expected vs actual; opportunity quality; strategy deterioration; missed opportunities; model contribution.
- **AGT-015** Problem attribution · CONFIRMED REQUIREMENT · §60 — It must distinguish: strategy problem vs execution problem vs market problem vs data problem vs model problem vs infrastructure problem.

## Roles and who performs them (Handoff Part 2)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Where each Part 2 section went: [Part 2 reconciliation](../traceability/part-2-reconciliation.md).

- **AGT-017** Previously discussed roles retained · CONFIRMED REQUIREMENT · P2§6, P2§200 — The previously discussed roles remain: Market Analyst; Quant Research Agent; Strategy Research Agent; Trading Director; Devil's Advocate; Performance Analyst; Strategy Optimizer; Model Evaluation Agent; AI Cost Manager. Final decomposition must be based on documented ownership.
- **AGT-018** New agents need documented boundaries · CONSTRAINT · P2§6 — Additional agents must only be introduced after responsibility boundaries are documented. Multiple agents with substantially overlapping ownership must be avoided.
- **AGT-019** What the Trading Director may do · SYSTEM REQUIREMENT · P2§7, P2§201 — The Trading Director may: interpret validated information; consider strategy context; consider market context; produce structured trade proposals; explain reasoning; request additional analysis; coordinate specialized agents.
- **AGT-020** What the Trading Director must not do · CONSTRAINT · P2§7, P2§201 — The Trading Director must not: submit unrestricted orders; override risk; override capital authority; override user hard policy; modify financial records; change production strategy outside the approved improvement process; bypass deterministic execution validation.
- **AGT-021** Additional analysis areas · SYSTEM REQUIREMENT · P2§73 — In addition to AGT-014, the Performance Analyst analyzes: rejection quality; false opportunities; slippage; fees; latency; regime-specific behavior.
- **AGT-022** Permission scopes · SYSTEM REQUIREMENT · P2§110, P2§299 — Each role has minimum-privilege permission scopes. Examples: Market Analyst — read market information; Strategy Research — read historical data; Trading Director — read validated decision context and create proposals; Performance Analyst — read execution/performance data; Strategy Optimizer — create research candidates. The prohibitions that apply to every research agent are in SEC-008.

The documented decomposition (AGT-017) is the one of [DEC-013](../decisions/DEC-013-ai-organization.md): five agents plus three deterministic services (Model Router, Model Evaluation, AI Cost Manager). [DEC-024](../decisions/DEC-024-part-2-reconciliation.md) confirms it against Part 2 (DUP-23). Every role is kept; none is dropped. AGT-017 does not revive AGT-001: that list of separate agents stays replaced by AGT-016. AGT-017 keeps the roles, and the table shows which agent or service performs each.

| Role (P2§6) | Performed by |
|---|---|
| Market Analyst | Market Analyst agent (AGT-008) |
| Quant Research Agent | Research Agent, quantitative-research tasks (AGT-010) |
| Strategy Research Agent | Research Agent, strategy-research tasks (AGT-012), inside the Strategy Factory (STR-012) |
| Strategy Optimizer | Research Agent, optimization tasks (AGT-012), inside the Strategy Factory (STR-012) |
| Trading Director | Trading Director agent (AGT-004, AGT-019, AGT-020) |
| Devil's Advocate | Devil's Advocate agent (AGT-006) |
| Performance Analyst | Performance Analyst agent (AGT-014, AGT-021) |
| Model Evaluation Agent | Deterministic Model Evaluation service (MEV-003, MEV-004); AI analysis of the results by the Performance Analyst ("model contribution", AGT-014) |
| AI Cost Manager | Deterministic AI Cost Manager service (COST-002), enforced by the AI Resource & Decision Governor (AIL-009) |

When the Research Agent works on a task, it holds only the permission scope of the role that task belongs to (AGT-022). The Trading Director's "coordinate specialized agents" means coordinating analysis for a trade proposal (the AIV-007 chain). Research coordination belongs to the Strategy Factory (STR-012).

## Rules that apply to every agent

The hard-safety boundary (AIL-003), structured and validated output (AIV-004 to AIV-006), the Hallucination Firewall (AIV-001 to AIV-003), and no unrestricted credentials (SEC-002).
