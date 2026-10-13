# Publishing and deployment status (2026-10-13)

## Public source: published

The public repository is [smallCattyCat/conversation-native-ui-for-codex](https://github.com/smallCattyCat/conversation-native-ui-for-codex). Its `main` branch contains all 58 release source files, including the Codex Skill, standalone demos, tests, landing-page source, and GitHub Actions workflows.

The initial publication commit is [9635209](https://github.com/smallCattyCat/conversation-native-ui-for-codex/commit/9635209e7e17c02f55ed3bf28623c4225bbb2a2f). The source tree matched the local R2 publication tree SHA `cb44fd4bb34d84e50882c91884b2a3348b264554`.

The first [Check Codex UI Kit workflow](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452145435) completed successfully, including Python tests, JavaScript checks, dependency installation and Chromium browser tests.

## GitHub Pages: deployed

GitHub Pages is enabled with **GitHub Actions** as its deployment source.

- **Live site:** [Conversation-Native UI for Codex](https://smallcattycat.github.io/conversation-native-ui-for-codex/)
- **Conversation demo:** [writing and editable note](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/claude-inspired/)
- **Interaction patterns:** [inline card, carousel, fullscreen workspace](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/pattern-gallery/)
- **Professional demo:** [evidence workbench](https://smallcattycat.github.io/conversation-native-ui-for-codex/examples/evidence-workbench/)
- **Pages workflow:** [run 38452675497, attempt 2 — success](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675497)
- **Automated tests:** [run 38452675625 — success](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452675625)

The deployment initially failed because Pages was not enabled. After the owner enabled Pages, the failed jobs were rerun. **Configure GitHub Pages**, static build, artifact upload and deployment completed successfully. The public site and all three examples were then opened in a browser, with no new console errors or failed asset loads during verification.

The `.github/workflows/pages.yml` workflow assembles a self-contained site from original example components. It does not expose hidden `.agents` URLs to GitHub Pages.

## History and security

Public history was initialized without the earlier locally generated macOS `.local` author emails. The earlier development history is preserved only in private local backup branches. Do not push all local branches or use `git push --mirror` without a separate audit.

All repository content was screened for credentials, personal paths and embedded private assets before publication. Demo data are illustrative. The repository is an **unofficial** adaptation of public design ideas, not an Anthropic/Claude or OpenAI product, and does not redistribute original Figma artwork.

## Open research / validation boundaries

The Codex Skill A/B benchmark is specified but **not run**. There is no Figma node-level pixel-match assertion or genuine Claude/ChatGPT MCP App host integration. Browser CI passing does not substitute for assistive-technology certification.

Primary references: [source crosswalk](figma-crosswalk.md), [R2 validation](validation-R2.md), [official GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

