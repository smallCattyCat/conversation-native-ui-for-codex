# R2 component contracts

These are **original standalone DOM reference components**, intended as an implementation guide, not a published npm component library or a real Claude MCP App.

## Importable assets

Copy the skill folder `.agents/skills/conversation-native-ui/` into your target project. Load both CSS files (in this order) in an element with the `.cnui` scope:

```html
<link rel="stylesheet" href=".agents/skills/conversation-native-ui/assets/claude-inspired.css">
<link rel="stylesheet" href=".agents/skills/conversation-native-ui/assets/patterns.css">
```

Use a module for the optional behaviors:

```js
import { initCarousel, initWorkspace } from "./.agents/skills/conversation-native-ui/assets/patterns.js";
const carousel = initCarousel(document.querySelector("[data-cn-carousel]"), choice => {
  console.log("local choice:", choice);
});
// Dispose resize observer if removing the carousel from the DOM:
carousel.destroy();
```

This is a reference with DOM event handlers and CSS, not a React package. When integrating with another framework, port **semantics and state transitions**, not the entire sample HTML.

## Inline card

- `.cn-pattern-card`, one result, up to 4–5 meaningful data points in embedded Claude mode.
- Bottom row `.cn-actions`, no more than **two** actions when designing for Claude Inline Card.
- States: ready, loading skeleton, empty, error. In loading/empty/error states, disable unavailable actions.
- No inline internal scroll or nested routed screens.
- The gallery uses a **simulated state switcher**, not network requests.

## Inline carousel

- Root `[data-cn-carousel]` with child `[data-carousel-track]`.
- Buttons `[data-carousel-previous]` and `[data-carousel-next]`.
- Between 3 and 8 `[data-carousel-option]` cards; include illustration/title/brief description and one `[data-select-option]` per card.
- The helper sets `aria-current` on cards, `aria-pressed` on actions, and disables navigation buttons at edges.
- Scroll-snap and native horizontal overflow allow touch, trackpad and keyboard scrolling. The outer page should never overflow.
- For actual MCP apps, map left/right safe-area insets from the host to the carousel root.

## Fullscreen workbench (standalone preview)

Use `<dialog class="cn-workspace-dialog">` with `initWorkspace(dialog, openButtons, closeButton)`. The dialog uses the browser's modal semantics and restores focus to its opener when closed. The workbench's own draft state stays untouched when closed. Text entry is a **standalone application editor**, not a second chat composer in Claude.

**Important:** a standalone `dialog` is not the host's fullscreen mode. Real MCP Apps must declare supported display modes and request host fullscreen via the official SDK; honor host safe areas, theme and composer. Do not imply that clicking this local dialog requests an MCP host display-mode transition.

## Suggested shared states

| Object | State | Truthful UI |
| --- | --- | --- |
| Inline result | ready/loading/empty/error | Different content and available controls |
| Comparison | none selected/selected | Mark current option + announce local selection |
| Document | unchanged/dirty/saved | Preserve draft until explicit discard |
| External decision | proposed/authorized/dispatched/executed/failed | Track separate authorization and real execution evidence |

The code only models the first three and **does not perform external actions**.

## Responsive / accessibility checks

At least 320px, 390px, tablet and desktop. Verify focus restoration, Escape close, touch target size, selected-state labels, dark mode, loading/empty/error, reduced motion and no body-wide horizontal overflow. Also perform real assistive-technology testing before production release.
