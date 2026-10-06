# Owner Decisions 1 — Part 1 open items put to the owner

> **Status:** HISTORICAL — source input: the owner's answers of 2026-09-30 to the four questions the Part 1 resolution round put to the owner directly (OQ-01, OQ-04, OQ-03, OQ-16). This is **not** an active source of truth. Each answer is applied through the decision record linked under it. Preserved on 2026-10-05 from the session record of the questions as asked and the answers as given, the same record the later owner-decision files were made from ([DEC-037](../decisions/DEC-037-final-decision-and-integrity-checkpoint.md)); until then only the decision records summarized these answers (master knowledge-base audit, finding A-17). The round was started by the owner's instruction of 2026-09-30, given before Handoff Part 2 and reproduced first below. Under it, four questions went to the owner directly; the builder accepted DEC-001 to DEC-005 (first recorded as PROPOSED) and decided all other open Part 1 items (DEC-010 to DEC-018, and the builder's parts of DEC-006 and DEC-008).
>
> **Formatting note:** first, the owner's instruction that started this resolution round, inside a text block exactly as written. Then the four questions, asked in one round of multiple choice. Each is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the answer. Where the owner chose an option, its label is quoted. Where the owner wrote an answer instead, it is reproduced inside a text block exactly as given; nothing was added, removed, or changed, including spelling. The question on venues allowed more than one option. The section and question headings, the bold field names, the bracketed notes after them, and the decision-record links are the builder's.

## The owner's instruction that started this round

```text
before i gave you the the hand off part two resolve the Unresolved items:
```

## Q1 — OQ-01 — custody and user model

**Label shown:** Custody

**Question as asked:** Who does the platform trade for, and who holds the funds? (Resolves OQ-01 custody/user model; also sets ledger and security scope.)

**Options shown:**

- Single operator (Recommended) — You trade your own capital through API keys on your own exchange accounts. No custody, deposits, withdrawals, or user accounts. The §84 custody model is recorded as FUTURE, not built.
- Multi-user, own exchange keys — Several users connect their own exchange accounts via API keys. No custody, but requires user accounts, per-user policy and capital isolation.
- Multi-user with custody — Users deposit funds into a platform account. Requires custody, wallets, a double-entry ledger, withdrawal controls, key management and compliance. Much larger scope with regulatory obligations.

**Owner's answer:** Single operator (Recommended)

**Applied by:** [DEC-006](../decisions/DEC-006-single-operator-and-trading-ledger.md)

## Q2 — OQ-04 — instruments

**Label shown:** Instruments

**Question as asked:** Which instruments should the first version trade? (Resolves OQ-04; drives the risk model, adapters and economics.)

**Options shown:**

- Spot only (Recommended) — Simplest and safest risk model: no leverage, margin or liquidation. Funding rates used only as market signals. Derivatives recorded as FUTURE.
- Spot + perpetual futures — Enables funding-rate opportunities and hedged arbitrage legs, but adds leverage, margin and liquidation risk to every core system.
- Spot, perps and margin — Widest opportunity set; largest risk surface and implementation scope.

**Owner's answer** (written, not one of the options):

```text
all because the control risks are there
```

**Applied by:** [DEC-007](../decisions/DEC-007-instrument-scope.md)

## Q3 — OQ-03 — venues

**Label shown:** Venues

**Question as asked:** Which exchanges should be in scope first? (Resolves OQ-03. Cross-exchange arbitrage needs at least two. Availability depends on your jurisdiction.)

**Options shown:** (more than one could be chosen)

- Binance — Previously discussed in the handoff (§42). Largest liquidity; not available in some jurisdictions.
- OKX — Previously discussed in the handoff (§42).
- Coinbase — Previously discussed in the handoff (§42). Widely available, including in the US.

**Owner's answer** (written, not one of the options):

```text
all add more space for more exchange like bybit and many more like kucoin exchange
```

**Applied by:** [DEC-008](../decisions/DEC-008-venues-and-trading-universe.md)

## Q4 — OQ-16 — technology stack

**Label shown:** Tech stack

**Question as asked:** Which primary technology stack should the platform use? (Resolves OQ-16; the constitution forbids me choosing this silently.)

**Options shown:**

- Python core (Recommended) — Python 3.12+ asyncio with exact Decimal arithmetic, PostgreSQL (+ time-series extension). Best ecosystem for exchange APIs, quant, backtesting and AI SDKs. Venue API latency (tens of ms) dominates; measured hot paths can move to Rust later.
- Rust core + Python research — Maximum speed and memory safety on the execution path; Python only for research/backtesting. Higher build complexity and slower delivery.
- Decide after Part 2 — Leave the stack open until Part 2's requirements are known. OQ-16 and storage (OQ-22) stay open.

**Owner's answer** (written, not one of the options):

```text
choose the best combination that suit mt system well
```

**Applied by:** [DEC-009](../decisions/DEC-009-technology-stack.md)
