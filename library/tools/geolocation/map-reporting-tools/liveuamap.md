---
id: liveuamap
name: LiveUaMap
description: Use when a case touches an active conflict/crisis zone and you need to map dated incidents in an area — returns geolocated events with source links.
url: https://liveuamap.com/
category: geolocation
path:
- geolocation
- map-reporting-tools
bestFor: Mapping dated conflict and crisis incidents in a region to contextualize a location or movement during unrest.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Public map is free; some features and ad-free/premium access are paid.
opsec: passive
opsecNote: Reads an aggregated public event map; no contact with the target and nothing about your search reaches them.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd/curated conflict-event aggregator; individual reports vary in reliability and must be traced to their cited source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Live Universal Awareness Map
tags:
- conflict
- crisis-mapping
- events
source: arf-seed
lastVerified: ''
enrichment: full
---

# LiveUaMap

> Live, curated map of conflict and crisis events (Ukraine and other theaters) — best for placing a location or movement in the context of dated incidents during unrest.

## When to use
Your case touches a conflict zone, disaster area, or region of active unrest and you have a `geolocation` you want to understand in time and context: which roads, checkpoints, strikes, or evacuation events were reported near that point on a given date. This helps explain why a route was closed, where displacement flowed, or what was happening around a last-known location. It is a context/situational-awareness layer — it does not contain personal records and rarely names individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://liveuamap.com/ and select the relevant theater/region.
2. Pan/zoom to your area and use the timeline to scrub to the date window of interest.
3. Click markers to read each incident summary and follow its cited source (news, social post).
4. Record the date, location, and source link for any incident relevant to your subject's movement.
5. Pivot: a road closure or front line near a last-known point reshapes which routes and areas to search.

## Inputs → Outputs
- **In:** `geolocation` (region/coordinate) plus an implicit date window
- **Out:** `geolocation` of dated incidents and per-event `metadata-exif` (timestamp, source link)
- **Empty/negative result looks like:** sparse or no markers in your area/time window — the map favors high-activity zones, so quiet regions yield little.

## Gotchas & OpSec
- Reliability varies per marker; always open and assess the cited source rather than trusting the pin alone.
- Coverage is heavily weighted to current major conflicts; older or low-profile events may be missing.
- Human-in-the-loop: you interpret events and verify sources.
- OpSec: passive; reading a public map leaks nothing to the subject.

## Overlaps ("do both")
- Pairs with imagery tools (`[[landsatlook-viewer]]`, `[[mapillary]]`) — LiveUaMap says what happened where and when; imagery confirms ground conditions.

## Trust & verifiability
`trust: community` — a curated/crowd-sourced conflict aggregator. The map is a lead generator; each incident's credibility rests on its underlying cited source, which you must check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | liveuamap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
