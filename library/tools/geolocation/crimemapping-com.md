---
id: crimemapping-com
name: CrimeMapping.com
description: Use when you have a `geolocation`/address and want recent reported crime around it — an interactive map of incidents from participating US law-enforcement agencies by area and date range.
url: https://www.crimemapping.com/
category: geolocation
path:
- geolocation
bestFor: Checking recent reported crime incidents near an address/area from official US police feeds.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public map. No account needed to browse; incident feeds come from participating agencies (coverage is patchy where an agency doesn't publish).
opsec: passive
opsecNote: You browse a public crime map — nothing about your subject is submitted and no agency is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Motorola Solutions, sourcing incidents directly from participating law-enforcement agencies; data is official but only as complete as which agencies contribute.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Crime Mapping
- crimemapping.com
tags:
- crime
- maps
- geolocation
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# CrimeMapping.com

> An official-feed crime map for the US — pick an area and date window and see the reported incidents participating police agencies have published there.

## When to use
You have an `address`/`geolocation` connected to your subject (a home, a last-known location, a scene) and want situational context: what kinds of crimes were reported nearby and when. In a missing-persons or safety assessment this helps characterise an area and surface incidents that might correlate with a timeline. It maps *reported incidents by location and time*; it does not name individuals or let you search by person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.crimemapping.com/ and search the address, city, or agency, or navigate the map to the area.
2. Set the **date range** (last 24 hours / week / month, or custom) and the **crime-type** filters.
3. Read the plotted incidents — each pin carries type, approximate location (often block-level, not exact), and date/time.
4. Note gaps: if the agency covering that area doesn't participate, you'll see no data even where crime occurred.
5. Pivot: incident dates/types feed a timeline; corroborate specific incidents with the agency's own reports or local news, and cross-check another crime-map source.

## Inputs → Outputs
- **In:** `address`/`geolocation`/agency + date range
- **Out:** mapped reported crime incidents (type, block-level `geolocation`, date/time) for that area
- **Empty/negative result looks like:** an empty map — usually means the local agency doesn't publish to CrimeMapping (coverage gap), **not** that the area is crime-free. Confirm coverage before drawing conclusions.

## Gotchas & OpSec
- **Coverage is agency-dependent** — only participating US departments feed it; many areas are blank. Absence ≠ safety.
- Locations are deliberately generalised (block/intersection level), and there's reporting lag; treat timing/precision as approximate.
- Reflects *reported* crime only, with each agency's classification quirks.

## Overlaps ("do both")
- Complements other crime-map/police-feed sources (e.g. agency dashboards, LexisNexis Community Crime Map): coverage differs by jurisdiction, so check more than one for any given area, and pair with local news for detail on a specific incident.

## Trust & verifiability
`trust: trusted` — run by Motorola Solutions and fed directly by participating law-enforcement agencies, so incidents are official records. The limitation is completeness, not authenticity: only contributing agencies appear, and locations are generalised.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crimemapping-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
