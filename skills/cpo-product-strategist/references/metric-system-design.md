# Metric System Design

## Contents

1. Metric-system contract
2. North Star selection
3. Causal metric tree
4. Ecosystem health
5. Validation and governance
6. Deliverable

## 1. Metric-system contract

Start from the decision and value mechanism, not a familiar KPI. Identify the user, buyer, payer, beneficiary, supply-side actor, and product job. Define the natural value cycle and whether the system is subscription, transactional, marketplace, service, physical, mission, AI, or hybrid.

Keep five layers distinct:

```text
Customer or mission value
→ North Star or primary outcome
→ causal value drivers and state transitions
→ controllable product and operating inputs
→ initiatives and experiments

Alongside: quality, harm, ecosystem, economic, and capacity guardrails
```

Do not mix a company goal, financial result, product outcome, input, health metric, target, and project in one undifferentiated tree.

## 2. North Star selection

A North Star should represent repeated delivery of core value, not attention or company size. Test candidates against:

- **Value:** does movement imply that the intended user received meaningful value?
- **Breadth:** does it cover the core product without rewarding irrelevant activity?
- **Frequency:** is the observation cycle natural for the product?
- **Leading power:** can it move before the ultimate retention, mission, or financial result?
- **Controllability:** can product and operating choices influence its causal inputs?
- **Integrity:** can it be measured consistently and reconciled?
- **Gaming resistance:** what harmful behavior could improve it?
- **Economics:** does sustained movement plausibly support contribution, mission, or strategic value?

Revenue, GMV, MAU, time spent, messages, tokens, installs, and feature usage are not automatically North Stars. They may be business outcomes, scale metrics, inputs, or diagnostics. For infrequent, multi-product, regulated, enterprise, or multi-sided systems, one universal North Star may be misleading. Use a primary outcome plus a compact balanced metric system when necessary, and explain why.

For AI or services, prefer the completed and accepted customer outcome over attempts, conversations, or generated output. Add persistence or downstream use when immediate completion can be superficial.

## 3. Causal metric tree

Build top-down, validate bottom-up:

1. Define the customer-value event and observation window.
2. Express the North Star through an identity or state bridge where possible.
3. Decompose into mutually interpretable drivers; do not force perfect MECE when mechanisms overlap.
4. Separate controllable inputs from contextual or exogenous drivers.
5. Mark each link `established`, `supported`, `hypothesized`, or `unknown`.
6. Attach the owner, measurement contract, and decision rule to each decision-critical metric.
7. Map initiatives only to the input they are hypothesized to change.

Useful structures:

```text
Value outcomes = eligible demand × value-event completion × accepted quality × repeat

Ending active value units
= retained + newly activated + reactivated - churned

Contribution
= successful outcomes × net revenue per outcome
- variable outcome cost - avoidable fixed cost
```

An arithmetic identity is not proof of causality. A causal arrow requires evidence or an explicit hypothesis. Avoid duplicated branches, ratios whose denominators drift, and trees that end in team activities.

## 4. Ecosystem health

For marketplaces, platforms, super-apps, agent networks, and operational systems, show actor value and system health separately.

| Layer | Questions |
|---|---|
| Demand | Did the intended user obtain the outcome with acceptable time, price, and quality? |
| Supply/partner | Did providers receive sustainable demand, income, utilization, and fair operating conditions? |
| Platform | Did matching, fulfillment, trust, liquidity, and contribution improve? |
| Society/risk | Did fraud, harm, bias, congestion, labor, safety, or regulatory exposure worsen? |

A platform metric must not improve by extracting unsustainable value from another side. Use actor-specific retention and contribution, match/fulfillment quality, concentration, dependency, and negative externalities as guardrails.

## 5. Validation and governance

For every critical metric define formula, entity, population, event/source, period, latency, exclusions, owner, gaming risk, target rationale, and action threshold. Reconcile product events to billing and finance for revenue or contribution claims.

Validate candidate inputs through cohort analysis, controlled experiments, quasi-experiments, or predictive checks appropriate to the claim. A correlation with retention is not automatically a lever. Version definition changes and preserve bridges when instrumentation changes.

Targets require a baseline and mechanism. With missing data, return the symbolic tree, missing-input list, and measurement plan rather than arbitrary percentages.

## 6. Deliverable

Provide:

1. decision and value mechanism;
2. candidate North Stars and selection rationale;
3. selected outcome or balanced system;
4. visual causal tree with evidence status on links;
5. metric dictionary for decision-critical nodes;
6. guardrails and gaming risks;
7. validation plan and owners;
8. explicit gaps and next review trigger.

Use Mermaid, an editable slide, or another visual artifact when the hierarchy and causal links are easier to understand graphically.
