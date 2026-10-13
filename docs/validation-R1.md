# R1 verification — 2026-10-13

## Checked

`python3 scripts/check_repo.py`: the original 17-artifact structural check and 8 new stdlib unit tests passed. New tests cover portable resources, attribution markers, source token values, theme/focus hooks, HTML asset paths and duplicate IDs, JavaScript DOM targets, self-contained skill links and safe sample rendering. They do not constitute full JSON Schema or JavaScript semantic validation.

`tests/browser-checks.html`: 39 assertions passed in the Mac connected Chromium browser. This harness runs the actual demo in same-origin iframes, changes their CSS viewport widths and exercises DOM events. Widths: 1425, 1024, 768, 390 and 320px. All checked widths had no horizontal overflow and kept the composer within the viewport. Task selection, light/dark theme color, system-theme selection, note opening, focus transfer, empty-edit rejection, version update, Escape handling, focus restoration, local input safety, reset, mobile note stacking and professional-workbench confirmation separation passed.

## Visual inspection

Inspected the connected browser's 1425x813 desktop screenshot and side-by-side 390px light/dark iframe screenshots. The visual target is the documented R1 profile, not an extracted Figma frame.

| Comparison point | Evidence and decision |
| --- | --- |
| Neutral palette | Documented warm canvas, softer rail and foreground card colors are distinct. Dark surfaces retain hierarchy. |
| Typography | Editorial serif title/response and sans-serif controls are deliberately separate; these are system-font substitutions. |
| Reading width | Conversation remains bounded at 720px on desktop; 390px layout reflows without horizontal clipping. |
| Geometry | Result card and composer use the shared radius, hairline treatment and restrained shadow; controls have stronger boundaries. |
| Actions and icons | Primary action is inverse-colored; secondary action is quiet; inline SVG strokes are consistent. |
| First-viewport usability | Reduced unnecessary vertical gaps for short desktop windows; composer now fits in the inspected desktop viewport. Sidebar appearance controls remain visible. |
| Narrow layout | Rail becomes a compact header; theme controls remain available; working note stacks below conversation. |

## Deliberate adaptations and remaining limits

Source facts were checked in Anthropic's public documentation. Access to the Figma Community node tree and official image downloads was not available, so no pixel-identical Figma or Claude-product claim is made. Widths, spacing assignments, system fonts and page composition are original adaptations. No generated concept image or third-party font is part of this version.

The browser checks use simulated DOM events and CSS-sized iframes; they are not physical-device, screen-reader or touch-gesture certification. Clipboard success, cross-browser behavior, live model integration and MCP transport were not tested. The new demo is a frontend reference with authored samples, not a deployed assistant.
