---
id: manhole-co-il
name: manhole.co.il
description: Use when you have an `image` or `geolocation` and want to identify a manhole/utility cover's origin — returns geolocation clues (country/city) by matching cover design against a global catalog.
url: https://manhole.co.il/default.asp
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Geolocating a photo by identifying the manhole/utility cover in it against a catalog of ~14,000 covers from 80 countries.
selectorsIn:
- image
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse and search the catalog; no account or payment required.
opsec: passive
opsecNote: You browse a static reference catalog and compare imagery yourself — no query about the subject leaves your machine beyond ordinary page loads. Fully passive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running enthusiast catalog maintained by Eli Zvuluny; imagery and locations are hobbyist-contributed, so treat matches as leads to corroborate, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- The ultimate manhole covers site
tags:
- mapsandlocationsites
- geolocation
- image-geolocation
source: uk-osint
lastVerified: '2026-07-20'
enrichment: full
---

# manhole.co.il

> A hobbyist catalog of ~14,000 photographed manhole and utility covers from 80 countries and 1,000+ cities — usable as a chartable reference for image-geolocation.

## When to use
You have an `image` (a street-level photo, a video still, a hostage/proof-of-life frame) that contains a manhole cover, storm-drain grate, or utility lid, and you want to narrow the location. Municipal cover designs, foundry marks, and text are highly local, so matching the cover in your photo against this catalog can suggest a country or even a specific city — a classic chart-and-cross-reference geolocation move.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the covers map at https://manhole.co.il/coversMap.asp or browse by country/city from https://manhole.co.il/.
2. Read the cover in your target image: foundry name, city name, utility (water/gas/telecom), language/script, and geometric pattern.
3. Filter the catalog by the country or city you suspect, or scan by design, and compare cover photos side-by-side with your image.
4. Treat a close visual + textual match as a geolocation lead; confirm against street-view imagery of the candidate city.
5. Pivot: a candidate city feeds mapping/street-view tools and address databases for that locale.

## Inputs → Outputs
- **In:** `image` (photo containing a cover), or a known `geolocation`/`address` to browse local examples
- **Out:** `geolocation` lead (country/city the cover style matches)
- **Empty/negative result looks like:** no visually/textually similar cover in the catalog — common, since coverage is patchy; a miss does NOT rule out any location.

## Gotchas & OpSec
- Human-in-the-loop: matching is a manual visual comparison, not an automated reverse-image search — you do the eyeballing.
- Coverage is hobbyist and uneven; many cities have zero examples, so it complements rather than replaces broader geolocation.
- OpSec: passive; you only read a public catalog.

## Overlaps ("do both")
- Use alongside general street-view/mapping tools and reverse-image search: this narrows the *style* to a place, and those confirm the exact spot.

## Trust & verifiability
`trust: community` — an enthusiast-maintained catalog, accurate as a design reference but not an authoritative gazetteer. Always corroborate a suggested city with independent imagery before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manhole-co-il |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image, geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
