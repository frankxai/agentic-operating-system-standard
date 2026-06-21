# README Quality Checklist

Use this checklist before publishing or standardizing an Agentic Operating System repo README.

## Positioning

- [ ] The title names the repo, module, product, or standard directly.
- [ ] The opening line identifies the buyer/operator, input, output artifact, and operating method.
- [ ] The README avoids slogan-only positioning.
- [ ] The status is clear: draft, active, experimental, archived, private implementation, open module, or standard repo.
- [ ] The first screen explains why this repo exists without requiring private context.

## Operational Clarity

- [ ] The README explains what the repo does in concrete workflow terms.
- [ ] Inputs are named.
- [ ] Outputs are named.
- [ ] The first-win workflow includes input, route, artifact, validation, and approval gate.
- [ ] The file map explains the role of important files and directories.
- [ ] Agents, skills, workflows, loops, ledgers, schemas, and gates are described when they exist.
- [ ] External services or integrations are named only when the repo actually uses them.

## Engineering Accuracy

- [ ] Setup commands are real for this repo.
- [ ] Validation commands are real for this repo.
- [ ] Required environment variables are named without exposing values.
- [ ] Configuration examples use safe placeholders.
- [ ] CI badges, schema references, screenshots, and sample outputs point to existing artifacts.
- [ ] Known gaps are listed plainly.
- [ ] The README distinguishes working features from planned features.

## Safety And Public Boundary

- [ ] No secrets, tokens, wallet material, credentials, internal hosts, private paths, raw customer logs, or private customer data are present.
- [ ] Risky actions have human approval gates before execution instructions.
- [ ] Money movement, publication, production changes, customer-impacting actions, and regulated decisions are gated.
- [ ] Legal, tax, medical, investment, trademark, and compliance language is framed as review, triage, or approval workflow, not certainty.
- [ ] Public examples use synthetic or approved data.
- [ ] Screenshots and traces are redacted.

## Ecosystem Fit

- [ ] The README names the standard or module family it aligns with.
- [ ] The compliance target or maturity level is stated when relevant.
- [ ] Upstream and downstream contracts are named.
- [ ] Related repos are referenced only when the relationship is accurate and public-safe.
- [ ] The README preserves repo-local `AGENTS.md` instructions and local ownership.

## Evidence

- [ ] At least one proof artifact, example, schema, report, or validation output is referenced.
- [ ] The evidence is reproducible or clearly marked as illustrative.
- [ ] Sample inputs and outputs are sanitized.
- [ ] Validation result is recorded in the handoff or README.

## Presentation Quality

- [ ] Headings are scannable.
- [ ] Tables are used where comparison improves comprehension.
- [ ] The README avoids filler, hype, and prompt-pack framing.
- [ ] Long lists are grouped by function.
- [ ] Safety and validation are easy to find.
- [ ] The README can be understood without a sales call or private walkthrough.

## Launch Decision

| Area | Pass | Notes |
|---|---|---|
| Positioning |  |  |
| Operational clarity |  |  |
| Engineering accuracy |  |  |
| Safety and public boundary |  |  |
| Ecosystem fit |  |  |
| Evidence |  |  |
| Presentation quality |  |  |

Minimum bar:

- No blocker in Safety and public boundary.
- No invented command or unsupported capability claim.
- README reaches R3 or higher from `docs/README_EXCELLENCE_STANDARD.md`.
- Validation result is recorded before handoff.
