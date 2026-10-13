# Critical capability sequencing

Use this method when a program depends on roles, skills, agents, services, platforms, or governance functions whose outputs shape several downstream decisions.

## Separate four states

Do not collapse these into one readiness color:

1. **Capability quality** — can the role or component produce a decision-ready result for the intended job?
2. **Evidence readiness** — which representative, adversarial, stability, and human-calibration evidence supports that claim?
3. **Execution readiness** — is there a bounded runner, permission model, owner, budget, failure handling, and rollback?
4. **Runtime integration** — can the control plane route, invoke, validate, persist, and recover the capability safely?

A high-quality skill can be unintegrated. An integrated runner can execute a weak skill. Neither state implies the other.

## Find the risk-adjusted critical path

For each material capability, record:

| Capability | Consequential outputs | Downstream consumers | Current evidence | Failure/rework impact | Substitute or human fallback | Next irreversible spend |
|---|---|---|---|---|---|---|

Treat a capability as critical when several downstream choices inherit its errors, its output is expensive to reverse, qualified review is scarce, or no credible substitute exists. Do not use roadmap position, implementation effort, organizational seniority, or runtime availability as a proxy for criticality.

## Set two learning gates

For a weak critical upstream capability, use both gates:

1. **Pre-output gate** — strengthen the minimum knowledge, method, boundaries, and adversarial evals needed before it creates a consequential artifact. Require an accountable owner and observable acceptance evidence.
2. **Post-canary gate** — run one bounded, reversible real case; measure first-pass acceptance, defects, human rework, review time, cost, latency, and downstream corrections; convert failures into regression evidence before broader use.

Do not choose between theoretical preparation and empirical learning when both are needed. Keep the pre-output gate small enough to avoid speculative perfection, and keep the canary bounded enough that a weak result cannot silently propagate.

## Sequence decision

Return one of:

- `PROCEED` — the upstream capability meets the evidence gate for the next bounded output;
- `PROCEED_WITH_CANARY` — the capability meets a limited gate, the output is reversible, and independent review contains the risk;
- `STRENGTHEN_FIRST` — a weak upstream capability would create broad or expensive downstream rework;
- `HUMAN_SUBSTITUTE` — qualified human ownership is the smallest safe bridge;
- `STOP_OR_REDIRECT` — the capability or program no longer justifies investment.

State the decision owner, evidence required, downstream work paused or allowed, and the event that triggers reassessment. Never hide a capability debt inside a feature roadmap.
