---
id: gsm-arena
name: GSMArena
description: Use when you have a phone model name, a partial description, or EXIF `device-id` and want to confirm the exact handset and its specs — returns device identification and technical details.
url: https://www.gsmarena.com/
category: phone
path:
- phone
bestFor: Identifying and verifying a specific phone model (dimensions, camera, release date) from a model name, spec fragment, or photo metadata.
selectorsIn:
- device-id
- metadata-exif
selectorsOut:
- device-id
- metadata-exif
status: live
pricing: free
costNote: The specifications database, phone finder and comparisons are entirely free; the site is ad-supported with no account required.
opsec: passive
opsecNote: Browsing GSMArena is passive and unrelated to any subject — you are looking up device facts, not querying a person. No sock puppet needed; standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: GSMArena is the long-established, industry-standard reference for mobile-phone specifications; its device data is accurate and widely cited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GSM Arena
- gsmarena.com
tags:
- device-identification
- phone-specs
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# GSMArena

> The definitive phone-specifications database — use it to turn a model number, EXIF device tag, or "what phone is this?" question into a confirmed handset and its full spec sheet.

## When to use
You have a device clue and need to identify or verify the exact handset. Typical cases: a photo's EXIF `Make`/`Model` field names a phone (`metadata-exif` → confirm it's real and when it shipped); a witness or listing describes "a Samsung with three rear cameras and a stylus"; or you need a phone's exact dimensions/screen size to gauge scale in an image. GSMArena's `device-id` lookup corroborates all of these.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gsmarena.com/.
2. Search the model name/number directly, or use the "Phone Finder" to filter by brand, release year, camera count, screen size, dimensions, etc. to match a described device.
3. Open the device page: exact model variants, release date, dimensions/weight, camera and display specs, and supported network bands.
4. Cross-check against your clue — e.g. does the EXIF model exist, and does its camera match the image quality; do the dimensions fit a scale estimate.
5. Pivot: a confirmed model + release date bounds *when* a photo could have been taken; network bands hint at the region/carrier the device was sold in.

## Inputs → Outputs
- **In:** `device-id` (model name/number) or `metadata-exif` (EXIF make/model)
- **Out:** confirmed `device-id` (exact model + variants) and authoritative device specs; corroboration/refutation of a `metadata-exif` tag
- **Empty/negative result looks like:** no matching device — the model string is fabricated, misspelled, a region-specific rebrand (search the alternate name), or too new/old to be listed; absence suggests the EXIF tag may be spoofed.

## Gotchas & OpSec
- Rebrands/variants: the same handset ships under different names by region/carrier — search variants before concluding a model doesn't exist.
- EXIF can be spoofed or stripped; GSMArena confirms a model is *plausible*, not that a given photo truly came from it.
- OpSec: passive — this is device research, not person lookup.

## Overlaps ("do both")
- Pairs with EXIF/metadata viewers — the viewer reads the `Model` tag, GSMArena validates and enriches it.
- Pairs with reverse-image and geolocation work — knowing the exact device narrows capture date and helps scale/lens reasoning.

## Trust & verifiability
`trust: trusted` — GSMArena is the industry-standard specifications reference; its device data is reliable and independently citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gsm-arena |
