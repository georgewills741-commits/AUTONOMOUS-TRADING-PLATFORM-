# AUTONOMOUS-TRADING-PLATFORM-

A production-grade autonomous cryptocurrency trading platform, with **Stage 1 (FOUNDATION) complete**: the owner approved the Stage 1 plan and authorized its implementation on 2026-10-05. The code foundation was built in the plan's checkpoints A to D, each verified and committed, the stage's exit reports were made and its completion certificate written, and on 2026-11-10 the owner approved proceeding to the planning of Stage 2 (DATA FOUNDATION), and on 2026-11-17 its plan, with changes, which authorizes Stage 2's implementation, checkpoint by checkpoint (DEC-073); Stage 2's checkpoint A is built and verified: the environment's readiness, Stage 2's dependencies, and the venues' verification, SYS-02's market-data contracts and Stage 2's settings, and the measurement framework; and so is the first increment of its checkpoint B: the validation, freshness, quality, and quarantine of market data, and the detection of clock drift. The platform has no trading capability, and no stage after Stage 2 is authorized.

For where the project currently stands, start with [`docs/project-state.md`](docs/project-state.md).

| Document | Purpose |
|---|---|
| [`docs/project-state.md`](docs/project-state.md) | Current stage, blockers, recent decisions, next approved step |
| [`docs/README.md`](docs/README.md) | Documentation index: every specification, register, and record |
| [`docs/development.md`](docs/development.md) | Developer guide: install, check, and test the platform from a clean clone |
| [`docs/builder/claude-code-builder-constitution.md`](docs/builder/claude-code-builder-constitution.md) | Rules governing how Claude Code builds and maintains this repository; four other builder texts are in the same directory, and the sixth, owner decisions 9, is kept under `docs/handoffs/` where it was preserved; `CLAUDE.md` loads all six |
| [`CLAUDE.md`](CLAUDE.md) | Session instructions loaded automatically by Claude Code |
| [`tools/docs/`](tools/docs/README.md) | Documentation generator and checker, and the generator of the verification matrix; run `python3 tools/docs/build_index.py` after changing any document, requirement marker, or test function |
