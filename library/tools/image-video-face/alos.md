---
id: alos
name: ALOS
description: Use when you have a `geolocation` and want Japanese-satellite earth-observation imagery — returns ALOS optical/radar scenes of the area (via JAXA's data portal).
url: https://www.eorc.jaxa.jp/ALOS/en/index_e.htm
category: image-video-face
path:
- image-video-face
bestFor: Accessing JAXA ALOS satellite earth-observation imagery (optical PRISM/AVNIR and PALSAR radar) for a location.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: freemium
costNote: Mission/data is JAXA-operated; browsing and many products are free via JAXA's G-Portal (free registration), with some higher-level products restricted.
opsec: passive
opsecNote: You download published satellite imagery of a place — no subject is contacted. Registering for JAXA's data portal discloses an email; use a sock-puppet account for sensitive research.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: JAXA (Japan's national space agency) operates the ALOS satellites; imagery is authoritative first-party earth-observation data.
missingPersonsRelevance: low
coverage:
- global
- jp
auth: account
api: false
localInstall: false
registration: true
aliases:
- Advanced Land Observing Satellite
- JAXA ALOS
- ALOS-2
- ALOS-4
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- jaxa
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# ALOS

> JAXA's Advanced Land Observing Satellite programme — a source of Japanese earth-observation imagery (optical and PALSAR radar) for looking at a location from space.

## When to use
You have a `geolocation` and want satellite imagery to analyse terrain or change — especially where radar (PALSAR, which sees through cloud and at night) or JAXA's optical/elevation products add something Western sources (Sentinel, Landsat, Planet) don't. A niche, specialist source: reach for it when you specifically need ALOS radar/elevation data or Japanese-region coverage, not as a first-choice imagery browser.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at JAXA's ALOS EORC pages (https://www.eorc.jaxa.jp/ALOS/en/index_e.htm) to understand available sensors/products (PRISM, AVNIR-2, PALSAR/PALSAR-2, ALOS-4).
2. Go to JAXA's **G-Portal** data portal and create a free account.
3. Search by `geolocation`/scene, filter by sensor and date, and download the scene.
4. Analyse the `image` (optical or radar) in a GIS/imagery viewer.
5. Pivot: elevation/terrain and radar change-detection corroborate ground events; combine with optical sources for interpretation.

## Inputs → Outputs
- **In:** `geolocation` (area/scene + date/sensor)
- **Out:** ALOS satellite `image` scenes (optical or PALSAR radar), elevation products
- **Empty/negative result looks like:** no scene for your area/date/sensor — ALOS acquisitions aren't continuous everywhere; a gap means no matching capture, not that imagery is unavailable elsewhere.

## Gotchas & OpSec
- Access is via **JAXA's data portal with a free account**, not a one-click map; expect a data-portal workflow and product-level restrictions.
- Radar imagery (PALSAR) needs different interpretation skills than optical — don't read it like a photo.
- OpSec: passive; registration exposes an email — use a sock puppet.

## Overlaps ("do both")
- Pairs with Sentinel Hub/Copernicus, Landsat, and [[planet-gallery]] — those give easy optical/time-series; ALOS adds cloud-penetrating radar and JAXA elevation data those lack.

## Trust & verifiability
`trust: trusted` — JAXA operates the satellites, so the imagery is authoritative first-party earth-observation data. The caveats are access workflow and acquisition coverage, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alos |
