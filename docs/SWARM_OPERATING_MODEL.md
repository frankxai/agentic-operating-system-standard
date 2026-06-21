# Swarm Operating Model

The standard uses multi-agent execution only when the work benefits from separation of concerns. More agents are useful when each lane has a clear contract, artifact, gate, and handoff.

## Coordinator

One coordinator owns synthesis and risk decisions. The coordinator does not do every task. The coordinator keeps the objective stable, routes work, checks gates, and produces the final handoff.

## Standard Swarm Lanes

| Lane | Agent | Artifact | Gate |
|---|---|---|---|
| Strategy | Standard Steward | Standard impact note. | Consistency gate. |
| Module | Module Architect | Module charter and repo shape. | Buyer and first-win clarity gate. |
| SIS | SIS Integration Lead | Memory, provenance, taxonomy, and eval note. | Privacy and retention gate. |
| ACOS | ACOS Integration Lead | Skills, commands, agents, hooks, and adapter note. | Runner compatibility gate. |
| Product | Product Packager | Offer, proof artifact, and launch path. | Claim and buyer value gate. |
| Revenue | Revenue Architect | Price ladder and growth loop. | Outcome-claim gate. |
| Risk | Risk Sentinel | Blockers and approval requirements. | Publication, regulated, and data gate. |
| Repo | Repo Operator | Files, validation, CI, commit, and release note. | Validation gate. |
| Language | Language Editor | README and docs language pass. | Clarity and credibility gate. |

## Execution Waves

### Wave 1: Definition

- Define module.
- Define buyer.
- Define first-win workflow.
- Define public/private boundary.

### Wave 2: Contracts

- Write agent contracts.
- Write skill contracts.
- Write workflow contracts.
- Write loop map.

### Wave 3: Proof

- Build first proof artifact.
- Add examples.
- Add validation.
- Add risk review.

### Wave 4: Repo Standardization

- Add `README.md`.
- Add `AGENTS.md`.
- Add `SKILLS.md`.
- Add `WORKFLOWS.md`.
- Add `LOOPS.md`.
- Add registry and schemas.
- Add CI.

### Wave 5: Distribution

- Publish public starter.
- Keep pro implementation private.
- Add commercial offer.
- Add support path.
- Add adoption notes.

## Handoff Rule

Every worker must return:

- Objective.
- Artifact.
- Evidence.
- Blockers.
- Approval gates.
- Files changed.
- Validation run.
- Next action.

Use [handoff-packet.md](../templates/handoff-packet.md).
