---
id: convert-geographic-units
name: Convert Geographic Units
description: Use when you have a `geolocation` in one coordinate format and want it in another (DD, DMS, UTM, NATO) across map datums — returns the converted `geolocation`.
url: http://rcn.montana.edu/resources/Converter.aspx
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Converting a single set of coordinates between decimal degrees, DMS, UTM and NATO/MGRS across datums like WGS84 and NAD83.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free academic resource hosted by Montana State University; no account.
opsec: passive
opsecNote: A purely client/server math conversion of coordinates you already hold — nothing is sent to any subject and there is no target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by Montana State University's Yellowstone Research Coordination Network; conversions are deterministic geodesy, verifiable against any other converter.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- what3words
aliases:
- coordinate converter
- Yellowstone RCN converter
tags:
- bellingcat-toolkit
- maps
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# Convert Geographic Units

> A coordinate-format converter: paste a location in one system (decimal degrees, DMS, UTM, NATO) and get it back in the others, honouring the map datum.

## When to use
Different sources hand you coordinates in different shapes — a phone GPS gives decimal degrees, a military grid reference is NATO/MGRS, a surveying record is UTM, a photo caption is degrees-minutes-seconds. When two datasets or teams need the *same* point in a *different* format (or datum), this converts cleanly so you don't misplot a location by transposing formats by hand.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://rcn.montana.edu/resources/Converter.aspx.
2. Enter the `geolocation` in whichever field matches its current format (decimal lat/long, DMS, standard UTM with zone+hemisphere, or NATO UTM with digraph).
3. Select the correct map datum (WGS84, NAD83, WGS72, or a historical ellipsoid) — this matters; the wrong datum shifts the point by tens of metres.
4. Convert and read the equivalent values in all other formats.
5. Pivot: take the output into a mapping tool or share the format a responder's system expects; use `[[what3words]]` if you also need a shareable three-word label.

## Inputs → Outputs
- **In:** a `geolocation` in DD, DMS, UTM or NATO form + a datum
- **Out:** the same `geolocation` expressed in the other formats
- **Empty/negative result looks like:** malformed input (missing zone/hemisphere for UTM, out-of-range degrees) produces an error or a nonsensical value — sanity-check the result by plotting it once.

## Gotchas & OpSec
- Datum matters: NATO conversions here assume WGS84; mixing datums silently offsets the point.
- Values are rounded to the nearest metre, adequate for mapping but not survey-grade.
- OpSec: passive; a self-contained math operation on data you already hold.

## Overlaps ("do both")
- Pairs with `[[what3words]]` — that resolves/creates a shareable three-word code, while this reshapes raw coordinates into the technical formats GIS and responder systems ingest.

## Trust & verifiability
`trust: trusted` — a university-hosted deterministic converter; any conversion can be independently reproduced in another geodesy tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | convert-geographic-units |
