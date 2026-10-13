# AI and Agent FinOps

## Contents

1. Scope and accounting boundary
2. Cost taxonomy and P&L mapping
3. Telemetry and allocation
4. Unit economics
5. Bottom-up forecast
6. Capacity, commitments, and cash
7. Scenarios and variance
8. Deliverable and controls

## 1. Scope and accounting boundary

Build three connected but distinct views:

1. **Operational consumption:** tokens, model calls, tool calls, storage, compute time, retries, evaluations, and human work.
2. **Product economics:** cost and contribution per attempt, completed task, accepted outcome, customer, cohort, and product.
3. **Financial reporting:** revenue, cost of revenue/COGS, R&D, sales and marketing, G&A, operating result, cash commitments, and vendor liabilities.

Management allocation and statutory accounting are not interchangeable. State entity, jurisdiction, accounting standard, management policy, accrual/cash basis, tax/VAT treatment, currency, and reporting period. For capitalization, transfer pricing, material commitments, or statutory classification, require the company's accounting policy and qualified finance/accounting review; do not make a legal accounting determination from a generic framework.

## 2. Cost taxonomy and P&L mapping

Classify first by purpose and cost behavior, then map to the approved chart of accounts.

| Cost pool | Typical examples | Management P&L candidate | Allocation basis |
|---|---|---|---|
| Production inference | input/output/cached tokens, dedicated serving, batch inference | cost of revenue/COGS | metered use by product/customer/outcome |
| Production tools and data | search, browser, API calls, vector/database operations, licensed data, egress | cost of revenue/COGS | call, byte, record, workflow, or attributable use |
| Production human operations | review, escalation, moderation, exception handling | cost of revenue/COGS when tied to delivery | minutes/cases by outcome or cohort |
| Shared serving platform | gateways, observability, routing, security, on-call serving operations | COGS or allocated serving overhead per policy | capacity, calls, tokens, runtime, or direct trace |
| Product and model development | experiments, prompt/retrieval development, eval creation, prototypes, engineering | R&D/product development unless policy says otherwise | project, environment, team time, experiment tags |
| Customer implementation/support | onboarding, configuration, support, success | COGS or sales/service expense per policy | customer time/cases/contracts |
| Acquisition and sales | demos, presales pilots, sales-specific AI use | sales and marketing | campaign, opportunity, account, or team |
| Corporate AI | internal assistants for finance, legal, HR, administration | G&A by function | seat, team, workflow, or metered use |
| Commitments and fixed capacity | minimum spend, reserved capacity, dedicated clusters, platform licences | relevant function plus unused-capacity disclosure | consumed versus idle/committed capacity |

Do not put every vendor invoice into one `AI` line. Separate development from production by project and environment. Separate direct, shared, fixed, variable, step-fixed, committed-but-unused, and exceptional incident cost. Treat free credits and discounts transparently; do not let temporary credits define steady-state margin.

## 3. Telemetry and allocation

Create an auditable cost ledger with at least:

- timestamp and billing period;
- vendor, model/version, region, endpoint, environment, and price-card version;
- product, feature, workflow, agent, customer/account, cohort, and cost center;
- input, cached-input, output, reasoning or other billable token categories exposed by the vendor;
- tool/data calls, storage, compute duration, egress, and third-party fees;
- attempts, retries, failures, fallbacks, eval/shadow traffic, and human-review minutes;
- currency, list price, contracted price, credits, taxes, and invoice reconciliation key;
- task/outcome identifier and acceptance status.

Use immutable raw usage plus a versioned allocation table. Prefer direct trace. Allocate shared cost only with a causal, documented driver; show unallocated material cost rather than hiding it with arbitrary percentages. Reconcile usage ledger → vendor bill → general ledger → management P&L.

## 4. Unit economics

Use several denominators because each answers a different question:

```text
Cost per attempt = attributable production cost / attempted tasks
Cost per completed task = attributable production cost / technically completed tasks
Cost per accepted outcome = attributable production cost / accepted outcomes
Cost per retained outcome = attributable production cost / outcomes still valid or used at the defined horizon
```

Attributable production cost should include, when relevant:

```text
model inference
+ retries and fallbacks
+ tools, retrieval, licensed data, storage, and egress
+ quality/safety checks and sampled evaluation
+ human review, escalation, rework, and support
+ allocated shared serving and observability
+ expected failure, refund, incident, or remediation cost
```

Then calculate:

```text
Net revenue per outcome
= recognized revenue attributable to accepted outcomes
- discounts, refunds, channel share, and revenue taxes

Contribution per accepted outcome
= net revenue per accepted outcome
- cost per accepted outcome

AI gross margin
= (AI-product net revenue - cost of revenue under the stated policy)
/ AI-product net revenue
```

