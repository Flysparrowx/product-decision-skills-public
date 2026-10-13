# Quantitative Decision Science

## Contents

1. Role boundary
2. Quantitative decision contract
3. Calculation router
4. Method ladder
5. Unit economics and scenario calculators
6. Product P&L, cash, and plan-versus-actual
7. Experiments, samples, and causal validity
8. Segments, countries, and heterogeneous effects
9. Value of information and constrained optimization
10. Calculator output contract
11. Synthetic evidence boundary
12. Completion gate

## Role boundary

CPO owns the decision, customer and business mechanism, price of error, alternatives, economic meaning, and recommendation. A qualified quantitative analyst owns quantitative design, reproducible calculation, uncertainty, causal validity, and model diagnostics. Do not make the user coordinate the handoff manually: formulate a bounded quantitative question, use a qualified quantitative workflow when available; otherwise disclose the limitation and return the calculator contract, then integrate the result into the product decision.

Do not route trivial arithmetic away. CPO may calculate transparent totals, ratios, contribution, break-even, and one-way scenarios directly. Route when the answer needs statistical inference, sample size or power, factorial or sequential experiments, causal identification, Monte Carlo, optimization, hierarchical or heterogeneous effects, or material model validation.

If Data Scientist is unavailable, return `QUANTITATIVE_HANDOFF_REQUIRED` with the complete contract below. Do not replace a missing calculation with general advice.

## Quantitative decision contract

Before calculating, state:

| Field | Required content |
|---|---|
| Decision | Exact choice and accountable owner |
| Alternatives | Actions being compared, including baseline or do-nothing where viable |
| Decision unit | Customer, order, episode, account, market, project, month, or another real unit |
| Outcome | Customer and business result the choice should change |
| Loss/payoff | Cost of false positive, false negative, delay, and additional evidence |
| Population | Eligibility, exclusions, segments, geography, and time window |
| Inputs | Value/range, unit, period, provenance, freshness, and confidence |
| Minimum meaningful change | Smallest effect that changes action, derived from value, economics, risk, or capacity |
| Method | Calculation or design selected and why it is the simplest adequate one |
| Uncertainty | Interval, scenario range, sensitivity, or probability with assumptions |
| Decision rule | What result leads to proceed, revise, stop, extend, or collect more evidence |
| Calculator | Manipulable inputs and outputs the decision owner needs |

Separate supplied and sourced data, derived values, assumptions, and unknowns. Preserve formulas even when numeric results are available.

## Calculation router

Choose calculations from the decision, not from a standard finance template. Do not run every row.

| Decision | Minimum useful calculations | Typical decision output |
|---|---|---|
| Is one customer/order/use profitable? | net revenue bridge, variable cost, contribution, margin, support/rework burden | improve price/cost/process, narrow segment, or stop |
| Can the product become a viable business? | volume × price, cohort retention/repeat, CAC/payback, fixed and step-fixed costs, cash timing, break-even | model and scale gate |
| Is the product P&L on course? | plan/forecast/actual bridge by volume, price/mix, retention, cost and timing; gross profit, contribution, operating result, cash | corrective action and reforecast |
| What price/package should be tested? | cost floor, value boundary, willingness-to-pay evidence, elasticity or choice design, margin and adoption trade-off | price/package test |
| Is growth real and valuable? | cohort/state bridge, activation, retention, expansion/contraction, contribution by cohort/channel | invest in the binding growth transition |
| How large is the opportunity? | bottom-up capacity/reach, top-down triangulation, value capture, uncertainty | enter, narrow, partner, or decline |
| Which hypothesis/test is worth running? | minimum meaningful effect, sample/power or precision, validity, expected decision loss and value of information | run, redesign, or skip experiment |
| How much can we deliver? | demand, throughput, utilization, bottleneck capacity, queue/service level, step costs, quality/rework | capacity or scope decision |
| Which portfolio bet gets resources? | incremental cash flows, opportunity cost, risk, reversibility, dependency, NPV/payback when inputs support them | allocate, stage, partner, or stop |
| Is an AI/agent workflow economical? | successful outcomes, attempts/retries, model/tool/human cost, quality loss, escalation, vendor commitments | routing, autonomy, price, or kill decision |
| Where should portfolio resources go? | direct/shared/incremental resource ledger, current outcome, lifecycle potential, marginal contribution per constraint, opportunity cost and evidence maturity | invest, maintain, test, reallocate, partner, or stop |
| Is a new product hypothesis economically coherent? | shadow P&L, break-even inputs, capacity/cash exposure, sensitivity, evidence tags and promotion gate | test the governing assumption or decline the hypothesis |

Treat ROI, NPV, IRR, payback, LTV, market size, and composite scores as optional methods, not badges of rigor. Use them only when their cash-flow boundary, horizon, comparator, discount rate or cohort assumptions are defined. Prefer transparent incremental cash flows over a single summary ratio.

## Method ladder

