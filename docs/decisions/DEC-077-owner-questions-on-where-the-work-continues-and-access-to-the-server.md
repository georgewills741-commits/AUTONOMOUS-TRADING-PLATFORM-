# DEC-077 — The owner's questions of 2026-11-20 on where the work continues and on the builder's access to the server (owner decisions 44)

- **Status:** ACCEPTED
- **Date:** 2026-11-20
- **Decided by:** builder, under [DEC-004](DEC-004-preserve-original-handoffs.md) (original source material is preserved verbatim) and [DEC-047](DEC-047-preserve-stage-transition-persistence-rules.md) (decision 7: the owner's messages that carry an approval, an instruction, or a question are kept); the instruction on the builder's access to the server is the owner's.

## Context

During Gate 3's run 1 of the first increment of Stage 2's checkpoint B, the owner sent two messages ([owner decisions 44](../handoffs/owner-decisions-44-questions-on-where-the-work-continues-and-access-to-the-server.md)). The client delivered each as a user turn of its own, of origin human, so each is the owner's.

The first, queued at 11:06 UTC while the builder worked and delivered at 11:35 UTC, asks whether a server is rented for a period of data collection and the work then comes back here, or whether the building continues there. The builder answered at 11:36 UTC:

- **The building stays here:** code, tests, the three gates, and commits are made in this environment and the repository, for the whole project.
- **The server runs the platform's parts:** in Stage 2, the collectors of the venues whose access is verified, the database with 30 days of market data, and the measurement framework ([Stage 2 record](../traceability/stage-02-data-foundation.md), "Hosting options for Stage 2's live work"); U1 found no venue's public market data permitted from this environment, in the United States, and the platform runs without a session ([DEC-034](DEC-034-verification-and-platform-independence.md)). What it records and measures comes back to the repository.
- **How long:** from the first connection to a venue, for as long as live collection is wanted, through Stage 2's live work and the stages after it; switched off, it collects nothing. Nothing is bought yet.

The second, of 11:56 UTC, quotes the builder's sentence "Either you run the setup steps the repository gives you, or you give this workspace key-based access to it" and says that the owner wants the builder to have access, to set the server up completely and see it, the owner giving the keys. The builder answered at 11:57 UTC:

- **This environment cannot connect to a server by SSH:** at 11:57 UTC a direct connection to port 22 (of github.com, an SSH server) was refused, and no SSH client is installed.
- **Its recommendation:** Claude Code run on the server itself. The owner creates the server in the owner's account, with the owner's own login key, logs in once, installs Claude Code, signs in, and opens this repository there; the builder then sets the server up and sees all of it, the setup written in the repository and verified through the three gates, and no key passing through the chat. The alternative: Claude Code on the owner's own computer, which can log in to the server but must be on while the builder works.
- **Its limits:** suited to Stage 2, whose server holds no trading credential; before any trading credential goes on a server, the builder's access to it is reviewed, as the rules keep production secrets from unrestricted AI agents (master execution constitution §42); Claude Code on the server uses the owner's Claude account and its usage limits.

## Decision

1. **Both messages are preserved word for word**, as owner decisions 44, a HISTORICAL source listed in the preserved-text manifest. They were taken by script from their user turns in the session record and kept byte for byte, including the space that ends the first message and the one that ends the second's first line, so `git diff --check` reports those lines; the text is not trimmed to satisfy it.
2. **The first is a question, answered; it changes nothing.** The building continues in the repository, and the server runs the platform's parts, as the Stage 2 record and DEC-034 state.
3. **The second is the owner's instruction for when a server is approved:** the builder is to have the access needed to set the server up completely and see it, the owner giving that access. The Stage 2 record states it ("Hosting options for Stage 2's live work"). How: RECOMMENDED — NOT YET APPROVED, Claude Code run on the server under the owner's login, since this environment cannot open SSH connections; the owner confirms it, or chooses the alternative, when the server is ordered. Unchanged: no server is approved ([DEC-075](DEC-075-owner-operating-decisions-and-future-membership.md), decision 2); the owner orders the server in the owner's own account, and the builder buys nothing and holds no billing access ([DEC-073](DEC-073-stage-2-plan-approved-with-changes.md), decision 6; [DEC-074](DEC-074-owner-answers-on-jurisdiction-operator-server-and-exchanges.md), decision 4); no key goes in the chat or the repository; and before any trading credential goes on a server, the builder's access to it is reviewed (master execution constitution §42).
4. **They are preserved with the change in progress, whose record names them** ([checkpoint B (U5) verification](../traceability/stage-02-checkpoint-b-u5-verification.md)): that change's Gate 3 run 2 reviews a copy made after both ([traceability README](../traceability/README.md), Scope); the first was queued before run 1's copy and delivered after it, which run 1 found (its I-03).

## Alternatives considered

- **Treat the first message as procedural.** Not chosen: it asks a question, which DEC-047 (decision 7) keeps.
- **Take the account's keys, so that the builder orders and manages the server.** Not chosen: the builder holds no billing access (DEC-073, decision 6; DEC-074, decision 4), and setting the server up needs access to the server only.
- **Connect from this environment by SSH with a key the owner gives.** Not possible: the environment refuses such a connection and has no SSH client; a key would also have to pass into an environment whose files do not outlast its session.
- **Trim the messages' spaces, so that `git diff --check` stays clean.** Not chosen: a text kept in a text block equals the message as received, byte for byte (the [documentation tools](../../tools/docs/README.md)' rule for preserved texts).

## Consequences

- Owner decisions 44 is listed in the preserved-text manifest and the documentation index.
- The Stage 2 record states who sets the server up, and how, as RECOMMENDED; the project state lists it with the server's approval.
- The record of the change in progress names both messages.
- No requirement, rule, gate, or code changes, and no server is approved.
