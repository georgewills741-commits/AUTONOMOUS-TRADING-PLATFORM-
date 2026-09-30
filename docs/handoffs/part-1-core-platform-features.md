# GPT → CLAUDE CODE MASTER PROJECT HANDOFF

> **Status:** HISTORICAL — source input, received 2026-09-30. This is **not** an active source of truth.
>
> The content below has been analysed, classified, and redistributed into the canonical project documents. Where to find each section: [`docs/traceability/handoff-coverage.md`](../traceability/handoff-coverage.md).
>
> **Formatting note:** converted from plain text to Markdown (headings, lists, paragraph breaks). No wording was added, removed, or changed. Section numbers (§00–§103) are the handoff's own and are used as source references throughout the documentation.

PART 1 OF 2 — CORE PLATFORM FEATURES, SYSTEMS & CANONICAL FEATURE SPECIFICATION

Status: Master feature/system handoff — Documentation phase only

Builder: Claude Code

Project Architect / Specification Author: GPT

Project Type: Production-grade autonomous cryptocurrency trading platform

Implementation Philosophy: Company-grade, dependency-aware, traceable, deterministic-first, safety-first, performance-conscious, continuously verifiable.

## 00 — PART-SPECIFIC HANDOFF INSTRUCTION

This document is a project-knowledge and feature-specification input.

It is NOT permission to begin implementing the described trading functionality.

Claude Code must:

1. Analyze every feature and system described here.
2. Determine the authoritative system responsible for each feature.
3. Determine the correct repository documentation location.
4. Create the necessary documentation structure because the repository may initially be empty.
5. Derive the exact repository structure from the architecture and this handoff rather than blindly creating every possible folder.
6. Place each requirement under the appropriate authoritative file.
7. Do not simply place this entire handoff into one giant Markdown file.
8. Break the information into logically owned specifications.
9. Update the master documentation index.
10. Add important requirements to the requirements registry.
11. Add traceability relationships.
12. Map features to roadmap stages.
13. Record dependencies.
14. Identify duplicate responsibilities.
15. Identify architectural conflicts.
16. Identify unclear requirements.
17. Distinguish:
- Confirmed requirement
- Confirmed architectural principle
- Constraint
- System requirement
- Proposed idea
- Future feature
- Open question
- Technical concern
- Previously discussed / requiring confirmation
- Deprecated / replaced
18. Never silently convert a proposal into an approved requirement.
19. Never silently remove a requirement.
20. Never create duplicate sources of truth.
21. Never invent systems merely because they appear useful.
22. Do not begin normal feature implementation.
23. Do not modify production trading behavior.
24. Do not deploy anything.
25. Do not activate live trading.
26. Continue documentation initialization until all applicable information has an authoritative location.
27. Wait for the remaining handoff and required approval gates.

### Critical principle

The repository must become the canonical project knowledge base.

The conversation is not the permanent source of truth.

## 01 — PLATFORM IDENTITY

The project is a professional autonomous cryptocurrency trading platform.

It is not merely an AI trading bot.

The platform combines:

- Autonomous trading
- Directional trading
- Cross-exchange arbitrage
- Triangular arbitrage
- Quantitative analysis
- Market-data infrastructure
- Whole-universe opportunity monitoring
- Portfolio management
- Capital management
- Risk management
- Strategy management
- Backtesting
- Paper trading
- Live trading
- Exchange connectivity
- AI-assisted research
- AI reasoning
- Natural-language policy control
- Model routing
- AI cost management
- Strategy improvement
- Monitoring
- Recovery
- Reconciliation
- Security
- Auditability
- Reporting
- Controlled deployment
- Continuous development

The architecture must therefore be designed as a long-lived production platform rather than a collection of independent scripts or bots.

## 02 — CORE PLATFORM OBJECTIVE

The platform should provide a controlled autonomous trading environment capable of:

1. Connecting to supported trading venues.
2. Establishing authorized capital.
3. Receiving user objectives and restrictions.
4. Understanding those instructions through a controlled policy interface.
5. Representing them as structured, persistent policy.
6. Enforcing applicable hard constraints deterministically.
7. Monitoring the configured market universe continuously.
8. Detecting potential opportunities.
9. Evaluating opportunities deterministically.
10. Selecting appropriate validated strategies.
11. Performing quantitative analysis.
12. Using AI selectively for reasoning and research.
13. Applying deterministic risk controls.
14. Managing capital competition between strategies.
15. Validating execution conditions.
16. Executing through controlled exchange adapters.
17. Managing positions.
18. Reconciling internal and external state.
19. Recovering after interruptions.
20. Monitoring strategy and platform health.
21. Recording decisions and events.
22. Generating reports and alerts.
23. Improving strategies through controlled research.
24. Preventing unvalidated AI reasoning from directly controlling protected trading infrastructure.

The system must never assume that automation, AI, arbitrage, or a strategy guarantees profit.

## 03 — MULTI-STRATEGY ARCHITECTURE

The platform contains multiple trading systems.

### A. Directional Trading

Trades based on validated directional opportunities.

### B. Cross-Exchange Arbitrage

Trades executable discrepancies between venues.

### C. Triangular Arbitrage

Trades executable multi-leg opportunities within a venue/market graph.

These systems share infrastructure.

They must not become three unrelated applications.

Conceptual architecture:

```text
                 AUTONOMOUS TRADING PLATFORM
                           |
          +----------------+----------------+
          |                |                |
     DIRECTIONAL     CROSS-EXCHANGE    TRIANGULAR
       TRADING        ARBITRAGE         ARBITRAGE
          |                |                |
          +----------------+----------------+
                           |
                  SHARED INFRASTRUCTURE
                           |
 DATA / QUANT / STRATEGY / CAPITAL / RISK /
 PORTFOLIO / EXECUTION / AI / STORAGE /
 MONITORING / RECOVERY / SECURITY

```

## 04 — SHARED INFRASTRUCTURE PRINCIPLE

Trading systems must reuse common infrastructure.

They must not independently recreate:

- Market-data ingestion
- Data normalization
- Quantitative calculations
- Risk enforcement
- Capital accounting
- Portfolio accounting
- Exchange connectivity
- Execution
- Logging
- Monitoring
- Storage
- Recovery
- Reconciliation
- Security
- Strategy lifecycle
- AI infrastructure

A trading system owns its trading behavior.

Shared infrastructure owns common platform capabilities.

## 05 — DIRECTIONAL TRADING SYSTEM

The Directional Trading System identifies and manages opportunities where expected market movement creates a valid trading opportunity.

Responsibilities may include:

- Trend analysis
- Momentum
- Signal generation
- Entry conditions
- Exit conditions
- Confirmation
- Market-condition filtering
- Regime compatibility
- Strategy selection
- Position sizing
- Stop-loss
- Take-profit
- Risk/reward
- Trade filtering
- Strategy monitoring
- Backtesting
- Paper trading
- Performance analysis
- Strategy improvement

It cannot bypass:

