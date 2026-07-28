---
id: thingful-net
name: Thingful
description: Use when you have a `geolocation` and want public IoT/sensor devices there (weather, air quality, energy, marine) plotted on a map — returns geolocation-scoped device data.
url: https://www.thingful.net/
category: search-engines
path:
- search-engines
bestFor: Finding publicly-shared connected sensors (weather, air quality, energy, marine, seismic) by location on a map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse the map of public sensor data; programmatic/API access has paid tiers.
opsec: passive
opsecNote: Passive read of public sensor feeds; you disclose only your own map queries, nothing about a subject. Safe without a sock puppet, though VPN hygiene is fine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A discovery index of publicly-shared IoT data; device presence/accuracy depend on third-party owners publishing feeds, so coverage and freshness vary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- thingful
aliases:
- Thingful.net
tags:
- iot
- sensors
- geolocation
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Thingful

> A search engine for the Internet of Things — public sensors (weather, air quality, energy, marine, seismic) plotted on a world map, browsable by location.

## When to use
You have a `geolocation` and want environmental/sensor context for that place from publicly-shared connected devices: local weather stations, air-quality monitors, energy or marine sensors. In OSINT this adds real-world measurement context to a location — corroborating conditions, spotting anomalies, or finding a nearby public sensor that reports on an area of interest. It indexes public device data by place; it doesn't find people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thingful.net/ and navigate the map to your `geolocation`.
2. Filter by data type (weather, air quality, energy, marine, etc.).
3. Open a device to read its public readings and metadata.
4. Note timing/values as environmental corroboration for the location.
5. Pivot: combine with webcams (`[[city-webcams-com]]`), outage maps (`[[outage-map]]`) and imagery to build a fuller picture of conditions at a place.

## Inputs → Outputs
- **In:** `geolocation` (map area) + optional sensor-type filter
- **Out:** publicly-shared sensor readings and metadata for that area (`geolocation`-scoped environmental data)
- **Empty/negative result looks like:** few or no devices near the target — public-sensor coverage is patchy and owner-dependent; fall back to official environmental datasets.

## Gotchas & OpSec
- OpSec: passive; nothing about your target is disclosed.
- Coverage depends entirely on third parties publishing device data — expect gaps and stale/dead sensors.
- It surfaces *public* devices only; treat it as environmental context, not a way to access private/secured systems.

## Overlaps ("do both")
- Do both with webcams and outage/environmental maps — Thingful gives sensor measurements, webcams give live scenes, outage maps give infrastructure status; together they characterise a place and time.

## Trust & verifiability
`trust: community` — a discovery index of third-party public sensors; verify individual readings against the device's own source or an official dataset before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thingful-net |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
