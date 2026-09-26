#!/usr/bin/env python3
"""Dependency-free structural validator for Owner Agent."""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
skill=root/'skills/owner-agent/SKILL.md'
text=skill.read_text(encoding='utf-8')
if not text.startswith('---\n'): errors.append('missing frontmatter')
m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
if not m: errors.append('invalid frontmatter')
else:
    fm=m.group(1)
    if not re.search(r'^name:\s*owner-agent\s*$',fm,re.M): errors.append('name must be owner-agent')
    if not re.search(r'^description:\s*',fm,re.M): errors.append('missing description')
required=[
'# Owner Agent','## Operating contract','### 1. Bootstrap once','### 2. Route each task',
'### 3. Discover missing capabilities conditionally','### 4. Lazy-load skills','### 5. Arbitrate skills',
'### 6. Govern tools','### 7. Delegate narrowly','### 8. Apply trust and action gates','### 9. Self-configure safely',
'### 10. Recover and escalate','### 11. Optimize context and tokens','### 12. Verify before completion']
for h in required:
    if h not in text: errors.append(f'missing section: {h}')
if len(text.split())>5000: errors.append('SKILL.md exceeds 5000 words')
for p in [
'skills/owner-agent/references/capability-registry.md','skills/owner-agent/references/skill-arbitration.md',
'skills/owner-agent/references/trust-and-permissions.md','skills/owner-agent/references/recovery.md',
'skills/owner-agent/references/subagent-orchestration.md','skills/owner-agent/references/efficiency.md',
'skills/owner-agent/templates/skill-metadata.yaml','skills/owner-agent/templates/subagent-contract.yaml',
'schemas/capability-registry.schema.json','evals/cases/owner-agent.json','evals/fixtures/scenarios.md']:
    if not (root/p).exists(): errors.append(f'missing file: {p}')
for p in ['schemas/capability-registry.schema.json','evals/cases/owner-agent.json']:
    try: json.loads((root/p).read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'invalid JSON {p}: {e}')
if errors:
    print('FAIL'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('PASS: Owner Agent structural contract is valid')
