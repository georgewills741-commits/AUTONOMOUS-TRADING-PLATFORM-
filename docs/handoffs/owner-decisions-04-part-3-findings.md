# Owner Decisions 4 — Part 3 findings and review

> **Status:** HISTORICAL — source input: the owner's answers of 2026-10-02 to the eight questions left for the owner by the Part 3 reconciliation ([DEC-031](../decisions/DEC-031-part-3-reconciliation.md)) and the master execution constitution's adoption ([DEC-033](../decisions/DEC-033-adopt-master-execution-constitution.md)). This is **not** an active source of truth. Each answer is applied through [DEC-035](../decisions/DEC-035-owner-decisions-part-3-findings.md).
>
> **Formatting note:** the questions were asked in two rounds of multiple choice. Each is recorded with the short label shown above it, the question as asked, the options shown (label, then description), and the option the owner chose. The owner added no written notes. Nothing was added, removed, or changed in what was shown or answered; the round and question headings and the bold field names are the builder's.

## Round 1

### Q1 — CF-17

**Label shown:** CF-17 order

**Question as asked:** CF-17 — Rule precedence. Your safety floor (DEC-026) stays on top. Below it, Part 3's order is: your hard constraints → security → risk → capital → execution → strategy → market → AI. That means security controls outside the floor rank below your hard policy: the transfer restrictions (only to your own venue accounts) and AI least privilege. Where should those security controls rank?

**Options shown:**

- Security above my policy (Recommended) — Transfer restrictions and AI least privilege rank above your hard policy, like the safety floor. Your policy cannot override them; changing one needs a formal, audited security change. Safer: a policy mistake cannot open a transfer route or give AI more power.
- Keep Part 3's order — Security sits below your hard constraints, as Part 3 wrote it (except what is inside the safety floor). Your hard policy wins if it conflicts with those security controls. More flexible, less protected against a policy mistake.

**Owner's answer:** Security above my policy (Recommended)

### Q2 — CF-18

**Label shown:** CF-18 growth

**Question as asked:** CF-18 — Capital growth. When the account grows, the builder's resolution is: growth updates available capital and re-checks capabilities automatically, but it raises limits or authorized capital only where your policy already allows that scaling and the Readiness System has validated it. Anything else needs your approval. Confirm?

**Options shown:**

- Confirm (Recommended) — Automatic scaling only inside the bounds your policy already sets, after readiness validation. Raising a bound (more capital, leverage, venues) still comes to you.
- Always ask me — No limit or authorized capital ever rises from growth without your explicit approval, even within policy. Safest, but you are asked more often.
- Fully automatic — Growth may raise limits and authorized capital whenever readiness validates it, inside the safety floor, without prior policy authorization. Most autonomous; conflicts with Part 3's 'unless explicitly authorized' wording.

**Owner's answer:** Confirm (Recommended)

### Q3 — CF-19

**Label shown:** CF-19 cycle

**Question as asked:** CF-19 — Feature lifecycle. The master constitution (§107) requires one canonical lifecycle: IDEA → PROPOSED → APPROVED → DESIGNED → IMPLEMENTING → IMPLEMENTED → VERIFYING → PAPER/SAFE TEST → CANARY → PRODUCTION → DEPRECATED → RETIRED. Part 3 only proposed a different list: PROPOSED, RESEARCH, APPROVED, IN DEVELOPMENT, VALIDATING, DEPLOYED, DEPRECATED, RETIRED. Which is canonical?

**Options shown:**

- Constitution's lifecycle (Recommended) — Use §107's states. Part 3's names map onto them (IN DEVELOPMENT = IMPLEMENTING, VALIDATING = VERIFYING, DEPLOYED = CANARY or PRODUCTION, RESEARCH = evaluation before PROPOSED). Strategies keep their own lifecycle.
- Part 3's statuses — Use Part 3's shorter list as canonical and map the constitution's extra states (IDEA, DESIGNED, IMPLEMENTED, PAPER/SAFE TEST, CANARY) onto it.
- Decide at Stage 1 — Leave CF-19 open until features are actually tracked at Stage 1 planning. Nothing is blocked before then.

