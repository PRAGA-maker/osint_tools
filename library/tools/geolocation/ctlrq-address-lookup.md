---
id: ctlrq-address-lookup
name: CTLRQ Address Lookup
description: Use when you need to convert between a map pin/coordinates and a street address — drop a pin to get the address, or enter an address to get exact GPS coordinates.
url: https://ctrlq.org/maps/address
category: geolocation
path:
- geolocation
bestFor: Quick reverse-geocoding (pin → address) and forward geocoding (address → coordinates) on a Google map.
selectorsIn:
- geolocation
- address
selectorsOut:
- address
- geolocation
status: unknown
pricing: free
costNote: Free utility (Digital Inspiration / ctrlq.org); no account. Availability of individual ctrlq tools has varied over time.
opsec: passive
opsecNote: Geocoding is computed from map data; it does not contact or notify any person at the address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ctrlq.org (Amit Agarwal / Digital Inspiration) is a reputable utilities site, but its individual tools have come and gone — verify this page still loads before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ctrlq Find Address
- ctrlq.org maps address
tags:
- geospatial-research-and-mapping-tools
- geocoding
- reverse-geocoding
source: awesome-osint
lastVerified: ''
enrichment: full
---

# CTLRQ Address Lookup

> A lightweight geocoding utility on ctrlq.org: drop a pin on a Google map to get the nearest street `address`, or type an `address` to get its exact latitude/longitude.

## When to use
You have a `geolocation` (coordinates, or a spot you can pin from imagery/EXIF) and need the human-readable `address`, or vice versa. Common in missing-persons work after geolocating a photo or a sighting: convert the pin you placed into an address you can canvass, or convert a tip address into coordinates to overlay with other location data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ctrlq.org/maps/address (confirm it loads — ctrlq tools have changed over the years).
2. For reverse geocoding: drag/drop the map marker onto the location to read the nearest address. For forward geocoding: enter the `address` to get its coordinates.
3. Read the returned `address` / lat-long pair.
4. Pivot: feed coordinates into imagery review or your case map; feed the address into people/property search and street-level imagery.

## Inputs → Outputs
- **In:** `geolocation` (map pin / coordinates) or `address`
- **Out:** `address` and/or `geolocation` (the converted counterpart)
- **Empty/negative result looks like:** an ambiguous or "nearest road" address for a rural/featureless pin, or no match for a malformed address — geocoding precision drops where Google's address data is sparse.

## Gotchas & OpSec
- Reverse-geocoded addresses are approximate, snapping to the nearest known address — don't treat the result as the exact building without corroboration.
- ctrlq's individual utilities have been deprecated/moved before; verify the page works rather than assuming.
- OpSec: passive — geocoding queries Google's map data, not the person; nothing reaches the address's occupant.

## Overlaps ("do both")
- Pairs with EXIF/image-geolocation tools (you get coordinates from a photo, then this gives you the address) and with mapping utilities like [[dual-maps]] for visual confirmation of the spot.

## Trust & verifiability
`trust: community` — from a well-regarded utilities publisher, but a thin convenience wrapper around Google geocoding whose availability has fluctuated. Cross-check any address against a primary map (Google/Bing) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ctlrq-address-lookup |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
