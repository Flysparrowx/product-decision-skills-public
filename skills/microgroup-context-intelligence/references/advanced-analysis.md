# Advanced Analysis

Use only the methods that can change the product decision. Start with manual evidence coding; add computation after the corpus and question justify it.

## Method router

| Need | Minimum basis | Method | Do not use when |
|---|---|---|---|
| Short-video culture | Relevant audio, frames, captions, overlays, and comments | Transcription + OCR + visual/audio coding | Captions alone are the only captured modality |
| Community structure | A meaningful relation and enough public/authorized entities | Network graph + cluster/bridge review | “Similarity” is based only on profile attributes |
| Place effects | Product decision depends on locality | Safe spatial aggregation + time/place comparison | Only individual or sparse location traces exist |
| Emerging trends | At least three comparable time windows | Normalized velocity, persistence, diffusion, change points | Corpus volume or collection method changed silently |
| Topic discovery | Hundreds of distinct items with recurring themes | Embedding/topic clustering + manual labeling | Tiny corpus; under roughly 100 items default to thematic coding |
| Lookalike discovery | Valid seed and explicit product-relevant axes | Prototype similarity + exclusions + human validation | Sensitive traits or individual targeting are required |

## Multimodal protocol

Treat each modality as separate evidence before synthesis:

```text
spoken words and tone
music/sound and remix lineage
caption and hashtags
on-screen text via OCR
visual composition, objects, gestures, colors, and symbols
comments, replies, and audience reinterpretation
platform format and recommendation context
```

Record the original item, timestamp/segment, extraction method, transcription/OCR uncertainty, and whether the signal came from the creator or audience. Never use face recognition, biometric inference, or identity matching.

## Network protocol

Define nodes and edges before analysis. Prefer public organizations, creators, venues, events, topics, and artifacts over private individuals.

Possible edges: reply, mention, collaboration, shared event, co-appearance, shared venue, or repeated topic. Do not mix edge meanings without labeling them.

Inspect:

- clusters and their boundary signals;
- bridge nodes and cross-group translators;
- centralization and dependence on one creator;
- peripheral/newcomer voices;
- negative or conflict edges;
- stability across time and platforms.

Algorithmic clusters are hypotheses. Compare them with manual coding and counterexamples.

## Geo-social protocol

Use the coarsest geography that still supports the decision. Aggregate to venue catchments, neighborhoods, or cells; never expose home/live locations.

Compare:

- active time windows and seasonality;
- anchor places, routes, waiting zones, and nearby services;
- local versus imported cultural signals;
- venue/event schedules against online activity;
- one target area with at least one comparable area;
- missing populations and visitor/tourist bias.

Do not treat geotag density as population density or a tag as proof of residence.

## Trend protocol

For each candidate calculate or assess:

```text
share of the comparable corpus, not raw mentions alone
velocity and acceleration
persistence across windows
source and creator diversity
cross-platform or cross-place diffusion
event, campaign, bot, or algorithm explanation
product relevance and reversibility
```

Keep the collection method stable. Mark breaks caused by API, search ranking, source coverage, or query changes. A change-point algorithm may flag a shift; only evidence explains it.

## Safe adoption policy

Do not install or copy external code by default. For every candidate inspect provenance, license, current maintenance, dependencies, permissions, network behavior, telemetry, storage, known issues, and exit path.

Prefer, in order:

1. copy the method as a cited procedure;
2. write a small standard-library check;
3. call an already-approved tool;
4. copy minimal code with license and commit provenance;
5. adopt a dependency only when the previous options fail.

Current references are `REFERENCE_ONLY` until a task-specific audit approves more:

| Project | Useful idea retained | Default decision |
|---|---|---|
| 4CAT / Zeeschuimer | Reproducible collection run, processor pipeline, explicit platform limitations | `REFERENCE_ONLY` |
| Minet | Source-adapter and normalization patterns | `REFERENCE_ONLY` |
| BERTopic | Multilingual/dynamic/multimodal topic discovery and small-corpus limits | `REFERENCE_ONLY` |
| NetworkX / Leiden | Graph construction, community and bridge hypotheses | `OPTIONAL_TOOL` |
| H3 / PySAL | Coarse spatial aggregation and spatial comparison | `OPTIONAL_TOOL` |
| ruptures | Change-point hypothesis generation | `OPTIONAL_TOOL` |
| QualCoder | Human qualitative coding across text, image, audio, and video | `OPTIONAL_TOOL` |

If code is copied, record project URL, exact commit, file/function, license, modifications, reviewer, and test evidence. Never copy code with an unclear or incompatible license.

## Human calibration

For `DEEP` work, ask group members or domain adults to review the interpretation without exposing other participants' data. Record agreements, disagreements, missing voices, and changed conclusions. Convert material corrections into regression cases.
