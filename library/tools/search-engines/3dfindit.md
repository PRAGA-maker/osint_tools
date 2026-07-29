---
id: 3dfindit
name: 3DFindit
description: Use when you have a part image, sketch, or keyword and want to identify matching CAD/BIM models and their manufacturers — returns employer-org, document-id.
url: https://3dfindit.com/textsearch
category: search-engines
path:
- search-engines
bestFor: Identifying a mechanical/CAD part and its manufacturer via text, sketch, or 3D-geometry search.
selectorsIn:
- image
selectorsOut:
- employer-org
- document-id
status: live
pricing: freemium
costNote: Free to search the public 3D CAD/BIM catalogs; a free account and paid tiers unlock model downloads and advanced search features.
opsec: passive
opsecNote: Passive — a search over indexed manufacturer CAD/BIM catalogs; nothing is sent to any subject. Uploading a proprietary part sketch does, however, send that geometry to the service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A CADENAS-operated commercial catalog search; results reflect the manufacturer catalogs it has indexed and should be corroborated with the manufacturer directly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- 3DFindit
- 3Dfindit.com
- CADENAS 3DfindIT
tags:
- Search engines
- cad
- 3d-models
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# 3DFindit

> A visual search engine over thousands of manufacturer CAD/BIM catalogs — identify an unknown mechanical part or building component and trace it back to its maker.

## When to use
A niche but real pivot: you have a **part or product** — a photo, a screenshot, a rough sketch, or a spec keyword — and want to know what it is and **who manufactures it**. 3DFindit searches ~3,500 CAD/BIM catalogs by text, sketch, screenshot, or 3D geometry and returns matching models with their manufacturer (`employer-org`) and catalog entry. Useful when an image in an investigation shows equipment, hardware, or a component you need to attribute.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://3dfindit.com/textsearch and choose a search mode — text keyword, or the sketch/screenshot/geometry search.
2. Enter the keyword or upload/draw the shape.
3. Browse the matched CAD/BIM models; each result names the manufacturer and catalog it came from.
4. Downloading the model files typically requires a free account; identification/browsing does not.
5. Pivot: the identified manufacturer (`employer-org`) feeds company/registry research and narrows where the depicted equipment could have been sourced.

## Inputs → Outputs
- **In:** `image` (part photo/sketch/screenshot), or a text keyword/spec
- **Out:** matching model `document-id`s and their `employer-org` (manufacturer/supplier)
- **Empty/negative result looks like:** no catalog match — the part is bespoke, unindexed, or the image is too ambiguous; a miss is not proof the part is rare.

## Gotchas & OpSec
- Passive for catalog search, but uploading a sketch/screenshot sends that geometry to the service — don't upload anything sensitive.
- Coverage is limited to catalogs 3DFindit has indexed (strong for industrial/engineering parts, weak for consumer goods).
- Manufacturer attribution is a lead — confirm with the manufacturer's own catalog before relying on it.

## Overlaps ("do both")
- Complements general reverse-image search — a mainstream engine finds where an image appears online, while 3DFindit specifically identifies the CAD/engineering object in it.

## Trust & verifiability
`trust: unverified` — a commercial catalog aggregator (CADENAS); results are only as complete as its indexed catalogs, so corroborate any attribution at the manufacturer source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 3dfindit |
| category | search-engines |
| selectorsIn → selectorsOut | image → employer-org, document-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
