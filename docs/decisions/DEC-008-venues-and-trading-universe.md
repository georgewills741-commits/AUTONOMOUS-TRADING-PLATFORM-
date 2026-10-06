# DEC-008 — Venues, trading universe, and adapter requirements

- **Status:** ACCEPTED
- **Later changes:** The question as asked (three options, Binance, OKX, Coinbase, more than one allowed) and the owner's answer are preserved verbatim in [owner decisions 1](../handoffs/owner-decisions-01-part-1-open-items.md) ([DEC-037](DEC-037-final-decision-and-integrity-checkpoint.md)). The answer reads "all add more space for more exchange like bybit and many more like kucoin exchange"; the quotation below adds a comma, changes "exchange" to "exchanges" and "bybit" to "Bybit", and replaces "and many more like kucoin exchange" with "and KuCoin". Naming Bybit and KuCoin as initial venues, alongside the room for many more (decision 2), is the builder's reading of the answer, reported to the owner the same day ("Exchanges: Binance, OKX, Coinbase, Bybit and KuCoin"), without objection. The statement under "Alternatives considered" that the question is not recorded no longer holds. The text below is kept as written.
- **Date:** 2026-09-30
- **Decided by:** project owner (venue set: "all, add more space for more exchanges like Bybit and KuCoin"); builder under delegation (universe definition, adapter requirements from TC-05)
- **Resolves:** OQ-03, TC-05
- **Affects:** [exchange adapters](../systems/exchange-adapters.md), [opportunity detection](../systems/opportunity-detection.md), [execution engine](../systems/execution-engine.md)

## Decision

1. **Initial venues (owner):** Binance, OKX, Coinbase, Bybit, KuCoin (EXA-005). EXA-002 (the §42 "previously discussed" list) is marked DEPRECATED / REPLACED by EXA-005.
2. **Room for more venues (owner):** adding a venue requires only a new adapter and its configuration, with no change to any other system (EXA-006). This strengthens EXA-004.
3. **Legitimate access (builder):** a venue is enabled only where the operator's account is permitted to use it. The platform never circumvents a venue's geographic or eligibility restrictions (EXA-007).
4. **Trading universe (builder):** every market of an enabled instrument type on an enabled venue, minus exclusions set in the Policy System. It updates automatically as venues list and delist markets (OPP-009).
5. **Adapter requirement (TC-05):** every adapter must support client-assigned order IDs and querying order state after a timeout. A venue lacking either cannot be used for automated trading (EXA-008, EXE-008).

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **Only the three venues previously discussed** (Binance, OKX, Coinbase; §42, EXA-002, OQ-03): not the decided set, which is five initial venues and room for more (EXA-005, EXA-006), decided on the owner's answer ("all, add more space for more exchanges like Bybit and KuCoin"); EXA-002 is DEPRECATED / REPLACED. The question put to the owner is not recorded.
- No alternatives were recorded for the builder's parts (legitimate access, the trading universe, the adapter requirement). OQ-03 listed no options for the trading universe, and TC-05's recommendation was adopted.

## Consequences

Cross-exchange arbitrage has five venues to compare. Venue availability depends on the operator's jurisdiction; that remains the operator's responsibility.
