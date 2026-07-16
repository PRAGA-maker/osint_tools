---
id: plates-mania
name: Plates Mania
description: Use when you have a `vehicle-plate` and want user-uploaded photos of the actual vehicle wearing it — returns image, geolocation.
url: http://platesmania.com
category: transportation
path:
- transportation
bestFor: Finding crowd-sourced photos of a specific license plate (and the vehicle/place it was shot) across a large plate-spotting community.
selectorsIn:
- vehicle-plate
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free to search and view. A free account is only needed to upload photos or use some catalog features; no payment involved.
opsec: passive
opsecNote: Searching is a passive read against a public photo community — no notification to any vehicle owner. Do not upload the plate you are investigating; that would publish your interest and add a photo to the very database you are searching.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large volunteer plate-spotting community (user-uploaded photos); coverage and accuracy vary by country and depend on hobbyists, not official records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- PlatesMania
- platesmania.com
tags:
- vehicle
- transportation
- plate-spotting
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Plates Mania

> A global plate-spotting community: search a registration number and see user-uploaded photos of the vehicle actually carrying it, tagged by country and place.

## When to use
You have a `vehicle-plate` and want visual confirmation — a photo of the make/model/colour and condition of the car wearing that plate, and often the city/region and date it was photographed. In a missing-persons or vehicle-trace context it can corroborate a plate against a described vehicle, surface an image you didn't have, or geographically anchor a sighting. Strongest coverage is Russia, ex-USSR, Europe, and Latin America; thinner in the US.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://platesmania.com and select the relevant country (the plate format and gallery are country-scoped).
2. Use the "search by plate number" / gallery search and enter the registration exactly as it appears.
3. Review results: each hit is a user photo of a vehicle with that plate — note the make/model/colour, any visible location/background, and the upload date/region.
4. Pivot: the vehicle `image` corroborates or contradicts your description; the photo's `geolocation` (country/city) anchors a sighting; combine with official plate/VIN registries for ownership (this site does not provide owner identity).

## Inputs → Outputs
- **In:** `vehicle-plate` (registration number, correct country)
- **Out:** `image` (community photos of the vehicle), `geolocation` (country/region where photographed), plus make/model/colour and date
- **Empty/negative result looks like:** no photos for that plate — extremely common for plates outside the site's strong regions (e.g. most US plates). Absence means "no hobbyist photographed it," not that the vehicle doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none to search; account only for uploads.
- OpSec: **passive** for searching. Never upload the target plate.
- This is a hobbyist photo archive, **not** a registry — it returns pictures, not the registered owner's name or address. Coverage is highly uneven by country.

## Overlaps ("do both")
- Do both with an official plate/VIN registry or salvage-auction lookup (`[[copart-auction]]`) — PlatesMania supplies the community photo/geolocation; the registry supplies ownership/title.

## Trust & verifiability
`trust: community` — crowd-sourced photos, timestamped and geotagged by uploaders; verify a critical match against the visible plate in the photo rather than the caption alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plates-mania |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
