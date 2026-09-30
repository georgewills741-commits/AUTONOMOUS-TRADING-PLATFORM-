# Security Architecture

> **Status:** DOCUMENTED (Handoff Parts 1 and 2) — not implemented · **System:** SYS-31 (cross-cutting) · **Roadmap stage:** FOUNDATION ("Security foundation"); later stages are not mapped · **Sources:** §89 (also §52)

Canonical definition of what the platform must protect. The builder's own rules on secrets (constitution Rules 110 and 153) also apply to this repository.

## Requirements

- **SEC-001** Protected assets · CONFIRMED REQUIREMENT · §89 — Protect: exchange credentials; API keys; secrets; wallet keys where applicable; user accounts; trading permissions; financial records; audit records; AI access; administrative operations.
- **SEC-002** No unrestricted credentials for AI agents · CONSTRAINT · §89 — AI agents must not receive unrestricted credentials.

SEC-002 agrees with the AI hard-safety boundary item "receive unrestricted secrets" (AIL-003). Research must not directly modify exchange credentials (STR-008).

## Decisions applied (2026-09-30)

- **SEC-003** Trading keys cannot withdraw · DEPRECATED / REPLACED · DEC-012 — API keys used for trading must not have withdrawal permission and, where the venue supports it, are restricted to known IP addresses. Automated inter-venue transfers, if enabled (CAP-022), use a separate key restricted to a withdrawal-address whitelist containing only the operator's own venue accounts.
- **SEC-004** Credential separation · CONSTRAINT · DEC-015 — Trading-enabled credentials exist only in the production environment. AI credentials are held only by the AI gateway and are separate from trading credentials.
- **SEC-005** Secrets handling · CONSTRAINT · DEC-009 — Secrets are never stored in the repository, logs, or AI prompts. They are injected at runtime from the environment or a secret manager.

With a single operator ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)), "user accounts" in SEC-001 means the operator's own access to the platform.

## Owner correction applied (OC-1, [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md))

SEC-003 is replaced by SEC-006, which keeps its no-withdrawal rule for trading keys.

- **SEC-006** Three separate authorities · CONSTRAINT · DEC-019 — Trading authority (trading only), rebalancing transfer authority (approved transfers between approved exchange accounts), and withdrawal/custody authority (separate and independently controlled) use separate credentials. Trading credentials must not carry withdrawal permission and, where the venue supports it, are restricted to known IP addresses. Automated rebalancing is restricted to approved accounts and venues owned or controlled by the operator, and must not become a general-purpose withdrawal mechanism. The platform itself holds no general withdrawal or custody authority (custody is FUTURE).
- **SEC-007** Transfer credential restrictions · CONFIRMED REQUIREMENT · DEC-019 — Automated transfers must have additional protection. Where supported, transfer credentials should be restricted by: destination allowlists; asset allowlists; amount limits; frequency limits; venue restrictions; authentication controls; audit logging; policy enforcement.

Builder note: where a venue cannot enforce one of the SEC-007 restrictions itself, the platform enforces it before any transfer request is sent (CAP-025).

## Handoff Part 2 applied (2026-09-30)

New requirements from [Handoff Part 2](../handoffs/part-2-consolidated-additional-systems.md), cited as P2§N. Part 2 sections that only restate an existing requirement add nothing here; where each section went is in the [Part 2 reconciliation](../traceability/part-2-reconciliation.md). Placement and duplicate resolutions: [DEC-024](../decisions/DEC-024-part-2-reconciliation.md).

- **SEC-008** Least-privilege AI permissions · CONSTRAINT · P2§110, P2§299 — AI permissions follow minimum privilege. No research agent automatically receives: live order permission; wallet signing; withdrawal permission; production deployment permission.
- **SEC-009** Production security scope · SYSTEM REQUIREMENT · P2§160 — Production hardening must cover: authentication; authorization; secrets; encryption; network controls; audit; AI permissions; tool permissions; key management; dependency security; vulnerability monitoring; security incident handling; environment separation.

Already covered: live credentials never in lower environments and paper/live credential separation (P2§161, §162) are SEC-004, MODE-006, and PAP-011. Trading permission not implying withdrawal (P2§116, §305) is SEC-006. No plain-text secrets in migration packages (P2§135) is MIG-009. Per-role permission scopes are AGT-022, and tool access is AIL-013. Security incidents use the incident record of INC-002.

## Not yet specified

Threat model, authentication for the operator interface, and tests. Key management for custody is FUTURE (CUS-002).
