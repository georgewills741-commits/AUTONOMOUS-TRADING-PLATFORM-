# DEC-017 — Reporting, alerting, logging, and initial performance targets

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Later changes:** The performance targets (PERF-007) are superseded by [DEC-019](DEC-019-company-grade-autonomous-operating-model.md); the 50 ms / 500 ms figures remain only as DESIGN TARGETS ([DEC-020](DEC-020-value-classification.md)).
- **Date:** 2026-09-30
- **Resolves:** OQ-13, OQ-19

## Reporting and alerting (OQ-13)

Reporting and alerting are owned by **Monitoring and Observability (SYS-28)**. No new system is created.

- **Alerts (MON-007):** severities INFO, WARNING, CRITICAL, and EMERGENCY, delivered to at least one operator-configured channel. CRITICAL and EMERGENCY alerts require acknowledgement.
- **Reports (MON-008):** daily and on demand. They cover P&L, exposure, strategy performance, expected vs actual, AI cost, and incidents, as read-only views over the ledger, portfolio, audit trail, and Performance Controller.
- **Operational logs (MON-009):** kept separate from the audit trail and rotated after 90 days (AUD-006). This resolves "Logging" from §04.

## Initial performance targets (OQ-19)

**Design targets, to be replaced by measurements in DATA FOUNDATION (PERF-006, PERF-007):**
- Internal decision latency (market event received → order submitted, excluding venue network time): p99 ≤ 50 ms on arbitrage paths, ≤ 500 ms on directional paths.
- Market-data freshness limits are set per stream (MKD-006).
- **Tiered monitoring:** every market in the universe is monitored at ticker level, and full order-book depth is subscribed for markets the scanner flags as candidates, within venue rate limits (OPP-012). This keeps whole-universe coverage (OPP-001) within venue connection and rate limits.

## Alternatives considered

_Added on 2026-10-02 under the owner's decision on TC-08 ([DEC-035](DEC-035-owner-decisions-part-3-findings.md)). Each alternative below is one the repository records as proposed, weighed, or ruled out, and its source is named. Nothing is reconstructed from memory (constitution Rule 181)._

- **A separate system for reporting and alerting:** the record rules it out ("No new system is created"); both belong to Monitoring and Observability (SYS-28).
- No alternatives were recorded for the performance targets (OQ-19) or the tiered monitoring.
