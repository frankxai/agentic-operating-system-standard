# Ecosystem Rollout Plan

## Purpose

This plan describes how to standardize README quality and positioning across Agentic Operating System ecosystem repos without overwriting local ownership, private implementation details, or active work from other operators.

The rollout goal is consistent public comprehension: every repo should explain what it is, how it operates, how it is validated, and where human approval is required.

## Rollout Principles

- Preserve repo-local `AGENTS.md` instructions.
- Prefer additive docs and templates before modifying high-traffic files.
- Keep public and private surfaces separate.
- Treat README claims as engineering claims backed by files, commands, examples, or evidence.
- Avoid broad rewrites while other agents are working.
- Record validation results in every handoff.

## Target Artifacts

Each standardized repo should have:

- `README.md` with R3 or R4 quality from `docs/README_EXCELLENCE_STANDARD.md`.
- `AGENTS.md` with local operating rules and public/private boundaries.
- `SKILLS.md`, `WORKFLOWS.md`, and `LOOPS.md` when the repo exposes agentic execution.
- A validation command or documented manual gate.
- A first-win workflow.
- A public-safe proof artifact or example.
- A clear standard version or compatibility note.

## Repo Classification

| Repo Type | README Emphasis | Required Boundary |
|---|---|---|
| Standard repo | Normative definitions, schemas, compliance levels, governance. | Do not imply implementation capability beyond the standard. |
| Open module repo | Runnable starter workflows, public examples, adoption path. | Keep pro workflows and customer data out of public docs. |
| Private module repo | Operating instructions, delivery workflows, private evals. | Mark what can be extracted publicly and what must stay private. |
| Customer implementation | Specific configuration, evidence ledger, operational approvals. | No public release without customer approval and redaction. |
| Template repo | Copyable structure, placeholders, validation gates. | Avoid fake claims and invented integrations. |

## Phased Rollout

### Phase 0: Inventory

Create a simple tracker for each repo:

- Repo name.
- Repo type.
- Current README quality level.
- Existing validation command.
- Missing standard artifacts.
- Public/private risk level.
- Active owners or concurrent agents.
- Recommended first PR.

Exit criteria:

- Every target repo has a classification.
- Repos with active work are flagged before editing.
- High-risk private or customer surfaces are separated from public rollout.

### Phase 1: Additive Standard Artifacts

Make low-conflict additions before changing primary README files:

- Add `AGENTS.md` if missing.
- Add or update `SKILLS.md`, `WORKFLOWS.md`, and `LOOPS.md` when relevant.
- Add `docs/README_EXCELLENCE_STANDARD.md` reference or local README notes.
- Add `templates/readme-quality-checklist.md` or repo-specific equivalent.
- Add validation documentation if a command already exists.

Exit criteria:

- Standard language exists in repo-local docs.
- No private paths, credentials, internal hosts, or customer data are introduced.
- Validation command is known, even if it currently fails.

### Phase 2: README Lift

Upgrade README files in small, reviewable passes:

1. First screen: name, one-line position, status, and produced artifact.
2. Operating surface: system map, first-win workflow, commands, and validation.
3. Safety surface: public/private boundary, approval gates, regulated-action limits.
4. Ecosystem surface: standard level, module family, contracts, and related repos.
5. Evidence surface: sanitized examples, schemas, badges, release notes, screenshots, or sample reports.

Exit criteria:

- README reaches at least R3 quality.
- First-win workflow is executable or reviewable.
- Claims are supported by repo contents.
- Known gaps are visible and precise.

### Phase 3: Validation And Evidence

Align README claims with automated and manual gates:

- Run the repo's validation command.
- Add or verify CI badge if CI exists.
- Confirm schemas and examples referenced by README exist.
- Add sanitized proof artifacts where they are missing.
- Record known validation gaps in the README or handoff.

Exit criteria:

- Validation result is recorded.
- README does not claim gates that are not present.
- Evidence artifacts are public-safe.

### Phase 4: Ecosystem Consistency Pass

Compare standardized repos against the shared language guide:

- Use consistent terms: agent, skill, workflow, loop, ledger, gate, module, standard.
- Align module naming and compliance levels.
- Normalize "first win", "proof artifact", and "approval gate" language.
- Remove prompt-pack framing where the repo is an operating system or module.
- Ensure private pro capabilities are not described as public open-source features.

Exit criteria:

- Cross-repo README patterns are recognizable.
- Each repo still preserves its local purpose and constraints.
- Standard compatibility is easy to verify.

### Phase 5: Release And Maintenance

Treat README quality as a maintained interface:

- Check README quality during release prep.
- Update validation commands when tooling changes.
- Refresh examples after schema changes.
- Review public/private boundaries before publishing artifacts.
- Re-score README quality after major positioning or module changes.

Exit criteria:

- README quality checklist is part of release review.
- Changes in architecture, commands, or safety gates are reflected in docs.

## PR Strategy

Prefer narrow PRs:

| PR Type | Contents | Review Focus |
|---|---|---|
| Docs baseline | Add checklist, standards references, and missing operating docs. | Public safety and local instruction preservation. |
| README positioning | Upgrade title, opening, status, audience, and artifact language. | Clarity and claim discipline. |
| README operations | Add commands, workflows, architecture map, and validation. | Engineering accuracy. |
| Evidence | Add examples, schemas, sample reports, or CI references. | Sanitization and reproducibility. |
| Consistency | Normalize language across repos after local approvals. | Ecosystem alignment. |

Avoid combining implementation refactors with README quality changes unless the README would otherwise be inaccurate.

## Acceptance Gates

A repo is rollout-ready when:

- README quality is R3 or higher.
- Validation command is documented and has a recorded result.
- Public/private boundary is explicit.
- Approval gates are visible before risky workflows.
- Examples and proof artifacts are sanitized.
- The repo's ecosystem role is named.
- Local instructions remain intact.
- The rollout handoff lists files changed, validation, standard impact, public/private risk, and follow-up.

## Risk Controls

| Risk | Control |
|---|---|
| Concurrent agent edits | Prefer new files, check `git status`, avoid broad rewrites, and do not revert unknown changes. |
| Private data exposure | Review examples, screenshots, logs, paths, and config snippets before commit. |
| Unsupported claims | Tie every capability claim to a file, command, workflow, schema, or example. |
| Regulated language | Use review, triage, queue, and approval language for legal, financial, medical, tax, investor, trademark, and customer-impacting work. |
| README drift | Add README review to release and validation checklists. |
| Template overreach | Keep templates specific enough to be useful while requiring repos to fill real commands and boundaries. |

## Suggested Rollout Tracker

| Repo | Type | README Level | Validation | Missing Artifacts | Public Risk | Owner | Next Step |
|---|---|---|---|---|---|---|---|
| Example module | Open module | R1 | Unknown | First-win workflow, gates | Medium | TBD | Add checklist and README operations pass. |

## Maintenance Cadence

- Review README quality during every major release.
- Re-run checklist after schema, workflow, or approval-gate changes.
- Audit public examples quarterly or before external distribution.
- Keep the standard repo's templates aligned with field learnings from module repos.
