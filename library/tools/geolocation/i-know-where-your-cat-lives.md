---
id: i-know-where-your-cat-lives
name: I Know Where Your Cat Lives
description: Use as a demonstration of geotag risk — maps public cat photos by the GPS `geolocation` embedded in their EXIF, illustrating how image metadata reveals a home location.
url: https://iknowwhereyourcatlives.com/
category: geolocation
path:
- geolocation
bestFor: Illustrating (and teaching) how EXIF GPS in publicly-posted photos exposes a precise location.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public art/awareness project; no account needed to browse the map.
opsec: passive
opsecNote: Browsing the map is passive. Its real OpSec lesson is defensive: it shows how the GPS EXIF in a photo pinpoints where it was taken (often a home) — a reminder to strip metadata from your own images and to check subjects' photos for the same leak.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known data-art/awareness project mapping already-public geotagged cat photos; it demonstrates a real technique rather than serving as an investigative lookup.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- jeffrey-friedl-s-image-metadata-viewer
- exiftool
aliases:
- iknowwhereyourcatlives.com
tags:
- geolocation
- exif
- awareness
- privacy
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# I Know Where Your Cat Lives

> A data-art project that plots public cat photos on a world map using the GPS baked into their EXIF — the memorable illustration of "your photos know where you live."

## When to use
This is primarily a **concept/awareness reference**, not an investigative lookup. Reach for it to understand and demonstrate the core geolocation technique it embodies: that ordinary photos posted online carry EXIF GPS that pins their capture location (frequently a home). Use it to explain to a subject/witness why an image matters, to train the instinct to check every photo's metadata, and as a reminder to sanitise your own operational images. For actually extracting a photo's coordinates, use a metadata viewer — this site just makes the risk vivid.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iknowwhereyourcatlives.com/.
2. Browse/zoom the map — each pin is a public cat photo placed by the GPS coordinates in its EXIF.
3. Note the takeaway: these locations came *only* from metadata the posters didn't realise they were sharing.
4. Apply the lesson operationally: run any subject's photo through a metadata viewer to see if it carries the same GPS leak.
5. Pivot: for a real case, `[[jeffrey-friedl-s-image-metadata-viewer]]` or `[[exiftool]]` extracts the actual `geolocation` from a specific image.

## Inputs → Outputs
- **In:** (conceptually) an `image` with embedded GPS; on the site itself you just browse the `geolocation` map
- **Out:** `geolocation` points derived from photo EXIF — demonstrating the technique
- **Empty/negative result looks like:** N/A as a lookup — it's a fixed dataset/demo. The "negative" lesson is that a photo *without* EXIF GPS (stripped by the platform) reveals nothing, which is exactly the mitigation.

## Gotchas & OpSec
- Not an investigative search tool for arbitrary targets — it's a curated awareness demo. Don't treat it as a way to locate a specific person.
- The real, transferable value is the method: check EXIF GPS on real evidence with a dedicated tool.
- OpSec: passive to browse; the defensive point is to strip metadata from your own images.

## Overlaps ("do both")
- Pairs with `[[jeffrey-friedl-s-image-metadata-viewer]]` and `[[exiftool]]` — this explains *why* photo metadata matters; those actually *extract* the GPS `geolocation` from a case image.

## Trust & verifiability
`trust: community` — a reputable, widely-cited awareness/art project using genuinely public geotagged photos. It reliably demonstrates the EXIF-geolocation risk; it is not a source of investigative data on individuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i-know-where-your-cat-lives |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
