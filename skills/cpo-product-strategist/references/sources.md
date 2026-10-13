# Framework Sources and Audited Community Skills

Use this file to trace concepts to original authors or authoritative maintainers. Verify current pages when a claim is material. These links are starting points, not blanket endorsements.

## Core framework sources

| Area | Source | Link |
|---|---|---|
| Business Model Canvas | Strategyzer | https://www.strategyzer.com/library/the-business-model-canvas |
| Value Proposition Canvas | Strategyzer | https://www.strategyzer.com/library/the-value-proposition-canvas |
| Opportunity Solution Trees / continuous discovery | Teresa Torres, Product Talk | https://www.producttalk.org/opportunity-solution-trees/ |
| Product operating model | Silicon Valley Product Group | https://www.svpg.com/the-product-operating-model-an-introduction/ |
| Product strategy | Silicon Valley Product Group | https://www.svpg.com/product-strategy-overview/ |
| Positioning components | April Dunford | https://www.aprildunford.com/post/an-introduction-to-positioning |
| RICE | Intercom, Sean McBride | https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/ |
| North Star framework | Amplitude | https://amplitude.com/books/north-star |
| Shape Up | Basecamp | https://basecamp.com/shapeup |
| Team Topologies | Matthew Skelton and Manuel Pais | https://teamtopologies.com/key-concepts |
| Software delivery and operational performance | DORA | https://dora.dev/guides/dora-metrics-four-keys/ |
| Web accessibility | W3C Web Accessibility Initiative, WCAG | https://www.w3.org/WAI/standards-guidelines/wcag/ |
| Application security verification | OWASP ASVS | https://owasp.org/www-project-application-security-verification-standard/ |
| Wardley Mapping | Simon Wardley | https://learnwardleymapping.com/ |
| Scenario planning | Shell Scenarios | https://www.shell.com/news-and-insights/scenarios.html |
| Lean Startup | Eric Ries | https://theleanstartup.com/principles |
| Jobs to Be Done | Clayton Christensen Institute | https://www.christenseninstitute.org/theory/jobs-to-be-done/ |
| Working Backwards | Amazon/AWS materials | https://aws.amazon.com/executive-insights/content/working-backwards-to-invent-on-behalf-of-customers/ |
| OKRs | What Matters / John Doerr resources | https://www.whatmatters.com/faqs/okr-meaning-definition-example |

Book-derived frameworks such as the strategy kernel (Richard Rumelt), Playing to Win (A.G. Lafley and Roger Martin), Seven Powers (Hamilton Helmer), and pricing research texts should be named and summarized at a high level. Do not reproduce substantial copyrighted passages or proprietary templates.

## Audited community skills

These community skills are recorded influences on the capability gap analysis, not authoritative framework sources. The precise history of smaller adaptations is incomplete. The strategy red-team procedure is treated as an adaptation of Paweł Huryn’s MIT-licensed skill; the package ATTRIBUTION.md and THIRD-PARTY-NOTICES.txt identify its scope and preserve the terms. Other named sources remain methodological references; this is not permission to reproduce their text.

| Skill/repository | Useful strength observed | Limitation addressed here |
|---|---|---|
| CPO Advisor | CPO-level portfolio, PMF, metrics, and org orientation | Some benchmark-like rules require source/context; narrower scaling-company focus |
| Product Manager Skills / Product Strategy Session | End-to-end orchestration from positioning through roadmap | Depends on a large suite of component skills and can become workshop-heavy |
| PM Skills Marketplace by Paweł Huryn | Broad modular library spanning discovery, strategy, market research, analytics, GTM, execution, and a strong strategy red-team | Audited as untrusted reference content at commit `18468a95b427e70e258b51389796367c6f684e7d`; it is a PM toolkit rather than a single CPO orchestrator, and some modules contain generic numeric heuristics that require stronger evidence and permission gates |
| Product Manager Toolkit | Practical RICE, discovery, PRD, and GTM utilities | PM execution toolkit is not a complete CPO strategy/economics system |
| Product Skills collection | Broad framework catalog and pattern-oriented progressive disclosure | Individual framework skills still need a decision router and evidence contract |

