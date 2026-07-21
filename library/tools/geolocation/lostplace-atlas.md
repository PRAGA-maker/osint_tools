---
id: lostplace-atlas
name: Lostplace-Atlas
description: Use when you have a `geolocation` (or an image of an abandoned site) in Germany/Europe and want to identify or cross-reference it — returns catalogued abandoned-place `geolocation`s.
url: https://www.google.com/maps/d/viewer?mid=1yRkY_mc-IpSVTfQgR3G6Pvjno3w&hl=en_US&ll=36.86911339765801%2C22.7511350249344&z=4
category: geolocation
path:
- geolocation
bestFor: Cross-referencing photos of abandoned/derelict "lost places" against a crowd-mapped atlas, mainly in Germany and Europe.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free crowd-curated Google My Maps layer; no account needed to view.
opsec: passive
opsecNote: Viewing a public Google My Map is passive. It is hosted on Google Maps, so your view is subject to normal Google logging — use a sock-puppet Google session if that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-maintained Google My Maps layer; pin locations are user-contributed and unverified, so treat any match as a candidate to confirm on satellite/street imagery.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Lostplace atlas
- lost places map
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
- urbex
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Lostplace-Atlas

> A crowd-mapped Google My Maps layer of abandoned and derelict sites ("lost places"), concentrated in Germany and wider Europe — a reference for geolocating urbex-style photos.

## When to use
You have a photo of an abandoned building, factory, hospital, bunker, or derelict site (a common backdrop in urban-exploration and some missing-persons imagery) and need to identify where it is, or you have a rough `geolocation` and want to know which abandoned sites are nearby. Matching a photographed ruin to a catalogued pin can pin down a location that has no street address and doesn't appear on normal maps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map link (a Google My Maps "Lostplace-Atlas" layer).
2. Pan/zoom to your area of interest, or scan the region where you suspect the photo was taken.
3. Open individual pins to read their descriptions/photos and compare architectural detail against your image.
4. When a pin looks like a match, confirm it independently on Google Earth/Street View or satellite imagery before relying on it.
5. Pivot: a confirmed `geolocation` feeds chronolocation (sun/shadow, `[[earth]]` weather), satellite-imagery archives, and local-news/records searches for the site.

## Inputs → Outputs
- **In:** `geolocation` (area to scan) and/or an `image` of an abandoned site
- **Out:** catalogued abandoned-place pins with `geolocation` and descriptions → candidate location matches
- **Empty/negative result looks like:** no nearby pins or no matching site — the atlas is incomplete and Germany/Europe-weighted, so a miss means "not catalogued here," not "not an abandoned site."

## Gotchas & OpSec
- **Crowd-sourced and unverified:** pins are user-added; some are approximate, outdated, or wrong — always confirm on independent imagery.
- Coverage is heavily Germany/Europe-centric and patchy elsewhere.
- Owner-dependent: as a single user's Google My Map, it could be edited or removed by its creator at any time.

## Overlaps ("do both")
- Pairs with satellite/Street View and chronolocation tools (`[[earth]]`) — this suggests *which* ruin; those confirm the exact spot and the time-of-day/weather in the photo.

## Trust & verifiability
`trust: unverified` — a helpful community atlas, but every pin is user-contributed; treat a match as a candidate and verify it against authoritative imagery before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lostplace-atlas |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
