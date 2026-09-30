# AI Agents

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented. **The roster itself is PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION.** · **System:** SYS-23 · **Roadmap stage:** AI INTELLIGENCE ("Agents", "Trading Director", "Devil's Advocate") · **Sources:** §54–§60
>
> §99 sketches `docs/ai/agents/` as a folder. One file is enough for Part 1's content; the split can happen when agent specifications grow (DEC-002).

Canonical definition of the AI agents and the overlap analysis that §54 requires before implementation.

## Roster

- **AGT-001** Previously discussed roster · PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION · §54 — Previously discussed AI responsibilities include: 1. Market Analyst; 2. Quant Research Agent; 3. Strategy Research Agent; 4. Trading Director; 5. Devil's Advocate; 6. Performance Analyst; 7. Strategy Optimizer; 8. Model Evaluation Agent; 9. Research Agent; 10. AI Cost Manager; 11. News/Sentiment Agent.
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

The final roster is OQ-11. No agent is to be built until it is resolved (AGT-003).

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

## Rules that apply to every agent

The hard-safety boundary (AIL-003), structured and validated output (AIV-004 to AIV-006), the Hallucination Firewall (AIV-001 to AIV-003), and no unrestricted credentials (SEC-002).
