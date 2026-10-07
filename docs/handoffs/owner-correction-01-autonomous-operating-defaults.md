# REQUIRED CORRECTION — COMPANY-GRADE AUTONOMOUS OPERATING DEFAULTS

> **Status:** HISTORICAL — source input: an owner directive received 2026-09-30, replacing the operating defaults recorded earlier. This is **not** an active source of truth.
>
> Its content is applied through [DEC-019](../decisions/DEC-019-company-grade-autonomous-operating-model.md) (items 1–30, 32–33) and [DEC-020](../decisions/DEC-020-value-classification.md) (item 31). Each decision record maps every item to the requirements it produced.
>
> **Formatting note:** converted from plain text to Markdown (headings, lists, paragraph breaks). No wording was added, removed, or changed. Item numbers (1–33) are the directive's own and are used as source references ("OC-1 item N"). The owner sent it with the covering line "here is my Defaults you may want to check answers", which is not reproduced below (noted on 2026-10-06 by the [quality audit](../traceability/quality-audit-2026-10-06.md)).

The previously recorded defaults under “Defaults you may want to check” must be revised.

The project is intended to become a production-grade autonomous financial platform capable of operating 24/7, not a manually supervised trading bot.

The following decisions supersede the weaker defaults previously recorded.

These are architectural requirements and operating principles. They must be incorporated into the appropriate authoritative documentation, requirements registry, architecture, risk model, deployment model, and roadmap.

## 1. INTELLIGENT AUTONOMOUS REBALANCING

The previous default:

“Each rebalancing transfer requires user confirmation.”

is not the intended final architecture.

The platform must be capable of making autonomous rebalancing decisions when doing so is authorized by policy and economically justified.

The objective is not:

Ask the user every time funds should move.

The objective is:

The system should intelligently determine when rebalancing is necessary, economically beneficial, safe, and authorized, and execute it automatically within strict predefined boundaries.

Rebalancing decision flow

```text
VENUE INVENTORY STATE
↓
CAPITAL REQUIREMENTS
↓
CURRENT RESERVES
↓
EXPECTED OPPORTUNITY DISTRIBUTION
↓
LIQUIDITY REQUIREMENTS
↓
FUTURE OPPORTUNITY FORECAST / EXPECTED VALUE
↓
TRANSFER COST
↓
TRANSFER TIME
↓
NETWORK CONDITIONS
↓
VENUE HEALTH
↓
RISK
↓
CAPITAL POLICY
↓
REBALANCING POLICY
↓
TRUE ECONOMIC BENEFIT
↓
AUTONOMOUS REBALANCING DECISION
├── NO TRANSFER
├── WAIT
├── SCHEDULE
└── EXECUTE TRANSFER
```

The platform should not move funds simply because balances are unequal.

Likewise, it should not refuse to move funds merely because a human is unavailable.

It must evaluate whether moving funds improves the system's ability to operate profitably and safely.

## 2. REBALANCING MUST BE ECONOMICALLY INTELLIGENT

Before executing a transfer, the system should consider:

- Current inventory
- Required reserve
- Available capital
- Reserved capital
- Expected opportunity flow
- Venue-specific capital requirements
- Transfer fees
- Network fees
- Transfer latency
- Blockchain/network conditions
- Venue liquidity
- Expected future opportunity value
- Risk
- Capital efficiency
- Minimum reserve requirements
- Maximum transfer limits
- Transfer frequency limits
- Operational health
- Exchange availability

The system should calculate whether:

```text
EXPECTED BENEFIT
>
TRANSFER COST + RISK COST + OPPORTUNITY COST
```

before transferring.

A transfer should not occur merely because the mathematical balance between exchanges is uneven.

## 3. AUTONOMOUS REBALANCING MUST REMAIN BOUNDED

Autonomous does not mean unrestricted.

The platform must operate within explicit controls such as:

- Maximum transfer amount
- Maximum daily transfer amount
- Minimum venue reserve
- Maximum venue exposure
- Approved destination venues
- Approved source venues
- Approved assets
- Transfer frequency limits
- Emergency restrictions
- Risk restrictions
- Capital restrictions
- User policy restrictions

If the system reaches a condition outside its authorization boundary:

```text
REBALANCING REQUIRED
↓
OUTSIDE AUTHORIZED BOUNDARY
↓
DO NOT EXECUTE
↓
WAIT / ALERT / REQUEST AUTHORIZATION
```

The system must never invent authorization.

## 4. TRANSFER AUTHORITY MUST BE SEPARATE FROM TRADING AUTHORITY

Trading credentials must not automatically provide unrestricted withdrawal authority.

