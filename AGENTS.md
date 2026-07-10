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

<!-- PREMIUM-WEB-OS:START -->
## Premium Intelligence Web OS Adoption

This repo participates in the Starlight Premium Intelligence Web OS.

For any website, app, landing page, dashboard, brand surface, visual asset, motion system, 3D/WebGL scene, generated media, or public-facing UI work:

- Read the estate OS first: `../_intelligence/README.md` when working inside the Starlight estate.
- Use the activation contract: `../_intelligence/adoption/activation-contract.md` when available.
- Treat the adopting estate's `_intelligence/` directory as the source of truth for premium web taste, design, motion, WebGL, copy, assets, and quality gates.
- Use `/pwo` or the `premium-web-os` skill for full builds; use `/mad` for a design council pass.
- Use `/pwo review-pr` before absorbing another agent's PR or branch.
- Use `/pwo absorb-assets` before using external, generated, scientific, audio, video, or 3D assets.
- Use `/pwo motion-score` before shipping cinematic scroll, sound-paired motion, or complex choreography.
- Build static composition first, add Track A local motion second, add Track B GSAP/Lenis scroll only when earned, and add 3D only with fallback and reduced-motion behavior.
- Use VIS through `../visual-intelligence` when available for asset provenance, curation packets, rights, and publication records.
- Use `../_intelligence/visual-worlds/neural-cosmos.md` when available for neuroscience, cerebrum, spine, electron, signal, or golden spiral direction.
- Do not copy reference sites or agencies. Deconstruct principles and create original execution.
- Do not ship without responsive, accessibility, performance, reduced-motion, and visual QA checks appropriate to the change.

Repo-local instructions remain authoritative when stricter.
<!-- PREMIUM-WEB-OS:END -->

<!-- STARLIGHT-REPO-CONTRACT:START -->
## Starlight repository contract

Contract: `starlight.repo_profile.v2` · Team: `starlight-platform-team` · Priority: `now`
- Work only in assigned paths and preserve unrelated dirty files.
- Read `SYSTEM.md`, `SCHEMA.md`, and `SKILLS.md` before architectural changes.
- Use the smallest 3–5 role team and an independent verifier for release-affecting work.
- Required handoff: artifacts, checks, verifier verdict, risks, approvals, rollback, and next bounded action.
- Human-gated actions: DNS, secrets, billing, spend, migrations, destructive operations, permissions, legal/IP, brand identity, external sends, and high-risk production changes.
<!-- STARLIGHT-REPO-CONTRACT:END -->
