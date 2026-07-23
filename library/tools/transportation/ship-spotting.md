---
id: ship-spotting
name: Ship Spotting
description: Use when you have a vessel `name` or IMO/registration and want dated, geolocated photographs of it — returns `image`, `geolocation`, and sighting history.
url: https://shipspotting.com
category: transportation
path:
- transportation
bestFor: Finding community-submitted, dated and located photographs of a specific ship to confirm its appearance, movements, and history.
selectorsIn:
- name
- vehicle-plate
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free to search and view photos; a free account is only needed to upload.
opsec: passive
opsecNote: Browsing the public photo database is passive and reveals nothing about your subject. Photographer names and captions are public user content — treat them as leads.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running enthusiast ship-photography community; photos and metadata are user-contributed, so dates/locations are as reliable as the submitter.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- shipspotting.com
tags:
- maritime
- vessel-photos
source: metaosint
lastVerified: '2026-07-23'
relatedTools:
- shipspotting-com
- shipspotting-live-ais
---

# Ship Spotting

> A large community archive of ship photographs, searchable by vessel name and IMO — the visual counterpart to AIS tracking, showing what a ship looked like and where it was, when.

## When to use
You have a vessel `name`, IMO number, or callsign and want photographic evidence: confirm a ship's identity and appearance, place it at a port on a date (from a dated, located photo), or reconstruct part of its history and name changes. Complements live AIS tools — AIS says where a ship is now; ShipSpotting shows where it has visibly been.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shipspotting.com and search by vessel name or IMO number.
2. Open the matching vessel gallery; each photo carries a date, location, and photographer where provided.
3. Read the metadata: capture location (`geolocation`), date, and any noted name/flag changes across photos.
4. Pivot: an IMO number feeds registry and AIS lookups; a dated port sighting corroborates a movement timeline; the photo itself feeds reverse-image search.

## Inputs → Outputs
- **In:** vessel `name`, IMO, or callsign (`vehicle-plate`-style identifier)
- **Out:** `image` (photos), `geolocation` (capture locations), sighting dates and history
- **Empty/negative result looks like:** no photos for that vessel (small/obscure craft are under-represented) — absence of photos is not absence of the ship.

## Gotchas & OpSec
- Photo location/date are submitter-reported and can be wrong or approximate; corroborate with AIS or registry data.
- Ships change names and flags; search by IMO (which is permanent) when the name is ambiguous.
- OpSec: **passive** — a public photo archive; browsing exposes nothing.

## Overlaps ("do both")
- Pairs with `[[shipspotting-live-ais]]` and MarineTraffic/VesselFinder — AIS gives current/recent position and IMO; ShipSpotting gives the visual, historical record.

## Trust & verifiability
`trust: community` — a reputable long-standing community archive; the images are strong evidence, but treat user-entered dates/locations as claims to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ship-spotting |
| category | transportation |
| selectorsIn → selectorsOut | name, vehicle-plate → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
