---
id: landviewer
name: LandViewer
description: Use when you have a `geolocation` and want historical/current satellite imagery of it — returns browsable Sentinel/Landsat (and commercial) scenes by date, with analysis bands.
url: https://eos.com/products/landviewer/
category: image-video-face
path:
- image-video-face
bestFor: On-the-fly browsing of dated satellite scenes over a location — pick a date, compare change over time, apply band combinations.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: freemium
costNote: Free plan allows a capped number of scene views/analytics per month (around 15 images) from open sources like Sentinel and Landsat; unlimited access, hi-res commercial imagery, and full analytics are paid.
opsec: passive
opsecNote: You browse an imagery archive on EOS's servers, not the target — nothing reaches any person or place. A free account (email) is needed for most viewing, so queries tie to that login; use a research account. Imagery is historical satellite passes, so there is no risk of "alerting" a location.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by EOS Data Analytics, a commercial satellite-analytics firm, serving standard open imagery (Sentinel/Landsat) plus commercial scenes; the open-source imagery is authoritative and independently checkable.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- land-viewer
aliases:
- Land Viewer
- EOS LandViewer
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- change-detection
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# LandViewer

> A browser-based satellite-imagery viewer (EOS) — pull dated Sentinel/Landsat and commercial scenes over any location, step through time, and apply band combinations for analysis.

## When to use
You have a `geolocation` and need overhead imagery — to see what was at a place, how it changed over a date range, or to verify a scene from another source. For geolocation and missing-persons work, LandViewer lets you compare a location across dates (construction, vehicles, vegetation/water changes, disturbed ground) and apply spectral band combos (e.g. NDVI, false-color) that plain map imagery can't. Reach for it when Google Earth's historical imagery is too sparse for the dates you need and you want the frequent revisit of Sentinel/Landsat.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://eos.com/products/landviewer/ and sign in (free account; use a research login).
2. Search or navigate to your `geolocation` / area of interest.
3. Filter available scenes by date range, cloud cover, and sensor (Sentinel-2, Landsat, SAR, or paid hi-res).
4. Open a scene; step through dates to compare, and apply band combinations / indices to highlight features (vegetation, water, burn scars, bare soil).
5. Watch the free-tier scene/analytics quota — it's limited per month.
6. Pivot: a dated observation → build a timeline; a spotted feature → cross-check on Google Earth historical imagery, Sentinel Hub, or field/news sources.

## Inputs → Outputs
- **In:** `geolocation` / area + date range
- **Out:** dated satellite `image` scenes over that `geolocation`, band/index analysis layers
- **Empty/negative result looks like:** few/no cloud-free scenes for your dates, or resolution too coarse to see the detail — open imagery tops out around 10 m/pixel (Sentinel); for finer detail you need paid commercial scenes.

## Gotchas & OpSec
- Human-in-the-loop: account login required, and the free tier is quota-capped (~15 scenes/month) — plan your views.
- Open imagery resolution (~10 m Sentinel / ~30 m Landsat) won't show people or small objects; hi-res is paid.
- Cloud cover and revisit gaps limit which exact dates are usable.
- Fully passive; the only footprint is your account's query log.

## Overlaps ("do both")
- Pairs with `[[land-viewer]]`, Google Earth (historical imagery), and Sentinel Hub — cross-check the same location/date across viewers, since each exposes different scenes, dates, and processing options.

## Trust & verifiability
`trust: trusted` — a commercial operator serving standard open Sentinel/Landsat data you can independently re-pull from the source archives, so imagery findings are verifiable; treat any EOS-specific analytics as their processing of that public data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landviewer |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
