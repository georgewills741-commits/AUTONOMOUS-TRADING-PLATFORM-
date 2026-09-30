# GPT → CLAUDE CODE MASTER PROJECT HANDOFF

> **Status:** HISTORICAL — source input, received 2026-09-30. This is **not** an active source of truth.
>
> The content below has been analysed, classified, and reconciled with Part 1 and the owner's earlier decisions. Where each section went: [`docs/traceability/part-2-reconciliation.md`](../traceability/part-2-reconciliation.md).
>
> **Formatting note:** converted from plain text to Markdown (headings, lists, text blocks, paragraph breaks). No wording was added, removed, or changed. The owner sent it with the covering line "this is the hand off part 2", which is not reproduced below. Section numbers (§1–§350) are the handoff's own; the documentation cites them as `P2§N` to keep them apart from Part 1's `§NN`.
>
> **Received as-is:** the table in §339 arrived with its cell boundaries lost (for example "Market dataAuthoritativeInterpret"). It is kept exactly as received here. The row-by-row reading is ARCH-022 in the [architecture overview](../architecture/overview.md).

PART 2 — COMPLETE CONSOLIDATED ADDITIONAL SYSTEMS, DETERMINISTIC/AI SEPARATION, PAPER OPERATION, READINESS, ARBITRAGE, DEPLOYMENT PORTABILITY & PREVIOUSLY DISCUSSED REQUIREMENTS

Status: Master project knowledge handoff — documentation/reconciliation phase only

Builder: Claude Code

Project Architect / Specification Author: GPT

Project: Production-grade autonomous cryptocurrency trading platform

Relationship: Continuation of Part 1 and all previously discussed project requirements

## IMPORTANT MASTER INSTRUCTION

This Part 2 must not be treated as an isolated specification.

Claude must combine:

```text
PART 1
+
ALL PREVIOUSLY DISCUSSED PROJECT REQUIREMENTS
+
THIS COMPLETE PART 2
```

into one coherent project knowledge system.

The purpose of this document is not to tell Claude to immediately start coding.

The first responsibility is:

```text
RECONCILE → ORGANIZE → CLASSIFY → DEDUPLICATE → RESOLVE CONFLICTS → ASSIGN OWNERSHIP → DOCUMENT → BUILD DEPENDENCY GRAPH → BUILD ROADMAP → DEFINE VERIFICATION → STOP FOR HUMAN APPROVAL
```

Only after approval should normal implementation begin.

## 1 — CORE PROJECT IDENTITY

The project is not merely an "AI crypto trading bot."

It is a:

Deterministic-first autonomous financial software platform with an AI intelligence layer.

The platform is intended to combine:

- Whole-market monitoring
- Real-time market-data infrastructure
- Quantitative computation
- Market-regime detection
- Opportunity detection
- Strategy management
- Risk management
- Capital management
- Portfolio management
- Execution
- Cross-exchange arbitrage
- Triangular arbitrage
- Paper/demo trading
- Live trading
- AI research
- AI market interpretation
- AI-assisted strategy discovery
- Natural-language policy
- Controlled autonomous decision-making
- Controlled strategy improvement
- Performance analysis
- Reconciliation
- Auditability
- Security
- Monitoring
- Incident management
- Recovery
- Backup/restore
- Deployment portability
- Local hosting
- Server/cloud hosting
- Migration
- Failover/standby where approved
- Production change control

The foundational principle remains:

AI provides intelligence. Deterministic infrastructure provides authority.

And:

If the system does not know enough to act safely, it must be able to choose NO TRADE, WAIT, SAFE MODE, or another explicitly defined safe state.

## 2 — DETERMINISTIC CORE VS AI INTELLIGENCE

The distinction between the deterministic trading infrastructure and AI intelligence is a foundational architectural principle.

It must remain explicit throughout the repository.

### DETERMINISTIC TRADING CORE

The deterministic core owns functions where correctness, repeatability, financial accuracy, timing, enforcement and safety are critical.

This includes, where applicable:

- Market-data ingestion
- WebSocket management
- Market-data normalization
- Data validation
- Data-quality scoring
- Data quarantine
- Data lineage
- Timestamp validation
- Time synchronization
- Market-data storage
- Quantitative calculations
- Indicators
- Feature calculations
- Regime classification
- Opportunity calculations
- True net profitability
- Fee calculations
- Slippage calculations
- Liquidity calculations
- Market-impact calculations
- Funding calculations
- Position sizing
- Exposure calculations
- Capital availability
- Capital reservation
- Portfolio state
- Order validation
- Order execution
- Exchange communication
- Order reconciliation
- Position reconciliation
- Balance reconciliation
- Risk limits
- Capital limits
- Kill switches
- Safe modes
- No-new-position mode
- Policy enforcement
- Audit logging
- Persistent financial state
- Backtesting
- Paper trading
- Deterministic monitoring
- Recovery
- Reconciliation
- Failure handling

### AI INTELLIGENCE LAYER

The AI layer provides intelligence where interpretation, research, reasoning, synthesis or hypothesis generation is useful.

It includes, where applicable:

- Market interpretation
- Research
- Strategy discovery
- Hypothesis generation
- Strategy analysis
- News analysis
- Sentiment/context analysis
- Complex event interpretation
- Failure analysis
- Strategy improvement proposals
- Research prioritization
- Model evaluation
- Opportunity interpretation
- Portfolio contextual reasoning
- Devil's Advocate analysis
- Trading proposals

AI must not replace deterministic authorities.

## 3 — AI MUST NEVER BECOME THE FINANCIAL SOURCE OF TRUTH

AI must never become authoritative for:

- Account balance
- Available capital
- Reserved capital
- Position size
- Position state
- Order state
- Fill state
- Fees
- Slippage
- P&L
- Exposure
- Risk limits
- Capital reservations
- Net profitability
- Ledger balances
- Reconciliation state
- Policy enforcement
- Kill-switch state

AI may interpret these values.

It may propose actions based on them.

It cannot redefine them.

## 4 — DETERMINISTIC OPERATION WITHOUT AI

The core platform should remain capable of performing functions that do not genuinely require intelligence.

Normal path:

```text
MARKET DATA ↓ VALIDATION ↓ NORMALIZATION ↓ QUANT ↓ REGIME ↓ OPPORTUNITY ↓ NET ECONOMICS ↓ RISK ↓ CAPITAL ↓ EXECUTION 
```

Not:

```text
MARKET TICK ↓ LLM ↓ CALCULATE SPREAD ↓ LLM ↓ CALCULATE FEES ↓ LLM ↓ TRADE 
```

AI is introduced only when interpretation or reasoning is genuinely useful.

## 5 — AI PROPOSAL / DETERMINISTIC AUTHORITY MODEL

The fundamental interaction is:

```text
AI ↓ PROPOSAL ↓ STRUCTURED OUTPUT ↓ SCHEMA VALIDATION ↓ POLICY VALIDATION ↓ RISK VALIDATION ↓ CAPITAL VALIDATION ↓ EXECUTION VALIDATION ↓ DETERMINISTIC DECISION 
```

AI cannot skip deterministic validation.

## 6 — ORIGINAL AI AGENT ORGANIZATION

Previously discussed AI roles include:

### Market Analyst

Responsible for:

- Market interpretation
- Contextual analysis
- Market-event analysis

### Quant Research Agent

Responsible for:

- Quantitative research
- Hypothesis analysis
- Statistical interpretation

### Strategy Research Agent

Responsible for:

- Strategy discovery
- Strategy analysis
- Candidate generation

### Trading Director

Responsible for:

- Synthesizing validated information
- Coordinating analysis
- Producing structured trade proposals

### Devil's Advocate

Responsible for:

- Challenging assumptions
- Identifying weaknesses
- Attempting to disprove proposed decisions

### Performance Analyst

Responsible for:

- Performance analysis
- Expected-vs-actual analysis
- Strategy-health analysis

### Strategy Optimizer

Responsible for:

- Proposing controlled strategy improvements

### Model Evaluation Agent

Responsible for:

- Evaluating model performance
- Comparing task-specific model behavior

### AI Cost Manager

Responsible for:

- AI resource consumption
- Cost/value analysis
- AI usage optimization

Additional agents must only be introduced after responsibility boundaries are documented.

Claude must avoid creating multiple agents with substantially overlapping ownership.

## 7 — TRADING DIRECTOR AUTHORITY BOUNDARY

The Trading Director may:

- Interpret validated information
- Consider strategy context
- Consider market context
- Produce structured trade proposals
- Explain reasoning
- Request additional analysis
- Coordinate specialized agents

It must not:

- Submit unrestricted orders
- Override risk
- Override capital authority
- Override user hard policy
- Modify financial records
- Change production strategy outside the approved improvement process
- Bypass deterministic execution validation

## 8 — HALLUCINATION FIREWALL

Material AI claims should be evidence-backed.

Where applicable, outputs should reference:

- Data source
- Timestamp
- Market
- Venue
- Dataset/version
- Calculation
- Evidence identifier
- Relevant event

The system must distinguish:

```text
OBSERVED FACT 
```

from:

```text
AI INTERPRETATION 
```

from:

```text
AI HYPOTHESIS 
```

from:

```text
DECISION PROPOSAL 
```

These must never be represented as equivalent.

## 9 — EVIDENCE-BACKED AI

For material claims:

```text
CLAIM ↓ EVIDENCE ↓ SOURCE ↓ TIMESTAMP ↓ VALIDATION 
```

If evidence cannot be established where evidence is required:

- Mark the claim unsupported
- Reject it where necessary
- Request more evidence
- Enter WAIT / NO TRADE where appropriate

## 10 — MULTI-AGENT VALIDATION

Important decisions may use multiple analytical agents.

Example:

```text
TRADING DIRECTOR ↓ PROPOSAL ├── MARKET ANALYST ├── QUANT RESEARCH ├── DEVIL'S ADVOCATE └── PERFORMANCE / RISK ANALYSIS ↓ STRUCTURED RESULT ↓ DETERMINISTIC VALIDATION 
```

AI agreement cannot override deterministic safety.

## 11 — AI DISAGREEMENT

Disagreement must be a supported state.

```text
AI DISAGREEMENT ↓ UNCERTAINTY INCREASES ↓ ADDITIONAL VALIDATION OR WAIT / NO TRADE 
```

Artificial consensus must not be manufactured merely to generate a trade.

## 12 — AI RESOURCE & DECISION GOVERNOR

The previously established AI Resource & Decision Governor remains part of the architecture.

It should control, where applicable:

- Whether AI is required
- AI call frequency
- AI budgets
- Model selection
- Agent activation
- Context size
- Scheduling
- Caching
- Failover
- Degradation
- Cost limits
- Task prioritization
- Financial-consequence-aware escalation

The system must avoid unnecessary AI consumption.

## 13 — MODEL ROUTER

The Model Router selects models according to:

- Task
- Complexity
- Quality requirement
- Cost
- Latency
- Reliability
- Context requirements
- Availability
- Financial consequence
- Current model health
- Historical performance

The architecture must support multiple providers/models.

It must not hard-code one model throughout the system.

## 14 — TASK-SPECIFIC MODEL SELECTION

Conceptually:

```text
TASK ↓ CLASSIFICATION ↓ QUALITY REQUIREMENT ↓ RISK / CONSEQUENCE ↓ AVAILABLE MODELS ↓ QUALITY / COST / LATENCY / RELIABILITY ↓ MODEL SELECTION 
```

The routing decision must be deterministic and auditable.

## 15 — AI MODEL EVALUATION

Models should be evaluated using measured performance.

Possible metrics:

- Accuracy
- Validation success
- Hallucination rate
- Cost
- Latency
- Structured-output compliance
- Useful contribution
- Failure rate
- Task-specific performance
- Reliability
- Evidence compliance

Historical results should be retained.

## 16 — AI CACHING

AI results should be cached where appropriate.

Caching must account for:

- Context
- Market state
- Timestamp
- Data version
- Model version
- Prompt/version
- Validity period
- Financial consequence

Stale AI output must not be treated as current truth.

## 17 — AI FAILOVER

If an AI provider becomes unavailable:

```text
AI FAILURE ↓ IS AI REQUIRED? ├── NO → DETERMINISTIC OPERATION └── YES ↓ FALLBACK MODEL OR WAIT OR NO TRADE 
```

The failure of an AI provider must not automatically cause uncontrolled system failure.

## 18 — AI DEGRADATION

The system should define graceful degradation states.

