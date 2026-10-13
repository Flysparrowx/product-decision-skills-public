# Economics and Scenario Modeling

## Contents

1. Modeling discipline
2. Universal economic spine
3. Model-specific economics
4. Market sizing
5. Pricing research
6. Financial sensitivities
7. Strategic scenario planning

## Modeling discipline

For each input record: name, value/range, unit, period, segment/cohort, source, date, confidence, and whether it is verified, supplied, assumed, or estimated.

Keep actuals, plan, forecast, and scenario separate. Ensure numerator and denominator use the same cohort and period. Show pre-tax/post-tax and cash/accrual treatment when material.

If inputs are missing, provide formulas and the smallest data request needed. Do not populate a “realistic” model from intuition.

## Numeric-input gate

Before calculating, inspect every material numeric input.

- If it is supplied by the user, preserve its provenance and caveats.
- If it is externally sourced, cite it and verify that geography, segment, model, unit, and period are comparable.
- If it can be derived, show the derivation.
- If it is missing, leave it symbolic or show the break-even value the business would need.

Do not invent example prices, CAC, conversion, attach, churn, returns, cost, margins, market share, or launch investment merely because the user asks for “indicative economics.” A range made from invented endpoints is still invented.

Only create a hypothetical numeric sandbox when the user explicitly requests a worked numerical illustration. Label every invented input `ARBITRARY TEACHING INPUT`, keep it separate from the decision model, and do not describe the result as plausible, realistic, market-based, or recommended.

## Universal economic spine

At minimum model:

- volume or active units;
- price or revenue per unit;
- discounts, refunds, taxes collected, and channel share where applicable;
- variable cost per unit;
- contribution margin per unit and total;
- fixed and step-fixed operating costs;
- acquisition or selling cost;
- retention/repeat/renewal or replacement cycle;
- working capital and timing of cash flows where material;
- capacity constraints;
- break-even condition;
- key sensitivity drivers.

Basic formulas:

```text
Net revenue = gross billings - discounts - refunds - channel share - taxes excluded from revenue
Contribution per unit = net revenue per unit - variable cost per unit
Contribution margin % = contribution / net revenue
Break-even units = avoidable fixed costs / contribution per unit
Operating result = total contribution - fixed and step-fixed operating costs
```

Define what is included in “variable cost” and contribution level. Do not compare CM1 from one model with CM3 from another.

## Model-specific economics

### Subscription and SaaS

```text
MRR = active paying accounts × ARPA
Gross margin = (revenue - cost of revenue) / revenue
CAC = attributable acquisition and sales cost / new customers acquired
Gross-profit payback months = CAC / monthly gross profit per new customer
NRR = (starting recurring revenue - churn - contraction + expansion) / starting recurring revenue
GRR = (starting recurring revenue - churn - contraction) / starting recurring revenue
```

Use `LTV ≈ ARPA × gross margin / churn` only as a rough steady-state shortcut when churn definition, cohort stability, and horizon make it valid. Prefer cohort cash-flow LTV. Include onboarding, implementation, support, infrastructure, payment, and partner costs consistently.

### Marketplace

```text
GMV = completed transactions × average transaction value
Net revenue = GMV × realized take rate + other net revenue
Contribution = net revenue - payments - incentives - variable support - trust/safety - refunds/losses - other variable costs
```

Model supply and demand acquisition separately. Add match/fulfillment rate, time to match, repeat, cancellation, disintermediation, geographic/category density, and incentive dependence. Do not call GMV revenue.

### Physical product and hardware

```text
Net unit revenue = sell-through price - channel margin - discount - expected returns/refunds
Unit contribution = net unit revenue - landed COGS - fulfillment - payment - expected warranty/service - variable selling cost
Cash conversion cycle = inventory days + receivable days - payable days
```

Include yield/scrap, tooling, minimum order quantities, freight, duties, inventory write-downs, working capital, returns, warranty, certification, and service. Separate sell-in from sell-through.

### Services

```text
Delivery capacity = available delivery hours × target utilization
Realized rate = recognized service revenue / billable hours delivered
Engagement contribution = engagement revenue - delivery labor - contractors - travel - other variable delivery costs
```

Include bench, presales, rework, scope creep, senior review, founder time, collections, and capacity steps. Distinguish booked, billed, recognized, and collected revenue.

