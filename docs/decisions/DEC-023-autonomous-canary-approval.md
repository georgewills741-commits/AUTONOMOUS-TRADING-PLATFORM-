# DEC-023 — Policy-driven autonomous approval by the Governance and Readiness Engine

- **Status:** ACCEPTED
- **Date:** 2026-09-30
- **Decided by:** project owner ([owner decisions 2, CF-13](../handoffs/owner-decisions-02-cf-11-to-cf-13.md))
- **Resolves:** CF-13

## Decision

The lifecycle APPROVAL stage (STR-001 §34, STR-009 §38) is performed automatically by a deterministic **Governance and Readiness Engine** when every mandatory check passes. Human approval is needed only where policy explicitly requires it. No AI agent and no human can bypass the deterministic safety gates.

| Requirement | What it says |
|---|---|
| STR-019 | The Governance and Readiness Engine performs APPROVAL automatically when all mandatory readiness, risk, validation, capital, data-integrity, liquidity, execution, and operational checks pass. Canary entry also needs the eligibility policy satisfied and sufficient capital |
| STR-020 | Canary allocation, exposure limits, duration, and promotion criteria are enforced by deterministic controls |
| STR-021 | Human approval only where policy explicitly marks a deployment as needing it (e.g. a brand-new strategy class, a material risk-model change, an exceptional capital increase, a security-sensitive change, an unresolved governance exception) |
| STR-022 | No AI agent or human may bypass the gates. Failing any mandatory gate blocks canary and puts the strategy in a blocked / readiness-failed state until the conditions are met |

## Placement (builder), so no duplicate system is created

The owner names the Governance and Readiness Engine. It is registered as a **component of Strategy Management (SYS-14)**, not as a new system. Strategy Management already owns promotion (STR-003) and the canary readiness gates (STR-013); the engine is the component that evaluates those gates and issues the "canary authorization" named in STR-013. Checks it needs from other systems (capital, risk, policy, market data, system health) are consumed through their owners ([dependency map](../architecture/dependency-map.md), D-51).

## Consistency

STR-014 (automatic canary unless policy designates a human gate), MODE-007, and PLT-014 already express the same model; STR-019 to STR-022 make it specific. Which deployments need a human is a policy value (V-28 in the [values register](../requirements/values-register.md)).
