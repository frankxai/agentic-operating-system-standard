# Skills Standard

Skills are durable domain instructions. They give agents reusable competence without relying on a single chat thread.

## Skill Contract

Each skill should define:

- Name.
- Description.
- Trigger conditions.
- Source order.
- Operating loop.
- Expected outputs.
- Quality gates.
- Safety boundaries.
- Examples.
- Publication status.

## Skill Levels

| Level | Meaning |
|---|---|
| Context Skill | Short guidance for a recurring task. |
| Workflow Skill | Multi-step procedure with outputs and gates. |
| Domain Skill | Deep subject-matter operating model. |
| System Skill | Cross-repo or cross-runner orchestration logic. |
| Product Skill | Packaged capability that can be sold, licensed, or supported. |

## Skill Quality Bar

A skill is not ready if:

- It only describes vibes or preferences.
- It lacks a clear output shape.
- It has no safety boundaries.
- It requires hidden context.
- It cannot be reused by another agent.

## Publication Rules

Public skills may include:

- General methods.
- Sanitized examples.
- Open-source setup instructions.
- Non-sensitive templates.

Private skills may include:

- Proprietary processes.
- Customer-specific workflows.
- Internal pricing and deal strategy.
- Sensitive system routing.
- Private memory or non-public repo topology.

## Minimal Skill Template

```markdown
---
name: module-skill-name
description: Use when...
---

# Skill Name

## Source Order

1. Repo instructions.
2. Module registry.
3. Relevant examples.

## Operating Loop

1. Clarify objective.
2. Gather inputs.
3. Produce artifact.
4. Run gates.
5. Write handoff.

## Output Shape

- Summary.
- Artifact.
- Evidence.
- Risks.
- Next action.
```