Stop at the first method that can resolve the decision:

1. Exact arithmetic or accounting identity.
2. Symbolic formula, break-even condition, or threshold when inputs are missing.
3. One-way sensitivity for dominant drivers.
4. A small set of coherent multi-variable scenarios.
5. Statistical interval, sample/precision calculation, or controlled experiment.
6. Causal or quasi-experimental design when randomization is unavailable.
7. Monte Carlo only when distributions, dependencies, and calibration are defensible.
8. Constrained optimization only when objective, constraints, feasible actions, and uncertainty are explicit.

Complexity must earn its keep by changing a decision. Do not use simulation to decorate uncertain guesses.

## Unit economics and scenario calculators

Start from the archetype-specific formulas in `economics-and-scenarios.md`. At minimum, expose:

- customer or value-producing unit;
- price and net revenue bridge;
- variable and attributable service cost;
- contribution per unit and contribution margin;
- acquisition/selling cost and retention, repeat, or renewal where relevant;
- capacity and step-fixed costs;
- cash timing and working capital where material;
- break-even volume, price, conversion, retention, utilization, or payback condition;
- dominant sensitivities and the decision they can reverse.

For each output show the formula and linked inputs. Reconcile totals to unit economics. Do not show CAC, LTV, margin, or payback without definitions and cohort/period alignment.

When inputs are uncertain but anchored, show a scenario or sensitivity table. Use Monte Carlo only when the input distributions and dependencies come from evidence or an explicitly approved assumption set. Report the probability of crossing a decision threshold, not a cloud of simulated numbers without an action.

## Product P&L, cash, and plan-versus-actual

CPO owns the product drivers and actions; Finance remains the source of truth for accounting policy, statutory reporting, tax, capitalization, and booked actuals. Reconcile rather than create a parallel ledger.

Use the smallest P&L view that explains the decision:

```text
Net revenue
- cost of revenue / COGS
= gross profit
- additional variable or attributable operating costs excluded from COGS
= contribution
- avoidable product, delivery, sales, and operating expenses in scope
= product operating result
```

Keep gross profit, contribution, EBITDA-like measures, accounting profit, and cash distinct. State what each subtotal includes. Add one-time investment, capex, working capital, collections/payment timing, tax, and shared-cost allocation only when they affect the decision.

For management cadence, preserve four states:

- `Actual` — reconciled booked or operational result;
- `Plan/Budget` — approved target and assumptions;
- `Forecast` — current expected result from observed drivers;
- `Scenario` — conditional outcome under explicit choices or uncertainties.

Build a driver bridge instead of reporting only variance:

```text
Revenue variance = volume + price + mix + retention/repeat + timing + FX where relevant
Contribution variance = revenue bridge + unit-cost + channel + refunds/losses + service/rework
Cash variance = operating result + collection/payment timing + working capital + investment
```

For each material variance show source, whether it is timing or structural, owner, corrective lever, forecast effect, and next decision. Never plug an unexplained residual into “other” if it can reverse the decision.

Use cohort or segment P&L when acquisition source, customer type, geography, plan, fulfillment mode, or product version changes revenue quality or cost-to-serve. A profitable aggregate can conceal loss-making new cohorts; a loss-making launch cohort can conceal improving unit economics. Compare like-for-like cohort age and period.

## Experiments, samples, and causal validity

Before sample size or power, define the primary decision metric, randomization unit, analysis unit, baseline, variance or event rate, minimum meaningful effect, alpha or interval coverage, desired power or precision, allocation, attrition, clustering, and planned analysis.

If these inputs are missing:

- identify exactly which are missing;
- provide the formula or calculation method;
- show which input most changes the required sample;
- propose the smallest pilot that estimates the missing variance, rate, or operational constraint;
- do not invent a universal sample size.

For factorial experiments, separate factors and interactions. A design such as `story × visual treatment × country` requires enough replication for the main effects and preselected interactions that matter to the decision. Do not create every possible cell when a fractional factorial, staged design, or narrower hypothesis resolves the choice more cheaply.

Pre-specify eligibility, exposure, primary outcome, guardrails, stopping rule, multiple-testing treatment, sample-ratio mismatch checks, contamination, delayed effects, and missing-data handling. Do not equate a statistically detectable effect with a worthwhile effect.

For observational evidence, name confounders, selection, reverse causality, concurrent changes, and the identification strategy. Without a credible counterfactual, label the result descriptive or associational and state the cheapest design that could support a causal decision.

## Segments, countries, and heterogeneous effects

Do not blend populations whose behavior or measurement process may differ. Predefine decisive slices such as country, age band, prior familiarity, channel, customer type, or warm/cold audience only when they map to a product decision.

Distinguish:

- overall effect;
- segment-specific effect;
- treatment-by-segment interaction;
- composition or mix shift;
- measurement or collection differences;
- exploratory subgroup finding versus pre-specified claim.

