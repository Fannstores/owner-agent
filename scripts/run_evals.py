#!/usr/bin/env python3
"""Static eval contract checker; behavioral execution is host-agent dependent."""
from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
case=json.loads((root/'evals/cases/owner-agent.json').read_text())
errors=[]
if len(case['positive_triggers']) < 3: errors.append('need >=3 positive triggers')
if len(case['negative_triggers']) < 2: errors.append('need >=2 negative triggers')
if len(case['behavioral_evals']) < 4: errors.append('need >=4 behavioral evals')
required_words=['minimum','lazy','discover','sub-agent','critical','verify','recovery']
skill=(root/'skills/owner-agent/SKILL.md').read_text().lower()
for word in required_words:
    if word not in skill: errors.append(f'skill missing behavioral concept: {word}')
if errors:
    print('FAIL'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print(f"PASS: {len(case['positive_triggers'])} positive, {len(case['negative_triggers'])} negative, {len(case['behavioral_evals'])} behavioral eval contracts")
print('NOTE: live host-agent execution requires a host exposing the tested capabilities.')
