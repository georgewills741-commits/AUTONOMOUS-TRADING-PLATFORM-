# Owner Decisions 40 — The approval of Stage 2's plan, with changes to D1 and D2, of 2026-11-17

> **Status:** HISTORICAL — source input: the owner's answers of 2026-11-17, 18:58 UTC, to the builder's two questions of 17:32 UTC on the plan of Stage 2, DATA FOUNDATION: whether the owner approves the plan with the builder's recommendations for its decisions D2 to D12, and which of the five initial exchanges the owner's account is legally permitted to use where the owner is (D1). The owner approves the plan with changes: its overall technical direction and the recommendations D3 to D12, subject to the existing canonical requirements, with conditions: for D1, the five candidate exchanges kept, none assumed available, public read-only market-data access verified per venue without credentials or workarounds, and account eligibility and trading authorization kept apart from it; for D2, a focused environment-readiness check before infrastructure-dependent implementation, the smallest compliant solution, and a report with the safest alternative and any decision or expense for the owner where the environment cannot be provided; Stage 2 strictly read-only, a small opportunity never discarded for its small apparent percentage; the gates, security, testing, traceability, and recovery rules kept, with no duplicates and no rework beyond what the changes affect; and D1 and D2 updated, reconciled, and verified before the authorized checkpoints proceed. To the second question the owner keeps all five as candidate market-data sources without declaring the account authorized on each. This is **not** an active source of truth. It is applied by [DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md).
>
> **Formatting note:** the questions are recorded as [owner decisions 34](owner-decisions-34-approval-to-plan-stage-2-and-answers-on-the-directive.md) and [owner decisions 38](owner-decisions-38-one-reusable-backup-branch.md) record theirs: the short label shown above each, the question as asked, the options shown (label, then description), the preview shown beside the first option of the first question, and the owner's answer, in a text block. Each answer is reproduced exactly as received. Nothing was added, removed, or changed in them. The title, this banner, and the headings are the builder's.

## The questions of 2026-11-17, 17:32 UTC, and the answers of 18:58 UTC

### Q1 — the Stage 2 plan

**Label shown:** Stage 2 plan

**Question as asked:** Do you approve the Stage 2 (Data Foundation) plan with my recommendations for its decisions D2 to D12? Stage 2 builds read-only market-data collection, quantitative and market-regime analysis, and opportunity monitoring. It holds no exchange credentials, reads no account, and cannot place orders. Nothing is built until you approve.

**Options shown:**

- Approve as recommended (Recommended) — I record your approval in a decision record, then start checkpoint A: environment, data contracts, and the measurement framework.
- Approve with changes — Tell me which decisions to change (in the notes or Other). I update the plan, through its gates, before anything is built.
- Not yet — I explain any decision in more detail first. Nothing is built meanwhile.

**Preview shown beside the option "Approve as recommended (Recommended)":**

```text
D2  Runs in this cloud environment; latency figures are first baselines only. Hard limits (V-08, V-17) stay unset until you set them.
D3  Provisional data-freshness and clock-drift limits, from first measurements, used only to mark data.
D4  One code module per system, imports in one direction only.
D5  Exact amounts from each exchange's own text; UTC nanosecond times; repeatable evidence IDs; floats only in indicators.
D6  TimescaleDB with exact NUMERIC amounts; versioned SQL migrations, with a restorable backup before any data-rewriting one; Parquet archive after 30 days.
D7  One process with bounded internal queues (no message bus yet); OpenTelemetry metrics, JSON logs; Docker Compose for the dev database.
D8  Each exchange's published fee schedule in configuration, with source and date.
D9  Eight market-regime states from versioned, deterministic rules.
D10 Deterministic opportunity filters; size orders the search but never drops a small opportunity.
D11 Recorded public data replayed in tests; live checks opt-in only.
D12 New libraries: CCXT, psycopg 3, DuckDB, OpenTelemetry, testcontainers. Pinned and reviewed for advisories and licenses.
```

**Owner's answer:**

