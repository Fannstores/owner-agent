# Owner Agent

**Owner Agent** is a portable orchestration skill designed to make agent-driven work easier for developers and other users. It manages the *selection and coordination* of skills, tools, capabilities, and bounded sub-agents instead of forcing the user to manually assemble them.

## What it solves

- one-time project trust instead of repetitive routine approvals
- capability discovery when a required tool is not currently exposed
- minimum-capability routing instead of loading every skill
- lazy loading to control context/token usage
- bounded sub-agent delegation
- safe self-configuration and recovery
- verification before claiming success
- explicit gates for destructive, security-sensitive, and irreversible actions

## Important boundary

Owner Agent cannot create host capabilities that do not exist, cannot bypass platform permissions, and cannot guarantee identical behavior across every agent host. Adapters translate real host mechanisms into the generic discovery contract.

## Layout

```text
skills/owner-agent/SKILL.md
skills/owner-agent/references/
schemas/
evals/
scripts/
adapters/generic/
examples/
```

## Validate

```bash
python3 scripts/validate_skill.py
python3 scripts/run_evals.py
```

The static eval suite verifies the contract. Live behavioral testing must be run in each target host because tool and permission APIs differ.

## Design principles

1. User intent first.
2. Minimum sufficient capability.
3. Progressive disclosure/lazy loading.
4. Conditional capability discovery.
5. Bounded autonomy with explicit critical-action gates.
6. Verification over claims.
7. Host permissions remain authoritative.

## Compatibility

The core follows the open Agent Skills-style model: a `SKILL.md` entry point plus supporting resources. Host-specific discovery and execution belong in thin adapters.
