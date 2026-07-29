---
id: submarinecablemap-com
name: Submarinecablemap.com
description: Use when you have a `geolocation`/country/landing point and want to see the submarine communications cables serving it — returns geolocation (cable routes, landing points) context.
url: https://www.submarinecablemap.com/
category: transportation
path:
- transportation
bestFor: Interactive map of the world's submarine communications cables, their routes, landing points, and owners.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free interactive map from TeleGeography; no account required.
opsec: passive
opsecNote: Fully passive — a public reference map. Browsing reveals nothing about any person and touches only TeleGeography's site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by TeleGeography, the recognized authority on submarine cable infrastructure; data is well-sourced from industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- submarinecablemap.com
- TeleGeography Submarine Cable Map
tags:
- Maps, Geolocation and Transport
- Maritime
- infrastructure
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Submarinecablemap.com

> TeleGeography's authoritative interactive map of the undersea cables that carry the world's internet — routes, landing stations, owners, and ready-for-service dates.

## When to use
You have a `geolocation`, country, or coastal city and want to understand its international connectivity: which submarine cables land there, where they run, who owns them, and when they entered service. Useful for infrastructure/geopolitical analysis, explaining outages or connectivity in a region, or contextualizing why traffic to/from an area routes as it does. It's reference infrastructure data, not a people or live-traffic tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.submarinecablemap.com/.
2. Pan/zoom to your `geolocation`, or search a cable, country, or landing point.
3. Click a cable for its profile: route, length, owners, landing stations, and ready-for-service date. Click a landing point to list cables terminating there.
4. Read connectivity for the area (redundancy, chokepoints).
5. Pivot: a landing station's location → local infrastructure/geolocation context; cable owners → the operators/orgs behind a region's connectivity.

## Inputs → Outputs
- **In:** a `geolocation` / country / cable name / landing point
- **Out:** cable routes, landing stations, owners, and service dates (`geolocation` infrastructure context)
- **Empty/negative result looks like:** no cables shown for a landlocked or poorly-connected area — that area has no submarine landing (it relies on terrestrial links), not a data error.

## Gotchas & OpSec
- Covers submarine cables only — terrestrial fiber and satellite links aren't shown.
- Reflects announced/known cables; some routes are approximate and planned cables may shift.
- OpSec: fully passive public reference.

## Overlaps ("do both")
- Complements internet-outage and BGP tools (IODA, `[[team-cymru-ip-to-asn]]`) — the cable map explains the physical layer; routing/outage tools show the logical impact.

## Trust & verifiability
`trust: trusted` — TeleGeography is the authoritative source for submarine cable infrastructure; data is industry-sourced and well-maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | submarinecablemap-com |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
