#!/usr/bin/env python3
"""Score a README against the Agentic Operating System README quality bar."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


CHECKS = [
    ("title", 8, re.compile(r"^#\s+\S+", re.MULTILINE), "Has a top-level product title."),
    ("promise", 10, re.compile(r"\*\*.+\*\*"), "Has a concise bold promise near the top."),
    ("buyer_or_audience", 10, re.compile(r"\b(buyer|audience|founder|creator|investor|operator|team|agency|portfolio)\b", re.IGNORECASE), "Names who it is for."),
    ("first_win", 12, re.compile(r"\b(first[- ]win|first workflow|first win|use it|quick start)\b", re.IGNORECASE), "Shows the first useful workflow."),
    ("artifact_map", 12, re.compile(r"\b(artifact|what it produces|output|repository map|core files)\b", re.IGNORECASE), "Names concrete outputs."),
    ("validation", 12, re.compile(r"\b(npm run validate|python .*validate|ci|github actions|validation)\b", re.IGNORECASE), "Shows how the repo is validated."),
    ("safety_gates", 12, re.compile(r"\b(gate|safety|approval|privacy|human review|human approval)\b", re.IGNORECASE), "States approval or safety gates."),
    ("standard_alignment", 10, re.compile(r"\b(standard|compliance|agentic operating system|SIS|ACOS|AIS)\b", re.IGNORECASE), "Connects to the standard or ecosystem."),
    ("commercial_or_release_path", 8, re.compile(r"\b(commercial|offer|release|support|pricing|paid|pro|managed)\b", re.IGNORECASE), "Explains release, support, or commercial path."),
    ("bounded_claims", 6, re.compile(r"\b(no |not |requires qualified human review|triage|evidence|public-safe)\b", re.IGNORECASE), "Bounds claims and uncertainty."),
]

BLOCKERS = [
    ("local_windows_path", re.compile(r"C:\\Users\\", re.IGNORECASE)),
    ("local_unix_path", re.compile(r"/Users/[A-Za-z0-9._-]+/")),
    ("secret_language", re.compile(r"\b(api[_ -]?key|secret[_ -]?token|private[_ -]?key|seed phrase|recovery phrase)\b", re.IGNORECASE)),
    ("outcome_certainty", re.compile(r"\bguaranteed\s+(income|returns|profit|revenue)\b", re.IGNORECASE)),
]


def score_readme(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    checks = []
    total = 0
    for check_id, points, pattern, description in CHECKS:
        passed = bool(pattern.search(text))
        if passed:
            total += points
        checks.append({"id": check_id, "points": points, "passed": passed, "description": description})

    blockers = []
    for blocker_id, pattern in BLOCKERS:
        if pattern.search(text):
            blockers.append(blocker_id)

    return {
        "path": str(path),
        "score": total,
        "maxScore": sum(item[1] for item in CHECKS),
        "passed": total >= 80 and not blockers,
        "checks": checks,
        "blockers": blockers,
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Assess README quality.")
    parser.add_argument("readme", nargs="?", default="README.md")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    args = parser.parse_args(argv)

    result = score_readme(Path(args.readme))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"README score: {result['score']}/{result['maxScore']}")
        for check in result["checks"]:
            marker = "PASS" if check["passed"] else "FAIL"
            print(f"{marker} {check['id']}: {check['description']}")
        if result["blockers"]:
            print("BLOCKERS: " + ", ".join(result["blockers"]))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
