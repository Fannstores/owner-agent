# Trust and Permissions

Owner Agent has a project-level trust policy, but the host remains authoritative.

## First-run prompt

Ask once when no trust state exists:

> Grant Owner Agent project-level trust for safe and reversible work? This reduces repeated prompts for routine operations. Critical, destructive, security-sensitive, and protected actions still follow explicit approval rules.

Options:

- `full_project_trust`
- `limited_trust`

## Action policy

| Class | Default behavior |
|---|---|
| SAFE | execute automatically when within trusted scope |
| SENSITIVE | follow explicit project policy; otherwise ask |
| CRITICAL | require explicit authorization unless an exact policy already grants it |

A generic "full access" setting must never be interpreted as permission to expose secrets, bypass security, destroy data, or cross a protected boundary.
