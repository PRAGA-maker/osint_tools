---
id: baidu-maps
name: Baidu Maps
description: Use when a person, address, or photo points to mainland China and you need the local-quality map, POIs, satellite, and street-level Panorama imagery that Google Maps lacks there.
url: https://map.baidu.com/
category: geolocation
path:
- geolocation
bestFor: Mapping, POI discovery, and street-level imagery inside mainland China where Western maps are weak.
selectorsIn: [address, geolocation, name]
selectorsOut: [address, geolocation, employer-org]
status: live
pricing: freemium
costNote: Viewing maps, POIs, and Panorama street view in a browser is free with no login; the Baidu Maps developer API/SDK requires a Baidu account and key.
opsec: passive
opsecNote: You browse Baidu's public map; no contact with the target. Baidu is a Chinese platform that logs requests — use a clean/sock browser session and avoid signing into a Baidu account tied to your identity.
humanInLoop: true
humanInLoopReason: [captcha]
bestInteractionPattern: web-manual
trust: trusted
trustNote: Baidu Maps is China's dominant first-party mapping service (Baidu, NASDAQ-listed); imagery and POI data are authoritative for China, with the caveat of the BD-09 coordinate offset.
missingPersonsRelevance: medium
coverage: [cn]
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: [bing-maps, arcgis, batchgeo]
aliases: [baidu-ditu, baidu-map]
tags: [china, street-view, panorama, poi, mapping]
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Baidu Maps

> China's leading first-party map (Baidu Ditu): the place to get accurate streets, POIs, satellite, and street-level "Panorama" imagery for mainland China, Hong Kong, Macau, and Taiwan.

## When to use
A `name`, `address`, `geolocation`, or photo background ties to China and Google/Bing coverage is thin or wrong. Baidu gives local-quality streets, business/POI listings (`employer-org`), 3D city views, indoor views, and Panorama street-level imagery — essential for confirming an address, identifying a storefront, or matching a photo to a Chinese location. It is Chinese-language only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://map.baidu.com/ (no login needed to view).
2. Search by Chinese-language `address`, place `name`, or coordinates; use a translation aid if you don't read Chinese.
3. Switch layers: standard map, satellite, and Panorama (the person-icon street-level view) to inspect a location.
4. Read POIs around the point for nearby businesses/`employer-org`, hours, and labels.
5. Pivot: convert coordinates carefully (see below) before using them in non-Baidu tools; cross-check imagery with `[[bing-maps]]`.

## Inputs -> Outputs
- **In:** `address`, `geolocation`, `name` (Chinese-language search terms)
- **Out:** `address`, `geolocation`, `employer-org` (POIs/businesses), street-level imagery
- **Empty/negative result looks like:** no POIs/Panorama for very rural areas, or a mis-snapped pin if you fed WGS-84 coordinates without converting to BD-09.

## Gotchas & OpSec
- **Coordinate system trap:** Baidu uses **BD-09**, an extra offset on top of China's GCJ-02. Plain GPS/WGS-84 coordinates land tens-to-hundreds of metres off. Convert WGS-84 → BD-09 (and back) before moving coordinates between Baidu and other tools.
- Chinese-language only; a CAPTCHA may appear on heavy use.
- Avoid logging into a personal Baidu account — it associates your research with you on a foreign platform.
- China-only focus; coverage outside the region is poor.

## Overlaps ("do both")
- Pairs with `[[bing-maps]]` to compare imagery and dates (and because Bing sometimes has imagery Baidu blurs, and vice versa).
- Pairs with `[[arcgis]]` for boundary/terrain context once you have a confirmed point.

## Trust & verifiability
`trust: trusted` — first-party, dominant Chinese mapping platform with authoritative China data. The main reliability caveat is the BD-09 coordinate offset, not data quality; always reconcile coordinates explicitly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baidu-maps |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation, name → address, geolocation, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
