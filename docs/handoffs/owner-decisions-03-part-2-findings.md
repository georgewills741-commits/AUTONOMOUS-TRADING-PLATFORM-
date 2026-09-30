# Owner Decisions 3 — Part 2 findings

> **Status:** HISTORICAL — source input: the owner's answers of 2026-09-30 to the ten questions raised by the Handoff Part 2 reconciliation ([DEC-024](../decisions/DEC-024-part-2-reconciliation.md)). This is **not** an active source of truth. Each answer is applied through the decision record linked under it.
>
> **Formatting note:** the questions were asked in three rounds of multiple choice; each is quoted as asked, with the options shown. Where the owner chose an option, the option is quoted. Where the owner wrote an answer, it is reproduced inside a text block exactly as given; nothing was added, removed, or changed. An earlier attempt to ask Q1 to Q4 was dismissed by the owner, who then asked for the questions to be shown; that attempt has no answers and is not reproduced.

## Q1 — CF-14

**Question as asked:** Who has the final word, your hard rules or the platform's built-in safety rules (e.g. never trade on stale prices, never trade an exchange whose balances don't match our records)?

**Options shown:**

- Safety floor (Recommended) — Nobody can switch off a safety rule, not even you. Above that floor, your hard rules beat everything else and can always make the platform stricter.
- My rules win outright — Your hard rules win even over a safety rule, as Part 2 wrote it.
- Safety, named exceptions — Safety rules win, but you may switch off one named rule through an explicit, confirmed, logged change. AI can never do this.

**Applied by:** [DEC-026](../decisions/DEC-026-safety-floor-and-layered-control.md)

**Owner's answer (verbatim; written, not one of the options):**

```text
SAFETY-FLOOR PRINCIPLE:

The platform's immutable system-safety invariants must never be disabled or bypassed by an AI agent, strategy, policy, administrator, or automatic process.

However, the safety floor must not be confused with ordinary operational limits or configurable policies.

The platform shall use a layered control model:

1. IMMUTABLE SAFETY INVARIANTS
   These cannot be overridden:
   - Never trade on stale or invalid market data.
   - Never execute against an unreconciled exchange state.
   - Never exceed the platform's absolute risk boundaries.
   - Never send an invalid, duplicated, unauthorized, or unsafe order.
   - Never trade when required exchange connectivity/integrity checks fail.
   - Never allow an AI agent to directly bypass deterministic safety enforcement.

2. CONFIGURABLE POLICY LAYER
   Capital allocation, strategy limits, exposure limits, execution parameters, opportunity thresholds, and other operational policies may be changed automatically or administratively, but only within the immutable safety envelope.

3. ADAPTIVE OPERATION
   The platform may automatically adjust operational limits, execution methods, capital allocation, strategy availability, and opportunity thresholds according to available capital, liquidity, market conditions, system health, historical performance, and verified risk conditions, provided that no immutable safety invariant is violated.

4. RECOVERY AND FAIL-SAFE BEHAVIOR
   If a safety condition temporarily blocks an operation, the platform should automatically diagnose the cause, attempt safe recovery where possible, revalidate all required conditions, and resume only when the safety requirements are satisfied.

5. NO DEADLOCK BY SAFETY
   A safety rule must prevent unsafe activity, not permanently disable unrelated healthy parts of the platform. The system should isolate the affected component, preserve unaffected operations where safe, and recover automatically when possible.

6. EXPLICIT CHANGE CONTROL
   Any proposed change to an immutable safety invariant must require a formal, versioned, audited human-controlled policy change. AI may analyze and propose such changes, but may never authorize or silently implement them.

The objective is maximum autonomy inside a deterministic safety envelope: the system should be capable of operating 24/7 and recovering intelligently without sacrificing the fundamental safety guarantees of the platform.
```

## Q2 — OQ-25

**Question as asked:** Where does a strategy run while it trades with simulated money (paper mode)?

**Options shown:**

- Separate setup (Recommended) — A separate paper setup that sees live prices but holds no real exchange keys, so it cannot touch your accounts.
- Inside live system — Runs inside the live system, with its orders sent to the simulator.

**Applied by:** [DEC-027](../decisions/DEC-027-part-2-open-questions.md)

**Owner's answer:** selected "Separate setup (Recommended)".

## Q3 — OQ-24

**Question as asked:** What is the 'global platform controller' that Part 2 names but never defines?

**Options shown:**

- Existing parts (Recommended) — Not a new system: the name for your policy rules, the Risk Engine's emergency controller, and System Health working together.
- New system — A new, separate system. You would tell me what it does beyond those three.

**Applied by:** [DEC-027](../decisions/DEC-027-part-2-open-questions.md)

**Owner's answer:** selected "Existing parts (Recommended)".

## Q4 — OQ-26

**Question as asked:** What is 'adaptive execution', mentioned once in Part 2's checklist and never defined?

**Options shown:**

- Future feature (Recommended) — Execution that adjusts order type, order splitting, and price to liquidity and volatility, inside risk limits. Not built until you approve it.
- Keep as idea — Leave it undefined for now.
- Drop it — Not part of the platform.

