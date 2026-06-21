# README Excellence Standard

## Purpose

This standard defines the quality bar for README files in Agentic Operating System repos. A compliant README should make the repo understandable, runnable, inspectable, and safe to evaluate without relying on private context or implied claims.

The README is not marketing copy alone. It is the public operating surface for the repo.

## Scope

Use this standard for:

- Standard repos.
- Open module repos.
- Private module repos before public extraction.
- Example repos, templates, and starter kits.
- Customer-safe implementation handoffs after sensitive details are removed.

## Reader Outcomes

A premium README enables a qualified reader to answer these questions in under five minutes:

1. What system, module, or artifact is this?
2. Who is it for?
3. What inputs does it accept?
4. What artifacts does it produce?
5. What agents, skills, workflows, loops, schemas, or ledgers are involved?
6. What can be run locally or in CI?
7. What actions require human approval?
8. What data is safe to publish?
9. How does this repo connect to the wider ecosystem?
10. What is the smallest useful adoption step?

## Required README Structure

Every ecosystem README should include these sections or clear equivalents.

| Section | Required Content | Quality Bar |
|---|---|---|
| Title | Product, module, or standard name. | Names the thing directly; avoids slogan-only headings. |
| One-line position | Buyer, messy input, produced artifact, operating method. | Concrete enough to distinguish the repo from a generic AI tool. |
| Status | Draft, active, archived, experimental, private implementation, or standard module. | Includes maturity and any known limits. |
| What it does | Core workflows and outputs. | Uses verbs tied to artifacts: routes, validates, records, publishes, audits, evaluates. |
| Who it is for | Buyers, operators, developers, or maintainers. | Defines real operating context rather than broad personas. |
| System map | Agents, skills, workflows, loops, schemas, ledgers, gates, and integrations. | Shows how the repo executes work, not just what files exist. |
| First-win workflow | Smallest useful path from input to validated artifact. | Includes input, route, output, validation, and approval gate. |
| Installation or use | Commands, prerequisites, and configuration. | Commands are copyable and scoped to safe local or CI execution. |
| Validation | Test, lint, schema, build, or review commands. | Names the exact gate used before handoff. |
| Public/private boundary | What belongs in public docs and what remains private. | Blocks secrets, customer data, internal hosts, private paths, and regulated claims. |
| Safety and approvals | Human approval requirements and restricted actions. | Covers money movement, publication, customer impact, investor/legal/tax/medical decisions, credentials, and production changes. |
| Ecosystem connection | Standard version, module family, upstream/downstream repos, and contracts. | Explains interoperability without leaking private implementation details. |
| Evidence | Sample outputs, schema examples, screenshots, reports, CI badges, or release notes. | Demonstrates capability with sanitized artifacts. |
| License and contribution | License, contribution path, governance, or maintainer contact. | Matches repo visibility and maturity. |

## Positioning Formula

Use this structure for the opening promise:

```text
[Repo or module] helps [buyer/operator] turn [input] into [validated artifact] through [agents, skills, workflows, loops, ledgers, and approval gates].
```

Good examples:

- Business OS helps founders turn scattered operating priorities into decision ledgers, revenue workflows, and reviewable execution artifacts.
- Creator OS helps creator teams turn campaign ideas into publishable assets, launch checklists, and approval-gated release workflows.
- Domain Intelligence helps operators turn domain candidates into verification queues, risk notes, and portfolio decision artifacts.

Weak examples:

- A powerful AI system for anything.
- The ultimate autonomous revenue engine.
- A prompt pack that changes how you work.

## Engineering-Grounded Best Practices

### Commands Must Be Real

README commands should reflect the repo as it exists.

- Include `npm run validate`, `npm test`, `npm run build`, or the actual project command when available.
- Do not invent setup commands.
- If a command requires environment variables, list variable names and safe descriptions without values.
- If validation is manual, document the manual checklist and the reason no automated gate exists.

### Architecture Must Be Inspectable

Describe operational components in terms a maintainer can verify:

- Agents and their responsibilities.
- Skills and activation rules.
- Workflow inputs, outputs, and handoffs.
- Persistent loops and review cadence.
- Schemas, registries, ledgers, and evidence artifacts.
- External services and their approval boundaries.

