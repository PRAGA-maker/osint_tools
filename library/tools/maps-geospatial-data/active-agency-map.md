---
id: active-agency-map
name: Active Agency Map
description: Use when you have a `geolocation` / region and want to see a community-curated Google My Map of agency locations plotted for it — returns `address` / `geolocation` pins.
url: https://www.google.com/maps/d/viewer?mid=1eYVDPh5itXq5acDT9b0BVeQwmESBa4cB
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Reading a shared Google My Maps layer of plotted agency locations as a starting geographic reference.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: A free, publicly viewable Google My Maps custom map; no Google account needed to view.
opsec: passive
opsecNote: Passive read of a shared Google map. Google logs your view under your session/IP; use a clean browser if you do not want the view tied to you. You are not contacting any plotted location, so it is passive toward third parties.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A user-created ("This map was created by a user") Google My Map with no named maintainer or provenance; pins are unverified and may be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-my-maps
aliases:
- Active Agency Map
tags:
- google-my-maps
- custom-map
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Active Agency Map

> A shared, community-built Google My Maps layer plotting agency locations — a quick geographic index you inspect live rather than a verified dataset.

## When to use
You want a ready-made map layer of plotted "agency" locations for a region as a jumping-off point — e.g. to see what is clustered in an area of interest and pull each pin's address/coordinates. Because it is a user-curated custom map, treat it as a lead-generator: open it, read the pins that fall in your area of interest, and verify each independently.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map URL in a browser (a Google My Maps viewer, no login required).
2. Use the layer panel on the left to browse plotted markers, or pan/zoom to your region of interest.
3. Click any pin to read its label, description, and coordinates.
4. Copy the pin's `address`/`geolocation` and confirm it against an authoritative source (official registry, Street View, the agency's own site) before relying on it.
5. Pivot: a confirmed location feeds address- and organisation-lookups; use `[[google-my-maps]]` techniques to export the whole layer as KML if you need the full point set.

## Inputs → Outputs
- **In:** `geolocation` / region of interest
- **Out:** plotted `address` and `geolocation` pins with labels/descriptions
- **Empty/negative result looks like:** the map loads but has no pins in your area, or the map fails to load (the creator may have deleted or restricted it) — fall back to authoritative directories.

## Gotchas & OpSec
- Provenance is unknown — Google explicitly labels it "created by a user." Pins can be inaccurate, outdated, or opinionated; never cite a pin as fact without independent confirmation.
- The map can be edited or removed by its owner at any time; re-verify freshness on each use.
- OpSec: passive read; Google associates the view with your session. Use a clean/sock-puppet browser if attribution matters.

## Overlaps ("do both")
- Pairs with `[[google-my-maps]]` — the same viewer engine; use its export/KML tricks to lift every point out of this layer for bulk processing.

## Trust & verifiability
`trust: community` — an anonymous user-curated custom map with no stated methodology or maintainer; useful as a pointer, not as evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | active-agency-map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
