---
id: mapy-cz
name: Mapy.cz
description: Use when you have a `geolocation`/`address` and want high-quality maps, aerial imagery and street-level panoramas — strongest in Czechia and Central Europe — returns geolocation.
url: https://mapy.cz
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Street-level panoramas and detailed aerial/topographic imagery, especially across Czechia and Central Europe.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use in the browser and mobile app (operated by Seznam.cz); no account required to view maps or panoramas.
opsec: passive
opsecNote: Passive map browsing; you disclose only your own queries, nothing about a target. Standard VPN hygiene is enough. Panorama capture dates vary, so note the imagery date when using it as evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Seznam.cz, a major Czech internet company; imagery and panoramas are first-party and widely used by geolocation investigators.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Seznam Mapy
- mapy.com
tags:
- maps
- panorama
- geolocation
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Mapy.cz

> A Czech mapping service prized by geolocation investigators for its street-level panoramas and crisp aerial/topographic imagery — an essential cross-check against Google/Bing, especially in Central Europe.

## When to use
You have a `geolocation` or `address` and want a second (or better) view than Google Maps — particularly in Czechia, Slovakia and the wider Central/Eastern European region where Mapy.cz coverage and panorama detail often beat Google Street View. Reach for it to confirm a location, read building/terrain detail, or find street-level panoramas for a place where Google has gaps. It's a place-verification tool, not a person finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mapy.cz.
2. Search an `address`/place name or pan/zoom to your `geolocation`.
3. Switch base layers — aerial (letecká), topographic (turistická), winter — to compare imagery.
4. Drag the panorama ("panorama"/pegman-style) control onto a road to get street-level views; note the capture date shown.
5. Pivot: match landmarks, signage and terrain against other imagery (`[[google-maps]]`-style tools, Bing, Yandex) to triangulate an exact spot.

## Inputs → Outputs
- **In:** `geolocation` (map point) or `address`/place name
- **Out:** `geolocation` confirmation via aerial/topographic imagery and street-level panoramas; coordinates
- **Empty/negative result looks like:** no panorama coverage for a road, or low-res aerial in remote areas — coverage is strongest in Central Europe and thinner elsewhere; fall back to another provider.

## Gotchas & OpSec
- OpSec: fully passive; nothing about your target leaves your browser.
- Panorama and aerial capture dates differ from Google's — this is a feature (compare epochs) but note the date when citing.
- Coverage and UI are strongest in Czech; the interface offers English, and imagery quality drops outside Central Europe.

## Overlaps ("do both")
- Do both with Google/Bing/Yandex imagery — Mapy.cz frequently has panoramas and clarity the others lack in its core region, and vice versa; triangulating across providers is how you nail a geolocation.

## Trust & verifiability
`trust: trusted` — first-party imagery from Seznam.cz, a major Czech provider; widely relied on in the geolocation community.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapy-cz |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
