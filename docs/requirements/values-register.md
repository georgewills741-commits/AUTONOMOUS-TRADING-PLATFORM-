# Values Register

> **Status:** ACTIVE — 2026-09-30. Required by ARCH-018 ([DEC-020](../decisions/DEC-020-value-classification.md); OC-1 item 31).
>
> Every concrete operating value used by a requirement is listed here with its classification: DEFAULT, DESIGN TARGET, POLICY-CONTROLLED PARAMETER, HARD LIMIT, IMPLEMENTATION CHOICE, or OBSERVED. **No value is a permanent hard-coded requirement**; none has been explicitly approved as one. Where no value is adopted, the operator sets it in the Policy System. Until it is set, the autonomous action that depends on it is outside authorization and does not run (CAP-025, PLT-015).
>
> Illustrative examples quoted from a source are **not** operating values: the +0.1% … +5% examples in TNP-006, "1% per day" in TNP-012, "5% daily return" in TNP-014, and the "1% per trade", "1% every day", and "5% every day" that Part 2 §34 forbids the architecture to encode.

| ID | Value | Used by | Class | Current value | Notes |
|---|---|---|---|---|---|
| V-01 | Canary maximum initial allocation | STR-015 | POLICY-CONTROLLED PARAMETER (upper bound; the actual allocation is computed dynamically within it) | Not set | The former default of 5% (DEC-015) was withdrawn by OC-1 items 16, 18, 31 |
| V-02 | Canary evidence: minimum live duration | STR-018, STR-020 | POLICY-CONTROLLED PARAMETER (optional evidence requirement) | Not set | The former 14 days was withdrawn; time alone never decides readiness |
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
| V-24 | Period a transient trigger condition must stay cleared before automatic kill-switch recovery | RSK-021 | POLICY-CONTROLLED PARAMETER | Not set | [DEC-021](../decisions/DEC-021-kill-switch-recovery.md) |
| V-25 | Repeated-trip limit (trips within a window that stop automatic recovery and escalate) | RSK-024 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-26 | Limited-recovery stages (exposure and capital allowed at each step before full operation) | RSK-023 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-27 | Kill-switch cause classification: transient (automatically recoverable) vs latched | RSK-021, RSK-022 | POLICY-CONTROLLED PARAMETER | Baseline from DEC-021 | Unclassified causes are latched (RSK-022) |
| V-28 | Deployments that require human authorization | STR-021 | POLICY-CONTROLLED PARAMETER | Baseline examples from DEC-023 | Policy must mark them explicitly: brand-new strategy class, material risk-model change, exceptional capital increase, security-sensitive change, unresolved governance exception ([DEC-023](../decisions/DEC-023-autonomous-canary-approval.md)) |
| V-29 | Confidence required to treat critical state as reconciled | REC-016 | HARD LIMIT (value in policy) | Not set | |
| V-30 | Loss-streak thresholds and the response at each (reduce exposure, pause, review, cooldown, suspend) | RSK-026 | POLICY-CONTROLLED PARAMETER | Not set | P2§40: "Exact thresholds must be policy/configuration driven" |
| V-31 | Excessive-trading thresholds (order rate, repeated failed opportunities, churn) and responses | RSK-027 | POLICY-CONTROLLED PARAMETER | Not set | |
| V-32 | Arbitrage quality-tier boundaries: Tier 1 ≈ ≥1%, Tier 2 ≈ 0.5–1%, Tier 3 ≈ 0.2–0.5%, Tier 4 < ≈0.2% true net | ARB-015 | DEFAULT (analytical reporting categories) | As listed | Categories for analysis and reporting only. They never gate execution (ARB-015, TNP-005, TNP-016) |
| V-33 | Readiness evidence required for each readiness transition | RDY-002, RDY-004 | POLICY-CONTROLLED PARAMETER | Not set | Includes the canary evidence of V-02 to V-05. Missing evidence means NOT_READY |
| V-34 | Capital bucket sizing rules: directional trading capital, emergency reserve, per-exchange reserve (how each scales with capital, exposure, liquidity, exchange requirements, active strategies, transfer constraints, system health) | CAP-029, CAP-030 | POLICY-CONTROLLED PARAMETER | Not set | [DEC-028](../decisions/DEC-028-capital-buckets-and-progressive-activation.md): policy-set, never fixed hard-coded amounts |
| V-35 | Capability eligibility thresholds (capital and proven capacity and safety needed before a capital-intensive capability becomes eligible) | CAP-032, RDY-008 | POLICY-CONTROLLED PARAMETER | Not set | Eligibility never exceeds the operator's authorizations |

**HARD LIMIT values are part of the safety floor.** They are the numbers inside the immutable safety invariants (RSK-034), so changing one needs a formal, versioned, audited, human-controlled change (RSK-039, [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)). POLICY-CONTROLLED PARAMETERS belong to the configurable layer (RSK-035).

To add a value: give it the next V-number, name the requirement that uses it, and classify it. To make any value a permanent hard-coded requirement, the owner must approve it explicitly in a decision record (ARCH-018).
