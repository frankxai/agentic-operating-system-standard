# Portable Repository And Team Profile Contracts

This standard recognizes two versioned Starlight contracts:

| Contract | Canonical schema identifier | Purpose |
|---|---|---|
| `starlight.repo_profile.v2` | `https://starlight.local/schemas/starlight-repo-profile.v2.schema.json` | Describes one repository's operating identity, runtime surface, team binding, permissions, and release evidence. |
| `starlight.team_profile.v2` | `https://starlight.local/schemas/starlight-team-profile.v2.schema.json` | Describes a composable agent team, its role scopes, routing, gates, verifier, and evaluation requirements. |

These are portable identifiers. The canonical schemas and full operational payloads belong to the adopting organization's control plane. A public standard, registry, or module MUST reference the identifiers and interoperability concepts; it MUST NOT copy private topology, credentials, customer context, absolute machine paths, or internal policy data into a public projection.

## Repository Profile Interoperability

A conforming `starlight.repo_profile.v2` implementation exposes, directly or through documented adapters:

- Stable repository identity, operating unit, lifecycle, priority, human owner, and canonical-source status.
- Commands, services, documentation, runtime dependencies, and data classification.
- Deployment targets, promotion policy, and rollback ownership without secret values.
- A `starlight.team_profile.v2` binding and references to skills, plugins, tools, and allowed write scopes.
- Required local, CI, security, experience, AI, release, and evidence gates.

The profile is an operating contract, not a repository inventory dump. Fields that are not needed for routing, safety, verification, or ownership SHOULD remain in their product-owned systems.

## Team Profile Interoperability

A conforming `starlight.team_profile.v2` implementation exposes:

- One accountable coordinator and the smallest useful set of specialist roles.
- Per-role capability references, tool permissions, allowed write scopes, stop conditions, and expected outputs.
- Explicit routing and handoff rules for completion, failure, blocked work, and approval requests.
- Required skills, plugins, human gates, and evaluation-suite references.
- An independent verifier with no implementation write scope for the artifact being verified.
- Owner, lifecycle, version, canonical source, and projection provenance.

A team profile defines available composition. A job contract selects the bounded subset required for one objective; it SHOULD NOT activate every role by default.

## Public Registry Binding

A public or sanitized registry stores references rather than canonical payloads. Its binding SHOULD contain:

- Contract ID and exact canonical schema identifier.
- Stable profile ID and registry record ID.
- Role-scope, gate, verifier, routing, and repo-to-team references.
- Projection kind, portable source reference, content hash when available, owner, lifecycle, version, and review date.

Every reference MUST resolve within the registry or through a declared external namespace. The contract ID and schema identifier MUST be paired exactly. A verifier MUST be independent for the artifact under review.

## Authority And Drift

Resolution order is:

1. Canonical profile owned by the adopting control plane.
2. Repo-local projection generated from that profile.
3. Capability-registry projection used for routing and discovery.
4. Runner-specific adapter generated from the registry projection.

Higher-numbered projections MUST NOT silently override lower-numbered authority. A projection is stale when its contract version, content hash, owner, role scopes, gates, verifier, routing, or lifecycle differs from its canonical source. Stale projections MUST be regenerated, reviewed, or marked unavailable.

## Compatibility

- Additive optional fields are backward-compatible within v2.
- A stricter gate, narrower write scope, or new human approval requirement takes effect immediately and is not treated as a breaking relaxation.
- Renaming required fields, weakening gates, widening permissions, or changing profile identity requires a new major contract version.
- Adapters MAY preserve legacy filenames such as `.agent-harness.json`, but MUST declare that the payload implements `starlight.repo_profile.v2`.
- Logical schema identifiers are identity anchors; adopters MAY resolve them through a local catalog rather than a public network request.

Use [repo-profile.md](../templates/repo-profile.md) and [team-profile.md](../templates/team-profile.md) to document a sanitized projection.
