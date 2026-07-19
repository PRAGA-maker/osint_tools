---
id: aqicn
name: AQICN (World Air Quality Index)
description: Use when you have a `geolocation` and want a map of live air-quality monitoring stations there — returns station points that double as corroborating environmental data.
url: https://aqicn.org/map/world/
category: geolocation
path:
- geolocation
bestFor: Viewing a worldwide map of real-time air-quality monitoring stations and their readings for a given area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The interactive world map and station readings are free with no account. A free API token is available for programmatic access; there is no hard paywall on basic use.
opsec: passive
opsecNote: You read a public environmental-data map; nothing about your subject is queried or exposed. Fully passive — ordinary browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: World Air Quality Index project aggregates official government and citizen monitoring stations worldwide; readings are third-party sensor data, reliable as environmental context.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- World Air Quality Index
- waqi
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- environmental-data
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# AQICN (World Air Quality Index)

> A worldwide map of live air-quality monitoring stations — a niche source of time-stamped environmental data that can corroborate conditions at a place and time.

## When to use
You have a `geolocation` and want environmental context: where the nearest air-quality stations are and what they were reading. Its OSINT value is indirect but real — historical/real-time air-quality readings can help corroborate weather/haze/smoke conditions visible in a photo or video, or place an event in time by matching documented conditions. It is not a people or location-pinpointing tool; it's supporting environmental evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://aqicn.org/map/world/ and pan/zoom to your area of interest.
2. Read the coloured station markers (AQI value) and click one for its detailed, time-stamped readings and location.
3. Note the station's exact position and reading for the date/time relevant to your case.
4. For bulk/historical queries, request a free API token and pull station data programmatically.
5. Pivot: use readings to corroborate visible conditions (smog/smoke/clear air) in imagery you're dating or geolocating.

## Inputs → Outputs
- **In:** `geolocation` (map area)
- **Out:** nearby monitoring-station `geolocation`s and their air-quality readings (as environmental corroboration)
- **Empty/negative result looks like:** no stations in view — common for rural/remote areas with sparse monitoring; absence of a station isn't evidence about conditions there.

## Gotchas & OpSec
- Indirect relevance: this is environmental context, not a locator — sensible only as corroboration alongside other evidence.
- Station coverage is uneven and denser in cities/developed regions; historical depth varies by station.
- Readings are third-party sensor data of varying quality (official vs citizen sensors) — note the source.
- OpSec: fully passive.

## Overlaps ("do both")
- Complements imagery-dating workflows — pair a reading with satellite imagery from `[[earth-engine-dataset]]` or weather archives to corroborate conditions at a specific time.

## Trust & verifiability
`trust: community` — an aggregator of official and citizen air-quality stations. Reliable as environmental context, but check each station's source and timestamp before using a reading to date or corroborate anything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aqicn |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
