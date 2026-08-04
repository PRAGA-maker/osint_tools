---
id: amazonia-socio-ambiental-raisg
name: Amazonia Socio Ambiental (RAISG)
description: Use when you have a `geolocation`/area in the Amazon basin and want land-use context — returns maps and downloadable shapefiles of indigenous territories, mining, oil concessions, roads, fires and deforestation.
url: https://www.raisg.org/en/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Amazon-basin geospatial layers (indigenous lands, mining, roads, fires, deforestation) as maps and shapefiles.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to view online and download; datasets provided as shapefiles plus APIs, no account required.
opsec: passive
opsecNote: You browse/download published environmental datasets — nothing touches any individual or subject. Fully passive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: RAISG (Amazon Geo-Referenced Socio-Environmental Information Network) is an established consortium of Amazon-basin research/NGO institutions; a Bellingcat-toolkit-listed authoritative source.
missingPersonsRelevance: low
coverage:
- br
- pe
- co
- ec
- bo
- ve
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- RAISG
- raisg.org
- amazoniasocioambiental.org
tags:
- bellingcat-toolkit
- environment-wildlife
- geospatial
- amazon
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Amazonia Socio Ambiental (RAISG)

> The authoritative geospatial atlas of the Amazon basin — interactive maps and downloadable shapefiles for indigenous territories, protected areas, mining, oil/gas concessions, roads, fires and deforestation across nine countries.

## When to use
Your case touches the Amazon (Brazil, Peru, Colombia, Ecuador, Bolivia, Venezuela, the Guianas) and you need to know what's on the ground at a `geolocation`: is a point inside an indigenous territory or protected area? Near a legal or illegal mining block, an oil concession, a road, a recent fire or deforestation front? RAISG turns coordinates into land-use and rights context — valuable for environmental-crime, land-conflict and remote-area investigations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.raisg.org/en/.
2. Use the interactive online map (or the AMA 2.0 monitoring platform) and navigate/search to your `geolocation`/area.
3. Toggle thematic layers — indigenous territories, protected areas, mining (legal + illegal), oil/gas, roads, fire hotspots, deforestation.
4. For analysis, download the relevant theme's shapefile (or use the API) and overlay your own coordinates in GIS software.
5. Pivot: a coordinate falling inside a concession or protected area feeds land-rights records, company research (concession holders) or news search for the specific block.

## Inputs → Outputs
- **In:** `geolocation` / `address` / area within the Amazon basin
- **Out:** land-use `geolocation` context — indigenous/protected status, mining, concessions, roads, fires, deforestation
- **Empty/negative result looks like:** a point with no overlapping layers — meaning it's outside mapped features (or outside the Amazon coverage area), not that the location is undocumented.

## Gotchas & OpSec
- Human-in-the-loop: none; shapefile analysis needs GIS skills.
- OpSec: **passive** — public environmental data, no exposure.
- Data has an update cadence (layers dated by revision); check each theme's vintage and pair with near-real-time fire/deforestation feeds for current events.

## Overlaps ("do both")
- Pair with fire/deforestation feeds (NASA FIRMS, MapBiomas) and satellite imagery — RAISG gives the tenure/land-use context; those give the timely change detection over it.

## Trust & verifiability
`trust: trusted` — a respected multi-institution socio-environmental network, widely cited (Bellingcat toolkit); authoritative for Amazon land-use layers, with revision dates to check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazonia-socio-ambiental-raisg |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
