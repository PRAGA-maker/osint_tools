---
id: bigfoot-sightings-and-density-of-the-us-with-biomes
name: Bigfoot Sightings and Density of the US with Biomes
description: Use when you have a US `geolocation` and want the density of reported Bigfoot sightings and the local biome there — returns `geolocation` context layers.
url: https://www.arcgis.com/apps/View/index.html?appid=f987f36187c140aeab6eb157e909eb64
category: geolocation
path:
- geolocation
bestFor: Visualising where BFRO Bigfoot-sighting reports cluster across the US, overlaid on biome data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public ArcGIS web map; no account needed to view.
opsec: passive
opsecNote: A read-only public ArcGIS map; browsing it is passive and reveals nothing to any target. Only your requests to Esri's ArcGIS hosting are logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist ArcGIS StoryMap built from crowd-sourced BFRO sighting reports; the underlying "sightings" are anecdotal and unverifiable.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bigfoot density map
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Bigfoot Sightings and Density of the US with Biomes

> A novelty ArcGIS map of crowd-sourced Bigfoot sighting density across the US, layered on biome data — a fringe geolocation curiosity, not an investigative lookup.

## When to use
Genuinely marginal for missing-persons work. Its only investigative angle: the underlying BFRO "sighting" reports are geotagged, dated, first-person accounts of people being in remote wilderness at a specific time. If a case involves a witness who filed such a report, or you are building a picture of foot traffic / anecdotal activity in a remote area, this map shows where those reports cluster and what biome each is in. Otherwise it is a demonstration of ArcGIS density mapping, nothing more.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ArcGIS app URL in any browser.
2. Pan/zoom to the US region of interest; the heat/density layer shows reported-sighting concentration, with a biome layer beneath.
3. Click a cluster or point (where the app exposes it) to read the report attributes — date, county, narrative.
4. Pivot: a specific report links back to the BFRO database, whose full narrative may name a witness or describe access routes; the biome context feeds terrain/search-area reasoning.

## Inputs → Outputs
- **In:** `geolocation` (a US area you pan to)
- **Out:** `geolocation` context — sighting-report density and biome classification for that area
- **Empty/negative result looks like:** sparse or no points over your area of interest — simply no reports were filed there; it says nothing about a person.

## Gotchas & OpSec
- The data is anecdotal folklore; treat every "sighting" as unverifiable and of interest only for the human-activity metadata around it, never as fact.
- Read-only and public — no OpSec exposure beyond ArcGIS hosting logs.
- Density is normalised to reporting behaviour, not ground truth; heavily-populated or internet-active regions over-report.

## Overlaps ("do both")
- Pairs with other terrain/biome and wilderness-activity maps when scoping a remote search area — this one only adds anecdotal sighting-report locations.

## Trust & verifiability
`trust: unverified` — a hobbyist StoryMap over crowd-sourced BFRO reports. The map renders reliably; the source data is anecdotal and cannot be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bigfoot-sightings-and-density-of-the-us-with-biomes |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