The platform should use a separate controlled transfer authority for automated rebalancing where supported.

The intended architecture is:

```text
TRADING AUTHORITY
→ trading only

REBALANCING TRANSFER AUTHORITY
→ approved transfers between approved exchange accounts

WITHDRAWAL / CUSTODY AUTHORITY
→ separate and independently controlled
```

Automated rebalancing must be restricted to approved accounts/venues owned or controlled by the platform/user according to the approved architecture.

It must not become a general-purpose withdrawal mechanism.

## 5. TRANSFER SECURITY

Automated transfers must have additional protection.

Where supported, transfer credentials should be restricted by:

- Destination allowlists
- Asset allowlists
- Amount limits
- Frequency limits
- Venue restrictions
- Authentication controls
- Audit logging
- Policy enforcement

The system must record:

- Why the transfer was initiated
- Source
- Destination
- Asset
- Amount
- Expected benefit
- Transfer cost
- Policy version
- Authorization boundary
- Execution result
- Reconciliation result

## 6. TRANSFER STATE MUST BE VERIFIED

A transfer timeout must never automatically mean:

“The transfer failed.”

Correct behavior:

```text
TRANSFER REQUEST
↓
UNKNOWN / TIMEOUT
↓
QUERY VENUE / BLOCKCHAIN
↓
DETERMINE ACTUAL STATE
├── SUCCESS
├── PENDING
├── FAILED
└── UNKNOWN
```

If the state remains unknown:

```text
NO DUPLICATE TRANSFER
↓
RECONCILIATION
↓
SAFE STATE
```

This requirement applies to all autonomous transfer operations.

## 7. EMERGENCY STATE — REPLACE SIMPLE CANCEL-ONLY BEHAVIOR

The previous default:

“Emergency state cancels open orders but does not close positions.”

is too simplistic for a company-grade system.

The final architecture should use a graduated emergency/safety framework.

An emergency should not be treated as one universal action.

Different emergencies require different responses.

## 8. EMERGENCY SAFETY LEVELS

The platform should support multiple deterministic safety states, for example:

NORMAL

Normal authorized operation.

CAUTION

Detected degradation but execution may continue under tighter controls.

Possible actions:

- Reduce new exposure
- Increase validation
- Restrict affected venues
- Reduce capital allocation
- Increase monitoring

RESTRICTED

New risk-taking is significantly restricted.

Possible actions:

- Stop new positions for affected strategies
- Cancel selected pending orders
- Reduce exposure
- Disable affected strategies
- Preserve existing positions according to strategy-specific rules

SAFE MODE

The platform stops initiating new risk unless explicitly permitted by the safety policy.

Existing positions are managed according to deterministic position-protection rules.

EMERGENCY

Critical system condition.

Possible actions include:

- Cancel appropriate open orders
- Prevent new positions
- Disable affected strategies
- Isolate affected venues
- Preserve capital
- Reconcile all external state
- Activate emergency monitoring
- Apply predefined position-management rules

CRITICAL RECOVERY

The system is uncertain about financial/external state.

The priority becomes:

```text
STOP NEW RISK
↓
RECONCILE
↓
RESTORE STATE CERTAINTY
↓
VALIDATE
↓
RESUME
```

## 9. EMERGENCY POSITION HANDLING MUST BE POLICY-DRIVEN

The system must not blindly close every position during an emergency.

Nor should it blindly leave every position untouched.

The correct behavior depends on the emergency type and the predefined policy.

For example:

```text
EMERGENCY TYPE
↓
POSITION EXPOSURE
↓
MARKET CONDITIONS
↓
LIQUIDITY
↓
STRATEGY
↓
RISK POLICY
↓
POSITION PROTECTION POLICY
↓
ACTION
```

Possible actions:

- Hold
- Reduce
- Hedge
- Close
- Cancel associated orders
- Freeze strategy
- Move to protected state
- Wait for liquidity
- Escalate

These decisions must be deterministic and policy-controlled.

AI must not independently decide how to handle emergency positions.

## 10. EMERGENCY ACTIONS MUST BE IDEMPOTENT

Emergency handling must be safe if triggered multiple times.

For example:

```text
EMERGENCY TRIGGER
↓
CANCEL ORDERS
```

If the emergency controller receives the same trigger again, it must not accidentally create duplicate actions or unintended orders.

Emergency operations should be:

- Idempotent
- Auditable
- Deterministic
- Retry-safe
- Reconciliation-aware

## 11. AUTOMATIC 24/7 RESTART AND RECOVERY

The previous default:

