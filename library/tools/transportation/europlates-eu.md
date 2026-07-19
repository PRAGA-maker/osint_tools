---
id: europlates-eu
name: Europlates.eu
description: Use when you have a photo of a `vehicle-plate` and want to identify its country/region of origin by matching format and design — returns a `geolocation` lead.
url: https://www.europlates.eu/
category: transportation
path:
- transportation
bestFor: Identifying which country (and often region/era) a licence plate comes from by comparing its layout, colours and codes against a photo reference archive.
selectorsIn:
- vehicle-plate
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference archive; users can also submit plate photos. It is NOT a registration-lookup service — no owner data.
opsec: passive
opsecNote: You are browsing a static photo catalogue; nothing is queried against any official registry and no one is alerted. Fully safe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A collaborative enthusiast-maintained photo archive of plate designs worldwide; excellent for visual identification, but it holds no registration data and entries are community-submitted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- europlates.eu
- €uroplates
tags:
- vehicle-plate
- license-plate
- geolocation
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Europlates.eu

> A worldwide photo catalogue of licence-plate designs, used to identify a plate's country and region of origin from an image — not a registration lookup.

## When to use
You have an image of a vehicle plate (from a photo, video frame or CCTV still) and need to know **where it's from** before you can do anything else with it. Match the plate's colours, format, side codes and font against Europlates' reference photos to pin down the country, and often the region or issue period. This is a geolocation/identification aid, not a way to get the registered keeper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.europlates.eu/.
2. Use the interactive world map or the country dropdowns to browse to a candidate country, or scan by continent.
3. Compare your `vehicle-plate` image against the reference thumbnails — colour scheme, character layout, blue EU/side band, regional prefix — clicking through for full-size examples.
4. Read out the `geolocation`: the matching country (and, from regional codes, a narrower area).
5. Pivot: once you know the issuing country, take the actual characters to that country's official/greyzone registration or insurance check (Europlates itself will not resolve an owner).

## Inputs → Outputs
- **In:** `vehicle-plate` characters/design or an `image` of the plate
- **Out:** `geolocation` (country, often region/era of the plate style)
- **Empty/negative result looks like:** no visual match — either the plate is a rare/vanity/temporary type not catalogued, or the country isn't covered; do not force a match, and treat a near-match as a hypothesis to confirm elsewhere.

## Gotchas & OpSec
- **No owner data.** This identifies the plate *style*, not the vehicle keeper. Don't expect names or addresses.
- Community-submitted photos can lag current designs; confirm era-sensitive IDs against a second source.
- OpSec: entirely passive — browsing a static archive.

## Overlaps ("do both")
- Use first to establish the country, then hand off to a country-specific plate/registration lookup — this tool narrows *where*, the registry tool answers *who/what*.

## Trust & verifiability
`trust: community` — a well-regarded hobbyist archive that is authoritative for visual plate identification but carries no registration data; corroborate the identified country with the plate's actual regional codes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europlates-eu |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
