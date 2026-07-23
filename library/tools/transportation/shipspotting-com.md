---
id: shipspotting-com
name: ShipSpotting.com
description: Use when you have a vessel `name`/IMO and want photos and sighting history — returns dated, often geolocated ship photographs and vessel details.
url: https://www.shipspotting.com/
category: transportation
path:
- transportation
bestFor: Finding photographs and historical sightings of a specific vessel by name or IMO number.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free community photo database; viewing and searching need no account (uploading requires registration).
opsec: passive
opsecNote: "You're browsing a public photo archive, not contacting any subject — passive. ShipSpotting logs visitors; use a sock-puppet session for sensitive research. Photo dates/locations are contributor-supplied and can be approximate or mislabeled, so treat a single sighting as a lead, not a fix."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known community ship-photo database featured in the Bellingcat toolkit; photos are authentic contributor uploads, but metadata (date/place) quality depends on the uploader.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ship-spotting
- shipspotting-live-ais
aliases:
- ShipSpotting
- shipspotting.com
tags:
- bellingcat-toolkit
- transport
- vessels
- maritime
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# ShipSpotting.com

> A community archive of vessel photographs: search a ship by name or IMO and get contributor photos — many dated and located — that document where and when it was seen.

## When to use
You have a vessel identifier — its `name` or IMO number (loosely a maritime "plate") — and want visual confirmation and sighting history: what the ship looks like, its markings/flag, and dated photos placing it in specific ports over time. Complements live AIS tracking with a historical, human-verified photo record. Maritime OSINT, so low direct missing-persons relevance, though it can place a vessel (and by extension people/cargo) at a time and place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.shipspotting.com/ and search by vessel `name` or IMO number.
2. Browse the photo gallery for that vessel; open individual photos for the contributor's date, location, and notes.
3. Read the vessel-detail page: type, flag, IMO/MMSI, dimensions, and name history (ships get renamed/reflagged).
4. Build a rough movement/appearance timeline from dated photos; note markings for cross-identification.
5. Cross-check sightings against live AIS ([[shipspotting-live-ais]]) and vessel registries.

## Inputs → Outputs
- **In:** vessel `name`/IMO (as `vehicle-plate`)
- **Out:** dated, often located `image`s of the vessel (`geolocation`), vessel details and name history
- **Empty/negative result looks like:** no photos — the vessel is small/obscure, or hasn't been photographed by contributors; absence isn't proof it doesn't exist (check registries by IMO).

## Gotchas & OpSec
- Photo date/location metadata is **contributor-supplied** — verify against other sources before treating a sighting as fact.
- Ships are frequently renamed/reflagged; always anchor identification to the IMO number, not the current name.
- Coverage skews to ports and vessels that enthusiasts photograph; commercial/naval coverage varies.

## Overlaps ("do both")
- Pairs with live AIS trackers ([[shipspotting-live-ais]], [[ship-spotting]]) — ShipSpotting gives the historical, photo-verified record while AIS gives real-time position; combine to confirm a vessel's identity and track.

## Trust & verifiability
`trust: community` — a genuine community photo archive; images are authentic, but sighting metadata varies in quality, so corroborate dates/locations and identify by IMO before relying on a photo.
