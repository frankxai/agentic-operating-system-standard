# Quality-first orchestration extension

Status: optional draft extension, version 1. No existing conformance claim is
upgraded by adopting this document.

The companion `schemas/orchestration-dispatch.v1.schema.json` describes portable
task packets. Each packet identifies intent, repository, input references, owned
paths, artifact, stop condition, verification, risk, dependencies and required
runtime capabilities. Graph cycles, conflicting writer scopes and capability
freshness require runtime checks in addition to schema validation.

## Responsibilities

Company leadership sets outcome priorities. One coordinator owns dependencies,
integration, review and eligible merges. Domain owners define acceptance criteria;
specialists produce bounded artifacts. Role names do not imply active processes.

Supported reference patterns are single owner, sequential handoff, independent
parallel workers, manager with synthesis, and implementer/verifier refinement.
Admission limits concurrency. Retry and refinement limits are explicit. A timed
out worker must not be assumed stopped until its runtime confirms cancellation.

## Evidence levels

1. **Documented:** official guidance describes a capability.
2. **Available:** a successful probe verifies the exact account and runtime.
3. **Tested:** deterministic tests verify implementation behavior.
4. **Evaluated:** frozen live tasks compare quality and resource usage.
5. **Reviewed:** an independent provider reviews immutable artifacts.
6. **Released:** repository and publication gates pass with recorded evidence.

These levels are separate facts. A model catalog, passing fixture demo or authored
review cannot substitute for a later level. Missing usage remains unknown.

## Reference implementations

- Runtime: `frankxai/starlight-swarm`, `src/swarm/orchestration`.
- Runnable distribution: `frankxai/agentic-creator-os`, `tools/orchestration`.
- Evaluation: `frankxai/starlight-evals`, `harness/orchestration`.

All three are candidate additions on `codex/orchestration-quality-20260924` until
their independent review and release gates pass. Provider-specific presets are
examples outside the vendor-neutral standard. Native delegation, SDK handoffs and
hosted orchestration require separate capability and trust-boundary verification.

References: [OpenAI evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices),
[Anthropic delegation lessons](https://www.anthropic.com/engineering/multi-agent-research-system),
[ADK workflow composition](https://adk.dev/workflows/).
