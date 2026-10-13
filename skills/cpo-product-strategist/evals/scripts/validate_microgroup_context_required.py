#!/usr/bin/env python3
"""Validate the bounded CPO-to-microgroup request without a model judge."""

from __future__ import annotations

import os
import re
import sys


OUTPUT = os.environ.get("EVAL_FINAL_MESSAGE", "")

REQUIRED_LINES = (
    "Microgroup context: REQUIRED",
    "Evidence status: MISSING",
    "MicrogroupContextRequest",
    "Decision held open",
    "Evidence boundary",
    "Not proof of: market size, demand, willingness to pay, or causality.",
)

REQUEST_FIELDS = (
    "Decision to inform",
    "Provisional behavioral group definition",
    "Geography",
    "Time/freshness need",
    "Decision surfaces",
    "Existing evidence",
    "Access/ethics boundary",
    "Evidence budget",
    "Stop condition",
)

DECISION_FIELDS = (
    "Dependent decision",
    "Unaffected analysis",
)

FORBIDDEN_CLAIMS = (
    re.compile(
        r"\b(?:proves?|proven|confirms?|confirmed|validates?|validated|demonstrates?)\b"
        r".{0,80}\b(?:market size|demand|willingness to pay|causality)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:доказан\w*|подтвержд[её]н\w*|валидирован\w*)\b"
        r".{0,80}\b(?:размер\w* рынк\w*|спрос\w*|готовност\w* платить|причинн\w*)\b",
        re.IGNORECASE | re.DOTALL,
    ),
)


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


if not OUTPUT.strip():
    fail("EVAL_FINAL_MESSAGE is empty")

missing_lines = [line for line in REQUIRED_LINES if line not in OUTPUT]
if missing_lines:
    fail(f"missing required contract lines: {missing_lines}")

if "MicrogroupContextPack" in OUTPUT:
    fail("research was forbidden, but a MicrogroupContextPack was returned")

request_start = OUTPUT.find("MicrogroupContextRequest")
decision_start = OUTPUT.find("Decision held open", request_start + 1)
boundary_start = OUTPUT.find("Evidence boundary", decision_start + 1)
if not request_start < decision_start < boundary_start:
    fail("contract sections are missing or out of order")

request_section = OUTPUT[request_start:decision_start]
decision_section = OUTPUT[decision_start:boundary_start]

for section, fields in (
    (request_section, REQUEST_FIELDS),
    (decision_section, DECISION_FIELDS),
):
    for field in fields:
        pattern = re.compile(
            rf"^[ \t]*[-*]?[ \t]*{re.escape(field)}:[ \t]*\S[^\r\n]*$",
            re.MULTILINE,
        )
        if not pattern.search(section):
            fail(f"missing, empty, or misplaced field: {field}")

for pattern in FORBIDDEN_CLAIMS:
    if pattern.search(OUTPUT):
        fail("microgroup context was upgraded into prohibited proof")

print("bounded MicrogroupContextRequest contract satisfied")
