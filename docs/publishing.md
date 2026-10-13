# Public publishing checklist (2026-10-13)

This repository is prepared for public distribution but **cannot create a GitHub repository with the currently connected GitHub API actions**. No public repository or GitHub Pages site is claimed until GitHub confirms it exists and Actions completes successfully.

## One action needed from the owner

1. Visit https://github.com/new under the GitHub account **smallCattyCat**.
2. Create a **public** repository named **conversation-native-ui-for-codex**.
3. Repository description suggestion: `Independent Claude-inspired UI patterns for Codex — reusable Skill, tokens, components and live examples.`
4. Set default branch to **main**. Adding the default GitHub README is optional; the publisher can reconcile it, but an empty repository is easiest for standard Git push.
5. Make sure the existing ChatGPT GitHub connection has read/write access to this new repository. GitHub App installations scoped to selected repositories may require adding the new one.

After creation, request that the assistant finish the publish. The assistant can use the connected GitHub repository tools to upload the release contents and verify the result. No credentials should be pasted into chat.

## Safe publication rule

Historical local commits used an automatically generated macOS `.local` author email, so do **not** push the old history by accident. For public release, the distribution `main` branch is prepared as a **new root commit** under the owner's GitHub noreply address, while the previous commit history is retained in a private local backup branch. Do not use `git push --all`, `git push --mirror`, or `git push --tags` without auditing refs.

## GitHub Pages activation

A Pages workflow at `.github/workflows/pages.yml` builds a static bundle with no external frontend dependencies. The build stages examples and copies portable CSS/JS to public `assets/`, avoiding accidental exclusion of the hidden `.agents` path.

When the repo is public, open **Settings → Pages → Build and deployment → Source: GitHub Actions**. The next `main` push (or manual `workflow_dispatch` run) should build and deploy the demo. See [GitHub official custom workflows documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

Expected URL **only after successful deployment**:
`https://smallCattyCat.github.io/conversation-native-ui-for-codex/`

## Verification gates

- No third-party proprietary UI assets bundled; README/NOTICE contain clear credits.
- No private Nutstore paths, secrets, personal research data, or local Git machine emails in published history.
- Run offline Python tests and site build; test links and browser demos.
- Observe GitHub Actions actual results after push. Do not claim green Actions or a live URL based solely on YAML files.
- The Codex A/B performance benchmark is a written protocol only, not verified improvements.
