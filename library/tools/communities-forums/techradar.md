---
id: techradar
name: TechRadar
description: Use when you have an image or partial description of a consumer device and want to identify its make/model, specs, and release date from detailed reviews — returns `device-id`, `physical-description`.
url: https://www.techradar.com
category: communities-forums
path:
- communities-forums
bestFor: Identifying and dating a consumer electronic device (phone, camera, laptop, wearable) from in-depth reviews.
selectorsIn:
- image
- device-id
selectorsOut:
- device-id
- physical-description
status: live
pricing: free
costNote: Free to read, ad-supported; no account or paywall for reviews.
opsec: passive
opsecNote: Reading reviews reveals nothing to any subject — you are researching a product, not a person. No target queries are made.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: TechRadar (Future plc) is an established consumer-tech publication with broad review coverage; reliable for device identification, though it is journalism, not a hardware registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wiredmagazine-electronic-device-reviews
tags:
- toddington
- curated-directory
- device-identification
- reviews
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# TechRadar

> A high-volume consumer-tech review site — a reference for identifying and dating a gadget you can see but can't name, across phones, cameras, laptops, and wearables.

## When to use
You have a photo or rough description of a consumer device connected to a case and need its make, model, specs, and release timeframe. TechRadar reviews an unusually broad range of gear (including mid-range and regional models Wired skips), so it's a strong second source for the device-identification step of an image investigation. It's a reference/context tool, not a person-lookup — low direct relevance, but useful when a device in an image is itself a lead (dating a photo, tying a listing to a model).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.techradar.com, or run a site-scoped query: `site:techradar.com "model or feature"`.
2. Search by the device's visible traits (form factor, brand, camera bump, port layout) or a suspected model name.
3. Read the review to confirm model, specs, and release date.
4. Read the output: a confirmed `device-id` and `physical-description` to match against the image; the release date bounds the earliest a photo could exist.
5. Pivot: a confirmed model feeds marketplace/serial searches and EXIF cross-checks against a photo's camera metadata.

## Inputs → Outputs
- **In:** `image` of a device or a partial `device-id`
- **Out:** `device-id` (make/model), `physical-description` (identifying features, release era)
- **Empty/negative result looks like:** no matching review — the device is too obscure or old; try the manufacturer's site or a dedicated device database (e.g. GSMArena for phones).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive; no subject query.
- Broad but not exhaustive, and reviews reflect the launch period — a "release date" bounds a timeline but a device stays in use long after.

## Overlaps ("do both")
- Pairs with `[[wiredmagazine-electronic-device-reviews]]`, EXIF tools, and marketplace searches — cross-check the model across two review sources, confirm the camera via EXIF, then tie the model to listings. Do both review sites when one lacks the device.

## Trust & verifiability
`trust: trusted` — an established consumer-tech publication reliable for product facts; use it as sourced journalism for identification and corroborate exact specs against the manufacturer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | techradar |
| category | communities-forums |
| selectorsIn → selectorsOut | image, device-id → device-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