Examples:

- Full AI operation
- Reduced AI
- Fallback model
- Deterministic-only operation
- Research-only AI
- No-trade where AI is mandatory

## 19 — STRATEGY FACTORY

The Strategy Factory provides a controlled strategy-development pipeline:

```text
RESEARCH ↓ HYPOTHESIS ↓ STRATEGY DEFINITION ↓ BACKTEST ↓ VALIDATION ↓ OUT-OF-SAMPLE ↓ WALK-FORWARD ↓ ROBUSTNESS ↓ PAPER ↓ APPROVAL ↓ CANARY ↓ PRODUCTION 
```

No AI-generated strategy may jump directly into unrestricted live production.

## 20 — STRATEGY REGISTRY

Every strategy should have a canonical identity.

At minimum:

- Strategy ID
- Version
- Description
- Objective
- Applicable markets
- Applicable regimes
- Risk profile
- Parameters
- Dependencies
- Validation history
- Status
- Creation timestamp
- Approval status
- Retirement status

Lifecycle may include:

```text
DRAFT RESEARCH BACKTESTED VALIDATING PAPER APPROVED CANARY PRODUCTION SUSPENDED RETIRED 
```

## 21 — STRATEGY VERSION IMMUTABILITY

Once used for important production decisions, a strategy version must remain reconstructable.

Parameter changes must create a new version.

Historical versions must not be silently rewritten.

## 22 — MARKET REGIME ENGINE

The Regime Engine is deterministic.

Potential states:

- TRENDING
- RANGING
- HIGH_VOLATILITY
- LOW_VOLATILITY
- PANIC
- ABNORMAL
- UNKNOWN

The taxonomy may evolve.

UNKNOWN must remain a valid state.

## 23 — UNKNOWN REGIME

If a strategy requires a known regime and the regime is:

```text
UNKNOWN 
```

the system must not infer a regime.

Possible responses:

- No trade
- Wait
- Reduced exposure
- Additional validation

## 24 — WHOLE-MARKET SCANNING

The platform should be designed to evaluate the relevant market universe rather than only a manually selected small set.

Whole-market scanning must remain bounded by:

- Data quality
- Liquidity
- Venue availability
- Resource constraints
- Risk policy
- Market eligibility

The exact universe-selection architecture must be documented.

## 25 — OPPORTUNITY FILTER

The Opportunity Filter prevents expensive processing for insignificant events.

```text
MARKET EVENTS ↓ FAST DETERMINISTIC FILTER ↓ SIGNIFICANT? ├── NO → CONTINUE └── YES → DEEPER PROCESSING 
```

## 26 — NO AI ON EVERY TICK

This is a foundational requirement.

The system must not accidentally implement:

```text
EVERY MARKET TICK ↓ AI CALL 
```

Normal market processing must remain deterministic.

## 27 — OPPORTUNITY DATABASE

Important opportunities should be retained.

Records may include:

- Opportunity ID
- Timestamp
- Market
- Venue
- Strategy
- Expected economics
- True net economics
- Required capital
- Liquidity
- Risk
- Decision
- Rejection reason
- Execution result
- Expected result
- Actual result
- Missed-opportunity status
- Data/evidence references
- Strategy version
- Policy version

Both executed and rejected opportunities must be preserved.

## 28 — REJECTED OPPORTUNITIES ARE DATA

Rejected opportunities are necessary for analyzing:

- Correct rejection
- Over-rejection
- Under-rejection
- Capital constraints
- Risk constraints
- Data problems
- Latency
- Liquidity
- Policy restrictions
- Execution constraints

## 29 — TRUE NET PROFITABILITY

Opportunity evaluation must use:

- TRUE EXECUTABLE NET ECONOMICS

not:

- Headline spread
- Gross percentage
- AI prediction
- Fixed return assumption

The calculation should account for relevant:

- Fees
- Slippage
- Funding
- Market impact
- Liquidity
- Precision
- Execution costs
- Capital constraints
- Rebalancing costs where applicable
- Other relevant costs

## 30 — FEE ENGINE

Fees must be calculated deterministically.

The Fee Engine should account for applicable:

- Venue
- Instrument
- Maker/taker status
- Fee schedule
- Trading tier
- Funding
- Transfer costs where relevant

AI may interpret fee implications but cannot become the authoritative fee calculator.

## 31 — SLIPPAGE ENGINE

The Slippage Engine should model expected execution effects.

Where data permits, consider:

- Order-book depth
- Order size
- Liquidity
- Volatility
- Spread
- Execution type
- Market impact
- Historical execution behavior

## 32 — LIQUIDITY PROTECTION

A theoretical opportunity may be rejected if actual liquidity cannot support execution.

Liquidity evaluation should be deterministic wherever possible.

## 33 — FUNDING COSTS

For instruments involving funding, expected funding costs must be incorporated into opportunity economics.

Funding must not be ignored merely because the headline price spread is attractive.

## 34 — NO GUARANTEED RETURNS

The architecture must never encode:

- 1% per trade
- 1% every day
- 5% every day
- Any other guaranteed-return assumption

Previously discussed percentages are:

- Analytical thresholds
- Targets
- Opportunity categories

They are not guarantees.

## 35 — OPPORTUNITY ACCUMULATION

The system should be able to accumulate many individually valid opportunities rather than requiring a fixed return per trade.

The architecture should optimize for:

- Quality
- Executability
- Risk-adjusted economics
- Capital efficiency

not artificial trade-count targets.

## 36 — COMPOUNDING

Realized gains may become available for future trading if authorized.

The system must distinguish:

```text
REALIZED P&L AVAILABLE CAPITAL AUTHORIZED TRADING CAPITAL RESERVED CAPITAL 
```

Compounding is a capital-management consequence, not a guaranteed strategy outcome.

## 37 — CAPITAL AUTHORITY

There must be one canonical Capital Authority.

It should control/coordinate:

- Available capital
- Reserved capital
- Allocation
- Limits
- Strategy reservations
- Venue allocations
- Capital release
- Reconciliation
- Emergency reserve

No competing Capital Authority should exist.

## 38 — ATOMIC CAPITAL RESERVATION

Capital reservation must be safe under concurrency.

Two strategies must not simultaneously reserve the same capital.

Reservation should be atomic or otherwise protected against race conditions.

## 39 — GLOBAL RISK AUTHORITY

There must be one canonical Risk Authority.

Specialized risk modules may exist, but they must integrate into the global risk authority rather than competing with it.

## 40 — LOSS-STREAK PROTECTION

The system should support configurable protection against repeated losses.

Possible responses:

- Reduce exposure
- Pause strategy
- Require review
- Enter cooldown
- Suspend strategy

Exact thresholds must be policy/configuration driven.

## 41 — EXCESSIVE-TRADING PROTECTION

The platform should detect abnormal trade frequency.

Possible triggers:

- Excessive order rate
- Repeated failed opportunities
- Strategy loop
- Execution churn
- Unexpected activity

Responses may include:

- Throttle
- Pause
- Review
- Kill switch

## 42 — STRATEGY DRIFT

The platform should monitor whether production behavior is diverging from validated strategy behavior.

Possible dimensions:

- Win/loss distribution
- Execution quality
- Slippage
- Opportunity frequency
- Regime distribution
- Latency
- P&L distribution
- Risk behavior

Significant drift should trigger review or controlled suspension.

## 43 — PORTFOLIO AUTHORITY

Portfolio state must have one authoritative owner.

It should track:

- Positions
- Exposure
- Realized P&L
- Unrealized P&L
- Venue positions
- Strategy attribution
- Relevant balances

## 44 — EXCHANGE ADAPTER SYSTEM

Target venues previously discussed include:

- Binance
- OKX
- Coinbase

Other venues may be added through the same abstraction.

Architecture:

```text
TRADING ENGINE ↓ EXCHANGE ABSTRACTION ↓ VENUE ADAPTER ↓ EXCHANGE 
```

Exchange-specific behavior must not be scattered throughout the trading engine.

## 45 — EXCHANGE ADAPTER RESPONSIBILITIES

Adapters may handle:

- Authentication
- Market-data subscriptions
- Symbol mapping
- Precision
- Fee metadata
- Order submission
- Cancellation
- Order querying
- Balance retrieval
- Position retrieval
- Exchange-specific errors
- Rate limits
- WebSocket state
- Connection management

Shared trading logic remains outside adapters where possible.

## 46 — EXCHANGE NORMALIZATION

Exchanges differ in:

- Symbols
- Orders
- Fills
- Fees
- Positions
- Timestamps
- Precision
- Errors
- Rate limits

The adapter layer must normalize these into canonical platform objects.

## 47 — RATE-LIMIT MANAGEMENT

Rate limits must be treated as deterministic infrastructure.

The system should understand:

- Per-endpoint limits
- Venue limits
- Backoff
- Retry policy
- Priority
- WebSocket limits
- REST limits

Retries must not create duplicate financial actions.

## 48 — CONNECTION MANAGEMENT

Connections should be resilient.

The platform should support:

- Connection health
- Reconnect
- Heartbeats
- Stale-feed detection
- Backoff
- Circuit breaking
- Venue degradation states

## 49 — DATA QUALITY

Market data must be validated before being treated as authoritative.

Checks may include:

- Timestamp validity
- Sequence continuity
- Duplicates
- Out-of-order events
- Impossible prices
- Missing data
- Stale data
- Cross-source inconsistencies

Invalid data may enter:

- DATA QUARANTINE

rather than contaminating the trading path.

## 50 — DATA LINEAGE

Important calculations and decisions should be traceable to:

- Source
- Timestamp
- Dataset
- Data version
- Processing version
- Feature version
- Strategy version
- Policy version

## 51 — TIME SYNCHRONIZATION

Time is critical to:

- Market data
- Orders
- Fills
- Funding
- Arbitrage
- Latency
- Reconciliation
- Backtesting

The system should detect meaningful clock drift.

## 52 — BACKTESTING INTEGRITY

Backtests must prevent:

- Look-ahead bias
- Data leakage
- Survivorship bias
- Future information leakage
- Incorrect fee assumptions
- Unrealistic execution
- Unrealistic liquidity
- Unrealistic slippage

## 53 — DATASET SEPARATION

Where applicable:

```text
TRAINING ↓ VALIDATION ↓ OUT-OF-SAMPLE ↓ PAPER ↓ PRODUCTION 
```

Data boundaries must prevent leakage.

## 54 — ANTI-OVERFITTING

Strategy validation should consider:

- Out-of-sample performance
- Walk-forward testing
- Parameter sensitivity
- Stress testing
- Market-regime diversity
- Monte Carlo/distribution analysis
- Robustness testing

A strategy must not be approved merely because one historical backtest looks profitable.

## 55 — WALK-FORWARD TESTING

Where applicable:

```text
TRAIN ↓ TEST ↓ ROLL FORWARD ↓ RETRAIN / REVALIDATE ↓ TEST 
```

The exact methodology must be documented.

## 56 — STRESS TESTING

Strategies should be exposed to adverse conditions including, where relevant:

- Volatility spikes
- Spread widening
- Liquidity deterioration
- Execution delays
- Exchange outages
- Slippage increases
- Partial fills
- Data interruptions

## 57 — MONTE CARLO / DISTRIBUTION ANALYSIS

Where appropriate, performance analysis should examine distributions rather than relying solely on average return.

Potential outputs:

- Drawdown distribution
- Losing streaks
- Return distribution
- Tail behavior
- Execution variance
- Risk-of-ruin-related measures

The exact methodology requires architectural specification.

## 58 — PAPER TRADING IS A REAL OPERATING MODE

Paper/demo trading must not be treated as merely a toy simulator.

The platform should support continuous real-time paper operation.

Conceptually:

```text
LIVE MARKET DATA ↓ DETERMINISTIC PROCESSING ↓ STRATEGIES ↓ RISK ↓ PAPER CAPITAL ↓ PAPER EXECUTION ↓ PAPER POSITIONS ↓ PAPER P&L ↓ PERFORMANCE ↓ READINESS ANALYSIS 
```

## 59 — CONTINUOUS PAPER OPERATION

The paper system should be capable of operating continuously against real market data.

It should accumulate evidence over time.

The system should record:

- Opportunities
- Decisions
- Simulated orders
- Simulated fills
- Slippage assumptions
- Fees
- P&L
- Drawdown
- Exposure
- Risk events
- Rejected trades
- Missed opportunities
- Strategy behavior
- Model behavior
- Incidents

