# Repository instructions for Codex

This is a framework-neutral **Claude-inspired UI design starter for Codex**, with optional evidence-aware interaction patterns and dependency-free browser demos. Keep the project small, portable and inspectable.

When the task is to design, implement or review an AI-facing interface, read .agents/skills/conversation-native-ui/SKILL.md and use its patterns as relevant. Do not impose UI machinery on unrelated work.

Visual direction:
- For Claude-inspired work, read the skill's references/claude-ui-design.md and assets/claude-inspired.css first.
- Use the documented neutral palette, restricted type hierarchy, quiet borders, monochrome SVG icons and reading-led layout. Do not drift back into a generic green-accent dashboard.
- Preserve source attribution and distinguish documented tokens from our own spacing, font substitutions and page compositions.
- Evidence/authorization UI is task-dependent; do not add it to every ordinary writing or research screen.
- Reuse the optional assets/patterns.css and patterns.js only when building an interactive card, comparison or workbench. Check references/pattern-contracts.md for state semantics.

Priorities:
1. Understand the user's **decision/action**, not just the desired layout.
2. Separate observed evidence, computed result, model inference and unknown/unverified content.
3. Prefer compact, single-purpose cards; expand to a workbench for complex inspection.
4. Every consequential action must have a distinct human confirmation and a separate execution result. Demo controls must not claim live execution.
5. Preserve provenance, applicability limits, version, and review/feedback state.
6. Support keyboard, touch, reduced motion, narrow screens, and dark mode.
7. Never use or vend third-party proprietary UI assets, logos, or fonts without explicit license review.
8. Treat the community Figma link as inspiration; only claim pixel fidelity when an actual design file/node has been accessed.

Scope:
- Use plain HTML/CSS/JS for the demonstration unless a deliberate migration is requested.
- Keep demo data clearly marked illustrative. Do not imply real simulations, live API outputs, or physical control actions.
- Avoid dependencies, tracking, telemetry and credentials.

Checks before completion:
- Run: python3 scripts/check_repo.py
- Run: python3 scripts/check_visual_profile.py && python3 -m unittest discover -s tests -p 'test_*.py'.
- Serve the repository; open tests/browser-checks.html and check the full assertion report, including editor draft safety, gallery patterns and narrow screen behavior.
- Record any checks not performed; don't invent passing tests.
