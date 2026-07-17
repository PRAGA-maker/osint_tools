---
id: lykdat-com
name: Lykdat
description: Use when you have an `image` showing clothing and want to identify the garments and find visually matching retail products — returns clothing identification and shopping matches as an appearance lead.
url: https://lykdat.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse-image search specialised for fashion — pinpointing what clothing items appear in a photo and where to buy visually similar pieces.
selectorsIn:
- image
selectorsOut:
- physical-description
status: live
pricing: freemium
costNote: Basic visual clothing search is free; a consumer subscription (~US$3.99/mo) adds coupons/recommendations, and a separate "Lykdat for Business" API is the paid B2B product. The free consumer search is enough for identification.
opsec: passive
opsecNote: You upload an `image` to Lykdat's servers — treat the photo as disclosed to a third party. Crop to just the garment and strip identifying background/faces before uploading a case image; do not upload a victim's face.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial fashion visual-search company; matching is optimised for retail products, so it identifies garment type/style well but is not a forensic identity tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-lens
aliases:
- lykdat.com
tags:
- image-search-and-identification
- reverse-image-search
- fashion
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Lykdat

> A fashion-specialised reverse-image search — upload a photo and it identifies the clothing and finds visually matching retail items, useful for pinning down what a subject was wearing.

## When to use
You have an `image` of a person (from a last-seen photo, CCTV still, or social post) and the **clothing** is the actionable detail. Lykdat identifies garment type, colour, and style and surfaces near-identical retail products — which can turn "grey hoodie" into a specific brand/model, help match a described outfit to a photo, or corroborate that two images show the same clothing. Directly relevant to missing-persons "last seen wearing" descriptions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lykdat.com/ and use the visual/clothing search.
2. Upload the `image`, ideally **cropped to the garment** (remove faces/background first).
3. Read the results: identified item type, attributes (colour, pattern, style), and visually similar products with retailer links.
4. Note the specific brand/model matches — those refine a clothing description.
5. Pivot: a refined `physical-description` → matching against other sightings/photos; a distinctive branded item → retailer/marketplace search for purchase trails.

## Inputs → Outputs
- **In:** `image` containing clothing
- **Out:** `physical-description` refinement (garment type, colour, style) + matching retail products
- **Empty/negative result looks like:** no confident matches / only loosely-related products — expected for obscured, low-res, or highly generic clothing. Treat weak matches as "style family," not identification.

## Gotchas & OpSec
- Upload = disclosure: the image goes to a commercial third party. Crop to the garment; never upload a victim's face.
- It matches to **retail catalogues**, so it excels at commercially available fashion and struggles with uniforms, homemade, or vintage items.
- It identifies clothing, not people — never treat a product match as identifying the individual.

## Overlaps ("do both")
- Pairs with `[[google-lens]]` — Google Lens does general reverse-image search (may find the exact source photo), while Lykdat is stronger at naming the specific garment; run both on a clothing crop.

## Trust & verifiability
`trust: community` — a legitimate commercial fashion visual-search product. Reliable for garment identification within its retail catalogue; corroborate any "same clothing" conclusion by direct visual comparison.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lykdat-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image → physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
