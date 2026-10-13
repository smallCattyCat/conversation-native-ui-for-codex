---
name: conversation-native-ui
description: Design or refine Claude-inspired web interfaces in Codex using source-mapped warm-neutral colors, typography, spacing, subtle borders, accessible controls and conversational layouts. Also provides optional evidence-aware cards and human-authorization patterns for professional assistants.
---

# Conversation-Native UI

Use this skill for Claude-inspired visual design and conversational interfaces. The visual profile is reusable on its own; evidence and authorization components are optional, task-dependent extensions.

## Visual profile first

When the user requests Claude-like UI, read [references/claude-ui-design.md](references/claude-ui-design.md) and use [assets/claude-inspired.css](assets/claude-inspired.css) as a scoped visual starting point. Preserve the warm-neutral palette, restrained hierarchy, hairline surfaces, monochrome icons and reading-oriented layout. Separate documented source values from our adaptations. Do not replace this direction with generic dashboard cards or a new accent palette.

When the task needs an interactive result, comparison, or document, read [references/surfaces.md](references/surfaces.md) and [references/pattern-contracts.md](references/pattern-contracts.md). Reusable, original standalone component CSS and DOM behaviors live in [assets/patterns.css](assets/patterns.css) and [assets/patterns.js](assets/patterns.js). Use the smallest surface and preserve the target project's conventions.

Use the user's product identity. Do not redistribute proprietary fonts or marks. A normal writing page does not need confidence meters, execution states or an evidence ledger merely because this skill supports them.

## Workflow

1. **State the job:** identify the user, question, decision, necessary evidence and safe next action. Do not start with decorative styling.
2. **Select the smallest surface:** ordinary reading -> unboxed prose; sustained editing -> document; single actionable result -> card; comparison -> collection or table; complex inspection -> workbench. Read references/surfaces.md as needed.
3. **Choose the necessary data contract:** ordinary pages need only their task data. Where source-sensitive judgments or external actions exist, express evidence, conditions and authorization explicitly; read references/evidence.md. In this repository, schemas/decision-envelope.schema.json is an optional example, not a dependency of the copied skill.
4. **Lay out the information:** prioritize readable content and the next useful action. Reveal detail on request, not through a wall of cards.
5. **Represent meaningful states:** hover, focus, selected, disabled, loading, editing and saved. Drafts must not disappear when a panel is reopened; repeated saves without text changes must not invent new versions. For consequential external actions, separate proposal, authorization and actual execution outcome.
6. **Use platform rules:** in an existing web app, follow its typography, navigation, tokens and framework. In an MCP host, use host-supported display modes and respect host context, accessibility and permissions. Do not duplicate the host chat composer.
7. **Validate:** exercise the task's core interactions, invalid input, narrow screens, keyboard navigation and dark mode. Check evidence or consequential-action states when present, not as mandatory features of ordinary pages. Use references/review.md.

## Hand-off deliverable

Provide:
- a 1-paragraph user-task description,
- chosen surface with reasoning,
- the required task data contract, with a decision/evidence schema only when relevant,
- reusable component boundaries and responsive states,
- working implementation where requested,
- test results plus any unchecked areas.

## Non-goals

- Not a claim of pixel-identical Claude screens: visual borrowing is explicit, source-mapped and adapted to the target task.
- Not a claim that a normal webpage is already an MCP App.
- Not permission to execute a physical-world or external action without authorization.
- Not a requirement to include a chat sidebar in every application.

## References

- references/surfaces.md: pattern selection and interaction limits.
- references/evidence.md: provenance, applicability and approval states.
- references/review.md: quality gates and anti-patterns.
- references/claude-ui-design.md: self-contained visual recipes, source links, documented/adapted distinctions.
- references/pattern-contracts.md: card, carousel, fullscreen, and honest state boundaries.
- assets/claude-inspired.css: portable, scoped visual tokens and primitives; no external assets required.
- assets/patterns.css and assets/patterns.js: independent DOM pattern styles and helpers for standalone sites.
- Extra repository credit: NOTICE.md. Primary source links also travel inside the skill.
