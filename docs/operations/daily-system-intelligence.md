# Daily System Intelligence Dashboard and Report

> **Status:** DOCUMENTED (Handoff Part 2) — not implemented · **Owner:** SYS-28 Monitoring and Observability (component) · **Roadmap stage:** OPERATIONALIZATION · **Sources:** P2§69–P2§72, P2§339; [DEC-017](../decisions/DEC-017-reporting-alerting-and-performance-targets.md); [DEC-024](../decisions/DEC-024-part-2-reconciliation.md)
>
> Canonical specification of the daily operational picture given to the operator. Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Requirements

- **DSI-001** Daily System Intelligence Dashboard · CONFIRMED REQUIREMENT · P2§69 — The platform should eventually provide a Daily System Intelligence Dashboard / Report. Its purpose is to give the user a high-level operational understanding of the system. It should summarize, where applicable: market conditions; opportunities; executions; capital; risk; strategy health; AI activity; incidents; reconciliation; paper readiness; production readiness; unknown states; important changes.
- **DSI-002** Report sections · SYSTEM REQUIREMENT · P2§70 — A report may include: Market summary (market regime; volatility; major events; data-quality state); Opportunity summary (opportunities detected; opportunities accepted; opportunities rejected; missed opportunities; false opportunities; net economics); Execution summary (orders; fills; partial fills; slippage; latency; rejections); Capital summary (available capital; reserved capital; utilization; strategy allocation; venue allocation); Risk summary (risk events; exposure; drawdown; loss streak; risk-limit events); AI summary (AI calls; models used; cost; failures; fallbacks; unsupported claims; AI contribution); Strategy health (performance; drift; regime behavior; degradation; suspensions); Incidents (exchange issues; data issues; execution issues; system issues; security issues); Readiness (current readiness; evidence accumulated; missing evidence; blocking conditions).
- **DSI-003** Historical reports · CONFIRMED REQUIREMENT · P2§71 — Daily reports should be retained where appropriate. The user should be able to compare today vs yesterday vs last week vs a historical baseline, to support operational trend analysis.
- **DSI-004** Unknown is reported, never shown as normal · CONSTRAINT · P2§72 — The dashboard should explicitly report unknown/uncertain states. Examples: unknown market regime; unknown order state; unknown exchange state; unknown reconciliation state; unknown data quality; unknown AI evidence. Unknown must not be silently represented as normal.
- **DSI-005** Deterministic aggregation, AI interpretation · CONFIRMED ARCHITECTURAL PRINCIPLE · P2§339 — For the dashboard, the deterministic core's role is deterministic aggregation and the AI layer's role is to summarize/interpret.
- **DSI-006** Part of reporting; one dashboard authority · CONFIRMED ARCHITECTURAL PRINCIPLE · DEC-024 — The dashboard and report extend the daily report of MON-008 and are produced by Monitoring and Observability (SYS-28) as read-only views over the systems that own each figure. There is one dashboard authority.

## Where each section comes from

The dashboard owns no figure. Each section reads its owner (DSI-006), so the report can never become a second source of truth.

| Section (DSI-002) | Read from |
|---|---|
| Market summary | SYS-04 Regime Engine (RGM); SYS-02 data quality (MKD-008) |
| Opportunity summary | SYS-05 Opportunity Database (OPP-014 to OPP-016); SYS-21 missed and false opportunities (PFC-012, PFC-013) |
| Execution summary | SYS-30 audit trail (AUD-003); SYS-21 expected vs actual (PFC-001) |
| Capital summary | SYS-07 Global Capital Authority (CAP-002, CAP-026) |
| Risk summary | SYS-09 Risk Engine (RSK-015, RSK-026); SYS-08 Portfolio (PRT-002) |
| AI summary | SYS-25 AI Cost Manager (COST-001); SYS-26 Model Evaluation (MEV-004); SYS-22 AI gateway and validation (AIL-006, AIV-019) |
| Strategy health | SYS-21 Performance Controller (PFC-003, PFC-009); SYS-14 Strategy Registry (STR-024) |
| Incidents | [Incident Management](incident-management.md) (INC-002) |
| Readiness | SYS-34 [Readiness System](../systems/readiness-system.md) (RDY-005) |
| Reconciliation, unknown states | SYS-11 (REC-016); SYS-29 System Health (HLT-011) |

## Boundary

- **Consumes:** the owners above, read-only.
- **Must not:** hold its own copy of any figure; present unknown as normal (DSI-004); let AI produce figures (DSI-005).
- **Not yet specified:** layout, delivery channel, the retention period for daily reports (a value to be added to the values register when set), interfaces, tests.
