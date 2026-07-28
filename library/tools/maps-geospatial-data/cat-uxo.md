---
id: cat-uxo
name: CAT-UXO
description: Use when you have an `image` of a suspected munition/ordnance and want to identify it — a reference database of bombs, mines, rockets, and IEDs; returns type/identification data.
url: https://cat-uxo.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Identifying explosive ordnance (bombs, mines, submunitions, rockets, IEDs) from reference photos and specs.
selectorsIn:
- image
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Core reference database is free to browse; some lessons/contribution features sit behind free membership.
opsec: passive
opsecNote: Browsing the reference library is passive and reveals nothing about your investigation. This is identification reference only — never act on a real-world device; report suspected ordnance to qualified EOD authorities.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A specialist EOD community knowledge base; well-regarded within the demining/EOD field, but a community resource — corroborate identifications with authoritative references.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cat-uxo.com
- Counter-terrorism and UXO
tags:
- maps-and-geospatial
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# CAT-UXO

> A specialist reference database of explosive ordnance — landmines, submunitions, grenades, aircraft bombs, rockets, missiles, mortars, and IEDs — used to identify munitions from photos and specifications.

## When to use
You're doing conflict/war-zone OSINT and have an `image` of a weapon, munition remnant, or suspected device that you need to identify — matching a photographed shell, bomb, or mine to a type, origin, and characteristics. Valuable for verifying imagery from conflict areas, attributing weapons, or understanding an incident. Niche and unrelated to typical missing-persons work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cat-uxo.com/ and browse by category (landmines, submunitions, aircraft bombs, rockets/missiles, mortars, IEDs, etc.).
2. Compare your subject `image` against the reference photos and specifications to find the closest match.
3. Read the identification details — designation, dimensions, origin, hazards.
4. Corroborate with other munitions references before asserting an identification.
5. Pivot: a confirmed weapon type/origin supports attribution and timeline work in a conflict investigation.

## Inputs → Outputs
- **In:** `image` / description of a munition
- **Out:** `document-id` (munition designation/type and reference data)
- **Empty/negative result looks like:** no close visual match — the item may be a variant, damaged beyond recognition, or outside the database's coverage; consult additional EOD references.

## Gotchas & OpSec
- **Reference only — safety first:** never approach, handle, or act on a real device based on an online ID. Report suspected ordnance to qualified EOD/authorities.
- Community-curated; a photo match is a lead, not a definitive identification — corroborate.
- Passive browsing; no exposure to your investigation.

## Overlaps ("do both")
- Pairs with other munitions-ID references and imagery-verification/geolocation tools — CAT-UXO identifies the *object*, while geolocation tools place *where* the image was taken; together they support conflict attribution.

## Trust & verifiability
`trust: community` — a respected specialist EOD knowledge base, but community-maintained; treat identifications as well-informed leads and confirm against authoritative ordnance references.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cat-uxo |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
