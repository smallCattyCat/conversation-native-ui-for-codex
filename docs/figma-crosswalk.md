# Design-source crosswalk — R2

Last checked: **2026-10-13**. Source of truth: [Anthropic MCP Apps for Claude design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines) and [transparent theme guidance](https://claude.com/docs/connectors/building/mcp-apps/transparent-theming). Original [Figma Community file](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude) is linked for designers but **was not inspected node-by-node**. No pixel fidelity claim is made.

| Reference | Published source detail | R2 implementation | Source status |
| --- | --- | --- | --- |
| Visual tokens | light #FFFFFF / #F5F4ED / #FAF9F5; dark #30302E / #262624 / #141413 | `assets/claude-inspired.css` (semantic host-first aliases) | documented values |
| Typography | heading/body/caption; 400/600 hierarchy; Anthropic Sans in host | System sans and Georgia substitute, 20/16/12px core components | source hierarchy; font choice adapted |
| Geometry | radius 4/6/8/10/12px, 0.5px regular border | 8px controls, 12px cards, thin separators | published scale; role assignment adapted |
| Inline Card | maximum 2 bottom actions, 4–5 points; no internal scroll | `pattern-gallery` compact card, four states, two actions | host rule reflected in example |
| Inline Carousel | 3–8 comparable cards, consistent hierarchy and one optional CTA each | Four options, matched artwork/title/summary/one action | behavior adapted; artwork original |
| Full Screen | detailed work with host composer/context; no floating panels | Standalone `dialog` fullscreen **simulator** | conceptual only; host integration not implemented |
| Mobile | 44pt targets, safeAreaInsets and scroll-padding with host context; 320px+ width | 44px web targets, CSS `env(safe-area-inset-*)`, scroll-snap | adapted; not real hostContext |
| Loading | skeleton matches end-state content | Card loading skeleton without artificial network delay | principle applied |
| Chat vs app | text interaction in host composer; direct manipulations in UI | Standalone composer only; components use direct controls | valid standalone; embedded use differs |

## What is still unverified

The community file's exact frame dimensions, typography rendering, image treatment and per-component spacing were not available from its public URL. To measure these details directly, open/duplicate the Figma source and supply a **node-specific `figma.com/design/...` link** with permission to read. Do not invent the original designers' pixel measurements.

## New host-integration test for a later release

Build a separate, true MCP App example with the official [MCP Apps SDK](https://github.com/modelcontextprotocol/ext-apps), test `ui/initialize`, `availableDisplayModes`, `ui/request-display-mode`, safeAreaInsets, theme changes, CSP, and the native host composer. Only then describe the demo as working inside Claude/ChatGPT.
