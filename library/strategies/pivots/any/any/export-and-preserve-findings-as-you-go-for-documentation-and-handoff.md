---
id: export-and-preserve-findings-as-you-go-for-documentation-and-handoff
name: Export and preserve findings as you go for documentation and handoff
description: Use when On every tool run that returns results that might later be deleted, edited, or set private.
type: technique
summary: cupidcr4wl's --export-results writes hits to a self-contained HTML report (cc_results.html), reflecting a discipline of preserving evidence at the moment of discovery rather than reconstructing it later. In missing-persons work, profiles and posts can be deleted or go private quickly, so capturing results into a durable, shareable artifact protects the chain of custody and supports the final report or law-enforcement handoff. The transferable technique is to default to export/capture for every tool run so no live finding is lost to later takedown.
missingPersonsRelevance: medium
phase: reporting
pivotFrom: []
pivotTo: []
steps:
- Enable result export (e.g., cupidcr4wl --export-results) on each run.
- Save the generated artifact (HTML report, screenshots) with a timestamp.
- Note the live URL and capture method alongside the export for provenance.
- Aggregate exports into the case file for the final report and any handoff.
signals:
- You have a durable artifact for each finding even after the source goes offline
pitfalls:
- Relying on memory or live links that may vanish
- Capturing the result but not the source URL/timestamp needed for provenance
toolsUsed:
- cupidcr4wl
tags:
- evidence-preservation
- export
- chain-of-custody
- reporting
evidence:
- type: tool
  url: https://github.com/OSINTI4L/cupidcr4wl
  note: --export-results writes hits to cc_results.html for documentation
trust: community
source: osinti4l-user
---

# Export and preserve findings as you go for documentation and handoff

> cupidcr4wl's --export-results writes hits to a self-contained HTML report (cc_results.html), reflecting a discipline of preserving evidence at the moment of discovery rather than reconstructing it later. In missing-persons work, profiles and posts can be deleted or go private quickly, so capturing results into a durable, shareable artifact protects the chain of custody and supports the final report or law-enforcement handoff. The transferable technique is to default to export/capture for every tool run so no live finding is lost to later takedown.

**When to use:** On every tool run that returns results that might later be deleted, edited, or set private.

## Steps
- Enable result export (e.g., cupidcr4wl --export-results) on each run.
- Save the generated artifact (HTML report, screenshots) with a timestamp.
- Note the live URL and capture method alongside the export for provenance.
- Aggregate exports into the case file for the final report and any handoff.

## Signals it's working
- You have a durable artifact for each finding even after the source goes offline

## Pitfalls
- Relying on memory or live links that may vanish
- Capturing the result but not the source URL/timestamp needed for provenance

**Tools:** cupidcr4wl

_Harvested from `osinti4l-user` — methodology only, no case PII. Promote/curate as needed._
