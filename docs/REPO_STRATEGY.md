# Repository Strategy

## Strategic Rule

Use one standard repo and many module repos.

The standard repo defines language, contracts, schemas, compliance levels, and templates. Module repos implement the standard for a specific buyer and workflow.

## Recommended Repo Graph

| Repo | Role | Visibility |
|---|---|---|
| `agentic-operating-system-standard` | Public standard and compliance layer. | Public |
| `Starlight-Intelligence-System` | Intelligence kernel and public doctrine. | Public |
| `Agent-Intelligence-System` | Discovery, profiles, routing, MCP, and metadata. | Public |
| `agentic-creator-os` | Creator execution substrate and multi-runner skills. | Public |
| `agentic-business-os` | Founder, revenue, operations, and business command module. | Public or split public/pro |
| `agentic-investor-os` | Thesis, diligence, memo, portfolio support, and investor workflows. | Public starter plus private pro |
| `domain-intelligence-system` | Domain asset intelligence plugin and managed-offer system. | Private pro |
| `agentic-asset-intelligence-system` | Cross-vertical asset intelligence umbrella. | Public starter plus private pro |

## Split Rule

Create a new repo only when the module has:

- Its own buyer.
- Its own first workflow.
- Its own examples.
- Its own release cadence.
- Its own commercial path.

Otherwise, keep it as a folder, document, or template inside this standard repo.

## Public/Private Model

Public repos should contain:

- Standards.
- Starter docs.
- Sanitized examples.
- General templates.
- Installation and adoption guides.

Private repos may contain:

- Premium plugins.
- Customer workflows.
- Proprietary scoring and routing logic.
- Internal pricing and deal strategy.
- Sensitive integrations.
- Customer ledgers.

## Naming Rule

Use precise names:

- `agentic-creator-os`
- `agentic-business-os`
- `agentic-investor-os`
- `domain-intelligence-system`
- `agentic-asset-intelligence-system`

Avoid names that promise outcomes, imply assured income, or blur public standard with private implementation.
