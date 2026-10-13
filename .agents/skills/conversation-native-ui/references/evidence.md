# Evidence and decision semantics

## Information identity

Each source must carry one of:
- observed: directly observed/measured in this context;
- computed: derived by a named method from identified inputs;
- reported: asserted by an external person or document;
- inferred: model or analyst conclusion dependent on other evidence;
- illustrative: fabricated solely to demonstrate the UI.

Use exact source IDs and descriptions. An observed or computed label is **not** proof of correctness: inputs, method, timestamp and verification must remain inspectable.

## Applicability

Express conditions under which a result may be used, and exclusions/unknowns. An uncertain or incomplete conclusion must support 'request additional evidence' or 'defer', not just 'approve'.

## States

Suggested lifecycle:
- proposed (the AI produced a suggestion);
- human-confirmed (an authorized person reviewed it);
- dispatched (an integration acknowledged the request);
- executed (the underlying external system reported success);
- failed (outcome did not succeed);
- superseded (replaced by later evidence/revision).

Use confirmation UI only when it corresponds to a real authorization control. Demo examples must explicitly state that confirmation is local-only and no external action occurred.

## Data

The starter repository includes an optional example at `schemas/decision-envelope.schema.json`. It is not a dependency of this portable skill. In another project, define the task's own contract and validate server outputs rather than trusting arbitrary LLM text as structured data.
