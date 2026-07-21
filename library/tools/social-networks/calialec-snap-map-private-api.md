---
id: calialec-snap-map-private-api
name: CaliAlec/snap-map-private-api
description: Use when you have a `geolocation` (coordinates/place) and want the public Snapchat snaps and stories posted there — returns Snap Map media with location, timestamps and thumbnails.
url: https://github.com/calialec/snap-map-private-api
category: social-networks
path:
- social-networks
bestFor: Pulling public Snap Map snaps/stories for a set of coordinates via Snapchat's unofficial map API.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: degraded
pricing: free
costNote: Free, open-source Node.js library; no account or API key required, but you self-host it.
opsec: passive
opsecNote: The library hits Snapchat's public Snap Map endpoints from YOUR IP — no login is used and the posters are not notified, but the requests originate from you, so run it behind a VPN/sock-puppet if you don't want your IP hitting Snap's endpoints.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: unverified
trustNote: Unofficial community wrapper (single-author, minimal commit history) around Snapchat's private Snap Map API; unaffiliated with Snap and liable to break whenever Snap changes its endpoints.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- snap-map-private-api
- Snapchat Snap Map API wrapper
tags:
- snapchat
- open-source
- cli
- geolocation
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# CaliAlec/snap-map-private-api

> A Node.js wrapper over Snapchat's unofficial Snap Map API: give it coordinates and it returns the public snaps and stories people posted at that spot.

## When to use
You have a `geolocation` — a last-known location, an event site, an address — and want to see public Snapchat activity there. Snap Map publishes user snaps/stories geotagged to a place; this library pulls them programmatically for a radius, which can surface eyewitness media, place a subject at a location by time, or reveal what was happening at a scene. Note the input is a *location*, not a username — Snap Map is location-first.

## How to use it (`bestInteractionPattern`: api)
1. Clone the repo (`github.com/calialec/snap-map-private-api`) and install it in a Node.js project (`npm install`).
2. Call its methods: `getPlaylist()` to fetch snaps within a radius of a lat/long, `getPoiPlaylist()` for a specific place/story, and `getSearchCards()` to resolve a location search.
3. Pass the target coordinates (and radius) for the location you're investigating.
4. Read the returned snap objects: media URLs, thumbnails/overlays, durations, timestamps, and localized place titles — build playable URLs from the media metadata.
5. Pivot: timestamps + location build a scene timeline; media can be reverse-image-searched or run for background geolocation cues; recurring nearby stories map local activity.

## Inputs → Outputs
- **In:** `geolocation` (lat/long + radius, or a place/POI)
- **Out:** `geolocation`-tagged Snap Map media (`image`/video snaps) with timestamps, place titles and thumbnails
- **Empty/negative result looks like:** an empty playlist — no public snaps at those coordinates in Snap's current window, or (increasingly common) Snap changed the endpoint and the call errors. An empty result is *not* proof nothing happened there.

## Gotchas & OpSec
- **Unofficial and fragile:** it depends on a private Snap endpoint that changes without notice; expect it to break periodically and check for a maintained fork.
- Snap Map only shows content users chose to make public, and only recent snaps — it's a live window, not an archive.
- OpSec: **passive** toward posters, but the requests come from **your** IP; use a VPN/sock-puppet.

## Overlaps ("do both")
- Pairs with the official Snap Map web view (map.snapchat.com) for manual cross-checking and with reverse-image/EXIF tools to enrich the media it pulls.

## Trust & verifiability
`trust: unverified` — a single-author unofficial wrapper marked `status: degraded` because it rides a private API Snap can change at any time. Treat pulled media as real but verify each snap's location/time against its own metadata and the live Snap Map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | calialec-snap-map-private-api |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
