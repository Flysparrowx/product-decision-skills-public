# Infographic Expression

## Contents

1. Output contract
2. Choose the medium
3. Choose the visual grammar
4. Distill the thought
5. Build information hierarchy
6. Preserve evidence and uncertainty
7. Compose and style
8. Produce the artifact
9. Run visual QA
10. Completion gate

## 1. Output contract

When the user asks for an infographic, visual explainer, information map, large visual summary, or says that prose is hard to perceive, create the actual visual artifact unless the user explicitly requests only a concept or wireframe.

An infographic is an information system, not decorated prose. It must make a relationship easier to perceive: comparison, sequence, causality, hierarchy, system structure, geography, scale, composition, or change over time.

Before production, establish or infer:

- audience and the decision, understanding, or action the artifact should enable;
- one-sentence thesis;
- medium, aspect ratio, editability, reading setting, and expected viewing size;
- verified evidence, supplied data, assumptions, unknowns, and sources;
- brand, template, language, accessibility, confidentiality, and style constraints.

Ask only when a missing answer materially changes the artifact. Otherwise make a reversible assumption, state it briefly, and proceed.

## 2. Choose the medium

| Need | Preferred route |
|---|---|
| Compact static relationship inside the answer | Mermaid when labeled nodes and edges are sufficient |
| Interactive comparison, scenario, map, simulation, or exploration | `visualize` |
| Editable executive infographic or live presentation | `Presentations`, usually one or two slides |
| Print, email, or fixed-layout distribution | `pdf`, often with an editable source when useful |
| Precise chart from numeric data | chart-capable presentation, spreadsheet, or visualization workflow |
| Aesthetic illustration or metaphor without exact data | `imagegen` |

Do not use generated raster imagery to represent exact numbers, axes, labels, causal structure, or decision logic. Do not force an interactive HTML surface when a compact static diagram is clearer.

If format is unspecified, choose the smallest medium that preserves the intended reading experience. For executive strategy, default to an editable single-slide or two-slide visual. For exploratory scenarios, prefer an in-conversation interactive view. For asynchronous distribution, prefer a readable PDF.

## 3. Choose the visual grammar

Choose by relationship, not by visual fashion:

| Relationship to communicate | Suitable grammar |
|---|---|
| Before → after or staged change | transition, timeline, or state sequence |
| Cause → mechanism → outcome | causal chain, driver tree, or value loop |
| Several exact alternatives | comparison table or aligned small multiples |
| Two decision dimensions | matrix or frontier, only with defensible placement |
| Part → whole | stacked composition, treemap, or nested hierarchy |
| Ownership, layers, or dependencies | hierarchy, architecture, or system map |
| Process and handoffs | flow or swimlane |
| Branching choices | decision tree or scenario branches |
| Quantitative trend | line, area, or slope chart |
| Ranked magnitude | ordered bars or dot plot |
| Distribution or uncertainty | histogram, interval plot, box plot, or sensitivity view |
| Geography | sourced map with verified geometry |
| Multiple models with the same dimensions | small multiples with shared visual scales |

Do not use a 2×2, radar chart, funnel, timeline, map, or flowchart merely because it looks strategic. Every axis, position, area, arrow, and color must have a defined meaning.

## 4. Distill the thought

Build the content layer before styling:

1. State the thesis as a conclusion, not a topic.
2. Identify the audience question the visual must resolve.
3. Select three to seven supporting claims that are necessary to understand or act on the thesis.
4. Attach evidence status and source to every material claim.
5. Identify the relationship among claims and select one dominant visual grammar.
6. Remove detail that does not change interpretation, choice, or action.
7. Move calculations, definitions, and source detail to an appendix or companion artifact when needed.

Do not reproduce the order of the source document or conversation. Reconstruct the logic around the audience's reading path.

## 5. Build information hierarchy

Design for three reading depths:

- **Five seconds:** the thesis and dominant pattern are obvious.
- **Thirty seconds:** the reader understands the main structure, comparison, or causal mechanism.
- **Two minutes:** the reader can inspect evidence, assumptions, exceptions, and the next decision.

Use:

- one dominant message and one primary visual field;
- four to seven semantic zones for a one-page infographic;
- short conclusion labels rather than section headings;
- direct labels on marks, paths, and objects rather than distant legends;
- progressive disclosure through scale, position, grouping, and reading order;
- no more than 250 audience-visible words on a one-page executive infographic unless the format and viewing distance justify more.

Avoid paragraphs, tiny footnotes, repeated equal-weight cards, icon grids, decorative badges, redundant legends, and several unrelated visual grammars competing on one page.

## 6. Preserve evidence and uncertainty

Use real supplied or cited data for quantitative charts. Show units, period, population, definition, and source. Never invent values to complete a chart.

For qualitative diagrams:

- label conceptual placement, inferred causality, assumptions, and unknowns;
- do not make line thickness, bubble size, area, distance, or chronology imply measurement unless measured;
- distinguish verified evidence from inference and proposed design;
- keep caveats near the claim they qualify rather than hiding them in a footer.

When data is missing, visualize a formula, threshold, range supported by inputs, evidence gap, or decision gate instead of a fabricated number.

## 7. Compose and style

Translate the requested mood into operational design decisions: grid, spacing, type hierarchy, line weight, palette, contrast, image treatment, and density. Do not imitate a style through decorative clichés.

For example, `Japanese minimalism` should normally mean disciplined whitespace, asymmetric balance, a restrained grid, fine rules, a limited neutral palette, one purposeful accent, and careful typography—not ornamental kanji, lanterns, waves, or unrelated cultural motifs.

Keep color semantic. Use one accent for the pivotal choice or active path; add category colors only when they remain stable and necessary. Use icons only when they speed recognition and share one visual language.

## 8. Produce the artifact

Create the final artifact with the skill appropriate to the requested medium and obey that skill's file, implementation, accessibility, and rendering requirements.

For an editable presentation infographic:

- create the actual `.pptx`;
- preserve editability for text, labels, charts, and simple shapes;
- use searched or generated imagery only when it adds meaning;
- do not rasterize the entire information layer into one opaque image.

For a PDF, preserve readable text and links when possible. For an interactive view, keep controls minimal and let the information relationship dominate.

## 9. Run visual QA

Inspect the final rendered artifact, not only its source or successful export status.

Check:

- thesis recognition at thumbnail size;
- reading order and grouping;
- legibility at the actual viewing size;
- wrapping, clipping, overlaps, contrast, and source readability;
- consistent encodings, labels, scales, and arrow meanings;
- grayscale and color-independent comprehension where practical;
- whether the visual still works without oral explanation;
- whether dense areas can be cut, split, or moved instead of shrinking type.

Inspect full size and overview. If mobile, print, or projection matters, inspect that mode too. Revise and rerender every material failure.

## 10. Completion gate

Do not call the infographic complete unless:

- it answers the audience's question and makes one relationship materially clearer than prose;
- the chosen grammar matches the information;
- facts, data, assumptions, and unknowns remain distinguishable;
- the actual requested artifact exists and has been rendered or previewed;
- visual QA was performed on the exact final version;
- the file can be understood at the intended size without reading a report aloud.
