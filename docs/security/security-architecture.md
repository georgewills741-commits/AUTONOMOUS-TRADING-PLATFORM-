# Security Architecture

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-31 (cross-cutting) · **Roadmap stage:** FOUNDATION ("Security foundation"); later stages are not mapped · **Sources:** §89 (also §52)

Canonical definition of what the platform must protect. The builder's own rules on secrets (constitution Rules 110 and 153) also apply to this repository.

## Requirements

- **SEC-001** Protected assets · CONFIRMED REQUIREMENT · §89 — Protect: exchange credentials; API keys; secrets; wallet keys where applicable; user accounts; trading permissions; financial records; audit records; AI access; administrative operations.
- **SEC-002** No unrestricted credentials for AI agents · CONSTRAINT · §89 — AI agents must not receive unrestricted credentials.

SEC-002 agrees with the AI hard-safety boundary item "receive unrestricted secrets" (AIL-003). Research must not directly modify exchange credentials (STR-008).

## Decisions applied (2026-09-30)

- **SEC-003** Trading keys cannot withdraw · CONSTRAINT · DEC-012 — API keys used for trading must not have withdrawal permission and, where the venue supports it, are restricted to known IP addresses. Automated inter-venue transfers, if enabled (CAP-022), use a separate key restricted to a withdrawal-address whitelist containing only the operator's own venue accounts.
- **SEC-004** Credential separation · CONSTRAINT · DEC-015 — Trading-enabled credentials exist only in the production environment. AI credentials are held only by the AI gateway and are separate from trading credentials.
- **SEC-005** Secrets handling · CONSTRAINT · DEC-009 — Secrets are never stored in the repository, logs, or AI prompts. They are injected at runtime from the environment or a secret manager.

With a single operator ([DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)), "user accounts" in SEC-001 means the operator's own access to the platform.

## Not yet specified

Threat model, authentication for the operator interface, and tests. Key management for custody is FUTURE (CUS-002).
