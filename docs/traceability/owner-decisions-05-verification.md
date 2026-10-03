# Owner Decisions 5 — Verification Record

> **Status:** ACTIVE record of the checkpoint that applies the owner's answers of 2026-10-03 on the master knowledge-base audit: its four findings, the feature process, the acceptance of the review, and the authorization of Stage 1 planning ([DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md)). Format: [traceability README](README.md). Made under the three-gate procedure of [DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md).

## Identity

- **Date:** 2026-10-03
- **Stage:** FOUNDATION — documentation initialization (before Stage 1)
- **Starts from:** commit `16df57f`. This record's own commit is entered in the [project state](../project-state.md)'s checkpoint log by the next checkpoint.

## Scope

| Change | Files |
|---|---|
| The owner's seven answers, kept verbatim (HISTORICAL), with their manifest line | [owner decisions 5](../handoffs/owner-decisions-05-audit-findings.md); `tools/docs/preserved-texts.sha256` |
| Decision | DEC-036; [decision log](../decisions/README.md) |
| CF-20: production never depends on one machine | MIG-033 added in [Hosting and migration](../operations/hosting-and-migration.md) (with its banner sources and the deployment note); [roadmap](../roadmap/roadmap.md) (OPERATIONALIZATION row); [source-of-truth map](../architecture/source-of-truth-map.md); [Deployment and operational readiness](../operations/deployment-and-operational-readiness.md) and [platform overview](../product/platform-overview.md) findings notes |
| CF-21: PLT-010 matched to DEC-006 | PLT-010 reworded in the [platform overview](../product/platform-overview.md); notes in [Security architecture](../security/security-architecture.md) and [Capital Management](../systems/capital-management.md); DEC-006 "Later changes" |
| DUP-40: retention values only in TEC-012 | MKD-007 reworded in [Market Data](../systems/market-data.md), MON-009 in [Monitoring and observability](../operations/monitoring-and-observability.md); [values register](../requirements/values-register.md) V-18, V-19; [Technology stack](../architecture/technology-stack.md) note; DEC-009 and DEC-017 "Later changes" |
| OQ-28: PLT-011 confirmed | [Open-question register](../open-questions/register.md); notes in the platform overview, [Risk Engine](../risk/risk-engine.md), Capital Management, [Exchange adapters](../systems/exchange-adapters.md), [Portfolio](../systems/portfolio-management.md); DEC-007 "Later changes" |
| Feature process confirmed | [Architecture governance](../architecture/architecture-governance.md) note |
| Findings resolved | [Findings register](../conflicts/register.md) (CF-20, CF-21, DUP-40, status and summary lines); open-question register (OQ-28, status line) |
| Review accepted | `tools/docs/build_index.py` (the registry's Approval text for handoff requirements: "reviewed (DEC-036)"; the registry's explanation of the column); the audit record's "Later changes" line |
| Stage 1 planning authorized; project memory | [Project state](../project-state.md) (current stage, gate table, objective, continuation contract, the owner's decisions, completed work, open questions, recent decisions and changes, next step, checkpoint log), roadmap header and FOUNDATION status, [documentation index](../README.md), [traceability README](README.md) |
| Brought in line with the decisions (found by the Gate 3 review) | DEC-028 and DEC-035 "Later changes"; the [reliability and recovery model](../operations/reliability-and-recovery-model.md) (MIG-033 in the disaster row); the TEC-011 note in the technology stack; "since 2026-10-03" source lines above PLT-010, MKD-007, and MON-009 |
| Generated | `docs/requirements/registry.md`, `docs/traceability/handoff-coverage.md` |

Out of scope: the Stage 1 plan, which is the next checkpoint; any platform code (none exists; implementation is not authorized).

## Checks

| # | Check | Command or method | Result |
|---|---|---|---|
| 1 | The verbatim record matches what was asked and answered | Every label shown, question, option (label and description), and chosen answer in the record parsed back and compared with the AskUserQuestion calls and results in the session transcript, by script | PASS: 7 of 7 labels, questions, all options, and all 7 answers identical; the owner added no notes |
| 2 | Generated files current; references, links, coverage, system rules, preserved texts, orphans | `python3 tools/docs/build_index.py --check-only` | PASS (exit 0): 734 requirements (decisions: 212), 47 prefixes, 99 findings, 36 decisions, 34 systems, 47 system rules; the registry shows 0 "pending documentation review" and 512 "reviewed (DEC-036)" |
| 3 | Only the decided requirements change | `python3 tools/docs/compare_requirements.py 16df57f --strict --expect-changed=MKD-007:text,MON-009:text,PLT-010:text` | PASS (exit 0): added MIG-033; MKD-007, MON-009, PLT-010 changed in their text only; nothing removed; nothing else changed |
| 4 | The tools still fail on broken input | `python3 tools/docs/selftest.py` | PASS: 34 cases |
| 5 | Code checks of the tools | `ruff check tools/docs`; `ruff format --check tools/docs`; `mypy --check-untyped-defs tools/docs` | PASS |
| 6 | No stale statements | Sweep of every active document for the four findings' IDs, "pending documentation review", "awaits/awaiting the owner", "for the owner", "open for the owner"; each hit judged historical or stale | PASS: the remaining hits are historical records kept as written (earlier verification records, the audit record under its "Later changes" line, register entries' original sources), DEC-005's title, and DEC-036 itself |
| 7 | Hygiene | `git diff --check`; `git status --short --ignored`; every removed line outside generated files reviewed; scan for secrets, local paths, model identifiers | PASS: whitespace clean (new files included); only intended files and ignored caches; nothing found by the scan |

