---
id: ethics-legal-does-not-equal-right
name: 'Ethics: legal does not equal right'
description: Use when Throughout, and especially before reporting or escalating any finding.
type: pattern
summary: 'TOFM''s ethical frame is that ''just because something is not illegal doesn''t make it right.'' Investigators bear moral responsibility for the impact of their work on the subject and on third parties. In missing-persons OSINT this directly shapes restraint: do not expose third-party bystanders, do not publish unvalidated identity claims, and weigh harm before acting on a finding.'
missingPersonsRelevance: medium
phase: reporting
pivotFrom: []
steps:
- Before acting on a finding, weigh its impact on the subject and on uninvolved third parties.
- Avoid collecting or exposing data on bystanders beyond what the mission requires.
- Do not report unvalidated identity claims that could harm an innocent person.
signals:
- Your report contains only validated, mission-relevant findings with minimized third-party exposure
pitfalls:
- Justifying harmful collection because it is technically legal
- Dragging uninvolved third parties into the report
tags:
- ethics
- harm-minimization
- reporting
- tracelabs
evidence:
- type: doc
  url: https://raw.githubusercontent.com/tracelabs/tofm/main/tofm.md
  note: 'TOFM ethics: ''Just because something is not illegal doesn''t make it right''; investigators bear moral responsibility for impacts.'
trust: community
source: tofm
---

# Ethics: legal does not equal right

> TOFM's ethical frame is that 'just because something is not illegal doesn't make it right.' Investigators bear moral responsibility for the impact of their work on the subject and on third parties. In missing-persons OSINT this directly shapes restraint: do not expose third-party bystanders, do not publish unvalidated identity claims, and weigh harm before acting on a finding.

**When to use:** Throughout, and especially before reporting or escalating any finding.

## Steps
- Before acting on a finding, weigh its impact on the subject and on uninvolved third parties.
- Avoid collecting or exposing data on bystanders beyond what the mission requires.
- Do not report unvalidated identity claims that could harm an innocent person.

## Signals it's working
- Your report contains only validated, mission-relevant findings with minimized third-party exposure

## Pitfalls
- Justifying harmful collection because it is technically legal
- Dragging uninvolved third parties into the report

_Harvested from `tofm` — methodology only, no case PII. Promote/curate as needed._
