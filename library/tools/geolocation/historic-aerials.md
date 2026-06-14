---
id: historic-aerials
name: Historic Aerials
description: Use when you have a `geolocation`/`address` and need decades of historical aerial photos and topo maps to see how a site changed over time.
url: https://www.historicaerials.com/?javascript=&
category: geolocation
path:
- geolocation
bestFor: Comparing a location's aerial imagery and topo maps across past decades.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free viewing of historical imagery; high-res prints/downloads and some features require purchase or an account.
opsec: passive
opsecNote: You browse archival imagery of a place; the target is never contacted. A free account unlocks more years/features.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: NETROnline's HistoricAerials.com, a long-standing US-focused historical imagery archive widely used in research and due diligence.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- land-viewer
- google-maps-update-alerts
aliases: []
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Historic Aerials

> A US-focused archive of historical aerial photography and topographic maps spanning back many decades, for seeing how a specific place changed over time.

## When to use
You have a `geolocation` or `address` (a property, a rural parcel, a last-known site) and need to know what it looked like in prior years — structures since demolished, old outbuildings, former access roads, changes to the land. Comparing eras can surface places someone could be, or confirm a witness's recollection of how a site used to look.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and search the `address` or navigate to the `geolocation`.
2. Use the year slider to step through available aerial captures and topo maps for that exact spot.
3. Compare eras to spot vanished structures, old roads, or land disturbance.
4. Cross-check the modern view in [[land-viewer]]; set up [[google-maps-update-alerts]] to catch future refreshes.

## Inputs → Outputs
- **In:** `geolocation` / `address`
- **Out:** time-series aerial imagery and historical topo maps for that point (`geolocation` context)
- **Empty/negative result looks like:** few or no historical layers for a location — coverage is strongest in the US and varies by county and era.

## Gotchas & OpSec
- Human-in-the-loop: a free account widens access; high-resolution downloads/prints are paywalled.
- Coverage is primarily US; rural/older years can be sparse.
- OpSec: passive — archival imagery only; the target is not contacted.

## Overlaps ("do both")
- Pairs with [[land-viewer]] (recent multispectral satellite) — Historic Aerials covers the past, Land Viewer covers the present. Use [[google-maps-update-alerts]] to monitor for new imagery.

## Trust & verifiability
`trust: community` — NETROnline's established historical-imagery service, widely cited in research; verify any specific capture's date label.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | historic-aerials |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
