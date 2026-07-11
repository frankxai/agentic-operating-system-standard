# Prompt Contract and Compilation Standard

Version: `0.1.0`

Status: public draft

## Thesis

A prompt is not a block of clever prose. In an Agentic Operating System, a prompt is a **versioned interaction contract** that connects human intent to context, specialist capability, a governed workflow, an output schema, evaluation, and a handoff.

The same canonical prompt contract can be compiled into:

- a gentle web interaction;
- a one-question-at-a-time interview;
- a Markdown prompt;
- an agent or skill instruction;
- an MCP prompt, resource, or tool definition;
- an API request and response contract;
- a Codex, Claude Code, Cursor, Grok, or Gemini command;
- a Notion or repository template;
- a checklist, lesson, or cohort exercise;
- an evaluation fixture;
- a public product preview.

Raw prompt libraries SHOULD be treated as source material, not the final delivery model.

## The Prompt Stack

A complete interaction is composed from six layers.

| Layer | Job | Example |
|---|---|---|
| Invitation | Gives the person a clear reason to begin. | “What needs to move today?” |
| Intake | Captures only the state needed to act safely. | Outcome, time, current artifact, privacy, authority. |
| Context | Retrieves selected memory, evidence, standards, and brand rules. | Voice contract, previous decision, research sources. |
| Procedure | Defines the reasoning and execution sequence. | Diagnose, draft, evaluate, revise, hand off. |
| Output | Names the artifact and schema. | Brief, lesson, memo, code change, review packet. |
| Review | Applies evidence, quality, safety, approval, and memory rules. | Claims gate, human approval, memory proposal. |

A string that contains only instructions is an incomplete prompt contract.

## Required Prompt Contract

Every published prompt SHOULD define:

1. `id` — stable machine identifier;
2. `name` — human-readable name;
3. `version` — semantic version;
4. `status` — draft, beta, stable, deprecated, internal, or archived;
5. `job` — the one operating job this prompt performs;
6. `invitation` — the human-facing entry language;
7. `roles` — human roles or operating modes it serves;
8. `triggers` — intents, events, states, or commands that activate it;
9. `required_inputs` — blocking inputs;
10. `optional_inputs` — useful but non-blocking inputs;
11. `context_selectors` — memory, sources, files, policies, or tools to retrieve;
12. `capacity_profile` — time, depth, pace, and teaching/execution preference;
13. `procedure` — ordered steps and stop conditions;
14. `capabilities` — agents, skills, tools, and workflows composed underneath;
15. `output_contract` — artifact type, schema, format, and acceptance criteria;
16. `quality_gates` — evaluations required before handoff;
17. `approval_gates` — actions that remain human-owned;
18. `privacy` — allowed data classes and retention behavior;
19. `failure_recovery` — what happens when context, evidence, tools, or confidence are insufficient;
20. `teaching_note` — what the person should understand after using it;
21. `memory_proposal` — what may be worth retaining;
22. `delivery_targets` — interfaces this prompt may compile into;
23. `provenance` — authors, sources, lineage, and license;
24. `owner` — maintaining module or team;
25. `evaluation_suite` — fixtures, score threshold, and last evaluation date.

## Prompt Classes

Use a small set of explicit classes rather than treating every instruction as the same thing.

### Invitation Prompt

Begins from a human outcome and lowers the cost of entry.

```text
What needs to move today?
```

### Guided Interview

Collects high-signal context one question at a time. It is the preferred derivation mechanism for brand, business, identity, health, wealth, and other sensitive operating profiles.

### Working Brief

Converts conversation into structured state that other agents and workflows can use without re-interviewing the person.

### Execution Prompt

Runs a bounded procedure and produces a named artifact. Execution prompts should be less conversational and more explicit about inputs, tools, outputs, stop conditions, and gates.

### Review Prompt

Evaluates an artifact against a rubric. It must separate observations from interpretations and expose failure reasons.

### Reflection Prompt

Helps the person consolidate learning, decisions, patterns, and next commitments. It does not force memory retention.

### Handoff Prompt

Packages state for another person, agent, repo, or service. It states what has been completed, what remains uncertain, what evidence exists, and who owns the next decision.

### Recovery Prompt

Handles missing evidence, tool failure, conflict, unsafe requests, low confidence, or scope overload. Recovery is part of the product contract, not an afterthought.

## Composition Rules

Prompts SHOULD compose capabilities through references rather than copy entire instructions into every surface.

```text
human invitation
  -> intake schema
  -> context selectors
  -> workflow
  -> agents and skills
  -> output schema
  -> evaluation suite
  -> gate and handoff
```

Composition MUST preserve:

