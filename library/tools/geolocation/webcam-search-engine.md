---
id: webcam-search-engine
name: Webcam Search Engine
description: Use when you have a `geolocation` or place name and want public live webcams there — returns webcam feeds and their approximate `geolocation` for scene/landmark corroboration.
url: https://cse.google.com/cse?cx=013991603413798772546:gjcdtyiytey#gsc.tab=0
category: geolocation
path:
- geolocation
bestFor: Finding publicly listed live webcams near a place to corroborate weather, scenery or landmarks.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account. As a community-maintained CSE, its indexed source list can drift or go stale over time.
opsec: passive
opsecNote: You are searching a Google CSE and then loading third-party webcam-directory pages — those sites and Google see your IP, the target does not. Only ever use publicly published webcams; do not attempt to reach private/unsecured cameras.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Google Custom Search Engine curated by an unknown third party; it only surfaces public webcam directories, so quality depends on that curation and Google's index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- webcam CSE
- public webcam search
tags:
- geolocation
- webcams
- live-imagery
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Webcam Search Engine

> A Google Custom Search Engine tuned to public webcam directories: search a place and get live public camera feeds for that area.

## When to use
You have a `geolocation`, address or place name and want live or near-live public imagery of the area — to corroborate weather, lighting, traffic, seasonal state or a landmark visible in a target photo. Useful in geolocation/chronolocation work when you need to match ground truth at a known spot to a scene in your evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at the URL above.
2. Search a place name, landmark or region (e.g. "Times Square", "Zermatt", "Lake Tahoe").
3. Read the results — links into public webcam directories (EarthCam, WebcamTaxi, Windy webcams, tourism-board cams, etc.) that host live or refreshed feeds.
4. Open a feed and compare its scene, weather and shadows against your reference imagery; note the camera's stated `geolocation`.
5. Pivot: use a matching live view to confirm a location, or feed the confirmed coordinates into mapping/street-view tooling for closer geolocation.

## Inputs → Outputs
- **In:** `geolocation` / `address` / place name
- **Out:** links to public webcam feeds, their approximate `geolocation`, live `image` frames
- **Empty/negative result looks like:** the CSE returns unrelated pages or nothing for an obscure spot — meaning no public webcam is indexed nearby, not that none exists. Cross-check a dedicated map-based webcam service (e.g. Windy) before giving up.

## Gotchas & OpSec
- Human-in-the-loop: none, though some linked directory sites may throw ads or interstitials.
- OpSec: **passive** relative to any person — you touch Google and webcam directories, never the target. Stay strictly on public, published cameras; never probe private or misconfigured devices.
- Being a curated CSE, its source list ages; broken or dead directory links are common, and coverage is patchy outside tourist areas.

## Overlaps ("do both")
- Complements map-based webcam layers (Windy, EarthCam maps) — this searches by keyword; those let you pan a map to find every camera near exact coordinates.

## Trust & verifiability
`trust: community` — a third-party Google CSE with no owned data; it only points at public webcam directories, so verify each feed's location and freshness at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webcam-search-engine |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