## 60 — PAPER/LIVE ARCHITECTURAL PARITY

Paper trading should use the same logical architecture as live trading where practical.

```text
STRATEGY ↓ RISK ↓ CAPITAL ↓ EXECUTION INTERFACE ├── PAPER EXECUTOR └── LIVE EXECUTOR 
```

The difference should primarily be the execution environment.

## 61 — SIMULATED CAPITAL

Paper mode must have explicit simulated capital.

The system should track:

- Starting capital
- Current simulated capital
- Reserved capital
- Available capital
- P&L
- Fees
- Exposure
- Drawdown

Simulated capital must not be confused with real exchange capital.

## 62 — PAPER EXECUTION MODEL

The paper executor should model relevant execution conditions rather than assuming:

```text
SIGNAL ↓ PERFECT FILL 
```

Where possible, simulate:

- Spread
- Slippage
- Liquidity
- Partial fills
- Latency
- Fees
- Order types
- Rejections
- Market movement

## 63 — PAPER EXPECTED-VS-OBSERVED ANALYSIS

The platform should compare:

```text
EXPECTED vs OBSERVED 
```

Examples:

- Expected fill price vs observed simulated fill
- Expected slippage vs observed
- Expected profitability vs realized paper profitability
- Expected opportunity frequency vs observed
- Expected execution latency vs observed
- Expected strategy behavior vs observed

## 64 — PAPER EVIDENCE ACCUMULATION

Paper mode should accumulate evidence rather than producing only a single score.

Evidence should be versioned by:

- Strategy
- Strategy version
- Policy
- Policy version
- Model
- Model version
- Market
- Regime
- Time period

## 65 — PAPER READINESS SYSTEM

The platform should have a canonical readiness system for determining whether a strategy/system is ready to progress.

Readiness must not be a single arbitrary profitability number.

It should consider:

- Data quality
- Strategy stability
- Out-of-sample behavior
- Risk behavior
- Drawdown
- Execution quality
- Slippage
- Liquidity
- Reliability
- Error rates
- Operational incidents
- Policy compliance
- Reconciliation health
- Paper evidence
- Model behavior where applicable
- Monitoring health
- Recovery capability

## 66 — READINESS MUST BE EXPLICIT

Possible readiness states:

```text
NOT_READY RESEARCH VALIDATING PAPER_REQUIRED PAPER_ACTIVE READINESS_REVIEW READY_FOR_CANARY CANARY_ACTIVE PRODUCTION_APPROVED PRODUCTION_ACTIVE SUSPENDED REJECTED 
```

Exact states may be refined during architecture.

## 67 — READINESS MUST BE CANONICAL

There must not be several independent systems each claiming whether a strategy is "ready."

One authoritative Readiness System should aggregate evidence from:

- Validation
- Risk
- Performance
- Execution
- Data quality
- Reliability
- Incidents
- Policy
- Paper trading

## 68 — PAPER → READINESS → CANARY → PRODUCTION

The canonical progression should be:

```text
RESEARCH ↓ BACKTEST ↓ VALIDATION ↓ OUT-OF-SAMPLE ↓ WALK-FORWARD ↓ STRESS ↓ PAPER ↓ READINESS REVIEW ↓ CANARY ↓ PRODUCTION 
```

No stage should be silently bypassed.

## 69 — DAILY SYSTEM INTELLIGENCE DASHBOARD

The platform should eventually provide a Daily System Intelligence Dashboard / Report.

Its purpose is to give the user a high-level operational understanding of the system.

It should summarize, where applicable:

- Market conditions
- Opportunities
- Executions
- Capital
- Risk
- Strategy health
- AI activity
- Incidents
- Reconciliation
- Paper readiness
- Production readiness
- Unknown states
- Important changes

## 70 — DAILY SYSTEM INTELLIGENCE REPORT

A report may include:

### Market Summary

- Market regime
- Volatility
- Major events
- Data-quality state

### Opportunity Summary

- Opportunities detected
- Opportunities accepted
- Opportunities rejected
- Missed opportunities
- False opportunities
- Net economics

### Execution Summary

- Orders
- Fills
- Partial fills
- Slippage
- Latency
- Rejections

### Capital Summary

- Available capital
- Reserved capital
- Utilization
- Strategy allocation
- Venue allocation

### Risk Summary

- Risk events
- Exposure
- Drawdown
- Loss streak
- Risk-limit events

### AI Summary

- AI calls
- Models used
- Cost
- Failures
- Fallbacks
- Unsupported claims
- AI contribution

### Strategy Health

- Performance
- Drift
- Regime behavior
- Degradation
- Suspensions

### Incidents

- Exchange issues
- Data issues
- Execution issues
- System issues
- Security issues

### Readiness

- Current readiness
- Evidence accumulated
- Missing evidence
- Blocking conditions

## 71 — HISTORICAL DASHBOARD

Daily reports should be retained where appropriate.

The user should be able to compare:

```text
TODAY vs YESTERDAY vs LAST WEEK vs HISTORICAL BASELINE 
```

This supports operational trend analysis.

## 72 — UNKNOWN REPORTING

The dashboard should explicitly report unknown/uncertain states.

Examples:

- Unknown market regime
- Unknown order state
- Unknown exchange state
- Unknown reconciliation state
- Unknown data quality
- Unknown AI evidence

Unknown must not be silently represented as normal.

## 73 — PERFORMANCE ANALYSIS

The Performance Analyst should analyze:

- Expected vs actual
- Strategy performance
- Execution performance
- Opportunity quality
- Rejection quality
- Missed opportunities
- False opportunities
- Slippage
- Fees
- Drawdown
- Latency
- Regime-specific behavior

## 74 — EXPECTED-VS-ACTUAL ANALYSIS

The platform should retain expected values before execution where possible.

Then compare:

```text
EXPECTED ↓ ACTUAL ↓ VARIANCE ↓ CAUSE 
```

Potential causes:

- Slippage
- Latency
- Liquidity
- Fee changes
- Market movement
- Strategy assumptions
- Data quality
- Execution failure

## 75 — MISSED-OPPORTUNITY ANALYSIS

The platform should preserve opportunities that were not executed when measurable.

Reasons may include:

- Risk rejection
- Capital unavailable
- Policy restriction
- Insufficient net profit
- Liquidity
- Latency
- Exchange degradation
- AI uncertainty
- Execution uncertainty

Later analysis may determine whether the rejection was appropriate.

## 76 — FALSE-OPPORTUNITY ANALYSIS

The system should analyze opportunities that appeared attractive but failed to produce expected economics.

This helps detect:

- Poor models
- Bad assumptions
- Data problems
- Slippage underestimation
- Liquidity errors
- Strategy degradation

## 77 — INCIDENT MANAGEMENT

Production operations require structured incident management.

Incidents should record:

- Incident ID
- Time
- Environment
- System
- Severity
- Detection method
- Symptoms
- Root cause
- Impact
- Actions
- Recovery
- Follow-up
- Related changes

## 78 — KILL SWITCHES

Kill switches must be deterministic.

Potential levels:

- Global trading
- Strategy
- Venue
- Arbitrage
- New positions
- Specific execution path

## 79 — NO-NEW-POSITION MODE

The platform should support:

```text
NO NEW POSITIONS 
```

while still allowing controlled management of existing positions where policy permits.

This is distinct from a full shutdown.

## 80 — SAFE MODE

Safe Mode must be a first-class state.

Possible triggers:

- Critical state uncertainty
- Reconciliation failure
- Risk engine failure
- Capital integrity issue
- Security incident
- Exchange state uncertainty
- Data corruption
- Migration failure

## 81 — NO-TRADE IS A SUCCESSFUL DECISION

Examples:

- Opportunity insufficient
- Risk too high
- Data stale
- Unknown regime
- Capital unavailable
- Exchange degraded
- AI unavailable when required
- Policy restriction
- Execution uncertain

"No trade" is not inherently a failure.

## 82 — WAIT IS A FIRST-CLASS STATE

WAIT means the system needs more information.

It should not be forced to generate a trade merely because the opportunity engine was activated.

## 83 — RECOVERY AFTER CRASH

After restart:

```text
PERSISTENT STATE ↓ EXTERNAL STATE ↓ RECONCILIATION ↓ RECOVERY STATE ↓ RESUME DECISION 
```

The system must not assume in-memory state is correct.

## 84 — ORDER TIMEOUT

A timeout does not mean an order failed.

Correct:

```text
ORDER REQUEST ↓ TIMEOUT ↓ QUERY EXCHANGE ↓ DETERMINE ACTUAL STATE 
```

Never automatically submit a duplicate order because of an unverified timeout.

## 85 — TRANSFER TIMEOUT

Likewise:

```text
TRANSFER ↓ TIMEOUT ↓ VERIFY BLOCKCHAIN / VENUE ↓ DETERMINE STATE 
```

## 86 — RESTART SAFETY

Before active execution resumes, verify:

- Open orders
- Positions
- Balances
- Capital reservations
- Pending transfers
- Strategy states
- Exchange connectivity
- Policy version
- System mode
- Risk state

## 87 — CROSS-EXCHANGE ARBITRAGE

Cross-exchange arbitrage must calculate:

```text
EXCHANGE A PRICE + EXCHANGE B PRICE + FEES + SLIPPAGE + LIQUIDITY + CAPITAL + REBALANCING ECONOMICS ↓ TRUE NET RESULT 
```

Raw price differences are not guaranteed profit.

## 88 — TRIANGULAR ARBITRAGE

The platform should dynamically discover routes such as:

```text
ASSET A ↓ ASSET B ↓ ASSET C ↓ ASSET A 
```

It must calculate:

- Prices
- Fees
- Precision
- Liquidity
- Slippage
- Capital requirement
- Execution sequence
- True net result

## 89 — TRIANGULAR EXECUTION RISK

The system must account for:

- Leg failure
- Partial fills
- Price movement
- Liquidity deterioration
- Exchange rejection
- Precision constraints
- Rate limits
- Timing
- Residual assets

A mathematically profitable route may still be operationally invalid.

## 90 — CROSS-EXCHANGE CAPITAL PRE-POSITIONING

Arbitrage may use pre-positioned capital:

```text
Exchange A: USDT + BTC Exchange B: USDT + BTC Exchange C: USDT + BTC 
```

This reduces dependence on immediate blockchain transfers.

## 91 — INTELLIGENT REBALANCING

Inventory imbalance must not automatically trigger transfers.

The Rebalancing Engine should consider:

- Transfer cost
- Transfer time
- Network conditions
- Future opportunity probability
- Liquidity
- Reserve requirements
- Capital utilization
- Expected opportunity value

## 92 — ARBITRAGE CAPITAL RESERVES

Capital Authority may distinguish:

- Available capital
- Reserved capital
- Arbitrage capital
- Directional capital
- Emergency reserve
- Venue-specific reserve

Exact categories require architecture approval.

## 93 — ARBITRAGE RISK ENGINE

Arbitrage-specific risks include:

- Leg failure
- Execution delay
- Liquidity collapse
- Exchange outage
- Inventory imbalance
- Transfer risk
- Venue risk
- Correlated execution failure

These should integrate with the global Risk Authority.

## 94 — ARBITRAGE KILL SWITCH

Arbitrage should be independently disableable.

Example:

```text
GLOBAL TRADING = ACTIVE ARBITRAGE = DISABLED 
```

Directional strategies may continue if permitted.

## 95 — ARBITRAGE PERFORMANCE CONTROLLER

Track:

- Expected opportunities
- Executed opportunities
- Net profitability
- Failed opportunities
- Slippage
- Execution latency
- Rebalancing costs
- Inventory efficiency
- Expected vs actual

Deterioration may trigger:

- Throttling
- Suspension
- Review
- Recalibration

not uncontrolled live strategy rewriting.

## 96 — ARBITRAGE QUALITY TIERS

Previously discussed analytical categories:

- Tier 1: approximately ≥1% true net
- Tier 2: approximately 0.5–1%
- Tier 3: approximately 0.2–0.5%
- Tier 4: below approximately 0.2%

These are analytical categories only, not unconditional execution rules.

## 97 — PAPER ARBITRAGE

Arbitrage must also be testable in paper mode.

The simulator should account for:

- Multi-leg execution
- Liquidity
- Slippage
- Fees
- Partial fills
- Timing
- Venue failure
- Inventory
- Rebalancing

## 98 — ARBITRAGE EXPECTED-VS-ACTUAL

The arbitrage subsystem should compare:

```text
THEORETICAL vs EXPECTED EXECUTABLE vs PAPER OBSERVED vs LIVE OBSERVED 
```

This helps detect unrealistic arbitrage assumptions.

## 99 — PORTFOLIO / STRATEGY ATTRIBUTION

P&L should be attributable where possible to:

- Strategy
- Venue
- Market
- Asset
- Trade
- Opportunity
- Arbitrage route

This supports performance analysis.

## 100 — POLICY SYSTEM

The user should be able to specify high-level objectives and constraints.

Example:

"Protect capital, operate autonomously, avoid unnecessary risk, and only trade genuine executable opportunities."

The system should translate this into structured policies.

## 101 — USER POLICY HIERARCHY

Conceptual hierarchy:

```text
USER HARD POLICY ↓ SYSTEM SAFETY ↓ RISK ↓ CAPITAL ↓ EXECUTION ↓ STRATEGY ↓ AI 
```

No lower layer may override a higher-level hard constraint.

## 102 — POLICY COMPILER

Natural-language policy should eventually compile into machine-readable policy.

Potential fields:

- Policy ID
- Version
- Objective
- Hard constraints
- Soft preferences
- Risk limits
- Capital limits
- Allowed markets
- Restricted markets
- Allowed strategies
- Forbidden conditions
- Emergency rules
- Effective time
- Expiration
- Change history

## 103 — POLICY TRACEABILITY

Important decisions should reference the active policy version.

The system should answer:

- Which policy permitted or restricted this decision?

## 104 — POLICY IMMUTABILITY

A policy change creates a new version.

Historical decisions remain associated with the policy that governed them.

## 105 — POLICY SIMULATION

Material policy changes should be testable before activation.

The system should compare:

```text
CURRENT POLICY vs PROPOSED POLICY 
```

and identify meaningful behavioral differences.

## 106 — AUTONOMY

Autonomous operation means the system can act within authorized boundaries.

It does not mean:

- Unlimited capital
- Unlimited leverage
- Unlimited strategy changes
- Unlimited AI authority
- Unlimited withdrawals
- Unlimited deployment access

The system must never invent authorization.

## 107 — CONTROLLED SELF-IMPROVEMENT

Correct:

```text
OBSERVE ↓ ANALYZE ↓ HYPOTHESIS ↓ TEST ↓ VALIDATE ↓ PAPER ↓ APPROVE ↓ CANARY ↓ PRODUCTION 
```

Incorrect:

```text
LOSS ↓ AI CHANGES LIVE SYSTEM ↓ IMMEDIATE DEPLOYMENT 
```

## 108 — PRODUCTION UNDERSTANDABILITY

Increasing autonomy must increase observability.

Important decisions should be explainable through:

- Data
- Policy
- Strategy
- Risk
- Capital
- AI contribution
- Execution
- Reconciliation

## 109 — TOOL-FIRST AI ARCHITECTURE

AI agents should interact through controlled tools.

```text
AI AGENT ↓ TOOL REQUEST ↓ SCHEMA VALIDATION ↓ AUTHORIZATION ↓ DETERMINISTIC SERVICE ↓ RESULT 
```

AI should not receive arbitrary operating-system access to production infrastructure.

## 110 — AI PERMISSION SCOPES

Example:

Market Analyst:

- Read market information

Strategy Research:

- Read historical data

Trading Director:

- Read validated decision context
- Create proposal

Performance Analyst:

- Read execution/performance data

Strategy Optimizer:

- Create research candidate

No research agent automatically receives:

- Live order permission
- Wallet signing
- Withdrawal permission
- Production deployment permission

## 111 — PRODUCTION DEPLOYMENT AUTHORITY

Normal lifecycle:

```text
PROPOSE ↓ VALIDATE ↓ TEST ↓ APPROVE ↓ DEPLOY 
```

AI must not independently promote production changes unless explicitly authorized by the approved deployment architecture.

## 112 — SECURITY BOUNDARY

If custody functionality is ever approved:

AI must never have direct access to:

- Private keys
- Unrestricted withdrawal authority

Controlled interface:

```text
AI PROPOSAL ↓ POLICY ↓ RISK ↓ WITHDRAWAL SERVICE ↓ AUTHORIZATION ↓ SIGNING BOUNDARY 
```

## 113 — CUSTODY REMAINS A SEPARATE DOMAIN

Previously discussed platform-account/custody functionality must not accidentally become part of the core trading engine.

If formally approved, custody requires separate architecture for:

- User accounts
- Wallets
- Deposits
- Withdrawals
- Internal ledger
- Key management
- Reconciliation
- Security
- Compliance
- Disaster recovery

Until approved, custody remains an architectural option/future domain.

## 114 — INTERNAL LEDGER

If the platform manages user balances, the ledger becomes a financial authority.

It must support:

- Deposits
- Withdrawals
- Trades
- Fees
- Funding
- Adjustments
- Reservations
- Internal transfers
- Reconciliation

Application-level balance fields cannot replace the authoritative ledger.

## 115 — LEDGER RECONCILIATION

Distinguish:

```text
INTERNAL LEDGER EXCHANGE BALANCES BLOCKCHAIN BALANCES TRADING STATE 
```

They must be reconciled.

## 116 — WITHDRAWAL AUTHORITY

Trading permission does not imply withdrawal permission.

These authorities must remain separate.

## 117 — AUDIT SYSTEM

The platform should preserve decision/audit history.

Important events should include:

- Who/what initiated action
- Policy version
- Strategy version
- Model/version
- Evidence
- Validation
- Risk decision
- Capital decision
- Execution result
- Reconciliation result

## 118 — DECISION LINEAGE

Important decisions should be reconstructable:

```text
MARKET EVENT ↓ DATA ↓ FEATURES ↓ REGIME ↓ OPPORTUNITY ↓ STRATEGY ↓ AI INPUT/OUTPUT ↓ POLICY ↓ RISK ↓ CAPITAL ↓ EXECUTION ↓ RESULT 
```

## 119 — EXPERIMENT REPRODUCIBILITY

Experiments should record:

- Dataset version
- Code version
- Strategy version
- Parameters
- Model/version
- Configuration
- Random seeds where applicable
- Environment
- Results

A historical experiment should be reproducible as closely as technically possible.

## 120 — CONTRACT-FIRST DEVELOPMENT

Core interfaces should be defined before implementations where practical.

Examples:

- Market-data contract
- Order contract
- Position contract
- Risk contract
- Capital contract
- Opportunity contract
- Strategy contract
- AI tool contract
- Exchange adapter contract

## 121 — API / INTERFACE VERSIONING

Important interfaces should support versioning.

Breaking changes must be explicit.

Historical data and strategies must not silently break because an interface changed.

## 122 — CONCURRENCY

The platform must account for concurrent:

- Market events
- Opportunities
- Strategies
- Capital reservations
- Orders
- Fills
- Reconciliation
- AI requests

Financial state transitions must be atomic or otherwise concurrency-safe.

## 123 — BACKPRESSURE

The platform must prevent downstream overload.

Possible controls:

- Queues
- Rate limits
- Priorities
- Dropping non-critical work
- Degradation
- Resource budgets

Safety-critical processing must have higher priority than research.

## 124 — RESOURCE PRIORITY

Conceptual priority:

- Emergency safety
- Risk
- Capital integrity
- Execution
- Market data
- Reconciliation
- Monitoring
- Live AI
- Research
- Background analytics

Exact implementation is an architecture decision.

## 125 — RESEARCH COMPUTE ISOLATION

Heavy research workloads must not consume resources required by:

- Risk
- Execution
- Market-data processing
- Reconciliation
- Monitoring

Research workloads should be isolated or resource-limited.

## 126 — EVENT-DRIVEN ARCHITECTURE

The system should be event-driven.

Examples:

```text
MARKET UPDATE → OPPORTUNITY EVALUATION RISK STATE CHANGE → STRATEGY EVALUATION EXCHANGE DEGRADATION → VENUE ELIGIBILITY CHANGE POLICY CHANGE → POLICY RECOMPILATION STRATEGY DEGRADATION → STRATEGY REVIEW 
```

## 127 — REMOTE AI PROVIDER FAILURE

External AI failure must not destroy deterministic operation.

```text
AI FAILURE ↓ IS AI REQUIRED? ├── NO → CONTINUE └── YES → FALLBACK / WAIT / NO TRADE 
```

## 128 — HOSTING CHOICE

The platform must support:

- LOCAL

and:

- REMOTE SERVER / CLOUD

The user must not be forced into one hosting architecture.

## 129 — LOCAL HOSTING

Possible components:

- Trading services
- Database
- Monitoring
- AI gateway
- Research
- Configuration
- Strategy registry
- Local execution

Minimum and recommended resources must eventually be documented.

## 130 — SERVER HOSTING

The same logical platform should be deployable remotely.

Changing:

```text
LOCAL 
```

to:

```text
SERVER 
```

must not require rewriting trading logic.

## 131 — HOSTING ABSTRACTION

Separate:

```text
TRADING / BUSINESS LOGIC 
```

from:

```text
HOSTING ENVIRONMENT 
```

Trading components must not assume:

- "This service always runs on the user's PC."

## 132 — LOCAL ↔ SERVER PORTABILITY

Required capability:

```text
LOCAL ↓ EXPORT / BACKUP ↓ SERVER ↓ RESTORE ↓ VALIDATION ↓ RESUME 
```

and:

```text
SERVER ↓ EXPORT / BACKUP ↓ LOCAL ↓ RESTORE ↓ VALIDATION ↓ RESUME 
```

## 133 — MIGRATION IS A FIRST-CLASS CAPABILITY

Migration must not mean randomly copying:

- Source files
- Database files
- Configuration
- Secrets
- Cache

The platform should define a formal migration process.

## 134 — PORTABLE PLATFORM STATE

Potential migration package:

- Database state
- Schema version
- Strategy registry
- Strategy versions
- Policy versions
- User configuration
- Risk configuration
- Capital configuration
- Exchange configuration
- Venue metadata
- Opportunity records
- Experiment metadata
- AI configuration
- Model routing
- Feature flags
- Audit metadata
- Deployment metadata
- Recovery state

Secrets must be handled separately and securely.

## 135 — SECRETS MUST NOT BE EXPORTED UNSAFELY

Migration packages must not contain plain-text:

- API keys
- Exchange secrets
- Wallet keys
- Passwords
- Authentication tokens

## 136 — ENVIRONMENT-SPECIFIC CONFIGURATION

Distinguish:

### Portable

- Strategies
- Policies
- Risk definitions
- Model-routing rules
- Market-universe rules

### Environment-specific

- Host paths
- Network addresses
- Runtime settings
- Hardware settings
- Storage paths
- Server credentials

Migration must resolve target-environment values.

## 137 — CONFIGURATION COMPILER / ENVIRONMENT ADAPTER

Conceptually:

```text
PORTABLE PLATFORM CONFIG ↓ TARGET ENVIRONMENT ↓ ENVIRONMENT RESOLUTION ↓ VALIDATION ↓ DEPLOYABLE CONFIG 
```

## 138 — DATABASE MIGRATION

```text
SOURCE STATE ↓ SCHEMA VERSION ↓ MIGRATION PLAN ↓ SCHEMA UPDATE ↓ VALIDATION ↓ RESTORE 
```

Financial records must never be silently corrupted.

## 139 — MIGRATION PRE-FLIGHT

Before migration:

- Safely suspend new trading
- Determine positions
- Determine open orders
- Determine capital
- Determine exchange connectivity
- Verify database
- Verify backup
- Verify migration compatibility
- Verify destination
- Verify dependencies
- Verify secrets
- Verify schema compatibility

## 140 — MIGRATION STATES

Possible states:

```text
MIGRATION_PREPARING MIGRATION_FROZEN MIGRATION_IN_PROGRESS VALIDATING RECOVERY_READY RESUMING FAILED ROLLBACK 
```

## 141 — OPEN ORDERS DURING MIGRATION

Internal orders must be reconciled against exchange orders.

Copying database state does not transfer exchange state.

## 142 — OPEN POSITIONS DURING MIGRATION

Internal positions must be reconciled against venue positions.

If uncertain:

```text
NO NEW TRADE 
```

until reconciliation completes.

## 143 — CAPITAL DURING MIGRATION

Verify:

```text
MIGRATED INTERNAL STATE vs VENUE STATE vs LEDGER STATE 
```

The migrated database alone is not authoritative.

## 144 — MIGRATION VALIDATION

