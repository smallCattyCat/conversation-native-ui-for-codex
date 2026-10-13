# Claude-inspired visual design

Reference checked: 2026-10-13. This is a practical visual profile for Codex, not a requirement to build an evidence dashboard.

## Sources and scope

- [S1: Anthropic, MCP Apps design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines): public host tokens, typography, borders, icons, interaction constraints.
- [S2: Anthropic, transparent theming](https://claude.com/docs/connectors/building/mcp-apps/transparent-theming): runtime host styles, transparent embedded backgrounds, theme changes.
- [S3: Anthropic, brand-guidelines skill](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md): brand palette, including the terracotta accent. Corporate brand guidance is not the same specification as Claude's product UI.
- [S4: MCP Apps for Claude Figma Community file](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude): original design resource. This version does not claim node-level inspection of that file.

The numeric values labeled **documented** below are from the public documentation. Layout widths, spacing assignments, font substitutions and component compositions labeled **adapted** are our implementation choices. Never describe them as extracted Figma measurements.

## 1. A warm neutral foundation — documented [S1]

| Role / public token | Light | Dark |
| --- | --- | --- |
| Primary surface / color-background-primary | #FFFFFF | #30302E |
| Secondary surface / color-background-secondary | #F5F4ED | #262624 |
| Tertiary surface / color-background-tertiary | #FAF9F5 | #141413 |
| Primary text / color-text-primary | #141413 | #FAF9F5 |
| Secondary text / color-text-secondary | #3D3D3A | #C2C0B6 |
| Tertiary text / color-text-tertiary | #73726C | #9C9A92 |
| Quiet border / color-border-tertiary | rgba(31,30,29,.15) | rgba(222,220,209,.15) |

Use white as a foreground surface, the warmer secondary color for navigation and selected rows, and the tertiary color for the reading canvas. Those **role assignments are adapted**; the values are documented. Use the host's live variables when embedded rather than freezing these fallback values.

Terracotta #D97757 is a **documented brand accent [S3]**, not a universal primary-button requirement. Keep it to small, non-text accents. Our buttons use inverse text/background tokens; orange-on-white body copy must not be assumed accessible.

## 2. Quiet typographic hierarchy — documented and adapted

S1 recommends three hierarchy levels and regular/emphasized text. Its text sizes include 12, 14, 16 and 20px; heading sizes extend to 36px. Choose a small subset per surface instead of using every available size.

Default component profile: title 20px, body 16px, caption 12px, controls 14px; weights 400/600. Use a 36px editorial title only for the standalone page, not inside every card.

The Figma resource uses Anthropic Sans and Anthropic Serif; the Claude host provides Anthropic Sans at runtime [S1, S2]. **No font files are bundled.** For standalone use, our UI stack is system-ui / platform sans, and our editorial stack is Georgia / platform serif. Serif page titles and an optional serif response paragraph are our adaptation, not a claim about every Claude screen. Do not substitute the corporate Poppins/Lora brand specification for the MCP product specification.

Published 16px text line-height is 1.4 [S1]. We increase long-form reading text to 1.65; this is **adapted**, not an official token value.

## 3. Geometry without a wall of cards — documented [S1]

The published corner-radius scale is 4 / 6 / 8 / 10 / 12px, plus a fully rounded value. The regular border token is 0.5px. The hairline shadow is 0 1px 2px rgba(0,0,0,.05).

Use 8px buttons, 12px result cards and composer, quiet hairline separators, and at most one subtle elevation cue. These assignments are **adapted**. Use a stronger focus outline and sufficient control boundaries; a subtle divider is not a keyboard focus indicator.

Do not put all assistant text inside a box. Reserve a border for a selectable object, editable document or result that needs its own controls. Avoid a KPI grid unless the task is genuinely numerical monitoring.

## 4. Layout rhythm — adapted, informed by S1

Standalone starting points: 240px navigation rail, 720px reading column, 24px desktop gutters; spacing scale 4 / 8 / 12 / 16 / 24 / 32 / 48px. These are our defaults, not extracted Claude layout constants.

Let conversation prose sit on the canvas, distinguish the user's message with a secondary surface, and reveal an adjacent working note only when opened. On narrow screens stack or move the note below the conversation. Keep the input visible without covering content.

Use ordinary sentence-case labels. Do not add decorative overlines, repeated numbering, 'PROTOTYPE' pills or status badges to every section. A single clear local-demo label is sufficient.

## 5. Component recipes

| Component | Concrete recipe | Source status |
| --- | --- | --- |
| Navigation row | 44px interaction area, 8px radius, subtle selected background, one monochrome icon | Adapted from S1 |
| Assistant prose | Unboxed, bounded reading width, intentional paragraphs, sources where useful | Our composition |
| User message | Secondary surface, compact padding, aligned toward the trailing edge | Our composition |
| Result card | Short title, summary, optional source cue, bottom actions; no nested scrolling | S1 principles, our composition |
| Primary button | Inverse background/text tokens, 8px radius, 14px emphasized label | S1 tokens, our sizing |
| Secondary button | Quiet outline or transparent surface, no competing accent | Adapted |
| Composer | Text field above a separate utility row, 12px radius, restrained shadow | Standalone adaptation |
| Expandable working note | Separate document object; explicit save state; visible close control | Adapted |

Use consistently stroked monochrome SVG icons, with visible labels or accessible names. Do not substitute miscellaneous Unicode symbols for a coherent icon set.

## 6. Interaction details

Use visible segmented options for small choice sets. Preserve focus and context when opening/closing a note. Hover, focus-visible, selected and disabled states must differ. Provide at least 44px tap targets in this web implementation; the source uses 44pt mobile guidance [S1].

Respect reduced motion. For real async loading use a layout-matching skeleton [S1], but do not add artificial 'thinking' delays to a static demo.

An embedded MCP App must use host context and must not duplicate the host composer or navigation [S1, S2]. Our full-page composer is for a **standalone** website only. This repository does not implement a live MCP transport or model backend.

## 7. Reuse without forcing a domain

Start with the visual profile in ../assets/claude-inspired.css. It provides scoped .cnui styles and host-first semantic aliases. Read the task before adding evidence, confidence, applicability, approval or execution fields. Ordinary writing interfaces should not inherit engineering-control paperwork.

When asked for Claude-like design, preserve these recognizable choices before inventing new colors, gradients, bento grids or ornamental graphics. Build original components, cite the public reference, and use the user's own name/identity.
