#!/usr/bin/env python3
"""Validate the Agentic Operating System Standard repo."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "STANDARD.md",
    "MODULES.md",
    "AGENTS.md",
    "SKILLS.md",
    "WORKFLOWS.md",
    "LOOPS.md",
    "registry/agentic-operating-system-standard.json",
    "schemas/module.schema.json",
    "schemas/agent-contract.schema.json",
    "schemas/workflow.schema.json",
    "templates/module-charter.md",
    "templates/agent-contract.md",
    "templates/workflow.md",
    "templates/handoff-packet.md",
    "templates/repo-readme.md",
    "templates/agents.md",
    "templates/skills.md",
    "modules/creator-os.md",
    "modules/business-os.md",
    "modules/investor-os.md",
    "modules/domain-intelligence.md",
    "modules/asset-intelligence.md",
    "docs/SIS_ACOS_INTEGRATION.md",
    "docs/REPO_STRATEGY.md",
    "docs/LANGUAGE_GUIDE.md",
    "docs/COMMERCIAL_STRATEGY.md",
    "docs/STANDARDIZATION_ROADMAP.md",
    "docs/ADOPTION_PLAYBOOK.md",
    "docs/REPO_GRAPH.md",
    "docs/SWARM_OPERATING_MODEL.md",
]

TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".txt"}
FORBIDDEN_PATTERNS = [
    re.compile(r"C:\\Users\\", re.IGNORECASE),
    re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    re.compile(r"\bguaranteed\s+(income|returns|profit|revenue)\b", re.IGNORECASE),
    re.compile(r"\bnot\s+financial\s+advice\b", re.IGNORECASE),
]


def fail(message: str) -> int:
    print(f"validation failed: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: JSON root must be an object")
    return data


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def validate_registry(root: Path) -> int:
    registry_path = root / "registry/agentic-operating-system-standard.json"
    registry = load_json(registry_path)
    for key in ["id", "version", "status", "coreSystems", "modules", "contracts", "complianceLevels"]:
        if key not in registry:
            return fail(f"registry missing {key}")
    if registry["id"] != "agentic-operating-system-standard":
        return fail("registry id mismatch")
    if len(registry["modules"]) < 5:
        return fail("registry must define at least five modules")
    for module in registry["modules"]:
        doc = module.get("doc")
        if not doc or not (root / doc).exists():
            return fail(f"module doc missing for {module.get('id')}")
    for _, relative in registry["contracts"].items():
        if not (root / relative).exists():
            return fail(f"contract path missing: {relative}")
    return 0


def validate_examples(root: Path) -> int:
    required = [
        "id",
        "name",
        "buyer",
        "purpose",
        "first_workflow",
        "agents",
        "skills",
        "workflows",
        "loops",
        "approval_gates",
        "proof_artifact",
        "visibility",
    ]
    for path in (root / "examples").glob("*.module.json"):
        data = load_json(path)
        for key in required:
            if key not in data:
                return fail(f"{path.relative_to(root)} missing {key}")
    return 0


def validate_text(root: Path) -> int:
    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            match = pattern.search(text)
            if match:
                return fail(f"{path.relative_to(root)} contains forbidden phrase or path: {match.group(0)}")
    readme = (root / "README.md").read_text(encoding="utf-8")
    for phrase in ["Agentic Operating System", "Creator OS", "Investor OS", "Business OS"]:
        if phrase not in readme:
            return fail(f"README missing {phrase}")
    return 0


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            return fail(f"missing {relative}")
    for relative in ["schemas/module.schema.json", "schemas/agent-contract.schema.json", "schemas/workflow.schema.json"]:
        schema = load_json(root / relative)
        if schema.get("type") != "object":
            return fail(f"{relative} must be an object schema")
    for check in [validate_registry, validate_examples, validate_text]:
        result = check(root)
        if result:
            return result
    print("Agentic Operating System Standard validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
