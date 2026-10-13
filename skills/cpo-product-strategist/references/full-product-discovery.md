# AI-Native Full-Product Discovery

Use this method to decide whether a coherent live product, rather than an interview, mockup, landing page, concierge test, technical spike, or partial MVP, should be the primary evidence vehicle.

## Doctrine

Optimize for trustworthy decision-relevant learning, not for the smallest artifact. AI-assisted creation can make a coherent product as cheap to build and rebuild as a traditional proxy. When the hypothesis depends on the integrated experience, a weaker proxy may be slower, less valid, or more expensive in total.

`Full product` means a complete end-to-end experience for one narrow segment, job, promise, and channel. It does not mean feature completeness, scale infrastructure, every role or integration, permanent architecture, or the long-term roadmap.

Keep the product coherent. Bound the audience, operational exposure, support promise, capital commitment, data access, and blast radius. Treat code, UX, positioning, and workflow as disposable research material until repeated value and viability evidence justify hardening.

## Test-vehicle decision

Compare candidate tests on:

- the claim and decision each test can update;
- fidelity to real discovery, onboarding, value realization, repeat behavior, payment, and delivery cost;
- time and cash to launch, observe, interpret, and rebuild—not generation time alone;
- operational, legal, safety, privacy, reputation, support, and partner exposure;
- reversibility and cost of false positive or false negative;
- usefulness of the resulting asset and learning if the thesis fails.

Prefer bounded Full-Product Discovery when all material conditions hold:

- build and rebuild cost is low relative to the decision;
- the product can be released to a bounded representative group;
- the value mechanism depends on an integrated end-to-end experience or repeated real behavior;
- instrumentation can observe the critical journey and economics;
- operational and downside exposure are limited and reversible;
- the team is willing to redesign or discard the product rather than defend sunk work.

Prefer a lighter or staged evidence vehicle when a credible proxy answers the decision sooner, or when real release creates disproportionate physical, clinical, legal, privacy, security, financial, contractual, reputational, partner, or operational exposure. Cheap code does not make the whole experiment cheap.

## Pre-launch contract

Before building or exposing the product, record:

| Field | Required treatment |
|---|---|
| Decision | Name what will change after the observation |
| Segment and job | Define the narrow user, context, trigger, and non-target |
| Product promise | State the end-to-end outcome the product must make possible |
| Load-bearing hypotheses | Separate problem, value, adoption, payment, channel, feasibility, and delivery-cost claims |
| Required completeness | Include only capabilities needed to deliver and observe the promise |
| Explicit exclusions | Exclude scale, platforms, roles, integrations, automation, and polish unrelated to the hypotheses |
| Critical journey | Define discovery, onboarding, first value, repeat value, commitment or payment, and failure paths |
| Instrumentation | Specify events, cohorts, denominators, qualitative evidence, costs, support load, and data quality |
| Exposure boundary | Limit audience, geography, data, spend, promises, support, integrations, and autonomy |
| Guardrails and fallback | Define safety, privacy, quality, human escalation, rollback, and manual continuity |
| Decision rule | Precommit `CONTINUE`, `NARROW`, `REDESIGN`, `PARTNER`, or `KILL` logic without inventing unsupported thresholds |

Do not require interviews or mockups as ceremonial prerequisites. Use them when they resolve a material uncertainty more efficiently or improve the live test. Existing research may shape the product, but only observed behavior, real commitment, economics, and appropriate direct evidence can support the corresponding claims.

## Learning loop

```text
Product thesis
→ coherent narrow product
→ bounded real exposure
→ observed journey, commitment, quality, cost, and unintended effects
→ separate adoption, value, experience, technical, GTM, and measurement failures
→ CONTINUE | NARROW | REDESIGN | PARTNER | KILL
→ rebuild or harden only what the next decision requires
```

Shipping is not evidence of value. Initial traffic, compliments, demo success, code quality, feature count, and model sophistication are not success criteria. Diagnose weak distribution or onboarding before declaring a value failure, but do not use those explanations indefinitely to protect the thesis.

## Factory-level measures

Track the factory by learning and decision quality, not products or code produced:

- time and total cost to observed representative behavior;
- cost per resolved decision-critical uncertainty;
- share of launches producing a clear continue, redesign, or kill decision;
- time from evidence to rebuild, narrow, or shutdown;
- repeated value, commitment or payment, delivery contribution, quality, and support burden where relevant;
- inventory and carrying cost of products with no active evidence path or owner.

Do not reward survival. A fast, well-evidenced kill can be a successful factory outcome.

## Boundaries

The CPO selects the evidence vehicle, defines product completeness, exposure, economics, measures, and decision gates. The Product Architect selects technical structure and produces the `ArchitectureSpec`. Do not turn Full-Product Discovery into permission for the CPO to prescribe services, agents, storage, deployment, or runtime topology.
