---
id: boatnerd-great-lakes-shipping
name: BoatNerd (Great Lakes Shipping)
description: Use when you have a Great Lakes vessel name and want to identify and track it — returns vessel details, photos, history and AIS-based positions for lake and seaway ships.
url: https://boatnerd.com
category: transportation
path:
- transportation
bestFor: Identifying and tracking Great Lakes / St. Lawrence Seaway vessels and reading their history.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free enthusiast resource; no account required.
opsec: passive
opsecNote: Reading vessel info and public AIS feeds is passive; you query a shipping-enthusiast site and public AIS data, not any individual. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Great Lakes shipping enthusiast community; vessel data and photos are hobbyist-maintained but detailed and well-regarded for the region.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ais-boatnerd-com
aliases:
- BoatNerd
- boatnerd.com
tags:
- toddington
- curated-directory
- specialty-search
- maritime
- shipping
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# BoatNerd (Great Lakes Shipping)

> The enthusiast hub for Great Lakes and Seaway shipping — vessel profiles, photos, histories and live AIS positions for lakers and ocean-going ships on the lakes.

## When to use
Your investigation touches a Great Lakes or St. Lawrence Seaway vessel — a ship a subject crews, owns, photographed, or is associated with — and you want to identify it and place it. BoatNerd offers detailed vessel information (dimensions, operator, build history), photo galleries, and, via its AIS feed, current/recent positions (`geolocation`). It's a niche regional maritime source, useful for vessel identification and for placing a named ship in time and space.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://boatnerd.com and use the vessel database / fleet listings, or the photo galleries, to look up a ship by name.
2. Read the vessel profile: operator/owner, dimensions, build year and history, and browse photos to confirm identity.
3. For live tracking, use the AIS map (`[[ais-boatnerd-com]]`) to see the vessel's current or recent `geolocation` on the lakes/seaway.
4. Pivot: the operator/owner feeds company research; a confirmed vessel position corroborates a timeline or a photo's location; ship photos can be cross-checked against a subject's imagery.

## Inputs → Outputs
- **In:** a Great Lakes vessel name (or a photo to match against galleries)
- **Out:** vessel details, history, photos, and AIS-based `geolocation` (current/recent position)
- **Empty/negative result looks like:** no matching vessel — it may not be a Great Lakes ship (BoatNerd is regional), or the name is off; try a global AIS/registry source instead.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Coverage is the Great Lakes / Seaway region specifically — for ocean-going or other-region vessels use global AIS and ship registries.
- Enthusiast-maintained: detailed and reliable for the region, but corroborate ownership/registry facts against an official vessel registry.

## Overlaps ("do both")
- Pairs with `[[ais-boatnerd-com]]` (its live AIS map) and global ship-tracking/registry tools — BoatNerd gives rich regional history and photos, while global AIS/registries give ownership of record and worldwide positions.

## Trust & verifiability
`trust: community` — a respected hobbyist community resource; treat vessel identifications as strong regional leads and confirm ownership/registration against an official maritime registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boatnerd-great-lakes-shipping |
| category | transportation |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
