---
id: osmbuildings-org
name: OSM Buildings
description: Use when you're verifying a `geolocation` from a photo and need building shapes/heights — returns a 3D map of buildings (footprint, height, type) to match against a skyline or structure in an image.
url: https://osmbuildings.org/
category: geolocation
path:
- geolocation
bestFor: 3D visualization of building footprints and heights to corroborate a location from a photo's structures/skyline.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The public 3D map viewer is free to browse; OSM Buildings also offers commercial data/API products (ONEGEO), but visual verification needs no account.
opsec: passive
opsecNote: Browsing a public 3D map built from OpenStreetMap data contacts no subject and reveals nothing about your target. Standard clean-session hygiene applies to the site itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built on crowdsourced OpenStreetMap building data; footprints/heights are community-contributed, so completeness and height accuracy vary by city.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-earth
- openstreetmap
- mapillary
aliases:
- osmbuildings.org
- OSM Buildings
tags:
- geolocation
- 3d-buildings
- openstreetmap
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# OSM Buildings

> A 3D map that renders building footprints, heights, and types from OpenStreetMap data — a geolocation aid for matching the structures or skyline in a photo to a real place.

## When to use
You are verifying or narrowing a `geolocation` from an image where buildings are the main clue: a distinctive tower, a row of specific footprints, a skyline profile. OSM Buildings lets you view candidate areas in 3D and compare building shapes, relative heights, and arrangement against the photo, helping you confirm or reject a location hypothesis when street-level landmarks are absent or ambiguous.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osmbuildings.org/ and navigate to your candidate area.
2. Rotate/tilt the 3D view to match the camera angle of your source photo.
3. Compare building footprints, heights, and spacing to the structures in the image; click a building for its recorded height/type/purpose where available.
4. If the arrangement matches, cross-confirm in a photo-based tool; if not, test the next candidate.
5. Pivot: confirm the match in `[[google-earth]]` (imagery/terrain) and `[[mapillary]]` (street-level photos) for ground-truth.

## Inputs → Outputs
- **In:** `geolocation` (a candidate area to compare against a photo)
- **Out:** `geolocation` corroboration — 3D building footprints, heights, and types to confirm/reject the location
- **Empty/negative result looks like:** flat or missing buildings in the area — OSM has no 3D building data there (common outside well-mapped cities), so the tool can't help for that spot; fall back to imagery-based methods.

## Gotchas & OpSec
- Coverage and height accuracy depend on OpenStreetMap contributions — dense in major cities, sparse or absent elsewhere; a bare area means "not mapped," not "no buildings."
- Rendered heights are approximate; use for relative comparison, not exact measurement.
- OpSec: **passive** — a public map, no subject interaction.

## Overlaps ("do both")
- Pairs with `[[google-earth]]` (authoritative imagery/3D in more places) and `[[mapillary]]` (street-level views) — OSM Buildings gives quick 3D massing, and those confirm with real imagery.

## Trust & verifiability
`trust: community` — it visualizes crowdsourced OSM data, so treat matches as strong leads to confirm against real imagery; completeness and heights vary by how well the area is mapped.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osmbuildings-org |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