### API, data, and AI

```text
Unit gross profit = unit revenue - compute/model/tool/data/egress/human-review/support cost per unit
Gross margin by cohort = cohort revenue less attributable cost of revenue / cohort revenue
```

Choose a real unit: task, call, token, minute, workflow, active agent, query, or outcome. Model free-tier leakage, retries, model routing, peak capacity, quality/safety evaluation, human escalation, observability, and vendor concentration. Do not assume scale automatically improves inference margin.

### Advertising or media

Model active users, eligible impressions, ad load, fill rate, viewability, realized eCPM, revenue share, content/moderation cost, and retention impact. Revenue per active user can rise while product value deteriorates; add guardrails.

### Fintech or transaction products

Model processed volume, take/interchange, payment/network fees, fraud/credit losses, reserves/capital, chargebacks, incentives, compliance/operations, and cost of funds. Regulatory treatment requires current qualified evidence.

### Hybrid hardware plus recurring service

Model device contribution and recurring cohort economics separately, then combine through attach rate, activation, renewal, service cost, replacement, return/warranty, and cash timing.

## Market sizing

Triangulate rather than choose the largest number.

- **Bottom-up:** reachable entities/users × realistic adoption × price/usage.
- **Top-down:** credible category data narrowed by explicit filters.
- **Value theory:** share of economic value created or cost avoided that could plausibly be captured.

State whether sizing is revenue pool, spend, GMV, users, units, or value created. Define geography, period, segment, exclusions, currency, and source year.

SOM must be constrained by channel reach, sales capacity, production capacity, regulation, switching, competition, and time. “One percent of TAM” is not a bottom-up SOM.

## Pricing research

Separate:

- value metric;
- packaging and fences;
- list price;
- realized price and discounting;
- willingness to pay;
- cost floor;
- competitive/reference price;
- price elasticity;
- monetization and billing mechanics.

Choose method by decision:

- live offer, preorder, paid pilot, or negotiation for behavioral evidence;
- Gabor-Granger for purchase likelihood across prices;
- Van Westendorp for perceived price thresholds, not direct demand optimization;
- conjoint/discrete choice for feature-package-price trade-offs;
- value-based interviews and economic value modeling for complex B2B;
- cohort or geo experiments when ethical, operationally feasible, and statistically designed.

Do not derive a precise optimum from a small convenience sample. Report sampling, stimulus, method, uncertainty, and differences between stated and actual behavior.

## Financial sensitivities

Build base/downside/upside from explicit drivers, not blanket percentages. Typical drivers include volume, price, conversion, retention/repeat, mix, take rate, gross margin, CAC, sales cycle, utilization, return/loss rate, compute cost, inventory, and capacity.

Do not create base/downside/upside numbers until each driver has a supplied, sourced, or derived anchor. With no anchors, return a blank driver table, formulas, break-even conditions, and a measurement plan.

Rank drivers by effect on the decision. Use one-way sensitivity for clarity; use multi-variable scenarios for coherent states. When distributions and dependencies are defensible, simulation may help, but do not imply certainty from uncalibrated distributions.

Scenario table:

| Driver | Downside | Base | Upside | Evidence/source | Trigger/signpost |
|---|---:|---:|---:|---|---|
| Volume | | | | | |
| Price/mix | | | | | |
| Retention/repeat | | | | | |
| Unit cost | | | | | |
| Acquisition/sales efficiency | | | | | |

For each scenario show revenue, contribution, fixed cost, operating result/cash, break-even timing or condition, capacity, and main failure mode as appropriate.

## Strategic scenario planning

Use strategic scenarios when external uncertainty changes what should be done today. Scenarios are plausible alternative futures, not predictions.

1. Define focal decision and horizon.
2. Separate predetermined trends from critical uncertainties.
3. Choose two decision-relevant, sufficiently independent uncertainties for a 2×2, or use morphological combinations when two axes oversimplify.
4. Write internally coherent worlds with causal chains.
5. Test every strategic option across the worlds.
6. Identify robust moves, options to preserve, hedges, and no-regret investments.
7. Define observable signposts and decision triggers.

Do not assign probabilities unless evidence and a calibration method justify them. Do not pick a favorite scenario and call it “base case.”
