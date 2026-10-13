# R2 validation and boundaries

Date: **2026-10-13**. Scope: public Codex UI Kit source and local browser examples.

## Verified

- `python3 scripts/check_repo.py` — static structure and required assets: PASS.
- `python3 scripts/check_visual_profile.py` — 10 markup/visual-source assertions: PASS.
- `python3 -m unittest discover -s tests -p 'test_*.py'` — 4 stdlib unit tests (Skill installer and GitHub Pages site construction): PASS.
- `git diff --check` — no patch-format violations.
- Browser harness at `/tests/browser-checks.html` — 75 DOM interaction and responsive assertions PASS: 1425/1024/768/390/320px conversation views, pattern gallery responsive layout, unsaved draft preservation, scenario confirmation, versioning, append-only local conversation, card states, carousel selection, fullscreen browser dialog and local review boundaries.
- The connected desktop Chromium browser loaded the independent landing page and navigated to the staged gallery.
- The published [GitHub Actions Check Codex UI Kit run](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675625) completed successfully, including Playwright/Chromium checks.
- [GitHub Pages](https://smallcattycat.github.io/conversation-native-ui-for-codex/) deployed successfully after the owner enabled Pages; the homepage and all three live demo routes loaded in a browser with working controls and no new asset loading failures.
- GitHub accepted the full release source tree; remote and local published tree both resolved to `cb44fd4bb34d84e50882c91884b2a3348b264554`.

## Remaining limitations

1. No pixel-identical Figma claim: original design nodes were not examined; see [source crosswalk](figma-crosswalk.md).
2. No genuine MCP host display-mode integration. The standalone fullscreen dialog is a browser demonstration.
3. Codex design-output improvement is **unverified**. The [A/B benchmark](../benchmarks/README.md) is a protocol, not completed results.
4. Browser tests do not constitute full screen-reader or physical mobile-device accessibility certification.
5. GitHub Pages is [publicly deployed](https://smallcattycat.github.io/conversation-native-ui-for-codex/), with [deployment workflow attempt 2 successful](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675497). Deployment success and browser verification do not guarantee all future host configurations or device states.
6. Professional example data are explicitly illustrative, not engineering calculations or real-world actuation.

## Design provenance

Published Anthropic design tokens and surface constraints inform independently written component CSS and JavaScript. Our reading-column width, navigation dimensions, system-font fallback and fullscreen browser dialog are **adaptations**, not extracted Figma geometry.