```text
I select **Approve with changes** for Stage 2 — Data Foundation.

I approve the overall technical direction and the recommendations D3–D12, subject to the existing canonical requirements and the following conditions.

**1. D1 — Exchange authorization and availability**

Preserve the five previously selected candidate exchanges: Binance, OKX, Coinbase, Bybit, and KuCoin, with architecture extensible to additional exchanges.

Do not assume all five are legally or technically available to the operator. Verify public-data access and applicable restrictions before enabling each venue, and distinguish read-only market-data availability from future trading eligibility.

Do not contact prohibited endpoints or bypass geographical restrictions. Request only genuinely missing owner-level information.

**2. D2 — Infrastructure readiness**

The Stage 2 plan identifies that the current cloud environment lacks a running Docker daemon and TimescaleDB.

Before beginning infrastructure-dependent implementation, perform a focused environment-readiness check.

Determine the smallest compliant solution using the approved technology stack and existing available infrastructure.

If the necessary environment cannot be provided, report the exact limitation, safest viable alternative, dependencies, and any decision or expense requiring my approval.

Do not spend repeated development cycles attempting a configuration already known to be unavailable.

**3. Preserve our existing trading architecture**

Stage 2 remains strictly read-only.

Maintain accurate numerical processing, reliable market-data validation, clock synchronization, deterministic quantitative analysis, extensible regime detection, and continuous opportunity monitoring.

Preserve our previously approved rule that smaller opportunities must not be discarded solely because their apparent profit percentage is small.

Do not introduce live trading, private account access, capital deployment, or order execution during this stage.

**4. Preserve project quality and efficiency**

Maintain all three verification gates, security requirements, testing, traceability, root-cause correction, and repository recovery rules.

Do not create duplicate functionality or governance mechanisms.

Do not rework unrelated approved parts of the plan. Revalidate only what the changes materially affect, subject to the existing mandatory verification rules.

Keep the process efficient and avoid unnecessary token consumption, repeated reviews, or preventable loops.

**5. Controlled authorization**

Update D1 and D2 to reflect these conditions, reconcile them with existing canonical decisions, and complete the required plan verification.

This approval does not authorize bypassing unresolved entry prerequisites, making unapproved infrastructure purchases, or weakening technical requirements.

Once the revised plan satisfies its entry conditions and required verification, proceed with the authorized Stage 2 checkpoints according to the established roadmap.

I want faster meaningful implementation, but never at the expense of financial safety, technical correctness, or long-term company-grade reliability.
```

### Q2 — the exchanges

**Label shown:** Exchanges

**Question as asked:** Which of the five initial exchanges (Binance, OKX, Coinbase, Bybit, KuCoin) is your trading account legally permitted to use where you are? This is decision D1. Stage 2 only reads their public market data, but the platform enables an exchange only where your account may use it, and never works around a regional restriction.

**Options shown:**

- All five — Adapters for all five; each is enabled only if it also answers from this environment without a workaround.
- None confirmed yet — No exchange is contacted until you confirm; the work that needs no exchange can go ahead. To name some, type them in Other.

**Owner's answer:**

```text
**D1 — Exchange Selection and Authorization**

Preserve all five previously approved initial exchanges: Binance, OKX, Coinbase, Bybit, and KuCoin. Maintain the architecture's ability to support additional exchanges later.

I want all five retained as candidate market-data sources, but I am not making an unverified declaration that my trading account is legally authorized on every exchange.

For Stage 2:

1. Distinguish exchange support, lawful public market-data access, account eligibility, and future trading authorization.
2. Where permitted by applicable laws and the exchange's terms, verify each exchange's public, read-only API access from the current environment without credentials or restriction workarounds.
3. Enable public market-data monitoring only for venues whose access is confirmed and permitted.
4. Keep venues with unresolved access or eligibility disabled for the relevant operation, with their status recorded.
5. Do not equate successful public API access with permission for authenticated trading.
6. Do not access private accounts, submit orders, or authorize live trading during Stage 2.
7. Before later trading activation, require verification of the account's actual eligibility, supported instruments, jurisdiction, and all applicable risk and readiness gates.

Preserve DEC-008, EXA-005, EXA-006, EXA-007, and the existing canonical requirements. Do not duplicate exchange adapters or create conflicting authority.

Continue Stage 2 through the approved roadmap and three verification gates. Do not bypass restrictions or claim unverified authorization.
```
