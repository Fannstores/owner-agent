
## Unreleased

### Fixed
- Added a hard interaction gate: when a blocking question is asked, Owner Agent pauses all execution until the user answers.
- Changed blocking clarification to one question per turn so users can make one decision at a time without the agent continuing or stacking questions.
- Added explicit direct-install intent handling so identifiable skill installation is executed instead of converted into an option questionnaire.
- Added sequential blocker re-evaluation after every user answer so previously answered decisions are not repeated.
# Changelog

## 0.1.2

- Hardened the interaction gate into a one-question-at-a-time synchronization protocol.
- Added sequential blocker re-evaluation after every user answer.
- Added explicit prohibition against stacked blocking questions and execution while waiting.
- Added install-intent behavior that bypasses unnecessary option questionnaires.

## 0.1.1

- Added the initial blocking-question pause and direct-install intent rules.

## 0.1.0

- Added universal bootstrap and capability discovery contract.
- Added lazy skill loading and skill arbitration.
- Added trust/permission gates and bounded recovery.
- Added sub-agent scoping and efficiency rules.
- Added structural and behavioral eval contracts.
- Added generic adapter contract and capability registry schema.
