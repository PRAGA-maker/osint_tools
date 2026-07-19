---
id: bhuvan
name: Bhuvan
description: Use when you have a `geolocation` in India and want satellite/aerial imagery and thematic map layers — returns ISRO earth-observation imagery and geospatial data.
url: https://bhuvan.nrsc.gov.in/home/index.php
category: image-video-face
path:
- image-video-face
bestFor: ISRO's Indian geoportal — high-detail satellite imagery and thematic map layers for locations across India.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- image
status: live
pricing: freemium
costNote: Free to browse the map viewer and many layers; some datasets and downloads require a free registration. Run by India's National Remote Sensing Centre (ISRO).
opsec: passive
opsecNote: Viewing satellite/map imagery is passive and reveals nothing about your subject. Registering to download data creates an account with a government body; use appropriate discretion.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official ISRO/NRSC (Government of India) earth-observation platform; the imagery is authoritative government remote-sensing data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ISRO Bhuvan
- NRSC Bhuvan
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- india
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Bhuvan

> ISRO's Indian geoportal — a Google-Earth-style viewer backed by India's own satellites, often with better detail and thematic layers for Indian territory than Western imagery providers.

## When to use
Your investigation touches a location in India — a village, address, terrain, or route — and you need satellite/aerial imagery or thematic geospatial layers (land use, administrative boundaries, disaster data) for that `geolocation`. Bhuvan frequently shows Indian areas at detail and recency that complements or beats Google Earth for the subcontinent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://bhuvan.nrsc.gov.in/ and open the map viewer (Bhuvan 2D/3D or a thematic portal).
2. Navigate to the Indian location of interest by search or by panning/zooming.
3. Toggle imagery and thematic layers (satellite, terrain, land use, admin boundaries) to build context around the point.
4. Use measurement/coordinate tools to read exact lat/long and distances.
5. For downloads or specialized datasets, create a free account where prompted.
6. Pivot: confirmed coordinates → cross-check against Google Earth/Street View and local records; terrain/land-use context → search planning for a ground location.

## Inputs → Outputs
- **In:** a `geolocation` in India (place name or coordinates), or an `image` scene to place
- **Out:** satellite/aerial `image`ry, thematic map layers, and precise `geolocation` (coordinates) for Indian territory
- **Empty/negative result looks like:** sparse or lower-resolution coverage outside India, or no thematic layer for a niche dataset — Bhuvan's strength is India; for locations elsewhere, use a global imagery provider.

## Gotchas & OpSec
- India-focused: best-in-class for the subcontinent, thinner elsewhere. Don't expect global parity with Google Earth.
- Some layers/downloads are gated behind free registration and portal performance can be slow.
- Imagery dates vary by layer; check capture dates before treating a scene as current.
- OpSec: passive viewing; only downloads create a footprint (a government-site account).

## Overlaps ("do both")
- Complements global imagery/Street View tools — use Bhuvan for authoritative, detailed Indian imagery and a Western provider for cross-verification and street-level views.

## Trust & verifiability
`trust: trusted` — official ISRO/NRSC government imagery; the earth-observation data is authoritative, though always note the capture date of the specific layer you cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bhuvan |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, image → geolocation, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
