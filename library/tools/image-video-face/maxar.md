---
id: maxar
name: Maxar (Discover / Xpress)
description: Use when you have a `geolocation` and want to see what high-resolution satellite imagery exists over it and when — returns dated `image` captures (browse free, full imagery paid).
url: https://discover.maxar.com/
category: image-video-face
path:
- image-video-face
bestFor: Discovering the dates and footprints of Maxar's high-resolution satellite imagery over an area — useful for finding when a location was imaged.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: freemium
costNote: Browsing the imagery archive footprints/previews over an area is free (account may be required); ordering or downloading full-resolution imagery is a paid commercial product.
opsec: passive
opsecNote: You query an imagery catalog by area, not a person; nothing about a subject is submitted and no one is alerted. Passive.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maxar is a major commercial satellite operator; imagery and capture metadata are authoritative, but the high-value full-resolution product sits behind a paywall.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Maxar Discover
- Maxar Xpress
- SecureWatch
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Maxar (Discover / Xpress)

> A catalog of one of the world's largest high-resolution satellite archives — draw an area and see which images exist over it and on what dates; previews are browsable, full imagery is a paid product.

## When to use
You have a `geolocation` and need to know whether — and when — high-resolution satellite imagery captured it. Maxar's archive can establish that a place was imaged on specific dates (`image`), which supports chronolocation and change-over-time analysis of a site relevant to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://discover.maxar.com/ (it redirects to Maxar's current imagery portal, e.g. xpress.maxar.com); create an account if prompted.
2. Navigate to or draw an area of interest on the map.
3. Browse the available captures over that footprint, filtered by date.
4. Read the output: the set of dated imagery captures (`image`) covering the area, with previews/thumbnails.
5. Pivot: use capture dates to bracket events; obtain full-resolution imagery via the paid product, or cross-check with free sources (Sentinel/Landsat, Google Earth historical) for the same dates.

## Inputs → Outputs
- **In:** `geolocation` (area of interest)
- **Out:** `image` (dated high-resolution satellite captures / previews over that area)
- **Empty/negative result looks like:** no captures listed for the area/date window — Maxar may not have imaged it then; fall back to other satellite archives.

## Gotchas & OpSec
- **Freemium with a real paywall:** discovering footprints and low-res previews is free, but ordering/downloading full-resolution imagery is a paid commercial transaction — plan around that (partial paywall).
- Archive depth and revisit rate vary by location; some areas are imaged frequently, others rarely.
- OpSec: passive; you query an area, not a person.

## Overlaps ("do both")
- Complements free satellite sources (Sentinel Hub, Google Earth historical imagery): use Maxar to find whether high-res captures exist and when, and the free sources for openly-downloadable imagery on the same dates.

## Trust & verifiability
`trust: trusted` — a leading commercial satellite operator; imagery and capture metadata are authoritative. The limitation is cost/access, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maxar |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
