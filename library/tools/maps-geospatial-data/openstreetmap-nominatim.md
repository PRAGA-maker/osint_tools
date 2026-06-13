---
id: openstreetmap-nominatim
name: OpenStreetMap Nominatim
description: Free geocoding service from OpenStreetMap that converts a street address into latitude/longitude coordinates and structured location data.
url: https://nominatim.openstreetmap.org
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Geocoding an address obtained during an investigation into precise coordinates for mapping, distance, and area analysis.
selectorsIn:
- address
selectorsOut:
- geolocation
- address
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Official OpenStreetMap geocoder; free and open. Public endpoint has a strict usage policy (max ~1 req/sec, no heavy bulk use).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Nominatim
- OSM geocoding
- osm
tags:
- geocoding
- address-to-coordinates
- openstreetmap
- maps
- api
source: xsint
lastVerified: ''
enrichment: full
---

# OpenStreetMap Nominatim

> Free geocoding service from OpenStreetMap that converts a street address into latitude/longitude coordinates and structured location data.

- **URL:** https://nominatim.openstreetmap.org
- **Best for:** Geocoding an address obtained during an investigation into precise coordinates for mapping, distance, and area analysis.
- **Source:** harvested from `xsint`

Integrated by xsint as the osm module to geocode an input address into coordinates. Respect the Nominatim usage policy (rate-limit, set a User-Agent) or self-host. Useful for placing a last-known address on a map and computing search radii.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
