# Values Register

> **Status:** ACTIVE — 2026-09-30. Required by ARCH-018 ([DEC-020](../decisions/DEC-020-value-classification.md); OC-1 item 31).
>
> Every concrete operating value used by a requirement is listed here with its classification: DEFAULT, DESIGN TARGET, POLICY-CONTROLLED PARAMETER, HARD LIMIT, IMPLEMENTATION CHOICE, or OBSERVED. **No value is a permanent hard-coded requirement**; none has been explicitly approved as one. Where no value is adopted, the operator sets it in the Policy System. Until it is set, the autonomous action that depends on it is outside authorization and does not run (CAP-025, PLT-015).
>
> Illustrative examples quoted from a source are **not** operating values: the +0.1% … +5% examples in TNP-006, "1% per day" in TNP-012, and "5% daily return" in TNP-014.

| ID | Value | Used by | Class | Current value | Notes |
|---|---|---|---|---|---|
| V-01 | Canary maximum initial allocation | STR-015 | POLICY-CONTROLLED PARAMETER (upper bound; the actual allocation is computed dynamically within it) | Not set | The former default of 5% (DEC-015) was withdrawn by OC-1 items 16, 18, 31 |
| V-02 | Canary evidence: minimum live duration | STR-018 | POLICY-CONTROLLED PARAMETER (optional evidence requirement) | Not set | The former 14 days was withdrawn; time alone never decides readiness |
| V-03 | Canary evidence: minimum trade count | STR-018 | POLICY-CONTROLLED PARAMETER (optional evidence requirement) | Not set | The former 50 trades was withdrawn |
| V-04 | Canary allocation stages and the gate thresholds between them | STR-016 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-05 | Canary deterioration thresholds | STR-017 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-06 | Arbitrage path: internal decision latency | PERF-009, PERF-012 | DESIGN TARGET (soft) | p99 ≤ 50 ms (initial engineering target) | Former PERF-007. To be replaced by a measured baseline (PERF-010) |
| V-07 | Directional path: internal decision latency | PERF-009, PERF-012 | DESIGN TARGET (soft) | p99 ≤ 500 ms (initial engineering target) | Former PERF-007. Strategy-dependent (PERF-009) |
| V-08 | Performance hard limits per path (e.g. maximum decision latency, maximum data staleness) | PERF-012, MKD-006 | HARD LIMIT (value in policy) | Not set | Derived from the measured baseline in DATA FOUNDATION (PERF-010) |
| V-09 | Latency-path measurements (p50 / p95 / p99 / p99.9, jitter, round-trip, queue delay, and others) | PERF-010 | OBSERVED | — | Measured continuously once running |
| V-10 | Rebalancing controls: maximum transfer amount, maximum daily amount, minimum venue reserve, maximum venue exposure, frequency limits, approved source/destination venues, approved assets | CAP-025, SEC-007 | POLICY-CONTROLLED PARAMETER | Not set | Autonomous rebalancing cannot run until set |
| V-11 | Uncertainty-margin confidence multiplier `k` | TNP-019 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-12 | Risk limits (position, exposure, leverage, loss, slippage, liquidity, correlation, distance to liquidation, margin ratio, funding and borrow cost, derivatives notional) | RSK-002, RSK-013 | HARD LIMIT (value in policy) | Not set | |
| V-13 | Kill-switch trigger thresholds | ARB-010, RSK-008 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-14 | Emergency-type → safety-level rules; position-protection rules | RSK-016, RSK-017 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-15 | Premium-model confirmation threshold (capital at risk) | AIV-014 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-16 | SUPERVISED proposal expiry time | MODE-005 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-17 | Market-data freshness limit per stream | MKD-006 | HARD LIMIT (value in policy) | Not set | From measurements |
| V-18 | Market-data retention in TimescaleDB | TEC-012, MKD-007 | DEFAULT | 30 days | Then permanent Parquet archive |
| V-19 | Operational log retention | MON-009, TEC-012 | DEFAULT | 90 days | |
| V-20 | Initial directional research timeframes | DIR-005 | DEFAULT | 1 hour, 4 hours | Research candidates only |
| V-21 | Python version | TEC-001 | IMPLEMENTATION CHOICE | 3.12 or later | |
| V-22 | PostgreSQL version | TEC-006 | IMPLEMENTATION CHOICE | 16 | |
| V-23 | Execution lease duration and renewal interval | REC-013, TEC-013 | IMPLEMENTATION CHOICE | Not set | To be chosen from measured failover behavior |

To add a value: give it the next V-number, name the requirement that uses it, and classify it. To make any value a permanent hard-coded requirement, the owner must approve it explicitly in a decision record (ARCH-018).
