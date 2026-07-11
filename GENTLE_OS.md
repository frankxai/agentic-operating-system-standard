# Gentle OS Experience Contract

Version: `0.1.0`

Status: public draft

## Definition

A **Gentle OS** is the human-facing experience profile of an Agentic Operating System. It may coordinate deep memory, specialist agents, tools, workflows, evaluations, and delivery infrastructure, while presenting the person with only the smallest coherent decision they can use now.

Gentle does not mean weak, passive, decorative, or simplified beyond usefulness. It means the system respects human capacity, authority, privacy, attention, and timing.

The core invariant is:

```text
one clear commitment -> one visible artifact -> one reviewable decision -> one optional memory
```

The person should never need to understand the underlying agent topology before receiving value.

## Experience Thesis

Most AI products expose either a blank prompt box or the machinery of the system. A Gentle OS does neither.

It begins from the person's current state, composes the necessary intelligence underneath, and returns a bounded agenda. The architecture expands only when the work proves that more structure is useful.

The experience should feel like a thoughtful operating partner:

- calm enough to enter without preparation;
- precise enough to produce serious work;
- transparent enough to trust;
- modular enough to grow with the person;
- owned enough to leave with their data, decisions, and artifacts.

## The Five-Beat Loop

Every Gentle OS session SHOULD follow this loop.

### 1. Arrive

Capture the smallest useful state:

- what matters now;
- what outcome the person wants;
- how much time and energy they have;
- what already exists;
- what is private or sensitive;
- what the system is allowed to do.

Ask one question at a time. Do not force a complete profile before the first useful result.

### 2. Orient

Return a short model of the situation and the recommended next move.

A compliant orientation includes:

- one-sentence understanding;
- one essential move;
- why that move is load-bearing;
- what input is still required;
- what the system will not do without approval.

Ask at most one blocking question before making a useful draft. Missing non-critical information becomes a visible assumption or TODO, not an interrogation.

### 3. Make

Compose agents, skills, tools, research, and templates behind the interface. Expose the work, not the internal org chart.

The first execution SHOULD produce an inspectable artifact such as:

- a brief;
- a lesson or practice set;
- a draft;
- a plan;
- a decision packet;
- a workflow;
- a repository change;
- a review agenda;
- a clinician, customer, investor, or team handoff.

The artifact MUST identify assumptions, missing evidence, and approval-sensitive actions.

### 4. Review

Separate evidence from judgment.

Use this epistemic ladder where interpretation matters:

```text
observation -> interpretation -> hypothesis -> evidence -> decision
```

The system may observe, interpret, and propose hypotheses. It must not silently collapse those layers. The final decision remains with the person or named human owner.

Review SHOULD answer:

- What changed?
- What is supported by evidence?
- What remains uncertain?
- What requires approval?
- What is the next consequential decision?

### 5. Remember

Propose what should persist; do not assume everything should.

A memory proposal SHOULD state:

- the candidate fact, preference, decision, or pattern;
- why it may be useful later;
- its privacy class;
- its source and confidence;
- when it should be reviewed or expire.

The person can accept, edit, decline, export, or delete the proposal. The session closes with one next invitation, not an infinite task list.

## Gentle Agenda Contract

A default agenda contains:

| Field | Requirement |
|---|---|
| Essential move | Exactly one action that materially advances the stated outcome. |
| Timebox | Honest estimate or bounded session size. |
| First artifact | The concrete thing produced or changed. |
| Why now | The constraint or leverage point that makes this the right move. |
| Required context | Only the information necessary to start safely. |
| Optional moves | Zero to two; clearly subordinate to the essential move. |
| Review gate | Evidence, quality, privacy, money, legal, medical, production, or publication check. |
| Memory proposal | What may be worth carrying forward, with consent. |
| Next invitation | One reversible continuation after review. |

A Gentle OS MUST NOT present a backlog as an agenda.

## Progressive Disclosure

A Gentle OS grows through evidence and consent, not product pressure.

