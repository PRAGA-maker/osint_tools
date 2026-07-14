---
id: nyc-crime-map
name: NYC Crime Map
description: Use when you have a New York City `address` or `geolocation` and want the local crime picture — returns mapped NYPD crime incidents by area, type and time.
url: http://maps.nyc.gov/crime/
category: geolocation
path:
- geolocation
bestFor: Understanding the crime context around a specific NYC address or neighborhood.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official City of New York / NYPD tool; no account.
opsec: passive
opsecNote: Fully passive — you browse an official public map, nothing is attributed to any subject. It shows area/incident data, not individuals, so there's no personal-data leakage about a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official NYPD/City of New York crime data (now served via the City's ArcGIS mapping); authoritative for reported incidents, with the usual caveats that not all crime is reported or precisely geocoded.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- spotcrime
- crimereports
aliases:
- NYPD crime map
- maps.nyc.gov/crime
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- crime
- nyc
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# NYC Crime Map

> The City of New York's official NYPD crime map — mapped, filterable reported incidents for building area context around a New York City location.

## When to use
You have a NYC `address` or `geolocation` and want the crime context around it: what incident types are reported nearby, how frequent, and when. This is environmental/contextual intelligence — useful for understanding a location tied to a subject (a last-known address, a scene, a neighborhood), corroborating an event, or assessing an area. It maps incidents, not people, so it complements person-centric tools rather than replacing them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://maps.nyc.gov/crime/ (it now redirects to the City's ArcGIS-hosted crime map).
2. Navigate to the `address`/neighborhood of interest or search for it.
3. Filter by crime type and time period to read the local incident pattern.
4. Read incident markers for type, approximate location, and date/time.
5. Pivot: an area crime pattern contextualises a subject's last-known location; a specific incident can be cross-referenced with news, court records (`[[courts-and-tribunals-judiciary]]`-style sources), or NYPD precinct reporting.

## Inputs → Outputs
- **In:** `address` or `geolocation` (within NYC)
- **Out:** mapped `geolocation` crime incidents — type, approximate location, date/time, frequency
- **Empty/negative result looks like:** a map area with no plotted incidents for your filters — meaning no *reported* crimes of that type/time there, which understates reality (unreported crime, geocoding to intersections, reporting lag).

## Gotchas & OpSec
- NYC only — outside the five boroughs, use a national crime-map tool.
- Reported-crime bias: absence of markers ≠ absence of crime; locations are often approximated to protect victims.
- Contextual, not person-level — it won't name anyone; pair it with person-centric sources.

## Overlaps ("do both")
- Pairs with `[[spotcrime]]` and `[[crimereports]]` (national/multi-jurisdiction crime maps) — use those outside NYC and to cross-check, since aggregators and the official map can differ in coverage and freshness.

## Trust & verifiability
`trust: trusted` — official NYPD/City data. Authoritative for reported, geocoded incidents; interpret gaps as reporting/geocoding limits, not as ground truth about safety.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nyc-crime-map |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
