# Sub-agent Orchestration

Use sub-agents only when delegation has a material benefit.

Good reasons:

- independent parallel work
- specialized domain skill
- isolation of a risky/complex analysis
- host-native delegation that reduces context pressure

Avoid delegation for one-file edits, simple explanations, straightforward formatting, or tasks that can be verified directly.

Each sub-agent contract should contain:

```yaml
role: security-auditor
objective: inspect authentication changes
inputs: [specific files or evidence]
allowed_capabilities: [code_read, static_analysis]
constraints: [read_only]
output: findings with file/line evidence
verification: findings reference existing evidence
```