Define CM0/CM1/CM2 explicitly if used. Never compare margins with different inclusion rules. Show product, customer, use-case, model-route, and cohort distributions; averages hide long tasks, abusive users, low-quality retries, and unprofitable contracts.

## 5. Bottom-up forecast

Forecast demand, workload, routing, consumption, and price separately.

```text
Ending active customers[m]
= starting retained customers[m]
+ new activated customers[m]
+ reactivated customers[m]
- churned customers[m]

Eligible tasks
= eligible active entities × task opportunities per entity

Attempts
= eligible tasks × adoption/attempt rate

Route attempts[r]
= attempts × route share[r]

Model calls[r]
= route attempts[r] × turns/calls per attempt[r] × (1 + retry/fallback rate[r])

Token cost[r]
= input tokens[r] / price unit × effective input price[r]
+ cached input tokens[r] / price unit × effective cached-input price[r]
+ output tokens[r] / price unit × effective output price[r]
+ other billable token classes[r]

Tool/data cost[r]
= calls or units by tool × effective unit price

Human cost[r]
= escalated/reviewed cases × minutes per case / 60 × loaded hourly cost
```

Add evaluation/shadow traffic, batch jobs, storage retention, embedding/re-indexing, observability, peak or dedicated capacity, support, taxes, FX, and minimum commitments where material.

Maintain a versioned price table: vendor, SKU/model, region, currency, billing unit, input/cached/output distinctions, batch or priority tier, contract discount, minimum, effective dates, and primary source. Browse or obtain the current contract before decision use. Never reuse remembered public prices as current contracted cost.

Forecast accepted outcomes separately:

```text
Accepted outcomes
= attempts
× P(technical completion | attempt)
× P(quality acceptance | technical completion)
× P(no material harm | quality-accepted completion)

Cost per accepted outcome
= forecast production cost / accepted outcomes
```

Estimate these transitions on consistent task and customer cohorts; do not assume statistical independence. For B2B, model new logos, activation timing, churn, contraction/expansion, seats or eligible users, workflow rollout, and contract start/end dates separately when they drive workload or revenue. A customer forecast and a usage forecast are not the same model.

This prevents a cheaper but less reliable model from appearing economical when retries, human escalation, or failed outcomes increase.

## 6. Capacity, commitments, and cash

Model average and peak demand. Include concurrency, requests/tokens per minute, latency SLO, queueing, region redundancy, rate limits, tool limits, batch windows, and failover capacity. Identify step functions that require a new reserved tier, dedicated deployment, team, or review queue.

Separate:

- expense recognition from cash payment;
- prepaid credits and deposits from consumption;
- committed minimum from variable overage;
- reserved capacity from utilized capacity;
- invoice lag and usage accrual;
- list-price exposure from negotiated price and FX exposure.

Show unused commitment and headroom explicitly. Vendor concentration is both a financial and continuity risk.

## 7. Scenarios and variance

Build scenarios from named drivers, not blanket `±20%`:

- active entities and task frequency;
- adoption and workflow mix;
- context/input/output length;
- turns, retries, fallbacks, and tool use;
- model-routing mix and cache/batch share;
- success, acceptance, escalation, and review sampling;
- vendor price, discount, FX, and commitments;
- peak capacity, incidents, abuse, and regulatory controls.

At minimum consider demand growth, context inflation, quality regression/retry storm, vendor price/routing change, and high-risk human-review cases when relevant.

Explain forecast-to-actual variance as a bridge:

```text
Volume
→ mix/route
→ tokens per call
→ calls/retries per task
→ tool and human intensity
→ success/acceptance
→ price/discount/FX
→ allocation or accounting change
```

Do not label an allocation-policy change as product efficiency. Reforecast when a model, prompt, retrieval scheme, tool, contract, price card, or product workflow materially changes.

## 8. Deliverable and controls

Provide:

1. scope, accounting policy assumptions, and cost-object map;
2. P&L mapping with direct/shared and fixed/variable treatment;
3. usage and allocation data contract;
4. actual unit economics by attempt, completion, accepted outcome, customer, and product;
5. bottom-up monthly forecast with workload and routing drivers;
6. base/downside/upside only from anchored inputs;
7. capacity, cash, commitment, and vendor-risk view;
8. forecast-versus-actual bridge and owners;
9. missing data, reconciliation breaks, and next decision thresholds.

Recommended controls: environment and cost-center tags, per-agent/customer budgets, hard and soft limits, anomaly alerts, approval for expensive routes, quality-aware routing, cache/batch policy, retry ceilings, kill switches, invoice reconciliation, price-card versioning, and monthly FinOps–product–finance review.
