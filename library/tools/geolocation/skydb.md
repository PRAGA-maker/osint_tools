---
id: skydb
name: SKYDB
description: Use when you have an `image`/`geolocation` clue featuring a tall building and want to identify it — returns building height, city, year, developer and photos from a global skyscraper database.
url: https://www.skydb.net/
category: geolocation
path:
- geolocation
bestFor: Identifying a skyscraper or tall building from a skyline/photo and pulling its location, height, and details for geolocation confirmation.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Basic exploration/search is free; full database access, consulting, and API are paid memberships. The free tier is usually enough to identify a building and read core details.
opsec: passive
opsecNote: Passive reference lookup — you search a public building database; no target is touched or notified. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, continuously updated tall-buildings database (~177k records) with expert-verified entries and source drill-down; core facts (height, location, year) are well-sourced, though some records vary in depth.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- SkyDB
- skydb.net
tags:
- Maps, Geolocation and Transport
- Urban and industrial infrastructure
- skyscrapers
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# SKYDB

> A global database of ~177,000 skyscrapers and tall buildings, searchable and filterable by city/country/height — the go-to when a distinctive tall building anchors a photo you're geolocating.

## When to use
You are geolocating an `image` with a recognisable skyscraper or tall building in the skyline, or you have a `geolocation` and want to identify/verify a specific tower. SKYDB lets you filter by city/country and browse tallest-building lists, so you can match a building's silhouette, height, or distinctive features to a named building and pin the city — then confirm with street-view/mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.skydb.net/ and use search or filter by city/country/region; or browse the "top 1000 tallest" list.
2. Match the building in your photo by shape, height, floor count, or completion era.
3. Open the record for location, height, year, floor count, developer/`employer-org`, photos, and construction status.
4. Confirm the identification against street-view/satellite imagery for the exact position.
5. Pivot: the confirmed building `geolocation` anchors the photo; the developer/owner `employer-org` feeds further corporate OSINT.

## Inputs → Outputs
- **In:** `geolocation`/city clue or an `image` of a tall building
- **Out:** identified building `geolocation`, height/year/floors, `employer-org` (developer/owner), and photos
- **Empty/negative result looks like:** no match — the structure may be below the "tall building" threshold, very new/unrecorded, or in a thinly covered region. Not every building qualifies; fall back to street-view sweeps.

## Gotchas & OpSec
- Only covers *tall* buildings — ordinary low-rise structures won't be listed.
- Some records are richer than others; verify height/year against the drill-down source.
- Full access/API is paid, but the free tier usually suffices for identification.

## Overlaps ("do both")
- Pairs with street-view/satellite tools and building-name web search — SKYDB names and locates the tower, while mapping confirms the exact vantage point of the photo.

## Trust & verifiability
`trust: community` — a large, expert-verified database with source drill-down; core facts are reliable, and every record links to its source so you can confirm before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skydb |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
