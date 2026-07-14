---
id: worldtimelapse-mapping-website
name: WorldTimeLapse Mapping Website
description: Use when you have a `geolocation`/`address` and want to see how that place changed year-by-year in satellite imagery (1984–present) — returns time-lapse imagery of the location.
url: http://world.time.com/timelapse
category: geolocation
path:
- geolocation
bestFor: Viewing decades of annual satellite imagery for a location to see construction, terrain and land-use change over time.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free. The original Time-hosted URL (world.time.com/timelapse) is legacy; the live project is Google Earth Timelapse (earthengine.google.com/timelapse or g.co/Timelapse).
opsec: passive
opsecNote: Fully passive — you view public satellite imagery of a place, not the subject. Nothing is sent about any person and no target is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The imagery comes from the Google Earth Timelapse project (Google Earth Engine with Carnegie Mellon CREATE Lab) — authoritative satellite data. The Time.com URL is a defunct legacy pointer; use the Google endpoint.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Earth Timelapse
- Timelapse
- world.time.com/timelapse
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# WorldTimeLapse Mapping Website

> Time-lapse satellite imagery of any location from 1984 to the present — originally hosted by Time, now the Google Earth Timelapse project.

## When to use
You have a `geolocation` or `address` and want to see how that exact place has changed over the decades: when a building went up, when a road or lake appeared or vanished, how land use shifted. This is powerful for verifying or dating imagery, checking whether a structure existed at a claimed time, and understanding the historical state of a last-known location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Google Earth Timelapse app at earthengine.google.com/timelapse (or g.co/Timelapse). The legacy world.time.com/timelapse URL is defunct — go straight to the Google endpoint.
2. Use the search bar to enter the place name, `address`, or coordinates.
3. Play the time-lapse: it scrubs through annual satellite composites from 1984 onward.
4. Read the output: the visual change history of the location (`geolocation`). Note the years when notable changes occur.
5. Pivot: dated changes corroborate or contradict other imagery/testimony; the confirmed coordinates feed mapping and current-imagery tools for present-day detail.

## Inputs → Outputs
- **In:** `geolocation`/`address` (a place or coordinates)
- **Out:** `geolocation` — an animated multi-decade satellite history of that spot
- **Empty/negative result looks like:** the place resolves but shows little visible change, or very remote areas have coarse imagery — the tool always renders *something* for a valid location; a blank is a bad query, not a data gap.

## Gotchas & OpSec
- The original Time-hosted URL is dead; don't rely on it — use the Google Earth Timelapse endpoint.
- Imagery is annual, cloud-composited, and moderate-resolution — good for macro change, not for reading a license plate or a person.
- OpSec: fully passive; no subject interaction.

## Overlaps ("do both")
- Pairs with current high-resolution satellite/street-level tools — Timelapse shows *how a place changed over years*, those show *what it looks like now* in detail. Use both to date and confirm a location.

## Trust & verifiability
`trust: trusted` — the imagery is from Google Earth Engine's Timelapse (with CMU's CREATE Lab), an authoritative satellite source. The only caveat is the stale Time.com URL; the underlying data is reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldtimelapse-mapping-website |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
