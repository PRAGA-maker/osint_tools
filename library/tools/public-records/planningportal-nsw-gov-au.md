---
id: planningportal-nsw-gov-au
name: NSW Planning Portal Spatial Viewer
description: Use when you have an `address` in New South Wales and want the property's planning, zoning, and land context — returns geolocation, lot/parcel and council-area detail.
url: https://www.planningportal.nsw.gov.au/spatialviewer/#/find-a-property/address
category: public-records
path:
- public-records
bestFor: Turning a NSW street address into precise parcel, zoning, hazard, and council-area context on an official map.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free NSW Government service; no account, download, or plugin required.
opsec: passive
opsecNote: You query a government map by address; the subject is never contacted and the lookup is not tied to any account. Standard sock-puppet browser hygiene is enough — no login, no notification to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official NSW Government (Department of Planning) property/planning data — authoritative for zoning, parcel, and hazard layers.
missingPersonsRelevance: high
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- NSW Planning Portal Spatial Viewer
- planningportal.nsw.gov.au
tags:
- propertysites
- Property Related Sites
- australia
- property-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# NSW Planning Portal Spatial Viewer

> The NSW Government's official property map — enter an address and get the parcel, zoning, council area, and hazard overlays for that piece of land.

## When to use
You have a NSW `address` (from a lead, a document, or a self-reported location) and want to pin it to a real parcel and understand the property: exact lot/parcel identifier, land-use zone, council/LGA, and whether it sits in a bushfire, flood, or heritage area. It won't name the owner (that's the paid Land Registry), but it confirms an address is real, locates it precisely (`geolocation`), and gives council context for the next records request.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Spatial Viewer's **Find a property → Address** search.
2. Type the street address, suburb, and postcode; pick the correct match from the dropdown (or search by lot number).
3. The map zooms to the parcel. Read the property panel: lot/DP number, land-use zone, floor-space ratio, and applicable planning instruments.
4. Toggle hazard layers (bushfire, flood planning, heritage) to understand the site's context.
5. Pivot: the confirmed parcel + council area (`geolocation`) feeds a Land Registry title search (for ownership) and local-council development-application records for the address history.

## Inputs → Outputs
- **In:** `address` (or lot/DP number)
- **Out:** confirmed `address`, `geolocation` (precise parcel/coordinates), lot number, council/LGA, zoning and hazard context
- **Empty/negative result looks like:** the address doesn't resolve to a dropdown match — either mistyped, outside NSW, or not a titled parcel. Try the lot/DP number or a neighbouring address.

## Gotchas & OpSec
- No owner names: this is planning/zoning data, not a proprietor register — pair it with a paid title search for ownership.
- NSW-only; other Australian states have their own portals.
- OpSec: fully **passive** — no login, nothing sent to the subject.

## Overlaps ("do both")
- Pairs with land-registry/title and council DA-record tools — the Spatial Viewer confirms and locates the parcel; those tools attach ownership and building/development history to it.

## Trust & verifiability
`trust: trusted` — first-party NSW Government mapping; zoning, parcel, and hazard layers are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | planningportal-nsw-gov-au |
| category | public-records |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
