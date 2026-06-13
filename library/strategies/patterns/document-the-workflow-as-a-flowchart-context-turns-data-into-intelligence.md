---
id: document-the-workflow-as-a-flowchart-context-turns-data-into-intelligence
name: Document the workflow as a flowchart - context turns data into intelligence
description: Use when Throughout the investigation and especially before submitting/handing off findings.
type: pattern
summary: The team built a draw.io flowchart synthesizing every intelligence pathway, the geolocation comparisons, and the validation logic, and explicitly framed their guiding principle as 'information without context is not intelligence.' For Trace Labs scoring (and real case handoff), how you found and verified each datapoint is as important as the datapoint itself; a transparent, source-and-confirmation flowchart is what won the Most Valuable OSINT award. The transferable pattern is to capture provenance and verification chains as you go and present them visually, so each finding is auditable and th
missingPersonsRelevance: medium
phase: reporting
pivotFrom: []
pivotTo: []
steps:
- Record the source and verification method for each datapoint as you discover it.
- Lay out the pivot chain (selector -> finding -> confirmation) as a flowchart in draw.io or similar.
- Include side-by-side geolocation comparisons and the BOLO/face-match evidence in the documentation.
- Submit findings with the context and confirmation logic attached, not just raw data.
signals:
- Every claim in the report traces back to a source and a verification step
- Reviewers can follow the reasoning without asking how you got there
pitfalls:
- Submitting raw datapoints with no provenance or confirmation logic
- Leaving verification methods undocumented so findings can't be audited
toolsUsed:
- draw.io
tags:
- reporting
- documentation
- provenance
- flowchart
- tracelabs
evidence:
- type: writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: draw.io flowchart of pathways and validation logic; 'Information without context is not intelligence'; won Most Valuable OSINT award
trust: community
source: osinti4l-user
---

# Document the workflow as a flowchart - context turns data into intelligence

> The team built a draw.io flowchart synthesizing every intelligence pathway, the geolocation comparisons, and the validation logic, and explicitly framed their guiding principle as 'information without context is not intelligence.' For Trace Labs scoring (and real case handoff), how you found and verified each datapoint is as important as the datapoint itself; a transparent, source-and-confirmation flowchart is what won the Most Valuable OSINT award. The transferable pattern is to capture provenance and verification chains as you go and present them visually, so each finding is auditable and th

**When to use:** Throughout the investigation and especially before submitting/handing off findings.

## Steps
- Record the source and verification method for each datapoint as you discover it.
- Lay out the pivot chain (selector -> finding -> confirmation) as a flowchart in draw.io or similar.
- Include side-by-side geolocation comparisons and the BOLO/face-match evidence in the documentation.
- Submit findings with the context and confirmation logic attached, not just raw data.

## Signals it's working
- Every claim in the report traces back to a source and a verification step
- Reviewers can follow the reasoning without asking how you got there

## Pitfalls
- Submitting raw datapoints with no provenance or confirmation logic
- Leaving verification methods undocumented so findings can't be audited

**Tools:** draw.io

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
