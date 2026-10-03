# Owner Decisions 5 — Audit findings, review acceptance, and Stage 1 planning

> **Status:** HISTORICAL — source input: the owner's answers of 2026-10-03 to the seven questions left for the owner by the [master knowledge-base audit](../traceability/master-knowledge-base-audit-2026-10-02.md): its four open findings (CF-20, OQ-28, CF-21, DUP-40), the optional confirmation of the feature process, the acceptance of the review, and the authorization of Stage 1 planning. This is **not** an active source of truth. Each answer is applied through [DEC-036](../decisions/DEC-036-owner-decisions-audit-findings.md).
>
> **Formatting note:** the questions were asked in two rounds of multiple choice. Each is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the option the owner chose. The owner added no written notes. Nothing was added, removed, or changed in what was shown or answered; the round and question headings and the bold field names are the builder's.

## Round 1

### Q1 — CF-20

**Label shown:** CF-20 host

**Question as asked:** CF-20 — Hosting. Some requirements say local hosting must be supported and you must not be forced into one hosting setup (MIG-001, MIG-002, PLT-017). Your audit request says production must NOT depend on your laptop. May the live trading platform run on your own computer?

**Options shown:**

- No single machine (Recommended) — Production never depends on any one machine, yours included: an active host plus a standby (DEC-030), and it can be rebuilt without you (OPS-017). Your computer can still be a production host, but only if it meets the same readiness bar as a server.
- Never on my computer — Live trading always runs on servers or the cloud. Your own computer is only for development, research, and paper trading. This narrows MIG-001's local hosting, by decision record.

**Owner's answer:** No single machine (Recommended)

### Q2 — OQ-28

**Label shown:** OQ-28 scope

**Question as asked:** OQ-28 — Instruments. DEC-007 records your answer 'all, because the control risks are there' as three types: spot, perpetual futures, and margin (PLT-011). The original question also mentioned 'other derivatives'. Which instruments should the platform trade? Every type stays switched off until its risk controls are in place (PLT-012).

**Options shown:**

- Spot, perpetuals, margin (Recommended) — Confirm PLT-011 as it stands. No other derivatives.
- Add dated futures — Also futures that expire on a set date (quarterly futures). Adds their own risk rules (expiry, rollover) to the CORE TRADING FOUNDATION stage.
- Add dated futures and options — Also expiring futures and options. Options bring a separate risk model (Greeks, expiry, assignment), which is a much larger scope.

**Owner's answer:** Spot, perpetuals, margin (Recommended)

### Q3 — CF-21

**Label shown:** CF-21 words

**Question as asked:** CF-21 — Withdrawal wording. PLT-010 says the platform has 'no deposit, withdrawal, or multi-user account functions'. Your original decision (DEC-006) said 'no deposit or withdrawal handling for others'. Read literally, PLT-010 would block the rebalancing transfers between your own exchange accounts that you approved (DEC-019, SEC-006). What should PLT-010 say?

**Options shown:**

- Match DEC-006 (Recommended) — PLT-010 says 'no deposit or withdrawal handling for others' and points to SEC-006: rebalancing transfers only between your own allowlisted accounts, with their own separate keys. No custody and no general withdrawals stay forbidden.
- You decide — Delegate the wording to the builder, within DEC-006 and SEC-006.
- No transfers at all — Keep PLT-010 literal: the platform never moves funds between exchanges. This takes away the rebalancing transfers you approved in DEC-019, so automatic rebalancing would be dropped.

**Owner's answer:** Match DEC-006 (Recommended)

### Q4 — DUP-40

**Label shown:** DUP-40

**Question as asked:** DUP-40 — Retention values. Market data kept 30 days and then archived (MKD-007), and operational logs kept 90 days (MON-009), are written in two places each. The other place is the technology-stack choice TEC-012, which has a different class. Where should those values live?

**Options shown:**

- Only in TEC-012 (Recommended) — The values stay in the technology-stack decision. MKD-007 and MON-009 point to it instead of repeating the numbers. One place to change later.
- You decide — Delegate to the builder, under your stack delegation (DEC-009).
- Leave both as they are — Keep the values in both places. They must then always be changed together.

**Owner's answer:** Only in TEC-012 (Recommended)

## Round 2

### Q5 — Feature process

**Label shown:** Features

**Question as asked:** Feature process. Your audit request lists a 19-step sequence for adding any future feature (understand, inspect, classify, check duplicates and conflicts, design, implement, verify, release, monitor, document). The existing upgrade process already covers every step: GOV-002 with GOV-022, under GOV-021 and GOV-024. The mapping is written in Architecture governance. Is that the process you meant?

**Options shown:**

- Yes, use GOV-002/GOV-022 (Recommended) — Your sequence stays mapped onto the existing process. There is one process and no duplicate list to keep in step.
- Add my list as its own rule — Record your 19 steps word for word as a separate requirement, by decision record. It must then be kept consistent with GOV-002 and GOV-022.

**Owner's answer:** Yes, use GOV-002/GOV-022 (Recommended)

### Q6 — Documentation review

**Label shown:** Review

**Question as asked:** The audit (verdict B: ready with non-blocking findings) is the complete documentation review that handoff §101 and P2§329 require before implementation. Do you accept it? If you do, the registry's status for the 512 handoff requirements changes from 'pending documentation review' to 'reviewed'.

**Options shown:**

- Accept the review (Recommended) — The documentation review is closed, with your decisions from this round applied.
- Ask for changes — Say what should be checked or changed first, using Other or the notes.

**Owner's answer:** Accept the review (Recommended)

### Q7 — Stage 1 planning

**Label shown:** Stage 1

**Question as asked:** Stage 1 planning. May the builder now write the Stage 1 (FOUNDATION) plan, with its objective, scope, out-of-scope, dependencies, outputs, tests, verification, and completion criteria (constitution Rule 140), for your approval? This is planning only. No platform code is written until you separately say 'Begin Stage 1'.

**Options shown:**

- Authorize planning (Recommended) — The builder writes the Stage 1 plan, verifies it through the three gates, commits it, and stops for your approval.
- Not yet — Apply this round's decisions and stop. No Stage 1 plan yet.

**Owner's answer:** Authorize planning (Recommended)
