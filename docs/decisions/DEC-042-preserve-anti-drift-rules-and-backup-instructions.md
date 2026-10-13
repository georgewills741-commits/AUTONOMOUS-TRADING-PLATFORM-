# DEC-042 — Preserve the owner's anti-drift rules and backup instructions; apply the backup's lifecycle

- **Status:** ACCEPTED
- **Later changes:** On 2026-10-13 the reconciliation with checkpoint B's commit listed the labels each of the backup's commits carries ([checkpoint B verification](../traceability/stage-01-checkpoint-b-verification.md#reconciliation-of-the-temporary-backup)). Decision 4 gives the branch's status and says its commits "also" carry two more labels, as if every commit carried the status labels: nine of the eleven do. The first two, `ab78d52` and `540fe4a`, made on 2026-10-12, before the owner's lifecycle message, say UNVERIFIED, NOT APPROVED, NOT A VERIFIED CHECKPOINT, NOT PRODUCTION-READY, and NOT AUTHORIZED FOR MERGE. The text below is kept as written.
- **Date:** 2026-10-13
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and the owner's checkpoint rule ([DEC-032](DEC-032-adopt-checkpoint-and-verification-rule.md): "EVERYTHING MUST BE PRESERVED IN THE REPOSITORY"); the rules and instructions themselves are the owner's

## Context

Three messages of the owner arrived during Stage 1 while checkpoint B's gates were running:

- **2026-10-07** ([owner decisions 9](../handoffs/owner-decisions-09-requirement-drafting-and-anti-drift-rules.md)): permanent builder rules for drafting and reconciling requirements and against drift, which reinforce the existing builder texts rather than replace them (its Rule 0). The builder planned to adopt them as a builder text after checkpoint B's commit, so as not to mix that change into checkpoint B (constitution Rule 162), and kept the text in the session only. On 2026-10-13, while applying the owner's backup instructions, the builder found that this left the owner's rules, and their adoption as the next step, nowhere in the repository: the gap that Gate 3 found for owner decisions 8 ([DEC-041](DEC-041-preserve-opportunity-and-economics-directive.md)).
- **2026-10-12 and 2026-10-13** ([owner decisions 10](../handoffs/owner-decisions-10-unverified-backup-and-lifecycle.md)): check whether the existing rules permit an isolated backup of unverified work; if they do, preserve checkpoint B's work that way, labelled, and otherwise report the conflict; continue the verification sequence; then the lifecycle of any such temporary backup, to its reconciliation with the verified checkpoint and its retirement or retention under the repository's policy, asking the owner where no policy exists.

## Decision

1. **The three messages are preserved word for word now**, in checkpoint B's commit, as owner decisions 9 and 10, HISTORICAL sources listed in the preserved-text manifest.
2. **Owner decisions 9 changes nothing yet.** Its adoption as a builder text that `CLAUDE.md` loads is a later change, with its own decision record and three gates, made before the audit of owner decisions 8, since that audit drafts and reconciles requirements (the [project state](../project-state.md)'s "Next approved step").
3. **The rules permitted the backup, so it was made, on 2026-10-12.** DEC-032 governs the checkpoint commit, which waits for the three gates, and does not forbid a separate backup. The [master execution constitution](../builder/master-execution-constitution.md) allows remaining changes to be "committed or explicitly documented as intentionally uncommitted" (§52), defines an emergency checkpoint record (§132), and says how unverified work is labelled (§133). The owner's directive asks that substantial work not exist "only in an uncommitted or undocumented session state" ([DEC-034](DEC-034-verification-and-platform-independence.md)). And the builder pushes to a branch other than its designated one only with the owner's permission (the [stage record](../traceability/stage-01-foundation.md), "Machine checks on GitHub"), which these messages give. No backup mechanism, branch convention, or retention policy existed, and none is created beyond what the owner's messages state.
4. **The backup of checkpoint B is the branch `claude/unverified-backup-checkpoint-b`.** Its status: TEMPORARY, UNVERIFIED, PENDING VERIFICATION, NOT FOR MERGE, NOT PRODUCTION-READY (its commits also say NOT APPROVED and NOT A VERIFIED CHECKPOINT). It is traceable to the session and the work (each commit's message and trailers, and its emergency checkpoint record), to its verification process (checkpoint B's [verification record](../traceability/stage-01-checkpoint-b-verification.md), "Identity"), and, once resolved, to checkpoint B's commit, which the reconciliation records. Each update is a new commit on the branch, whose tree is the work then under verification; its history is never rewritten, and it is never merged.
5. **After checkpoint B's commit is pushed,** the builder compares the backup with it by owner decisions 10's eight checks and records the result. If a gate fails instead, the backup is kept and stays traceable until the work reaches one of owner decisions 10's terminal states.
6. **The repository has no branch-retention policy,** so whether a reconciled backup is deleted or kept, and how, is the owner's decision, asked as [OQ-30](../open-questions/register.md). The backup is kept until the owner answers. The owner answered on 2026-10-13: the reconciled backup's last commit is kept under an archive tag and the branch deleted ([DEC-043](DEC-043-retire-checkpoint-b-backup-under-an-archive-tag.md)).
7. **Owner decisions 10's lifecycle applies to any later temporary backup too.** Whether it joins a builder text that `CLAUDE.md` loads is decided with owner decisions 9's adoption.

## Alternatives considered

- **Keep owner decisions 9 in the session until its adoption.** Rejected: a session ending first would lose the owner's rules and the request to adopt them (master execution constitution §01, §90).
- **Adopt owner decisions 9 in checkpoint B's commit.** Rejected: it changes the builder texts that every session loads, a governance change that needs its own gates, and it would mix that change into checkpoint B (constitution Rule 162).
- **Choose a retention policy for the backup.** Rejected: owner decisions 10 says not to invent one, and to ask where none exists.

## Consequences

- Checkpoint B's commit also carries this record, the two preserved texts, OQ-30, and the backup's description; its verification record says so.
- The project state's next steps are: reconcile the backup once checkpoint B is pushed; adopt owner decisions 9; then the audit of owner decisions 8; then checkpoints C and D.
- Under owner decisions 10, a session that starts before checkpoint B's commit exists inspects the repository first, finds the work on the backup branch, and recovers it from there, never redoing it.
