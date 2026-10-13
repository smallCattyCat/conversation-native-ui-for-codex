# Codex Skill A/B benchmark (reproducible protocol, **not yet run**)

This directory provides three neutral task briefs, identical across control and treatment conditions, and a scoring rubric. It contains **no generated outputs or fabricated performance claims**.

## Why

R1 had basic CSS and a Skill, but no evidence that Codex with the Skill produces better designs. R2 establishes the same tasks, quality dimensions and record-keeping for an honest evaluation.

## Conditions

- A / baseline: same Codex model, reasoning level, tools and target project, **without** this Skill.
- B / treatment: identical conditions, copy the Skill to `.agents/skills/conversation-native-ui/` and explicitly invoke `$conversation-native-ui` alongside the same brief.
- Fresh checkout/workspace for each run; record model/version, date, prompts, available tools, decisions and generated artifacts.
- Conduct at least **two independently started runs per task and condition** (3 tasks × 2 conditions × 2 repeats = 12 outputs). More is better.
- Keep the base task text byte-for-byte identical. Add only the Skill invocation in treatment, note this intervention.
- Blind reviewers to condition when scoring; randomized ordering is recommended. Take identical desktop/mobile screenshots.

## Measure

Use `rubric.md`; evaluate job fit, information hierarchy, design fidelity, interaction semantics, accessibility/responsiveness, reusability, evidence/authorization accuracy (where applicable), and code quality. Record 0–4 per dimension, plus major defects, time and token usage if observable.

There is no asserted winning condition until scores and artifacts exist. Use `results-template.csv` to record runs and provide screenshots and Git SHAs separately.

## Running in Codex

Take each task from `tasks/`, then ask:

> Implement the attached brief as a working interactive page. Run the supplied tests and inspect the browser at desktop and 390px. Include a short audit and file list. Follow any project instructions, and do not claim model/API integration unless real.

For treatment append:

> Use $conversation-native-ui and the source-mapped Claude-inspired visual profile. Apply task-relevant interaction patterns and their tests.

This produces a falsifiable usability and repeatability comparison, not an unverifiable "looks nicer" assertion.
