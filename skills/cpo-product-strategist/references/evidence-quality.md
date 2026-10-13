# Evidence and Confidence Protocol

## Contents

1. Evidence ledger
2. Evidence hierarchy
3. Confidence
4. Research and citation rules
5. Customer evidence
6. Anti-hallucination checks

## Evidence ledger

Tag decision-relevant statements:

| Tag | Meaning | Required treatment |
|---|---|---|
| Verified | Directly supported by supplied or cited evidence | Name the source and relevant date/period |
| Supplied | Provided by the user or organization but not independently verified | Preserve provenance; do not silently upgrade to verified |
| Inference | Reasoned conclusion from evidence | Show the reasoning and plausible alternative |
| Assumption | Provisional input | State why it is needed and how to test it |
| Estimate | Calculation based on inputs | Show formula, units, period, range, and input provenance |
| Unknown | Material missing information | Explain decision impact and fastest credible way to learn |

A compact evidence ledger should include claim/input, tag, source, freshness, decision impact, confidence, and next validation step.

## Evidence hierarchy

Use the strongest available evidence suited to the claim:

1. Direct product telemetry, transactions, contracts, observed behavior, audited finance, and controlled experiments.
2. Direct customer or buyer research with traceable sampling and raw evidence.
3. Official statistics, regulation, filings, standards, and primary research.
4. Credible secondary research with disclosed methods.
5. Expert judgment with relevant domain experience.
6. Analogy to comparable products with explicit differences.
7. Team belief or untested assumption.

Higher is not automatically better: telemetry can reveal what happened but not always why; interviews can reveal context but not population prevalence. Triangulate different evidence types.

## Confidence

Use qualitative confidence unless a calibrated probability is justified.

- **High:** multiple independent, relevant, recent sources or strong direct behavioral/financial evidence; material contradictions addressed.
- **Medium:** some relevant evidence but incomplete coverage, limited sample, aging data, or meaningful alternative explanations.
- **Low:** analogy, expert opinion, weak proxy, small biased sample, or untested assumption dominates.

Confidence is not enthusiasm. Do not convert labels to arbitrary percentages.

## Research and citation rules

- Browse whenever current facts could change the recommendation: competitors, product capabilities, prices, laws, standards, market conditions, funding, company status, or benchmarks.
- Prefer first-party and primary sources for factual claims. Use multiple sources when the decision benefits from triangulation.
- Record publication date and the date the underlying event/data covers when they differ.
- Cite the page that supports the specific claim, not a search result or homepage.
- Distinguish source statements from your inference.
- Do not treat vendor marketing as neutral evidence. It can verify what the vendor claims, not that the claim is true in practice.
- Do not use unsourced benchmark numbers as universal norms. Match geography, segment, business model, cohort definition, and period.

## Customer evidence

Never invent personas, interview quotes, needs, frequency, willingness to pay, or demand.

Classify customer evidence:

- observed behavior;
- actual purchase/renewal/churn;
- stated past behavior;
- stated current problem;
- hypothetical intent;
- team interpretation.

Treat hypothetical intent as weaker than commitment or behavior. Preserve minority and contradictory evidence rather than averaging it away.

For research plans, define:

- decision and population;
- recruitment/sampling logic;
- method and stimulus;
- evidence threshold;
- bias controls;
- analysis method;
- stop/continue rule.

Do not prescribe a universal interview count. Sample needs depend on heterogeneity, decision risk, method, and saturation or statistical design.

## Anti-hallucination checks

Before finalizing, search the draft for:

- exact market size with no source;
- competitor capability or price with no current evidence;
- invented customer quotation;
- “industry standard” with no definition/source;
- precise conversion, retention, CAC, LTV, churn, or timeline without data;
- arbitrary 30/60/90-day plans or payback horizons without capacity, dependency, deadline, or historical-cycle evidence;
- product-market fit declared from one metric;
- revenue presented as profit;
- scenario values with no driver;
- fake precision in scoring;
- causal language supported only by correlation.

Replace each with sourced evidence, an explicit assumption, a range, a symbolic model, or an Unknown.
