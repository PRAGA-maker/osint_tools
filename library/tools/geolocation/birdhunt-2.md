---
id: birdhunt-2
name: BirdHunt
description: Use when you have a `geolocation`/`address` and want tweets posted from or tagged near that spot on a map — returns social-profile handles and their post locations.
url: https://birdhunt.huntintel.io/
category: geolocation
path:
- geolocation
bestFor: Finding geotagged (or location-inferred) tweets around a specific point/radius and mapping them for location-based Twitter/X OSINT.
selectorsIn:
- geolocation
- address
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: freemium
costNote: Free core location search; some advanced query options are paywalled. Practical usefulness is throttled by how little location data Twitter/X still exposes to external tools.
opsec: passive
opsecNote: You query a third-party front-end for public tweets around a location; you never contact any account, so it is passive. Standard operator logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Made by HuntIntel (Louis Tomos Evans, Cardiff), listed in OSINT tool directories; a legitimate community tool, but its data depends entirely on Twitter/X's increasingly restricted location search.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BirdHunt
- birdhunt.huntintel.io
- birdhunt.info
tags:
- twitter
- geolocation
- location-search
source: osintambition-social
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- huntel-io
- instahunt-2
---

# BirdHunt

> A map-based tool for finding tweets by location — enter a point and radius and it surfaces geotagged (and location-inferred) tweets, plotting who posted from an area.

## When to use
You have a `geolocation` or `address` (a coordinate, place or radius) and want to see Twitter/X activity there — eyewitness posts around an incident, tweets from a specific venue, or a subject's posts if they geotag. BirdHunt uses Twitter's geocoded search to find tweets within a distance of a lat/lng, including some where the location is inferred from profile data rather than an explicit tag. The payoff is posting `social-profile`s and their `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://birdhunt.huntintel.io/.
2. Set the location (search a place or drop a point) and a search radius.
3. Use "advanced options" to add keyword/date filters and narrow the search (some options are paywalled).
4. Run it; review results on the map, click through to tweets, and note handles and locations.
5. Pivot: a handle feeds full Twitter/X profile OSINT; a location cluster feeds mapping and local-source work.

## Inputs → Outputs
- **In:** `geolocation`/`address` (+radius, optional keyword/date)
- **Out:** `social-profile` (posting handles), `geolocation` (post/estimated locations)
- **Empty/negative result looks like:** few or no results — increasingly the norm, because X's API restrictions have sharply cut the geotagged/location-inferred tweets any third party can retrieve. Treat a hit as a bonus and absence as expected.

## Gotchas & OpSec
- **Degraded by X's API lockdown:** the tool is fine, but the data pool it draws from is a shrinking fraction of tweets; don't conclude "no activity" from an empty map.
- Location can be inferred (from profile), not GPS-precise — verify before trusting a post's placement.
- Advanced filters are paywalled; core search is free.

## Overlaps ("do both")
- Pairs with `[[one-million-tweet-map]]` and other Twitter geo/advanced-search tools — run more than one, since each queries X differently and coverage of geotagged posts is patchy.

## Trust & verifiability
`trust: community` — a legitimate community tool, but wholly dependent on X's restricted location data; confirm any post's location from its content and the account, not the map marker alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | birdhunt-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
