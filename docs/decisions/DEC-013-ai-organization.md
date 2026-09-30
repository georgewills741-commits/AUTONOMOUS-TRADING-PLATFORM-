# DEC-013 — AI organization: agent roster, deterministic model services, AI gateway, output contract, validation policy

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Date:** 2026-09-30
- **Resolves:** DUP-11, DUP-12, DUP-13, DUP-14, DUP-15, OQ-11, OQ-12, OQ-14, OQ-18, CF-04, TC-02, TC-06

## Agent roster (OQ-11, DUP-11 to DUP-15)

Eleven previously discussed agents become **five agents** plus **three deterministic services** (AGT-016). AGT-001 is marked DEPRECATED / REPLACED.

| Agent | Absorbs | Why it is a separate agent |
|---|---|---|
| Market Analyst | News/Sentiment Agent | Same inputs and output (market context interpretation) |
| Research Agent | Quant Research Agent, Strategy Research Agent, Strategy Optimizer, Research Agent | Same boundary (research inside the Strategy Factory) and constraints; they differ only by task type, which the Model Router can route |
| Trading Director | — | Only agent that produces trade proposals (§55) |
| Devil's Advocate | — | Must stay independent of the proposer to be able to reject (§56) |
| Performance Analyst | — | AI interpretation and root-cause attribution (§60); detection itself is deterministic (PFC-007) |

**Deterministic services, not agents (TC-02):** Model Evaluation (MEV-003), AI Cost Manager (COST-002), and Model Router (RTR-003). Their work is measurement, accounting, and rules (QNT-003; constitution Rules 87 and 201). "Research coordination" (§51) belongs to the Strategy Factory (STR-012).

## AI gateway (OQ-14)

The single access point for all AI calls (AIL-006). It:
- abstracts providers;
- holds AI credentials, kept apart from trading credentials;
- enforces budgets and rate limits set by the AI Cost Manager;
- records prompts and outputs in the audit trail;
- validates outputs against their contracts;
- applies timeouts and fallbacks.

It is provider-agnostic (AIL-007).

## Output contract (CF-04, OQ-12)

- The Decision field allows BUY, SELL, HOLD, NO_TRADE, WAIT, UNCERTAIN, and INSUFFICIENT_EVIDENCE.
- AI may also *recommend* REDUCE_RISK or SUSPEND_STRATEGY, for deterministic systems to evaluate (AIV-013).
- UNCERTAIN and INSUFFICIENT_EVIDENCE always mean no new position (RSK-014).
- Arbitrage is deterministic end to end. AI never proposes or approves arbitrage trades (ARB-013), so no multi-leg AI contract is needed.

## Validation policy (OQ-18)

- "Important decisions" are:
  - every AI-originated trade proposal;
  - every AI-proposed strategy change;
  - every AI interpretation of policy that would loosen a constraint (AIV-015).
- Every AI-originated trade proposal gets a mandatory Devil's Advocate review. Unresolved disagreement means NO TRADE (AIV-014).
- Premium-model confirmation is required when the capital at risk exceeds an operator-configured threshold. This threshold is on capital, not profit, so it does not conflict with TNP-005.

## Evidence identifiers (TC-06)

Every stored data item and calculation output carries a stable identifier, source, and timestamp (MKD-005), so AI claims can cite them (AIV-001).
