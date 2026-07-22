---
id: openswitchmapsweb
name: OpenSwitchMapsWeb
description: Use when you have a `geolocation` (coordinates or a map view) and want to inspect that exact spot across 160+ map/imagery services in one click — returns geolocation corroboration across providers.
url: https://tankaru.github.io/OpenSwitchMapsWeb/index.html
category: geolocation
path:
- geolocation
bestFor: Jumping the same coordinates between Google, Bing, OSM, Yandex, satellite and 160+ other map services to cross-check a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source (web page, bookmarklet, and Chrome/Firefox extensions); no account.
opsec: passive
opsecNote: The switch page itself just builds outbound links, but clicking through queries each destination map provider (Google, Yandex, Baidu, etc.) with the target coordinates from your browser. Use a clean/sock-puppet browser and neutral IP; assume each provider logs the lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community project by tankaru (open-source on GitHub); it only redirects to third-party maps, so trust rests on those providers, not this switcher.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OpenSwitchMaps
tags:
- maps
- geolocation
- map-switcher
- satellite
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# OpenSwitchMapsWeb

> A one-click "map switcher": take one set of coordinates and open that identical spot in 160+ mapping and imagery services to cross-verify what's actually there.

## When to use
You have a `geolocation` — coordinates, or a location you're viewing in one map — and you want to check the same point in other providers because coverage, imagery date, labels, and detail differ wildly between them. Essential in geolocation/verification work: what's blurry or outdated on Google may be sharp on Yandex or Bing, and street-level, historical, or regional services (Mapillary, Baidu, national portals) fill gaps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tankaru.github.io/OpenSwitchMapsWeb/index.html and enter/paste your coordinates (or install the bookmarklet/extension so you can trigger it from any map you're already viewing).
2. The tool renders a list of 160+ services, each linking to the **same lat/long and zoom**.
3. Click through to compare — e.g. satellite imagery across Google/Bing/Esri, street-level via Mapillary/Yandex Panoramas, and regional providers for better local coverage.
4. Corroborate: confirm a `geolocation` by matching landmarks, imagery dates, and building shapes across independent providers.
5. Pivot: a confirmed spot feeds street-view enumeration, historical-imagery comparison, or nearby-camera/webcam lookups.

## Inputs → Outputs
- **In:** `geolocation` (coordinates / current map view)
- **Out:** `geolocation` — the same point opened across many providers for cross-verification (differing imagery, dates, detail)
- **Empty/negative result looks like:** every destination provider showing no/blank imagery for the coordinates — likely a data-void area rather than a tool failure.

## Gotchas & OpSec
- It doesn't host data — it only redirects; each linked service has its own coverage, imagery age, and terms.
- Some listed services are Japanese/regional and may be irrelevant to your area; scan for the providers with local coverage.
- OpSec: clicking through sends your target coordinates to each third-party provider; treat those queries as logged and use a sanitised browser.

## Overlaps ("do both")
- Pairs with street-level and webcam geolocation tools: OpenSwitchMaps gets you into the right provider fast, while those confirm ground-truth detail at the spot.

## Trust & verifiability
`trust: unverified` — an open-source convenience layer that merely constructs links; verifiability comes from the underlying map providers you land on, so corroborate across several rather than trusting any single one.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openswitchmapsweb |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