“Trading doesn't resume automatically unless you turn that on.”

does not represent the intended final operating model.

The platform is designed to operate 24/7.

Therefore, the system should support automatic restart and automatic recovery.

However:

Automatic restart must never mean blind automatic trading.

The correct architecture is:

```text
FAILURE / CRASH / RESTART
↓
SERVICE RECOVERY
↓
LOAD PERSISTENT STATE
↓
VERIFY DATABASE
↓
VERIFY POLICY
↓
VERIFY STRATEGY STATE
↓
VERIFY CAPITAL
↓
VERIFY POSITIONS
↓
VERIFY OPEN ORDERS
↓
VERIFY EXCHANGE STATE
↓
RECONCILE
↓
VERIFY RISK STATE
↓
VERIFY SYSTEM HEALTH
↓
VERIFY ACTIVE-INSTANCE OWNERSHIP
↓
RECOVERY DECISION
├── SAFE TO RESUME → AUTOMATIC RESUMPTION
├── PARTIALLY SAFE → RESTRICTED OPERATION
└── UNKNOWN / UNSAFE → SAFE MODE / NO TRADE
```

## 12. AUTOMATIC RECOVERY MUST BE STATE-AWARE

The platform should automatically recover from:

- Process crashes
- Service restarts
- Server restarts
- Container restarts
- Network interruptions
- Exchange disconnections
- WebSocket failures
- Temporary AI-provider failures
- Database/service interruptions where recoverable

Recovery must be based on verified external state, not assumptions.

## 13. 24/7 DOES NOT MEAN BLIND RESUMPTION

The system should be autonomous enough to recover without requiring a human to press:

“Start Trading”

after every ordinary restart.

But it must also be intelligent enough to say:

“I restarted, but my state is uncertain. I will remain in SAFE MODE until reconciliation completes.”

Therefore:

```text
AUTOMATIC RESTART
+
AUTOMATIC RECONCILIATION
+
AUTOMATIC HEALTH CHECK
+
AUTOMATIC SAFE RESUMPTION WHEN CONDITIONS ARE SATISFIED
```

This is the intended company-grade behavior.

## 14. AUTOMATIC RECOVERY FAILURE HANDLING

If recovery cannot establish sufficient certainty:

```text
RECOVERY FAILED
↓
NO NEW TRADES
↓
SAFE MODE
↓
RETRY / RECONCILE
↓
ALERT / INCIDENT
```

The system should continue operating its recovery and monitoring functions where possible.

A human should only be required when the system reaches a condition outside its authorized recovery capabilities.

## 15. ACTIVE INSTANCE PROTECTION DURING RESTART

Automatic recovery must integrate with split-brain protection.

A restarted instance must first establish that it is the authorized active execution instance.

```text
RESTART
↓
ACQUIRE / VERIFY EXECUTION LEASE
↓
CHECK OTHER INSTANCES
↓
VERIFY ACTIVE OWNERSHIP
↓
RECONCILE
↓
RESUME
```

Two instances must never independently believe that they are the active live trading authority.

## 16. CANARY DEPLOYMENT MUST BE READINESS-DRIVEN

The previous default:

“5% of target capital for at least 14 days and 50 trades.”

must not be treated as a universal hard-coded production rule.

Canary deployment should be automatically activated when sufficient capital and all required readiness conditions exist.

Capital availability is one condition, not the only condition.

## 17. AUTOMATIC CANARY READINESS

A candidate strategy version should only become eligible for canary deployment when the system verifies the required conditions.

Conceptually:

```text
CANDIDATE STRATEGY
↓
BACKTEST
↓
OUT-OF-SAMPLE
↓
WALK-FORWARD
↓
STRESS TEST
↓
ROBUSTNESS
↓
PAPER TRADING
↓
RISK VALIDATION
↓
POLICY VALIDATION
↓
OPERATIONAL VALIDATION
↓
CAPITAL AVAILABILITY
↓
LIQUIDITY AVAILABILITY
↓
MARKET/REGIME COMPATIBILITY
↓
SYSTEM HEALTH
↓
CANARY AUTHORIZATION
```

Only then may the platform automatically enter canary operation.

## 18. CANARY CAPITAL MUST BE DYNAMIC

Do not permanently hard-code:

5%

as the universal canary allocation.

The system should determine an appropriate initial allocation within policy-defined limits based on factors such as:

- Available capital
- Target capital
- Strategy risk
- Portfolio exposure
- Liquidity
- Expected opportunity frequency
- Historical validation quality
- Strategy confidence
- Market regime
- Capital efficiency
- Existing portfolio correlation
- Current system risk

