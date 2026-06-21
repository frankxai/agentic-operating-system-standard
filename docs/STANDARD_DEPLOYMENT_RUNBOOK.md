# Standard Deployment Runbook

This runbook turns the Agentic Operating System Standard into a repo-estate rollout instead of a set of disconnected READMEs.

## Deployment Principle

Do not update every repo blindly. Deploy the standard in waves, starting with clean repos and clear module ownership. Dirty branches, production apps, customer repos, and private-memory repos need explicit review before edits.

## Wave 1: Standard And Active Modules

Targets:

- `agentic-operating-system-standard`
- `agentic-investor-os`
- `domain-intelligence-system`

Required:

- README states buyer, first win, output artifacts, validation, and safety gates.
- `AGENTS.md`, `SKILLS.md`, `WORKFLOWS.md`, and `LOOPS.md` exist where appropriate.
- Registry names the module role and compliance target.
- CI or local validation passes.

## Wave 2: Existing Public Modules

Targets:

- `agentic-creator-os`
- `agentic-business-os`
- `agentic-income-*`
- `health-intelligence-system`
- other clean module repos

Required:

- Preserve existing repo-specific instructions.
- Add standard references without overwriting local doctrine.
- Add README quality checklist.
- Add public/private boundary language.

## Wave 3: Substrates

Targets:

- `Starlight-Intelligence-System`
- `Agent-Intelligence-System`
- `starlight-swarm`
- `agentic-ops-hub`

Required:

- Document the substrate role.
- Do not force module-specific language into kernel repos.
- Expose compatibility contracts and routing points.

## Wave 4: Private Pro Modules

Targets:

- `domain-intelligence-system`
- private pro plugins
- customer or managed-offer repos

Required:

- Keep premium logic private.
- Keep public-safe examples sanitized.
- Add explicit approval gates.
- Validate publication safety before any public artifact.

## Multi-Agent Deployment Pattern

Use one coordinator and bounded workers:

| Lane | Scope | Output |
|---|---|---|
| Coordinator | Repo selection, risk, synthesis, push. | Final handoff and release. |
| Standard Worker | Standard docs, templates, schemas. | Standard patch. |
| Module Worker | One module repo. | Module patch. |
| Risk Worker | Claims, privacy, regulated language. | Blockers and fixes. |
| Quality Worker | README and docs quality. | Language and structure pass. |

Workers must own disjoint files or disjoint repos.

## README Deployment Gate

Run:

```bash
python scripts/assess_readme_quality.py README.md
```

Minimum passing score is `80`. A module README should read like an executable product spec, not a prompt.
