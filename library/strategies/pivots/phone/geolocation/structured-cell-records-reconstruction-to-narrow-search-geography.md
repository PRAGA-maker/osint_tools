---
id: structured-cell-records-reconstruction-to-narrow-search-geography
name: Structured cell-records reconstruction to narrow search geography
description: Use when When you have call/text logs, EXIF, or any raw activity dataset and need to convert it into a search area.
type: technique
summary: 'In the Brandon Lawson case a volunteer transcribed jumbled cellular records into structured spreadsheets with tabs for process notes, calls, texts, and raw data, attaching tower location coordinates to each event. This converted unusable raw documents into a geo-temporal map that let searchers narrow the physical search area to tower-ping locations. The transferable method: whenever you obtain call/location logs or any noisy raw dataset, normalize it into a structured, geocoded timeline so the last-ping cluster becomes a defined search box.'
missingPersonsRelevance: medium
phase: enrichment
pivotFrom:
- phone
- metadata-exif
- geolocation
pivotTo:
- geolocation
- address
steps:
- Transcribe raw, jumbled records into a normalized table (one row per event).
- Separate tabs/views for process notes, calls, texts, and raw source data for auditability.
- Attach tower/location coordinates to each event to geocode the timeline.
- Cluster the final-hours pings to define a bounded physical search area.
signals:
- A cluster of final pings collapses a wide area into a defined box
- Timeline gaps reveal where the subject went dark
pitfalls:
- Working from raw jumbled records without normalizing, producing errors
- Losing chain-of-custody by not separating raw data from interpretation
toolsUsed:
- spreadsheet (Excel)
tags:
- geolocation
- data-normalization
- timeline
- tower-ping
evidence:
- type: case-study
  url: https://uncovered.com/the-power-of-collective-impact-brandon-lawson-case-study/
  note: Volunteer built an Excel report with tabs for process notes, calls, texts and raw data plus tower coordinates to narrow the search area; evidence recovered ~9 years later.
trust: community
source: uncovered-missing
---

# Structured cell-records reconstruction to narrow search geography

> In the Brandon Lawson case a volunteer transcribed jumbled cellular records into structured spreadsheets with tabs for process notes, calls, texts, and raw data, attaching tower location coordinates to each event. This converted unusable raw documents into a geo-temporal map that let searchers narrow the physical search area to tower-ping locations. The transferable method: whenever you obtain call/location logs or any noisy raw dataset, normalize it into a structured, geocoded timeline so the last-ping cluster becomes a defined search box.

**When to use:** When you have call/text logs, EXIF, or any raw activity dataset and need to convert it into a search area.

## Steps
- Transcribe raw, jumbled records into a normalized table (one row per event).
- Separate tabs/views for process notes, calls, texts, and raw source data for auditability.
- Attach tower/location coordinates to each event to geocode the timeline.
- Cluster the final-hours pings to define a bounded physical search area.

## Signals it's working
- A cluster of final pings collapses a wide area into a defined box
- Timeline gaps reveal where the subject went dark

## Pitfalls
- Working from raw jumbled records without normalizing, producing errors
- Losing chain-of-custody by not separating raw data from interpretation

**Tools:** spreadsheet (Excel)

_Harvested from `uncovered-missing` — methodology only, no case PII. Promote/curate as needed._
