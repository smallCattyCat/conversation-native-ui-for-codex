# Design philosophy

## From answers to reviewable action

Conventional chat ends with an answer. Professional users often need to **inspect why**, check where the answer applies, revise inputs, and decide what to do next.

We propose the minimal interaction loop:

    Intent -> Structured suggestion -> Inspectable evidence
                  |                       |
                  +------ Revise <--------+
                  |
                Human choice -> Optional execution -> Reported outcome

The UI should represent these as **different states**, not confuse a suggestion with a command.

### Six principles

1. **Task over decoration.** Begin with the user's decision and consequence, not a dashboard layout.
2. **Small first, deep on demand.** Present one succinct result; unfold the sources only when the job requires them.
3. **Source-aware claims.** Separate measurements, calculations, citations, inferences, and illustrative samples.
4. **Conditional knowledge.** Show where a previous judgment applies and when it should be rechecked.
5. **Visible human agency.** Separate suggestions from confirmation and execution; log revisions and feedback.
6. **Portable by construction.** Keep design tokens, data contract, interface patterns and integration adapters distinct.

### Two layers of reuse

- **Design-level reuse:** Codex skill, decision rules, data contract, quality gates, documentation.
- **Implementation-level reuse:** original HTML/CSS/JS browser reference; adapt it into React/Vue/etc. only when appropriate.

This is **not** an evaluation of learning outcomes, a mechanical-control implementation, or a published evidence-based design validation. It is a practical OSS design method and reference implementation.

## Provenance

Informed by publicly documented MCP Apps UI principles, especially fitting UI to the conversation, compact inline results, multi-option layouts, adaptive full-screen workspaces, and progressive disclosure. See NOTICE.md. Our evidence contracts, interaction semantics and implementation are original additions.