After restore:

```text
RESTORE ↓ SCHEMA ↓ CONFIG ↓ STRATEGIES ↓ POLICY ↓ CAPITAL ↓ POSITIONS ↓ ORDERS ↓ EXCHANGE HEALTH ↓ SYSTEM HEALTH ↓ SAFE VALIDATION ↓ RESUME AUTHORIZATION 
```

## 145 — MIGRATION ROLLBACK

If validation fails:

DO NOT RESUME NORMAL TRADING.

The platform should support:

- Deployment rollback
- Prior-state restoration
- Previous-environment recovery
- Financial-state preservation
- External-state reconciliation

## 146 — DEPLOYMENT PACKAGE

The project should define a reproducible deployment package.

The exact technology is an architecture decision.

Possible approaches include:

- Containers
- Infrastructure configuration
- Deployment manifests
- Environment templates

No implementation technology should be assumed prematurely.

## 147 — INFRASTRUCTURE AS CODE

Where approved, infrastructure should be reproducible and version controlled.

Potentially:

- Services
- Networks
- Storage
- Databases
- Monitoring
- Queues
- Environment variables
- Permissions
- Resource limits

## 148 — SINGLE DEPLOYMENT SOURCE OF TRUTH

The repository must contain the authoritative deployment definition.

Local and server environments may differ through explicit overrides.

## 149 — BACKUP VS MIGRATION

These are distinct.

### Backup

Answers:

- Can we recover state?

### Migration

Answers:

- Can we intentionally move the platform?

Both are required.

## 150 — LOCAL/SERVER MIGRATION TESTING

Eventually verify:

```text
LOCAL → SERVER SERVER → LOCAL SERVER A → SERVER B 
```

where relevant.

## 151 — MIGRATION DRY RUN

Where practical:

```text
SOURCE ↓ EXPORT ↓ PACKAGE VALIDATION ↓ SIMULATED RESTORE ↓ DEPENDENCY CHECK ↓ SCHEMA CHECK ↓ CONFIG CHECK ↓ REPORT 
```

## 152 — USER-FACING HOSTING EXPERIENCE

The eventual product should abstract unnecessary infrastructure complexity.

Normal user experience may eventually be:

```text
RUN LOCALLY 
```

or:

```text
RUN ON SERVER 
```

while the platform handles the underlying deployment workflow.

## 153 — LOGICAL IDENTITY PRESERVATION

Migration should preserve, where appropriate:

- User identity
- Policy history
- Strategy history
- Audit history
- Experiment history
- Configuration history
- Logical platform state

while updating environment-specific identifiers.

## 154 — ENVIRONMENT IDENTITY

Instances should remain distinguishable.

Possible identifiers:

- Platform ID
- Environment ID
- Deployment ID
- Version

## 155 — SPLIT-BRAIN PROTECTION

The platform must prevent both local and server instances from simultaneously executing live trades against the same account without authorization.

Possible mechanisms:

- Deployment lease
- Active-instance lock
- Coordinator
- Activation token
- Production ownership state

Exact mechanism requires architecture design.

## 156 — ACTIVE TRADING AUTHORITY

For each production account there must be a clearly identifiable active execution authority.

Other instances may be:

- Standby
- Read-only
- Development
- Paper
- Recovery

but not accidentally active.

## 157 — FAILOVER

If high availability is eventually approved:

```text
FAILOVER ↓ CHECK INSTANCE OWNERSHIP ↓ CHECK ORDERS ↓ CHECK POSITIONS ↓ CHECK CAPITAL ↓ CHECK EXCHANGE STATE ↓ RECONCILE ↓ ACTIVATE 
```

Failover must begin with reconciliation.

## 158 — STANDBY MODE

A standby instance must not automatically become active without:

- Authorization
- Lease/ownership
- State validation
- Reconciliation

## 159 — CLOUD/LOCAL RESOURCE DIFFERENCES

The system must account for different:

- CPU
- RAM
- Disk
- Network
- GPU

Trading correctness must not depend on a specific hardware configuration.

Resource-dependent features should degrade explicitly.

## 160 — PRODUCTION SECURITY

Production hardening must cover:

- Authentication
- Authorization
- Secrets
- Encryption
- Network controls
- Audit
- AI permissions
- Tool permissions
- Key management
- Dependency security
- Vulnerability monitoring
- Security incident handling
- Environment separation

## 161 — ENVIRONMENT SEPARATION

Explicitly separate:

- Development
- Testing
- Staging
- Paper
- Canary
- Production

Live credentials must never accidentally appear in lower environments.

## 162 — PAPER / LIVE CREDENTIAL SEPARATION

Paper mode must never accidentally execute against live accounts.

Environment and credentials must be independently controlled.

## 163 — LIVE TRADING GATE

Live trading requires explicit authorization and activation.

Documentation/development/testing/paper environments must not accidentally inherit live execution authority.

## 164 — PRODUCTION CHANGE CONTROL

Production changes should follow:

```text
PROPOSAL ↓ REVIEW ↓ TEST ↓ APPROVAL ↓ DEPLOY ↓ MONITOR ↓ ROLLBACK IF REQUIRED 
```

## 165 — CANARY DEPLOYMENT

Production strategy/system changes should use canary deployment where appropriate.

Canary must have:

- Limited exposure
- Defined success criteria
- Defined failure criteria
- Monitoring
- Rollback path

## 166 — ROLLBACK

Rollback must be deterministic and tested.

The system should know:

- What version was active
- What changed
- What prior version is valid
- How to restore it
- How to reconcile state afterward

## 167 — DISASTER RECOVERY

The project must eventually define:

- Backup strategy
- Recovery points
- Recovery procedures
- Recovery validation
- Environment restoration
- Financial reconciliation
- Operational restart
- Incident procedures

## 168 — PERFORMANCE TESTING

The system should measure:

- Latency
- Throughput
- CPU
- Memory
- Database performance
- Queue latency
- Network latency
- Execution path latency
- AI latency

## 169 — LOAD TESTING

Test behavior under:

- High market event rates
- Many opportunities
- Multiple venues
- Concurrent strategies
- Large historical datasets
- AI bursts
- Reconciliation load

## 170 — CHAOS TESTING

Where appropriate, test:

- Exchange disconnect
- WebSocket failure
- Database failure
- AI provider failure
- Queue failure
- Network degradation
- Slow responses
- Partial services
- Process restart
- Host failure

The system should enter safe states rather than undefined behavior.

## 171 — MONITORING

Monitoring should cover:

- Market data
- Data quality
- Risk
- Capital
- Execution
- Exchanges
- Strategies
- AI
- Infrastructure
- Database
- Queues
- Reconciliation
- Security
- Migration
- Backup

## 172 — ALERTING

Alerts should be prioritized according to severity.

Examples:

- Critical capital discrepancy
- Unknown order state
- Unknown position state
- Risk engine failure
- Exchange outage
- Security incident
- Reconciliation failure
- Excessive trading
- Strategy degradation
- Data corruption

## 173 — CANONICAL CONSISTENCY SYSTEM

The project should eventually have a mechanism for detecting contradictions between:

- Requirements
- Architecture
- Interfaces
- Schemas
- Strategies
- Policies
- Roadmap
- Tests
- Documentation

Exact implementation remains an architecture decision.

## 174 — GLOBAL PROJECT CONSTITUTION

A central constitution/specification may define non-negotiable principles:

- Deterministic core
- AI boundary
- Capital preservation
- Risk precedence
- No fixed returns
- True net profitability
- Unknown-state safety
- Controlled self-improvement
- Auditability
- Reconciliation
- No duplicate authorities

Final naming is an architecture decision.

## 175 — CONSISTENCY ORCHESTRATION

When a requirement changes:

```text
REQUIREMENT ↓ AFFECTED ARCHITECTURE ↓ AFFECTED INTERFACES ↓ AFFECTED SCHEMAS ↓ AFFECTED TESTS ↓ AFFECTED ROADMAP ↓ AFFECTED DOCUMENTATION 
```

The system should identify affected artifacts.

## 176 — DOMAIN COMMAND LANGUAGE

A compact structured command language may eventually reduce repetitive orchestration.

It must never bypass:

- Validation
- Authorization
- Audit
- Policy
- Risk
- Schema validation

It remains a proposal until formally approved.

## 177 — DOCUMENTATION-FIRST REPOSITORY

The repository is the canonical project knowledge base.

Conversation history is not the permanent source of truth.

Claude must organize project knowledge into authoritative files.

## 178 — DOCUMENTATION OWNERSHIP

Major systems should have authoritative documentation locations.

At minimum:

- Requirements
- Architecture
- Market Data
- Quant
- Regime
- Opportunities
- Risk
- Capital
- Portfolio
- Execution
- Arbitrage
- AI
- Policy
- Strategies
- Security
- Paper Trading
- Readiness
- Monitoring
- Performance
- Testing
- Deployment
- Migration
- Recovery
- Roadmap

## 179 — REQUIREMENTS REGISTRY

One canonical requirements registry.

Each requirement should contain:

- Requirement ID
- Description
- Source
- Classification
- Owner
- System
- Dependencies
- Status
- Priority
- Roadmap stage
- Verification method
- Related documents
- Approval state

## 180 — SOURCE CLASSIFICATION

Possible classifications:

- Confirmed requirement
- Architectural principle
- Constraint
- Design decision
- Proposal
- Future concept
- Requires confirmation
- Open question
- Technical concern
- Deprecated
- Replaced

## 181 — NO SILENT REQUIREMENT PROMOTION

A previously discussed idea must not automatically become an approved production requirement.

For example:

- Platform-managed accounts

must remain an architectural option unless formally approved.

## 182 — CONFLICT REGISTER

The repository must contain a conflict register.

Potential conflicts:

- Different risk assumptions
- Duplicate services
- Different profitability definitions
- Different capital authorities
- Different policy authorities
- Different strategy lifecycles
- Conflicting deployment assumptions

Each conflict must be:

- Identified
- Analyzed
- Resolved or marked open
- Linked to affected requirements
- Reflected in documentation

## 183 — DUPLICATE-SYSTEM AUDIT

Before implementation, search for duplicate responsibilities.

Examples:

- Two Capital Managers
- Two Risk Engines
- Two Fee Engines
- Two Portfolio authorities
- Two Strategy Registries
- Two Opportunity Engines
- Two Policy Engines
- Two AI Gateways
- Two Market-data normalizers
- Two audit authorities
- Two Readiness systems
- Two dashboard authorities

Ownership must be resolved.

## 184 — CANONICAL SERVICE PRINCIPLE

Centralize fundamental authorities.

Examples:

One:

- Capital Authority
- Risk Authority
- Portfolio Authority
- Policy Authority
- Fee Engine
- Slippage Engine
- Exchange abstraction
- Audit system
- Market-data normalization layer
- Strategy Registry
- Readiness System
- Opportunity Registry

Specialized systems may operate above these authorities.

## 185 — CROSS-REFERENCE INSTEAD OF DUPLICATION

If a requirement affects multiple systems:

Create one authoritative definition.

Cross-reference it.

Do not duplicate conflicting copies.

## 186 — MASTER ROADMAP

Part 1 + all prior discussions + this Part 2 must feed one master roadmap.

There must not be competing master roadmaps.

Specialized roadmap views are acceptable, but one dependency-driven roadmap remains authoritative.

## 187 — MASTER TRACEABILITY

One traceability system should connect:

```text
SOURCE → REQUIREMENT → ARCHITECTURE → SYSTEM → IMPLEMENTATION → TEST → VERIFICATION → ROADMAP → APPROVAL 
```

## 188 — ROADMAP: DETERMINISTIC FOUNDATION

The master roadmap should generally establish:

```text
DATA ↓ NORMALIZATION ↓ QUANT ↓ REGIME ↓ OPPORTUNITY ↓ RISK ↓ CAPITAL ↓ EXECUTION ↓ RECONCILIATION ↓ PORTFOLIO ↓ MONITORING 
```

before advanced AI functionality.

## 189 — ROADMAP: AI INFRASTRUCTURE

Potential sequence:

```text
AI GATEWAY ↓ STRUCTURED SCHEMAS ↓ TOOL PERMISSIONS ↓ MODEL ROUTER ↓ RESOURCE GOVERNOR ↓ CACHING ↓ FAILOVER ↓ AGENT ARCHITECTURE ↓ HALLUCINATION FIREWALL ↓ MULTI-AGENT VALIDATION ↓ CONTROLLED STRATEGY RESEARCH 
```

