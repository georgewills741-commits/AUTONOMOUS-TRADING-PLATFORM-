# DEC-015 — Operating modes, canary, and policy governance

- **Status:** ACCEPTED (delegated: builder decision under the owner's instruction to resolve all open items; the owner may override)
- **Date:** 2026-09-30
- **Resolves:** OQ-08, OQ-09, OQ-15, OQ-17, CF-08

## Operating modes (OQ-08)

- Mode is part of policy. The Policy System owns the platform-wide maximum mode and each strategy's mode, and a mode change is a policy change (POL-008).
- Each strategy runs in its own mode, capped by the platform maximum (MODE-003).
- Moving to a more permissive mode requires the operator's confirmation and lifecycle eligibility. Moving to a less permissive mode can happen automatically (MODE-004).
- In SUPERVISED mode the operator approves each proposal. An unapproved proposal expires as NO TRADE, and an approved one is revalidated before execution (MODE-005).
- **Modes vs environments:** real orders can only come from the production environment, the only one holding trading-enabled credentials. Every other environment is technically unable to place real orders (MODE-006, SEC-004; constitution Rules 109 and 111).

## Canary (OQ-09)

A newly approved strategy version trades live with a capped capital allocation and tightened risk limits, for a minimum period and trade count (STR-011).
- Promotion to production requires expected-vs-actual results within tolerance and no safety incidents.
- A breach suspends the version or rolls back to the previous one.
- Initial defaults, all operator-configurable: capital cap of 5% of the strategy's target allocation; minimum 14 days **and** 50 trades.

## Policy governance (OQ-17)

- **Important change (POL-005):** any change that loosens a limit or restriction; increases authorized capital, leverage, or venues; moves a strategy to a more permissive mode; or changes a hard constraint. It requires the operator's explicit confirmation after seeing the difference, the conflict check, and the risk analysis.
- **Simulation (POL-006)** — a replay over recent market data, or a paper run — is required before activating a change that loosens risk limits or increases capital or leverage.
- **Tightening changes (POL-007)** may activate immediately; they are still versioned and audited.
- **Before the NL interface exists (POL-010),** the operator edits structured policy through a validated operator interface under the same rules.

## Policy location (CF-08, OQ-15)

The operator's actual policy exists only in the Policy System's versioned runtime store (POL-009). `docs/product/trading-policy.md` from §98 is **not created**: a repository copy of runtime policy would be a second source of truth. The product-level description of what the operator controls is NLP-002.
