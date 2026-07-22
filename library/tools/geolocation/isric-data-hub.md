---
id: isric-data-hub
name: ISRIC Data Hub
description: Use when you have a candidate `geolocation` and want soil/terrain ground-truth to verify it against a photo — returns soil-type and land attribute geodata layers.
url: https://data.isric.org/geonetwork/srv/eng/catalog.search#/home
category: geolocation
path:
- geolocation
bestFor: Cross-checking soil colour/type and land attributes at a coordinate to confirm or reject a geolocation hypothesis from imagery.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Open scientific data catalogue (ISRIC World Soil Information / SoilGrids). Data and maps are free and openly licensed; no account needed to browse or download most layers.
opsec: passive
opsecNote: You browse a public scientific geodata catalogue; you never touch the subject or the location. No disclosure risk. Standard web access to an open data portal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: ISRIC — World Soil Information is an established independent scientific institute (Wageningen, NL); its SoilGrids and soil-profile data are peer-reviewed and authoritative for what they cover.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ISRIC
- World Soil Information
- SoilGrids
tags:
- geolocation
- terrain-verification
- geospatial-data
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# ISRIC Data Hub

> An open global soil-and-terrain geodata catalogue (SoilGrids, soil profiles) that geolocation analysts use as ground-truth to confirm or reject where a photo was taken.

## When to use
You are geolocating imagery and have a candidate `geolocation` — you can see soil colour, terrain, or exposed ground in the photo and want to check whether it is consistent with a proposed coordinate. ISRIC's SoilGrids provides modelled soil type, colour, pH, texture, and depth at ~250 m global resolution, so a reddish laterite scene can be tested against a location's predicted soil, helping rule locations in or out. It is a verification aid, not a locator — it won't find a place for you, but it can break ties between candidates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the catalogue at https://data.isric.org/geonetwork/srv/eng/catalog.search#/home and search for the relevant layer (e.g. "SoilGrids", soil colour, texture class).
2. Open the map viewer / WMS layer and navigate to your candidate coordinate, or pull the value via the SoilGrids REST API for exact-point queries.
3. Read the predicted soil property at that point (type, colour, texture) and compare against what the image actually shows.
4. Pivot: a match strengthens a `geolocation` hypothesis; a clear mismatch (e.g. photo shows dark clay, model predicts pale sand) is evidence against it — combine with vegetation, terrain and sun-angle checks.

## Inputs → Outputs
- **In:** candidate `geolocation` (coordinate/area) + observed ground characteristics from imagery
- **Out:** predicted soil/terrain attributes at that `geolocation` (type, colour, texture, depth) to confirm/refute the location
- **Empty/negative result looks like:** the layer has no data or only coarse global fill for the point, or the modelled value plainly contradicts the image — the latter is a useful negative, the former just means low resolution here.

## Gotchas & OpSec
- SoilGrids is **modelled/interpolated**, not a per-field survey — ~250 m resolution means it's for regional consistency checks, not distinguishing two nearby fields.
- Predicted soil colour ≠ observed surface colour (moisture, crops, disturbance all differ); use it as corroboration alongside other geolocation signals, never as sole proof.
- Zero direct people-search value — its only investigative use is terrain/soil verification of image locations.
- OpSec: fully passive; browsing an open data portal discloses nothing to any subject.

## Overlaps ("do both")
- Pair with satellite/terrain imagery and vegetation/land-cover datasets — ISRIC checks the ground composition while imagery checks shape and structure; agreement across both is what makes a geolocation defensible.

## Trust & verifiability
`trust: trusted` — ISRIC is a recognised independent soil-science institute and SoilGrids is peer-reviewed; the data is authoritative for soil modelling, with the honest caveat that it is a global model, not a local ground survey.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | isric-data-hub |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
