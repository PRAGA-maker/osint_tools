---
id: inpe-image-catalog
name: INPE Image Catalog
description: Use when you have a `geolocation` (an area of interest, esp. South America) and want free medium-resolution satellite imagery for it — returns image, geolocation.
url: http://www.dgi.inpe.br/catalogo/
category: image-video-face
path:
- image-video-face
bestFor: Free CBERS / Amazonia / Landsat-class satellite scenes over Brazil and South America by area and date.
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Imagery is free of charge; a free account registration is required to place download orders.
opsec: passive
opsecNote: Searching and ordering imagery touches a Brazilian government (INPE) portal, not any target — nobody at the location is alerted. You must register a free account to download, so use a sock-puppet identity/email if you don't want the order tied to you.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by INPE, Brazil's National Institute for Space Research — an authoritative government source for CBERS and related satellite data.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- INPE Catálogo de Imagens
- DGI INPE catalog
tags:
- satellite-imagery
- remote-sensing
- geolocation
- south-america
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# INPE Image Catalog

> Brazil's space agency catalogue of free satellite imagery — the go-to for medium-resolution CBERS/Amazonia scenes over South America, and a global archive beyond it.

## When to use
You have a `geolocation` / area of interest and need overhead imagery for free — to establish what was at a location on a given date, corroborate a scene, or fill a gap where commercial imagery is paywalled. Strongest coverage is Brazil and South America (CBERS and Amazonia satellites), which makes it the specialist choice for that region, but the catalogue also holds broader archives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dgi.inpe.br/catalogo/.
2. Define your area of interest (draw/enter coordinates or pick the region) and set a date range and satellite/sensor filter.
3. Browse returned scenes; inspect quick-look thumbnails to judge cloud cover and framing over your `geolocation`.
4. Register a free INPE account (required) to place a download order for the full-resolution scene.
5. Pivot: downloaded imagery feeds change-detection over time, corroboration of a location's state on a date, or comparison against street-level and other-provider imagery.

## Inputs → Outputs
- **In:** `geolocation` (area of interest + date range)
- **Out:** `image` (satellite scenes), `geolocation` (scene footprints/coordinates and acquisition date)
- **Empty/negative result looks like:** no scenes for your area/date, or only heavily cloud-covered quick-looks — widen the date range or accept that no clear pass exists for that window.

## Gotchas & OpSec
- Resolution is medium (tens of metres for many products) — good for landscape/context, not for reading number plates or identifying individuals.
- The interface is Portuguese-first and the ordering/download flow requires a **free account**; expect some latency between order and delivery.
- OpSec: passive toward any target, but downloads are tied to your registered account — use a sock-puppet email.

## Overlaps ("do both")
- Pairs with global imagery browsers (Sentinel/Landsat viewers): INPE gives free CBERS/Amazonia coverage that shines over South America, while the others give complementary Sentinel/Landsat passes and dates.

## Trust & verifiability
`trust: trusted` — a first-party government (INPE) archive, so provenance and acquisition metadata are authoritative; the limiting factor is resolution and cloud cover, not data trust.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inpe-image-catalog |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
