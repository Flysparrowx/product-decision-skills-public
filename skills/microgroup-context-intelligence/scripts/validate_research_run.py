#!/usr/bin/env python3
"""Validate the core integrity of a Microgroup Research Run JSON file."""

import json
import sys


REQUIRED = {
    "schema_version", "run_id", "decision", "research_depth", "target_group",
    "geography", "time_window", "access_and_ethics", "sources", "evidence",
    "findings", "limitations", "expiry", "recommendation",
}
DEPTH_MINIMUMS = {"SCAN": (6, 3), "STANDARD": (15, 3), "DEEP": (15, 3)}


def validate(data):
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))

    depth = data.get("research_depth")
    if depth not in DEPTH_MINIMUMS:
        errors.append("research_depth must be SCAN, STANDARD, or DEEP")

    ethics = data.get("access_and_ethics", {})
    if ethics.get("authorized_sources_only") is not True:
        errors.append("authorized_sources_only must be true")
    if ethics.get("risk") == "STOP":
        errors.append("STOP-risk runs cannot be marked valid")
    if depth == "DEEP" and ethics.get("human_review") is not True:
        errors.append("DEEP requires human_review=true")

    sources = data.get("sources", [])
    source_ids = [item.get("id") for item in sources]
    if None in source_ids or len(source_ids) != len(set(source_ids)):
        errors.append("source ids must be present and unique")

    evidence = data.get("evidence", [])
    evidence_ids = [item.get("id") for item in evidence]
    if None in evidence_ids or len(evidence_ids) != len(set(evidence_ids)):
        errors.append("evidence ids must be present and unique")
    for item in evidence:
        if item.get("source_id") not in source_ids:
            errors.append(f"evidence {item.get('id')} references unknown source")

    if data.get('recommendation') == 'INSUFFICIENT_EVIDENCE' and not data.get('limitations'):
        errors.append('insufficient-evidence runs must disclose limitations')

    # Sparse evidence is truthfully reportable, but cannot certify sufficient research.
    if depth in DEPTH_MINIMUMS and data.get('recommendation') != 'INSUFFICIENT_EVIDENCE':
        minimum_items, minimum_types = DEPTH_MINIMUMS[depth]
        source_types = {item.get("source_type") for item in evidence if item.get("source_type")}
        if len(evidence) < minimum_items:
            errors.append(f"{depth} requires at least {minimum_items} evidence items")
        if len(source_types) < minimum_types:
            errors.append(f"{depth} requires at least {minimum_types} source types")

    for finding in data.get("findings", []):
        for evidence_id in finding.get("evidence_ids", []) + finding.get("counterevidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"finding {finding.get('id')} references unknown evidence {evidence_id}")

    if data.get("recommendation") not in {"GO", "REVISE", "INSUFFICIENT_EVIDENCE"}:
        errors.append("invalid recommendation")
    return errors


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_research_run.py <run.json|->")
    stream = sys.stdin if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8")
    try:
        data = json.load(stream)
    finally:
        if stream is not sys.stdin:
            stream.close()
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("VALID STRUCTURE — evidence sufficiency is not certified")


if __name__ == "__main__":
    main()
