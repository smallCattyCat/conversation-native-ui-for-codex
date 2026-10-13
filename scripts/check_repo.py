#!/usr/bin/env python3
"""Offline starter-kit validation; requires Python 3.8+ and no dependencies."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent.parent
required=[
    "README.md","README.zh-CN.md","AGENTS.md","LICENSE","NOTICE.md",
    ".agents/skills/conversation-native-ui/SKILL.md",
    ".agents/skills/conversation-native-ui/references/surfaces.md",
    ".agents/skills/conversation-native-ui/references/evidence.md",
    ".agents/skills/conversation-native-ui/references/review.md",
    "docs/philosophy.md","docs/patterns.md","docs/quality-gates.md","docs/codex-workflow.md",
    "schemas/decision-envelope.schema.json",
    "examples/evidence-workbench/index.html",
    "examples/evidence-workbench/styles.css",
    "examples/evidence-workbench/app.js",
    ".agents/skills/conversation-native-ui/assets/patterns.css",
    ".agents/skills/conversation-native-ui/assets/patterns.js",
    "examples/pattern-gallery/index.html",
    "examples/pattern-gallery/styles.css",
    "examples/pattern-gallery/app.js",
    "scripts/install_skill.py",
    "docs/component-contracts.md",
    "docs/figma-crosswalk.md",
    "tests/browser-checks.html",
    "benchmarks/rubric.md"
]
for path in required:
    f=root/path
    assert f.is_file() and f.stat().st_size>0, f"Missing/empty {path}"
schema=json.loads((root/"schemas/decision-envelope.schema.json").read_text())
assert schema["$schema"].endswith("2020-12/schema")
for prop in ("status","finding","evidence","conditions","actions"):
    assert prop in schema["required"]
html=(root/"examples/evidence-workbench/index.html").read_text()
js=(root/"examples/evidence-workbench/app.js").read_text()
css=(root/"examples/evidence-workbench/styles.css").read_text()
for marker in ("id=\"scenario\"","id=\"evidence-list\"","id=\"confirm\"","id=\"reset\"","id=\"theme\""):
    assert marker in html, marker
for marker in ("function render()","function updateState()","replaceChildren()","textContent","addEventListener"):
    assert marker in js, marker
assert "@media(max-width:590px)" in css
assert "prefers-reduced-motion" in css
skill=(root/".agents/skills/conversation-native-ui/SKILL.md").read_text()
assert skill.startswith("---\nname: conversation-native-ui\n")
print(f"PASS — {len(required)} required artifacts; schema + static UI contracts present.")
print("NOTE — Static checks do not substitute for browser interaction, numerical validation or accessibility testing.")
from check_visual_profile import run_checks
run_checks()
