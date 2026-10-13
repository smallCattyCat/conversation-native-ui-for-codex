# Evaluation rubric

Score each dimension from **0** (absent/broken), **1** (materially deficient), **2** (adequate), **3** (strong), **4** (excellent). Include concrete examples and screenshot/file evidence. Don't average away critical failures.

| Dimension | What to inspect |
| --- | --- |
| Task fit | Does the page support the specified user action without unrelated dashboard filler? |
| Information hierarchy | Is the primary content readable at first glance, with judicious progressive disclosure? |
| Visual coherence | Do typography, token usage, rhythm, border/icon style and theme remain consistent? |
| Interaction correctness | Are visible controls functional, with predictable states, no lost drafts and truthful status? |
| Accessibility | Keyboard, labels, focus, touch targets, contrast, reduced motion |
| Responsive behavior | Desktop, tablet, 390px and 320px, no page overflow or hidden mandatory action |
| Reusability | Reusable primitives, scoped design variables, minimal coupling to task/domain |
| Evidence/safety fit | When source-sensitive/external action is involved, does it preserve provenance and authorization boundary? |
| Code quality | Clear structure, tests, no unlicensed assets, no fake API/data results |

**Critical fails** (flag separately): loss of user edits; external action without confirmation; mislabeled fake data; text inaccessible on mobile; leaked secrets. Report them even if average score is high.

Write down exact reviewed build and tool versions and the test command, not merely subjective aesthetic preferences.
