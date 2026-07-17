---
id: light-pollution-world-map
name: Light Pollution World Map
description: Use when you have a candidate `geolocation` and a night photo and want to test whether the sky brightness/darkness matches — returns a layered light-pollution map (by year since 2012) to corroborate or exclude a location.
url: https://www.lightpollutionmap.info/
category: geolocation
path:
- geolocation
bestFor: Corroborating a night-scene location by comparing observed sky glow against measured light-pollution data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse the interactive map and standard overlays. Some advanced overlays/data downloads are gated behind a paid tier, but the core map that supports geolocation reasoning is free.
opsec: passive
opsecNote: You browse a public map; no target is contacted. Fully passive. Use a VPN only for general hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates published scientific light-pollution datasets (e.g. VIIRS satellite radiance); the underlying data is authoritative, the site is a community-run viewer over it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- lightpollutionmap.info
- light pollution map
tags:
- Maps, Geolocation and Transport
- Nature
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Light Pollution World Map

> An interactive map of measured night-sky brightness (satellite radiance, year by year) — a corroboration layer for geolocating night photos and astronomical scenes.

## When to use
You have a night photograph with visible sky (stars faint or bright, city glow on the horizon) and one or more candidate `geolocation`s. Light-pollution data tells you how dark the sky *should* be at each candidate: a photo showing a rich starfield can't come from a city center, and strong sky glow rules out a remote dark-sky site. It won't pinpoint a location on its own, but it excludes or supports candidates and is a strong secondary check when combined with terrain, horizon, and star-field analysis. Direct person-finding relevance is low; it's a supporting geolocation technique.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.lightpollutionmap.info/.
2. Navigate to a candidate `geolocation` and read the color-coded radiance (Bortle-scale-like darkness) at that point.
3. Use the year selector to view historical layers (data from ~2012 onward) so the comparison matches the photo's era.
4. Compare the map's predicted darkness against what the photo actually shows (star visibility, horizon glow, direction of the nearest bright zone).
5. Pivot: a surviving candidate feeds terrain/horizon and star-field (e.g. astronomical) geolocation; the direction of a distant glow points toward the nearest population center.

## Inputs → Outputs
- **In:** a candidate `geolocation` (plus a night photo to reason against)
- **Out:** measured sky-brightness at that location and era — used to confirm or exclude the `geolocation`
- **Empty/negative result looks like:** the map is uniform/uninformative for your area, or the photo's sky is ambiguous — light pollution alone can't decide it; lean on other geolocation cues.

## Gotchas & OpSec
- Corroboration only: it narrows and excludes candidates, it does not locate a photo by itself.
- Match the data year to the photo's date; light pollution changes over time (LED conversions can raise or lower local radiance).
- OpSec: **passive** — browsing a public map; no target interaction.

## Overlaps ("do both")
- Pairs with terrain/horizon-matching and star-field geolocation: light pollution constrains the *region*, those pin the *point*.

## Trust & verifiability
`trust: community` — a community-run viewer over published scientific radiance datasets (e.g. VIIRS); the measurements are authoritative, so conclusions drawn carefully from them are defensible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | light-pollution-world-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