- Capital controls
- Risk controls
- Execution validation
- User restrictions
- Portfolio limits
- Exchange constraints

## 06 — CROSS-EXCHANGE ARBITRAGE

The Cross-Exchange Arbitrage System detects and evaluates executable price discrepancies between venues.

It must evaluate real executable economics, not merely displayed prices.

Responsibilities:

- Exchange monitoring
- Price comparison
- Order-book evaluation
- Liquidity analysis
- Fee calculation
- Slippage estimation
- Market-impact analysis
- Latency analysis
- Capital availability
- Exchange health
- Position availability
- True net-profit calculation
- Opportunity ranking
- Execution validation
- Opportunity tracking
- Expected-vs-actual analysis

A displayed price difference is not automatically an arbitrage opportunity.

## 07 — TRIANGULAR ARBITRAGE

The Triangular Arbitrage System identifies executable multi-leg routes.

Example:

```text
Asset A
   ↓
Asset B
   ↓
Asset C
   ↓
Asset A

```

Responsibilities:

- Trading-pair graph construction
- Route discovery
- Route validation
- Profitability calculation
- Fees
- Slippage
- Liquidity
- Execution sequence
- Partial-fill handling
- Route invalidation
- Multi-leg risk
- Execution feasibility
- Expected-vs-actual analysis

## 08 — WHOLE-UNIVERSE OPPORTUNITY MONITORING

The platform must continuously monitor the configured trading universe, not merely a small manually selected list.

The opportunity-monitoring architecture should be capable of scanning relevant supported markets across:

- Exchanges
- Assets
- Trading pairs
- Directional conditions
- Cross-exchange relationships
- Triangular routes
- Liquidity conditions
- Volatility
- Funding
- Market regimes
- Significant events

The purpose is to allow the system to discover opportunities wherever they exist within the authorized universe.

This does not mean blindly processing every possible market event through AI.

The architecture should be:

```text
WHOLE MARKET UNIVERSE
        ↓
DETERMINISTIC MARKET DATA
        ↓
QUANTITATIVE PROCESSING
        ↓
OPPORTUNITY SCANNING
        ↓
FILTERING
        ↓
SIGNIFICANT / EXECUTABLE OPPORTUNITY
        ↓
STRATEGY / RISK / CAPITAL
        ↓
AI ONLY WHEN JUSTIFIED

```

The system must distinguish:

Market Monitoring

“What is happening across the trading universe?”

from:

Operational Monitoring

“Is the platform itself functioning correctly?”

These must remain separate.

## 09 — OPPORTUNITY DETECTION ENGINE

The platform requires a shared opportunity-detection capability.

It should identify:

- Directional opportunities
- Cross-exchange arbitrage
- Triangular arbitrage
- Market-regime changes
- Significant anomalies
- Liquidity changes
- Strategy conditions
- Relevant market events

Deterministic systems perform high-volume screening.

AI is activated only when its reasoning adds meaningful value.

## 10 — MARKET-DATA INFRASTRUCTURE

Market data is foundational shared infrastructure.

Where supported, it should include:

- OHLCV
- Tick/trade data
- Order books
- Bid/ask
- Spread
- Volume
- Funding rates
- Exchange metadata
- Trading-pair metadata
- Timestamps
- Market status
- Execution-related information

Pipeline:

```text
EXCHANGE
   ↓
ADAPTER
   ↓
RAW DATA
   ↓
VALIDATION
   ↓
NORMALIZATION
   ↓
QUALITY CHECKS
   ↓
STORAGE
   ↓
QUANTITATIVE ENGINE
   ↓
STRATEGIES / OPPORTUNITY ENGINE

```

Protect against:

- Invalid timestamps
- Duplicate events
- Missing data
- Out-of-order data
- Corruption
- Look-ahead bias
- Training/validation contamination
- Survivorship bias
- Incorrect symbol mappings
- Precision errors

## 11 — MARKET REGIME ENGINE

The system requires explicit market-regime awareness.

Possible states include:

- Trending
- Ranging
- High volatility
- Low volatility
- Panic/stress
- Uncertain
- UNKNOWN REGIME

The system must not force uncertain conditions into an artificial classification.

A strategy may be rejected when the current regime is incompatible.

## 12 — DETERMINISTIC QUANTITATIVE ENGINE

The Quantitative Engine performs calculations without requiring an LLM.

Examples:

- RSI
- MACD
- ATR
- Moving averages
- Volatility
- Spread
- Returns
- Drawdown
- Exposure
- Position sizing
- Risk/reward
- Correlation
- Liquidity metrics
- Slippage
- Fees
- Arbitrage economics

If a calculation can be performed deterministically, the system should not ask an LLM to perform it.

## 13 — TRUE NET-PROFIT ENGINE

Every opportunity must be evaluated using realistic executable economics.

Conceptually:

```text
GROSS OPPORTUNITY
       -
TRADING FEES
       -
SPREAD
       -
EXPECTED SLIPPAGE
       -
MARKET IMPACT
       -
FUNDING COSTS
       -
REBALANCING / TRANSFER COSTS
       -
OTHER EXECUTION COSTS
       -
SAFETY / UNCERTAINTY MARGIN
       =
TRUE NET EXPECTED RESULT

```

The exact formula must be formally defined.

The platform must never treat displayed percentage differences as guaranteed profit.

## 14 — POSITIVE-NET-PROFIT OPPORTUNITY PRINCIPLE

This is a critical requirement.

The system must not impose an artificial universal minimum profit threshold that prevents it from taking a genuinely executable positive-net opportunity.

For example:

If a fully validated opportunity produces:

```text
TRUE NET EXPECTED PROFIT = +0.1%

```

and all applicable conditions are satisfied:

- Fees included
- Slippage included
- Liquidity sufficient
- Execution feasible
- Risk acceptable
- Capital available
- No higher-priority conflict
- Expected value justifies execution
- Safety margin satisfied

then the system may execute it.

The same applies to:

- +0.2%
- +0.3%
- +0.5%
- +1%
- +2%
- +5%
- or any other positive result that genuinely survives the complete evaluation.

The system must evaluate economics, not an arbitrary percentage label.

## 15 — SMALL-PROFIT ACCUMULATION

Small profitable opportunities may be valuable when they can be executed repeatedly and safely.

Example:

```text
Opportunity 1 → +0.1%
Opportunity 2 → +0.2%
Opportunity 3 → +0.1%
Opportunity 4 → +0.3%
...

```

The system may accumulate these results over time when each individual opportunity is independently valid.

This means the architecture must not assume:

“Only large trades matter.”

The objective is to maximize risk-adjusted executable net profitability, including the cumulative effect of many smaller opportunities.

However, small profit does not automatically mean trade.

The opportunity must still pass:

- Net-profit validation
- Risk controls
- Liquidity requirements
- Execution feasibility
- Capital allocation
- Cost analysis
- Strategy validity
- Safety requirements

## 16 — NO ARTIFICIAL PROFIT CEILING

The platform must not impose a conceptual ceiling such as:

“The system is only allowed to make 1% per day.”