**Applied by:** [DEC-027](../decisions/DEC-027-part-2-open-questions.md)

**Owner's answer:** selected "Future feature (Recommended)".

## Q5 — TC-07

**Question as asked:** When the platform moves between your computer and a server, how do we make sure only one copy trades? (Each copy has its own database, so the current 'one active copy' lock can't see the other.)

**Options shown:**

- Freeze + new keys (Recommended) — During every move, freeze the old copy, then create new exchange API keys for the new location and delete the old ones, so the exchange itself refuses the old copy.
- Decide later — Leave it open until the migration feature is planned.

**Applied by:** [DEC-030](../decisions/DEC-030-high-availability-and-single-active-copy.md)

**Owner's answer:** selected "Freeze + new keys (Recommended)".

## Q6 — CAP-028

**Question as asked:** Add three more capital categories: money for directional trading, an emergency reserve, and a reserve per exchange?

**Options shown:**

- Yes, policy-set (Recommended) — Add them, with the amounts set in your policy rather than fixed in code.
- No — Keep the current capital categories.

**Applied by:** [DEC-028](../decisions/DEC-028-capital-buckets-and-progressive-activation.md)

**Owner's answer (verbatim; written, not one of the options):**

```text
Yes — policy-set, dynamically managed.

Add:
1. Directional Trading Capital
2. Emergency Reserve
3. Per-Exchange Reserve

These must be controlled by the Capital Allocation & Treasury Engine, not fixed hard-coded amounts. Allocation should dynamically scale with total available capital, risk exposure, liquidity, exchange requirements, active strategies, withdrawal/transfer constraints, and system health.

The system must automatically rebalance these capital buckets when conditions justify it, without requiring me to be online or manually approve routine movements. However, all transfers must remain within hard safety, risk, liquidity, and authorization policies.

Capital allocation must also support progressive capability activation: smaller accounts operate safely within their available capital and do not activate capital-intensive features prematurely. As capital grows and the system proves sufficient capacity and safety, additional capabilities may become eligible automatically.

No capital movement may violate the platform's safety floor, emergency reserve requirements, exchange-specific reserves, exposure limits, or reconciliation requirements.
```

## Q7 — OPS-009

**Question as asked:** Manage the server setup as code files ('infrastructure as code')?

**Options shown:**

- Not separately (Recommended) — Not a separate commitment for now; the Docker setup file kept in the repository already covers it.
- Yes, approve now — Approve infrastructure as code as a requirement now.

**Applied by:** [DEC-029](../decisions/DEC-029-infrastructure-as-code.md)

**Owner's answer (verbatim; written, not one of the options):**

```text
YES — Infrastructure as Code is a mandatory production requirement.

All production infrastructure must be reproducible and version-controlled as code. This includes compute, containers, networking, databases, storage, monitoring, logging, alerting, deployment, scaling, failover, backup, and disaster-recovery configuration.

Infrastructure must be separated logically from application code and may be placed in a dedicated infrastructure repository when the project structure requires it. The system must not depend on undocumented manual server configuration.

Infrastructure changes must be validated, tested, reviewed, auditable, and safely deployable/rollbackable. Secrets must never be stored as plaintext in the repository.

The architecture must support automated provisioning, recovery, migration between environments, and rebuilding production infrastructure without relying on my physical availability.
```

## Q8 — ARCH-034

**Question as asked:** A special short command language for giving the system instructions?

**Options shown:**

- Keep as idea (Recommended) — Leave it as an idea; nothing is built.
- Approve it — Make it a planned feature.
- Drop it — Not part of the platform.

**Applied by:** [DEC-027](../decisions/DEC-027-part-2-open-questions.md)

**Owner's answer:** selected "Keep as idea (Recommended)".

## Q9 — REC-021

**Question as asked:** Should there be a standby copy that takes over automatically if the main one fails (high availability)?

**Options shown:**

- Not now (Recommended) — One active copy that restarts itself automatically; revisit after the platform goes live.
- Yes, plan it now — Plan a standby copy that takes over after checking and reconciling state.

**Applied by:** [DEC-030](../decisions/DEC-030-high-availability-and-single-active-copy.md)

**Owner's answer:** selected "Yes, plan it now".

## Q10 — DEC-024

**Question as asked:** Keep my five organizing choices from merging Part 2? (a) The Readiness System, which decides when a strategy may go live, is its own system. (b) Canary (trying a strategy live with a small amount of money) runs inside the live system, not a separate environment. (c) The Performance Controller, which compares expected and actual results, is built one stage earlier, because paper trading needs it. (d) One opportunity database for the whole platform. (e) Five AI agents plus deterministic services cover all nine AI roles.

**Options shown:**

- Keep all five (Recommended) — Keep them as recorded in DEC-024.
- Change some — Tell me which ones to change (use Other to write it).

**Applied by:** [DEC-027](../decisions/DEC-027-part-2-open-questions.md)

**Owner's answer:** selected "Keep all five (Recommended)".
