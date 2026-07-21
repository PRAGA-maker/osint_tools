---
id: autogespot
name: Autogespot
description: Use when you have a `vehicle-plate` or a photo of a distinctive car and want crowd-sourced sightings — returns geolocation, date, and images tying that vehicle to a place and time.
url: https://www.autogespot.us/spots
category: transportation
path:
- transportation
bestFor: Placing an exotic or distinctive vehicle at a specific city and date from enthusiast "spot" photos.
selectorsIn:
- vehicle-plate
- image
- geolocation
selectorsOut:
- geolocation
- image
- vehicle-plate
status: live
pricing: freemium
costNote: Free to browse and search all spots; an optional premium membership adds features but browsing is open.
opsec: passive
opsecNote: You only read a public photo community; nothing reaches the vehicle's owner. Uploading your own spot would expose you, so stay a consumer of the data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: User-generated car-spotting community; sightings are enthusiast-submitted, so location/date are as reliable as the uploader.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Autogespot
- autogespot.com
tags:
- vehicle-osint
- car-spotting
- transportation
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Autogespot

> A vast enthusiast database of "spotted" exotic and luxury cars — nearly two million geotagged, dated photos, often with license plates in frame.

## When to use
Your subject drives a distinctive, high-end, or rare vehicle and you have its `vehicle-plate` or a clear photo of it. Autogespot's community photographs such cars in the wild and tags each spot with a city and date. Searching can place *that specific car* at a location on a date, corroborate that the subject was in an area, or surface additional photos revealing the plate and surroundings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.autogespot.com/ (the .us address redirects here).
2. Browse or filter by manufacturer/model, by city/country, or by date to narrow toward the target car.
3. Open individual spots to read the location and upload date, and zoom the images for the `vehicle-plate` and background context.
4. For a known plate, use site search / a site-scoped Google search (`site:autogespot.com "PLATE"`) since plates often appear in captions or comments.
5. Pivot: a confirmed `geolocation`+date feeds a movement timeline; a legible plate feeds national plate lookups.

## Inputs → Outputs
- **In:** `vehicle-plate`, an `image` of the car, or a `geolocation` to browse
- **Out:** dated sightings with `geolocation`, additional `image`s, and often a visible `vehicle-plate`
- **Empty/negative result looks like:** no spots for that car/plate — expected for ordinary vehicles; the site skews heavily to supercars, luxury, and modified cars.

## Gotchas & OpSec
- Coverage bias: everyday cars are rarely spotted; this shines only for eye-catching vehicles.
- Uploader-supplied location/date can be wrong or delayed — corroborate before relying on it.
- OpSec: passive as a reader; do not upload or comment, which would tip your hand.

## Overlaps ("do both")
- Pairs with national plate-lookup tools and reverse image search — Autogespot supplies the where/when sighting, those turn a plate or photo into ownership/identity leads.

## Trust & verifiability
`trust: community` — a hobbyist-run, user-submitted archive; the photos are genuine but metadata is only as accurate as the spotter, so treat each sighting as a lead to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autogespot |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, image, geolocation → geolocation, image, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