## 190 — ROADMAP: PAPER / READINESS

Potential sequence:

```text
PAPER EXECUTOR ↓ SIMULATED CAPITAL ↓ CONTINUOUS PAPER ↓ EXPECTED-VS-ACTUAL ↓ EVIDENCE ACCUMULATION ↓ READINESS SYSTEM ↓ READINESS DASHBOARD ↓ CANARY ↓ PRODUCTION 
```

## 191 — ROADMAP: ARBITRAGE

```text
EXCHANGE ADAPTERS ↓ MARKET DATA ↓ FEE ENGINE ↓ SLIPPAGE ENGINE ↓ LIQUIDITY ↓ CAPITAL ↓ RISK ↓ EXECUTION ↓ RECONCILIATION ↓ CROSS-EXCHANGE ↓ TRIANGULAR ↓ INVENTORY ↓ REBALANCING ↓ EXPECTED-VS-ACTUAL 
```

## 192 — ROADMAP: HOSTING & PORTABILITY

Include:

- Environment abstraction
- Local deployment
- Server deployment
- Portable configuration
- Database migration
- Backup/restore
- Migration package
- Migration validation
- Active-instance protection
- Split-brain prevention
- Failover where approved
- Local/server migration testing

## 193 — ROADMAP: AUTONOMY

```text
DETERMINISTIC FOUNDATION ↓ POLICY REPRESENTATION ↓ POLICY COMPILER ↓ POLICY VALIDATION ↓ GLOBAL CONTROLLER ↓ SAFE STATES ↓ AUTONOMOUS ORCHESTRATION ↓ AI INTEGRATION ↓ CONTROLLED AUTONOMOUS IMPROVEMENT 
```

## 194 — ROADMAP: PRODUCTION HARDENING

Before production:

- Security
- Secrets
- Monitoring
- Alerting
- Reconciliation
- Backup
- Restore
- Disaster recovery
- Failure testing
- Performance testing
- Load testing
- Chaos testing
- Deployment
- Canary
- Rollback
- Incident management

## 195 — MASTER DEPENDENCY PRINCIPLE

Claude must not implement features according to the order in which they appear in conversation.

Implementation must follow dependencies.

A feature must not be implemented before the infrastructure required to make it safe exists.

## 196 — ORIGINAL ADDITION: DETERMINISTIC CORE VS AI INTELLIGENCE LAYER

The distinction between the deterministic trading infrastructure and AI intelligence layer is foundational.

The deterministic core owns correctness, financial authority, execution and safety.

The AI layer owns interpretation, research, reasoning, hypotheses and proposals.

AI cannot replace deterministic authorities.

## 197 — AI MUST NOT BECOME FINANCIAL SOURCE OF TRUTH

AI cannot authoritatively determine:

- Balance
- Capital
- Positions
- Orders
- Fees
- Slippage
- P&L
- Exposure
- Risk
- Reservations
- Reconciliation
- Ledger state

## 198 — DETERMINISTIC SYSTEM MUST NOT DEPEND ON AI UNNECESSARILY

The normal trading path must remain deterministic.

## 199 — AI PROPOSAL / DETERMINISTIC AUTHORITY

AI outputs must pass:

```text
SCHEMA ↓ POLICY ↓ RISK ↓ CAPITAL ↓ EXECUTION 
```

## 200 — ORIGINAL AI AGENT ORGANIZATION

The previously discussed roles remain:

- Market Analyst
- Quant Research Agent
- Strategy Research Agent
- Trading Director
- Devil's Advocate
- Performance Analyst
- Strategy Optimizer
- Model Evaluation Agent
- AI Cost Manager

Final decomposition must be based on documented ownership.

## 201 — TRADING DIRECTOR AUTHORITY BOUNDARY

Trading Director coordinates intelligence and proposes trades.

It does not independently bypass deterministic authority.

## 202 — HALLUCINATION FIREWALL

Material claims must be evidence-bound.

## 203 — EVIDENCE-BACKED AI

Unsupported material claims should be rejected or marked uncertain.

## 204 — MULTI-AGENT VALIDATION

Important decisions may be independently reviewed.

## 205 — AI DISAGREEMENT

Disagreement must lead to additional validation or WAIT/NO TRADE where appropriate.

## 206 — MODEL ROUTER

Models should be selected by task, quality, cost, latency, reliability and consequence.

## 207 — MODEL SELECTION MUST BE TASK-SPECIFIC

Simple tasks should not automatically consume premium models.

## 208 — AI MODEL EVALUATION

Models must be measured rather than trusted based solely on reputation.

## 209 — STRATEGY FACTORY

Controlled strategy lifecycle:

```text
RESEARCH → HYPOTHESIS → BACKTEST → VALIDATION → OOS → ROBUSTNESS → PAPER → APPROVAL → CANARY → PRODUCTION 
```

## 210 — STRATEGY REGISTRY

Strategies require canonical IDs, versions, validation history and lifecycle states.

## 211 — STRATEGY VERSION IMMUTABILITY

Historical production strategy versions must remain reconstructable.

## 212 — MARKET REGIME ENGINE

Regime Engine remains deterministic and supports UNKNOWN.

## 213 — UNKNOWN REGIME MUST NOT BE TREATED AS SAFE

Unknown is not an invitation to guess.

## 214 — OPPORTUNITY DATABASE

The Opportunity Database retains meaningful opportunities and outcomes.

## 215 — REJECTED OPPORTUNITIES ARE DATA

Rejected opportunities must be preserved for analysis.

## 216 — CROSS-EXCHANGE ARBITRAGE

Use true executable economics, not raw spread.

## 217 — TRIANGULAR ARBITRAGE

Automatically discover and evaluate routes.

## 218 — TRIANGULAR EXECUTION

Account for leg failure, partial fills, liquidity, precision, timing and residual assets.

## 219 — CROSS-EXCHANGE CAPITAL PRE-POSITIONING

Pre-positioned capital may improve execution speed.

## 220 — INTELLIGENT REBALANCING

Do not transfer assets automatically after every opportunity.

## 221 — ARBITRAGE CAPITAL RESERVE

Capital Authority should support dedicated arbitrage reserves where approved.

## 222 — ARBITRAGE RISK ENGINE

Specialized arbitrage risk integrates with global Risk Authority.

## 223 — ARBITRAGE KILL SWITCH

Arbitrage can be disabled independently.

## 224 — ARBITRAGE PERFORMANCE CONTROLLER

Expected-vs-actual arbitrage performance must be measured.

## 225 — ARBITRAGE OPPORTUNITY QUALITY TIERS

Previously discussed tiers remain analytical categories only.

## 226 — NO GUARANTEED RETURN ARCHITECTURE

No fixed return is encoded.

## 227 — COMPOUNDING IS POLICY-DRIVEN

Compounding follows realized capital and policy authorization.

## 228 — CAPITAL AUTHORITY

One canonical Capital Authority.

## 229 — GLOBAL RISK AUTHORITY

One canonical Risk Authority.

## 230 — PORTFOLIO AUTHORITY

One canonical Portfolio Authority.

## 231 — EXCHANGE ADAPTER SYSTEM

Use standardized adapters.

## 232 — EXCHANGE ADAPTER RESPONSIBILITIES

Adapters own venue-specific mechanics.

## 233 — EXCHANGE NORMALIZATION

Normalize venue-specific representations.

## 234 — PAPER TRADING

Paper should share the live architecture where practical.

## 235 — LIVE TRADING GATE

Live execution requires explicit authorization.

## 236 — ENVIRONMENT MODES

Support:

- Development
- Testing
- Staging
- Paper
- Canary
- Production

## 237 — HOSTING CHOICE

Support local and server hosting.

## 238 — LOCAL HOSTING MODEL

Support required services locally according to available resources.

## 239 — SERVER HOSTING MODEL

Deploy the same logical system remotely.

## 240 — HOSTING ABSTRACTION

Business/trading logic must be separated from hosting.

## 241 — LOCAL ↔ SERVER PORTABILITY

Migration must support both directions.

## 242 — MIGRATION MUST NOT MEAN COPYING RANDOM FILES

Formal migration packages/processes are required.

## 243 — PORTABLE PLATFORM STATE

Portable state must be defined explicitly.

## 244 — SECRETS MUST NOT BE EXPORTED UNSAFELY

Secrets use secure migration mechanisms.

## 245 — ENVIRONMENT-SPECIFIC CONFIGURATION

Separate portable and deployment-specific configuration.

## 246 — CONFIGURATION COMPILER / ENVIRONMENT ADAPTER

Resolve target environment safely.

## 247 — DATABASE MIGRATION

Database migrations must preserve financial integrity.

## 248 — MIGRATION PRE-FLIGHT CHECK

Migration begins only after state and environment checks.

## 249 — SAFE MIGRATION OPERATING STATE

Migration has explicit deterministic states.

## 250 — OPEN ORDERS DURING MIGRATION

Orders must be reconciled against the exchange.

## 251 — OPEN POSITIONS DURING MIGRATION

Positions must be reconciled.

## 252 — CAPITAL STATE DURING MIGRATION

Capital must be reconciled against authoritative external state.

## 253 — MIGRATION VALIDATION

Migration is incomplete until validation and reconciliation succeed.

## 254 — MIGRATION ROLLBACK

Failed migration must not resume live trading.

## 255 — DEPLOYMENT PACKAGE

Deployment must become reproducible.

## 256 — INFRASTRUCTURE AS CODE

Use where approved.

## 257 — SINGLE SOURCE OF DEPLOYMENT TRUTH

Repository contains authoritative deployment definition.

## 258 — BACKUP + MIGRATION ARE DISTINCT

Both must exist.

## 259 — LOCAL/SERVER MIGRATION TESTING

Both migration directions must be tested.

## 260 — MIGRATION DRY RUN

Dry-run validation should be supported where practical.

## 261 — USER SHOULD NOT NEED TO UNDERSTAND INTERNAL MIGRATION DETAILS

Normal users should not reconstruct the system manually.

## 262 — HOSTING MIGRATION SHOULD PRESERVE LOGICAL IDENTITY

Logical platform identity should survive migration.

## 263 — UNIQUE ENVIRONMENT IDENTITY

Deployment instances must remain distinguishable.

## 264 — SPLIT-BRAIN PROTECTION

Only one authorized production execution instance may control a trading account.

## 265 — ACTIVE TRADING INSTANCE AUTHORITY

Standby/read-only instances cannot accidentally execute.

## 266 — LOCAL FAILURE / SERVER FAILOVER

Failover begins with reconciliation.

## 267 — STANDBY MODE

Standby must require explicit activation.

## 268 — CLOUD/LOCAL RESOURCE DIFFERENCES

Resource differences must not change financial correctness.

## 269 — AI HOSTING INDEPENDENCE

AI may run locally, remotely or through providers depending on approved architecture.

## 270 — REMOTE AI PROVIDER FAILURE

Core trading must remain independently operable where possible.

## 271 — RESEARCH COMPUTE IS NOT LIVE EXECUTION COMPUTE

Research workloads must not starve execution.

## 272 — RESOURCE PRIORITY

Safety and execution have priority over research.

## 273 — ORIGINAL EVENT-DRIVEN PRINCIPLE

Use events instead of unnecessary polling.

## 274 — OPPORTUNITY FILTER

Fast deterministic filtering should precede expensive processing.

## 275 — EVENT-DRIVEN AI ACTIVATION

AI triggers may include:

- Regime transition
- Major news
- Unusual volatility
- Conflicting signals
- Strategy deterioration
- Complex portfolio state
- Significant opportunity
- Research events
- Failure investigation

## 276 — NO AI ON EVERY TICK

This requirement remains mandatory.

## 277 — AUTONOMOUS SYSTEM OBJECTIVE

The platform should operate autonomously within authorized user objectives and constraints.

## 278 — AUTONOMY DOES NOT MEAN UNLIMITED AUTHORITY

Autonomy remains bounded.

## 279 — USER POLICY AS HIGHEST APPLICATION AUTHORITY

Hard user constraints outrank lower-level decisions.

## 280 — POLICY SHOULD BE MACHINE-READABLE

Natural language should eventually compile into structured policy.

## 281 — POLICY TRACEABILITY

Decisions reference policy versions.

## 282 — POLICY CHANGE MUST NOT REWRITE HISTORY

New policy = new version.

## 283 — POLICY SIMULATION

Material changes should be simulatable.

