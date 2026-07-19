---
id: vehicle-documents
name: Vehicle Documents
description: Use when you have a license plate or vehicle document in a photo and want to identify its country/type and read its format — returns plate/document identification and a geolocation lead.
url: http://www.vehicle-documents.it
category: transportation
path:
- transportation
bestFor: Identifying which country/era a license plate or vehicle document is from, and decoding its format, from an image.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free informational/reference site; no account or payment. Ad-supported reference pages.
opsec: passive
opsecNote: A reference library you read — you enter nothing about your target and query no owner database, so it leaks nothing. Purely passive; the only footprint is your own visit to the site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent enthusiast reference (cited by Italian traffic-police resources such as ASAPS) cataloguing plate and document formats; a knowledge base, not a live lookup service.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- vehicle-documents.it
tags:
- vehicle
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Vehicle Documents

> A reference catalogue of the world's licence plates and vehicle documents — used to identify *where* a plate or document in a photo comes from, not to look an owner up.

## When to use
You have a photo containing a `vehicle-plate` or a vehicle document (registration, insurance disc, foreign plate) and can't tell which country, region, or era it's from. This site catalogues plate designs and official vehicle-document formats internationally, so you can match the plate style/colours/format against reference images and pin down the issuing country — a `geolocation` lead. Reach for it during image geolocation when a vehicle is the only regional clue. It is a **reference library**, not a plate-to-owner lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.vehicle-documents.it (the plate index is under `/targhe.htm`).
2. Browse by country/region to the plate or document type you're trying to match.
3. Compare your photo's plate against the reference: format, colours, prefix/serial layout, era — to identify issuing country and roughly when it was issued.
4. Pivot: the identified country/region is a `geolocation` anchor for the wider image-geolocation effort; a decoded plate format may narrow the region further, feeding maps and local-record searches.

## Inputs → Outputs
- **In:** `vehicle-plate` / vehicle document seen in an image (visual, not typed into a lookup)
- **Out:** `geolocation` — the issuing country/region and format/era of the plate or document
- **Empty/negative result looks like:** no matching design in the catalogue — the plate is too new, too obscure, or a specialty/custom plate the reference doesn't cover; fall back to a general plate-format search or crowdsource the identification.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a browse-only reference.
- OpSec: fully passive — you submit nothing about the subject and touch no owner database.
- It identifies the *plate/document*, never the owner — pair it with a country-specific lookup once you know the jurisdiction. Content is enthusiast-maintained, so obscure or very recent designs may be missing or dated.

## Overlaps ("do both")
- Pairs with country-specific plate lookups once you've identified the jurisdiction, and with image-geolocation tooling — this narrows *where*, the lookups then go after the vehicle in that jurisdiction.

## Trust & verifiability
`trust: community` — an independent enthusiast reference (cited by traffic-police resources), reliable for format identification but not an official registry; confirm the jurisdiction against an authoritative source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vehicle-documents |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
