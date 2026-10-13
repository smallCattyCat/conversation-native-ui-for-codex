# Component choices and state contracts

This skill can be copied alone, so the recipes below do not depend on the surrounding repository.

## Inline result card

Use one result with no more than two meaningful bottom actions when designing for Claude inline. Limit data points to 4–5. Preserve loading/empty/error alternatives and never show a fake "completed" status. See `../assets/patterns.css` and `.cn-pattern-card`.

## Comparable choices

Use the `../assets/patterns.js` named `initCarousel(root, onSelect)` helper for 3–8 consistently sized options. The DOM contract is `[data-cn-carousel]`, `[data-carousel-track]`, `[data-carousel-previous]`, `[data-carousel-next]`, `[data-carousel-option]` and `[data-select-option]`. Each card gets one selection action. Support native horizontal scroll, focusable track, and visible selected state. For many or incomparable options, prefer a normal table.

## Fullscreen workspace

For a **standalone website**, a `<dialog class="cn-workspace-dialog">` plus `initWorkspace(dialog, openButtons, closeButton)` can demonstrate focused editing. The dialog is **not** an actual MCP host display-mode request. Actual Claude/ChatGPT MCP Apps must use official SDK APIs and host-provided safe areas/composer.

## Draft handling

Never reset editor text merely because the user clicks "Open" again. Track dirty state by comparing current text to the last applied version; increment versions only for actual changed content. Preserve unsaved drafts across close/reopen; ask before discarding them on task change/reset. Show local-only save explicitly when no real persistence exists.

## Source identity

Use the values and the documented/adapted distinction from [claude-ui-design.md](claude-ui-design.md). Do not claim a pixel-perfect reproduction of an inaccessible Figma file or redistribute logos/fonts.
