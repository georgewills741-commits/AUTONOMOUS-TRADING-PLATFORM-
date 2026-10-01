# Architecture Governance

> **Status:** DOCUMENTED (Handoff Part 3) — not implemented · **Owner:** cross-cutting (platform architecture) · **Requirement prefix:** GOV · **Roadmap stage:** FOUNDATION (applies to every later stage) · **Sources:** P3§401–P3§410, P3§462–P3§466, P3§472–P3§475, P3§508–P3§512, P3§519, P3§528, P3§532, P3§548; [DEC-031](../decisions/DEC-031-part-3-reconciliation.md)
>
> Canonical definition of how new features, changes, and removals enter the platform without damaging it: Part 3's "feature-extensibility governance model" (P3§537, P3§541 item 26). Requirement line format: [`docs/requirements/README.md`](../requirements/README.md).

## Scope and relationship to the builder constitution

The [builder constitution](../builder/claude-code-builder-constitution.md) and the [checkpoint and verification rule](../builder/checkpoint-and-verification-rule.md) govern how Claude builds this repository. The requirements here are **project requirements** from Handoff Part 3: they govern how any feature enters the platform, whoever builds it, for as long as the platform exists. Several say the same thing as a constitution rule (for example GOV-003 and constitution Rule 37, GOV-016 and Rules 142 to 144, GOV-019 and Rule 84). They are kept here as well because the platform must follow them without Claude (constitution Rule 198); the constitution is not restated.

The existing architecture rules they build on stay where they are: duplication control (ARCH-016), canonical sources (ARCH-017, ARCH-027, ARCH-037), feature classification (ARCH-015), no silent promotion (ARCH-029), contract-first development and interface versioning (ARCH-025, ARCH-026), change-impact identification (ARCH-033), and dependency order (RMP-011).

## Requirements

### Extensibility

- **GOV-001** Extensible without damage · CONFIRMED ARCHITECTURAL PRINCIPLE · P3§401, P3§532, P3§548 — The platform must be designed so that new capabilities can be added in the future without damaging existing systems. New functionality must not simply be inserted into production; every significant new feature should pass an integration analysis. New features must be addable without: breaking existing authorities; creating duplicate systems; corrupting financial state; violating policies; breaking contracts; destroying migration compatibility; creating uncontrolled AI authority; creating split-brain execution. The platform must be able to grow without becoming structurally unstable. Every significant new feature must first be: understood; classified; analyzed; checked for duplication; checked for conflict; checked for dependencies; checked for security; checked for performance; checked for migration impact; checked for testing; approved; and only then implemented.
- **GOV-002** New feature integration gate · CONFIRMED REQUIREMENT · P3§402, P3§519 — Before a new feature is approved for implementation: new feature → requirements analysis → duplicate check → conflict check → dependency check → ownership check → security review → risk review → capital review → performance review → data/schema impact → API/contract impact → test impact → deployment impact → migration impact → observability impact → documentation impact → approval → implementation. The complete feature-lifecycle loop continues: implement → validate → paper / safe environment → canary → production → monitor → deprecate / improve / retire when appropriate.
- **GOV-003** Duplicate detection · CONFIRMED REQUIREMENT · P3§403 — Before adding a new feature, Claude must search the repository for existing functionality that may already perform the same or substantially similar responsibility. Example: a new "Liquidity Manager" must first check whether a Liquidity Engine, Market Quality Engine, Execution Engine, or Risk Engine already contains overlapping functionality. The objective is: one responsibility, one authoritative owner.
- **GOV-004** Conflict detection · CONSTRAINT · P3§404 — The system must detect whether a new feature conflicts with: risk; capital; policy; execution; strategy; security; existing APIs; existing schemas; existing state machines; existing deployment architecture. A feature should not be implemented until conflicts are resolved or explicitly accepted.
- **GOV-005** Dependency analysis · CONSTRAINT · P3§405 — Claude must identify prerequisites. Example: a new arbitrage feature may require: market-data quality + exchange adapters + fee engine + slippage engine + liquidity + capital authority + risk + execution + reconciliation. The feature must not be implemented before its safety dependencies exist.

### Compatibility, contracts, and removal

- **GOV-006** Backward compatibility and versioning · CONSTRAINT · P3§406, P3§408 — New functionality should preserve existing valid behavior unless an intentional architectural change has been approved. Changes to: APIs; schemas; events; contracts; strategy interfaces; policies; must be versioned or migrated appropriately. Breaking changes must not silently break dependent components. Where appropriate: version → migration → compatibility → test → deploy.
- **GOV-007** Contract types · SYSTEM REQUIREMENT · P3§407 — In addition to the contracts named in ARCH-025, contracts defined before implementation may include: API contracts; event schemas; data schemas. Implementation should conform to approved contracts.
- **GOV-008** Controlled feature removal · CONSTRAINT · P3§409 — Removing a feature must also follow controlled analysis. Before deprecation/removal: identify dependencies; identify users; identify strategies; identify data; identify APIs; identify historical records; identify migrations; identify rollback implications. No important functionality should disappear silently.
- **GOV-009** Deprecation statuses · SYSTEM REQUIREMENT · P3§410 — The repository should support explicit statuses such as: ACTIVE; DEPRECATED; SUNSET_PENDING; RETIRED; REPLACED. Historical data and decisions must remain interpretable.

### Security-, observability-, testability-, and deployability-first

