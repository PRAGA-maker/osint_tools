---
id: cellular-towers-map-canada
name: Cellular Towers Map (Canada)
description: Use when you have a Canadian `geolocation`/`address` and want to identify nearby licensed cellular tower sites and their operators — returns tower locations and provider info.
url: http://www.ertyu.org/steven_nikkel/cancellsites.html
category: geolocation
path:
- geolocation
bestFor: Locating Canadian cell tower sites near a point and identifying which carrier operates them.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public map built from Industry Canada / ISED spectrum-licence data.
opsec: passive
opsecNote: Reads a static public dataset of licensed tower sites; no target, account, or query is exposed to any subject. Fully passive. This maps infrastructure, not people or devices — it cannot locate a phone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing independent project by Steven Nikkel using official Canadian spectrum-licence records. Data can lag the regulator; treat as approximate.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cellmapper
- opencellid
aliases:
- Canadian Cellular Towers
- ertyu.org cell sites
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- cell-towers
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Cellular Towers Map (Canada)

> A free map of licensed Canadian cell tower sites by location and carrier, derived from official spectrum-licence data.

## When to use
You are working a Canadian `geolocation` or `address` — say interpreting which network a device could have used, corroborating a photo's setting, or understanding coverage near a last-known location — and want to see which cellular tower sites exist nearby and who operates them. This is infrastructure context, not device tracking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ertyu.org/steven_nikkel/cancellsites.html.
2. Navigate/zoom the map to the Canadian area of interest, or search by location.
3. Filter by service provider if you only care about one carrier's sites.
4. Read the tower markers (site location, operating carrier). Pivot: cross-check with a live crowd-sourced database like `[[cellmapper]]` or `[[opencellid]]` for cell IDs and more current coverage.

## Inputs → Outputs
- **In:** `geolocation`/`address` (Canadian)
- **Out:** `geolocation`/`address` of nearby tower sites plus operating carrier
- **Empty/negative result looks like:** no markers in view — rural/uncovered area, or the dataset hasn't captured a newer site; sparse results don't mean zero coverage.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a static public dataset; nothing about your subject is disclosed.
- Canada-only, and data derived from licence records can lag reality — treat positions as approximate and confirm against a live source for anything decision-critical.

## Overlaps ("do both")
- Pairs with `[[cellmapper]]` and `[[opencellid]]` — those are crowd-sourced, near-real-time, and global with cell IDs; this gives licensed-site context specifically for Canada.

## Trust & verifiability
`trust: community` — an independent, long-lived project built on official Canadian spectrum-licence data. Authoritative source, but the map is a third-party rendering that may lag; verify critical points against ISED or a live database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cellular-towers-map-canada |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