Environment: Python 3.11, ruff 0.15.8, mypy 1.19.1, git.

## Three gates

| Gate | Result |
|---|---|
| 1 — Implementation / technical | PASS: checks 1 to 7 |
| 2 — Architecture / consistency | PASS: see below |
| 3 — Independent end-to-end / failure audit | PASS, no blocking finding; 6 non-blocking findings, all fixed: see below |

### Gate 2 — architecture and consistency (builder)

- **Each answer applied once, where it belongs:** CF-20 in the hosting set (MIG-033), CF-21 in PLT-010, DUP-40 in MKD-007 and MON-009 with the value kept only in TEC-012, OQ-28 and the feature process as confirmations without change, the review's acceptance in the registry generator. Nothing else changed meaning.
- **Only what the owner chose:** where an option left something open, the builder's reading is labelled in DEC-036 (the readiness bar; MKD-007's class, kept because the option shown did not change it; SEC-007 named in PLT-010).
- **History kept:** old texts quoted in DEC-036; decision records and the audit record annotated with "Later changes", never rewritten; register entries keep their sources and proposals.
- **Project memory:** the project state, roadmap, indexes, and registers agree: no finding waits for the owner; TC-09 and TC-10 stay open by design; the next step is the Stage 1 plan; implementation is not authorized.

### Gate 3 — independent review

**PASS.** An independent reviewer (a separate agent that did not write the change; read-only on the repository, experiments on a copy; `git status --short` identical before and after) re-verified the verbatim record against the session transcript (7 of 7 labels, questions, options, and answers; no notes), checked DEC-036 and every changed requirement against the chosen options, re-ran every tool, regenerated the indexes byte-identically on its copy, attacked the manifest (a changed word fails, a banner-only change passes), and swept every active document for stale statements. Its six non-blocking findings, all fixed before the commit:

| # | Finding | Fix |
|---|---|---|
| 1 | MKD-007's new wording narrowed its scope: the bracket of archived data types and "for backtesting" read as applying to all stored market data | Reworded: "Market data is stored, and OHLCV, trades, and order-book snapshots are archived for backtesting …"; a DEC-036 reading note says the scope is kept |
| 2 | DEC-009's "Later changes" line and the values register said the values are "stated only in TEC-012", though both state them | "Among the requirements …"; "No other requirement states it" |
| 3 | MIG-033 was missing from the reliability index and the TEC-011 note | Added to both |
| 4 | DEC-028's note did not mention that PLT-010 now matches DEC-006's "for others" | Added |
| 5 | DEC-035's "Next" line was out of date (already so at `16df57f`) | Its "Later changes" line now says the review is accepted and Stage 1 planning authorized |
| 6 | The reworded requirements' sections named only their original decisions; OQ-28 was marked RESOLVED where the register's rule says ANSWERED | "Wording since 2026-10-03: DEC-036" lines added; OQ-28 marked ANSWERED |

**Builder's own separate pass** (after the fixes): checks 2 to 7 re-run on the final tree; the stale-statement sweep and the hygiene scan repeated; the changed lines of the three specifications and three decision records re-read.

## Failures and fixes

| # | Failure | Cause | Fix | Re-run |
|---|---|---|---|---|
| 1 | The first build after the changes failed | The indexes linked this record before it existed | This record written | Check 2 PASS |
| 2 | PLT-010's first new wording called the transfer credentials "allowlisted", stronger than SEC-007's "where supported" | Written from the option's summary rather than SEC-007's text | Reworded: "a separate transfer credential (SEC-006) with the restrictions of SEC-007" | Check 3 PASS |
| 3 | The six Gate 3 findings | MKD-007 reworded from the values' point of view only; notes and indexes not swept for every place that lists the affected rules | Fixed as listed | Checks 2 to 7 PASS |

## Final status

**PASS.** All three gates passed. CF-20, CF-21, DUP-40, and OQ-28 are decided; the complete documentation review is accepted; Stage 1 planning is authorized (DEC-036). Remaining by design: TC-09 and TC-10 stay open until their stages are planned. Next: the Stage 1 plan, for the owner's approval. No platform code exists; implementation is not authorized.
