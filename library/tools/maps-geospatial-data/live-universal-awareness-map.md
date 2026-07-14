---
id: live-universal-awareness-map
name: Live Universal Awareness Map
description: Use when you have a `geolocation` and rough time and want to know what reported events (conflict, unrest, incidents) were mapped there — returns geolocated event markers with source links.
url: https://usa.liveuamap.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Correlating a location and time window with reported real-world events (conflict, unrest, disasters) on an interactive map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse the map and event markers; some regions/features and ad-free/premium access require a paid subscription.
opsec: passive
opsecNote: You read a public events map — nothing about your subject is transmitted. Fully passive. Treat the crowd/media-sourced markers as reported claims, not verified fact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Aggregates news and social-media reports onto a map; individual markers are only as reliable as their cited source, and coverage/bias vary by conflict — always click through to the source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- acled
- bellingcat-timeline
aliases:
- Liveuamap
- Live UA Map
- liveuamap.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- event-mapping
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Live Universal Awareness Map

> A real-time, map-based feed of reported events — conflict, unrest, disasters — pinned to where and when they were reported, with a link back to each source.

## When to use
You have a `geolocation` and a rough time window and want situational context: what was reported happening there and then? For a missing-persons or investigative case that intersects with conflict zones, protests, disasters, or major incidents, Liveuamap helps place a subject's last-known location against the reported events around it, and each marker links to the underlying news/social source you can verify.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the relevant regional map (e.g. https://usa.liveuamap.com/, or the Ukraine/Syria/other regional subdomains).
2. Navigate/zoom to your area of interest.
3. Use the timeline/date controls to move to the relevant window.
4. Click event markers to read the summary and, crucially, **follow the source link** to the originating report.
5. Pivot: verified source posts feed geolocation/chronolocation work; the event context corroborates or challenges a subject's account of where they were.

## Inputs → Outputs
- **In:** `geolocation` (+ approximate time)
- **Out:** `geolocation` — mapped event markers (what/where/when) each with a cited source link
- **Empty/negative result looks like:** no markers in your area/time — either nothing was reported/mapped there, or the region has thin coverage. Absence of a marker is not evidence nothing happened.

## Gotchas & OpSec
- **Reported, not verified** — markers come from news and social media; some are wrong, delayed, or propaganda. Always click through and corroborate.
- Coverage and editorial bias differ sharply by conflict/region; don't assume completeness.
- OpSec: fully passive reading of a public map.

## Overlaps ("do both")
- Pairs with structured conflict datasets like [[acled]] (curated, coded event data for rigorous analysis) and open-source investigation timelines — Liveuamap gives fast situational awareness; ACLED gives verified, analyzable records. Use both for a defensible picture.

## Trust & verifiability
`trust: unverified` — a real-time aggregator whose markers are reported claims of varying reliability; the value is speed and the source links, so verify every marker you rely on against its cited source and a second one.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-universal-awareness-map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
