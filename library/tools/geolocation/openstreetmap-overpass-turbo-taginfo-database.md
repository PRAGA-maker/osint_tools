---
id: openstreetmap-overpass-turbo-taginfo-database
name: OpenStreetMap (Overpass Turbo) TagInfo database
description: Use when you have a `geolocation` clue (a described object — kiosk, pylon, bench type) and want the exact OSM tag/key to query in Overpass Turbo — returns tag names, usage stats, and value distributions.
url: https://taginfo.openstreetmap.org/tags
category: geolocation
path:
- geolocation
bestFor: Finding the correct OpenStreetMap tag/key for an object so you can build an accurate Overpass Turbo query.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official OSM project; no account. Open data (ODbL).
opsec: passive
opsecNote: You are browsing OSM tag statistics, not querying anything about a subject — fully passive and leaks nothing about your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official OpenStreetMap project (taginfo) maintained by the OSM community; the authoritative reference for how tags are actually used across the OSM database.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- overpass-turbo
- open-street-map
- openstreetmap
- openstreetmap-2
- openstreetmap-nominatim
- whodidit
aliases:
- OSM taginfo
- taginfo.openstreetmap.org
tags:
- openstreetmap
- overpass
- geolocation
- map-tags
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# OpenStreetMap (Overpass Turbo) TagInfo database

> The OSM tag dictionary: look up which key/value actually maps a real-world object (a specific bollard, kiosk, power tower, shop type) so your Overpass Turbo geolocation query hits the right features.

## When to use
You are geolocating a photo and have spotted a distinctive mappable object — a particular bench, a power pylon, a phone box, a shop chain, a fire hydrant style — and you want to find every such feature in an area via Overpass Turbo. But Overpass only works if you know the exact OSM tag. TagInfo tells you the correct `key=value`, how common it is, its geographic distribution, and related tags — turning "that odd blue kiosk" into a queryable `amenity=*` / `shop=*` filter.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://taginfo.openstreetmap.org/ and search for the object or a candidate keyword (e.g. "pylon", "kiosk", "bollard").
2. Read the matching keys/tags: counts (how widely used), value distributions, and a map of where the tag appears — high usage means OSM likely has your object mapped.
3. Copy the exact `key=value` into an Overpass Turbo query (see `[[overpass-turbo]]`) bounded to your candidate area.
4. Run the Overpass query to enumerate every matching feature, then compare against the photo to narrow the location.
5. Pivot: a confirmed unique feature match fixes the `geolocation`, which then feeds street-level imagery and sun/shadow chronolocation.

## Inputs → Outputs
- **In:** a described real-world object / keyword (a `geolocation` clue from imagery).
- **Out:** the correct OSM tag(s), usage counts, value lists, and geographic distribution — enabling a precise Overpass query and a refined `geolocation`.
- **Empty/negative result looks like:** no tag matches, or the tag is barely used — the object may not be systematically mapped in OSM; fall back to visual landmarks and other map layers.

## Gotchas & OpSec
- TagInfo tells you how a tag is *used*, not whether your specific object is mapped in the target area — verify coverage per region (OSM density varies wildly by country).
- Tagging conventions differ locally; check the value distribution and the OSM wiki before trusting a rare tag.
- Passive — it's reference data; the actual geolocation query happens in Overpass.

## Overlaps ("do both")
- Inseparable from `[[overpass-turbo]]` — TagInfo finds the tag, Overpass finds the features. Combine with street-level imagery to confirm the visual match.

## Trust & verifiability
`trust: trusted` — the official OSM taginfo service over open community data. Usage statistics are authoritative for OSM itself; remember they describe the map, which is a crowd-sourced model of reality, not reality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openstreetmap-overpass-turbo-taginfo-database |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
