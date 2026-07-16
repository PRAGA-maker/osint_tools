---
id: geoportail-france
name: Géoportail (France)
description: Use when you have a French `address`/`geolocation` and want authoritative national maps and imagery — returns high-res aerial photos, cadastral parcels, topographic layers, and precise coordinates.
url: https://www.geoportail.gouv.fr/
category: geolocation
path:
- geolocation
bestFor: Authoritative French mapping — aerial/satellite imagery, cadastre, and topographic layers for a location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free national geographic portal operated by IGN; no account required for interactive use (API/keys available for developers).
opsec: passive
opsecNote: Passive lookup of published government map data — no subject is notified. Standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by IGN (France's national mapping agency) — authoritative, official cartographic and cadastral data.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: true
localInstall: false
registration: false
aliases:
- Geoportail
- geoportail.gouv.fr
- IGN Géoportail
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- journal-officiel-gouv-fr
---

# Géoportail (France)

> France's official national mapping portal (IGN) — layered, authoritative maps: high-resolution aerial imagery, cadastral parcels, and topographic data for any French location.

## When to use
You have a French `address` or `geolocation` and need precise, official map context: high-res aerial photography (often sharper/more current than global providers over France), the cadastre (parcel boundaries and numbers), historical aerial imagery, and topographic layers. Strong for verifying/geolocating a location, understanding a property's parcel, and comparing imagery over time in a French missing-person or asset case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.geoportail.gouv.fr/ and search the `address` or coordinates.
2. Toggle layers: aerial photography, cadastre (parcelles), topographic maps, and historical imagery.
3. Read coordinates and parcel identifiers; compare current vs historical aerial layers to see change over time.
4. Use the measurement and street-level integration tools to analyse the site.
5. Pivot: precise `geolocation`/parcel feeds the cadastre for ownership context; imagery corroborates a geolocated photo; cross-check `[[mapillary-2]]` for ground-level views.

## Inputs → Outputs
- **In:** French `address`/`geolocation`
- **Out:** high-res aerial `image`ry, cadastral parcels, topographic layers, precise `geolocation`/coordinates
- **Empty/negative result looks like:** location outside French coverage (it's France + overseas territories only) or an address that won't geocode — try coordinates or a nearby landmark.

## Gotchas & OpSec
- Scope: France and French overseas territories only — not a global tool.
- Cadastre shows parcels, not owner names directly (ownership is via separate services); use it for the geography, not identity.
- OpSec: passive; official public data, nobody is notified.

## Overlaps ("do both")
- Pairs with `[[mapillary-2]]` and global satellite tools — Géoportail gives authoritative French aerial/cadastral data, street-level and satellite tools add complementary angles.

## Trust & verifiability
`trust: trusted` — IGN's official national data; imagery and cadastral information are authoritative for France.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoportail-france |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
