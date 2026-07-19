---
id: pedestriansfirst
name: PedestriansFirst
description: Use when you have a `geolocation`/city and want walkability and urban-mobility metrics for it — returns per-city pedestrian-infrastructure data useful as environmental context.
url: https://pedestriansfirst.itdp.org/
category: geolocation
path:
- geolocation
bestFor: Pulling ITDP walkability/urban-mobility indicators for a city — contextual data about a place's pedestrian infrastructure, not a people lookup.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tool from ITDP (Institute for Transportation and Development Policy); no account required.
opsec: passive
opsecNote: Reading published urban-mobility data is fully passive — no target interaction. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by ITDP, a reputable non-profit transport-policy institute; the walkability metrics are derived from open geospatial data and are methodologically documented.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Pedestrians First
- ITDP PedestriansFirst
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- walkability
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# PedestriansFirst

> ITDP's tool for measuring the walkability and pedestrian-friendliness of cities worldwide — a source of environmental/urban context about a place, rather than anything about a specific person.

## When to use
You are building context around a `geolocation` — understanding the built environment of a city or district relevant to a case. PedestriansFirst provides indicators like block density, access to services, car-free space, and transit proximity, which can help characterise an area (walkable dense core vs car-dependent sprawl) when reasoning about how someone moves through or lives in a place. It's supporting context, not an identifier lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pedestriansfirst.itdp.org/ and locate the city/area of interest on the map or via search.
2. Read the walkability and urban-mobility metrics for that city (and sub-areas where available).
3. Interpret the indicators as environmental context — e.g. a highly walkable district implies different movement patterns than a car-dependent one.
4. Combine with mapping/street-view tools for the concrete geography.
5. Pivot: the environmental picture informs `geolocation` hypotheses (likely transport modes, catchment areas) rather than producing new selectors directly.

## Inputs → Outputs
- **In:** `geolocation` (city/area)
- **Out:** walkability/urban-mobility indicators contextualising that `geolocation`
- **Empty/negative result looks like:** the city isn't covered (coverage is broad but not every town is included), or metrics are too coarse for your sub-city question — fall back to direct map analysis.

## Gotchas & OpSec
- This is aggregate city-level data — it says nothing about individuals and won't geolocate a photo.
- Coverage and granularity vary by city; smaller places may be absent or coarse.
- OpSec: fully passive public data.

## Overlaps ("do both")
- Pairs with mapping/street-view and census/demographic tools — those give the concrete geography and population, while PedestriansFirst adds a walkability/mobility lens.

## Trust & verifiability
`trust: trusted` — a documented, methodology-transparent tool from a respected transport-policy non-profit; metrics are reliable as *contextual* indicators, not as case-specific evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pedestriansfirst |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
