# Security Architecture

> **Status:** DOCUMENTED (Handoff Part 1) — not implemented · **System:** SYS-31 (cross-cutting) · **Roadmap stage:** FOUNDATION ("Security foundation"); later stages are not mapped · **Sources:** §89 (also §52)

Canonical definition of what the platform must protect. The builder's own rules on secrets (constitution Rules 110 and 153) also apply to this repository.

## Requirements

- **SEC-001** Protected assets · CONFIRMED REQUIREMENT · §89 — Protect: exchange credentials; API keys; secrets; wallet keys where applicable; user accounts; trading permissions; financial records; audit records; AI access; administrative operations.
- **SEC-002** No unrestricted credentials for AI agents · CONSTRAINT · §89 — AI agents must not receive unrestricted credentials.

SEC-002 agrees with the AI hard-safety boundary item "receive unrestricted secrets" (AIL-003). Research must not directly modify exchange credentials (STR-008).

## Not yet specified in Part 1

Threat model, secret storage, key management (required if custody is retained, CUS-002), authentication and authorization model, least-privilege design for adapters and agents, separating environments technically (constitution Rule 111), and tests. "User accounts" in SEC-001 depends on OQ-01 (single operator or many users).