If the market provides multiple valid opportunities and the system can safely execute them, cumulative daily profitability could theoretically exceed previously discussed target percentages.

For example, a day could theoretically produce:

```text
0.1%
+ 0.2%
+ 0.5%
+ 1%
+ 2%
...

```

The system must not interpret this as a guaranteed 5% daily return.

There is:

- No guaranteed daily return
- No fixed daily target
- No fixed daily ceiling
- No assumption that opportunities will always exist

The actual result depends on market conditions, execution, liquidity, fees, risk, and available opportunities.

## 17 — OPPORTUNITY QUALITY

Opportunity quality should be evaluated using multiple dimensions rather than percentage alone.

Possible dimensions:

- True net profitability
- Confidence in market data
- Liquidity
- Slippage
- Market impact
- Execution latency
- Capital requirement
- Risk
- Strategy validity
- Exchange health
- Competition with other opportunities
- Expected repeatability
- Rebalancing requirements
- Safety margin

A percentage threshold may be used as a configurable research/filter parameter, but it must not become a universal hard rule that conflicts with the positive-net-opportunity principle.

## 18 — GLOBAL CAPITAL AUTHORITY

All trading systems must use one authoritative capital state.

It must distinguish:

- Available capital
- Reserved capital
- Capital committed to positions
- Capital committed to pending orders
- Capital allocated to arbitrage
- Capital held in reserve
- Capital by exchange
- Capital by strategy
- Capital pending release
- Capital involved in partial fills

A strategy must never independently assume that capital is available.

## 19 — CAPITAL RESERVATION

Before capital is committed:

```text
OPPORTUNITY
    ↓
CAPITAL REQUEST
    ↓
GLOBAL CAPITAL AUTHORITY
    ↓
RISK CHECK
    ↓
RESERVATION
    ↓
EXECUTION
    ↓
COMMIT / RELEASE

```

Reservations must be correctly released after:

- Rejection
- Cancellation
- Completion
- Failure
- Partial execution
- Recovery

## 20 — DYNAMIC CAPITAL ALLOCATION

The system should determine how available capital can be used most effectively while respecting risk.

It should evaluate:

- Net economics
- Risk
- Liquidity
- Existing exposure
- Capital reserve
- Strategy health
- Correlation
- User policy
- Execution constraints
- Opportunity duration

Capital allocation must optimize capital efficiency under constraints, not maximize exposure.

## 21 — OPPORTUNITY COMPETITION

Different strategies may discover opportunities simultaneously.

```text
DIRECTIONAL
     +
CROSS-EXCHANGE
     +
TRIANGULAR
     ↓
GLOBAL CAPITAL AUTHORITY
     ↓
RISK / EXPOSURE / LIQUIDITY
     ↓
ALLOCATION

```

Theoretical profitability alone must not determine allocation.

## 22 — ARBITRAGE ACCUMULATION AND COMPOUNDING

The arbitrage system should be capable of accumulating realized positive results over time.

The system may use realized profits to increase future available trading capital when permitted by:

- User policy
- Capital-management rules
- Risk limits
- Reserve requirements
- Strategy constraints
- Operational safety

Conceptually:

```text
VALID OPPORTUNITY
      ↓
NET PROFIT
      ↓
REALIZED RESULT
      ↓
ACCOUNTING / LEDGER
      ↓
AVAILABLE CAPITAL
      ↓
FUTURE CAPITAL ALLOCATION
      ↓
NEW OPPORTUNITIES

```

This creates the possibility of compounding.

However:

Compounding is an accounting/capital-allocation mechanism, not a promise of compound returns.

## 23 — ACTIVE TRADE PROTECTION

A new opportunity must not automatically interrupt an existing position merely because it appears theoretically better.

Existing commitments must be respected.

A new opportunity may be rejected because:

- Capital is committed
- Risk budget is committed
- Exposure limits are reached
- Execution resources are constrained
- Existing positions require management
- The opportunity is no longer executable

## 24 — PORTFOLIO MANAGEMENT

The platform requires one centralized portfolio view.

It should track:

- Positions
- Balances
- Exposure
- Unrealized P&L
- Realized P&L
- Allocated capital
- Reserved capital
- Available capital
- Pending orders
- Strategy exposure
- Exchange exposure
- Asset exposure
- Risk exposure

Trading systems consume portfolio state; they do not create competing portfolio truths.

## 25 — DETERMINISTIC RISK ENGINE

Risk enforcement must be deterministic.

Controls may include:

- Position limits
- Exposure limits
- Leverage limits
- Loss limits
- Position sizing
- Slippage limits
- Liquidity requirements
- Capital reserves
- Strategy limits
- Portfolio limits
- Exchange limits
- Correlation controls
- Trade authorization
- Emergency shutdown
- Kill switches

AI cannot bypass these controls.

## 26 — RISK DECISION HIERARCHY

Authority hierarchy:

```text
SYSTEM SAFETY
      ↓
USER HARD CONSTRAINTS
      ↓
PORTFOLIO / RISK POLICY
      ↓
VALIDATED STRATEGY RULES
      ↓
DETERMINISTIC MARKET CONDITIONS
      ↓
AI ANALYSIS / PROPOSAL

```

Lower layers cannot override higher layers.

## 27 — NO-TRADE / UNCERTAINTY SYSTEM

Valid outcomes include:

- TRADE
- WAIT
- NO TRADE
- REDUCE RISK
- SUSPEND STRATEGY
- SAFE MODE
- ROLLBACK
- UNCERTAIN
- I DON'T KNOW

The system must not manufacture confidence when evidence is insufficient.

## 28 — NATURAL LANGUAGE POLICY INTERFACE

The platform should provide a built-in Natural Language Policy Interface through which the user can express trading objectives, restrictions, preferences, and instructions in ordinary language.

Example categories:

### Objectives

“What am I trying to achieve?”

### Restrictions

“What must the system never do?”

### Capital authorization

“How much capital may the system use?”

### Venue authorization

“Which exchanges may be used?”

### Risk preferences

“What level of exposure is permitted?”

### Operating preferences

“How should the system behave within those boundaries?”

The Natural Language Policy Interface is an interface into the policy system, not the policy authority itself.

Architecture:

```text
USER NATURAL LANGUAGE
        ↓
POLICY INTERPRETATION
        ↓
STRUCTURED POLICY
        ↓
VALIDATION
        ↓
CONFLICT / AMBIGUITY CHECK
        ↓
POLICY VERSION
        ↓
DETERMINISTIC ENFORCEMENT

```

The LLM must never silently reinterpret an important instruction into a more permissive policy.

Ambiguous instructions must be surfaced.

## 29 — POLICY IS NOT AI MEMORY

Important user rules must not exist only inside an AI model's context or memory.

They must be stored persistently in structured, versioned policy.

This protects against:

- Context loss
- Model drift
- Session changes
- Accidental omission
- Ambiguity
- Unauthorized changes

## 30 — POLICY VERSIONING

Meaningful policy changes must create a new version.

Example:

```text
Policy v1.0
Policy v1.1
Policy v2.0

```

Important changes should follow:

```text
NEW INSTRUCTION
      ↓
INTERPRETATION
      ↓
DIFFERENCE ANALYSIS
      ↓
CONFLICT CHECK
      ↓
RISK ANALYSIS
      ↓
SIMULATION IF REQUIRED
      ↓
CONFIRMATION IF REQUIRED
      ↓
ACTIVATION

```

## 31 — OPERATING MODES

The platform should support:

### RESEARCH

No real-money trading.

### PAPER

Live/relevant market conditions with simulated capital.

### SUPERVISED

Trade proposals require authorization according to configured policy.

### AUTONOMOUS LIVE

Authorized trading executes automatically within policy and deterministic controls.

Transitions must be controlled and auditable.

## 32 — PAPER TRADING

Paper trading should use the production architecture as realistically as practical.

It should account for:

- Fees
- Spread
- Slippage
- Liquidity
- Latency
- Partial fills
- Rejections
- Position management
- Risk
- Capital reservation
- Portfolio interaction
- Opportunity competition
- Directional trading
- Cross-exchange arbitrage
- Triangular arbitrage

## 33 — BACKTESTING

Backtesting must support:

- Historical data
- Strategy execution
- Fees
- Slippage
- Liquidity
- Position management
- Risk
- Capital constraints
- Portfolio interaction
- Opportunity competition where applicable

Protect against:

- Look-ahead bias
- Data leakage
- Survivorship bias
- Training/test contamination
- Unrealistic execution assumptions

Backtesting alone does not authorize production.

## 34 — STRATEGY LIFECYCLE

```text
RESEARCH
   ↓
STRATEGY SPECIFICATION
   ↓
BACKTEST
   ↓
VALIDATION
   ↓
OUT-OF-SAMPLE / WALK-FORWARD
   ↓
STRESS / ROBUSTNESS
   ↓
PAPER
   ↓
APPROVAL
   ↓
CANARY
   ↓
PRODUCTION

```

No strategy bypasses required stages because an AI recommends it.

## 35 — STRATEGY FACTORY

Responsibilities:

- Research
- Hypothesis generation
- Candidate creation
- Backtesting
- Validation
- Robustness
- Paper testing
- Comparison
- Versioning
- Promotion
- Retirement

It must not directly modify live trading.

## 36 — STRATEGY VERSION CONTROL

Every meaningful strategy change creates a new version.

Examples:

```text
Directional Trend v1.0
Directional Trend v1.1
Directional Trend v2.0

```

Active production strategies must never be silently modified.

## 37 — RESEARCH / PRODUCTION SEPARATION

Research may:

- Analyze history
- Generate hypotheses
- Create candidate strategies
- Backtest
- Stress-test
- Paper-test

Research must not directly modify:

- Live strategies
- Production risk limits
- Exchange credentials
- Execution logic
- User hard constraints
- Kill switches

## 38 — CONTROLLED STRATEGY IMPROVEMENT

When a strategy deteriorates:

```text
PERFORMANCE DETERIORATION
        ↓
INVESTIGATION
        ↓
RESEARCH
        ↓
HYPOTHESIS
        ↓
NEW STRATEGY VERSION
        ↓
BACKTEST
        ↓
OUT-OF-SAMPLE
        ↓
ROBUSTNESS
        ↓
PAPER
        ↓
APPROVAL
        ↓
CANARY
        ↓
PRODUCTION

```

Never:

```text
LOSS
 ↓
AI CHANGES LIVE STRATEGY
 ↓
RISK INCREASES

```

## 39 — EXECUTION ENGINE

The Execution Engine is deterministic.

Responsibilities:

- Order validation
- Exchange rules
- Quantity precision
- Price precision
- Minimum orders
- Order construction
- Submission
- Monitoring
- Fill handling
- Partial fills
- Cancellation
- Reconciliation
- Retry handling
- Execution-state management

The system must never trust an AI statement that an order succeeded.

## 40 — STALE DECISION PROTECTION

Before execution:

```text
OPPORTUNITY
   ↓
ANALYSIS
   ↓
PROPOSAL
   ↓
MARKET CHANGES
   ↓
REVALIDATION
   ↓
VALID?
 ┌───────┴───────┐
YES             NO
 ↓               ↓
EXECUTE       REJECT/RECALCULATE

```

## 41 — IDEMPOTENT EXECUTION

A timeout does not prove an order failed.

Correct behavior:

```text
ORDER SUBMISSION
      ↓
NETWORK TIMEOUT
      ↓
DO NOT BLINDLY RESUBMIT
      ↓
QUERY EXCHANGE
      ↓
DETERMINE ACTUAL STATE
      ↓
RECONCILE
      ↓
CONTINUE SAFELY

```

This prevents duplicate orders.

## 42 — EXCHANGE ADAPTER ARCHITECTURE

Use standardized exchange adapters.

Previously discussed examples include:

- Binance
- OKX
- Coinbase

Adapters should handle:

- Authentication
- Market data
- Account data
- Orders
- Fills
- Balances
- Positions
- Precision
- Rate limits
- Errors
- Connectivity
- Exchange-specific capabilities

The rest of the platform should use standardized interfaces.

## 43 — ARBITRAGE INTELLIGENCE

Arbitrage-specific capabilities include:

- Opportunity discovery
- True net-profit calculation
- Liquidity intelligence
- Opportunity ranking
- Arbitrage-specific risk
- Opportunity database
- Capital reserve
- Dynamic capital allocation
- Rebalancing intelligence
- Kill switch
- Performance controller
- Expected-vs-actual analysis

It must reuse shared infrastructure.

## 44 — ARBITRAGE OPPORTUNITY DATABASE

Record:

- Detected opportunities
- Executed opportunities
- Rejected opportunities
- Rejection reasons
- Expected profitability
- Actual profitability
- Fees
- Slippage
- Liquidity
- Execution latency
- Capital used
- Capital unavailable
- Rebalancing costs
- Failure reasons

This supports learning and expected-vs-actual analysis.

## 45 — INTELLIGENT REBALANCING

The system must not automatically transfer assets after every arbitrage trade.

It should evaluate:

- Current balances
- Future opportunities
- Transfer costs
- Network fees
- Transfer time
- Exchange liquidity
- Capital efficiency
- Expected opportunities
- Reserve requirements
- Risk

Rebalancing is a capital-management decision.

## 46 — ARBITRAGE CAPITAL RESERVE

Arbitrage must maintain sufficient reserves where required to execute necessary legs and manage existing commitments.

The reserve must integrate with the Global Capital Authority.

No hidden arbitrage capital state is permitted.

## 47 — ARBITRAGE KILL SWITCH

Possible triggers:

- Exchange instability
- Abnormal execution failures
- Liquidity collapse
- Unexpected spreads
- Repeated losses
- Reconciliation problems
- API instability
- Market anomalies
- Capital inconsistency

The global safety architecture remains authoritative.

## 48 — EXPECTED VS ACTUAL PERFORMANCE

