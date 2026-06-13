---
id: use-osint-frameworks-and-flowcharts-to-know-your-next-pivot
name: Use OSINT frameworks and flowcharts to know your next pivot
description: Use when When you hold a selector and are unsure which pivot or tool applies next.
type: technique
summary: When you have a data point and are unsure what to do with it next, structured pivot maps tell you the available next moves. Beginners and experienced analysts alike use the OSINT Framework site and Michael Bazzell's OSINT flowcharts to see, for a given selector (email, username, phone, image), which tools and pivots apply. This prevents tunnel vision and surfaces pivot paths you would not have remembered under time pressure.
missingPersonsRelevance: medium
phase: pivot
pivotFrom: []
pivotTo: []
steps:
- Identify the selector you currently hold (email, username, phone, image, name).
- Open the OSINT Framework or a Bazzell flowchart for that selector type.
- Pick the next pivot/tool indicated and execute it.
- Repeat as each pivot yields a new selector.
signals:
- The framework reveals a pivot path you had not considered
- A flowchart turns a dead-end selector into a new lead
pitfalls:
- Tunnel vision on one pivot and missing obvious alternatives
- Treating the framework as exhaustive rather than a prompt
toolsUsed:
- OSINT Framework (osintframework.com)
- Michael Bazzell OSINT flowcharts
tags:
- frameworks
- pivot-map
- methodology
evidence:
- type: writeup
  url: https://wondersmithrae.medium.com/finding-missing-people-with-tracelabs-ctf-d5617c7cd659
  note: OSINT Framework illustrates how to pivot from gathered info; Bazzell flowcharts give systematic pathways
trust: community
source: searchparty-writeups
---

# Use OSINT frameworks and flowcharts to know your next pivot

> When you have a data point and are unsure what to do with it next, structured pivot maps tell you the available next moves. Beginners and experienced analysts alike use the OSINT Framework site and Michael Bazzell's OSINT flowcharts to see, for a given selector (email, username, phone, image), which tools and pivots apply. This prevents tunnel vision and surfaces pivot paths you would not have remembered under time pressure.

**When to use:** When you hold a selector and are unsure which pivot or tool applies next.

## Steps
- Identify the selector you currently hold (email, username, phone, image, name).
- Open the OSINT Framework or a Bazzell flowchart for that selector type.
- Pick the next pivot/tool indicated and execute it.
- Repeat as each pivot yields a new selector.

## Signals it's working
- The framework reveals a pivot path you had not considered
- A flowchart turns a dead-end selector into a new lead

## Pitfalls
- Tunnel vision on one pivot and missing obvious alternatives
- Treating the framework as exhaustive rather than a prompt

**Tools:** OSINT Framework (osintframework.com), Michael Bazzell OSINT flowcharts

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
