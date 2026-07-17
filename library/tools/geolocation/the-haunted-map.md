---
id: the-haunted-map
name: The Haunted Map
description: Use when you have a `geolocation` and want to check whether it coincides with a catalogued "haunted"/reported-sighting location — a niche crowd map, not an investigative geolocation tool.
url: https://www.google.com/maps/d/viewer?mid=1PdxFMPxgBmXdjMsusb-O2k074ok&hl=en&ll=45.17177063794067%2C7.41628581553573&z=5
category: geolocation
path:
- geolocation
bestFor: Cross-referencing a coordinate/place against a global crowd-sourced index of reportedly haunted or anomalous locations.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: A free public Google My Maps layer; no account needed to view.
opsec: passive
opsecNote: Hosted on Google My Maps; viewing is passive and reveals nothing about your subject. Google logs the map view under your session only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A single-author crowd-sourced novelty map built on data from ghostresearchinternational.com; entries are anecdotal and unvetted. Not authoritative for any factual claim.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Haunted Map
tags:
- maps-geolocation-and-transport
- anomalies-lost-places
- niche
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# The Haunted Map

> A crowd-sourced Google My Maps layer of reportedly haunted locations worldwide — a novelty/context resource, not a geolocation-solving tool.

## When to use
Rarely, and only for context: you have a `geolocation` or place name that comes up in a case tied to "paranormal tourism," urban-exploration, or a location folklore angle, and you want to see whether it appears in this catalogue of reportedly haunted/anomalous sites. It can surface the informal name or lore attached to an abandoned/anomalous place, which occasionally helps interpret social-media posts that reference such spots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map URL in a browser.
2. Pan/zoom to your area of interest, or use the map's search box to jump to a place.
3. Click a pin to read its label and the anecdotal note attached (site name, reported activity, sometimes an address).
4. Treat any place name it gives you as a lead only, then confirm the real coordinates/address in a proper mapping tool.
5. Pivot: a place name → standard maps/geocoding and street-level imagery for the actual `address`/`geolocation`.

## Inputs → Outputs
- **In:** `geolocation` (or place name)
- **Out:** matched pins with an informal location name, occasional `address`, and anecdotal notes
- **Empty/negative result looks like:** no pins near your coordinate — the vast majority of locations are not on the map; absence means nothing.

## Gotchas & OpSec
- Content is anecdotal and unverified — never cite it as fact; use only as a naming/lore lead.
- Coverage is sparse and clustered around where contributors happened to add pins.
- Passive; nothing reaches your subject.

## Overlaps ("do both")
- Pairs with mainstream mapping/geocoding and imagery tools — this map at most hands you a name or rough spot; a real geocoder gives you the verified `geolocation`.

## Trust & verifiability
`trust: unverified` — a hobbyist crowd map of anecdotal sightings. Fine as flavor/context, worthless as evidence; corroborate any location in an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-haunted-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
