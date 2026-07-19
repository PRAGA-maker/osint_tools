---
id: geohints
name: GeoHints
description: Use when you have an unidentified `image`/scene and want country-level geolocation clues — a reference of poles, bollards, signs, plates and road markings by region.
url: https://geohints.com/
category: geolocation
path:
- geolocation
bestFor: Narrowing where a photo/video was taken by matching visible infrastructure (utility poles, bollards, road signs, licence plates, road lines) to country/region references.
selectorsIn:
- image
- physical-description
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public reference site; no account. It's a knowledge base you read, not a data service that stores queries.
opsec: passive
opsecNote: You consult a static reference and never submit the target image anywhere — fully passive, nothing leaves your browser about your subject. No sock-puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded community geolocation reference (listed in Bellingcat's toolkit), popular with GeoGuessr players and OSINT researchers; content is crowd-curated, so cross-check specifics.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bellingcat-openstreetmap-search
aliases:
- Geo Hints
tags:
- bellingcat-toolkit
- geolocation
- geoguessr
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# GeoHints

> A reference library of the tell-tale physical details — utility poles, bollards, road signs, licence plates, road markings — that reveal which country or region a photo was taken in.

## When to use
You have an `image` or video of an unknown location and need to narrow the country/region before pinpointing it. GeoHints catalogues how mundane infrastructure differs by place: pole shapes, bollard styles, sign fonts/colours, plate formats, road-line colours, chevrons, and more. Match what's visible in your frame against its references to eliminate regions and focus your search — a core early step in geolocating imagery in missing-persons and verification work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://geohints.com/ and browse the categories (bollards, poles, signs, licence plates, road lines, etc.) or by country.
2. Identify a distinctive feature in your image (e.g. a specific bollard or plate colour).
3. Compare it against GeoHints' regional examples to see which countries match and which are ruled out.
4. Combine several independent clues (pole + sign + plate) to converge on a region — no single feature is conclusive.
5. Pivot: with a candidate country/region, move to feature-based location search like `[[bellingcat-openstreetmap-search]]` and satellite/street imagery.

## Inputs → Outputs
- **In:** an `image`/`physical-description` of a scene's infrastructure
- **Out:** candidate country/region (`geolocation` narrowing), not a precise point
- **Empty/negative result looks like:** the visible features are too generic/global to distinguish (e.g. common European bollards) — GeoHints narrows, it doesn't always pinpoint; you'll need more clues.

## Gotchas & OpSec
- It's a reference, not a search engine — you do the matching by eye; results are only as good as the clues you spot.
- Infrastructure styles overlap across borders and change over time; treat matches as probabilistic and corroborate with multiple features.
- OpSec: fully passive; nothing about your image is submitted or logged.

## Overlaps ("do both")
- Pairs with `[[bellingcat-openstreetmap-search]]` — GeoHints narrows the country from visible infrastructure; the OSM tool then finds the exact spot by feature clustering.

## Trust & verifiability
`trust: community` — a crowd-curated geolocation knowledge base used widely by researchers, but community-maintained; verify a decisive clue against primary sources (official plate/sign standards, street imagery) before locking in a region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geohints |
| category | geolocation |
| selectorsIn → selectorsOut | image, physical-description → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
