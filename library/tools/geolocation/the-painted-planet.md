---
id: the-painted-planet
name: The Painted Planet
description: Use when you have a `geolocation` and want artworks depicting that place — returns landscape/cityscape paintings (from Wikidata) tied to the area's coordinates.
url: https://hicsuntleones.nl/paintedplanet/
category: geolocation
path:
- geolocation
bestFor: Finding paintings/artworks that depict a specific geographic location, sourced from Wikidata coordinates.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: free
costNote: Free; a hobby/data-art project built on open Wikidata.
opsec: passive
opsecNote: You query a static Wikidata-backed map, not any person or the target's systems — nothing is signalled to anyone. It is a niche corroboration aid, not an investigative lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community data-visualisation project on top of Wikidata; the artwork-to-location links are only as good as Wikidata's crowd-sourced coordinates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Painted Planet
tags:
- geolocation
- wikidata
- art
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# The Painted Planet

> A map of the world's art: click a location and see the landscape/cityscape paintings that depict it, drawn from Wikidata coordinates.

## When to use
A narrow, occasional aid for geolocation puzzles: you have a `geolocation` (or are trying to place a scene shown in a painting/print) and want to see how artists have depicted that area, or to match a historical view to a real place. It is far from a core investigative tool — reach for it only when a case genuinely involves artwork tied to a location, otherwise a general geolocation workflow is more useful.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hicsuntleones.nl/paintedplanet/.
2. Pick a country from the dropdown or click a point/region on the map (toggle "cityscapes" for urban views).
3. Browse the returned paintings depicting that area.
4. Read the output: artwork `image`s with their Wikidata links and the coordinates they're pinned to.
5. Pivot: a matched artwork's Wikidata entry gives creator/date/location metadata to corroborate a place identification.

## Inputs → Outputs
- **In:** `geolocation` (map point or country)
- **Out:** paintings/`image`s depicting the location, with Wikidata provenance
- **Empty/negative result looks like:** no paintings pinned for the area — meaning Wikidata has no georeferenced artwork there, which is common for most ordinary locations.

## Gotchas & OpSec
- Coverage is sparse and art-historical — it maps *notable depicted places*, not arbitrary addresses, so most real-world investigation locations return nothing.
- Accuracy depends entirely on Wikidata's crowd-sourced coordinates; treat placements as approximate.
- OpSec: fully passive; a static open-data map.

## Overlaps ("do both")
- Pairs with a mainstream geolocation/reverse-image workflow — this only adds value in the rare case an artwork or historical view is part of the puzzle.

## Trust & verifiability
`trust: community` — a small independent project visualising Wikidata. Provenance is transparent (each result links back to Wikidata), but the underlying data is crowd-sourced, so verify coordinates before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-painted-planet |