Avoid diagrams or prose that imply hidden automation without naming the contracts that constrain it.

### Examples Must Be Sanitized

Examples should be useful without exposing private context.

- Use synthetic customer names and neutral sample data.
- Remove tokens, API keys, wallet material, internal URLs, private file paths, and raw logs.
- Redact sensitive identifiers before adding screenshots or traces.
- Do not include customer-specific outcomes unless approved for public release.

### Validation Must Be Explicit

Each README should name the current validation path:

- Automated validation command.
- Schema coverage.
- Test coverage or known gaps.
- CI badge when available.
- Manual review gate for language, safety, and privacy.

The README should distinguish between "validated by CI", "manually reviewed", and "example only".

### Claims Must Be Defensible

Use claims that can be supported by repo contents:

- "Produces a diligence memo template."
- "Routes candidates into a verification queue."
- "Defines approval gates before publication."
- "Includes schema validation for module records."

Avoid claims that require unavailable proof:

- Assured revenue, profit, returns, valuation, conversion, ranking, compliance, or safety.
- Legal, tax, medical, investment, trademark, or regulatory certainty.
- Autonomous action without human review.
- Real-time facts without a freshness check.

## Quality Levels

| Level | Name | README Quality |
|---|---|---|
| R0 | Stub | Names the repo but does not explain operation, validation, or safety. |
| R1 | Useful | Explains purpose, basic usage, and file map. |
| R2 | Operational | Adds real commands, first-win workflow, public/private boundary, and approval gates. |
| R3 | Standard-Ready | Adds ecosystem mapping, schemas/contracts, validation evidence, and compliance target. |
| R4 | Premium | Reads clearly, proves operational maturity, includes sanitized examples, and supports adoption without private explanation. |

Target R3 for all ecosystem repos and R4 for public launch surfaces.

## README Acceptance Criteria

A README is ready for standardization when:

- The first screen names the repo, category, buyer/operator, and produced artifact.
- The first-win workflow can be executed or reviewed from the repo alone.
- All commands have been run or marked as not available with a reason.
- Safety gates are visible before any risky workflow instructions.
- Public/private boundaries are explicit.
- Examples are sanitized.
- The repo's role in the ecosystem is clear.
- Known gaps are named without undermining trust.
- The README avoids prompt-pack language and unsupported claims.

## Review Rubric

Score each area from 0 to 2.

| Area | 0 | 1 | 2 |
|---|---|---|---|
| Positioning | Generic or vague. | Names category and audience. | Names buyer, input, artifact, and operating method. |
| Operational clarity | File list only. | Basic workflow described. | Inputs, routes, outputs, validation, and gates are concrete. |
| Engineering accuracy | Commands or architecture are missing or speculative. | Commands exist but gaps are unclear. | Commands, schemas, CI, examples, and limits are accurate. |
| Safety | Risk boundaries missing. | Some restricted actions named. | Public/private, approval, and regulated-action gates are explicit. |
| Ecosystem fit | Repo stands alone with no standard context. | Mentions ecosystem. | Maps to standard level, module family, and contracts. |
| Presentation | Hard to scan. | Readable. | Clear hierarchy, strong opening, tight tables, and no filler. |

Minimum launch score: 9 of 12, with no zero in Safety or Engineering accuracy.

## Common Anti-Patterns

- Hero copy that does not say what the repo does.
- Lists of agent names without contracts, inputs, or outputs.
- Architecture diagrams that cannot be traced to files.
- "Coming soon" sections larger than the working surface.
- Setup steps that require private knowledge.
- Screenshots containing private URLs, names, or tokens.
- Safety language placed only at the bottom after risky commands.
- Claims that read like guarantees rather than capabilities.

## Standardization Notes

README upgrades should be handled as small, reviewable changes:

- Add or update public-safe docs first.
- Keep implementation changes separate from language passes.
- Preserve repo-local instructions and owner-specific constraints.
- Record validation in the handoff.
- Use the checklist in `templates/readme-quality-checklist.md` before opening a release or rollout PR.
