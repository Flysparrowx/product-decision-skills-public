# Venture Studio and investment governance

Use this reference for a portfolio of early ideas, an explicit incubation decision, or a material investment decision. Keep ordinary product diagnosis in the lightest existing engagement mode.

## Venture Studio flow

```text
Idea intake
→ decision-critical assumptions and strategic fit
→ choose evidence vehicle: research | proxy | concierge | spike | bounded full product
→ bounded observation of problem, value, behavior, commitment, economics, and risk as applicable
→ evidence review
→ CONTINUE_TEST | INCUBATE | PARTNER | KILL
→ only after evidence: SCALE consideration
```

The CPO prepares evidence and a recommendation. The named human Product Owner or investment owner makes the decision and controls capital/capacity.

## Idea intake

Capture only information that can affect the next decision:

- idea, accountable owner, origin, and requested decision;
- problem, target user, buyer/payer, beneficiary, trigger, current alternative, and explicit non-target;
- supplied evidence with provenance and contradictions;
- strategic fit and portfolio role;
- economic mechanism and material unknown inputs;
- required capital/capacity when known;
- dependencies, risks, reversibility, option value, and opportunity cost;
- load-bearing assumptions and the most decision-efficient credible evidence vehicle, including a bounded full product when appropriate.

An attractive narrative is not problem, demand, willingness-to-pay, or feasibility evidence.

## Evidence-vehicle decision

Do not impose a universal problem-interview or mockup gate before building. Compare each candidate evidence vehicle on fidelity to the claim, time and total cost to observation, downside exposure, reversibility, and value of the resulting learning. Apply `full-product-discovery.md` when the actual journey is necessary and AI-assisted build/rebuild materially changes the cost structure.

A bounded full product may be the first credible test when it is a coherent narrow experience, release and operations are reversible, the representative audience is limited, and instrumentation and decision rules exist before exposure. Use safer staged evidence when physical, clinical, legal, privacy, security, financial, contractual, reputational, or partner risk dominates. Cheap code is not cheap exposure.

## Evidence maturity

Describe maturity by the strongest directly supported claim, not by an aggregate score:

- `IDEA_HYPOTHESIS` — problem, user, buyer, or mechanism remains assumed;
- `PROBLEM_EVIDENCE` — the target problem and context are observed, but the proposed value/mechanism is not validated;
- `SOLUTION_EVIDENCE` — representative users can obtain the intended value inside a bounded test;
- `VIABILITY_EVIDENCE` — buyer, economics, channel, capacity, risk, and operating assumptions have decision-relevant evidence;
- `SCALE_EVIDENCE` — repeated outcome and economic/operational controls support a scale decision for the stated scope.

Record evidence separately for problem, value, buyer, viability, feasibility, channel, risk, and scale. One strong dimension does not upgrade the others.

## Decision rules

- `CONTINUE_TEST` when a material assumption remains unresolved and another bounded test has positive decision value.
- `INCUBATE` when evidence supports a bounded product thesis and the next capital/capacity commitment is explicit and reversible.
- `PARTNER` when an external party can close a capability, channel, credibility, regulatory, or capital gap more efficiently without destroying the option's value.
- `KILL` when a load-bearing assumption is contradicted, the next test has poor decision value, opportunity cost dominates, or the option no longer fits strategy.
- consider `SCALE` only after repeated value and viability evidence, operational controls, dependencies, downside exposure, and capacity are visible.

Weak or negative evidence may justify kill, narrow, pivot, partner, or a different test. Do not defend the original thesis merely because work has already been invested.

## Multi-idea portfolio comparison

Do not rank heterogeneous ideas with invented weights or a single total score. Compare them on separate lenses:

- portfolio role and strategic fit;
- evidence maturity by risk dimension;
- decision-critical unknowns and value of the next test;
- capital, scarce capacity, cash exposure, and transition cost;
- dependencies, concentration, cannibalization, and opportunity cost;
- reversibility, option value, and what learning remains useful if the idea fails.

When inputs are not comparable, return an evidence-gated sequence: obligations first, then tests that resolve the highest-impact uncertainty per unit of scarce capital/capacity. State what evidence would make ranking valid.

## InvestmentMemo contract

Create `InvestmentMemo` only for a material fund, incubate, double-down, partner, or kill decision. Include:

1. decision and accountable human owner;
2. recommendation and confidence;
3. problem and supplied/verified evidence, contradictions, assumptions, and unknowns;
4. target user, buyer/payer, beneficiary, trigger, current alternative, and non-target;
5. why now, separating facts from inference;
6. product thesis, strategic fit, and portfolio role;
7. materially different alternatives, including narrow/test/partner/kill where viable;
8. economics mechanism, formulas, required inputs, dominant sensitivities, and break-even conditions;
9. capital/capacity requirement when known, otherwise the measurement request;
10. risks, dependencies, opportunity cost, reversibility, and option value;
11. most decision-efficient credible evidence vehicle and the evidence it must produce;
12. precommitted kill/change/double-down conditions;
13. recommended decision, immediate evidence-gated action, and next human gate.

Do not invent market size, price, cost, threshold, sample, date, or timeline. Use symbolic formulas and an input request when anchors are absent. A memo is decision support, not funding authority.

## Architecture boundary

The CPO owns the problem, target, value, economics, portfolio posture, evidence and investment recommendation. Product Architect owns technical structure and produces the ArchitectureSpec. State product constraints and required capabilities, then hand off architecture questions; do not invent services, agents, storage, deployment, or runtime topology inside the InvestmentMemo.

## Completion gate

Before delivery, confirm:

- the lightest mode was used and Venture Studio did not hijack a narrow request;
- evidence maturity is multidimensional and not a fabricated score;
- alternatives and opportunity cost are visible;
- missing economics remain formulas/input requests;
- negative evidence can change or end the thesis;
- the next decision and human owner are explicit;
- funding and technical authority were not claimed.
