"""Day 3 mini-project: a tiny eval harness for an "action item extractor" feature.

Evaluation is one of an AI engineer's core responsibilities, and it starts
before the feature is "done". This script runs fixed test cases through the
feature and checks the results with simple, deterministic rules.

Run:
    pip install openai
    export OPENAI_API_KEY="sk-..."
    python run_evals.py
"""

import json
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-4o-mini"  # any chat model your account can use

INSTRUCTIONS = """Extract action items from a meeting transcript.
Return JSON only: {"items": [{"owner": "<name>", "task": "<short task>"}]}
Rules:
- Only include tasks someone explicitly agreed to do.
- The owner must be one of the attendees.
- If there are no action items, return {"items": []}."""


def extract_action_items(client: OpenAI, attendees: list[str], transcript: str) -> list[dict]:
    """The feature under test."""
    response = client.responses.create(
        model=MODEL,
        instructions=INSTRUCTIONS,
        input=f"Attendees: {', '.join(attendees)}\n\nTranscript:\n{transcript}",
        temperature=0,
    )
    text = response.output_text.strip().removeprefix("```json").removesuffix("```")
    return json.loads(text)["items"]


def check(case: dict, items: list[dict]) -> list[str]:
    """Deterministic checks. Returns a list of failure reasons (empty = pass)."""
    failures = []
    owners = {item.get("owner") for item in items}

    if not case["min_items"] <= len(items) <= case["max_items"]:
        failures.append(
            f"expected {case['min_items']}-{case['max_items']} items, got {len(items)}"
        )
    for name in case["expected_owners"]:
        if name not in owners:
            failures.append(f"missing owner: {name}")
    invented = owners - set(case["attendees"])
    if invented:
        failures.append(f"owner not in attendees: {sorted(invented)}")
    return failures


def main() -> None:
    client = OpenAI()
    cases = json.loads((Path(__file__).parent / "eval_cases.json").read_text())
    passed = 0

    for case in cases:
        try:
            items = extract_action_items(client, case["attendees"], case["transcript"])
            failures = check(case, items)
        except (json.JSONDecodeError, KeyError) as err:
            items, failures = [], [f"bad output format: {err}"]

        status = "PASS" if not failures else "FAIL"
        passed += not failures
        print(f"[{status}] {case['id']}: {items}")
        for reason in failures:
            print(f"         - {reason}")

    print(f"\n{passed}/{len(cases)} cases passed")


if __name__ == "__main__":
    main()
