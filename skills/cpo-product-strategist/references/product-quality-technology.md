# Product Quality, Design, and Technology Governance

## Contents

1. Product quality model
2. Product taste and critique
3. Quality bar and release decisions
4. Product-technology choices
5. Platform, API, and data products
6. Reliability, security, privacy, and accessibility
7. Technical debt and investment
8. CPO-CTO boundary and deliverable

## 1. Product quality model

Define quality for the target job and risk, not as polish. Consider:

- outcome correctness and completeness;
- usability, comprehension, and time/effort to value;
- reliability, performance, continuity, and recovery;
- accessibility and inclusive use;
- safety, privacy, security, trust, and user control;
- coherence across surfaces, states, channels, and service handoffs;
- maintainability, observability, supportability, and cost-to-serve;
- emotional or brand quality only where it affects the intended experience.

Weight dimensions by context. A financial action, internal admin tool, consumer delight product, physical device, and AI recommendation need different failure tolerances.

## 2. Product taste and critique

Product taste is disciplined judgment informed by user behavior, design principles, craft, domain constraints, and coherent intent—not executive preference.

Run critique from the user's job:

1. What outcome and confidence should the user achieve?
2. Is the primary path and next action obvious?
3. What must the user understand, remember, enter, decide, or recover from?
4. Are hierarchy, language, feedback, defaults, errors, empty/loading states, permissions, and handoffs coherent?
5. What evidence supports the design and what remains a hypothesis?
6. Which simplification removes real complexity versus hiding it?

Use representative tasks, prototypes, usability evidence, accessibility review, production behavior, and support evidence. Do not settle design disputes by title, taste adjectives, or copying competitors.

## 3. Quality bar and release decisions

Set explicit must-pass, monitor, and reversible-exception criteria. Include target tasks, critical states, supported environments, performance/reliability, data integrity, accessibility, security/privacy, instrumentation, documentation/support, and rollback.

Separate:

- MVP: smallest coherent value and learning system;
- beta/limited availability: bounded audience and known limitations;
- production-ready: approved reliability, operations, trust, and support;
- quality debt: explicit exception with owner, exposure, remedy, and review date.

Do not call avoidable defects an MVP. Do not block low-risk learning with enterprise-wide ceremony. Scale gates to reversibility, exposure, and harm.

## 4. Product-technology choices

For consequential build/buy/partner, architecture, model, or integration decisions compare customer differentiation, time to learning/value, total cost, flexibility, reliability, security/compliance, data/IP, talent, vendor concentration, migration/exit, and operational burden.

Record the decision, context, options, assumptions, owner, consequences, and revisit trigger. Product leadership owns customer/business trade-offs; technology leadership owns technical integrity and feasibility. Shared decisions require one named accountable owner under the company's governance.

Do not prescribe architecture from a product framework or accept `technical necessity` without the constraint and alternatives being legible.

## 5. Platform, API, and data products

Treat internal and external platforms as products with named users, jobs, adoption, service expectations, roadmap, support, and economics. Define interface contracts, versioning, compatibility, migration, discoverability, documentation, observability, quotas, and deprecation.

Platform investment should reduce duplicated cognitive/operational load or enable differentiated capability. Measure adoption, successful workflows, integration time, reliability, developer/operator satisfaction with behavioral evidence, cost-to-serve, and avoided duplication. Do not optimize API calls or internal platform adoption without downstream value.

For data products define source, ownership, lineage, quality, freshness, access, permitted use, semantic contract, reconciliation, and deletion/retention.

## 6. Reliability, security, privacy, and accessibility

Start from critical user journeys and harms. Define service indicators and objectives only for behavior users or operations depend on; include tail latency, availability, correctness, recovery, data loss, and dependency failures as relevant.

Integrate threat modeling, privacy/data minimization, permissions, auditability, abuse/fraud, incident response, and regulatory review into discovery and design. Accessibility applies to flows, content, interaction, assistive technology, contrast, keyboard/focus, error recovery, and alternatives—not a final checklist.

Use current qualified standards and specialists for legal, security, safety, clinical, financial, or accessibility conclusions. The skill identifies required evidence and design implications; it does not certify compliance.

## 7. Technical debt and investment

Describe debt through its observable product/economic mechanism: slower change, incidents, quality variance, security exposure, vendor lock-in, cost, onboarding load, or blocked strategy. Estimate frequency, impact, affected outcomes, trend, alternatives, and cost of delay.

Balance feature, platform, reliability, security, migration, and debt work in one portfolio. Prefer thin enabling slices and measurable risk reduction. Do not demand a rewrite from disgust with old technology or reject infrastructure work because users cannot see it.

## 8. CPO-CTO boundary and deliverable

Provide the target user/job, quality model, critique findings, evidence, quality/release gates, technical options and trade-offs, platform/data implications, reliability/security/privacy/accessibility requirements, debt/investment case, decision ownership, and review triggers.

Preserve productive tension: CPO cannot delegate customer value and quality to Technology; CTO cannot be forced to accept unsafe or unsustainable implementation. Escalate unresolved company-level trade-offs with options and consequences, not departmental positions.
