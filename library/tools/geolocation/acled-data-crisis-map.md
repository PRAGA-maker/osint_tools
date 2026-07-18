---
id: acled-data-crisis-map
name: ACLED Data Crisis Map
description: Use when you have a `geolocation` and want dated political-violence, protest, and conflict events there — returns geolocated events with dates and actors.
url: https://acleddata.com/dashboard/#/dashboard
category: geolocation
path:
- geolocation
bestFor: Browsing an interactive map/dashboard of political violence, riots, and protests by country, date, and event type.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The public dashboard and curated data are free to browse; bulk data export/API and some datasets require free registration or an academic/nonprofit license.
opsec: passive
opsecNote: Passive — you browse a published conflict-events dashboard; nothing about your query is exposed to any subject. It reports events, not individuals, so there is no target to alert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ACLED (Armed Conflict Location & Event Data Project) is a widely-cited, methodologically documented nonprofit dataset used by researchers, journalists, and governments.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- acled-armed-conflict-location-and-event-data-project
- us-crisis-monitor
aliases:
- ACLED Dashboard
- ACLED crisis map
tags:
- Maps, Geolocation and Transport
- conflict
- crisis-mapping
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# ACLED Data Crisis Map

> The interactive dashboard over ACLED's conflict dataset — see political violence, riots, and protests plotted by place, date, and actor.

## When to use
You have a `geolocation` (a country, region, or area) and want to understand the security/conflict context there over a period — battles, violence against civilians, protests, riots, explosions — each event dated, geolocated, and attributed to actors. In a missing-persons or investigation context this is background/situational intelligence: characterizing whether a location was experiencing unrest, displacement, or violence around a relevant date, which can inform where and why a subject moved or disappeared.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ACLED dashboard at https://acleddata.com/dashboard/#/dashboard.
2. Filter by region/country, date range, and event type (violence, protests, etc.).
3. Read the map and time-series: each point is a recorded event with location, date, actors, and a description/source.
4. Drill into events near your area/date of interest; note the underlying source citations.
5. Pivot: an event's date/location contextualizes a subject's timeline; for systematic analysis, use ACLED's downloadable data/API (registration) rather than the dashboard.

## Inputs → Outputs
- **In:** `geolocation` (+ date/event-type filters)
- **Out:** geolocated conflict/protest events with dates, actors, and source notes (`geolocation` context layer)
- **Empty/negative result looks like:** no events in the filtered area/window — either genuinely no ACLED-recorded incidents, or the region/period is outside ACLED's coverage; absence is not proof nothing happened, only that ACLED logged nothing.

## Gotchas & OpSec
- ACLED records **events, not people** — it provides context, never an individual's location.
- Coverage and granularity vary by region and have expanded over time; older or remote areas may be sparse.
- Event geocoding is to a place, sometimes approximate; read the source notes before treating a point as precise.
- OpSec: fully passive; nothing reaches any subject.

## Overlaps ("do both")
- Pairs with `[[acled-armed-conflict-location-and-event-data-project]]` (the project's data/API for bulk analysis) and `[[us-crisis-monitor]]` (ACLED's US-focused view) — use the dashboard for quick visual context and the data exports for rigorous timeline work.

## Trust & verifiability
`trust: trusted` — ACLED is a reputable, transparently-sourced conflict dataset; individual events cite sources you can follow, though coding decisions and coverage gaps mean it should be read as curated data, not a complete record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | acled-data-crisis-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
