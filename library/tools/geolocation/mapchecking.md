---
id: mapchecking
name: MapChecking
description: Use when you need a defensible crowd-size estimate for an area in a photo/video — returns an estimated headcount for a drawn geolocation polygon.
url: https://www.mapchecking.com/
category: geolocation
path:
- geolocation
bestFor: Estimating how many people could fit in a defined area (crowd-size sanity check) by drawing a polygon on a map and setting a density.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account.
opsec: passive
opsecNote: You draw on a map and it computes area times density; no lookups, no contact with any target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known crowd-estimation utility; output is an area-times-density model, only as good as your polygon and density assumption.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
- crowd-estimation
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MapChecking

> Crowd-size estimator — draw a polygon over a real map, pick a crowd density, and it computes how many people that area can hold.

## When to use
You have imagery of a gathering near a known `geolocation` (a vigil, a search party, an event a subject may have attended) and need a sanity-check on claimed attendance, or you want to estimate how many people could be in a bounded area. It is a geometry/density calculator, not a way to find or identify anyone, so its direct value to locating a missing person is low — it is mainly for vetting crowd claims in associated reporting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mapchecking.com/ and navigate to the real-world location.
2. Click to draw a polygon around the occupied area.
3. Set the crowd density (the tool offers light/dense presets — people per square meter).
4. Read the estimated headcount range; vary the density to get a low/high bound.

## Inputs → Outputs
- **In:** `geolocation` (a polygon you draw) plus a density assumption
- **Out:** `geolocation` (the measured area) and an estimated person count
- **Empty/negative result looks like:** not applicable — it always returns a number; a misleading result comes from a sloppy polygon or an unrealistic density, not an "empty" state.

## Gotchas & OpSec
- The estimate is only as honest as your polygon boundary and density choice; report it as a range, never a precise figure.
- It models capacity, not actual occupancy — a full polygon does not mean the crowd filled it.
- OpSec: passive; pure calculation.

## Overlaps ("do both")
- Use a measurement/imagery tool (e.g. `[[mapquest]]` map, satellite imagery) to fix the real area, then MapChecking to estimate the count.

## Trust & verifiability
`trust: community` — a widely cited crowd-estimation tool. The math is sound; the result's credibility depends entirely on the inputs you choose, so always present a bounded range.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapchecking |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
