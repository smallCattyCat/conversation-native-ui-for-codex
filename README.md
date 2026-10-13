# Conversation-Native UI for Codex

**Claude-inspired visual patterns for Codex:** warm-neutral surfaces, a quiet type hierarchy, subtle borders, readable conversation layouts, and small, useful controls.

A reusable Agent Skill, scoped CSS profile, standalone DOM component helpers and three working browser demos. The visual details are explicitly grounded in Anthropic's public MCP Apps for Claude design guidance. Components and page compositions are independently implemented, with documented values distinguished from our adaptations.

**[Live interactive demos](https://smallcattycat.github.io/conversation-native-ui-for-codex/)** · [Conversation](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/claude-inspired/) · [Pattern gallery](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/pattern-gallery/) · [Evidence workbench](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/evidence-workbench/)

Use the visual profile alone for everyday pages. Evidence, applicability and authorization patterns are optional extensions for professional assistants. This is an unofficial starter, not an MCP transport or model backend.

[简体中文](README.zh-CN.md) · [Source map](docs/figma-crosswalk.md) · [Conversation demo](examples/claude-inspired/index.html) · [Pattern gallery](examples/pattern-gallery/index.html) · [Professional workbench](examples/evidence-workbench/index.html) · [Publishing guide](docs/publishing.md)

## What's included

- A **source-mapped visual guide**: exact documented colors, typography and geometry, plus clearly identified adaptation choices.
- **Scoped reusable CSS** at `.agents/skills/conversation-native-ui/assets/claude-inspired.css`: light/dark themes, host-first aliases and component primitives.
- **Pattern CSS and JS** in `assets/patterns.css` and `assets/patterns.js`: stateful inline cards, accessible horizontal comparisons, and a standalone fullscreen workspace.
- A general-purpose **conversation + editable working note** demo with local sample interactions.
- A **pattern gallery** showing card ready/loading/empty/error states, an interactive four-option carousel and a fullscreen editing simulator.
- Protected unsaved drafts, deliberate resets, content-based revision numbers and append-only local message history.
- A repository-level **AGENTS.md** with concise, actionable Codex conventions.
- A reusable **Agent Skill** at .agents/skills/conversation-native-ui/SKILL.md.
- Three surface patterns: **decision card**, **comparison collection**, **evidence workbench**.
- An original **Decision Envelope** JSON contract for evidence, limits, provenance, and reviewable actions.
- A standalone browser demo in examples/evidence-workbench/ (plain HTML/CSS/JS; no install).
- A safe Skill installer, GitHub Actions checks, browser interaction tests, benchmark tasks, review checklist and attribution notes.

## Try the working demo

Open `examples/claude-inspired/index.html` in your browser, or serve the repository:

    python3 -m http.server 8000

Then visit http://localhost:8000/examples/claude-inspired/ . The new gallery is at `/examples/pattern-gallery/`; the professional task demo is at `/examples/evidence-workbench/`.

The conversation demo supports three sample tasks, light/dark/system themes, protected working drafts, version increments for changed text and an append-only local conversation. It uses authored samples, not model-generated answers. The gallery and professional workbench also use illustrative data.

## Use with Codex in a different repository

Run the dependency-free installer against an existing target project:

    python3 scripts/install_skill.py --target /path/to/my-codex-project --dry-run
    python3 scripts/install_skill.py --target /path/to/my-codex-project

If the Skill is already installed, the installer refuses to overwrite it. Use `--force` only when you want it to **back up the previous copy before replacing it**. Alternatively copy this directory manually:

    .agents/skills/conversation-native-ui/

into your target project at the same relative path (or use a compatible skills installer). Ask Codex:

> Use $conversation-native-ui with the Claude-inspired visual profile. Read references/claude-ui-design.md and assets/claude-inspired.css first. Preserve warm neutrals, quiet typography, hairline surfaces, monochrome icons and the reading-oriented layout. Adapt to [task] and our product identity; do not generate a dashboard or evidence ledger unless the task needs one. Test interaction states and responsive behavior.

Optionally adapt the guidance from AGENTS.md into your project's existing AGENTS.md. Do **not** blindly replace existing project instructions.

The Skill is **guidance plus portable CSS and DOM helpers**, not a published React/npm component package or an MCP host implementation. See [component contracts](docs/component-contracts.md).

## Adapt with Figma

If you have a properly accessible Figma Design copy, connect Figma MCP to Codex, pass a **node-specific** design link, and ask Codex to map the design concepts to your project's own tokens and components. The original Figma Community URL alone is not a readable node-specific design file.

## Core rule

Separate **suggested action**, **human authorization**, and **execution outcome**. Display where evidence came from, where a conclusion applies, and where it does not.

## Project structure

    AGENTS.md
    .agents/skills/conversation-native-ui/
    docs/
    schemas/decision-envelope.schema.json
    examples/claude-inspired/
    examples/pattern-gallery/
    examples/evidence-workbench/
    scripts/check_repo.py
    scripts/install_skill.py
    benchmarks/
    .github/workflows/checks.yml

## Validation

    python3 scripts/check_repo.py
    python3 scripts/check_visual_profile.py
    python3 -m unittest discover -s tests -p 'test_*.py'

A successful check validates repository structure and key examples; it does **not** prove any simulated engineering result.

With the local server running, open `/tests/browser-checks.html` for browser-executed DOM and responsive assertions. [R2 validation](docs/validation-R2.md) records what was actually tested. Optional GitHub CI installs Playwright to automate Chromium checks; standalone demos themselves do not require npm. The [Codex A/B benchmark protocol](benchmarks/README.md) is prepared but **has not been executed**.

## Public demo deployment

Build the static GitHub Pages bundle locally without installing dependencies:

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --directory site-dist
```

The standalone landing page is at http://localhost:8000/ and links to all three demos. Source paths for the portable Skill are rewritten to public `assets/` in the generated site. **GitHub Pages is live at [the public demo site](https://smallcattycat.github.io/conversation-native-ui-for-codex/)**; the [deployment workflow](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675497) completed successfully on its second attempt. See [publishing instructions](docs/publishing.md).

## Attribution and licensing

Original code and writing in this repository: MIT license (see LICENSE).

Visual references: [Anthropic's public MCP Apps design guidance](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines) and [Figma UI Kit](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude). Source-to-implementation mapping and font substitutions: [visual guide](.agents/skills/conversation-native-ui/references/claude-ui-design.md). Full credits: [NOTICE.md](NOTICE.md). The original [MCP Apps for Claude Community resource](https://www.figma.com/community/file/1597641111449594397/mcp-apps-for-claude) is **not vendored** here. Claude, Anthropic, Codex, Figma, and other product names belong to their respective owners. This project is not affiliated with or endorsed by them.

