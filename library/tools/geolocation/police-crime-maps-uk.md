---
id: police-crime-maps-uk
name: Police Crime Maps (UK)
description: Use when you have a UK `address`/`geolocation` and want the area's recent recorded-crime picture plus the local policing team — returns street-level crime categories and neighbourhood contact details.
url: https://www.police.uk/
category: geolocation
path:
- geolocation
bestFor: Area-level UK crime context and the responsible neighbourhood policing team for a postcode/address.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official UK service; no account or payment required. Underlying crime data is also downloadable in open format.
opsec: passive
opsecNote: Passive, anonymous lookup of published area statistics — no individual is queried or notified. Crime locations are deliberately snapped to approximate map points, not exact addresses.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official service run by the UK Home Office / police forces of England, Wales and Northern Ireland — authoritative recorded-crime data (published with a ~2-month lag).
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- police.uk
- UK street-level crime map
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Police Crime Maps (UK)

> The official UK street-level crime map — turns a postcode or address into an area crime picture and the contact details for the responsible neighbourhood policing team.

## When to use
You have a UK `address` or `geolocation` and want context about that place: what categories of crime have been recorded on those streets recently, and which neighbourhood policing team and station is responsible. This is an **area/context** tool, not a person-finder — useful for understanding the environment around a last-known location and for identifying the local police contact to approach in a missing-person case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.police.uk/ and enter a postcode, street, or area.
2. View the crime map: dots mark the approximate locations of crimes reported in the last month(s), grouped by category (burglary, violence, anti-social behaviour, etc.).
3. Tap a neighbourhood boundary to see the local policing team, their priorities, the station, and contact details.
4. For analysis, download the open crime dataset or use the data API rather than reading the map.
5. Pivot: the neighbourhood team contact is a real lead in a missing-person case; crime context informs risk assessment of a location.

## Inputs → Outputs
- **In:** `geolocation`/`address` (postcode, street, or area)
- **Out:** area `geolocation` crime categories/counts, responsible policing team and station `address`/contacts
- **Empty/negative result looks like:** few or no crimes shown for the area, or "no data" for very recent months (data lags ~2 months). Absence of dots means low recorded crime, not that nothing happened — and it never identifies individuals.

## Gotchas & OpSec
- Not individual-level: locations are snapped to representative map points to protect privacy; you cannot derive a specific person or exact address from it.
- Lag: data is published roughly two months behind — recent events won't appear yet.
- Coverage: England, Wales, and Northern Ireland (Scotland is separate).

## Overlaps ("do both")
- Pairs with mapping/geolocation tools that place a subject's known address, and with local-news searches — police.uk gives official recorded-crime context while news fills in specific incidents.

## Trust & verifiability
`trust: trusted` — an official Home Office/police service; the recorded-crime data is authoritative for area statistics, with the caveat that locations are approximate and lag ~2 months.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-crime-maps-uk |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
