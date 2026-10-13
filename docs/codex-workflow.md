# Suggested Codex workflow

## Phase 1: Design brief

Ask Codex to extract:
- who acts,
- the user question,
- what becomes actionable,
- evidence available/missing,
- what happens if wrong,
- target environment (standalone web / Claude MCP App / ChatGPT App / internal tool).

## Phase 2: Architecture

Ask it to pick a card, comparison or workbench and explain why. Demand a small schema, reusable component boundaries and an explicit authorization-state model before full UI implementation.

## Phase 3: Implement

For an existing project, respect its framework and tokens. For a scratch demo, vanilla HTML/CSS/JS is sufficient. For a real MCP App, use the current official SDK and host guidelines; this repository is **not** an MCP Server.

Portable DOM patterns and interfaces: [component-contracts.md](component-contracts.md). Source-to-implementation rules: [figma-crosswalk.md](figma-crosswalk.md). Open the [pattern gallery](../examples/pattern-gallery/index.html) before adapting to another project.

## Phase 4: Verify

Test the interaction with real browser inspection, accessibility and narrow screens. Review every numerical and system-status label against its actual source. Verify code doesn't report an operation as completed merely because someone clicked.

Run the three [benchmark tasks](../benchmarks/README.md) under both baseline and Skill-enabled conditions to test whether the design instructions materially improve new Codex output. Do not report a result until the outputs have actually been generated and scored.

## Copy-paste prompt

> Use the conversation-native-ui skill in this repository. Build one actionable, evidence-aware screen for the current task. Start with the user decision; choose the smallest useful surface; express observed/computed/inferred/illustrative evidence separately; show conditions and unknowns; make consequential actions reviewable and authorized. Produce running code and verify behavior, responsiveness, keyboard accessibility, and truthful state transitions.

## Related research/application contexts

Education: make calculation and assumptions an object students can inspect, discuss and revise.

Engineering: make operational recommendations reviewable while keeping any external control channel explicitly outside the UI unless a verified authorized interface exists.
