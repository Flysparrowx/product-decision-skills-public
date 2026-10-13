# Context-Aware Intake and Change Impact

Use this protocol before product discovery or recommendation when a project may already
have product context. The latest message is usually a delta, not a complete brief.

## 1. Resolve the bounded context

Use only relevant, authorized inputs:

1. the latest owner request;
2. approved project artifacts and decisions;
3. explicitly supplied current-product evidence such as a site, repository, analytics,
   support evidence or operating documents;
4. authorized fresh research required for the current decision.

Record provenance and freshness. Treat prior assistant-generated text as an inference
unless the owner adopted it or a source verifies it. Context is evidence, not authority.
Do not search unrelated projects or silently import another client's context.

Separate:

- what is established and should remain invariant;
- what the latest request explicitly changes;
- what is inferred;
- what is stale, conflicting or unknown;
- what evidence could change the current decision.

## 2. Classify impact before prescribing

Use one behavioral label in analysis. These labels describe the decision; they are not
permission to invent a runtime state or artifact.

| Label | Use when | Product response |
|---|---|---|
| `NEW_PRODUCT` | No prior product exists and the owner is starting a new one | Run risk-sized discovery |
| `EXISTING_PRODUCT_BASELINE` | A product exists but the factory has no accepted baseline | Reconstruct the smallest supported value and production system from current evidence |
| `NO_DISCOVERY_CHANGE` | Actor, problem, promise, target action, value mechanism, economics, production cycle and consequential boundaries remain unchanged | Preserve approved product meaning and constrain work to the requested surface |
| `MATERIAL_PRODUCT_CHANGE` | The request changes any of those product fundamentals | Keep implementation closed until the affected product decision is revised and approved |
| `NEEDS_DECISION` | Material inputs are missing, stale or conflicting and no source has authority to resolve them | Show the conflict and ask only the decision-changing question |
| `NON_PRODUCT_WORK` | A technical or operational defect is already isolated and the product intent remains unchanged | Route to the appropriate owner without product or audience research |

A redesign is not automatically cosmetic. Changing audience, offer, target action,
proof, customer-to-buyer mechanism, channel role or production responsibility is a
product change even when the request uses visual language.

## 3. Resolve conflicts without a fake source hierarchy

Do not assume that the newest, most detailed or most formal source is automatically
correct. For each conflict state:

- the competing claims and their provenance;
- freshness and whether either source is approved or owner-supplied;
- the affected decision;
- what can proceed unchanged;
- the smallest owner or evidence action that resolves it.

If the latest owner instruction clearly and knowingly supersedes an older decision,
treat it as a proposed material change, not silent evidence that history was wrong.

## 4. Ask less, but do not guess

Reuse facts already available. Ask at most three questions, only when an answer can
change, stop, narrow or defer the current decision. Do not ask broad discovery
questions to complete a template.

When more than one path is plausible, offer materially different options. For each
state what it preserves, changes, assumes, risks and unlocks. If one path dominates,
recommend it and briefly explain why the others are not viable; do not manufacture
three options for ceremony.

## 4a. Do not reduce a context-heavy product to a research request

For a new product whose value may depend on local language, culture, community or
place, do not answer only "research the audience". Before collecting context, make the
smallest product decision visible:

- the user, buyer/payer, beneficiary, target action and outcome still to be chosen;
- the end-to-end loop: promise or acquisition → value creation/production → delivery or
  publication → use → feedback/learning;
- which part of that loop is invariant and which creative, language, distribution or
  representation choices actually depend on local evidence;
- at least two materially different, reversible first-release configurations when the
  choice is consequential; and
- the accountable human decision after the evidence arrives.

Treat research, editorial/story judgment, local/member review, production quality and
distribution learning as capabilities or decision responsibilities. Do not turn each
one into a new agent, runtime component or technical architecture. Ask Microgroup
Context only for a named decision that it can change. It cannot substitute for product
definition, demand evidence, willingness to pay, production quality or outcome
measurement.

## 5. Make research conditional

State `Research: REQUIRED` or `Research: NOT_REQUIRED` and name the dependent decision.
Research only an unknown whose plausible resolution changes, stops, narrows or defers
that decision. Set an evidence budget and stop condition before collection. Continue
unaffected analysis.

When language, trust, place, culture, community or distribution may change the
decision, the CPO invokes the existing Microgroup Context method directly and remains
owner of the product decision and evidence synthesis. It is not a separate decision
owner or mandatory agent handoff. Cultural evidence does not prove market size, demand,
willingness to pay or causality. For minors or vulnerable
people, use an elevated, proportionate research gate: name an adult research owner,
state the decision that justifies direct participation, minimise collection and access,
and define applicable consent, retention and deletion rules. Consented, age-appropriate
interviews, creative sessions and observations may be valid evidence. Persistent
individual profiles, cross-platform matching, private route or friendship maps, and
person-level lookalikes are never defaults; use them only when they are demonstrably
necessary, explicitly authorized and subject to appropriate legal/ethical review.

## 6. Return a decision-ready answer

Make the response legible without forcing a new canonical artifact:

1. `Classification`;
2. context used and preserved invariants;
3. explicit delta and conflicts;
4. evidence labels and material unknowns;
5. research decision and bounded request when required;
6. recommendation or materially different options;
7. next human decision and what remains blocked.

Fail the response when it ignores available context, re-asks answered facts, silently
resolves a material conflict, invents customer evidence, turns research into ceremony,
or sends a material product change directly to design, architecture or build.
