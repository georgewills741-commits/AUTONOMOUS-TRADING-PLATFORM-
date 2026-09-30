# DEC-014 — True net-profit formula and uncertainty margin

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Date:** 2026-09-30
- **Resolves:** OQ-05, TC-01, TC-04

## Context

TNP-003 requires a formal formula. TNP-005 and §103 forbid any universal minimum-profit threshold. A fixed "safety margin" would quietly become exactly such a threshold (TC-01). At margins like +0.1%, cost-estimation errors of the same size flip the sign (TC-04).

## Decision

**Formula (TNP-018).** For an opportunity at its intended size, in quote currency, with exact decimal arithmetic:

```text
true net expected result =
    gross edge at executable prices (walk the order book at the intended size)
  − trading fees at the account's actual fee tier
  − spread cost
  − expected slippage
  − expected market impact
  − funding and borrow costs over the expected holding period
  − attributed rebalancing / transfer costs
  − other execution costs
  − uncertainty margin
```

**Uncertainty margin (TNP-019).** Computed per opportunity from measured uncertainty:

```text
uncertainty margin = k × sqrt( cost_estimate_error² + latency_price_risk² )
```

- `cost_estimate_error` is the standard error of this venue/market/strategy's cost estimates, from expected-vs-actual history. With little history, a conservative prior is used.
- `latency_price_risk` is price volatility over the expected execution latency × size.
- `k` is an operator-configurable confidence multiplier.
- The margin is never a fixed percentage or a universal minimum.

**Eligibility (TNP-020).** An opportunity is economically eligible when the true net expected result is greater than zero after the margin. It must still pass TNP-011 (risk, liquidity, feasibility, capital, strategy validity, safety).

**Calibration (TNP-022, TC-04).** Cost estimates and `cost_estimate_error` are recalibrated continuously from expected-vs-actual results (PFC-001). Paper results alone do not validate small-margin strategies; their canary must confirm live costs (PAP-003).

## Alternatives considered

- **Fixed percentage safety margin:** rejected; it contradicts TNP-005.
- **No margin:** rejected; §13 and §14 require a safety/uncertainty margin.

## Consequences

The exact numerical methods for slippage and market impact (order-book walk, impact model) are part of the TNP interface contract expected in Part 2.
