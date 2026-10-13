# R2 — Claude-inspired, reusable conversation patterns

The public source of the Conversation-Native UI for Codex starter is now at [GitHub](https://github.com/smallCattyCat/conversation-native-ui-for-codex). Publication began on **2026-10-13**. GitHub Actions checks passed; interactive GitHub Pages requires the repository owner to enable Pages in Settings.

## Fixed

- Reopening a working note no longer overwrites uncommitted edits.
- Switching examples or starting a new conversation with dirty text requires confirmation.
- Revisions increment only for changed, nonblank content.
- Local follow-up messages append rather than replace earlier turns.
- Supported browsers warn before reloading/navigating away with unsaved drafts.

## Added

- **Pattern Gallery**: inline card (ready/loading/empty/error), four-option carousel and standalone browser-fullscreen editable workspace.
- Portable scoped `assets/patterns.css` and `assets/patterns.js`.
- Safe installer `scripts/install_skill.py` with dry-run and backup-before-force-update behavior.
- Figma/official source-to-implementation crosswalk.
- Three-task A/B benchmark protocol and scoring rubric (**not yet executed**).
- Python tests, 75 browser assertions and GitHub Actions tests (including Chromium).
- Independent GitHub Pages landing-page source, path tests and deployment workflow.

## Not included

True Claude or ChatGPT MCP-host integration, Figma node-level pixel comparison, a real model backend, live professional computations or measured Codex design-output improvement.

## Try it locally

```bash
python3 -m http.server 8000
# Browse /examples/pattern-gallery/
python3 scripts/check_repo.py
python3 scripts/check_visual_profile.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/install_skill.py --target /path/to/project --dry-run
```

See [README.md](README.md), [component contracts](docs/component-contracts.md), [validation](docs/validation-R2.md), and [Pages activation](docs/publishing.md).
