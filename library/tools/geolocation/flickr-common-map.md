---
id: flickr-common-map
name: Flickr Commons Map
description: Use when you have an old/undated `image` or a `geolocation` and want to browse geotagged Flickr Commons archive photos for that place to help identify or place a scene — returns candidate matching historical photos and their `geolocation`.
url: http://www.whatsthatpicture.com/flickr/commons-map.php
category: geolocation
path:
- geolocation
bestFor: Locating historical, copyright-free Flickr Commons archive photographs by place on a world map to assist old-photo identification and scene matching.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tool; no account. Built on the Flickr API over the Flickr Commons (public archive) collection.
opsec: passive
opsecNote: Passive — you browse a public map of institutional archive photos; nothing is sent to or about a living subject. Standard web-request egress only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent project by James Morley (What's That Picture) using the Flickr API and OpenLayers over Flickr Commons; it surfaces institutional archive images, so provenance traces back to named cultural institutions.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Flickr Commons World Map
- What's That Picture Flickr map
tags:
- Maps, Geolocation and Transport
- Social media and photos
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Flickr Commons Map

> A world map of geotagged **Flickr Commons** archive photos (27,000+ images, many pre-1950) — a niche aid for placing or identifying *old* photographs, not current people.

## When to use
You have an undated or unplaced historical `image` (a vintage street, building, or landscape) or a `geolocation` you want to see through archive photography, and you want to browse copyright-free institutional photos tied to that place. It shines for old-photo identification and historical scene-matching; it is **not** a tool for finding a living missing person's current whereabouts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.whatsthatpicture.com/flickr/commons-map.php (a JS/OpenLayers map — allow it to load; the host sometimes blocks headless fetchers, so use a real browser).
2. Pan/zoom to the location of interest; markers cluster geotagged Flickr Commons images by place.
3. Open markers to view the archive photos and their source institution, date and caption.
4. Compare candidate archive images against your unknown `image` (architecture, streetscape, landmarks) to place or date it.
5. Pivot: a source institution + caption feeds deeper archive research; a confirmed `geolocation` feeds mapping tools.

## Inputs → Outputs
- **In:** `geolocation` (map area) and/or an `image` you are trying to place
- **Out:** candidate historical archive photos with their `geolocation`, date and holding institution
- **Empty/negative result looks like:** no markers near the area, or only unrelated eras/scenes — the place isn't represented in Flickr Commons; use a general reverse-image or mapping tool instead.

## Gotchas & OpSec
- Scope is **Flickr Commons** (public cultural-archive collections) — historical and copyright-free, so nearly useless for recent/current imagery.
- The map depends on Flickr's API and the third-party host; if either is down the map won't render.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[flickr-com]]` (search live Flickr more broadly) and general reverse-image search — use those for modern photos, and this map when the image is old and you need archive context by place.

## Trust & verifiability
`trust: community` — an independent hobby/reference project layered over the Flickr API; the underlying photos come from named institutions, so verify any identification against the holding archive's own record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flickr-common-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
