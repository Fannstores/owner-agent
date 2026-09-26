# Generic Adapter Contract

The core skill is host-agnostic. An adapter maps a host's actual mechanisms into these abstract discovery operations:

- `discover_host`
- `discover_tools`
- `discover_skill_metadata`
- `discover_subagents`
- `discover_permissions`
- `discover_project_root`
- `read_project_state`
- `write_project_state` (only when permitted)

An adapter must report unsupported operations as unavailable. It must never fabricate a capability. Host-specific permissions remain authoritative.
