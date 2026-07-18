---
id: skyscraperpage
name: SkyscraperPage
description: Use when you have a building `name`/`address` or a skyline `image` and want to identify a structure — returns building details, height, dates, and to-scale diagrams.
url: https://skyscraperpage.com
category: public-records
path:
- public-records
bestFor: Identifying and profiling tall buildings from a name, city, or skyline image using a diagram database.
selectorsIn:
- address
- image
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free community database; no account required to browse.
opsec: passive
opsecNote: A reference database you browse — no subject is involved and nothing is signalled. Purely informational building data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running enthusiast-maintained building database; details and diagrams are community-contributed, generally accurate for notable structures but not an official record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- skyscraperpage.com
- Skyscraper Page
tags:
- buildings
- architecture
- geolocation
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# SkyscraperPage

> A community database of the world's tall buildings with to-scale diagrams — useful for putting a name (and a location) to a distinctive building in a photo.

## When to use
A niche geolocation aid: you have a skyline or building shown in an `image`, or a building `name`/city, and want to identify the structure and its details (height, floors, completion year, location). Matching a distinctive tower in a photo to a SkyscraperPage entry can pin a city or exact building — a supporting move in image geolocation, not a people lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://skyscraperpage.com.
2. Browse by city or search by building name; use the to-scale diagrams to compare silhouettes against a building in your image.
3. Open a building entry: height, floor count, year, location, and often photos.
4. Match the profile/silhouette to your image to identify the structure and its city.
5. Pivot: a confirmed building gives a `geolocation`/`address` anchor; combine with Street View/satellite to fix the exact viewpoint of the photo.

## Inputs → Outputs
- **In:** building `name`/city, or a skyline `image` to match
- **Out:** building identity, height/floors/year, and location (`geolocation`/`address`)
- **Empty/negative result looks like:** no match — the structure isn't notable/tall enough to be catalogued, or the diagram doesn't match; most ordinary buildings won't appear.

## Gotchas & OpSec
- Coverage is **notable/tall buildings** — low-rise and generic structures won't be listed, so it only helps with distinctive skylines.
- Data is enthusiast-contributed; heights/dates are usually right for famous buildings but verify anything decisive.
- OpSec: fully passive — a reference database.

## Overlaps ("do both")
- Pairs with Google Street View/Earth, Emporis-style building databases, and reverse-image search — SkyscraperPage helps name the building; mapping tools then fix the exact camera position.

## Trust & verifiability
`trust: community` — an enthusiast-maintained catalogue. Reliable for well-known structures, but community-sourced, so treat it as an identification aid and confirm the location on a map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skyscraperpage |
