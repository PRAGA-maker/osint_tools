---
id: mapalist
name: MapAList
description: Use when you want to batch-plot a spreadsheet of addresses onto one map — geocodes an address list to mapped points (likely defunct; verify).
url: http://mapalist.com
category: geolocation
path:
- geolocation
bestFor: Batch-mapping a list/spreadsheet of addresses to plotted points for clustering and visual review.
selectorsIn:
- address
selectorsOut:
- geolocation
status: down
pricing: free
costNote: Was free with optional paid tiers; service appears defunct/unreachable — confirm before relying on it.
opsec: passive
opsecNote: Batch geocoding of addresses you supply; no contact with any target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legacy "map a list" address-plotting service; the domain appears inactive, so treat as unavailable until verified live.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- geospatial-research-and-mapping-tools
- batch-geocoding
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MapAList

> Legacy "map a list" tool for batch-plotting many addresses onto a single map — likely defunct; treat as unavailable unless you confirm it loads.

## When to use
You have a set of addresses — several last-known residences, a list of associates' homes, employer locations — and want them all plotted on one map at once to spot geographic clustering or a search radius. This is the use case MapAList was built for. However, the service appears inactive; use a current equivalent (Google My Maps, `[[maphub]]`, batch geocoding via `[[map-maker]]`) unless the site is confirmed working.

## How to use it (`bestInteractionPattern`: web-manual)
1. Attempt to open http://mapalist.com. If it does not load, stop and use a live alternative.
2. (If live) create an account, import your address list (typically from a spreadsheet/Google Sheet).
3. Let it geocode and plot the points; review the resulting map for clusters.
4. Pivot: a cluster of associate addresses can focus a canvass or imagery review.

## Inputs → Outputs
- **In:** `address` (a batch/list)
- **Out:** `geolocation` (plotted points)
- **Empty/negative result looks like:** the site fails to load, or — more importantly — verify whether it is even online before investing in it.

## Gotchas & OpSec
- Strong likelihood this service is defunct; do not present it as working without confirming the page loads.
- Required an account/spreadsheet import historically.
- OpSec: passive; only addresses you supply are processed.

## Overlaps ("do both")
- Superseded by `[[maphub]]` and Google My Maps for no-code batch plotting; use `[[map-maker]]` if you only need the coordinates.

## Trust & verifiability
`trust: unverified` — a legacy batch-mapping service whose domain appears inactive. Marked `status: down` pending a live check; prefer a current alternative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapalist |
| category | geolocation |
| selectorsIn → selectorsOut | address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
