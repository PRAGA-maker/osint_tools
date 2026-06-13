---
id: capture-full-page-screenshots-of-every-finding-for-the-le-handoff
name: Capture full-page screenshots of every finding for the LE handoff
description: Use when For every flag you submit, throughout the investigation.
type: technique
summary: 'Web pages and social posts change or get deleted between when you find them and when law enforcement reviews the report. Preserve every submission with a full-page screenshot so the evidence survives. Equally important: each submission must include the discovery method and why it matters, because ''information without context is not intelligence'' and judges/LE reject findings that lack explanation. Build a living flow chart of intel points (e.g. in draw.io) so connections are legible to a downstream reader.'
missingPersonsRelevance: high
phase: reporting
pivotFrom: []
pivotTo:
- document-id
steps:
- When you find a fact, take a full-page screenshot before the page can change.
- 'Write a short note: how you found it and why it is relevant to the case.'
- Add the intel point to a shared flow chart / link map.
- Submit with that context attached so a judge or detective can follow the chain.
signals:
- Submissions are accepted on first review
- A later-deleted post is still documented in your evidence
pitfalls:
- Submitting a bare link with no explanation (gets rejected)
- Relying on a live URL that may 404 by review time
- Treating raw data as intelligence without context
toolsUsed:
- Nimbus Screenshot & Screen Video Recorder
- draw.io
tags:
- evidence-preservation
- reporting
- documentation
- context
evidence:
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Nimbus full-page capture because a webpage can change before LE review; judges reject submissions lacking explanation
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: draw.io flow chart of intel points; 'information without context is not intelligence' won the MVO award
trust: community
source: searchparty-writeups
---

# Capture full-page screenshots of every finding for the LE handoff

> Web pages and social posts change or get deleted between when you find them and when law enforcement reviews the report. Preserve every submission with a full-page screenshot so the evidence survives. Equally important: each submission must include the discovery method and why it matters, because 'information without context is not intelligence' and judges/LE reject findings that lack explanation. Build a living flow chart of intel points (e.g. in draw.io) so connections are legible to a downstream reader.

**When to use:** For every flag you submit, throughout the investigation.

## Steps
- When you find a fact, take a full-page screenshot before the page can change.
- Write a short note: how you found it and why it is relevant to the case.
- Add the intel point to a shared flow chart / link map.
- Submit with that context attached so a judge or detective can follow the chain.

## Signals it's working
- Submissions are accepted on first review
- A later-deleted post is still documented in your evidence

## Pitfalls
- Submitting a bare link with no explanation (gets rejected)
- Relying on a live URL that may 404 by review time
- Treating raw data as intelligence without context

**Tools:** Nimbus Screenshot & Screen Video Recorder, draw.io

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
