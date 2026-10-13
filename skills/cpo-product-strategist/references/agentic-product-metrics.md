# Agentic Product Strategy and Metrics

## Contents

1. Product unit
2. Eval-driven development
3. Metric stack
4. North Star and economics
5. Human-agent operating model
6. Release and monitoring gates

## 1. Product unit

Treat an agent as a delegated-work system, not a chat interface or model benchmark. Define the bounded job, intended outcome, authority, tools, data, stopping condition, unacceptable actions, and human escalation boundary.

Use a real unit: task, workflow, case, decision, transaction, artifact, resolved incident, or accepted outcome. Messages, sessions, tokens, tool calls, and agent runtime are consumption diagnostics unless the user receives value from them directly.

## 2. Eval-driven development

Maintain a representative case set with provenance, segment coverage, difficulty, known edge cases, and privacy treatment. Connect:

```text
offline case evaluation
→ shadow or limited production
→ online task outcome
→ customer/business impact
→ regression monitoring
```

Do not optimize an LLM judge score without measuring agreement with qualified human review and downstream outcomes. Separate model capability, orchestration quality, context/retrieval quality, tool execution, UX, and business-process effects.

## 3. Metric stack

Choose only metrics that change a decision.

| Layer | Example measures |
|---|---|
| Outcome | goal/task completion, accepted outcome, downstream use, durable resolution, self-service resolution |
| Quality | rubric pass, factual/citation integrity, defect severity, calibrated confidence, expert agreement |
| Trajectory | required-action recall, action precision, ordering, unnecessary steps, loop/retry rate, recovery after failure |
| Tools | tool selection, call success, argument validity, side-effect correctness, rollback/reversibility |
| Autonomy | straight-through completion, human takeover, escalation appropriateness, expert minutes per outcome |
| Reliability | completion availability, timeout, p50/p95 time-to-outcome, tail failure, dependency failure |
| Safety/trust | unsafe action, privacy/security breach, prompt injection success, override, complaint, harmful confident error |
| Economics | cost per attempt, successful outcome, accepted outcome, retained outcome, and incremental contribution |

Never collapse quality, safety, cost, and speed into one opaque score without preserving the components and decision weights. Report results by task type, user segment, risk tier, model route, and difficulty; a blended pass rate can hide critical failures.

## 4. North Star and economics

A defensible agentic North Star normally counts meaningful accepted outcomes within a natural cycle. Candidate structure:

```text
Accepted outcomes
= eligible tasks
× attempted share
× technical completion
× quality acceptance
× no-harm rate
× persistence or downstream-use rate
```

Keep economics paired with value:

```text
Cost per accepted outcome
= total attributable production cost / accepted outcomes

Contribution per accepted outcome
= net revenue or attributable value
- inference, tools, data, review, support, failure, and allocated serving cost
```

Do not use token volume, agent hours, number of agents, or autonomy alone as the North Star. More autonomy can increase risk; fewer escalations can conceal failures; more usage can destroy margin.

## 5. Human-agent operating model

Classify each step as agent-only, agent-proposed/human-approved, human-led/agent-assisted, or prohibited for automation. Measure:

- expert minutes and rework per accepted outcome;
- appropriate escalation versus avoidable escalation and missed escalation;
- queue time, capacity released, and new bottlenecks;
- variance across reviewers and segments;
- accountability, auditability, reversibility, and user recourse.

For multi-agent products, test whether specialization or debate improves accepted outcomes after extra latency, cost, coordination failure, and duplicated work. Agent count is not value.

## 6. Release and monitoring gates

Define by risk tier:

- minimum offline quality and safety evidence;
- cases that require deterministic checks or human approval;
- online outcome and guardrails;
- cost and latency ceilings;
- rollback and incident owner;
- regression thresholds after model, prompt, retrieval, data, tool, or policy changes.

Use sequential evidence gates rather than one permanent launch threshold. A product can pass a generic benchmark and still fail its real job, economics, trust, or operational responsibility.
