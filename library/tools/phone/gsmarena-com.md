---
id: gsmarena-com
name: gsmarena.com
description: Use when you have a phone/device model (a `device-id` or a phone seen in a photo) and want its full specifications — returns camera, dimensions, sensor and release data (`metadata-exif`-style device intel) for image and device analysis.
url: https://www.gsmarena.com/glossary.php3
category: phone
path:
- phone
bestFor: Looking up a mobile device's detailed specifications to support image/device analysis.
selectorsIn:
- device-id
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free to browse the full specifications database. No account or payment.
opsec: passive
opsecNote: You look up a device model in a public specs catalogue — no person, phone number, or account is queried, and nothing reaches any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The de-facto reference database for mobile-device specifications, widely cited and accurate for hardware specs. Note it is a spec catalogue, not a person/phone-number lookup.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GSMArena
- gsmarena.com
tags:
- mobilephone
- Mobile & Phone Related
- device-specs
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- gsm-arena
---

# gsmarena.com

> The reference catalogue of mobile-device specifications — identify or research the exact phone behind an EXIF camera string or a device seen in a photo, down to its camera and dimensions.

## When to use
You have a device model — read from an image's EXIF (`Make`/`Model`), printed on a device, or inferred from a photo — and want its hardware detail. GSMArena gives the camera sensor/resolution (helps sanity-check whether a photo could have come from that device), physical dimensions (useful for scale in a scene), release date (bounds when the device existed), and connectivity. It's supporting intelligence for image and device analysis, not a way to look up a person from a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gsmarena.com and use the search box or the phone finder.
2. Enter the model name (e.g. from EXIF `Model`) as a `device-id`.
3. Open the device page and read the full specs: main/selfie camera resolution and features, dimensions/weight, display, chipset, and announce/release dates.
4. Cross-check against your evidence — e.g. does the claimed camera resolution match an image's stated pixel dimensions? Does the release date predate the photo?
5. Pivot: a confirmed device model corroborates or contradicts a photo's claimed origin; pair with an EXIF viewer to verify `Make`/`Model` fields, and with `[[fcc-io]]` for the regulatory filing.

## Inputs → Outputs
- **In:** `device-id` (a phone model) or a device identified in an `image`
- **Out:** detailed device specifications (`metadata-exif`-adjacent hardware intel: camera, dimensions, sensors, dates)
- **Empty/negative result looks like:** no matching device — the model string is a typo, a regional/rebranded variant, or too obscure/new for the catalogue. Try alternate model names or the phone finder filters.

## Gotchas & OpSec
- Human-in-the-loop: none; a catalogue lookup.
- OpSec: **passive** — no person or number is queried.
- This does **not** map a phone number to an owner (despite the "phone" category) — it's a hardware-specs reference. Use it to reason about devices and images, not to identify people.

## Overlaps ("do both")
- Pairs with an EXIF/metadata viewer and `[[fcc-io]]` — the EXIF viewer tells you the claimed `Make`/`Model`, GSMArena tells you what that device actually is/can do, and fcc.io links the FCC filing. Together they let you validate a photo's device provenance.

## Trust & verifiability
`trust: trusted` — an authoritative, widely-used device-specs reference. Specs are reliable; just remember its scope is hardware, so treat it as corroboration for image/device claims rather than a person-finding tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gsmarena-com |
| category | phone |
| selectorsIn → selectorsOut | device-id, image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