- **GOV-010** Security-first extensibility · CONFIRMED REQUIREMENT · P3§462 — Every new feature must be analyzed for: new attack surface; new permissions; new secrets; new APIs; new network paths; new financial authority; new data access.
- **GOV-011** Observability-first extensibility · CONSTRAINT · P3§463 — A major feature should not be accepted into production without appropriate: metrics; logs; alerts; traces; health checks; audit events.
- **GOV-012** Testability-first extensibility · CONFIRMED REQUIREMENT · P3§464 — New functionality must include an appropriate verification plan. Possible levels: unit; integration; contract; simulation; backtest; paper; load; failure; security; chaos; end-to-end.
- **GOV-013** Deployability-first extensibility · CONFIRMED REQUIREMENT · P3§465 — New features must be compatible with: local deployment; server deployment; migration; backup; restore; rollback; environment separation.
- **GOV-014** No architectural debt by accident · CONSTRAINT · P3§466 — Claude must not add a shortcut that creates a second: authority; database of truth; risk system; capital system; policy system; execution path; configuration source.

### Knowledge, documentation, and decisions

- **GOV-015** Features enter the knowledge system · CONFIRMED REQUIREMENT · P3§472, P3§473 — A new feature is not complete merely because code exists. It must become connected to: requirements; architecture; ownership; dependencies; roadmap; tests; documentation; monitoring; security; deployment; traceability. If implementation changes architecture, the authoritative documentation must be updated. The repository must not become inconsistent with the actual system.
- **GOV-016** Architectural decision records; no silent architectural changes · CONFIRMED REQUIREMENT · P3§474, P3§475 — Important architectural choices should be recorded as ADRs. An ADR should explain: context; decision; alternatives; consequences; status; date/version. Claude must not make a major architectural decision silently. If a choice affects: authority; security; financial state; execution; deployment; data; strategy lifecycle; AI permissions; it must be documented.

### Future features and complexity

- **GOV-017** Future capability is not current implementation · CONSTRAINT · P3§508 — The architecture should allow future systems such as: additional exchanges; additional arbitrage types; additional strategy families; new data sources; new AI providers; new risk models; new execution models; new portfolio capabilities; new deployment environments. But future capability does not equal current implementation.
- **GOV-018** Feature status registry · PROPOSED · P3§509 — The repository may maintain features with the statuses: PROPOSED; RESEARCH; APPROVED; IN DEVELOPMENT; VALIDATING; DEPLOYED; DEPRECATED; RETIRED.
- **GOV-019** Feature justification · CONFIRMED REQUIREMENT · P3§510, P3§511 — No feature should be added just because it sounds powerful. A feature must have: purpose; owner; need; dependencies; risk assessment; operational impact; verification method; rollback strategy. The system should be highly capable without becoming unnecessarily complex; do not add complexity merely to make the architecture appear advanced. Every subsystem should justify: why it exists; what it owns; what depends on it; what it protects; how it is verified.
- **GOV-020** Complexity budget · CONSTRAINT · P3§512, P3§528 — Claude should avoid introducing: unnecessary microservices; duplicate queues; duplicate databases; duplicate orchestration; unnecessary AI agents; redundant abstractions; complex frameworks without clear benefit. Company-grade does not mean complexity for its own sake. The objective is not maximum feature count; it is maximum useful capability with minimum unnecessary complexity and strong safety/control.

## How the gate runs today, and later

Until implementation starts, the gate is this repository's documentation process: a new capability is added to its owning specification with a classification (ARCH-015), checked for duplicates and conflicts and recorded in the [findings register](../conflicts/register.md), mapped to its dependencies in the [dependency map](dependency-map.md), placed in the [roadmap](../roadmap/roadmap.md), and indexed in the [registry](../requirements/registry.md). [`tools/docs/build_index.py`](../../tools/docs/README.md) checks the references and links, and [`tools/docs/compare_requirements.py`](../../tools/docs/README.md) shows which requirements a change added, removed, reclassified, or reworded (ARCH-033). Decisions are recorded in [`docs/decisions/`](../decisions/README.md) (GOV-016).

When implementation starts, GOV-002's steps become part of each stage's plan, and GOV-011 to GOV-013 become entry criteria for production (RMP-010). Examples named in GOV-003 ("Liquidity Engine", "Market Quality Engine") are not registered systems: liquidity evaluation is the True Net-Profit Engine's (TNP-024) with metrics from the Quantitative Engine, and market-data quality is Market-Data Infrastructure's (MKD-008). See the [system registry](system-registry.md).

**Status vocabularies.** GOV-009's statuses apply to documented features and interfaces. Requirements keep their own classes (ARCH-015), where DEPRECATED / REPLACED plays the same role. GOV-018 is a proposal: until it is approved, the requirement classes and the Readiness System's capability registry (RDY-020) cover what it would record, and no separate feature registry is created (DUP-32, GOV-014).

**ADRs (GOV-016).** Decision records from DEC-031 onward include an "Alternatives" section. Most earlier records (DEC-001 to DEC-030) do not; this is TC-08 in the [open-question register](../open-questions/register.md).

## Boundary (§92)

- **Owns:** the rules every feature, change, and removal must pass before it is approved.
- **Does not own:** approval itself (the owner, or the deterministic Readiness System for strategy promotion, STR-019), the runtime capability registry (RDY-020), or the requirement classes (ARCH-015).
- **Not yet specified:** the per-stage form of the gate (produced when each stage is planned); tooling beyond the documentation checker.
