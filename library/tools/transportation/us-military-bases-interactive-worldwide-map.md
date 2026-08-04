---
id: us-military-bases-interactive-worldwide-map
name: US Military Bases Interactive Worldwide Map
description: Use when you have a country or `geolocation` and want to check for nearby US military bases — returns base locations and counts plotted on an interactive world map.
url: https://worldbeyondwar.org/no-bases/
category: transportation
path:
- transportation
bestFor: Locating US foreign military bases by country and reading the linked context for each.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and publicly accessible; the maintaining NGO seeks donations but the map is not paywalled.
opsec: passive
opsecNote: Passive — you browse a public advocacy map; no case data is submitted and no subject is contacted. Nothing to leak beyond your own browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Maintained by World BEYOND War, an advocacy NGO; a self-described work-in-progress compiled from public sources, so counts/details may lag or be incomplete.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- World BEYOND War No Bases map
tags:
- Maps, Geolocation and Transport
- Military tracking
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# US Military Bases Interactive Worldwide Map

> A Mapbox/OpenStreetMap-based visual database of US foreign military bases (hundreds across dozens of countries) — a geolocation reference for placing installations near an area of interest.

## When to use
You have a country or approximate `geolocation` and want to know whether US military bases sit nearby — for context on a subject with a military connection, on activity around a known installation, or for background on a region. It is a reference layer, not a person-finder; use it to add geographic context, not to locate an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://worldbeyondwar.org/no-bases/.
2. Explore the interactive map, or use the dashboard to select a country (e.g. "USA: 800+ bases across 90+ countries").
3. Click map markers to see base locations and the counts per country.
4. Follow the linked articles/sources for context on individual bases.
5. Pivot: cross-reference a base's location against satellite imagery, personnel records, or local reporting for deeper detail.

## Inputs → Outputs
- **In:** `geolocation` (country/region of interest)
- **Out:** `geolocation` / `address` (plotted base locations), plus counts and links to source articles
- **Empty/negative result looks like:** no markers in a region — meaning no bases are recorded in this dataset there, not a guarantee none exist (the database is incomplete by the maintainers' own note).

## Gotchas & OpSec
- Advocacy-sourced and a work-in-progress: treat counts and coordinates as approximate leads, not authoritative.
- No personnel/opening-date granularity is guaranteed per base despite older descriptions — content varies by entry.
- Passive and safe to browse; corroborate any specific base fact against primary/official sources.

## Overlaps ("do both")
- Complements satellite/mapping tools — this gives the "where the bases are" layer; imagery tools confirm and detail a specific site.

## Trust & verifiability
`trust: unverified` — a useful advocacy visualisation but compiled from mixed public sources; verify any base's specifics against authoritative records before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-military-bases-interactive-worldwide-map |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
