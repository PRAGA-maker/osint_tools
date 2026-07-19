---
id: license-plate-mania
name: License Plate Mania
description: Use when you have an image of a `vehicle-plate` and want to identify its country/region of origin and era — returns reference photos of plates from 119 countries plus the country-oval codes, so you can match a plate's design to a place.
url: https://licenseplatemania.com
category: transportation
path:
- transportation
bestFor: Identifying the country/region and era of a licence plate by comparing its design against a large reference collection.
selectorsIn:
- vehicle-plate
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference site; no account.
opsec: passive
opsecNote: You browse a static reference collection; nothing is submitted and the subject is not contacted. Fully safe to use.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Personal enthusiast archive (Jeroen Coninx, since 2000) of 6,800+ plate photos from 119 countries; excellent as a visual reference, but it is a hobby collection, not an authoritative registry, and it does not look up individual plate owners.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- licenseplatemania.com
- License Plate Mania
tags:
- transportation
- vehicles
- license-plates
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# License Plate Mania

> A long-running enthusiast archive of licence-plate photographs from 119 countries — use it to figure out *where* a plate is from and roughly *when*, by matching its colours, format, and country oval, not to identify an owner.

## When to use
You have a partial or full `vehicle-plate` visible in a photo/video and need to determine its country or region of origin and its era (plate designs change over time). Matching the plate's colour scheme, character layout, side codes, and the small country oval against this collection narrows an unknown vehicle to a place — a useful geolocation and vehicle-provenance step. It does **not** return the registered keeper; national registries (mostly restricted) do that.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://licenseplatemania.com.
2. Browse by country, or use the country-oval list to decode a `GB`/`NL`/`D`-style oval sticker next to a plate.
3. Compare the subject plate's format, colours, flags/side bands, and font against the reference photos to find the closest country and era match.
4. Confirm with a second source (a national plate-format guide) before asserting the origin, since neighbouring countries reuse similar layouts.
5. Pivot: a confirmed country of origin scopes which national registry or plate-decoder applies, and supports geolocating where the vehicle (and possibly the subject) is based.

## Inputs → Outputs
- **In:** `vehicle-plate` design / `image` of a plate
- **Out:** `geolocation` (country/region of origin) + era estimate
- **Empty/negative result looks like:** no close visual match, or several plausible countries with similar designs — treat it as narrowing, not a definitive ID, and disambiguate with a formal plate-format reference.

## Gotchas & OpSec
- Human-in-the-loop: yes — this is **manual visual comparison**; you eyeball the plate against reference images, so accuracy depends on your judgement and image quality.
- OpSec: fully **passive**; browsing a static archive reveals nothing to anyone.
- Scope limit: it identifies *plate origin/era*, never the *owner*. Do not expect a lookup-by-plate-number capability here.

## Overlaps ("do both")
- Pairs with national plate-format references and restricted registry/decoder tools — this collection tells you which country's system you're looking at; those tell you what the format encodes and (where lawful) who it belongs to.

## Trust & verifiability
`trust: community` — a respected but personal enthusiast archive; its photos are a strong visual guide yet not an official source, so corroborate any origin claim against a formal plate-format reference before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | license-plate-mania |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
