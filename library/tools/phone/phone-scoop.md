---
id: phone-scoop
name: Phone Scoop
description: Use when you have a phone make/model or `device-id` (or a photo of a handset) and want to confirm the exact model and its hardware specs/capabilities — returns `device-id` and device metadata (bands, cameras, sensors).
url: https://www.phonescoop.com/phones/
category: phone
path:
- phone
bestFor: Identifying a handset model and looking up its specs (network bands, GPS, cameras) from a model number or physical description.
selectorsIn:
- device-id
- physical-description
selectorsOut:
- device-id
- metadata-exif
status: live
pricing: free
costNote: Free reference database; no account required to browse or compare phones.
opsec: passive
opsecNote: Purely a reference lookup against Phone Scoop's own catalog — you enter a model, not any target data, so it leaks nothing about the subject. No sock puppet needed, though normal browser hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent phone-specs publication; spec data is editorially maintained and generally accurate, but it is a catalog, not a forensic source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PhoneScoop
- Phone Scoop phone finder
tags:
- phone
- device-specs
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Phone Scoop

> A large, browsable database of phone models and their hardware specs — use it to turn a model number or handset photo into confirmed device capabilities.

## When to use
You have a handset to identify — a `device-id`/model number seen on a device or box, or a `physical-description` from a photo — and you want to confirm the exact model and learn its specs: network bands, GPS/location capability, camera resolution, sensors, release date. Useful in a missing-persons context to reason about what a subject's phone can do (location tech, camera metadata potential) or to match a device seen in imagery to a make/model.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.phonescoop.com/phones/.
2. Enter the model number directly in the search box to jump to a specific handset, or use the Phone Finder to filter by specs/features, or browse by manufacturer/carrier.
3. Open the model page and read the full spec sheet.
4. Compare up to 5 candidate models side-by-side to disambiguate lookalikes.
5. Pivot: use confirmed specs (camera type, release year, bands) to sanity-check EXIF/metadata from the target's images, or to narrow which carrier/region a device belongs to.

## Inputs → Outputs
- **In:** `device-id` (model number/name) or `physical-description` (from a photo)
- **Out:** `device-id` (confirmed model) plus device metadata — camera specs that inform expected EXIF, network bands, GPS capability, dimensions, release date
- **Empty/negative result looks like:** no matching model (very new, region-exclusive, or non-US handsets may be missing) — absence here means "not in this catalog," not "no such phone."

## Gotchas & OpSec
- US-market-leaning catalog; some international/budget models are absent.
- It is a specs reference, not evidence — it tells you what a model can do, not what a specific device did.
- Fully passive; you never enter target data.

## Overlaps ("do both")
- Pairs with an EXIF/metadata reader like `[[jpegsnoop]]` — Phone Scoop tells you a model's capabilities, while EXIF from the target's photos tells you the actual device and settings used; cross-check the two.

## Trust & verifiability
`trust: community` — an independent, editorially maintained specs site. Reliable for hardware capability lookups; corroborate any device-to-target inference with metadata evidence.
