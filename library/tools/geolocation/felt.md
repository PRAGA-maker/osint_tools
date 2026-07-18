---
id: felt
name: Felt
description: Use when you have `geolocation` points, an `address` list, or an `image`/map to annotate — returns a shareable interactive map with drawn features, exportable as image/GeoJSON.
url: https://felt.com/
category: geolocation
path:
- geolocation
bestFor: Quickly building a collaborative annotated map — plotting points, drawing routes/areas, geocoding an address list — and sharing or exporting it.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free tier for individuals (create/share maps); paid plans add larger data, private teams and database connectors. Signup required.
opsec: passive
opsecNote: Felt is a workspace, not a query against the target — plotting points doesn't touch the subject. But maps are cloud-hosted and shareable, and a public/link-shared map can leak your investigation; keep maps private, and use a sock-puppet account, if the work is sensitive.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Felt is an established commercial cloud-GIS product; it's an authoring/visualisation tool, so trust concerns the base map/data you bring, not a dataset Felt asserts.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- felt.com
- Felt maps
tags:
- Maps, Geolocation and Transport
- mapping
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Felt

> A fast, browser-based collaborative mapping canvas — drop pins, draw routes and areas, geocode an address list, and share or export the result.

## When to use
You're assembling geographic findings and need to **see and share** them on a map: plotting a subject's known locations, sketching a last-seen route or a search area, geocoding a spreadsheet of `address`es into points, or overlaying your own data on a base map. Felt is the working surface — it turns scattered `geolocation`/`address` data into a single annotated, shareable map you can hand to a team or export as evidence. It's for *organising and communicating* geo-intel, not for discovering it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up / log in at https://felt.com/ (use an investigative account) and create a new map.
2. Add data: drop pins at known `geolocation`s, draw lines/routes and polygons for areas, add labels/notes, or **drag-and-drop a spreadsheet of addresses** to auto-geocode them into points.
3. Choose a base map/background suited to the task (satellite, street, terrain).
4. Collaborate or export: share a private link with your team, or export to image/PDF/GeoJSON/GeoPackage for your case file.
5. Pivot: coordinates plotted here feed satellite-imagery and street-level review; the exported GeoJSON feeds other GIS tools.

## Inputs → Outputs
- **In:** `geolocation` points, an `address` list (geocoded), your own overlays/`image`
- **Out:** an interactive annotated map; exportable `geolocation` data (GeoJSON/GeoPackage) and images
- **Empty/negative result looks like:** n/a — Felt renders whatever you give it. A bad geocode (address placed in the wrong place) is the failure mode; eyeball plotted points against the base map.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** required to create/save maps.
- OpSec: **passive** toward the target, but your map lives in Felt's cloud and is easy to share — a mis-set "public" or link-shared map can expose your investigation. Keep maps private; use a sock-puppet account for sensitive work.
- It's an authoring tool: accuracy depends on the data you import and the geocoder's quality — verify geocoded points, especially for ambiguous or partial addresses.
- Free-tier limits apply to data size and private collaboration.

## Overlaps ("do both")
- Complements imagery and street-level tools — plot and organise locations in Felt, then verify each point in satellite/streetview. Export GeoJSON to move findings into a heavier GIS if needed.

## Trust & verifiability
`trust: trusted` — a mature commercial mapping platform; because it visualises *your* data, verifiability rests on the sources you import and the geocoding, not on Felt itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | felt |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
