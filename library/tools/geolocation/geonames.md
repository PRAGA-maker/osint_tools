---
id: geonames
name: GeoNames
description: Use when you have a place name, postal code, or coordinate and need to resolve it to canonical lat/long, admin region, or nearby place names.
url: http://www.geonames.org
category: geolocation
path:
- geolocation
bestFor: 'Authoritative gazetteer: resolve place names/postal codes to coordinates and administrative hierarchy, and reverse-geocode.'
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free, CC-licensed data and a free web API (register a username; rate-limited). Premium/commercial servers available.
opsec: passive
opsecNote: Queries a public gazetteer; no contact with the target. API calls go under your registered username.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: GeoNames is a long-established, widely-used open geographical database (11M+ place names) under Creative Commons; a de facto standard gazetteer.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases: []
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# GeoNames

> A free, Creative-Commons gazetteer of 11M+ place names worldwide — resolves names, postal codes, and coordinates to canonical locations and administrative regions.

## When to use
You have an ambiguous or partial `address`/place name (a town from a witness statement, a postal code, a foreign locality) and need to pin it to a canonical `geolocation` and admin hierarchy (country → state → county), or reverse-geocode a coordinate to the nearest named places. Excellent for disambiguating duplicate town names and for international locations consumer maps handle poorly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.geonames.org and use the search box for a place name or postal code.
2. Read the result: coordinates, feature class, population, admin parents, and alternate names.
3. For programmatic use, register a free username and call the REST API (search, findNearby, postalCodeSearch, etc.).
4. Pivot: take the resolved `geolocation` into `[[google-maps]]`, `[[dualmaps]]`, or `[[esri]]` for imagery and analysis.

## Inputs → Outputs
- **In:** place `address`/name, postal code, or `geolocation` (for reverse lookup).
- **Out:** canonical `geolocation` (lat/long), `address`/admin hierarchy, alternate names.
- **Empty/negative result looks like:** no match or many same-named hits — narrow by country/admin code, or check alternate spellings.

## Gotchas & OpSec
- Human-in-the-loop: none for web search; API needs a free registered username and is rate-limited.
- Coordinates are place centroids, not exact street addresses — combine with a precise geocoder for door-level work.
- OpSec: passive; only GeoNames sees your queries.

## Overlaps ("do both")
- Pairs with `[[esri]]`/`[[google-maps]]` geocoders — GeoNames excels at place-name disambiguation and international/admin context.

## Trust & verifiability
`trust: trusted` — long-established open gazetteer used widely as a reference dataset; data is CC-licensed and documented.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geonames |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