| Level | Experience | System Exposure |
|---|---|---|
| G0 — Guest | One useful result without setup. | No persistent memory; minimal controls. |
| G1 — Guided Session | One outcome, one artifact, one review. | Temporary context and export. |
| G2 — Personal Rhythm | Daily or weekly agenda with chosen memory. | A small vault, review loop, and preferences. |
| G3 — Installed Module | A domain OS with workflows, templates, and permissions. | Named module, agent team, ledgers, and updates. |
| G4 — Composed OS | Multiple modules share memory and an agenda. | Cross-module routing and governance. |
| G5 — Sovereign Estate | A principal or organization owns a tuned intelligence estate. | Full topology, advanced agents, private infrastructure, and stewardship. |

Escalation SHOULD occur only when one of these is true:

- the current workflow has produced proof and needs repetition;
- coordination cost has become visible;
- memory would materially improve future work;
- risk requires stronger governance;
- the person explicitly asks for more control or capability.

## Capacity Is a First-Class Input

Every agenda generator SHOULD understand:

- available time;
- cognitive or emotional load;
- desired pace;
- current confidence;
- deadline pressure;
- whether the person wants teaching, execution, or both.

The same objective may produce a ten-minute move, a seven-day rhythm, or a ninety-day system. The system should reduce scope before increasing pressure.

## Authority and Autonomy

Every action surface MUST declare one mode:

- `read_only` — inspect and explain;
- `draft_only` — create local or reviewable artifacts;
- `approval_required` — prepare an action and wait for explicit approval;
- `delegated` — execute within a pre-approved, reversible scope;
- `blocked` — never executable by the agent.

Money movement, publication, external messaging, credential use, destructive operations, regulated decisions, and irreversible production changes MUST NOT be hidden behind a generic confirmation.

## Language Contract

Gentle interfaces SHOULD:

- use the person's language before internal product nouns;
- lead with the next outcome, not the agent count;
- explain why a question is necessary when it touches sensitive context;
- distinguish recommendation from requirement;
- make assumptions visible;
- offer a graceful pause, export, or decline path;
- describe limitations without legalistic fog.

Gentle interfaces SHOULD NOT:

- shame the person with missed streaks, red dashboards, or artificial urgency;
- expose dozens of agents or modules as a navigation burden;
- disguise an upsell as the recommended next action;
- require a taxonomy lesson before first value;
- manufacture certainty, intimacy, or dependence;
- treat every captured thought as permanent memory;
- send, publish, buy, deploy, diagnose, or invest without the relevant human gate.

## Product Surface Rules

The public product surface SHOULD expose no more than:

1. the outcome the person can move;
2. the first artifact they will receive;
3. the time or commitment required;
4. what the system quietly composes;
5. what remains human-owned;
6. how the system can grow after proof.

Internal engines, agents, and packs MAY be inspectable in advanced documentation, but SHOULD NOT become competing front-door products unless they have a distinct buyer, first-win workflow, support contract, and release lifecycle.

## Ownership Contract

A Gentle OS MUST distinguish:

- **person-owned state** — identity, goals, voice, private memory, decisions, data, artifacts, and custom configuration;
- **shared machinery** — generic workflows, agents, schemas, evaluators, adapters, and update logic;
- **public canon** — standards, protocols, research, templates, and attribution;
- **provider state** — billing, entitlements, telemetry, and operational metadata.

Person-owned state is never overwritten by a shared update. Shared machinery arrives as an inspectable proposal, diff, or versioned release. Export and exit remain available.

## Acceptance Tests

A surface is Gentle OS compliant when a new person can:

1. state one outcome without learning the system taxonomy;
2. receive a useful artifact before completing a full profile;
3. understand the next move and why it was selected;
4. see what the system assumed and what evidence is missing;
5. identify which actions require approval;
6. choose what is remembered;
7. pause, export, or leave without losing their work;
8. grow into a deeper module without rebuilding their identity or context;
9. use the same contract through web, chat, Codex, Claude, MCP, a repository, or a human-guided service;
10. remain the final authority over consequential decisions.

## Relationship to the Agentic Operating System Standard

The Agentic Operating System Standard defines the governed machinery. This contract defines how that machinery meets a human.

A system can be technically compliant and still fail the Gentle OS contract. Premium systems must satisfy both.