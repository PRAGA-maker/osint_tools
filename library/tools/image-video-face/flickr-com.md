---
id: flickr-com
name: flickr.com
description: Use when you want to browse geotagged Flickr photos on a map to place a person or scene — a duplicate listing pointing at Flickr's map view.
url: http://www.flickr.com/map/
category: image-video-face
path:
- image-video-face
bestFor: Map-based browsing of geotagged Flickr photos (duplicate of the canonical Flickr / Flickr Map entries).
selectorsIn:
- geolocation
- username
selectorsOut:
- image
- geolocation
- metadata
status: live
pricing: freemium
costNote: Free to browse; a free account/API key unlocks more.
opsec: passive
opsecNote: Public map browsing looks like normal web traffic; logging in ties activity to an account. Use a sock puppet for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Flickr URL; this is a harvested duplicate of the main Flickr listing pointing specifically at the world map view. Prefer the canonical entries.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
aliases:
- Flickr (map)
tags:
- flickr
- geolocation
source: uk-osint
lastVerified: ''
enrichment: full
---

# flickr.com

> A harvested duplicate of Flickr, linking to its world map view of geotagged photos.

## When to use
You have a `geolocation` (or a `username` whose photostream you want to place geographically) and want to browse public, geotagged Flickr images on a map. Functionally the same as the canonical `[[flickr]]` and `[[flickr-map]]` entries — use those for full guidance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.flickr.com/map/ (redirects to the current Flickr map).
2. Pan/zoom to the area of interest, or filter by a member's photos.
3. Click clustered pins to open geotagged photos and their info panels.
4. Read capture date, EXIF `metadata`, and exact map `geolocation`.
5. Pivot: confirm scene/location against mapping/Street View; reuse any `username` elsewhere.

## Inputs → Outputs
- **In:** `geolocation` / `username`
- **Out:** `image`, `geolocation`, `metadata`.
- **Empty/negative result looks like:** few or no pins in the area, or pins all from unrelated accounts.

## Gotchas & OpSec
- This is a duplicate entry; prefer `[[flickr]]` / `[[flickr-map]]` to avoid divergence.
- OpSec: **passive** browsing; geotags can be spoofed by uploaders.

## Overlaps ("do both")
- Same data as `[[flickr-map]]`; pairs with `[[flickr-hive-mind]]` for tag/keyword aggregation.

## Trust & verifiability
`trust: trusted` — first-party Flickr platform data; flagged as a duplicate of the canonical Flickr entries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flickr-com |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, username → image, geolocation, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
