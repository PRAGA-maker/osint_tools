---
id: ncei-noaa-gov
name: NCEI Natural Hazards Viewer
description: Use when you have a `geolocation` and want historical natural-hazard events near it — returns dated earthquake, tsunami and volcano events geolocated on a map.
url: https://www.ncei.noaa.gov/maps/hazards/
category: geolocation
path:
- geolocation
bestFor: Checking whether a location experienced a significant earthquake, tsunami or volcanic event on/around a given date.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free US-government service (NOAA/NCEI); no account or key needed to use the interactive viewer.
opsec: passive
opsecNote: You browse a public NOAA map; nothing about your subject is submitted. Standard web-log exposure only. No sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by NOAA's National Centers for Environmental Information — authoritative, curated global hazard event databases.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- noaa-data-access-viewer
- nexrad-data-inventory-search
- ngdc-bathymetry-map
aliases:
- NOAA Natural Hazards Viewer
- ncei.noaa.gov hazards
tags:
- maps
- geolocation
- nature
- hazards
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# NCEI Natural Hazards Viewer

> NOAA's authoritative map of historical significant earthquakes, tsunamis and volcanic eruptions — a way to place a location against the natural-disaster record.

## When to use
You have a `geolocation` (or place name) and want to know whether a significant natural hazard — earthquake, tsunami, or volcanic eruption — struck there and when. In an investigation this is context/corroboration: confirming a disaster event that a subject referenced, dating a photo against a known event, or explaining a gap in records (evacuation, displacement) tied to a specific place and time. It is a supporting layer, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ncei.noaa.gov/maps/hazards/.
2. Pan/zoom to the `geolocation` of interest, or search the location.
3. Toggle the hazard layers (Significant Earthquakes, Tsunami Events/Runups, Significant Volcanic Eruptions) in the layer panel.
4. Click a plotted event to read its record: date, magnitude/intensity, deaths/damage, and precise coordinates.
5. Pivot: the event date/coordinates anchor a timeline; combine with news archives or imagery tools to corroborate a subject's account or date media. The underlying databases are also downloadable/queryable via NCEI APIs.

## Inputs → Outputs
- **In:** `geolocation` (map location or place)
- **Out:** `geolocation`-tagged hazard events (date, type, magnitude, impact) near the location
- **Empty/negative result looks like:** no plotted events in the area/timeframe means no *significant* recorded hazard — minor events below the significance threshold are not included, so absence isn't "nothing ever happened."

## Gotchas & OpSec
- "Significant" is a curated threshold (deaths, damage, magnitude/Moment). Small local quakes won't appear — use USGS for exhaustive seismicity.
- Historical depth varies by region; older non-Western events are sparser.
- OpSec: fully passive; nothing about your subject leaves your browser.

## Overlaps ("do both")
- Pairs with `[[noaa-data-access-viewer]]` and `[[nexrad-data-inventory-search]]` — this covers geologic hazards, those cover climate/weather and radar data, so together they cover most of the natural-environment context around a location and date.

## Trust & verifiability
`trust: trusted` — a first-party NOAA/NCEI product drawing on its curated global hazard databases; event records are authoritative and citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ncei-noaa-gov |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
