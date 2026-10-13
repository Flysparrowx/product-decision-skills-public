# MicrogroupContextPack Contract

Return a concise executive layer first, followed by evidence and appendices. Markdown is the default; use equivalent versioned JSON/YAML when a machine-readable artifact is requested.

## Required structure

```markdown
# Microgroup Context Pack: <group>

## 1. Decision and scope
- Decision:
- Product/activity:
- Research depth: SCAN | STANDARD | DEEP
- Group definition:
- Geography/place:
- Time window and freshness cutoff:
- Included/excluded environments:
- Access and ethics classification:

## 2. Executive readout
- What this group is trying to achieve:
- Central tension:
- What matters now:
- Strongest product opportunity:
- Biggest misconception/risk:
- Recommendation: GO | REVISE | INSUFFICIENT EVIDENCE

## 3. Group boundary and microgroups
| Microgroup | Distinguishing behavior/context | Shared core | Evidence | Confidence |

## 4. Microgroup DNA
| Dimension | Finding | Evidence IDs | Counterevidence | Confidence |

Dimensions: shared situation, desired progress, values/trade-offs, identity boundary,
rituals/rhythms, language/humor, symbols/aesthetics, status/trust, places/platforms,
spending/decision dynamics, technology habits, current shifts.

## 5. Language and vibe lexicon
| Phrase/form | Meaning in context | Who/where uses it | Safe use: PRODUCT / INTERNAL ONLY / AVOID | Evidence |

## 6. Geo-social map
| Place/rhythm/network node | Role in group life | Online/offline link | Product relevance | Confidence |

## 7. Trend radar
| Candidate | SIGNAL/PATTERN/EMERGING/ESTABLISHED/FAD | Velocity | Persistence | Source diversity | Product fit | Evidence |

## 8. Lookalike discovery pack
- Seed definition:
- Similarity axes:
- Dissimilarity/exclusion axes:
- Adjacent audience hypotheses:
- Public ecosystem seeds or discovery queries:
- Validation tests:
- Forbidden matching criteria:

## 9. Product implications
| Decision surface | Do | Avoid | Evidence | Test/metric |

Decision surfaces: value proposition, features, onboarding, tone, content, visual direction,
distribution, partnerships, timing, pricing/offer, trust/safety.

## 10. Evidence ledger
| ID | Observation | Source/reference | Published/event date | Access date | Place | Bias/access note |

## 11. Confidence, contradictions, and unknowns
- High-confidence findings:
- Hypotheses:
- Negative cases/contradictions:
- Missing voices:
- Platform/sampling limitations:
- Unknowns:
- Expiry/refresh trigger:
- Next cheapest research step:
```

## Evidence and confidence rules

Use evidence IDs everywhere a conclusion appears.

### Confidence

- `HIGH`: direct and recent evidence, repeated across at least three independent source types/environments, with no material unresolved contradiction.
- `MEDIUM`: repeated evidence with one notable coverage, recency, or contradiction limitation.
- `LOW`: plausible but sparse, indirect, platform-bound, old, or contradicted evidence. Treat as a hypothesis.

Do not average confidence mechanically. One severe access or validity problem can keep confidence low.

### Evidence independence

Reposts, syndicated articles, copied reviews, and multiple accounts quoting one announcement count as one originating signal. Several comments under one creator's prompt are not automatically independent if the prompt shaped the response.

### Freshness

Attach one of:

- `LIVE`: days to weeks; volatile platform/trend signal;
- `CURRENT`: recent enough for the decision;
- `STRUCTURAL`: slow-changing norm supported over time;
- `STALE`: retain only as historical comparison.

Set an explicit refresh condition such as a season, event, platform change, launch, policy change, or 30/90/180-day interval.

## Product implication test

Accept an implication only when it states:

```text
because <evidence-backed context>
we should test/do <specific product decision>
for <microgroup and moment>
measured by <observable signal>
while avoiding <identified risk>
```

Reject implications that are generic, cannot be tested, or depend on mimicking surface slang without understanding its social role.

## Conditional CPO handoff

When the pack answers a `MicrogroupContextRequest`, keep the request's decision, behavioral group definition, geography, freshness need, decision surfaces, existing evidence, access/ethics boundary, evidence budget, and stop condition visible. Add a compact handoff table:

| Requested decision surface | CHANGED / UNCHANGED / UNSUPPORTED | Evidence IDs | CPO implication or open decision |
|---|---|---|---|

State the evidence boundary explicitly: the pack may support cultural, behavioral, trust, language, place, community, distribution, or conversion hypotheses, but it does not by itself prove market size, demand, willingness to pay, or causality.

## Sparse evidence and machine validation

A run may truthfully contain few or no observations when sources are unavailable. Return `INSUFFICIENT_EVIDENCE` with explicit limitations and a bounded next evidence request. Minimum SCAN/STANDARD/DEEP targets still apply to a claimed sufficient result; they are not a reason to fabricate evidence. The bundled validator checks core ledger IDs, links, access rules and depth floors for sufficient verdicts. It is not a full JSON Schema validator, source authenticity check, privacy sign-off or certificate of research sufficiency. `VALID STRUCTURE` means only those deterministic integrity checks passed.
