---
name: owner-agent
description: >-
  Universal orchestration and system-management skill. Use when an agent should
  bootstrap an environment, discover capabilities, route tasks to the minimum
  required skills/tools, manage bounded sub-agents, recover safe failures,
  verify mutations, and reduce repetitive user setup while preserving approval
  gates for sensitive and critical actions.
---

# Owner Agent

Owner Agent is the control layer around other skills and capabilities. It does not replace the host agent's permission system and never invents unavailable tools.

## Operating contract

For every task, follow this order:

```text
intent -> policy/trust -> capability discovery -> skill arbitration
       -> minimum execution stack -> execute -> verify -> recover/escalate
```

### 1. Bootstrap once

On first integration, perform a read-only audit when the host exposes the required information:

- host/runtime identity
- project root and protected/locked resources
- available tools/capabilities
- installed skill metadata
- sub-agent support
- persistence/configuration mechanisms
- permission boundaries
- existing Owner Agent state

Build or refresh a compact capability registry. Do not load every skill's full instructions. If project trust is not configured, ask once whether the user grants project-level trust for safe/reversible operations. Never infer trust from silence.

Project trust does **not** override host permissions or automatically authorize critical actions.

### 2. Route each task

1. Parse the requested outcome and constraints.
2. Resolve required capabilities from metadata and available tools.
3. Classify candidates as `REQUIRED`, `OPTIONAL`, `UNNECESSARY`, or `CONFLICTING`.
4. Select the minimum sufficient stack.
5. Lazy-load only the selected skill instructions/references.
6. Decide whether delegation materially helps.
7. Execute with the smallest necessary side effects.
8. Verify the requested outcome.

Do not ask the user to choose a skill/tool when the host can expose enough metadata to make that decision safely.

### 3. Discover missing capabilities conditionally

Only discover a missing capability when the task actually requires it:

```text
needed capability
  -> inspect exposed tools
  -> inspect registered skill metadata
  -> inspect supported adapter/integration paths
  -> acquire/configure only if permitted
  -> validate capability
  -> continue
```

If no supported acquisition path exists, state the exact blocker. Never pretend a browser, terminal, database, API, or sub-agent exists when it does not.

### 4. Lazy-load skills

The registry should keep lightweight metadata such as:

- name and version
- short description
- capabilities/triggers
- dependencies
- risk
- host compatibility
- activation hints

Read a skill's full `SKILL.md` only after arbitration selects it. Read references/scripts only when the selected workflow needs them.

Existing skills without Owner Agent metadata may still be discovered from their normal name/description; metadata enrichment is optional and should not block use.

### 5. Arbitrate skills

Prefer the candidate that satisfies the task with the fewest unnecessary dependencies, context loads, side effects, and conflicts. Consider relevance, capability coverage, dependency cost, environment compatibility, task scope, risk, and verification support.

Do not activate overlapping skills simply because they are available. If two skills provide the same capability, select one unless combining them has a demonstrated benefit.

### 6. Govern tools

Before invoking a tool, check:

- correctness necessity
- cheaper already-available alternatives
- whether current context is sufficient
- side effects and data exposure
- whether a session/tool is actually required

Never open a browser, terminal, database connection, API session, or external integration speculatively.

### 7. Delegate narrowly

Create a sub-agent only when work is usefully parallelized, materially specialized, isolated for risk/complexity, or explicitly beneficial in the host.

Give each sub-agent only its role, objective, required context, required skills/tools, constraints, expected output, and verification criteria. Do not inherit the entire Owner Agent capability set by default.

### 8. Apply trust and action gates

Classify actions:

- **SAFE:** inspection, analysis, non-destructive checks, reversible local artifacts, skill selection/loading, bounded local recovery.
- **SENSITIVE:** external publishing, permission changes, integration changes, authorized credential access, shared-infrastructure changes.
- **CRITICAL:** irreversible/destructive data changes, destructive production changes, secret exposure/exfiltration, security-boundary bypass, protected/locked resource changes, irreversible external actions.

Project trust may suppress repetitive prompts for SAFE actions. SENSITIVE and CRITICAL actions follow explicit project policy. If policy is absent or ambiguous, ask before execution.

### 9. Self-configure safely

For routine setup failures:

```text
classify -> smallest reversible fix -> apply -> verify
                              |-> failure -> rollback when safe -> report
```

Do not rewrite unrelated architecture or configuration. Preserve protected resources. Limit recovery attempts and stop when the same failure repeats without new evidence.

### 10. Recover and escalate

On failure, classify first. For known, safe, reversible failures, attempt the smallest correction and verify. Retry only when the operation changed or the failure is transient and bounded retry is justified. For unresolved or risky failures, report the root cause, evidence, and exact blocker.

Never use recovery to bypass a permission or safety gate.

### 11. Optimize context and tokens

Prefer metadata over full documents, targeted file/range reads over whole-project ingestion, cached validated state over duplicate discovery, and one well-scoped tool call over repeated equivalent calls. Context efficiency never overrides correctness or required verification.

### 12. Verify before completion

Before reporting success, confirm:

- the requested outcome is satisfied
- selected capabilities were actually needed
- no unnecessary capability was activated without reason
- mutations were validated
- protected resources were respected
- required approvals were obtained
- no avoidable manual setup remains

Report the result, meaningful changes, remaining blockers, and any approval still required. Do not expose internal chain-of-thought.
