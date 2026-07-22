---
id: ukraine-war-map-heatmap
name: Ukraine War Map/Heatmap
description: Use when you have a `geolocation` in the Ukraine conflict zone and want to see control/activity over time — returns a time-animated map of frontline and event density.
url: https://ruarq.github.io/ukraine-war-heatmap
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Visualising how territorial control and conflict activity around a location in Ukraine changed over time.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open-source web visualisation hosted on GitHub Pages; no account or payment.
opsec: passive
opsecNote: A static client-side web map — you load public data, contacting no target and disclosing nothing about a subject. Standard browsing; a VPN keeps even the map request private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/open-source visualisation built on aggregated open-source conflict reporting; it inherits the lag and error of its upstream data and is not an official source.
missingPersonsRelevance: low
coverage:
- ua
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ukraine-war-heatmap
- ruarq ukraine war map
tags:
- conflict-mapping
- geospatial
- ukraine
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Ukraine War Map/Heatmap

> A free, open-source time-animated heatmap of the war in Ukraine — useful for placing a location in its conflict context: who controlled it and how active it was, when.

## When to use
You have a `geolocation` inside the Ukraine conflict zone — from a photo, a report, a claimed movement — and want the temporal context: what side controlled that area at a given date, and how intense activity was around it over time. It supports conflict-zone verification and timeline work (e.g. does a claimed event at a place/date fit the known control situation) rather than finding an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ruarq.github.io/ukraine-war-heatmap in a browser.
2. Navigate/zoom to your candidate `geolocation`.
3. Use the time controls to scrub through dates and read the control/activity heat around that point.
4. Pivot: cross-check what you see against a primary control map (e.g. ISW/DeepState) and against imagery/reporting for the same date before drawing conclusions.

## Inputs → Outputs
- **In:** a `geolocation` / area within Ukraine + a date of interest
- **Out:** a time-resolved `geolocation` picture — control side and conflict-activity density around that point over time
- **Empty/negative result looks like:** sparse or no heat for a location/date, or coverage that lags real events — treat gaps as "no aggregated data here yet," not as "nothing happened."

## Gotchas & OpSec
- It is a **derived visualisation** of upstream open-source data, so it carries that data's lag, gaps, and bias — never cite it as an authoritative or real-time control map.
- Good for context and corroboration, not for precise frontline calls on a specific hour/street.
- OpSec: fully passive; loading a static map discloses nothing about any subject.

## Overlaps ("do both")
- Pair with authoritative frontline maps (ISW, DeepStateMap) and satellite imagery — this gives an at-a-glance temporal heat view, while those give sourced, dated control lines to verify against.

## Trust & verifiability
`trust: community` — an open-source hobby/community project; transparent but unofficial, so always confirm any control or activity claim against a primary conflict-mapping source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukraine-war-map-heatmap |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
