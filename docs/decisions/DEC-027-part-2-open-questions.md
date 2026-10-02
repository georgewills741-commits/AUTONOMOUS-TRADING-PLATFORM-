# DEC-027 — Owner answers on the Part 2 open questions

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 3, Q2, Q3, Q4, Q8, Q10](../handoffs/owner-decisions-03-part-2-findings.md)), each choosing the recommended option
- **Resolves:** OQ-24, OQ-25, OQ-26; confirms ARCH-034 as a proposal and [DEC-024](DEC-024-part-2-reconciliation.md) as a whole

## Decision

| Question | Owner's choice | Result |
|---|---|---|
| OQ-24: the "global platform controller" | Existing parts | ARCH-035: not a separate system. The name covers the Policy System, the Risk Engine's emergency controller, and System Health working together |
| OQ-25: where a PAPER-mode strategy runs | Separate setup | PAP-013: the paper environment, on live market data, with no real exchange keys |
| OQ-26: "adaptive execution" | Future feature | EXE-011 (FUTURE): execution that adjusts order type, order splitting, and price to liquidity and volatility, inside risk limits. Not built until the owner approves it |
| ARCH-034: domain command language | Keep as idea | ARCH-034 stays PROPOSED; nothing is built |
| DEC-024's five organizing choices | Keep all five | DEC-024 is confirmed by the owner: SYS-34 Readiness System; canary as a production stage (OPS-013); the Performance Controller's core in DIRECTIONAL TRADING; one Opportunity Database; five agents plus deterministic services covering the nine roles |

## Notes

- **PAP-013 and the paper architecture.** The paper environment reads market data through public or read-only access; it holds no exchange trading credentials (MODE-006, PAP-011). Paper evidence flows one way, read-only, to the Readiness System in production. Production accepts evidence from it, never commands. A strategy version that passes readiness is then deployed to production for canary as the same, unchanged version (STR-025).
- **EXE-011 belongs to the Execution Engine.** Like all execution it must be deterministic (EXE-001), and its adjustments stay within the safety envelope (RSK-034, RSK-036).

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

The options the owner did not choose, quoted in full in [owner decisions 3](../handoffs/owner-decisions-03-part-2-findings.md):

- OQ-25 (Q2): run inside the live system, with its orders sent to the simulator.
- OQ-24 (Q3): a new, separate system.
- OQ-26 (Q4): keep it as an undefined idea; or drop it.
- ARCH-034 (Q8): approve it as a planned feature; or drop it.
- DEC-024 (Q10): change some of the five choices.
