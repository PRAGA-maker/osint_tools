---
id: topotijdreis-nl
name: Topotijdreis.nl
description: Use when you have a Dutch `address`/`geolocation` and want to see how that spot looked across ~200 years of maps — returns historical Netherlands topographic maps by year for the same coordinates.
url: https://www.topotijdreis.nl
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Comparing a Dutch location across two centuries of topographic maps to see how it changed over time.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public service from the Dutch land registry (Kadaster); no account or payment.
opsec: passive
opsecNote: Fully passive — you browse historical map tiles; nothing is queried about any person and no target is contacted. Safe to use freely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Kadaster, the official Dutch land-registry/mapping agency; the historical maps are authoritative government cartography.
missingPersonsRelevance: low
coverage:
- nl
aliases:
- Topotijdreis
- topotijdreis.nl
- topographic time travel Netherlands
tags:
- bellingcat-toolkit
- maps
- historical
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Topotijdreis.nl

> Kadaster's "topographic time journey": scroll through ~200 years of official Dutch maps for any location to see exactly how a place — buildings, roads, waterways, land use — changed over time.

## When to use
You have a location in the Netherlands (an `address` or `geolocation`) and need its history: when a building or road appeared or vanished, what a site looked like in a given decade, or how a landscape changed between two dates. Reach for Topotijdreis for chronolocation and historical-imagery corroboration on Dutch soil — pairing a modern satellite view with the map from the relevant year to confirm or refute claims about when something existed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.topotijdreis.nl and pan/zoom to your Dutch location (search by place or navigate the map).
2. Use the year slider/timeline to move through the historical map series (roughly early-19th-century to present).
3. Compare the same coordinates across years: watch for the appearance/disappearance of structures, roads, and waterways.
4. Note the map year that matches (or contradicts) your evidence — e.g. a building present in a photo but absent from the map of that year.
5. Pivot: combine with modern satellite/aerial imagery and street-level views to build a full before/after picture; feed the confirmed date into your chronolocation.

## Inputs → Outputs
- **In:** a Dutch `geolocation`/`address`
- **Out:** historical topographic maps of that spot by year (a `geolocation`-anchored time series)
- **Empty/negative result looks like:** coverage only for the Netherlands — a location outside NL returns nothing; and very early maps are coarser, so fine detail may be absent in older years.

## Gotchas & OpSec
- Netherlands only — for other countries use national equivalents or historical-imagery archives.
- Older maps are less precise/less complete than modern ones; judge detail against the era's cartographic standards.
- OpSec: passive; browsing maps exposes nothing.

## Overlaps ("do both")
- Pairs with modern satellite/aerial imagery and historical-imagery tools — Topotijdreis gives the *map* history, those give the *photo* history; together they date changes precisely. Use alongside general mapping to fix the exact coordinates first.

## Trust & verifiability
`trust: trusted` — official Kadaster cartography, so the historical maps themselves are authoritative; the interpretive step (what a feature is, exact dating) is yours to confirm against other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | topotijdreis-nl |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
