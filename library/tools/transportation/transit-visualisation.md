---
id: transit-visualisation
name: Transit Visualisation
description: Use when you have an approximate `geolocation` and want to see live public-transport vehicle positions and route networks there — returns real-time transit `geolocation` context near-globally.
url: https://mobility.portal.geops.io/?baselayers=geops.travic
category: transportation
path:
- transportation
bestFor: Watching live trains/buses/trams move on a map (Travic) to establish transit context around a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to view and embed (geOps branding must remain); custom/commercial data solutions are paid via geOps.
opsec: passive
opsecNote: You are viewing an aggregated third-party map; you never contact the subject or any operator directly. Entirely passive — no query targets a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: geOps Mobility Portal / TRAVIC — a reputable Swiss mobility-data company aggregating published GTFS timetables and real-time feeds; coverage and accuracy depend on each transit agency's data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- live-train-tracker
aliases:
- TRAVIC
- geOps Mobility Portal
tags:
- bellingcat-toolkit
- transport
- transit-map
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Transit Visualisation

> geOps' TRAVIC map: live positions of thousands of trains, buses and trams worldwide, drawn from published timetables and real-time feeds.

## When to use
You have an approximate `geolocation` — a city, a station, a photo you're geolocating — and want the transit context around it: what lines run there, where vehicles are right now, and whether a claimed journey (a train seen in a background, a "I'm on the 14:05") is plausible. Useful for corroborating movement or narrowing where a person could have travelled, not for tracking an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mobility.portal.geops.io/?baselayers=geops.travic.
2. Pan/zoom to your `geolocation` of interest.
3. Watch moving markers = live/scheduled vehicles; coloured borders mark real-time on-time status (on time, 3–5 min delay, 5+ min, cancelled). Static lines = the route network.
4. Cross-reference: match a line/route or a station name to a timetable to test whether a claimed trip or a photo's transit backdrop fits the location and time.

## Inputs → Outputs
- **In:** `geolocation` (map area)
- **Out:** live/scheduled vehicle positions, route network, real-time delay status (all `geolocation` context)
- **Empty/negative result looks like:** a bare map with no vehicles/lines — that agency publishes no data to Travic, so absence means *no coverage*, not "no service".

## Gotchas & OpSec
- Fully passive — a public map, nobody is queried about a person.
- Coverage is uneven: many networks show only scheduled (not GPS) positions, so a marker may be a timetable estimate, not a confirmed live vehicle.
- Data is "subject to terms of others" (the operators) and accuracy is not guaranteed — treat it as corroboration, not proof.

## Overlaps ("do both")
- Pairs with `[[live-train-tracker]]` — Travic gives near-global multimodal coverage; dedicated national trackers often give richer per-service detail where they exist.

## Trust & verifiability
`trust: community` — aggregated by geOps, a credible mobility-data firm, but the underlying feeds come from hundreds of agencies of varying quality; verify a specific claim against the operator's own timetable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transit-visualisation |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
