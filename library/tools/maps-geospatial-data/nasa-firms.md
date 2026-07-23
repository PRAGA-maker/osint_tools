---
id: nasa-firms
name: NASA FIRMS
description: Use when you have a `geolocation`/`address` and a date and want satellite thermal-anomaly data — returns mapped fire/heat detections to corroborate fires, explosions, or burning.
url: https://firms2.modaps.eosdis.nasa.gov/map/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Confirming and timestamping fires, explosions, or thermal events at a location using satellite infra-red detections.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free NASA/US-government service; the interactive map needs no account, and the data-download/API portal offers a free MAP_KEY.
opsec: passive
opsecNote: "You query NASA's satellite archive, not any subject — fully passive and unattributable to a target. It's a US government site; standard sock-puppet browsing is more than enough. The data is aggregate earth-observation, so there's no personal-privacy exposure in the query itself."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authoritative NASA Earth-observation product (MODIS/VIIRS active-fire detections) featured in the Bellingcat toolkit; detections are real thermal anomalies but require interpretation — not every hotspot is a fire.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- firms
- nasa-earthdata-search
- nasa-kids-club
- nasa-worldview
aliases:
- FIRMS
- Fire Information for Resource Management System
tags:
- bellingcat-toolkit
- maps
- satellite
- thermal-detection
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# NASA FIRMS

> A world map of satellite-detected thermal anomalies (MODIS/VIIRS) — used in verification work to confirm and time-stamp fires, explosions, and large heat events at a given location.

## When to use
You have a `geolocation`/`address` and a date, and want independent satellite evidence that something burned or exploded there — corroborating a claimed strike, wildfire, industrial fire, or flare, and pinning down roughly when. A staple geolocation/verification tool (Bellingcat toolkit). Not a person-finder, so direct missing-persons relevance is low, though it can place/timestamp an event tied to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://firms2.modaps.eosdis.nasa.gov/map/ and navigate to the `geolocation`/`address` of interest.
2. Set the date range and the satellite/sensor layers (VIIRS gives finer ~375 m resolution than MODIS ~1 km).
3. Read the plotted detections: each point is a thermal anomaly with an acquisition date/time and confidence value.
4. Correlate detection timing/location with your other evidence; use the download/API portal (free MAP_KEY) for the raw points over an area/time.
5. Cross-check with a same-day satellite imagery layer to see what actually burned.

## Inputs → Outputs
- **In:** `geolocation`/`address` + date range
- **Out:** mapped thermal-anomaly detections with timestamps, confidence, and `geolocation`
- **Empty/negative result looks like:** no detections — the fire may have been too small/brief, cloud-obscured, or between satellite passes; absence is **not** proof nothing burned.

## Gotchas & OpSec
- Not every hotspot is a fire: gas flares, solar panels, hot industrial roofs, and sun glint produce anomalies — interpret, don't assume.
- Temporal gaps: polar-orbiting satellites pass a few times a day, so short events can fall between overpasses; resolution limits small fires.
- Confidence values and sensor differences matter — weight high-confidence VIIRS points over low-confidence MODIS ones.

## Overlaps ("do both")
- Pairs with its NASA siblings [[nasa-worldview]] and [[nasa-earthdata-search]] and with [[firms]] — FIRMS flags *where/when* heat was detected; Worldview/imagery shows *what* was there, so confirm a detection against same-day imagery.

## Trust & verifiability
`trust: trusted` — authoritative NASA sensor data; detections are real thermal anomalies with known caveats, so the verification comes from correctly interpreting confidence, timing, and imagery, not from doubting the source.
