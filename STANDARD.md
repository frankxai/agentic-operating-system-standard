# Agentic Operating System Standard

Version: `0.2.0`

Status: public draft

## Definition

An **Agentic Operating System** is a governed, repo-backed system that coordinates humans, agents, tools, skills, workflows, loops, ledgers, and approval gates to produce repeatable outcomes in a domain.

It is not a literal computer operating system. It is an operating standard for agent-native work.

## Core Objects

| Object | Definition |
|---|---|
| Module | A domain operating system such as Creator OS, Business OS, Investor OS, or Domain Intelligence. |
| Agent | A bounded worker role with a contract, permissions, expected artifact, stop condition, and handoff format. |
| Skill | Reusable domain knowledge with triggers, instructions, examples, and safety boundaries. |
| Workflow | A repeatable sequence that turns inputs into an artifact. |
| Loop | A recurring operating cycle that improves decisions, assets, or system quality over time. |
| Ledger | A durable record of evidence, decisions, owners, gates, and next review. |
| Gate | A required check before money, publication, legal, customer, wallet, production, or irreversible action. |
| Adapter | A runner-specific implementation surface for Codex, Claude Code, Antigravity, Grok, Cursor, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, or another agent runner. |
| Repository Profile | A versioned operating contract for repository identity, runtime boundaries, team binding, permissions, gates, and evidence. |
| Team Profile | A versioned composition contract for coordinator and specialist roles, routing, write scopes, gates, verification, and evaluation. |

## Required Repository Files

A compliant module SHOULD include:

- `README.md`
- `AGENTS.md`
- `SKILLS.md`
- `WORKFLOWS.md`
- `LOOPS.md`
- `registry/*.json`
- `schemas/*.schema.json`
- `templates/`
- `docs/`
- validation command in `package.json` or equivalent

## Control Plane

Every module MUST define:

1. Objective.
2. Audience.
3. Inputs.
4. Outputs.
5. Agent roles.
6. Skills.
7. Workflows.
8. Loops.
9. Evidence requirements.
10. Approval gates.
11. Public/private boundaries.
12. Release and support path.

## Portable Repository And Team Profiles

Ecosystem nodes SHOULD implement these portable contract identifiers:

- `starlight.repo_profile.v2` with canonical schema ID `https://starlight.local/schemas/starlight-repo-profile.v2.schema.json`.
- `starlight.team_profile.v2` with canonical schema ID `https://starlight.local/schemas/starlight-team-profile.v2.schema.json`.

The adopting control plane owns the canonical schemas and full payloads. Public registries and module repos MUST use sanitized references rather than copying private topology or policy data.

A repository profile binds identity, runtime, data classification, deployment policy, one team profile, allowed tools and write scopes, gates, and required evidence. A team profile defines coordinator and specialist roles, routing and handoffs, permissions, stop conditions, outputs, human gates, evaluation references, and an independent verifier.

The verifier MUST NOT hold implementation write scope over the artifact being verified. Contract projections MUST carry owner, lifecycle, version, portable source reference, and content hash when one is available. Canonical profiles take precedence over repo, registry, and runner projections.

See [Portable Repository And Team Profile Contracts](./docs/PORTABLE_PROFILE_CONTRACTS.md).

## Agent Contract

Every agent MUST have:

- `id`
- `role`
- `objective`
- `inputs`
- `allowed_tools`
- `forbidden_actions`
- `expected_artifact`
- `evidence_required`
- `stop_conditions`
- `handoff_format`
- `approval_gates`

Every agent used through a team profile SHOULD also declare its allowed write scope, completion and blocked-work routes, verifier relationship, and provenance source.

## Skill Contract

Every skill SHOULD have:

- Name.
- Trigger conditions.
- User intent it serves.
- Source order.
- Operating loop.
- Output shape.
- Quality gates.
- Safety rules.
- Example invocation.
- Publication status.

## Workflow Contract

Every workflow SHOULD define:

- Name.
- Owner module.
- Inputs.
- Steps.
- Agents.
- Skills.
- Outputs.
- Validation.
- Gate conditions.
- Ledger entry.
- Improvement loop.

## Standard Gates

| Gate | Required Before |
|---|---|
| Evidence Gate | Public claim, recommendation, report, or business decision. |
| Privacy Gate | Publishing, sharing, screenshots, examples, or training data. |
| Money Gate | Purchases, offers, transfers, pricing, renewal, payment, or spend. |
| Legal Gate | Trademark, regulated claims, investor documents, contracts, or IP-heavy decisions. |
| Wallet Gate | Wallet connection, signing, registration, transfer, resolver, or chain action. |
| Production Gate | Deployment, migration, customer-impacting automation, or persistent external state. |

## Compliance Levels

### L0: Context Pack

The repo has clear instructions and enough context for an agent to work safely.

### L1: Skill Pack

The repo defines reusable skills, triggers, and examples.

### L2: Workflow System

The repo defines reusable workflows, loop diagrams, and validation.

### L3: Agent OS

The repo defines agent roles, permissions, handoffs, ledgers, and gates.

### L4: Standard Module

The repo exposes schemas, templates, public/private boundaries, examples, and release discipline.

### L5: Ecosystem Node

The repo interoperates with SIS, ACOS, AIS, GitHub, and multiple agent runners without changing the core contract. It exposes compatible repository/team profile references when those profiles are used.

## Public Claims Policy

Compliant systems MUST avoid:

- Assured revenue claims.
- Legal, financial, medical, tax, or investment conclusions without professional review.
- Hidden private data in examples.
- Inflated agent autonomy claims.
- Unverifiable claims about performance, safety, availability, or market value.

## Versioning

Use semantic versioning for the standard.

- Patch: clarifications and non-breaking templates.
- Minor: new optional contracts, modules, or examples.
- Major: changes that alter compliance expectations.