Compare expected versus actual:

- Profitability
- Fees
- Slippage
- Execution price
- Latency
- Fill rate
- Liquidity
- Rebalancing cost
- Strategy performance

This is particularly important for arbitrage.

## 49 — PERFORMANCE CONTROLLER

The platform should continuously compare actual results against expected behavior.

It should detect:

- Strategy deterioration
- Execution degradation
- Unexpected fees
- Increasing slippage
- Reduced liquidity
- Opportunity-quality deterioration
- Model degradation
- Exchange degradation
- Infrastructure degradation

The controller should recommend or trigger only actions permitted by deterministic policy.

## 50 — MODEL HEALTH VS STRATEGY HEALTH

These are separate.

### Model Health

AI model reliability, cost, latency, calibration, hallucination rate, and task performance.

### Strategy Health

Trading strategy effectiveness under market conditions.

A healthy model does not imply a healthy strategy.

A healthy strategy does not imply a healthy AI model.

## 51 — AI INTELLIGENCE LAYER

AI responsibilities may include:

- Market interpretation
- Research
- Strategy discovery
- Hypothesis generation
- Backtest interpretation
- News analysis
- Sentiment
- Complex reasoning
- Strategy improvement proposals
- Failure investigation
- Performance interpretation
- Research coordination

AI proposes and analyzes.

Deterministic infrastructure enforces.

## 52 — AI HARD-SAFETY BOUNDARY

AI must not:

- Bypass risk
- Increase authorized risk
- Disable kill switches
- Override user hard restrictions
- Submit unrestricted arbitrary orders
- Deploy unvalidated strategies
- Modify protected test boundaries
- Assume unsupported claims are facts
- Assume execution succeeded
- Receive unrestricted secrets

## 53 — EVENT-DRIVEN AI ACTIVATION

AI must not inspect every market tick unnecessarily.

Preferred architecture:

```text
HIGH-VOLUME MARKET EVENTS
          ↓
DETERMINISTIC PROCESSING
          ↓
FILTERING
          ↓
SIGNIFICANT EVENT
          ↓
AI REASONING IF JUSTIFIED

```

## 54 — AI AGENT ORGANIZATION

Previously discussed AI responsibilities include:

1. Market Analyst
2. Quant Research Agent
3. Strategy Research Agent
4. Trading Director
5. Devil's Advocate
6. Performance Analyst
7. Strategy Optimizer
8. Model Evaluation Agent
9. Research Agent
10. AI Cost Manager
11. News/Sentiment Agent

Claude must identify overlapping responsibilities before implementation.

The project must not create multiple agents doing essentially the same job without an explicit architectural reason.

## 55 — TRADING DIRECTOR

The Trading Director generates structured trade proposals.

It may receive:

- Market state
- Quantitative features
- Regime
- Liquidity
- Volatility
- News
- Strategy state
- Portfolio state
- Existing positions
- Policy
- Risk state

It may propose:

- Asset
- Action
- Strategy
- Strategy version
- Entry
- Stop
- Target
- Size
- Confidence
- Evidence
- Invalidation conditions
- Risk observations

The deterministic system validates the proposal.

## 56 — DEVIL'S ADVOCATE

The Devil's Advocate challenges proposals.

It should examine:

- False signals
- Weak volume
- Conflicting evidence
- Liquidity
- Spread
- Volatility
- News risk
- Manipulation risk
- Regime mismatch
- Risk/reward
- Invalid assumptions
- Strategy deterioration

It must be able to reject a proposal.

## 57 — MARKET ANALYST

The Market Analyst interprets relevant market context.

Responsibilities may include:

- Market context
- Regime interpretation
- Event interpretation
- Cross-market relationships
- Relevant news
- Higher-level reasoning

It must not replace deterministic quantitative calculations.

## 58 — QUANT RESEARCH AGENT

Assists with:

- Quantitative research
- Hypothesis generation
- Feature exploration
- Backtest interpretation
- Statistical investigation
- Strategy research

It does not replace the deterministic Quantitative Engine.

## 59 — STRATEGY RESEARCH / OPTIMIZATION

AI may:

- Generate candidates
- Analyze historical behavior
- Suggest improvements
- Compare variants
- Investigate deterioration
- Propose hypotheses

Every resulting strategy must pass the formal lifecycle.

## 60 — PERFORMANCE ANALYST

Evaluates:

- Strategy performance
- Trade outcomes
- Drawdown
- Execution quality
- Expected vs actual
- Opportunity quality
- Strategy deterioration
- Missed opportunities
- Model contribution

It must distinguish:

```text
STRATEGY PROBLEM
vs
EXECUTION PROBLEM
vs
MARKET PROBLEM
vs
DATA PROBLEM
vs
MODEL PROBLEM
vs
INFRASTRUCTURE PROBLEM

```

## 61 — MODEL EVALUATION

Evaluate:

- Accuracy
- Reliability
- Calibration
- Cost
- Latency
- Failure patterns
- Hallucination frequency
- Task suitability

Do not confuse model performance with trading profitability.

## 62 — AI COST MANAGER

Monitor:

- API usage
- Cost per task
- Cost per model
- Cost per event
- Budget utilization
- Model routing
- Excessive calls
- Repeated calls
- Unnecessary premium-model usage

## 63 — MODEL ROUTER

The Model Router determines whether a task requires:

```text
NO AI
   OR
LOW-COST AI
   OR
PREMIUM AI

```

Consider:

- Task difficulty
- Financial consequence
- Context complexity
- Reliability
- Current model performance
- Cost
- Latency
- Budget
- Expected value

## 64 — HALLUCINATION FIREWALL

Important AI claims should reference:

- Data source
- Timestamp
- Dataset
- Calculation
- Event
- Evidence identifier

If evidence cannot be verified:

```text
UNVERIFIED

```

Unverified claims cannot become factual trading evidence.

## 65 — STRUCTURED AI OUTPUT CONTRACT

AI output must be machine-validated.

Conceptual schema:

```text
Decision:
BUY / SELL / HOLD / NO_TRADE

Confidence:
0–100

Evidence:
[]

Invalidation:
[]

RiskObservations:
[]

Strategy:
ID + VERSION

Reasoning:
Structured explanation

```

Malformed or incomplete output must be rejected.

## 66 — MULTI-AGENT VALIDATION

For important decisions:

```text
MARKET ANALYSIS
       ↓
QUANTITATIVE ANALYSIS
       ↓
TRADING DIRECTOR
       ↓
DEVIL'S ADVOCATE
       ↓
DETERMINISTIC RISK ENGINE

```

Possible policies:

- Single-agent analysis
- Multi-agent agreement
- Mandatory Devil's Advocate
- Premium confirmation
- No trade on unresolved disagreement

Risk remains authoritative.

## 67 — AI CONFIDENCE CALIBRATION

AI confidence must not automatically be interpreted as probability.

Compare:

```text
AI CONFIDENCE
     vs
OBSERVED OUTCOMES

```