Use hierarchical or partial-pooling models only when they improve inference across related groups and their assumptions are defensible. Otherwise report each relevant segment with uncertainty and abstain where evidence is insufficient. Do not call a country difference a cultural cause without an identification strategy and local evidence.

## Value of information and constrained optimization

Research earns priority only when its plausible outcomes can change the decision and its expected value exceeds its cost, delay, and risk.

Use this sequence:

1. Identify the uncertain variable and decisions it can reverse.
2. Estimate the consequence of choosing wrongly across plausible states.
3. Compare expected decision loss now with expected loss after information.
4. Subtract research cost, delay cost, and execution risk.
5. Prefer the cheapest credible evidence that resolves the highest-value uncertainty.

Use a qualitative value-of-information ranking when probabilities or payoffs lack evidence. Do not manufacture probabilities to force a monetary answer.

For constrained optimization, state the objective, budget/capacity constraints, feasible actions, indivisibilities, dependencies, guardrails, and uncertainty. Show the baseline allocation and sensitivity to binding constraints. A mathematically optimal plan that violates product, ethical, operational, or legal constraints is not feasible.

## Calculator output contract

Provide the smallest manipulable artifact that supports the decision:

| Complexity | Default output |
|---|---|
| One formula or threshold | Inline formula + input table + worked result from supplied data |
| Repeated unit economics or several scenarios | Spreadsheet-style table with editable inputs, formulas, outputs, units, provenance, and checks |
| Nonlinear sensitivity, many scenarios, or stakeholder exploration | Minimal read-only interactive calculator with reset, assumptions, boundary handling, and export only if needed |

Every calculator must expose:

- decision it supports;
- editable inputs and locked formulas;
- units, periods, segments, and provenance;
- base result and break-even/decision boundary;
- explicit decision inequality or rule for both sides of the boundary, plus the rounding convention for discrete units;
- uncertainty or sensitivity;
- invalid or missing-input behavior;
- three checks: normal, boundary, and invalid/missing input;
- explicit statement of what the calculator does not prove.

### Missing-input completion contract

When product-specific inputs are missing, do not respond with only a complete blank model. Make the calculator immediately actionable in this order:

1. Add provenance columns for every input: source or owner, as-of date or observation window, supplied/verified/assumed status, and confidence or freshness where material.
2. Before showing the full input dictionary, render a visibly labeled **Smallest first-fill set** containing only the minimum subset that can already produce a useful result such as contribution per unit, a break-even price or volume, a retention threshold, or a symbolic payback condition. Do not bury this subset inside the full model or require the full dataset before returning the first decision boundary.
3. State the first result unlocked by that subset and which product choice it can change. Then show the next sensitivity or cohort result unlocked by the next input layer.
4. End with one exact evidence gate: the population, cohort, or segment; the period, event window, or cohort age; the source or accountable owner; the fields to collect; and the `PROCEED`, `REVISE`, `STOP`, or equivalent product decision that the evidence will unlock.

For subscription viability, use progressive input layers rather than one undifferentiated table:

- first-fill: realized price/net-revenue deductions and variable cost-to-serve → contribution per active customer and the first price/cost boundary;
- next: avoidable fixed cost → break-even active-customer volume;
- next: CAC plus cohort retention or renewal → cohort contribution, payback, and the scale decision;
- later when material: acquisition volume, cash timing, step-fixed cost, and working capital → operating and cash exposure.

“Fill in the table” or “collect actual data” is not an evidence gate. A full input dictionary without a prioritized first-fill set is incomplete even when its formulas are correct.

Offer relevant calculator types when useful: unit economics and break-even; pricing/package; CAC/LTV/payback; capacity/utilization; cohort cash flow; market sizing; experiment sample/power; portfolio allocation; Monte Carlo probability of crossing a threshold; value of information. Do not offer a catalog detached from the current decision.

## Synthetic evidence boundary

LLM personas, simulated agents, synthetic respondents, and generated focus groups may:

- find ambiguities in a questionnaire or scenario;
- generate hypotheses and edge cases;
- rehearse operational flows;
- stress-test a decision rule.

They may not be counted as respondents or observations, estimate population preferences, calibrate demand, prove willingness to pay, supply an effect size, or replace real local/member evidence. Label synthetic outputs as simulation and keep them outside quantitative audience estimates.

## Completion gate

Before returning a quantitative recommendation, verify:

- the decision, alternatives, population, unit, outcome, and price of error are explicit;
- every material number has provenance or is clearly symbolic;
- the simplest adequate method was used;
- the calculation is reproducible and formulas remain visible;
- P&L labels and plan/forecast/actual/scenario states are not mixed, and important variances are traced to product drivers;
- uncertainty and decisive segments are shown;
- statistical and economic significance are separated;
- confounding and causal limits are stated;
- value of additional information is compared with cost and delay;
- the decision owner can vary the inputs that can reverse the choice;
- synthetic evidence has not been upgraded into real audience evidence;
- the result ends with a product decision or exact next evidence gate.