## 284 — AUTONOMOUS IMPROVEMENT REMAINS CONTROLLED

No direct self-modification of live production.

## 285 — PRODUCTION SYSTEM MUST REMAIN UNDERSTANDABLE

Autonomy must increase observability.

## 286 — DOCUMENTATION-FIRST REPOSITORY

Repository is canonical.

## 287 — DOCUMENTATION OWNERSHIP

Each major system gets authoritative documentation.

## 288 — REQUIREMENTS REGISTRY

One canonical requirements registry.

## 289 — SOURCE CLASSIFICATION

Every requirement is classified.

## 290 — NO SILENT REQUIREMENT PROMOTION

Ideas remain ideas until approved.

## 291 — CONFLICT REGISTER

Conflicts are documented and tracked.

## 292 — DUPLICATE-SYSTEM AUDIT

Duplicate ownership must be eliminated.

## 293 — CANONICAL SERVICE PRINCIPLE

Shared authorities remain centralized.

## 294 — REPOSITORY CONSISTENCY SYSTEM

The repository should eventually detect inconsistencies.

## 295 — GLOBAL-CONSTITUTION-STYLE PRINCIPLE

Central non-negotiable principles should be documented.

## 296 — CONSISTENCY ORCHESTRATION

Changes should identify affected artifacts.

## 297 — DOMAIN COMMAND LANGUAGE

Potential compact orchestration language remains a proposal.

## 298 — TOOL-FIRST AI ARCHITECTURE

AI accesses deterministic systems through controlled tools.

## 299 — AI PERMISSION SCOPES

Minimum privilege is required.

## 300 — PRODUCTION DEPLOYMENT AUTHORITY

AI does not automatically promote production.

## 301 — SECURITY BOUNDARY BETWEEN AI AND CUSTODY

AI cannot directly control keys or withdrawals.

## 302 — CUSTODY REMAINS A SEPARATE ARCHITECTURAL DOMAIN

Custody is not automatically part of core trading.

## 303 — INTERNAL LEDGER AUTHORITY

If custody is approved, the ledger becomes authoritative.

## 304 — LEDGER RECONCILIATION

Ledger, exchange and blockchain state must reconcile.

## 305 — WITHDRAWAL AUTHORITY SEPARATION

Trading and withdrawal permissions remain separate.

## 306 — RECOVERY AFTER CRASH

Recovery begins with reconciliation.

## 307 — ORDER TIMEOUT DOES NOT EQUAL ORDER FAILURE

Timeout requires external-state verification.

## 308 — TRANSFER TIMEOUT DOES NOT EQUAL TRANSFER FAILURE

Transfer state must be verified.

## 309 — RESTART SAFETY

Restart requires state verification.

## 310 — NO-TRADE AS FIRST-CLASS STATE

No-trade is valid.

## 311 — SAFE WAIT STATE

Wait is valid.

## 312 — CAPITAL PRESERVATION REMAINS PRIMARY

Conceptual hierarchy:

- Capital Preservation
- Risk Control
- Execution Safety
- Positive Net Profitability
- Capital Efficiency
- Compounding / Growth
- Opportunity Targets

## 313 — OVERALL SYSTEM OBJECTIVE

Maximize risk-adjusted, executable, net profitability while preserving capital and avoiding unnecessary exposure.

Not:

- Maximum trades
- Maximum AI activity
- Maximum leverage
- Maximum percentage per trade
- Fixed daily return

## 314 — COMPLETE HIGH-LEVEL ARCHITECTURE

```text
USER ↓ NATURAL-LANGUAGE POLICY ↓ POLICY COMPILER / VALIDATION ↓ STRUCTURED POLICY ↓ GLOBAL PLATFORM CONTROLLER ↓ WHOLE-MARKET UNIVERSE ↓ MARKET DATA ↓ DATA VALIDATION ↓ QUANTITATIVE ENGINE ↓ REGIME ENGINE ↓ OPPORTUNITY ENGINE ↓ OPPORTUNITY FILTER ↓ STRATEGY ENGINE ↓ AI INTELLIGENCE WHEN JUSTIFIED ↓ TRADE / OPPORTUNITY PROPOSAL ↓ DETERMINISTIC VALIDATION ↓ RISK AUTHORITY ↓ CAPITAL AUTHORITY ↓ EXECUTION ENGINE ↓ EXCHANGE ADAPTER ↓ VENUE ↓ RECONCILIATION ↓ PORTFOLIO / LEDGER ↓ MONITORING ↓ PERFORMANCE ANALYSIS ↓ CONTROLLED IMPROVEMENT ↓ VALIDATION ↓ PAPER ↓ CANARY ↓ PRODUCTION 
```

## 315 — COMPLETE AI ARCHITECTURE

```text
EVENT ↓ OPPORTUNITY / RESEARCH FILTER ↓ DOES THIS REQUIRE AI? ├── NO → DETERMINISTIC PATH └── YES ↓ AI RESOURCE GOVERNOR ↓ TASK CLASSIFICATION ↓ MODEL ROUTER ↓ SPECIALIZED AGENT ↓ STRUCTURED OUTPUT ↓ HALLUCINATION / EVIDENCE VALIDATION ↓ MULTI-AGENT VALIDATION WHERE REQUIRED ↓ DETERMINISTIC SYSTEM ↓ ACCEPT / REJECT / WAIT 
```

## 316 — COMPLETE LIVE TRADING LOOP

```text
MARKET DATA ↓ VALIDATE ↓ NORMALIZE ↓ QUANT ↓ REGIME ↓ OPPORTUNITY ↓ FILTER ↓ STRATEGY ↓ AI IF JUSTIFIED ↓ PROPOSAL ↓ RISK ↓ CAPITAL ↓ EXECUTION ↓ POSITION MONITORING ↓ RECONCILIATION ↓ P&L ↓ PERFORMANCE ↓ LEARNING INPUT 
```

## 317 — COMPLETE CONTROLLED IMPROVEMENT LOOP

```text
OBSERVATION ↓ PERFORMANCE ANALYSIS ↓ DRIFT / DETERIORATION ↓ RESEARCH ↓ HYPOTHESIS ↓ CANDIDATE STRATEGY ↓ BACKTEST ↓ OUT-OF-SAMPLE ↓ WALK-FORWARD ↓ STRESS TEST ↓ ROBUSTNESS ↓ PAPER ↓ APPROVAL ↓ CANARY ↓ PRODUCTION ↓ MONITOR ↓ ROLLBACK IF REQUIRED 
```

## 318 — COMPLETE HOSTING ARCHITECTURE

### OPTION A — LOCAL

```text
USER COMPUTER / SERVER ↓ PLATFORM RUNTIME ↓ DATABASE ↓ TRADING SERVICES ↓ AI SERVICES / PROVIDERS ↓ EXCHANGES 
```

### OPTION B — REMOTE SERVER

```text
USER ↓ REMOTE PLATFORM ↓ DATABASE ↓ TRADING SERVICES ↓ AI SERVICES / PROVIDERS ↓ EXCHANGES 
```

The trading logic remains the same.

## 319 — COMPLETE MIGRATION ARCHITECTURE

```text
LOCAL ↓ SAFE TRADING STATE ↓ BACKUP ↓ EXPORT PORTABLE STATE ↓ VERIFY ↓ TRANSFER ↓ RESTORE ↓ ENVIRONMENT CONFIGURATION ↓ SCHEMA VALIDATION ↓ POLICY VALIDATION ↓ STRATEGY VALIDATION ↓ CAPITAL RECONCILIATION ↓ POSITION RECONCILIATION ↓ ORDER RECONCILIATION ↓ EXCHANGE HEALTH ↓ RESUME 
```

Reverse migration must also be supported.

## 320 — MIGRATION MUST PRESERVE THE PROJECT, NOT JUST CODE

Migration is successful only when the destination reproduces the relevant logical state.

It is not sufficient that:

- "The application starts."

## 321 — MIGRATION COMPLETION CRITERIA

Migration is complete only when:

- Application starts
- Database is valid
- Schema is correct
- Configuration is valid
- Secrets are securely available
- Policies are intact
- Strategies are intact
- Active versions are correct
- Capital reconciles
- Positions reconcile
- Orders reconcile
- Exchanges are reachable
- Monitoring works
- Risk works
- Execution is configured correctly
- Active-instance ownership is established
- Safe operation is verified

## 322 — ROADMAP ADDITION: HOSTING & PORTABILITY

The master roadmap must include deployment portability.

## 323 — ROADMAP ADDITION: DETERMINISTIC CORE

The deterministic foundation must precede advanced AI.

## 324 — ROADMAP ADDITION: AI INFRASTRUCTURE

AI infrastructure follows deterministic foundations.

## 325 — ROADMAP ADDITION: ARBITRAGE

Arbitrage follows exchange, economics, capital, risk and execution foundations.

## 326 — ROADMAP ADDITION: AUTONOMY

Autonomy follows policy, safety and deterministic foundations.

## 327 — ROADMAP ADDITION: PRODUCTION HARDENING

Production requires security, observability, testing, backup, recovery and controlled deployment.

## 328 — MASTER DEPENDENCY PRINCIPLE

Claude must build according to dependency order, not conversation order.

## 329 — MASTER IMPLEMENTATION GATE

The complete project follows:

```text
PART 1 + PART 2 + ALL ADDITIONAL REQUIREMENTS ↓ DOCUMENTATION ANALYSIS ↓ CLASSIFICATION ↓ REQUIREMENTS REGISTRY ↓ CANONICAL ARCHITECTURE ↓ SYSTEM OWNERSHIP ↓ DEPENDENCY GRAPH ↓ CONFLICT ANALYSIS ↓ DUPLICATION ANALYSIS ↓ SECURITY REVIEW ↓ ROADMAP ↓ TRACEABILITY ↓ VERIFICATION PLAN ↓ HUMAN REVIEW ↓ APPROVAL ↓ IMPLEMENTATION 
```

## 330 — CLAUDE MUST NOT START IMPLEMENTATION FROM THIS HANDOFF ALONE

This is project knowledge.

It is not authorization to immediately begin coding.

## 331 — REQUIRED FIRST CLAUDE WORKFLOW

Claude must first:

Read Part 1.

Read the complete Part 2.

Inspect the repository.

Identify existing documentation.

Identify duplicates.

Identify conflicting requirements.

Identify missing systems.

Establish authoritative ownership.

Create/update the requirements registry.

Create/update the traceability matrix.

Create/update the dependency graph.

Create/update architecture documentation.

Create/update the master roadmap.

Create/update the Paper Trading architecture.

Create/update the Readiness System architecture.

Create/update the Daily System Intelligence Dashboard/Report specification.

Create/update arbitrage architecture.

Create/update deployment/migration architecture.

Record open questions.

Produce a documentation audit.

Stop for human review/approval before normal implementation.

## 332 — REPOSITORY MUST BECOME THE CANONICAL KNOWLEDGE BASE

The final repository should not require Claude to repeatedly search historical conversations.

Goal:

```text
CONVERSATION KNOWLEDGE ↓ ORGANIZED DOCUMENTATION ↓ CANONICAL REPOSITORY KNOWLEDGE 
```

## 333 — NO RANDOM KNOWLEDGE DUMP

Claude must not put everything into one giant miscellaneous file.

Information must be placed according to ownership.

Examples:

- Risk → Risk documentation
- Arbitrage → Arbitrage documentation
- Migration → Deployment/Migration documentation
- AI → AI architecture
- Policy → Policy architecture
- Testing → Verification architecture
- Paper → Paper Trading architecture
- Readiness → Readiness architecture
- Dashboard → Observability/System Intelligence architecture

## 334 — CROSS-REFERENCE INSTEAD OF DUPLICATION

Create one authoritative definition and reference it.

## 335 — MASTER ROADMAP MUST BE SINGLE

One authoritative dependency-driven roadmap.

## 336 — MASTER REQUIREMENTS REGISTRY MUST BE SINGLE

All approved requirements eventually enter one registry.

## 337 — MASTER TRACEABILITY MUST BE SINGLE

One canonical traceability system.

## 338 — FINAL CONSOLIDATED PROJECT PRINCIPLE

The platform is:

- Market-data infrastructure
- Quantitative computation
- Risk authority
- Capital authority
- Execution infrastructure
- Portfolio management
- Arbitrage
- Strategy management
- Controlled AI intelligence
- Natural-language policy
- Controlled strategy improvement
- Paper operation
- Readiness management
- Reconciliation
- Auditability
- Security
- Monitoring
- Recovery
- Performance engineering
- Deployment portability
- Local/server hosting
- Controlled migration
- Production operations

