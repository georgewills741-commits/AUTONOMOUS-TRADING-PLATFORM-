# DEC-008 — Venues, trading universe, and adapter requirements

- **Status:** ACCEPTED
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

## Consequences

Cross-exchange arbitrage has five venues to compare. Venue availability depends on the operator's jurisdiction; that remains the operator's responsibility.
