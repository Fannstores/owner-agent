# Capability Registry

Use a compact registry for discovery. The registry is metadata, not a copy of every skill.

Recommended fields:

```yaml
name: terminal
kind: tool
capabilities: [execute_commands, inspect_files]
triggers: [build, test, run, diagnose]
dependencies: []
risk: low
activation: on-demand
verification: command_exit_status
provider: host
compatible_hosts: [generic]
```

For skills, use `kind: skill` and point to the skill's location. Missing optional metadata must not prevent discovery; infer only what is supported by the host's exposed description.

Registry rules:

1. Keep entries small.
2. Refresh after installation/configuration changes.
3. Do not claim unavailable capabilities.
4. Mark unknown fields as unknown rather than guessing.
5. Prefer host-provided capability information over inference.
