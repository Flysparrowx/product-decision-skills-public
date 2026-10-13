---
name: microgroup-context-intelligence
description: "Research and synthesize evidence-backed context for small, local, professional, interest-based, or online groups: lived reality, language and catchphrases, vibe, values, rituals, places, networks, tensions, status markers, microsegments, adjacent/lookalike audiences, and emerging trends. Use when a product, service, campaign, community, content format, AI agent, or vibe-coded application has a known target audience and needs a Microgroup Context Pack, microculture/DNA analysis, geo-social research, social listening, audience discovery, or privacy-safe lookalike profile strategy before product decisions are made."
---

# Microgroup Context Intelligence

Build a decision-ready picture of how a group actually lives, speaks, relates, and changes. Treat the result as a bounded research artifact, not a personality horoscope or a list of people to target.

## Operating contract

- Match the user's language unless asked otherwise.
- Separate `OBSERVATION`, `INTERPRETATION`, `HYPOTHESIS`, and `PRODUCT IMPLICATION`.
- Cite every material factual claim to traceable evidence and record collection/access dates.
- Prefer recent primary self-expression by group members. Triangulate across platforms, time periods, and source types.
- Report platform, sampling, location, access, and recency bias. Never claim statistical representativeness from convenience samples.
- Preserve contradictions and minority patterns. Do not collapse a group into one average persona.
- Build for the stated decision. Do not collect extra personal data “just in case.”
- Use public, consented, or otherwise authorized sources and compliant access methods. Public visibility does not remove ethical duties.

Read [references/source-playbook.md](references/source-playbook.md) before research involving social platforms, local venues, maps, reviews, or audience expansion. Read [references/advanced-analysis.md](references/advanced-analysis.md) for `STANDARD`/`DEEP` work involving video, network, geo, topic, or trend analysis. Read [references/methods-and-learning.md](references/methods-and-learning.md) when selecting methods or explaining the research basis. Use [references/output-contract.md](references/output-contract.md) for the final artifact. Use [references/evaluation.md](references/evaluation.md) to self-check a substantial result.

## Supplemental method selection

For community versus scene/audience/trend classification, read [sociology-and-microculture-foundations.md](references/sociology-and-microculture-foundations.md). For interaction episodes, communication grammar and cohesion, read [conversation-and-cohesion-protocol.md](references/conversation-and-cohesion-protocol.md). For cross-city functional analogues, read [cross-city-expansion-protocol.md](references/cross-city-expansion-protocol.md). These lenses require evidence and local validation; style, hashtags, follower overlap and personality typing cannot establish membership. These methodological supplements do not replace the main CPO handoff or research-run validator.

## Choose the research depth

Select the smallest depth that can support the decision. State the choice.

| Depth | Use | Minimum evidence target |
|---|---|---|
| `SCAN` | Early hypothesis, naming, or product workshop | 6 independent signals, 3 source types, at least 2 recent signals |
| `STANDARD` | Product brief, positioning, UX, content, or go-to-market decision | 15 independent signals, 3 source types, 2 environments/platforms, 5 distinct voices/entities when available |
| `DEEP` | Expensive build, sensitive group, market entry, or high-impact decision | Multi-method research, explicit sampling plan, first-party validation, saturation log, human review |

Treat these as floors, not proof of quality. Tiny groups may have fewer public voices; lower confidence instead of fabricating breadth.

## Workflow

### 1. Frame the decision

Extract or state assumptions for:

```text
decision to inform
product or activity
target group and current evidence
geography and meaningful places
time horizon and required freshness
online/offline environments
known exclusions and adjacent groups
available first-party data
research depth
```

If the user only provides a broad demographic, turn it into a provisional behavioral definition. “Women 25–40” is not a community; “new mothers in Kazan who coordinate stroller walks through neighborhood chats” can be researched as one.

### 2. Run the ethics and access gate

Before collection, classify the work as `LOW`, `ELEVATED`, or `STOP` risk.

`STOP` or require explicit human/legal review when the request depends on:

- identifying, contacting, ranking, or exposing minors or vulnerable individuals;
- face recognition, cross-platform identity resolution, doxxing, precise movement tracking, or deanonymization;
- inferring health, religion, ethnicity, sexuality, political beliefs, financial distress, or other sensitive traits about individuals;
- entering closed/private groups deceptively or bypassing platform controls;
- scraping or storing data contrary to law, terms, community expectations, or consent;
- targeting people for manipulation, discrimination, exclusion, or high-impact decisions.

