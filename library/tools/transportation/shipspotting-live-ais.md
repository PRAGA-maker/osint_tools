---
id: shipspotting-live-ais
name: ShipSpotting
description: Use when you have a vessel name/IMO or a ship photo and want vessel identification and imagery — returns ship photos, vessel details, and photographer/location metadata.
url: https://www.shipspotting.com
category: transportation
path:
- transportation
bestFor: Identifying a vessel and finding dated photographs of it, plus the photographer and location behind each shot.
selectorsIn:
- name
- image
selectorsOut:
- image
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free to search and view the photo database; a free account is needed only to upload your own photos.
opsec: passive
opsecNote: Browsing the public photo database is passive and reveals nothing to any subject. Uploading a photo (to seek an ID) is a disclosure — strip your own metadata and use a puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-running community ship-photo database; identifications and captions are contributed by enthusiasts, so vessel IDs are usually reliable but caption details are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- ShipSpotting.com
- ship photo database
tags:
- maritime
- vessel-tracking
- ship-photos
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
relatedTools:
- ship-spotting
- shipspotting-com
---

# ShipSpotting

> A community database of hundreds of thousands of ship photographs with vessel details — the go-to for identifying a boat in an image and finding dated, located pictures of a named vessel.

## When to use
You have a vessel `name`/IMO tied to an investigation (a subject's boat, a ship in a photo, a maritime lead) and want to identify it and find imagery. ShipSpotting lets you search by ship name and browse contributed photos, each captioned with the vessel, and often the date, port/location, and photographer — useful for confirming a vessel's appearance over time, placing it at a location on a date, or reverse-identifying a ship from a photo by matching hull/livery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.shipspotting.com and search by ship `name` (or browse galleries).
2. Open matching photos: read the caption for vessel details, the date, the port/location, and the photographer's name.
3. To identify an unknown vessel from your own `image`, match distinctive features (name on hull, funnel livery, type) against the database.
4. Pivot: a photo's date + location gives a `geolocation`/timeline datapoint; for live position, hand the vessel/IMO to a dedicated AIS tracker (MarineTraffic/VesselFinder); a photographer name can be a further lead.

## Inputs → Outputs
- **In:** vessel `name`/IMO, or an `image` to identify.
- **Out:** ship photos (`image`), vessel details, capture date and port (`geolocation`), photographer, possible `metadata-exif` in originals.
- **Empty/negative result looks like:** no photos for the vessel — small/private craft are often unphotographed here. Absence doesn't mean the vessel doesn't exist.

## Gotchas & OpSec
- It's a photo archive, not a live tracker — despite the "Live AIS" label, use MarineTraffic/VesselFinder for real-time position.
- Captions are enthusiast-contributed; dates/locations are usually good but unverified — corroborate for anything critical.
- Photo timestamps reflect when the shot was taken/uploaded, not necessarily current status.

## Overlaps ("do both")
- Pair with AIS trackers (MarineTraffic/VesselFinder) for live position and with vessel registries for ownership; combine with reverse-image search on a ship photo.

## Trust & verifiability
`trust: community` — a reputable enthusiast archive. Vessel identifications are generally solid; treat caption metadata as leads and verify dates/locations against AIS history or registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shipspotting-live-ais |
| category | transportation |
| selectorsIn → selectorsOut | name, image → image, geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
