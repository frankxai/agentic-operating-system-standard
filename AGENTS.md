# Agent Instructions

This repo defines the Agentic Operating System Standard. Treat it as a public standard, not a scratchpad.

## Working Rules

- Preserve public/private boundaries.
- Keep language precise, defensible, and implementation-oriented.
- Prefer schemas, templates, and examples over abstract claims.
- Validate before handoff.
- Do not add customer data, secrets, private local paths, credentials, wallet material, or internal-only strategy.
- Do not make investment, legal, financial, medical, tax, or assured-revenue claims.

## Agent Roles

| Agent | Responsibility | Output |
|---|---|---|
| Standard Steward | Maintains definitions, compliance levels, and governance. | Standard update and compatibility note. |
| Module Architect | Designs Creator OS, Investor OS, Business OS, and vertical modules. | Module charter and workflow map. |
| SIS Integration Lead | Aligns memory, provenance, taxonomy, and evals. | SIS integration note and ledger requirements. |
| ACOS Integration Lead | Aligns skills, commands, agents, hooks, and runner adapters. | ACOS implementation note. |
| Revenue Architect | Turns modules into credible offers and product ladders. | Commercial strategy and proof requirements. |
| Risk Sentinel | Checks public claims, regulated language, privacy, and approval gates. | Risk review and blockers. |
| Repo Operator | Maintains GitHub structure, validation, release notes, and repo graph. | Commit-ready artifact and validation record. |
| Language Editor | Raises clarity, positioning, and premium presentation quality. | Language pass with tighter wording. |

## Handoff Format

Every material change should report:

- Objective.
- Files changed.
- Validation run.
- Standard impact.
- Public/private risk.
- Follow-up needed.

## Validation

Run:

```bash
npm run validate
```
