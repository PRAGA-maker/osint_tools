---
id: macrostrat-s-geologic-map-system-integrates-over-290-bedrock-geologic-maps-from-around-the-world-into-a-single-multisca
name: Macrostrat Geologic Map
description: Use when you have a `geolocation` and want the bedrock geology at that spot — returns rock type/formation/age to corroborate or narrow a location from ground clues.
url: https://macrostrat.org/
category: geolocation
path:
- geolocation
bestFor: Looking up the bedrock geology (rock type, formation, age) of a coordinate to cross-check or constrain a suspected photo location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open academic platform (University of Wisconsin); data under CC-BY-4.0, with a free public API.
opsec: passive
opsecNote: Passive query of a scientific map database; nothing about a person or the target site is signalled. Runs on Macrostrat's servers; no subject footprint.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-established academic geoscience platform integrating peer-reviewed geologic maps; authoritative for bedrock geology, though map resolution/coverage varies by region.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Macrostrat
- macrostrat.org geologic map
tags:
- geolocation
- geology
- maps
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Macrostrat Geologic Map

> An open, global geologic-map database with a click-anywhere interface — turn a coordinate into its bedrock rock type, formation, and age, a corroboration layer for visual geolocation.

## When to use
You're geolocating a photo and have a candidate `geolocation` plus visible geological clues — distinctive rock color, cliff strata, soil, an outcrop, a quarry. Macrostrat tells you the bedrock geology at any point, so you can test whether a candidate location's geology matches what the image shows, or eliminate candidates whose geology can't produce those features.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://macrostrat.org/ and go to the map.
2. Navigate/zoom to your candidate coordinate and click the location.
3. Read the returned bedrock unit: rock type, formation name, geologic age, and linked references.
4. Compare against the image's geological features to confirm or reject the candidate; for batch/automated checks, query the free Macrostrat API by lat/lng.

## Inputs → Outputs
- **In:** `geolocation` (a candidate point/area) + observed geological features
- **Out:** bedrock rock type/formation/age at that point (a `geolocation` corroboration signal)
- **Empty/negative result looks like:** no mapped unit / low-resolution coverage for that region — Macrostrat can't confirm or deny there; fall back to other geolocation cues. A geology mismatch is a strong signal to reject a candidate.

## Gotchas & OpSec
- Coverage and resolution vary hugely by region; well-mapped areas (US, Europe) are detailed, others coarse.
- It reports *bedrock*, not surface cover (vegetation, soil, urban fill) — reconcile with what's actually visible.
- Human-in-the-loop: interpreting whether geology matches an image requires judgment.

## Overlaps ("do both")
- Pairs with visual-geolocation tools like `[[street-clip]]` and terrain/elevation tools — geology is one corroboration layer among vegetation, climate, and architecture.

## Trust & verifiability
`trust: trusted` — authoritative, peer-reviewed geoscience data; the geology is reliable, but matching it to an image is your inference to make carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | macrostrat-s-geologic-map-system-integrates-over-290-bedrock-geologic-maps-from-around-the-world-into-a-single-multisca |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