Repository links:

- https://github.com/alirezarezvani/claude-skills/tree/main/c-level-advisor/skills/cpo-advisor
- https://github.com/deanpeters/Product-Manager-Skills
- https://github.com/phuryn/pm-skills
- https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/skills/business-marketing/product-manager-toolkit
- https://github.com/wdavidturner/product-skills

## Russian-language product practice sources

Treat these as practitioner and editorial sources that can surface useful questions, cases, and operating patterns. They do not establish universal benchmarks or causal claims by themselves. Trace consequential methods to stronger primary/statistical sources where possible.

| Source | Useful lens retained | Guardrail |
|---|---|---|
| GoPractice (`@gopractice`) | Cohort and segment discipline, correlation-versus-causation, experiment integrity, stage-appropriate analytics, and decision-specific dashboards | Educational/editorial material; verify statistical design and never import example metrics as norms |
| Epic Growth (`@epicgrowth`) | Activation as experienced value, systematic growth experiments, growth loops, narrow AI use cases, real-query evaluation, and economics of scaling | Conference/community cases are prompts for hypotheses, not proof of transferability |
| ProductSense (`@productsense`) | Strategy as daily choices, company-to-product alignment, investment mix, decision ownership, single source of truth, and evidence/decision/roadmap review cadences | Company cases illustrate operating options; adapt cadence and structure to stage, risk, and organization |
| Strategists' chat (`@stratchat`) | Not incorporated: no public web preview was accessible during review | Do not attribute methods to this chat without a user-supplied export or accessible primary material |

Reviewed starting points:

- https://t.me/gopractice
- https://gopractice.ru/data/correlation-vs-causation/
- https://gopractice.ru/data/ab-tests-guide/
- https://gopractice.ru/data/creating-dashboards-guide/
- https://t.me/s/epicgrowth
- https://t.me/s/productsense
- https://productsense.io/workshops/product-strategy
- https://sense23.com/post/kak-v-wrike-sinhroniziruyut-strategiyu-kompanii-kvartalnye-tseli-i-zadachi-na-sprint
- https://sense23.com/academy/video/product-operations-chto-eto-takoe-i-kuda-dvizhetsya-mir-produktovyh-speczialnostej-ilya-tregubov-head-of-product-operations-pandadoc/
- https://sense23.com/post/pyat-printsipov-dlya-postroeniya-protsessov-v-kompanii-na-etape-rosta

## Agentic-product and China-pattern starting points

These sources establish observable mechanisms and evaluation patterns, not universal benchmarks. Recheck current documentation, price cards, contracts, filings, regulation, and product behavior before using any number in a decision.

| Area | Primary or research starting point | Use |
|---|---|---|
| Agent trajectory evaluation | Google Cloud Vertex AI agent evaluation | Distinguish final outcome from action sequence, tool selection, ordering, precision, and recall |
| Outcome-linked agent evaluation | Nubank production agent framework | Connect offline evaluation, human reference, online outcome, and production iteration |
| Long-horizon delegated work | OpenAI agentic-work research | Understand the shift from short interactions to delegated tasks; do not treat runtime or tokens as value by themselves |
| Mini Programs and ecosystem transactions | Tencent/Weixin official disclosures | Examine embedded acquisition, service, payment, repeat use, merchant value, and platform dependency |
| Instant retail | Meituan official operating disclosures | Examine assortment, density, fulfillment, delivery certainty, participant health, and unit economics |
| AI, commerce, and instant-retail investment | Alibaba Group results and filings | Examine user growth together with AI adoption, unit economics, investment, cash flow, and ecosystem effects |

Starting points:

- https://cloud.google.com/blog/products/ai-machine-learning/introducing-agent-evaluation-in-vertex-ai-gen-ai-evaluation-service
- https://arxiv.org/abs/2606.08867
- https://openai.com/index/how-agents-are-transforming-work/
- https://www.tencent.com/en-us/articles/2202317.html
- https://www.meituan.com/news/NN250718108001691
- https://www.alibabagroup.com/zh-HK/document-1929990445136347136