AI is an intelligence layer inside this larger system.

## 339 — FINAL DETERMINISTIC VS AI RESPONSIBILITY TABLE

ResponsibilityDeterministic CoreAI LayerMarket dataAuthoritativeInterpretIndicatorsCalculateInterpretFeesCalculateExplainSlippageCalculateAnalyzeNet profitabilityCalculateInterpretRisk limitsEnforcePropose/analyzeCapitalAuthoritativeConsume informationPosition stateAuthoritativeInterpretOrder stateAuthoritativeInterpretExecutionExecuteProposePolicy enforcementEnforceInterpret user intentStrategy researchSupport dataPrimary intelligence roleStrategy proposalValidateGenerateStrategy deploymentControlProposeNews analysisProvide source/dataAnalyzeMarket interpretationProvide factsInterpretReconciliationAuthoritativeDiagnoseLedgerAuthoritativeRead/analyzeAuditAuthoritativeContribute metadataKill switchDeterministicCannot overrideSafe modeDeterministicCannot overrideAI selectionN/ARouter/GovernorModel evaluationDeterministic metrics + AI analysisAnalyzeResearchInfrastructureIntelligenceLive executionDeterministicAdvisory/proposalSelf-improvementControlled pipelineGenerate candidatesPaper executionDeterministic simulatorAnalyzeReadinessAuthoritative gateProvide analysisDashboardDeterministic aggregationSummarize/interpret

## 340 — FINAL HOSTING PRINCIPLE

The choice:

```text
LOCAL 
```

or:

```text
SERVER 
```

is an infrastructure/deployment decision.

It must not create two different trading platforms.

## 341 — FINAL MIGRATION PRINCIPLE

The platform must support:

```text
LOCAL → SERVER 
```

and:

```text
SERVER → LOCAL 
```

without rebuilding the trading architecture.

## 342 — FINAL STATE SAFETY PRINCIPLE

Before live execution begins, the system must know:

- Active policy
- Active strategy versions
- Capital
- Positions
- Orders
- Exchange state
- Risk state
- Execution state

If critical state is unknown:

```text
NO TRADE / WAIT / SAFE MODE 
```

## 343 — FINAL AUTONOMY PRINCIPLE

The user provides high-level objectives and boundaries.

The platform translates them into structured policies.

Deterministic infrastructure enforces them.

AI provides intelligence inside those boundaries.

The system must never invent authorization.

## 344 — FINAL PERFORMANCE PRINCIPLE

Latency-sensitive paths should remain deterministic wherever possible.

Minimize:

- Internal computation overhead
- Unnecessary AI calls
- Unnecessary network calls
- Repeated calculations
- Database bottlenecks
- Queue congestion
- Lock contention

Measure performance rather than assuming it.

## 345 — FINAL PROFITABILITY PRINCIPLE

Evaluate:

- TRUE EXECUTABLE NET ECONOMICS

not:

- Headline spread
- Gross percentage
- AI prediction
- Fixed daily target

A small positive executable opportunity may be valid.

A large theoretical opportunity may be rejected.

## 346 — FINAL SAFETY PRINCIPLE

When uncertain:

Do not invent certainty.

Do not assume an order failed.

Do not assume a position disappeared.

Do not assume a balance is correct.

Do not assume an exchange is healthy.

Do not assume AI is correct.

Do not assume data is valid.

Verify external state.

## 347 — FINAL MASTER OBJECTIVE

The final system should be:

- Deterministic-first
- AI-enhanced
- Autonomous within explicit authorization
- Risk-controlled
- Capital-preserving
- Execution-aware
- Latency-conscious
- Whole-market aware
- Arbitrage-capable
- Paper-operational
- Readiness-aware
- Self-improving only through controlled validation
- Auditable
- Reproducible
- Recoverable
- Secure
- Deployable locally or remotely
- Migratable between environments
- Testable
- Observable
- Consistent
- Production-grade

## 348 — FINAL MASTER HANDOFF INSTRUCTION

Claude Code must combine:

```text
PART 1 + PART 2 + ALL PREVIOUSLY DISCUSSED REQUIREMENTS 
```

into one coherent project knowledge system.

Claude must not treat them as competing specifications.

Correct process:

```text
PART 1 + PART 2 + PREVIOUS PROJECT KNOWLEDGE ↓ RECONCILIATION ↓ DEDUPLICATION ↓ CLASSIFICATION ↓ CONFLICT ANALYSIS ↓ AUTHORITATIVE OWNERSHIP ↓ REQUIREMENTS REGISTRY ↓ CANONICAL ARCHITECTURE ↓ DEPENDENCY GRAPH ↓ TRACEABILITY ↓ MASTER ROADMAP ↓ PAPER / READINESS ARCHITECTURE ↓ VERIFICATION PLAN ↓ DOCUMENTATION AUDIT ↓ HUMAN APPROVAL ↓ IMPLEMENTATION 
```

## 349 — FINAL REQUIREMENT: NOTHING IMPORTANT FROM PRIOR DISCUSSIONS MAY BE SILENTLY DROPPED

During reconciliation, Claude must explicitly check for previously discussed concepts including:

### Core Architecture

- Deterministic trading infrastructure
- AI intelligence layer
- Natural-language policy
- Autonomous operation
- Controlled self-improvement
- Global controller
- Policy compiler
- Safe states
- No-trade
- Wait
- Safe Mode

### Market Infrastructure

- Market-data ingestion
- WebSocket infrastructure
- Data normalization
- Data validation
- Data quality
- Data quarantine
- Data lineage
- Time synchronization
- Whole-market scanning
- Quantitative engine
- Regime engine
- UNKNOWN REGIME
- Opportunity Filter
- Opportunity Database
- True Net Profit
- Fee Engine
- Slippage Engine
- Liquidity protection
- Funding costs

### Risk / Capital / Portfolio

- Capital Authority
- Risk Authority
- Portfolio Authority
- Atomic capital reservation
- Capital allocation
- Capital utilization
- Loss-streak protection
- Excessive-trading protection
- Exposure control
- Drawdown control
- Strategy drift
- Kill switches
- No-new-position mode

### Execution

- Exchange adapters
- Binance
- OKX
- Coinbase
- Exchange normalization
- Order management
- Fill management
- Rate limits
- Connection management
- Partial fills
- Order timeout handling
- Reconciliation
- Execution latency
- Adaptive execution where approved

### Arbitrage

- Cross-exchange arbitrage
- Triangular arbitrage
- Pre-positioned capital
- Inventory management
- Intelligent rebalancing
- Arbitrage capital reserves
- Arbitrage risk
- Arbitrage kill switch
- Arbitrage performance controller
- Arbitrage opportunity tiers
- Expected-vs-actual arbitrage analysis
- Multi-leg execution risk

### Strategy

- Strategy Factory
- Strategy Registry
- Strategy versioning
- Strategy lifecycle
- Backtesting
- Out-of-sample testing
- Walk-forward testing
- Stress testing
- Monte Carlo/distribution analysis
- Anti-overfitting
- Paper trading
- Canary
- Production
- Rollback
- Strategy health
- Strategy drift
- Controlled optimization

### AI

- AI Resource Governor
- Model Router
- AI caching
- AI failover
- AI degradation
- AI cost/value optimization
- Market Analyst
- Quant Research
- Strategy Research
- Trading Director
- Devil's Advocate
- Performance Analyst
- Strategy Optimizer
- Model Evaluation
- AI Cost Manager
- Hallucination Firewall
- Evidence/timestamp requirements
- Multi-agent validation
- AI disagreement
- Tool-first architecture
- AI permission scopes

### Paper / Readiness

- Continuous real-time paper operation
- Simulated capital
- Paper execution
- Paper/live architectural parity
- Evidence accumulation
- Expected-vs-observed analysis
- Missed-opportunity analysis
- False-opportunity analysis
- Strategy-health analysis
- Paper readiness
- Canonical Readiness System
- Readiness states
- Readiness evidence
- Readiness blockers
- Paper → readiness → canary → production gate

### Intelligence / Observability

- Daily System Intelligence Dashboard
- Daily System Intelligence Report
- Market summary
- Opportunity summary
- Execution summary
- Capital summary
- Risk summary
- AI summary
- Strategy health
- Incident summary
- Readiness summary
- UNKNOWN reporting
- Historical reports
- Performance trends

### Safety

- No fixed return assumption
- No artificial daily profit ceiling
- Opportunity accumulation
- Capital compounding
- Safe states
- Kill switches
- Reconciliation
- Recovery
- Restart safety
- Unknown-state handling
- External-state verification
- Disaster recovery
- Backup/restore

### Data / Research Integrity

- Look-ahead bias prevention
- Data leakage prevention
- Protected dataset separation
- Survivorship bias protection
- Data deduplication
- Data integrity
- Experiment reproducibility
- Decision lineage
- Data lineage
- Version traceability

### Performance / Reliability

- Performance testing
- Load testing
- Chaos testing
- Backpressure
- Concurrency
- Atomicity
- Queue management
- Resource isolation
- Research compute isolation
- Connection resilience
- Rate-limit management

### Security

- AI permissions
- Tool permissions
- Secret management
- Environment separation
- Production change control
- Security monitoring
- Authentication
- Authorization
- Key-management boundary
- Withdrawal separation
- Custody isolation
- Incident management

### Deployment

- Local hosting
- Server/cloud hosting
- Hosting abstraction
- Local ↔ server migration
- Portable platform state
- Environment-specific configuration
- Configuration compiler/environment adapter
- Database migration
- Migration validation
- Migration dry-run
- Active-instance protection
- Split-brain prevention
- Failover
- Standby
- Deployment reproducibility
- Infrastructure-as-code where approved
- Backup/restore
- Disaster recovery

### Repository / Governance

- Canonical repository knowledge base
- Single master requirements registry
- Single master roadmap
- Single traceability system
- ADRs
- Conflict register
- Duplicate-system prevention
- Canonical service ownership
- Contract-first development
- API/interface versioning
- Deprecation
- Documentation ownership
- Consistency system
- Requirement classification
- No silent requirement promotion

This checklist is a reconciliation checklist, not permission to automatically classify every item as an approved production requirement.

Claude must classify each item according to the project's documentation rules.

## 350 — FINAL END STATE

After Part 1 + Part 2 + all previously discussed project requirements have been processed:

Claude should be able to understand the project without relying on the historical conversation.

The repository becomes the durable source of truth.

The central principle is:

AI provides intelligence. Deterministic infrastructure provides authority.

The operational principle is:

If the system does not know enough to act safely, it must be able to choose NO TRADE, WAIT, SAFE MODE, or another explicitly defined safe state.

The deployment principle is:

The same logical trading platform must be capable of running locally or on a server, with controlled migration between environments without corrupting financial, policy, strategy, or operational state.

The paper/readiness principle is:

Paper trading is a continuous evidence-generation environment, and progression toward live execution must be determined through a canonical readiness process rather than a single arbitrary performance number.

The improvement principle is:

The system may discover improvements autonomously, but production changes must pass controlled research, validation, paper, approval, canary and rollback processes.

The implementation principle is:

Documentation, architecture, requirements, dependencies, verification and approval come before production implementation.

## FINAL NON-NEGOTIABLES

No implementation gate is bypassed.

No important requirement should be silently dropped.

No duplicate authority should be created.

No AI component should become an uncontrolled financial authority.

No AI call should be placed on every market tick merely because AI exists.

No migration should be considered successful without reconciliation and validation.

No fixed return should be assumed.

No artificial daily profit ceiling should be introduced.

No theoretical spread should be treated as guaranteed profit.

No critical unknown state should be treated as safe.

No live strategy should be modified directly because of a single loss or AI suggestion.

No paper result should automatically become production authorization.

No historical strategy/policy/version should be silently rewritten.

No research workload should be allowed to compromise safety-critical execution infrastructure.

No local/server environment should become a separate trading architecture.

No custody functionality should be silently merged into the core trading engine.

No historical conversation should remain necessary once the repository documentation phase is complete.

## END OF COMPLETE CONSOLIDATED PART 2

PART 1 + PART 2 + PREVIOUS PROJECT KNOWLEDGE

must be treated as one canonical project knowledge base.

The repository must become the source of truth.

Documentation first.

Architecture second.

Dependencies third.

Verification fourth.

Human approval fifth.

Implementation after approval.