If systematic overconfidence occurs, the system may:

- Require stronger evidence
- Require additional validation
- Route to another model
- Reduce the model's role
- Suspend the model for that task

## 68 — AI MEMORY / PROJECT KNOWLEDGE

Important persistent project knowledge must not depend solely on temporary AI context.

The platform should have a clearly defined knowledge/memory architecture where required for:

- Strategy history
- Model evaluations
- Research findings
- Previous decisions
- Policy history
- System state
- Important lessons
- Validated constraints

Memory must be:

- Persistent
- Traceable
- Versioned where appropriate
- Scoped
- Auditable
- Protected against accidental contamination

Memory must not become an uncontrolled second source of truth.

Authoritative requirements remain in the appropriate canonical repository/system.

## 69 — CONSISTENCY / ANTI-DRIFT ARCHITECTURE

The platform must preserve consistency as the project grows.

The architecture should maintain:

- Canonical definitions
- Versioned requirements
- Explicit ownership
- Traceability
- Dependency mapping
- Conflict detection
- Decision records
- Strategy versions
- Policy versions
- Model versions
- Interface contracts

Changes must be checked against existing architecture before acceptance.

## 70 — DATA / COMPUTATION / STRATEGY / AI / RISK / EXECUTION SEPARATION

Canonical conceptual flow:

```text
DATA
 ↓
QUANTITATIVE COMPUTATION
 ↓
OPPORTUNITY
 ↓
STRATEGY
 ↓
AI REASONING
 ↓
CAPITAL / RISK
 ↓
EXECUTION
 ↓
EXTERNAL VENUE
 ↓
RECONCILIATION
 ↓
PORTFOLIO STATE

```

Each layer must have explicit responsibility.

No layer silently assumes another layer's authority.

## 71 — RECOVERY AND RECONCILIATION

The platform must assume external reality can change while offline.

Recovery:

```text
SYSTEM RESTART
      ↓
LOAD VERIFIED INTERNAL STATE
      ↓
VERIFY DATABASE
      ↓
CONNECT EXTERNAL SYSTEMS
      ↓
CHECK EXCHANGES
      ↓
FETCH BALANCES
      ↓
FETCH POSITIONS
      ↓
FETCH OPEN ORDERS
      ↓
FETCH FILLS
      ↓
RECONCILE
      ↓
RESOLVE MISMATCHES
      ↓
REFRESH MARKET DATA
      ↓
VALIDATE RISK
      ↓
VALIDATE CAPITAL
      ↓
VALIDATE POLICY
      ↓
VALIDATE STRATEGY STATE
      ↓
SAFE RESUME

```

## 72 — SAFE RESUME

Restarting does not automatically authorize trading.

Before resuming:

- Data integrity
- Exchange connectivity
- Account state
- Balance state
- Position state
- Order state
- Capital state
- Risk state
- Strategy state
- Policy state
- System health

must be established.

## 73 — ACTIVE TRADE RECOVERY

After interruption determine:

- Open positions
- Filled orders
- Partial fills
- Cancelled orders
- Triggered stops/targets
- Actual execution prices
- Balances
- Exposure
- Market conditions
- Strategy validity
- Emergency requirements

Never simply restore an old in-memory state.

## 74 — SYSTEM HEALTH STATE MACHINE

Possible states:

- STARTING
- HEALTHY
- DEGRADED
- WARNING
- RECOVERING
- SAFE MODE
- TRADING HALTED
- EXCHANGE DEGRADED
- DATA DEGRADED
- AI DEGRADED
- EMERGENCY
- STOPPED

The final state machine must be formalized during architecture implementation.

## 75 — CONTINUOUS OPERATION

The production system must support long-running operation under:

- High event volumes
- Large trade histories
- Increasing strategy count
- Increasing market universe
- AI provider failures
- Exchange rate limits
- Network failures
- Component restarts

## 76 — PERFORMANCE AS A FIRST-CLASS REQUIREMENT

Performance must be considered from architecture design.

The platform should be:

- Fast where latency matters
- Efficient
- Correct under concurrency
- Stable under load
- Scalable
- Resource-conscious
- Resistant to bottlenecks

## 77 — LATENCY-SENSITIVE PATH

```text
MARKET EVENT
    ↓
DATA VALIDATION
    ↓
FEATURE / SIGNAL PROCESSING
    ↓
OPPORTUNITY DETECTION
    ↓
STRATEGY EVALUATION
    ↓
RISK CHECK
    ↓
EXECUTION VALIDATION
    ↓
EXCHANGE ORDER

```

AI should not unnecessarily block latency-sensitive execution.

## 78 — PERFORMANCE ENGINEERING

Where justified:

- Event-driven processing
- Async processing
- Parallel processing
- Efficient data structures
- Caching
- Batching
- Precomputation
- Incremental calculations
- Connection reuse
- Concurrency controls
- Efficient persistence
- Backpressure
- Queues
- Work prioritization
- Resource isolation

Technology choices must be based on measured requirements.

## 79 — NUMERICAL PRECISION

Financial calculations must be deterministic and precise.

Includes:

- Prices
- Quantities
- Fees
- Slippage
- P&L
- Position sizing
- Exposure
- Leverage
- Risk
- Reservations
- Arbitrage economics
- Portfolio accounting

Exchange-specific precision must be respected.

## 80 — OPERATIONAL READINESS

Operational readiness is not the same as total project completion.

```text
OPERATIONAL READINESS
        ≠
PROJECT COMPLETION

```

A completed subsystem can become operational while unrelated development continues, provided production boundaries remain protected.

## 81 — DEVELOPMENT WHILE ONLINE

After an approved operational milestone:

- Development may continue.
- Production paths remain protected.
- New features remain isolated until verified.
- Deployments are controlled.
- Versioning is explicit.
- Rollback exists.
- Database changes are compatible.
- Shared infrastructure changes are tested.
- New functionality passes required gates before activation.

## 82 — PLATFORM SAFETY PRIORITY

The project's conceptual hierarchy is:

1. Capital Preservation
2. Risk Control
3. Execution Safety
4. Positive Net Profitability
5. Capital Efficiency
6. Compounding / Growth
7. Opportunity Targets

Higher priorities cannot be overridden by lower ones.

## 83 — NO GUARANTEED RETURNS

The platform must never assume:

- Fixed profit per trade
- Fixed daily return
- Guaranteed arbitrage profit
- Guaranteed strategy performance
- Guaranteed AI accuracy

The system is not constrained to a fixed daily percentage either.

Its objective is:

Maximize risk-adjusted, executable, net profitability while preserving capital and avoiding unnecessary exposure.

## 84 — PLATFORM ACCOUNT / CUSTODY ARCHITECTURE

A previously discussed architecture involved:

```text
USER
 ↓
PLATFORM ACCOUNT
 ↓
AUTHORIZED CAPITAL
 ↓
CONTROLLED TRADING INFRASTRUCTURE
 ↓
SUPPORTED VENUES / WALLETS
 ↓
EXECUTION

```

This remains classified as:

Previously discussed architecture / requires formal confirmation before becoming a final production requirement.

If retained, it requires:

- Custody
- Wallet management
- Deposit monitoring
- Blockchain monitoring
- Double-entry ledger
- Internal balances
- Reconciliation
- Withdrawal controls
- Security
- Key management
- Compliance architecture
- Exchange-account management

Claude must not silently assume this model is approved.

## 85 — LEDGER / ACCOUNTING FOUNDATION

If the platform becomes a user-facing capital platform, internal accounting must be authoritative.

Potential requirements:

- Deposits
- Withdrawals
- Trading
- Fees
- Realized P&L
- Internal transfers
- Capital allocation
- Reservations
- User balances
- Venue balances

Temporary trading-engine state must not become the authoritative financial ledger.

## 86 — AUDITABILITY

Important actions must be traceable.

Record where applicable:

- What happened
- When
- Which system acted
- Strategy
- Strategy version
- Policy version
- Model/agent
- Evidence
- Risk checks
- Capital reservation
- Execution
- External venue confirmation
- Final outcome

## 87 — EVENT AND DECISION HISTORY

Preserve meaningful events:

- Opportunity detected
- Opportunity rejected
- Trade proposed
- Risk rejection
- Capital unavailable
- Order submitted
- Order filled
- Partial fill
- Cancellation
- Exchange failure
- Recovery
- Strategy suspension
- Strategy promotion
- Strategy retirement
- Policy change
- Model change
- AI disagreement
- Kill-switch activation

## 88 — MONITORING AND OBSERVABILITY

### Trading

- Trades
- P&L
- Exposure
- Strategy performance
- Opportunity activity

### Infrastructure

- CPU
- Memory
- Latency
- Queue depth
- Database health
- API health

### Exchanges

- Connectivity
- Rate limits
- Errors
- Order failures
- Market-data health

### AI

- Calls
- Latency
- Cost
- Errors
- Confidence
- Validation failures

### Risk

- Rejections
- Exposure
- Limits
- Kill switches
- Safe mode

### Recovery

- Reconciliation
- State mismatches
- Recovery events

## 89 — SECURITY ARCHITECTURE

Protect:

- Exchange credentials
- API keys
- Secrets
- Wallet keys where applicable
- User accounts
- Trading permissions
- Financial records
- Audit records
- AI access
- Administrative operations

AI agents must not receive unrestricted credentials.

## 90 — FAILURE IS AN EXPECTED STATE

Potential failures:

- Market-data failure
- Exchange API failure
- Network failure
- Database failure
- AI provider failure
- Model failure
- Execution timeout
- Partial fill
- State inconsistency
- Resource exhaustion
- Process crash

The system must fail safely rather than fail creatively.

## 91 — CONTROLLED DEGRADATION

Example:

```text
AI UNAVAILABLE
      ↓
DETERMINISTIC CAPABILITIES CONTINUE
WHERE SAFE

```

or:

```text
EXCHANGE UNAVAILABLE
      ↓
VENUE RESTRICTED
      ↓
AFFECTED STRATEGIES RESTRICTED
      ↓
OTHER SAFE CAPABILITIES MAY CONTINUE

```

Failure behavior must be defined per subsystem.

## 92 — SYSTEM BOUNDARY PRINCIPLE

Every system must define:

- Purpose
- Responsibility
- Inputs
- Outputs
- Dependencies
- Interfaces
- Data owned
- Data consumed
- Data produced
- Allowed actions
- Forbidden actions
- Failure behavior
- Tests
- Roadmap stage

## 93 — FEATURE OWNERSHIP

For every feature:

```text
WHAT RESPONSIBILITY?
        ↓
WHICH SYSTEM OWNS IT?
        ↓
WHICH DOCUMENT DEFINES IT?
        ↓
WHICH MODULE IMPLEMENTS IT?
        ↓
WHICH REQUIREMENT TRACKS IT?
        ↓
WHICH ROADMAP STAGE?
        ↓
WHICH TEST VERIFIES IT?

```

This prevents duplicate implementation.

## 94 — FEATURE DEPENDENCY

Dependencies must be respected.

Example:

```text
EXCHANGE ADAPTER
      ↓
MARKET DATA
      ↓
QUANTITATIVE ENGINE
      ↓
OPPORTUNITY DETECTION
      ↓
STRATEGY
      ↓
RISK
      ↓
CAPITAL
      ↓
EXECUTION
      ↓
PORTFOLIO / RECONCILIATION

```

## 95 — ROADMAP STAGE CLASSIFICATION

At minimum:

### FOUNDATION

- Repository
- Documentation
- Requirements
- Architecture
- Interfaces
- Configuration
- Security foundation
- Testing foundation
- Traceability

### DATA FOUNDATION

- Exchange adapters
- Market-data ingestion
- Validation
- Normalization
- Storage
- Market universe
- Quantitative engine
- Regime engine
- Opportunity monitoring

### CORE TRADING FOUNDATION

- Portfolio
- Capital Authority
- Capital reservation
- Risk
- Opportunity economics
- Execution
- Reconciliation

### DIRECTIONAL TRADING

- Directional strategies
- Signals
- Entry/exit
- Position management
- Strategy lifecycle
- Backtesting
- Paper trading

### ARBITRAGE

- Cross-exchange
- Triangular
- Liquidity intelligence
- True net-profit calculation
- Opportunity database
- Rebalancing
- Capital reserve
- Accumulation
- Arbitrage risk
- Performance controller

### AI INTELLIGENCE

- AI gateway
- Natural Language Policy Interface
- Model router
- Agents
- Trading Director
- Devil's Advocate
- Hallucination Firewall
- Multi-agent validation
- AI cost management
- AI memory/knowledge

### OPERATIONALIZATION

- Monitoring
- Recovery
- Reconciliation
- Reporting
- Performance engineering
- Deployment
- Canary
- Live operation

Exact sequencing must be finalized in the master roadmap after dependency analysis.

## 96 — FEATURE STATUS CLASSIFICATION

Every feature must be classified as:

- CONFIRMED REQUIREMENT
- CONFIRMED ARCHITECTURAL PRINCIPLE
- CONSTRAINT
- SYSTEM REQUIREMENT
- PROPOSED
- FUTURE
- PREVIOUSLY DISCUSSED / REQUIRES CONFIRMATION
- OPEN QUESTION
- TECHNICAL CONCERN
- DEPRECATED / REPLACED

No silent classification changes.

## 97 — DUPLICATION CONTROL

Shared capability must be implemented once where appropriate.

Example:

```text
Directional Trading
        ↓
       RISK
        ↑
    Arbitrage

```

Both consume the shared Risk Engine.

Likewise:

- Capital
- Execution
- Portfolio
- Market data
- Quantitative calculations
- Monitoring
- Storage
- Recovery

must not be unnecessarily duplicated.

## 98 — CANONICAL SOURCE OF TRUTH

Major domains require authoritative locations.

Example:

```text
Risk
→ docs/risk/

Directional Trading
→ docs/systems/directional-trading.md

Arbitrage
→ docs/systems/arbitrage/

AI
→ docs/ai/

Execution
→ docs/systems/execution-engine.md

Capital
→ docs/systems/capital-management.md

Policy
→ docs/product/trading-policy.md
→ docs/systems/policy/

Roadmap
→ docs/roadmap/

Requirements
→ docs/requirements/

Architecture Decisions
→ docs/decisions/

```

Other documents should reference the authoritative source.

## 99 — REPOSITORY ORGANIZATION TARGET

Claude must derive the final structure from the actual repository, architecture, and handoffs.

A conceptual target is:

```text
/
├── docs/
│   ├── README.md
│   ├── product/
│   ├── requirements/
│   ├── architecture/
│   ├── systems/
│   │   ├── directional/
│   │   ├── arbitrage/
│   │   ├── market-data/
│   │   ├── exchanges/
│   │   └── recovery/
│   ├── ai/
│   │   └── agents/
│   ├── risk/
│   ├── security/
│   ├── operations/
│   ├── roadmap/
│   ├── decisions/
│   ├── conflicts/
│   ├── open-questions/
│   └── traceability/
│
└── implementation/

```

This is not an instruction to blindly create every folder.

Claude must derive the actual structure from:

1. Complete handoff
2. Canonical architecture
3. Repository state
4. Responsibility boundaries
5. Dependencies
6. Duplicate analysis
7. Conflict analysis

## 100 — DOCUMENTATION-FIRST COMPLETION GATE

After processing Part 1, Claude should be able to answer from the repository:

- What is the platform?
- What are its major trading systems?
- What infrastructure is shared?
- What is deterministic?
- What belongs to AI?
- Where does capital authority live?
- Where does risk authority live?
- Where does execution authority live?
- How does the Natural Language Policy Interface work conceptually?
- How are user instructions converted into enforceable policy?
- How does the system monitor the whole trading universe?
- How does it evaluate small positive opportunities?
- How does accumulation work?
- Is there an artificial daily-profit ceiling?
- How are strategies promoted?
- What happens after interruption?
- What happens after an execution timeout?
- How are AI models controlled?
- How are duplicate systems prevented?
- Where does every major feature belong?
- Which features depend on which others?
- Which requirements are confirmed?
- Which require confirmation?
- What remains for Part 2?

If these questions cannot be answered from the repository, the documentation foundation is incomplete.

## 101 — PART 1 DOES NOT AUTHORIZE IMPLEMENTATION

The processing sequence is:

```text
PART 1 RECEIVED
       ↓
ANALYZE
       ↓
CLASSIFY
       ↓
ORGANIZE
       ↓
PLACE INTO AUTHORITATIVE REPOSITORY FILES
       ↓
REGISTER REQUIREMENTS
       ↓
CREATE TRACEABILITY
       ↓
MAP TO ROADMAP
       ↓
CHECK DEPENDENCIES
       ↓
CHECK DUPLICATES
       ↓
CHECK CONFLICTS
       ↓
DOCUMENT UNCERTAINTIES
       ↓
WAIT FOR PART 2
       ↓
COMPLETE DOCUMENTATION REVIEW
       ↓
HUMAN APPROVAL
       ↓
ONLY THEN BEGIN IMPLEMENTATION

```

Receiving this handoff is not permission to build the trading system.

## 102 — PART 1 EXPECTED DOCUMENTATION COVERAGE

Part 1 must result in authoritative documentation covering, where applicable:

- Platform identity
- Platform objective
- Multi-strategy architecture
- Directional trading
- Cross-exchange arbitrage
- Triangular arbitrage
- Shared infrastructure
- Whole-universe market monitoring
- Opportunity monitoring
- Market data
- Market regime
- Quantitative engine
- Opportunity detection
- True net-profit calculation
- Small positive opportunity execution
- Opportunity accumulation
- Capital authority
- Capital reservation
- Dynamic capital allocation
- Opportunity competition
- Portfolio management
- Risk
- No-trade/uncertainty
- Natural Language Policy Interface
- Persistent policy
- Policy versioning
- Operating modes
- Paper trading
- Backtesting
- Strategy lifecycle
- Strategy factory
- Strategy improvement
- Execution
- Stale-decision protection
- Idempotent execution
- Exchange architecture
- Arbitrage intelligence
- Arbitrage opportunity database
- Intelligent rebalancing
- Arbitrage reserves
- Arbitrage kill switch
- Expected-vs-actual performance
- Performance controller
- AI architecture
- AI agents
- AI memory/knowledge
- AI consistency/anti-drift
- Model routing
- AI cost management
- Hallucination Firewall
- Structured AI outputs
- Multi-agent validation
- AI confidence calibration
- Recovery
- Reconciliation
- Safe resume
- Monitoring
- Observability
- Performance engineering
- Numerical precision
- Security
- Auditability
- Failure handling
- Controlled degradation
- System boundaries
- Feature ownership
- Dependencies
- Roadmap classification
- Requirement classification
- Duplicate prevention
- Canonical sources of truth

No major feature from this handoff may be silently dropped.

## 103 — PART 1 FINAL COMPLETION CONDITION

Part 1 is documented, not implemented, only when:

- Every major feature has an authoritative location.
- Every major system has a clear owner.
- Shared infrastructure is distinguished from system-specific behavior.
- Dependencies are recorded.
- Requirements are registered.
- Roadmap relationships exist.
- Duplicate responsibilities are identified.
- Conflicts are identified.
- Unresolved questions are recorded.
- Previously discussed but unconfirmed features are clearly marked.
- Cross-references exist.
- Documentation indexes are updated.
- No feature has been silently dropped.
- The small-profit accumulation principle is documented.
- Whole-universe opportunity monitoring is documented.
- Natural-language policy control is documented.
- No artificial daily-profit ceiling is introduced.
- No artificial universal minimum-profit rule contradicts the positive-net-opportunity requirement.

Final state:

```text
DOCUMENTATION FOUNDATION
        ↓
REQUIREMENTS
        ↓
ARCHITECTURE
        ↓
SYSTEM SPECIFICATIONS
        ↓
TRACEABILITY
        ↓
ROADMAP
        ↓
VALIDATION
        ↓
HUMAN REVIEW
        ↓
APPROVAL
        ↓
ONLY THEN: IMPLEMENTATION

```

## FINAL PART 1 STATUS

PART 1 = CORE PLATFORM FEATURES, SYSTEMS, CAPITAL/RISK/EXECUTION FOUNDATIONS, OPPORTUNITY MONITORING, ARBITRAGE ECONOMICS, AI ARCHITECTURE, POLICY INTERFACE, RECOVERY, PERFORMANCE, SECURITY, AND CANONICAL FEATURE ORGANIZATION.

Part 2 will cover the remaining detailed project requirements, deeper subsystem specifications, interfaces/contracts, complete dependency mapping, implementation-stage mapping, verification architecture, and remaining production requirements.

Do not interpret Part 1 as authorization to begin building the trading system.
