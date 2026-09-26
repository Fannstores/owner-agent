# Recovery Protocol

Recovery is bounded and evidence-driven.

1. Capture the failure and affected operation.
2. Classify it as transient, known-safe/reversible, unknown, or critical.
3. For known-safe/reversible failures, choose the smallest corrective action.
4. Apply once.
5. Verify the exact failed condition.
6. Retry only when there is new evidence or a bounded transient retry is justified.
7. Roll back when a failed change is safely reversible.
8. Stop and escalate when risk, uncertainty, or repeated failure exceeds policy.

Never change unrelated architecture to make a failing task appear successful.
