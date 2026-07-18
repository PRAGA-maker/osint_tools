---
id: toronto-live
name: Toronto Live
description: Use when you need live Toronto situational data (traffic collisions, incidents, cameras) around a `geolocation` in the city — returns `geolocation`.
url: https://apps.esri.ca/torontolive/
category: geolocation
path:
- geolocation
bestFor: Viewing live Toronto incident/traffic map layers to add situational context to a location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public Esri Canada demo map; no account required.
opsec: passive
opsecNote: You are viewing a public live map; nothing is sent to any subject and no personal query is made. Purely geographic/situational context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Esri Canada using City of Toronto / open live-data feeds; a demonstration app, reliable as a data viewer but not an investigative database.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Esri Toronto Live
tags:
- live-map
- toronto
- situational-awareness
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Toronto Live

> An Esri Canada live map of Toronto — traffic collisions, incidents, and other city feeds layered on a map for situational context around a location.

## When to use
You're building geographic context for a location in Toronto and want live/near-live city data: current traffic collisions, road incidents, and other municipal feeds. It's a situational-awareness map, not a person-finder — reach for it to understand conditions or events near a `geolocation`/`address` (e.g. corroborating "there was a collision on that street that afternoon"), not to look anyone up. Low missing-persons relevance; a supporting, city-specific context layer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://apps.esri.ca/torontolive/.
2. Pan/zoom to the Toronto `address`/area of interest.
3. Toggle the layers (e.g. Collision/incident layers) via the map's carousel/legend.
4. Click a feature (a collision/incident marker) to read its details and timestamp.
5. Read the output: incidents and conditions at a place and time (`geolocation` context). Pivot: pair with mapping/streetview tools for the same coordinates and with news feeds for the same incident.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a Toronto location — no personal query)
- **Out:** `geolocation` context: mapped live incidents/conditions with timestamps
- **Empty/negative result looks like:** no markers in the area/time — no reported incidents there (or the layer isn't currently feeding), not proof nothing happened; cross-check the city's open-data portal.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive; no subject query.
- It's a demo app on live feeds — coverage/layers can change or lapse; verify a critical data point against the City of Toronto open-data source.

## Overlaps ("do both")
- Pairs with satellite/streetview tools and local news feeds — this shows live incident context, while those give ground imagery and reporting for the same location. Do both to corroborate an event at a place and time.

## Trust & verifiability
`trust: trusted` — published by Esri Canada on City of Toronto open data; reliable as a viewer, but confirm specific incidents against the underlying municipal open-data source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toronto-live |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
