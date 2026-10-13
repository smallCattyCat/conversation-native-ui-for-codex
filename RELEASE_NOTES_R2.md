# R2 — Claude-inspired, reusable conversation patterns

This release upgrades the R1 visual example into a more reliable and portable design starter.

## Fixed

- A reopened working note no longer overwrites uncommitted edits.
- Switching examples or starting a new conversation while a note is dirty asks for explicit discard confirmation.
- Revisions increment only for changed, nonblank content.
- Follow-up local messages append to the conversation rather than overwriting its first sample.
- Reload/navigation attempts warn about unsaved drafts on browsers that permit `beforeunload` prompts.

## Added

- A standalone **Pattern Gallery** with a compact inline card (ready/loading/empty/error), a four-option horizontal carousel and a browser-fullscreen editable workspace.
- Portable scoped `assets/patterns.css` and `assets/patterns.js` in the Codex Skill.
- `scripts/install_skill.py`: dry run, refuses to overwrite, opt-in backup-before-replace.
- Official-guideline-to-implementation crosswalk and explicit source boundaries.
- Structured three-task A/B benchmark protocol and scoring rubric (not yet executed).
- Python installer unit tests, more static checks, 75 browser assertions and a GitHub Actions workflow with optional Playwright Chromium execution.

## Not included

Actual Claude or ChatGPT MCP host integration, Figma node-level pixel comparison, real model backend, live technical computation, completed Codex A/B evidence or public GitHub publication.

## Quick start

```bash
python3 -m http.server 8000
# Browse /examples/pattern-gallery/
python3 scripts/check_repo.py
python3 scripts/check_visual_profile.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/install_skill.py --target /path/to/project --dry-run
```

See [README.md](README.md), [component contracts](docs/component-contracts.md), and [validation](docs/validation-R2.md).
