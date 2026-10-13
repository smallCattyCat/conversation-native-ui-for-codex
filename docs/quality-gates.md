# Release and implementation quality gates

A page or component is ready to reuse only when:

- Its user task and decision point are explicit.
- The primary result and its source identity are visible.
- Applicability and uncertainty are not hidden.
- Demo samples are visibly marked.
- Proposed and executed states cannot be confused.
- Interactive controls cause real local effects, or are marked disabled.
- No external action can occur without an appropriate approval boundary.
- Narrow viewport and dark theme do not hide key content.
- Keyboard navigation, labels and focus indicator work.
- Contents are understandable without visual-only cues.
- Existing application patterns and design tokens remain respected.
- The page does not depend on proprietary images/fonts/logos.
- Source and attribution links are accurate.
- Drafts survive open/close; switching context while dirty asks permission to discard.
- Revision numbers represent real changes, not repeated clicks.
- Inline cards do not exceed two bottom actions; carousel options have a uniform card contract.
- Fullscreen standalone dialogs are not presented as a genuine MCP host display-mode request.

Recommended acceptance routine:
1. Run `python3 scripts/check_repo.py`, `python3 scripts/check_visual_profile.py` and `python3 -m unittest discover -s tests -p 'test_*.py'`.
2. Serve the repository and open `/tests/browser-checks.html`; require a full PASS report. Test scenario switch, unsaved draft prevention, carousel and workspace transitions.
3. Inspect desktop, 390px and 320px viewports in light/dark themes. Review keyboard focus, reduced motion and contrast; perform assistive-technology testing before production.
4. Recheck truthful labels and sources; explicitly identify any unrun CI or Codex A/B experiment.
