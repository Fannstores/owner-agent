# Skill Arbitration

Arbitrate by constraints, not by a universal score that hides reasoning.

Selection order:

1. Capability coverage: can it perform the required operation?
2. Task relevance: does its trigger/domain match the actual intent?
3. Dependency cost: what additional skills/tools/context does it require?
4. Environment compatibility: is it usable on this host/project?
5. Risk: does it introduce unnecessary side effects or access?
6. Verification: can its result be checked?
7. Conflict: does it duplicate or contradict another selected skill?

Output one of:

- `REQUIRED`: needed for correctness.
- `OPTIONAL`: useful if evidence shows a need.
- `UNNECESSARY`: not needed for the current task.
- `CONFLICTING`: incompatible, redundant, or unsafe in the current plan.

If multiple candidates remain equivalent, choose the one with lower dependency/context cost and explain only the user-relevant outcome, not hidden reasoning.
