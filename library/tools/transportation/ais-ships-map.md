---
id: ais-ships-map
name: ShipFinder (AIS Ships Map)
description: Use when you have a vessel `name`/identifier or a `geolocation` and want a ship's live position and movement history — returns current coordinates and voyage track.
url: https://www.shipfinder.com/Monitor/Index
category: transportation
path:
- transportation
bestFor: Locating a named commercial vessel live on an AIS map or seeing which ships are near a coordinate.
selectorsIn:
- name
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: A live AIS map is browsable for free; per-vessel tracking, satellite AIS, alerts and long history are gated behind paid plans (free tier limited to a single tracked vessel).
opsec: passive
opsecNote: You query a public vessel-tracking site, not the vessel or its crew; nothing reaches the subject. Browse over a sock-puppet if you register for the free tier.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial AIS aggregator; positions come from crowd-sourced terrestrial receivers plus satellite feeds, so coverage is strong on shipping lanes but sparse mid-ocean, and AIS itself can be switched off or spoofed by a vessel.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ShipFinder
- shipfinder.com
- AIS Ships Map
tags:
- maritime
- ais
- vessel-tracking
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# ShipFinder (AIS Ships Map)

> A live AIS vessel-tracking map — find a named ship's current position and recent track, or see what is moving near a set of coordinates.

## When to use
Your case touches a vessel: a subject reportedly aboard a named ship, a container/tanker of interest, or activity near a specific port or coordinate. ShipFinder plots ships broadcasting AIS onto a live map, so you can locate a vessel by `name` (or MMSI/IMO), read its current `geolocation`, and follow where it has been. Also useful in reverse — click a point at sea to see which vessels are there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.shipfinder.com/Monitor/Index; the live map loads with current AIS contacts.
2. Search the vessel by name, MMSI or IMO, or pan/zoom to the `geolocation` of interest.
3. Click a vessel marker to read its current position, speed, heading and reported destination; the free tier lets you follow one vessel — deeper history/alerts need a paid plan.
4. Pivot: take the vessel identity/owner into a maritime registry, and the destination port/timeline into other transportation and location tools.

## Inputs → Outputs
- **In:** vessel `name`/MMSI/IMO, or a `geolocation` to look around
- **Out:** live `geolocation` (position, course, speed), reported destination, recent track
- **Empty/negative result looks like:** the vessel isn't on the map — it may be out of receiver range, have AIS switched off, or be spoofing; absence is not proof it is not at sea.

## Gotchas & OpSec
- Human-in-the-loop: none to view the map; a free account (single tracked vessel) unlocks slightly more, most features are paywalled.
- OpSec: passive — you never contact the ship or crew.
- Data caveat: AIS can be legally turned off, delayed, or falsified; mid-ocean coverage depends on satellite feeds you may not have on the free tier. Corroborate with a second AIS source.

## Overlaps ("do both")
- Pairs with other AIS/vessel trackers because terrestrial-receiver coverage differs by provider — a ship missing here may show on another map, and cross-checking catches AIS spoofing.

## Trust & verifiability
`trust: community` — a commercial aggregator of crowd-sourced and satellite AIS; positions are generally reliable on busy lanes but must be corroborated, since AIS is self-reported by the vessel and can be manipulated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
