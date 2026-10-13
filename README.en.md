# Product Decision Skills — by Ksenia Vorobeva

**Choose what to build next — with a clearer view of your business, data and customers.**

Three independent Agent Skills for founders, product leaders, analysts and researchers. Turn a difficult question into something you can use: a comparison of strategic options, a readable chart or audience context that changes your product choice. Install the skill you need, or all three.

[По-русски](README.md) · [Short cards / Короткие карточки](SKILL-CARDS.md) · [Examples with inputs and outputs](examples/README.md)

## Pick the skill for your question

### CPO Product Strategist — decide what to build, who it serves and why

**Should you change the product, price, business model or how value gets delivered?** Compare options, connect customer value to business economics and identify the evidence needed to decide. The skill handles a narrow choice or a broader product/company redesign, with the scope shaped by the decision.

**Bring:** the decision, current model, available facts and numbers, constraints and options. **Get:** a decision brief with alternatives, trade-offs, a recommendation, economic conditions and the next evidence check. When inputs are missing, it identifies what you need to establish before committing resources.

[Skill instructions](skills/cpo-product-strategist/SKILL.md)

### Data Visualization & BI — turn your data into a clear business picture

**What changed, where is the gap and which values are comparable?** Choose charts around the business question and design a readable BI dashboard. A bundled local tool creates ready-to-use charts from the data you supply.

**Bring:** data, units, periods, provenance and the question the chart must answer. **Get:** an SVG for supported chart forms or a chart/dashboard specification covering layout, scales, labels, filters and reading rules.

[Skill instructions](skills/data-visualization-bi/SKILL.md)

### Microgroup Context Intelligence — understand your audience beyond age and interests

**Why does a specific group trust some offers and overlook others?** Explore the language, habits, places, relationships, norms and tensions of a small local, professional or online audience. Use it when those details affect positioning, product experience, communication or distribution.

**Bring:** the group and geography, product decision, time window and available observations or authorized sources. **Get:** an audience portrait: how people speak, whom they trust, what gets in the way of choosing your product and which hypotheses to test. Findings are tied to observations and sources, with differences within the group kept visible.

[Skill instructions](skills/microgroup-context-intelligence/SKILL.md)

## Try one question

These prompts use synthetic inputs. Replace them with your own materials for a real decision.

**Product choice**

```text
$cpo-product-strategist
Teaching case: a booking service sends email reminders. The team wants
SMS, but has no evidence about no-show causes or SMS costs yet.
Compare retaining email with adding SMS. What can we decide now,
which economic conditions need checking, and what evidence is missing?
Write a short founder decision brief without inventing numbers.
```

**Chart from data**

```text
$data-visualization-bi
Synthetic data: monthly change in active accounts — January 10,
February missing, March 0, April −2. Create a static SVG with exact
labels. Keep missing distinct from zero, preserve the negative value
and explain which comparisons these observations support.
```

**Audience context**

```text
$microgroup-context-intelligence
Teaching case: choose a booking method for an adult neighborhood repair
club. Three synthetic notes: one member prefers booking through the
organizer; another asks for an app; the organizer says newcomers value
meeting in person. Create a bounded context pack: observations,
contradictions, hypotheses and validation questions. Add no observations
and make no claims about how common these preferences are.
```

The [complete examples](examples/README.md) include supplied inputs and saved outputs from earlier independent executions. All data is synthetic. These illustrate the work; they are neither guarantees nor new evaluations.

## Install one skill or all three

Unzip the package and open a terminal in its extracted root. These commands create an example project and copy **complete skill folders**, including their supporting files:

```sh
project="$PWD/example project"
mkdir -p "$project/.agents/skills"
cp -R skills/cpo-product-strategist skills/data-visualization-bi skills/microgroup-context-intelligence "$project/.agents/skills/"
```

For your project, change the path in the first line. To install one skill, keep only its source folder in `cp -R`. Review existing destination folders before copying. Your Agent Skills host must support `.agents/skills`; explicit `$skill-name` invocation and automatic discovery depend on the host.

Local tools require Python 3, with no third-party packages or accounts:

```sh
python3 "$project/.agents/skills/data-visualization-bi/scripts/render_chart.py" examples/bi/supplied.json "$project/chart.svg"
python3 "$project/.agents/skills/microgroup-context-intelligence/scripts/validate_research_run.py" demos/audience-discovery/research.json
```

The first creates a chart. The second helps check research-ledger integrity.

## Use them together

Start with a CPO decision. Add BI when a quantitative comparison affects the choice, and Microgroup when audience context matters. Each skill also works independently. Companion dispatch requires host support; installing three folders does not establish that runtime capability. End-to-end orchestration across hosts remains unverified.

Additional [company analysis](demos/company-analysis/README.md), [audience discovery](demos/audience-discovery/README.md) and [strategic decision](demos/strategic-decision/README.md) demonstrations are authored synthetic integration artifacts, not recordings of multi-agent execution.

## Capabilities and limits

The local BI tool creates static SVG bars or lines, preserving missing observations, zeros and negatives; see the [contract](skills/data-visualization-bi/references/renderer-contract.md). Other chart forms and interactive dashboards need suitable tools. Microgroup does not invent interviews or infer prevalence or proven demand from sparse samples. Its validator checks ledger integrity, not source authenticity or full schema compliance.

## Package and licenses

The package contains skills, examples, demonstrations and `SHA256SUMS`. Rebuild with `python3 scripts/build_package.py`.

Ksenia Vorobeva’s contributions use [Apache-2.0](LICENSE). The Strategy Red-Team adaptation retains its [MIT terms and notice](THIRD-PARTY-NOTICES.txt); see [attribution](ATTRIBUTION.md). Release: [v0.1.0](https://github.com/Flysparrowx/product-decision-skills-public/releases/tag/v0.1.0) · [ZIP package](https://github.com/Flysparrowx/product-decision-skills-public/releases/download/v0.1.0/product-decision-skills-v0.1.0.zip) · [publication notice](PUBLICATION-NOTICE.md).
