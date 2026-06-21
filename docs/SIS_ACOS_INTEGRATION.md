# SIS, AIS, and ACOS Integration

## Roles

| System | Role |
|---|---|
| SIS | Intelligence kernel: memory, governance, provenance, taxonomy, evals, and system discipline. |
| AIS | Discovery and routing substrate: repo profile, agents inventory, `llms.txt`, MCP, and capability metadata. |
| ACOS | Execution substrate: skills, commands, agents, hooks, workflows, adapters, and creator-facing operations. |

## Integration Principle

SIS decides what should be remembered, governed, evaluated, and proven. ACOS executes with skills, commands, agents, and hooks. AIS makes the system discoverable and routable by humans, agents, and machines.

## Shared Contracts

- Module charter.
- Agent contract.
- Skill contract.
- Workflow contract.
- Evidence ledger.
- Approval gates.
- Public/private boundary.
- Release validation.

## Practical Mapping

| Need | Route |
|---|---|
| Preserve durable learning | SIS memory and ledger. |
| Run creator workflows | ACOS skills, commands, and agents. |
| Publish repo capability metadata | AIS profile, `agents.json`, and `llms.txt`. |
| Coordinate multi-agent work | SIS/ACOS swarm contract. |
| Verify release quality | Standard validation and CI. |

## Cross-Runner Posture

The standard is runner-agnostic. Codex, Claude Code, Antigravity, Grok, Cursor, OpenAI Agents SDK, Google ADK, and Microsoft Agent Framework should all consume the same module contracts and produce comparable handoff packets.
