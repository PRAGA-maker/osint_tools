---
id: license-plate-maps
name: License Plate Maps
description: Use when you have a photo of a `vehicle-plate` and want to identify its country/region of issue — a reference collection of plate-format guides and maps returning geolocation leads.
url: https://bellingcat.gitbook.io/toolkit/more/all-tools/license-plate-maps
category: transportation
path:
- transportation
bestFor: Identifying the issuing country/region of a license plate from its format, colors, and codes.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
opsec: passive
opsecNote: These are reference guides you read; identifying a plate's origin involves no query about the vehicle or owner and alerts no one. This tells you WHERE a plate is from, not WHO owns it — plate-to-owner lookups require restricted official databases, not these guides.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated on the Bellingcat investigation toolkit, which vets the resources it lists; the linked guides are community/reference material.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- about-maps-and-satellites
- bellingcat-meta-content-library
- bellingcat-s-online-investigation-toolkit-2
- china-related-resources
aliases:
- License Plate Maps
- number plate identification
tags:
- license-plate
- geolocation
- bellingcat-toolkit
- transport
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# License Plate Maps

> A curated set of reference guides and maps for reading license plates — match a plate's format, colors, and region codes to pin down which country or state issued it.

## When to use
You have an image with a visible `vehicle-plate` (from a photo, video, or street imagery) and need to know where the vehicle is registered. Plate designs, color schemes, character patterns, and regional prefix codes vary by jurisdiction; these guides let you narrow a plate to a country and often a state/province — a concrete `geolocation` anchor for a person or event, valuable in verification and missing-persons work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Bellingcat toolkit page: https://bellingcat.gitbook.io/toolkit/more/all-tools/license-plate-maps.
2. Note the plate's visible features: overall format, background/text colors, flags or country codes, and any regional prefix.
3. Use the linked plate-format references/maps to match those features to an issuing country and, where possible, sub-region.
4. Pivot: the identified region localizes the vehicle/subject; combine with visible landscape, signage, and street imagery to tighten the geolocation.

## Inputs → Outputs
- **In:** `vehicle-plate` (visual — format/colors/codes from an image)
- **Out:** `geolocation` (issuing country and often state/province)
- **Empty/negative result looks like:** the plate is too blurred/partial or its format ambiguous — you may only narrow to a set of candidate regions; combine with other scene clues rather than forcing a single match.

## Gotchas & OpSec
- Human-in-the-loop: none (reading reference material).
- OpSec: passive — no lookup of the vehicle or owner; nobody is alerted.
- These guides identify *origin*, not *owner*. Resolving a plate to a registered keeper requires restricted government/DMV databases and is legally gated — not something these maps provide.

## Overlaps ("do both")
- Pairs with mapping/satellite tools [[about-maps-and-satellites]] and chronolocation/geolocation workflows — the plate narrows the country, while imagery analysis of the surrounding scene confirms and refines the exact location.

## Trust & verifiability
`trust: trusted` — surfaced through Bellingcat's vetted investigation toolkit; the underlying guides are reference material, so cross-check an unusual plate against more than one guide before committing to a country/region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | license-plate-maps |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
