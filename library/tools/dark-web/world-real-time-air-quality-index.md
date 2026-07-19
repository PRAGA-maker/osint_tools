---
id: world-real-time-air-quality-index
name: World Real-Time Air Quality Index
description: Use when you have a place (`geolocation`/`address`) and want current or historical air-quality readings for environmental context — returns station-level AQI data, free and via API.
url: http://waqi.info
category: dark-web
path:
- dark-web
bestFor: Real-time and historical air-quality (AQI) readings by location, with a free data API.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Web map and station data are free; a free API token is available for programmatic access. Personal GAIA hardware sensors are a paid product but not needed for lookups.
opsec: passive
opsecNote: Reading a public environmental map is passive and involves no subject. Requesting an API token ties queries to an email — use a research address if you script it. Nothing here reaches or reveals a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official government EPA/monitoring-station feeds across 80+ countries; readings are sourced, though station coverage and calibration vary by region.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- WAQI
- aqicn
- waqi.info
tags:
- toddington
- curated-directory
- deep-web-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# World Real-Time Air Quality Index

> A global map of real-time air-quality readings from 10,000+ monitoring stations — environmental context, not a people-finder.

## When to use
You need environmental *context* for a location tied to a case — corroborating or dating conditions in a place (haze, wildfire smoke, a pollution event) that appears in a photo, a claim, or a timeline. It's a supporting/geolocation-context source: it holds station-level readings by place and time, not any information about individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://waqi.info and search a city/place, or click a station flag on the world map.
2. Read the current AQI plus the pollutant breakdown (PM2.5, PM10, O₃, NO₂, SO₂, CO) and the station's historical chart.
3. For scripting, get a free API token from the API page and query readings by station or geo-coordinates.
4. Cross-reference a reading's date/time against your evidence (e.g. a hazy skyline photo) to sanity-check when/where it was taken.
5. Pivot: an anomalous pollution event (wildfire, dust storm) can anchor a photo's approximate date to corroborate `geolocation`/`metadata-exif`.

## Inputs → Outputs
- **In:** a place (`geolocation` / `address` / city name)
- **Out:** station-level AQI and pollutant readings, current and historical (geo-context)
- **Empty/negative result looks like:** no nearby station — rural/low-coverage areas have sparse monitoring, so a blank map region means "no sensor," not "clean air."

## Gotchas & OpSec
- Coverage is uneven; readings come from the nearest station, which may be miles away and not representative of a micro-location.
- Holds zero personal data — don't expect any individual selectors from it.
- OpSec: fully passive; only an API token (if used) ties queries to an email.

## Overlaps ("do both")
- Pairs with weather-history and satellite-imagery tools — WAQI adds the air-quality dimension (smoke/haze events) that can date or corroborate outdoor imagery alongside weather and satellite context.

## Trust & verifiability
`trust: trusted` — it federates official monitoring-agency feeds, so readings are authoritative where stations exist; note station calibration and coverage vary by country.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-real-time-air-quality-index |
| category | dark-web |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