The initial canary allocation must always remain within hard risk limits.

## 19. CANARY MUST SCALE GRADUALLY

A successful canary should progress through controlled allocation stages.

Conceptually:

```text
CANARY
↓
SMALL INITIAL ALLOCATION
↓
OBSERVE
↓
VALIDATE LIVE PERFORMANCE
↓
CHECK EXPECTED VS ACTUAL
↓
CHECK RISK
↓
CHECK EXECUTION
↓
CHECK SLIPPAGE
↓
CHECK DRAWDOWN
↓
CHECK STABILITY
↓
INCREASE ALLOCATION
↓
REVALIDATE
↓
NEXT ALLOCATION STAGE
↓
FULL AUTHORIZED DEPLOYMENT
```

The allocation should never jump directly from:

```text
CANARY → FULL CAPITAL
```

without passing the required gates.

## 20. CANARY MUST BE ABLE TO STOP AUTOMATICALLY

If a canary deteriorates, the platform should automatically:

- Stop allocation increases
- Reduce exposure where policy requires
- Suspend the strategy
- Roll back the strategy version
- Return capital to the appropriate reserve
- Record the event
- Analyze expected vs actual performance

This must not require an AI agent to improvise the response.

## 21. CANARY READINESS MUST NOT DEPEND ON TIME ALONE

A strategy should not become production-ready merely because:

“14 days passed.”

Likewise, it should not be rejected merely because it has not reached an arbitrary number of days if all required evidence is otherwise sufficient.

Time and trade count can be useful evidence requirements, but the final readiness framework should be evidence-based and risk-based.

## 22. PERFORMANCE TARGETS — REPLACE FIXED NUMBERS WITH MEASURED PERFORMANCE ENGINEERING

The previous:

50 ms arbitrage

500 ms directional

should not be treated as permanent hard-coded universal targets.

These numbers may be useful as initial engineering targets, but the production architecture should use a measured performance framework.

The system should distinguish:

- Market-data latency
- Internal processing latency
- Opportunity detection latency
- Decision latency
- Risk-validation latency
- Capital-reservation latency
- Order-submission latency
- Exchange round-trip latency
- Fill latency
- End-to-end execution latency

## 23. LATENCY BUDGETS SHOULD BE PATH-SPECIFIC

Arbitrage and directional strategies have different latency characteristics.

Therefore:

```text
ARBITRAGE PATH
→ ultra-low-latency requirements

DIRECTIONAL PATH
→ strategy-dependent latency requirements

RESEARCH PATH
→ latency generally less critical

AI RESEARCH PATH
→ latency budget determined by task

MONITORING PATH
→ independent latency budget
```

The architecture should not force one latency target onto every subsystem.

## 24. PERFORMANCE MUST BE MEASURED, NOT ASSUMED

The platform should continuously collect performance measurements.

Metrics should include, where relevant:

- p50 latency
- p95 latency
- p99 latency
- p99.9 latency
- Maximum observed latency
- Jitter
- Exchange round-trip time
- Queue delay
- Processing delay
- Network delay
- Order acknowledgement delay
- Fill delay
- Missed-opportunity latency
- Data freshness

Performance targets should be established from:

```text
MEASURED BASELINE
↓
MARKET REQUIREMENTS
↓
STRATEGY REQUIREMENTS
↓
RISK REQUIREMENTS
↓
HARD PERFORMANCE LIMITS
↓
SLO / SLA-LIKE INTERNAL TARGETS
```

## 25. LATENCY MUST BE CONNECTED TO OPPORTUNITY ECONOMICS

For arbitrage especially, latency should not be treated as an isolated technical number.

The system should understand:

```text
EXPECTED OPPORTUNITY VALUE
vs
EXPECTED LATENCY DECAY
vs
EXECUTION RISK
```

An opportunity that theoretically produces positive net profit but is likely to disappear before execution should be rejected.

Therefore:

Executable net economics must incorporate realistic execution latency.

## 26. PERFORMANCE DEGRADATION MUST BE AUTOMATICALLY DETECTED

If latency deteriorates:

```text
PERFORMANCE DEGRADATION
↓
DETECT
↓
CLASSIFY
↓
ASSESS OPPORTUNITY IMPACT
↓
ADAPT
```

Possible actions:

- Reduce opportunity eligibility
- Reduce trading frequency
- Disable affected strategy
- Disable affected venue
- Reduce capital
- Increase safety restrictions
- Switch infrastructure path
- Enter degraded mode

The system should not continue behaving as though its performance characteristics remain normal.

## 27. PERFORMANCE SHOULD HAVE HARD SAFETY LIMITS AND SOFT TARGETS

