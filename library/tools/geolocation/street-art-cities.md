---
id: street-art-cities
name: Street Art Cities
description: Use when you have a photo of a mural/street-art in the background and want its `geolocation` — a crowdsourced world map of geotagged street artworks with photos.
url: https://streetartcities.com/
category: geolocation
path:
- geolocation
bestFor: Identifying and locating a specific mural or street artwork by browsing a global, geotagged, photo-rich map of urban art.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse the map and artwork photos; no account needed. An optional "Supporter" tier funds the community but isn't required for OSINT use.
opsec: passive
opsecNote: You browse a public community map, not the target — fully passive, nothing about your subject is exposed. Standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-driven urban-art platform; entries are user-submitted with photos and locations. Coverage and accuracy depend on contributors, so confirm a match against street-level imagery.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- StreetArtCities
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- street-art
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Street Art Cities

> The world's largest crowdsourced map of geotagged street art — tens of thousands of murals with photos, useful for pinning down where a distinctive artwork in a photo was taken.

## When to use
Your image or video shows a mural, graffiti, or distinctive street artwork in the background and you want to geolocate it. Street Art Cities maps documented artworks by city and exact location with photos, so a recognisable piece can be matched to a specific wall/coordinate — a strong geolocation lead when generic building features aren't enough. Browse by city if you already suspect a region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://streetartcities.com/ and go to the map, or pick a candidate city.
2. Browse geotagged artworks and compare their photos to the mural in your image.
3. When you find a match, open its entry for the exact location/coordinates, artist, and additional photos confirming the spot.
4. Verify against street-level/satellite imagery at those coordinates (murals can be repainted or removed).
5. Pivot: a confirmed `geolocation` anchors the rest of your geolocation; the artist/city can narrow further if the exact piece isn't listed.

## Inputs → Outputs
- **In:** an `image` of a mural/artwork (optionally a suspected city/`geolocation`)
- **Out:** the artwork's mapped `geolocation` (coordinates, city, artist) when documented
- **Empty/negative result looks like:** no matching artwork — the piece isn't in the community database (much street art is undocumented, and murals get painted over), so absence doesn't rule out a location; fall back to feature-based geolocation.

## Gotchas & OpSec
- Not a reverse-image search: you browse and match by eye; it won't identify a mural from an uploaded photo automatically.
- Coverage is contributor-dependent — strong in art-active cities, sparse elsewhere; entries can be outdated as art changes.
- Always confirm a matched location against independent imagery before treating it as fixed.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[bellingcat-openstreetmap-search]]` and `[[geohints]]` — Street Art Cities pins an exact spot from a distinctive mural; those narrow location from generic infrastructure when no artwork is visible.

## Trust & verifiability
`trust: community` — crowdsourced, photo-backed entries. A photo match plus consistent street-level imagery is strong; treat an unconfirmed single entry as a lead and verify the coordinates independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | street-art-cities |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
