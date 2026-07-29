---
id: identify-plans
name: Pl@ntNet Identify
description: Use when you have an `image` of vegetation in a photo and want to identify the plant species — narrows the `geolocation` by matching flora to its native range/climate.
url: https://identify.plantnet.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Identifying plant species from a photo to constrain where an image was taken (climate/region).
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to use on the web and via the Pl@ntNet app; an API exists with a free tier and paid higher volumes.
opsec: passive
opsecNote: You upload a cropped plant image to Pl@ntNet's servers (a scientific/academic project) — nothing about the subject is queried, but the image is sent to a third party. Crop to just the plant and strip EXIF before uploading if the source image is sensitive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Pl@ntNet is a citizen-science project by French research institutes (CIRAD, INRAE, IRD, Inria); its identifications are model suggestions ranked by confidence, backed by a large botanical dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- PlantNet
- Pl@ntNet
- plantnet.org
tags:
- Image Search and Identification
- geolocation-aid
- plant-id
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Pl@ntNet Identify

> A plant-identification engine — turn the greenery in a photo into a species name, then use that species' native range to constrain where the picture was taken.

## When to use
You're geolocating an image and the vegetation is a clue: identifying a distinctive tree, flower, or shrub tells you the climate/region it grows in, ruling large areas in or out. Pl@ntNet identifies plant species from a photo, which is a classic geolocation corroborator (alongside architecture, signage, and terrain). It's an image-analysis aid, not a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Crop the source image to the plant (leaf, flower, fruit, or whole habit) and open identify.plantnet.org (or the app).
2. Upload the crop and select the organ type (flower/leaf/fruit/bark) for a better match.
3. Read the ranked species suggestions with confidence scores; manually pick the plausible one and check its distribution map.
4. Cross-reference that species' native/cultivated range against your other geolocation clues.
5. Pivot: a species with a narrow range tightens `geolocation`; feed the constrained region back into mapping/satellite tools.

## Inputs → Outputs
- **In:** an `image` (cropped to the plant)
- **Out:** ranked species identifications → a `geolocation` constraint via the species' range
- **Empty/negative result looks like:** low-confidence or scattered suggestions — a poor/ambiguous crop, a cultivated ornamental (grown far outside its native range), or a species not in the dataset; treat low-confidence hits as weak.

## Gotchas & OpSec
- **Cultivated ≠ native:** ornamentals and crops are grown worldwide, so a match only constrains location if the plant is genuinely range-limited — reason about wild vs. planted context.
- Suggestions are ranked probabilities, not facts — pick with human judgment and corroborate with a second geolocation signal.
- **Passive**, but the image goes to a third party — crop tightly and strip EXIF for sensitive sources.

## Overlaps ("do both")
- Pairs with mapping/satellite and other geolocation cues (architecture, signage, sun position): Pl@ntNet supplies the botanical constraint; the others confirm the exact spot.

## Trust & verifiability
`trust: trusted` — a credible academic citizen-science project with a large curated dataset; identifications are confidence-ranked suggestions, so verify the top pick against its known range.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | identify-plans |