Distinguish:

Hard limits

Crossing these may make execution unsafe.

Soft targets

These are optimization goals.

Observed measurements

What the system actually experiences.

This prevents arbitrary design numbers from being mistaken for guaranteed real-world performance.

## 28. COMPANY-GRADE AUTONOMY PRINCIPLE

The overall operating model should be:

```text
AUTONOMOUS
+
POLICY-BOUNDED
+
RISK-BOUNDED
+
CAPITAL-BOUNDED
+
EVIDENCE-DRIVEN
+
SELF-MONITORING
+
SELF-RECOVERING
+
RECONCILIATION-AWARE
```

The system should require human intervention when necessary, but human absence must not itself cause normal 24/7 operation to stop.

## 29. HUMAN INTERVENTION SHOULD BE EXCEPTION-BASED

Human intervention should primarily be required for conditions such as:

- Policy changes requiring approval
- Security events
- Unrecoverable state
- Unknown financial state
- Unauthorized condition
- Custody/security event
- Infrastructure failure beyond automated recovery
- Architecture changes
- Production approval gates explicitly designated as human-controlled

Routine operation should remain autonomous.

## 30. REPLACE THE PREVIOUS FIVE DEFAULTS WITH THIS MODEL

The repository should no longer describe the system as:

“Rebalancing requires confirmation.”

“Trading does not automatically resume.”

“Canary requires a fixed 5% / 14-day / 50-trade rule.”

“50 ms / 500 ms are permanent performance targets.”

Instead, the authoritative model should be:

Rebalancing

Autonomous, economically intelligent, policy-bounded rebalancing, using dedicated transfer authority and strict security controls.

Emergency

Graduated deterministic safety states with policy-driven handling of orders, positions, exposure, venues and strategies.

Restart

Automatic 24/7 restart and recovery, followed by reconciliation and health validation before automatic safe resumption.

Canary

Automatic readiness-driven canary deployment when capital and all other required validation conditions are satisfied, with dynamic allocation and controlled scaling.

Performance

Measured, path-specific performance engineering with latency budgets, percentile metrics, hard safety limits, soft targets, and automatic degradation handling.

## 31. IMPORTANT CLASSIFICATION RULE

Claude must distinguish between:

Confirmed architectural requirement

Default

Design target

Policy-controlled parameter

Implementation choice

Open question

Future capability

The values such as:

- 5%
- 14 days
- 50 trades
- 50 ms
- 500 ms

must not silently become permanent hard-coded requirements unless they are explicitly approved as such.

The architecture should be designed to support configurable, evidence-driven values.

## 32. FINAL OPERATING PRINCIPLE

The intended platform behavior is:

The system should operate autonomously when it has sufficient authority, capital, information, infrastructure health, and state certainty to do so safely.

When it can act safely:

```text
ACT AUTONOMOUSLY
```

When it needs more information:

```text
WAIT / VALIDATE
```

When it is outside authorization:

```text
DO NOT ACT
```

When external state is uncertain:

```text
RECONCILE / SAFE MODE
```

When a condition is recoverable:

```text
RECOVER AUTOMATICALLY
```

When a strategy is ready:

```text
CANARY AUTOMATICALLY
```

When performance deteriorates:

```text
ADAPT / THROTTLE / SUSPEND
```

When an emergency occurs:

```text
ENTER APPROPRIATE SAFETY STATE
```

The system must therefore be autonomous without being uncontrolled.

## 33. THIS SECTION SUPERSEDES THE EARLIER DEFAULTS

Claude must treat this section as the corrected interpretation of the previously displayed operating defaults.

It must reconcile these decisions against Part 1, Part 2, the existing repository documentation, and the requirements registry.

If a conflict is discovered, Claude must record the conflict and surface it for review rather than silently changing an established requirement.

## END — COMPANY-GRADE AUTONOMOUS OPERATING DEFAULT CORRECTION

## One important point

I deliberately changed the architecture from “automatic” to “automatic + verified.”

That distinction is critical for a real 24/7 financial system.

For example, after a server crash, you do want:

restart → reconcile → verify → resume automatically

You do not want:

restart → immediately send orders.

Likewise, for rebalancing, you want:

detect → calculate economics → verify authorization → execute automatically → verify transfer

rather than:

detect imbalance → ask human every time.

And for canary, you want the platform to recognize when the strategy has actually become eligible, rather than waiting for you to manually activate it.

This gives Claude a much clearer definition of the system you're trying to build: autonomous 24/7 operation with deterministic safety boundaries, rather than human-operated automation.
