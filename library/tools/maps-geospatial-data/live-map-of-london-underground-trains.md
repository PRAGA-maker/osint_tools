---
id: live-map-of-london-underground-trains
name: Live map of London Underground trains
description: Use when you need near-real-time positions of London Underground trains to reason about a `geolocation` or timing on the Tube network — returns `geolocation`.
url: https://traintimes.org.uk/map/tube/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Watching live approximate Tube train positions and line status across the London Underground.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public visualisation built on Transport for London's open data; no account required.
opsec: passive
opsecNote: You are just viewing a public live map; nothing is sent to any subject and no query about a person is made. Purely situational/geographic context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Matthew Somerville on official TfL open data; a well-known, reliable public visualisation, though positions are interpolated from timetables/feeds, not GPS.
missingPersonsRelevance: low
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- traintimes tube map
- London Underground live map
tags:
- transit
- live-map
- london
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Live map of London Underground trains

> A live map of where London Underground trains are right now, from TfL open data — situational context for timing, network status, and where a Tube journey plausibly is.

## When to use
You're reasoning about movement on the London Underground: whether a line is running, roughly where trains are, or how long a Tube journey between two points would take at a given moment. It's a geographic/temporal context tool, not a person-finder — reach for it to sanity-check a Tube-related timeline or to understand the network around a location (`geolocation`), not to look anyone up. Low missing-persons relevance; occasionally useful for corroborating "could they have travelled X→Y by Tube in that window."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://traintimes.org.uk/map/tube/.
2. Watch the animated dots — each represents a train, positioned from TfL's live/timetable feed.
3. Hover/click a train for its line, direction, and next stops; check whether lines show as running or suspended.
4. Read the output: current network activity and approximate train positions (`geolocation` context), and effective travel timing between stations.
5. Pivot: combine with a station's real-world coordinates (via a geocoder) and journey-planner data to bound a movement window.

## Inputs → Outputs
- **In:** `geolocation` (a part of the Tube network you care about — no personal query)
- **Out:** `geolocation` context: live approximate train positions, line status, and journey timing
- **Empty/negative result looks like:** sparse/no dots on a line means service disruption or off-hours, not a data error — cross-check TfL status.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive; it involves no subject query whatsoever.
- Positions are interpolated from feeds/timetables, not live GPS, so treat them as approximate — good for "is this plausible," not precise tracking.

## Overlaps ("do both")
- Pairs with a geocoder and TfL journey-planner data — this shows live network state, while those give exact station coordinates and door-to-door timing. Do both to bound a Tube travel window.

## Trust & verifiability
`trust: trusted` — a well-known public visualisation on official TfL open data; reliable for network state, with the caveat that positions are interpolated rather than GPS-exact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-map-of-london-underground-trains |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
