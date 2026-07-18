---
id: world-license-plates
name: World License Plates
description: Use when you have an `image` of a licence plate (or its format) and want to identify where it's from — returns the country/region `geolocation` by matching plate design, colours and format.
url: https://worldlicenseplates.com
category: transportation
path:
- transportation
bestFor: Identifying the country/region of origin of a licence plate from its design, colours and format.
selectorsIn:
- image
- vehicle-plate
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference gallery; no account, nothing to install.
opsec: passive
opsecNote: A static reference gallery you browse — no query touches any target and nothing about your subject is submitted. Purely a visual identification aid.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running enthusiast reference site cataloguing plate designs worldwide (cited in OSINT toolkits such as Bellingcat's); it's a design catalogue, not an owner database, so it identifies origin, not people.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- licenseplates
aliases:
- License Plates of the World
- worldlicenseplates.com
tags:
- vehicle
- geolocation
- plate-identification
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# World License Plates

> A reference gallery of licence-plate designs from around the world — the tool for answering "which country/region is this plate from?" from a photo.

## When to use
You have an `image` of a vehicle with a partly-visible or unfamiliar licence plate and need to establish **where it's registered** — a geolocation clue in photo/video verification. By matching the plate's colours, layout, character format, flags, and regional codes against this catalogue, you can pin down the country and often the state/province/era. This identifies *origin*, not the owner — it will not decode a plate to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://worldlicenseplates.com and browse by continent/country, or search for distinctive features.
2. Compare the plate in your `image` to the catalogue: background/colour scheme, character font and spacing, blue EU/flag strips, regional prefixes, and shape.
3. Narrow to the matching country and, where shown, the region and time period (designs change over the years, which can also date a photo).
4. Confirm the format (letter/number pattern) matches the candidate country's scheme.
5. Pivot: once you know the country/region, use that country's official vehicle register or plate-lookup tool (where lawful) and feed the `geolocation` into wider image-verification.

## Inputs → Outputs
- **In:** `image` of a plate (or a described format / `vehicle-plate` string)
- **Out:** `geolocation` — country and often region/era of registration
- **Empty/negative result looks like:** no confident match — the plate is too blurred, a custom/novelty plate, a very recent design not yet catalogued, or a rare type. Corroborate with other plate-reference sites (Olav's Plates, Bellingcat's plate maps) before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — it's a static gallery; nothing is submitted or logged about your subject.
- **Not an owner lookup.** It only identifies plate origin/design; do not expect a name or address from it.
- Designs evolve and regions reuse formats — cross-check against a second reference and mind the era of the design.

## Overlaps ("do both")
- Do both with `[[licenseplates]]` and other plate-reference galleries to confirm the country, then hand the identified region to that jurisdiction's official register for any owner/vehicle lookup.

## Trust & verifiability
`trust: community` — a respected enthusiast catalogue used in OSINT workflows; reliable for *identifying* plate origin (verify against a second gallery), but it holds no owner data, so it's an identification aid only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-license-plates |
| category | transportation |
| selectorsIn → selectorsOut | image, vehicle-plate → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
