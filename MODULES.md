# Module Map

The standard is not one product. It is a family of interoperable operating systems.

## Core Stack

| Module | Job | Primary Output |
|---|---|---|
| SIS | Intelligence kernel and governance substrate. | Memory, taxonomy, provenance, evals, system rules. |
| AIS | Discovery, capability profiles, routing, and metadata. | `llms.txt`, `agents.json`, MCP, profile schema. |
| ACOS | Agentic creator execution substrate. | Skills, commands, agents, hooks, adapters. |

## Domain Modules

| Module | Buyer | First Workflow |
|---|---|---|
| Creator OS | Creators, founders, studios, agencies. | Brief to content, product, media, launch, distribution. |
| Business OS | Founders, operators, agencies, teams. | Objective to offer, revenue system, ops cadence, metrics. |
| Investor OS | Investors, founders, funds, angels, accelerators. | Thesis to diligence memo, risk register, portfolio support. |
| Domain Intelligence | Domain investors, creators, founders, agencies. | Candidate to verification, route, report, decision ledger. |
| Asset Intelligence | Operators turning digital surfaces into assets. | Surface to evidence, monetization route, system loop. |

## Module Requirements

Every module needs:

- A precise buyer and use case.
- A first-win workflow.
- Agent roles and skill inventory.
- Approval gates.
- Proof artifact.
- Repo ownership model.
- Commercial offer path.
- Public/private boundary.

## Recommended Repo Shape

```text
module-repo/
├─ README.md
├─ AGENTS.md
├─ SKILLS.md
├─ WORKFLOWS.md
├─ LOOPS.md
├─ registry/
├─ schemas/
├─ templates/
├─ examples/
├─ docs/
└─ scripts/
```

## Module Decision Rule

Create a separate repo when the module has:

- Its own buyer.
- Its own first-win workflow.
- Its own examples.
- Its own release cadence.
- Its own private/pro packaging path.

Keep it as a folder when it is only a supporting pattern or shared contract.
