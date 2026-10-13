# Choose a surface, not a screen clone

The patterns here are implementation-neutral. Anthropic's published inline restrictions are **host-specific guidance**, not universal laws for standalone websites.

## Decision card

Choose when a user needs to accept, question, or use **one bounded result**.

Content order: concise finding, key evidence, applicability/uncertainty, up to two prominent actions. Keep details expandable externally; do not bury the primary judgment under metadata. When building for Claude, follow official documented limits (up to 4–5 data points and 2 bottom actions). In other hosts, follow their own guidelines.

## Comparison collection

Choose when the user is selecting among alternatives measured on comparable dimensions. Require genuinely comparable units, the same baseline, and clear exceptions. A carousel helps only when options are few and visually scannable; otherwise prefer a comparison table.

## Evidence workbench

Choose for iterative settings, plotting, long evidence, revision history, or collaborative critique. Keep the output and its inputs visible at once when possible; make revisions distinct from original observations. On phones, collapse sidebars without hiding evidence or action status.

## Selection decision

- If the next action is 'acknowledge or inspect', choose a card.
- If the next action is 'choose among options', choose collection/table.
- If the next action is 'adjust, verify or co-edit', choose workbench.
- If the material is only a long document, use a normal document, not an inline card.

Never create a redundant chat input inside a conversational host. For standalone products, a chat entry may be appropriate, but treat it as its own component and avoid hiding task controls.
