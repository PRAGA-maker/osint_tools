---
id: geovisual-search
name: GeoVisual Search
description: Use when you want to find places that look like a chosen feature in satellite imagery (visual similarity search across the globe).
url: https://search.descarteslabs.com
category: geolocation
path:
- geolocation
bestFor: Visual-similarity search over satellite imagery — pick a feature, find lookalike sites worldwide.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Was a free research demo from Descartes Labs; the public demo has been unreliable/retired and may not load.
opsec: passive
opsecNote: Operates on public satellite imagery; no target contact. If the demo is offline, it cannot be used.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: GeoVisual Search was a real Descartes Labs research demo for satellite visual-similarity search; the company pivoted and the public demo's availability is uncertain. Treat current status as unverified.
missingPersonsRelevance: medium
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Descartes Labs GeoVisual Search
tags:
- geolocation
source: metaosint
lastVerified: ''
enrichment: full
---

# GeoVisual Search

> A Descartes Labs research demo for satellite visual-similarity search: click a feature (e.g. a wind turbine, a particular building shape) and it surfaces visually similar locations across imagery.

## When to use
You have an `image`/feature visible in satellite imagery — a distinctive structure, terrain pattern, or object near a last-known location — and want to find other places that look like it (to test where a similar scene in a photo might be). Useful for pattern-matching landscapes, less so for street-level person work. Note the public demo's availability is uncertain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try https://search.descarteslabs.com (the demo may be offline or limited).
2. Navigate the satellite map to a feature, select/click it as the query.
3. Review surfaced visually-similar `geolocation` candidates.
4. Pivot: verify any candidate in `[[google-earth-pro]]` / `[[earthexplorer]]`; for photo-based location use `[[geospy]]`.

## Inputs → Outputs
- **In:** a satellite-imagery feature (`image`/`geolocation` patch).
- **Out:** `geolocation` candidates that visually resemble the query.
- **Empty/negative result looks like:** the demo failing to load, or generic features returning too many weak matches.

## Gotchas & OpSec
- Human-in-the-loop: none if it loads; the main risk is the demo being retired.
- Matches aerial/landscape features, not faces or street-level cues — wrong tool for identifying a person.
- OpSec: passive; only public imagery is queried.

## Overlaps ("do both")
- Complements `[[geospy]]` (photo-to-location) — GeoVisual Search works top-down on aerial features; combine to triangulate a region.

## Trust & verifiability
`trust: unverified` — a genuine Descartes Labs research demo, but the company's pivot leaves current availability uncertain; verify the site loads before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geovisual-search |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
