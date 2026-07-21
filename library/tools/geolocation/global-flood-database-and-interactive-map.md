---
id: global-flood-database-and-interactive-map
name: Global Flood Database (interactive map)
description: Use when you have a `geolocation` and a date and want to know whether that area flooded then — corroborates chronolocation and event timelines with satellite-derived flood extents.
url: http://global-flood-database.cloudtostreet.ai/
category: geolocation
path:
- geolocation
bestFor: Checking whether and when a specific area was flooded over the past ~two decades, with flood extent, dates, duration, and people affected.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free interactive map and openly published dataset (satellite-derived flood events); no account required.
opsec: passive
opsecNote: You query a published scientific dataset; nothing touches the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Peer-reviewed research dataset (Cloud to Street / Floodbase, published in Nature) derived from MODIS satellite imagery; authoritative for mapped events within its coverage window.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Global Flood Database
- cloudtostreet flood map
- Floodbase
tags:
- Maps, Geolocation and Transport
- Nature
- chronolocation
- disasters
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Global Flood Database (interactive map)

> A satellite-derived map of major flood events over roughly the last two decades — for OSINT, a **chronolocation** and event-timeline check: did this place flood, and when?

## When to use
You have a `geolocation` and a date/period and need to confirm or rule out a flood: verifying a "flood photo/video" is from the claimed place and time, understanding why a subject relocated or a location changed, or corroborating a disaster-linked timeline in a missing-persons case. The database maps flood extent, dates, duration in days, and the estimated number of people affected for each event, so you can tie a location to a documented flood window.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://global-flood-database.cloudtostreet.ai/.
2. Navigate/zoom the interactive map to the target `geolocation`.
3. Inspect mapped flood events there: extent (flooded area), start/end dates, duration, and people-affected estimates.
4. Compare the event dates against your photo/claim/timeline for consistency.
5. Pivot: pair with `[[earth]]` (weather at that time), satellite-imagery archives, and local-news search (`[[refdesk-newspaper-search]]`) to confirm the event and its human impact.

## Inputs → Outputs
- **In:** `geolocation` + date/period
- **Out:** whether/when the area flooded — extent, dates, duration, people-affected — i.e. a consistency check for a place-and-time claim
- **Empty/negative result looks like:** no mapped flood at that location/time — either it genuinely didn't flood, or the event fell outside the dataset's coverage/detection (cloud cover, small events); treat a null as "not recorded here," not proof of no flooding.

## Gotchas & OpSec
- **Coverage window & detection limits:** satellite-derived, so it captures major events within its time span; small or cloud-obscured floods may be missed.
- Dates are event windows, not minute-precise — good for corroborating a period, not an exact hour.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[earth]]` and satellite-imagery/news tools — flood extent + weather + imagery + local reporting together confirm an event's place, time, and impact.

## Trust & verifiability
`trust: trusted` — a peer-reviewed, openly published dataset from satellite imagery; authoritative for the events it maps, within its documented coverage and detection limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-flood-database-and-interactive-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (flood history) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
