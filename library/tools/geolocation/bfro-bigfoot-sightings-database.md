---
id: bfro-bigfoot-sightings-database
name: BFRO Bigfoot Sightings Database
description: Use when you have a `geolocation` (US state/county or Canadian province) and want dated eyewitness reports pinned to remote areas — returns location, date, and narrative of each report.
url: https://www.bfro.net/gdb/
category: geolocation
path:
- geolocation
bestFor: A free, geographically indexed archive of dated eyewitness reports tied to specific rural/wilderness locations across the US and Canada.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- dob
status: live
pricing: free
costNote: Free to browse and search; report submission is also free.
opsec: passive
opsecNote: Reading the public database queries BFRO's site only — no target is contacted or notified. Nothing sensitive is submitted when browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Maintained by an all-volunteer network; reports are unverified eyewitness accounts of an unproven phenomenon. Value here is the geo/time-indexed narrative data (who was where, when, and what they described), not any cryptozoological claim.
missingPersonsRelevance: medium
coverage:
- us
- ca
aliases:
- Bigfoot Field Researchers Organization Database
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
- sightings-database
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# BFRO Bigfoot Sightings Database

> A US/Canada database of dated eyewitness reports indexed by state and county — treated as OSINT, it's a searchable archive of "someone was in this remote place on this date and described what they saw."

## When to use
Set aside the sasquatch framing: what BFRO offers an investigator is a large, free, geographically organized set of dated field reports from rural and wilderness areas — exactly the low-traffic places that ordinary web/social sources under-cover. When your anchor is a `geolocation` (a specific county, trailhead, or forest) and a rough timeframe, these reports can incidentally document who was present, vehicles seen, trail/campsite conditions, weather, and access routes near a location and date of interest. Use it as a supplementary source of witness narratives for remote areas, not as a primary record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bfro.net/gdb/.
2. Click the target US state (or Canadian province); drill down to the county to narrow to your `geolocation`.
3. Open individual reports — each carries a location description, the date/season of the encounter, and a narrative account (sometimes with investigator follow-up notes).
4. Use the "Recent Additions" page to catch newly posted reports for a region.
5. Read the narratives for incidental detail: nearby roads/landmarks, other people or vehicles present, time of day, conditions.
6. Pivot: a precise location + date → cross-reference with maps, weather archives, and any local news or missing-persons timeline for the same place and window.

## Inputs → Outputs
- **In:** `geolocation` (US state/county, Canadian province)
- **Out:** report `geolocation` (place descriptions), encounter dates (`dob`-style date fields), free-text witness narratives
- **Empty/negative result looks like:** a county/region with no reports listed — simply means no eyewitness account was filed there; it carries no bearing on your subject.

## Gotchas & OpSec
- Reports are unverified, subjective eyewitness accounts of an unproven phenomenon — mine them only for the incidental factual detail (place, date, people/vehicles), never as authoritative fact.
- Coverage is uneven and skewed toward wilderness; urban areas are sparse.
- Fully passive and login-free — safe background reading with no target exposure.

## Overlaps ("do both")
- Complements mapping and weather-archive tools and local news search: BFRO supplies the location-anchored witness narrative, which you then corroborate against harder geospatial and temporal sources.

## Trust & verifiability
`trust: unverified` — a volunteer-run collection of anonymous eyewitness reports with no independent verification; treat every claim as a lead to confirm elsewhere, and use it only for the geo/time-tagged incidental details it captures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bfro-bigfoot-sightings-database |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, dob |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
