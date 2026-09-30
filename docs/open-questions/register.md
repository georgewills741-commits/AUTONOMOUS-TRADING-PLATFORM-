# Open Questions and Technical Concerns

> **Status:** ACTIVE register. Last updated 2026-09-30 after processing Handoff Part 1.
>
> Missing information is recorded here rather than invented (constitution Rules 32 and 183). Many items may be answered by Handoff Part 2, which promises "deeper subsystem specifications, interfaces/contracts, complete dependency mapping, implementation-stage mapping, verification architecture, and remaining production requirements". Re-check every item after Part 2 arrives. When an item is answered, mark it ANSWERED with the source and the changed documents. Do not delete it (Rule 179).

## Open questions (OQ)

"Blocks" names what cannot be specified or built until the question is answered.

| ID | Question | Sources | Blocks | Status |
|---|---|---|---|---|
| OQ-01 | Is the platform-account / custody model confirmed or rejected? Does the platform serve one operator or many users? What compliance scope applies if custody is retained? | §84, §85, §89 ("user accounts") | Custody, ledger, key management, security scope, SEC-001 user accounts | OPEN |
| OQ-02 | Is an authoritative ledger required even if the platform is not user-facing? §22's compounding flow passes through "accounting / ledger", but §85 makes the ledger conditional. | §22, §85 | CAP-012, DUP-17 | OPEN |
| OQ-03 | Which venues are in scope (Binance, OKX, and Coinbase were previously discussed), and how is the "configured" / "authorized" trading universe defined, and by whom? | §02, §08, §42 | Exchange adapters, universe scanning | OPEN |
| OQ-04 | Which instruments are in scope: spot only, or margin, perpetuals, or other derivatives? Funding rates, funding costs, leverage limits, and positions imply more than spot, but it is never stated. | §10, §13, §25, §42, §79 | Adapters, risk limits, economics, portfolio model | OPEN |
| OQ-05 | What is the formal true-net-profit formula? §13 says it "must be formally defined". | §13 | TNP-003, TC-01 | OPEN |
| OQ-06 | What is the "global safety architecture"? Which system owns kill switches, emergency shutdown, safe mode, and trading halt? | §25, §27, §47, §74 | DUP-04, HLT-002, RSK-002 | OPEN |
| OQ-07 | What is the final health state machine: transitions, DEGRADED vs WARNING, and how subsystem-degraded states combine with overall state? | §74 | HLT-002 | OPEN |
| OQ-08 | Who owns the operating mode? What are the transition rules and approvals, and how is SUPERVISED authorization given? Can strategies run in different modes at once? How do modes relate to lifecycle stages and to constitution environments (Rule 109)? | §31, §34 | MODE-001, MODE-002 | OPEN |
| OQ-09 | What is "canary" (scope, capital, duration, promotion criteria)? | §34, §38, §95 | STR-001, STR-009, deployment | OPEN |
| OQ-10 | Is the Market Regime Engine deterministic? By what method are regimes classified? | §11, §95 | RGM-001 to RGM-004, DUP-08 | OPEN |
| OQ-11 | What is the final AI agent roster after overlap resolution? | §54 | AGT-001, DUP-11 to DUP-15 | OPEN |
| OQ-12 | How should the AI output contract express uncertainty (WAIT, UNCERTAIN, I DON'T KNOW) and non-directional (multi-leg arbitrage) decisions? | §27, §65, §07 | CF-04, AIV-005 | OPEN |
| OQ-13 | What are reporting and alerts (audience, contents, channels)? They are named but never defined. | §01, §02 item 22, §95 | PLT-004 item 22, monitoring | OPEN |
| OQ-14 | What is the "AI gateway" listed in §95? It is not described anywhere else. | §95 | AI INTELLIGENCE stage scope | OPEN |
| OQ-15 | What is `docs/product/trading-policy.md` meant to contain, as distinct from `docs/systems/policy/`? | §98 | CF-08 | OPEN |
| OQ-16 | What is the technology stack: languages, storage, messaging, AI providers/models, deployment platform? Part 1 names none (constitution Rule 104). | — | All implementation | OPEN |
| OQ-17 | Which policy changes are "important", and when are simulation and confirmation "required"? Who confirms? | §30 | POL-004 | OPEN |
| OQ-18 | Which multi-agent validation policy applies to which decisions? What makes a decision "important"? | §66 | AIV-007, AIV-008 | OPEN |
| OQ-19 | What are the performance targets: latency budgets, throughput, universe size? | §75–§78 | PERF-006 | OPEN |
| OQ-20 | What rules make up "system safety", the top layer of the risk hierarchy? | §26 | RSK-004 | OPEN |
| OQ-21 | Which directional strategies, timeframes, and instruments come first? | §05 | DIR-002 | OPEN |
| OQ-22 | What is the storage architecture and data retention? What are the historical data sources for backtesting? "Storage" and "logging" are named as shared infrastructure but not defined. | §03, §04, §10, §33, §95, §97 | MKD-003, BKT-001, AUD-003 | OPEN |
| OQ-23 | Is the interpretation of §96's classes in DEC-003 correct, especially CONFIRMED REQUIREMENT vs SYSTEM REQUIREMENT? | §96 | Classification of every requirement | OPEN |

## Technical concerns (TC)

| ID | Concern | Sources | Recommendation (RECOMMENDED — NOT YET APPROVED) | Status |
|---|---|---|---|---|
| TC-01 | The safety/uncertainty margin in the net-profit calculation (and "safety margin satisfied" as an execution condition) could quietly become the universal minimum-profit threshold that §14 forbids, which would violate the §103 completion condition. | §13, §14, §17, §103 | Derive the margin per opportunity from measured uncertainty (e.g. fee, slippage, and latency estimation error), never as one fixed percentage; define it together with OQ-05. | OPEN |
| TC-02 | Model evaluation, AI cost monitoring, and model routing are measurement, accounting, and rule evaluation. Implementing them as LLM agents (as the §54 roster names two of them) would conflict with "if a calculation can be performed deterministically, the system should not ask an LLM" and with constitution Rules 87 and 201. | §12, §54, §61–§63 | Implement as deterministic services. AI may interpret their output where useful. | OPEN |
| TC-03 | Opportunities from different trading systems compete for the same capital, so they must be compared on a common basis. The quality dimensions in §17 do not yet define how a directional trade and a triangular route are compared. | §17, §20, §21 | Define a common risk-adjusted comparison basis in the Global Capital Authority's allocation contract (Part 2 interfaces). | OPEN |
| TC-04 | Small-profit accumulation is sensitive to estimation error: at +0.1% expected, an error of similar size in fees or slippage flips the sign. Optimistic paper-trading fills would hide this. | §14, §15, §32, §48 | Use expected-vs-actual data to calibrate cost estimates and the safety margin; treat paper results as unvalidated for small-margin strategies until compared with live expected-vs-actual data. | OPEN |
| TC-05 | Idempotent execution requires querying order state after a timeout. Each venue adapter must support it (e.g. client order IDs and order-status queries). | §41, §42 | Make order-state query a mandatory part of the standard adapter interface; confirm per venue. | OPEN |
| TC-06 | The Hallucination Firewall requires AI claims to cite data source, timestamp, dataset, calculation, and evidence identifier. That only works if market data, quantitative outputs, and events carry stable identifiers. | §10, §12, §64, §86 | Include evidence identifiers in the data and calculation contracts from the DATA FOUNDATION stage onward. | OPEN |
