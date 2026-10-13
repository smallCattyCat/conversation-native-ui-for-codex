# Publishing and deployment status (2026-10-13)

## Public source: published

The public repository is [smallCattyCat/conversation-native-ui-for-codex](https://github.com/smallCattyCat/conversation-native-ui-for-codex). Its `main` branch contains all 58 release source files, including the Codex Skill, standalone demos, tests, landing-page source, and GitHub Actions workflows.

The initial publication commit is [9635209](https://github.com/smallCattyCat/conversation-native-ui-for-codex/commit/9635209e7e17c02f55ed3bf28623c4225bbb2a2f). The source tree matched the local R2 publication tree SHA `cb44fd4bb34d84e50882c91884b2a3348b264554`.

The first [Check Codex UI Kit workflow](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452145435) completed successfully, including Python tests, JavaScript checks, dependency installation and Chromium browser tests.

## One remaining owner setting: GitHub Pages

The [Pages workflow](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions/runs/38452145322) built the site and passed site-path tests, but failed at `actions/configure-pages` because GitHub Pages was not yet enabled for the repository. This is **not** a static-site build failure.

To enable:

1. Open [Settings → Pages](https://github.com/smallCattyCat/conversation-native-ui-for-codex/settings/pages).
2. Under **Build and deployment → Source**, choose **GitHub Actions**. Save if required.
3. In [Actions](https://github.com/smallCattyCat/conversation-native-ui-for-codex/actions), open the latest **Publish demo to GitHub Pages** run and choose **Re-run failed jobs**, or dispatch that workflow manually.
4. Wait for both build and deploy jobs to complete successfully, then open the site.

Expected public site **after the successful deployment only**:
https://smallCattyCat.github.io/conversation-native-ui-for-codex/

The Pages workflow stages original components into a self-contained static site. It does not require a model backend, API key, third-party fonts, or a running MCP host.

## History and security

Public history was initialized without the earlier locally generated macOS `.local` author emails. The earlier development history is preserved only in private local backup branches. Do not push all local branches or use `git push --mirror` without a separate audit.

All repository content was screened for credentials, personal paths and embedded private assets before publication. Demo data are illustrative. The repository is an **unofficial** adaptation of public design ideas, not an Anthropic/Claude or OpenAI product, and does not redistribute original Figma artwork.

## Open research / validation boundaries

The Codex Skill A/B benchmark is specified but **not run**. There is no Figma node-level pixel-match assertion or genuine Claude/ChatGPT MCP App host integration. Browser CI passing does not substitute for assistive-technology certification.

Primary references: [source crosswalk](figma-crosswalk.md), [R2 validation](validation-R2.md), [official GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
