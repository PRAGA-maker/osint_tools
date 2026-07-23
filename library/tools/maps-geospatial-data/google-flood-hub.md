---
id: google-flood-hub
name: Google Flood Hub
description: Use when you have a `geolocation`/`address` on a river and want current flood conditions and AI forecasts — returns river-level status and flood risk for that location.
url: https://sites.research.google/floods/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking AI-based river-flood forecasts and current flood conditions for a location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tool from Google Research; no account.
opsec: passive
opsecNote: Public environmental map — you look up a location, not a person; fully passive with no target signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Google Research using their published flood-forecasting models; the site itself flags outputs as approximate and informational, to be checked against official sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Flood Hub
- Google flood forecasting
tags:
- maps-geospatial-data
- flood
- environment
- forecasting
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Google Flood Hub

> Google Research's flood-forecasting map — current river conditions and AI-based flood predictions for locations worldwide.

## When to use
You have a `geolocation`/`address` near a river and need environmental context: is the river in flood, and what does the forecast say? Useful for corroborating or dating imagery/events tied to flooding, assessing conditions at a location under investigation, or situational awareness in disaster-response and humanitarian contexts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sites.research.google/floods/.
2. Navigate/search to the `geolocation` or `address` of interest along a monitored river.
3. Read the flood status and forecast for nearby gauges/reaches — conditions are labelled approximate.
4. Pivot: flood timing/extent helps date or verify on-the-ground imagery and cross-checks with satellite/weather sources for a location.

## Inputs → Outputs
- **In:** `geolocation` / `address` (near a monitored river)
- **Out:** current flood conditions and forecast for that `geolocation`
- **Empty/negative result looks like:** no coverage for the exact spot — many small/unmonitored rivers aren't modelled, so you'll get nothing there; use official/national flood services instead.

## Gotchas & OpSec
- Outputs are explicitly approximate and informational — not an authoritative emergency source; confirm with official agencies for real decisions.
- Coverage is limited to modelled rivers/regions; gaps are common outside major basins.
- It's environmental context, not a people/entity tool.

## Overlaps ("do both")
- Complements satellite/terrain tools (`[[peakvisor]]`, mapping) and weather archives — Flood Hub gives the flood signal; those confirm the physical scene and timing for verification.

## Trust & verifiability
`trust: trusted` — a Google Research product built on published models; reliable as context within its stated "approximate/informational" limits, so corroborate with official flood data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-flood-hub |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