- the human's stated outcome;
- selected privacy and authority modes;
- source attribution;
- output requirements;
- approval boundaries;
- version provenance.

A compiled prompt MUST NOT silently increase autonomy, data access, scope, or retention.

## Prompt Compiler

A Prompt Compiler reads the canonical contract and emits interface-specific artifacts.

### Web

Produces:

- invitation copy;
- progressive form or conversation state;
- sensible defaults;
- validation;
- preview of the output;
- review and approval controls;
- export and memory controls.

### Agent Runners

Produces:

- runner-specific command or skill files;
- explicit tool permissions;
- context-loading rules;
- stop conditions;
- structured response instructions;
- handoff packet.

### MCP and API

Produces:

- prompt metadata;
- JSON Schema inputs;
- resource dependencies;
- tool declaration;
- output schema;
- authority mode;
- errors and recovery states.

### Product Pack

Produces:

- quick-start guide;
- template or workspace;
- example inputs and outputs;
- prompt cards;
- checklist;
- evaluation rubric;
- update manifest;
- support boundary.

### Education

Produces:

- learning objective;
- explanation of the method;
- guided practice;
- independent exercise;
- example artifact;
- self-review rubric;
- next capability.

## Gentle Prompt Behavior

Human-facing prompts SHOULD:

- start from desired movement, not system taxonomy;
- ask one blocking question at a time;
- offer a useful default when safe;
- adapt to available time and energy;
- distinguish “I can draft” from “I can act”;
- explain why sensitive information is requested;
- make assumptions visible;
- produce an artifact before presenting a larger system;
- close with one review decision and one next invitation.

Avoid prompts that:

- begin with a long role-play preamble;
- imitate authority instead of earning it through method and evidence;
- expose internal agent names when the person only needs an outcome;
- demand exhaustive context before first value;
- combine research, creation, publication, payment, and memory into one opaque instruction;
- use personality as a substitute for an output contract;
- promise transformation without a proof artifact or operating loop.

## Evaluation Contract

A stable prompt MUST have representative fixtures for:

- a normal case;
- a sparse-context case;
- a conflicting-context case;
- a sensitive-data case;
- a low-capacity or short-time case;
- a tool-unavailable case;
- a request that should stop or escalate;
- a high-quality expected artifact.

Evaluation SHOULD score:

- intent fidelity;
- context economy;
- artifact usefulness;
- evidence discipline;
- voice and domain fit;
- gate compliance;
- recovery quality;
- teaching value;
- handoff completeness;
- unnecessary cognitive load.

A prompt is marketing-eligible only when it is versioned, owned, evaluated, connected to a real workflow, and produces an inspectable artifact.

## Provenance and Gratitude

Prompt contracts SHOULD name:

- originating authors and collaborators;
- research sources;
- open-source or framework lineage;
- customer or community contributions used with permission;
- license and attribution requirements.

Credits are not footer decoration. They allow the system to preserve trust, teach lineage, and improve responsibly.

## Lifecycle

Use semantic versioning.

- Patch — language, examples, recovery, or non-breaking evaluation improvements.
- Minor — new optional inputs, outputs, delivery targets, or capabilities.
- Major — changed job, authority, privacy, output schema, or approval expectations.

Deprecated prompts remain discoverable with a migration target. Archived prompts are excluded from product counts and generation surfaces.

## Minimum Example

```yaml
id: creator.article-from-insight
name: Article from insight
version: 1.0.0
status: stable
job: Turn one owned insight into a source-aware article draft and review packet.
invitation: What idea deserves a durable explanation?
roles: [creator, professional]
triggers:
  intents: [write article, explain insight]
required_inputs: [insight, intended reader]
optional_inputs: [sources, examples, voice sample, time_budget]
context_selectors: [voice, prior_research, claim_policy]
capacity_profile:
  default_minutes: 45
  modes: [guided, execution]
procedure:
  - establish the thesis and reader change
  - retrieve relevant evidence
  - draft the structure
  - write the article
  - run claims and voice review
  - prepare the handoff
capabilities:
  agents: [researcher, developmental-editor]
  skills: [content-strategy, source-discipline]
output_contract:
  artifact: article-review-packet
  format: markdown
quality_gates: [evidence, voice, usefulness]
approval_gates: [publication]
privacy:
  default: private
  retention: propose
failure_recovery:
  - surface missing evidence
  - produce an outline when drafting would invent facts
teaching_note: A strong article is a thesis, mechanism, evidence, and reader decision—not expanded social copy.
memory_proposal: Save the approved thesis and reusable evidence only.
delivery_targets: [web, markdown, mcp, codex, claude-code]
owner: creator-os
evaluation_suite: creator-article-v1
provenance:
  built_on: [agentic-operating-system-standard, sip]
```