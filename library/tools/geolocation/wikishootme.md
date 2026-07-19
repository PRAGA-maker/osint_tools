---
id: wikishootme
name: WikiShootMe
description: Use when you have a `geolocation` and want geotagged Wikipedia/Wikidata items and Commons images near it on a map — returns nearby `image`s and `geolocation` context.
url: https://wikishootme.toolforge.org/
category: geolocation
path:
- geolocation
bestFor: Showing, on a live map, the geotagged Wikipedia/Wikidata items and Wikimedia Commons photos near any point — useful for finding existing imagery of a place.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free, open-source Wikimedia Toolforge tool; no account needed to browse. Logging in with a MediaWiki account only unlocks contribution features (uploading/linking images).
opsec: passive
opsecNote: You query Wikimedia map data, not the target — nothing about your subject is exposed. Fully passive; logging in is optional and only for contributing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Runs on Wikimedia Toolforge over Wikidata/Commons; data is open, community-maintained Wikimedia content. The map faithfully reflects what's geotagged in those projects.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wikinearby
aliases:
- Wiki Shoot Me
tags:
- Maps, Geolocation and Transport
- Social media and photos
- wikimedia
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# WikiShootMe

> A live Wikimedia map that plots geotagged Wikipedia/Wikidata items and Commons images around any point — a fast way to find existing photos and encyclopedic features of a place.

## When to use
You have a `geolocation` and want to see what imagery and documented features already exist there: red/green/blue markers show Wikidata items with/without images and Commons photos nearby. In geolocation work it helps identify a landmark in a photo (does a matching item/photo exist at those coordinates?) and surfaces reference imagery of a location you're trying to confirm or describe.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikishootme.toolforge.org/ and pan/zoom to your area (or enter coordinates).
2. Read the colour-coded markers: Wikidata items with images, items lacking images, and Commons photos — click any marker for its item/photo and exact coordinates.
3. Open a Commons photo to compare it against your imagery, or follow a Wikidata item to its Wikipedia article for context.
4. (Optional) Log in with a MediaWiki account only if you want to contribute image links.
5. Pivot: a confirmed landmark/coordinate feeds your geolocation; existing Commons imagery corroborates a place's appearance.

## Inputs → Outputs
- **In:** `geolocation` (map area / coordinates); optionally an `image` to match
- **Out:** nearby geotagged Wikidata items, their `image`s, and precise `geolocation`s
- **Empty/negative result looks like:** few or no markers — the area is under-documented in Wikidata/Commons (common outside notable/urban spots), not that nothing is there.

## Gotchas & OpSec
- Coverage mirrors Wikidata/Commons: dense for notable places, sparse for ordinary streets and under-mapped regions.
- It shows what's geotagged in Wikimedia, not live/street-level imagery — absence of a marker ≠ absence of a feature.
- OpSec: fully passive Wikimedia lookup.

## Overlaps ("do both")
- Pairs with `[[copernix]]` and `[[wikinearby]]` — WikiShootMe emphasises geotagged images/Wikidata items on a map; those surface nearby Wikipedia articles as reading context.

## Trust & verifiability
`trust: trusted` — an official Wikimedia Toolforge tool over open Wikidata/Commons data. The imagery and coordinates are authentic community content; still confirm a specific match against the source item before concluding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikishootme |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