For groups likely to include minors—such as gymnasts at one gym—use only aggregate patterns from authorized adults, public organizational materials, consented interviews, and non-identifying observations. Require a named adult research owner; obtain guardian consent and participant assent for direct participation when applicable; define restricted access, retention, and deletion before collection. Do not enumerate or name child profiles, quote identifiable children, infer family routines, or use a minor as a public lookalike exemplar even when the profile is visible.

For lookalike work, default to archetypes, public organizations/creators, search motifs, and aggregate attributes. Use first-party identifiers only with valid consent and a platform-native compliant workflow.

### 3. Define the group as intersecting coordinates

Describe the group through evidence-bearing coordinates:

```text
shared activity, problem, identity, or aspiration
role or life/work stage
place, venue, route, or locality
time rhythm or event cycle
platforms and communication spaces
relationships and gatekeepers
membership/boundary signals
```

Do not split into microgroups merely because clustering is possible. Recognize a microgroup when several recurring signals align: shared vocabulary, repeated interaction, common place or ritual, recognizable boundaries, and a distinct tension or goal.

### 4. Build a source map

Create a coverage matrix before searching:

- direct voices: interviews, support conversations, diaries, community posts, comments;
- behavior: product analytics, event attendance, transactions, search interest, repeated routines;
- place: venue pages, schedules, reviews, maps, neighboring businesses, local events and media;
- network: mentions, collaborations, replies, memberships, public organizers and bridging accounts;
- culture: phrases, jokes, memes, symbols, aesthetics, taboos, heroes, villains, origin stories;
- comparison: adjacent groups, former members, newcomers, skeptics, and counterexamples.

Do not treat one platform as the group. Platform mechanics select what becomes visible.

### 5. Collect an evidence ledger

For every retained item record:

```text
evidence_id
observation or short compliant quote
source URL/reference and source type
author/entity class, never unnecessary identity data
published/event date and access date
place/geographic precision
group relevance
freshness
confidence
ethical/access note
```

Keep an immersion journal: record the research path, evolving vocabulary, surprises, researcher assumptions, platform effects, and reasons sources were included or rejected.

For a reproducible machine-readable run, write JSON conforming to [references/research-run.schema.json](references/research-run.schema.json) and validate it with `python scripts/validate_research_run.py <run.json>`. The validator uses only the Python standard library.

Expand queries iteratively from self-labels, place names, recurring phrases, rituals, public organizers, events, complaints, aspirations, and local spelling/transliteration variants. Preserve original-language phrases and add a plain-language gloss.

### 6. Apply the geo-social lens

For place-bound groups map:

- anchor places and the practical catchment area;
- routes, transport, waiting zones, nearby services, and friction points;
- weekday/weekend and seasonal rhythms;
- scheduled events and unscheduled gathering moments;
- local institutions, businesses, organizers, and trusted intermediaries;
- how online coordination changes offline behavior and vice versa;
- which signals are genuinely local versus imported from a wider internet culture.

Aggregate precise location evidence. Never publish an individual's home, routine, or live location.

### 7. Code the culture and discover microgroups

Code evidence across these lenses:

```text
jobs and desired progress
recurring tensions, fears, frictions, and workarounds
values, non-negotiables, and trade-offs
belonging and boundary markers
rituals, routines, milestones, and seasonal moments
language, phrases, humor, metaphors, and taboo words
symbols, objects, aesthetics, sounds, and visual codes
status markers, competence signals, heroes, and gatekeepers
trust and distrust channels
spending, access, and decision dynamics
technology and platform habits
places, routes, time rhythms, and local constraints
```

Cluster only after coding. Compare each proposed microgroup with at least one adjacent cluster and one negative case. Name clusters in neutral, descriptive language.

### 8. Build privacy-safe lookalike discovery

Translate a useful seed group into similarity dimensions rather than a list of identities:

- shared activity and behavior;
- role/stage and desired progress;
- language and recurring topics;
- place type and mobility pattern at safe granularity;
- rituals, tools, content formats, and trusted sources;
- public affiliations, events, organizations, or creator ecosystems;
- product-relevant constraints and value signals.

Exclude protected or sensitive traits unless the user has a lawful, necessary, consented research basis and human approval. Produce:

1. adjacent audience hypotheses;
2. discovery queries and public ecosystem seeds;
3. similarity and dissimilarity axes;
4. validation tests;
5. explicit forbidden matching criteria.

Public exemplars may be named only when they are organizations, businesses, public professionals, or creators and naming them is necessary and low risk. Otherwise report patterns, not handles.

### 9. Distinguish signals from trends

Classify:

- `SIGNAL`: isolated but potentially meaningful;
- `PATTERN`: repeated across evidence or time;
- `EMERGING TREND`: accelerating pattern spreading across sources or adjacent groups;
- `ESTABLISHED NORM`: stable baseline behavior;
- `FAD/NOISE`: short spike, coordinated promotion, or platform artifact.

Score each candidate on velocity, persistence, source diversity, cross-platform spread, local relevance, and product fit. Use Google Trends or platform metrics as directional evidence, never as a poll or proof of causality.

### 10. Synthesize Microgroup DNA

Express DNA as an evidence-backed system, not adjectives:

```text
shared situation and central tension
desired progress
collective story and identity boundary
values and trade-offs
rituals and rhythms
language and humor
symbols and aesthetics
status and trust system
places and digital habitats
current shifts and trend pressures
internal microgroups and contradictions
```

For every conclusion show supporting evidence IDs, confidence, and counterevidence.

### 11. Translate context into product action

Connect findings directly to:

- product concept and value proposition;
- feature priorities and excluded features;
- onboarding, interaction model, and trust design;
- language, content, visual direction, and tone boundaries;
- distribution, partnerships, creators, venues, and community hooks;
- pricing, offer structure, timing, and purchase friction;
- experiments, metrics, and failure signals;
- safety, appropriation, stereotyping, and reputation risks.

Do not imitate slang mechanically. Explain when a phrase is safe for product language, useful only for internal understanding, or likely to feel invasive/cringe when used by an outsider.

### 12. Deliver and stop responsibly

Use the `MicrogroupContextPack` in [references/output-contract.md](references/output-contract.md). End with:

- high-confidence findings;
- hypotheses requiring validation;
- unknowns and blind spots;
- freshness/expiry notes;
- next cheapest research step;
- clear `GO`, `REVISE`, or `INSUFFICIENT EVIDENCE` recommendation for the stated decision.

Stop collection when new evidence no longer changes the codebook or decisions, major source classes are covered, contradictions are understood, and another collection cycle has low expected information gain. “Many posts” is not saturation.

### CPO handoff

When invoked from `cpo-product-strategist`, require a bounded `MicrogroupContextRequest` with the decision, provisional behavioral group definition, geography, freshness need, decision surfaces, existing evidence, access/ethics boundary, evidence budget, and stop condition. If a material field is missing, return it as an explicit evidence request instead of widening the research silently.

Return one `MicrogroupContextPack` bound to that decision. In the executive layer, state which requested decision surfaces the evidence changes, does not change, or cannot yet support. Preserve `OBSERVATION`, `INTERPRETATION`, `HYPOTHESIS`, confidence, contradictions, provenance, freshness, and expiry so the CPO can use the pack without turning it into a persona or market fact. The pack informs product choices; it does not prove market size, demand, willingness to pay, or causality.

## Independent operation and structured return

Work directly from the user’s decision when used independently; a CPO invocation is optional. Never call CPO or BI recursively. If no browsing or authorized research source is accessible, deliver a research plan and an explicit evidence gap, not a completed research finding. Do not treat evidence-volume targets as permission to fabricate sources.

Every return distinguishes observations with source IDs, sources with dates/access status, interpretations, hypotheses, contradictions, limits and the decision implications. Qualitative observations and convenience samples are never representative statistics, proof of demand or causal effects. A missing voice remains missing. See the output contract for the full schema.

## Quality gate

Do not mark the pack ready unless all are true:

- every major claim is traceable to evidence;
- at least three source types or a documented limitation are present;
- recency and geography match the decision;
- observation and inference are visibly separated;
- contradictions and missing voices are preserved;
- microgroups differ on behavior/context, not decorative demographics;
- lookalike logic is aggregate, auditable, and privacy-safe;
- product recommendations follow from the evidence;
- no stereotype, fabricated quote, sensitive inference, or false representativeness remains;
- the pack declares uncertainty and an expiry/refresh trigger.
