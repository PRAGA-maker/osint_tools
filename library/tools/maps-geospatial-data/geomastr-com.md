---
id: geomastr-com
name: Geomastr
description: Use when you have an `image` of an unknown place and want country/region clues — returns a searchable reference of bollards, plates, signs, poles, and other visual identifiers by country.
url: https://geomastr.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying a photo's country/region from visual infrastructure clues (bollards, license plates, road signs, poles, alphabets).
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference/training hub; no account required.
opsec: passive
opsecNote: A reference site you consult while analysing an image offline — you never query or touch the subject. Nothing is signalled; the interpretation happens on your side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community GeoGuessr training resource; the visual-clue references are well-organised and broadly accurate, but it's a study aid, not an authoritative geographic database.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- geomastr.com
- Geomastr GeoGuessr hub
tags:
- geolocation
- geoguessr
- image-analysis
- visual-clues
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Geomastr

> A geolocation clue reference (built for GeoGuessr players, invaluable for OSINT): look up how bollards, plates, signs, poles, and alphabets differ by country to pin down where a photo was taken.

## When to use
You have an `image` — a photo/video frame of an unknown outdoor location — and need to narrow down the country or region from environmental details. Geomastr catalogues the tell-tale visual infrastructure geolocators rely on (bollard styles, license-plate formats, road-sign and road-marking conventions, utility-pole types, driving side, alphabets, phone prefixes, currencies, ccTLDs, postal branding), organised by country so you can match what's in the frame to a place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://geomastr.com/.
2. Identify distinctive elements in your image (a bollard, a plate colour/format, a sign font, a pole shape, a script/alphabet).
3. Use the reference/search to find which countries match those features; cross-reference several clues to converge.
4. Narrow to a country/region, then switch to a map tool (Street View, satellite) to confirm the exact spot.
5. Pivot: the candidate `geolocation` feeds mapping/Street-View confirmation and metadata cross-checks on the original image.

## Inputs → Outputs
- **In:** `image` with visible environmental/infrastructure clues
- **Out:** candidate country/region (`geolocation`) from matched visual identifiers
- **Empty/negative result looks like:** ambiguous clues that fit many countries — common with generic scenes; you'll need more distinctive features (plate, sign text, script) before Geomastr helps.

## Gotchas & OpSec
- It's a **reference/training aid**, not an automated geolocator — you do the matching; it won't take an image and output coordinates.
- Clues can be shared across neighbouring countries; rely on the *combination* of features, not a single one.
- OpSec: fully passive — offline reference use.

## Overlaps ("do both")
- Pairs with Google Street View / satellite imagery and reverse-image/EXIF tools: Geomastr narrows the country from visual clues, then Street View pinpoints the location and EXIF (if present) confirms it.

## Trust & verifiability
`trust: community` — a well-regarded community study resource. Its clue references are broadly reliable, but treat conclusions as hypotheses to confirm on a map, since visual features overlap across regions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geomastr-com |
