---
id: map-fight
name: MapFight
description: Use when you have two areas (countries, regions or cities) as `geolocation` and want to compare their true relative size by overlaying them at the same scale — returns a visual size `geolocation` comparison.
url: https://mapfight.xyz/browse/
category: geolocation
path:
- geolocation
bestFor: Comparing the real-world size of two countries, regions or cities by overlaying one on the other at a common scale.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account or payment required.
opsec: passive
opsecNote: A generic reference tool with no target-specific input — you compare place names, not people, so it leaks nothing about a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hobby/reference site; area figures come from public datasets and the value is the intuitive scale visual, not precise measurement.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mapfight.xyz
- country size comparison
tags:
- geolocation
- reference
- scale-comparison
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# MapFight

> A scale-comparison sandbox — overlay one country/region/city on another to see how big it *really* is, correcting for map-projection distortion.

## When to use
A supporting reference tool, not a lookup. When an investigation involves distances or areas — "how far could someone realistically travel", "how big is this search region", sanity-checking a claim about a place's size — Mercator-projection maps badly distort scale (Greenland looks huge, equatorial countries look small). MapFight overlays two places at the same true scale so you can reason about real distances and areas rather than distorted ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mapfight.xyz/browse/ (or the site's compare page).
2. Pick a first place (country, region or city) from the database or search box.
3. Pick a second place to compare against; the tool overlays them at a common scale and reports each area in km².
4. Read the overlay: the relative footprint tells you the true size ratio, correcting for projection distortion.
5. Use the result to frame reasoning — e.g. how a search area or a claimed travel range compares to a familiar region.

## Inputs → Outputs
- **In:** two `geolocation` references (place names / regions)
- **Out:** a same-scale visual overlay plus each area in km² (`geolocation` scale comparison)
- **Empty/negative result looks like:** a place not present in the database (nothing to overlay) — pick the nearest available administrative region instead.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and target-agnostic — you only enter public place names, so there's nothing sensitive to leak.
- It's a reasoning aid, not a measurement instrument; area figures are approximate and it does not do point-to-point distance for arbitrary coordinates.

## Overlaps ("do both")
- Complements proper mapping/GIS tools (e.g. `[[qgis]]`) when you need exact distances or to overlay real coordinates rather than whole administrative areas.

## Trust & verifiability
`trust: unverified` — a hobby reference site; treat its area numbers as ballpark and use it for intuition about scale, not as an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-fight |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
