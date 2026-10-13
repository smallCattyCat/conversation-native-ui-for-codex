# R2 validation and boundaries

Date: **2026-10-13**. Scope: local Codex UI Kit in Nutstore.

## Verified in this iteration

- `python3 scripts/check_repo.py` — structure and static contracts: PASS.
- `python3 scripts/check_visual_profile.py` — 10 visual/markup source checks: PASS.
- `python3 -m unittest discover -s tests -p 'test_*.py'` — 2 installer checks: PASS; install dry run, first install, refusal to overwrite, force-with-backup, and missing target covered.
- `git diff --check` — no whitespace/diff errors after final edits.
- Browser harness at `/tests/browser-checks.html`: **75 assertions PASS**, observed in the connected Chromium browser. Tests included 1425, 1024, 768, 390 and 320px conversation widths; pattern gallery at 320, 390, 768 and 1425px; draft retention on repeated open, unsaved switch confirmation/cancel, content-based versions, append-only local messages; card loading/empty/error; carousel choice state; fullscreen draft and close; theme; standalone workbench authorization boundary.
- Actual browser rendered the new pattern gallery with the public-token-inspired palette. No duplicated third-party logo/font/artwork.

## What these checks do NOT prove

1. An exact pixel match to the Figma source: no node-specific design file was inspected; see [figma crosswalk](figma-crosswalk.md).
2. Actual Claude/ChatGPT MCP display-mode compatibility: the fullscreen browser dialog is a **standalone simulator**, not an SDK integration.
3. Improved Codex model design output: the [A/B benchmark protocol](../benchmarks/README.md) is supplied but has **no completed runs**.
4. Screen-reader or physical mobile-device accessibility certification: browser interaction and width tests are narrower than comprehensive AT QA.
5. Deployment quality: no public GitHub Actions run is available until the GitHub repository is published. The CI configuration is provided, but a green remote run must be observed before calling remote CI verified.
6. Correctness of domain-specific engineering computations: all result content is illustrative only.

## Release acceptance

R2 is an honest, reusable **local design starter** with a working browser demo, portable Skill, non-destructive installer, source crosswalk, static and browser tests, and a GitHub-ready workflow. It is **not** yet a live MCP App, evidence of model-performance improvement, or a public GitHub deployment.

## Visual source decisions

Claude publicly documents the 3 display modes and shared color/type/radius tokens; we use those published constraints in original components. Our 720px reading column, 240px navigation, Georgia/system fallback and dialog-based standalone fullscreen remain *adaptations*, not exported Figma metrics.