**Owner's answer:** Constitution's lifecycle (Recommended)

### Q4 — OQ-27

**Label shown:** Part 4?

**Question as asked:** OQ-27 — Part 3's header mentions 'PART 4 MATERIAL PREVIOUSLY DISCUSSED', and its end says Parts 1–3 are the complete knowledge base. Is a separate Handoff Part 4 coming?

**Options shown:**

- No, Parts 1–3 are complete — The documentation review treats Parts 1–3 (plus your decisions and the builder texts) as the complete knowledge base.
- Yes, Part 4 is coming — The complete documentation review waits for Part 4, so it is reconciled into the same knowledge base first.
- Not sure yet — The review proceeds assuming Parts 1–3 are complete; if Part 4 arrives later, it is reconciled the same way Parts 2 and 3 were.

**Owner's answer:** No, Parts 1–3 are complete

## Round 2

### Q5 — TC-08

**Label shown:** TC-08

**Question as asked:** TC-08 — Part 3 asks every decision record to state the alternatives considered. DEC-031 onward do; most of DEC-001 to DEC-030 don't, because the alternatives were never written down. What should happen to the older records?

**Options shown:**

- Add when amended (Recommended) — Add an Alternatives section to an older record only when it is next amended, and only where the alternatives were actually considered and can be sourced. Nothing is reconstructed from memory.
- Add now where sourced — The builder goes through DEC-001 to DEC-030 now and adds Alternatives wherever the repository shows what was considered; records with no sourced alternatives say so.
- Leave old records as they are — Only records from DEC-031 onward need Alternatives.

**Owner's answer:** Add now where sourced

### Q6 — DUP-34 reading

**Label shown:** DUP-34

**Question as asked:** DUP-34 reading — Part 3's 'Rebalancing Engine' is placed inside the Global Capital Authority as its rebalancing-decision component, not as a separate system. Its outcomes (NO ACTION, now, later, partial, pre-position, wait, emergency) refine the existing rebalancing decision (CAP-023), it holds no capital state, and every capital move goes through the Capital Authority. Is that what you intended?

**Options shown:**

- Confirm (Recommended) — One capital authority. The Rebalancing Engine is a component of it, so there is no second place where capital decisions or capital state can live.
- Make it its own system — Register the Rebalancing Engine as a separate system (a new SYS entry) that still moves capital only through the Capital Authority. More separation, more interfaces to keep consistent.

**Owner's answer:** Confirm (Recommended)

### Q7 — DUP-35 reading

**Label shown:** DUP-35

**Question as asked:** DUP-35 reading — Part 3's emergency names were mapped onto the safety levels you adopted, not added as a new set. NORMAL, PROTECTIVE (= RESTRICTED), EMERGENCY, and SAFE MODE are safety levels; DEGRADED stays a health state that feeds the safety level; RECOVERY covers automatic and critical recovery; RESUMING is the limited, step-by-step return to normal. Confirm?

**Options shown:**

- Confirm (Recommended) — Keep your adopted safety levels (NORMAL, CAUTION, RESTRICTED, SAFE MODE, EMERGENCY, CRITICAL RECOVERY) as the one set, with Part 3's names mapped onto them.
- Use Part 3's names instead — Replace the safety-level set with Part 3's names (NORMAL, DEGRADED, PROTECTIVE, EMERGENCY, SAFE MODE, RECOVERY, RESUMING). This changes RSK-015, which you adopted, by a new decision.

**Owner's answer:** Confirm (Recommended)

### Q8 — Part 3 human review

**Label shown:** Part 3 review

**Question as asked:** Part 3 human review (P3§541 items 29–30). With the answers you've just given, do you approve the Part 3 reconciliation (DEC-031), so the builder can move on to the complete documentation review?

**Options shown:**

- Approved — DEC-031 is confirmed with today's answers. Next: the complete documentation review, then the Stage 1 plan for your approval. Implementation still needs your explicit 'Begin Stage 1'.
- Not yet — You want to read the reconciliation yourself first. The builder waits; nothing else changes.

**Owner's answer:** Approved
