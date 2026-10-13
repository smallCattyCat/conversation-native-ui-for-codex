# Reusable interaction patterns

| User job | Preferred surface | Primary content | Safeguard |
| --- | --- | --- | --- |
| Understand one recommendation | Decision card | finding, evidence, boundary, actions | no action implied by display |
| Compare candidate paths | Comparison collection or table | common criteria, alternatives, tradeoffs | no misleading non-comparable metrics |
| Explore a technical result | Evidence workbench | inputs, assumptions, output, sources, revision | no fake computed claim |
| Collaboratively refine a claim | Revision/work item | original, proposed revision, discussion | preserve version and author |
| Act on an external system | Explicit authorization flow | impact, approver, scope, result | confirm != execute |

## Pattern A: Decision card

Minimum: meaningful title, bounded conclusion, evidence hint, applicability and action. For uncertain results, replace 'proceed' with 'review evidence' or 'collect input'.

## Pattern B: Comparative collection

Options must be homogeneous in the dimensions compared. Show unequal source quality. If one option is incomparable, consider a side-by-side table with explanatory labels instead of a carousel.

## Pattern C: Evidence workbench

A reusable structure:

    [Context + task]
    [Primary result]         [Evidence/source panel]
    [Input assumptions]      [Applicability/unknowns]
    [Revision & review state] [Human action]

On mobile stack vertically, preserving order and making the outcome and limitation visible without opening a hidden drawer.

## Pattern D: Provenance drawer

Use stable evidence IDs, dates, origin type, method, and limitations. Never style 'illustrative' samples like verified measurements.

## Pattern E: Authorization boundary

Review, confirm, dispatch, and report execution are distinct. An action button on a standalone demo may record local selection, but must not imitate physical actuation or external data writes.
