---
id: divide-missing-persons-across-the-team-so-each-investigator-owns-a-foothold
name: Divide missing persons across the team so each investigator owns a foothold
description: Use when At the start of a multi-MP, multi-investigator event to allocate effort.
type: technique
summary: In a team CTF, each member typically picks one missing person to investigate and drives that case's initial foothold independently. This parallelizes coverage across multiple MPs and gives each case a clear owner accountable for building and pivoting from its selector set, while still allowing the team to converge (e.g., over voice chat) when a case needs extra hands or local knowledge.
missingPersonsRelevance: medium
phase: intake
pivotFrom:
- name
pivotTo:
- social-profile
- username
steps:
- Enumerate the available missing persons.
- Assign one MP per investigator as primary owner.
- Each owner builds their MP's foothold independently.
- Keep an open team channel so investigators can pull others in when a case stalls or needs local/area knowledge.
signals:
- Each MP has a clear owner driving it
- The team can surge onto a single hard case (e.g., geolocation) without losing coverage of others
pitfalls:
- 'Siloing: owners failing to share cross-case selectors or call for help when stuck'
toolsUsed:
- voice chat / team collaboration
tags:
- team
- task-allocation
- intake
- collaboration
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: '''each team member typically chooses one missing person (MP) to investigate and attempts to gain an initial foothold.'''
trust: community
source: osinti4l-mvo-writeup
---

# Divide missing persons across the team so each investigator owns a foothold

> In a team CTF, each member typically picks one missing person to investigate and drives that case's initial foothold independently. This parallelizes coverage across multiple MPs and gives each case a clear owner accountable for building and pivoting from its selector set, while still allowing the team to converge (e.g., over voice chat) when a case needs extra hands or local knowledge.

**When to use:** At the start of a multi-MP, multi-investigator event to allocate effort.

## Steps
- Enumerate the available missing persons.
- Assign one MP per investigator as primary owner.
- Each owner builds their MP's foothold independently.
- Keep an open team channel so investigators can pull others in when a case stalls or needs local/area knowledge.

## Signals it's working
- Each MP has a clear owner driving it
- The team can surge onto a single hard case (e.g., geolocation) without losing coverage of others

## Pitfalls
- Siloing: owners failing to share cross-case selectors or call for help when stuck

**Tools:** voice chat / team collaboration

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._
