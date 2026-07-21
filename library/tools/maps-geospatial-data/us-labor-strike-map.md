---
id: us-labor-strike-map
name: US Labor Strike Map
description: Use when you have a US `geolocation`/date and want labor-action context — returns mapped strikes/pickets by place and time to situate an event or a subject's whereabouts.
url: https://www.google.com/maps/d/viewer?mid=1hE1nDR-Ff_sVgOS67IteJSxGZlvqIP3k
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: A crowd-curated Google My Map plotting US labor strikes and actions by location, employer and date for situational context.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free to view (a public Google My Map); a Google account is only needed to save/copy it, not to browse.
opsec: passive
opsecNote: A public map you read — no target interaction and nothing leaked about a subject. Viewing is anonymous; you are looking at aggregated event pins, not querying anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A user-maintained Google My Map, not an official labor-statistics source; pins are crowd-curated and may be incomplete or dated — corroborate specific actions against news/union sources.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Labor strike tracker map
tags:
- maps
- labor
- context
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# US Labor Strike Map

> A crowd-curated Google My Map plotting US labor strikes, pickets and actions by place, employer and date — situational context, not a people-finder.

## When to use
You have a US `geolocation` and/or a date and want to know whether labor unrest (a strike, picket, walkout) was happening there and then — to situate an event, understand why a workplace or area was disrupted, or corroborate a subject's stated reason for being somewhere. It is context/background layered on a map, not a lookup that returns an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map link in a browser (no login to view).
2. Pan/zoom to the area of interest, or use the map's search/layers to filter.
3. Click a pin to read its details — employer/organisation, date, action type, and any linked source.
4. Cross-check the pin's date/place against your timeline.
5. Pivot: an employer named on a pin → company records and news; a place+date → local news archives for people and details the map omits.

## Inputs → Outputs
- **In:** a US `geolocation` (and optionally a date window)
- **Out:** mapped labor actions with `employer-org`, date and location context (`geolocation`)
- **Empty/negative result looks like:** no pins for your area/date — the map is crowd-curated and far from complete, so absence is not evidence no action occurred; confirm via news/union records.

## Gotchas & OpSec
- Unofficial and incomplete — a single maintainer's dataset, not Bureau of Labor Statistics; treat coverage as partial.
- Pins can be dated or sourced from secondary reporting; follow the linked source before relying on a detail.
- Fully passive; viewing needs no account.

## Overlaps ("do both")
- Complements local news archives and union sources — the map gives the where/when at a glance, those provide the who and the confirmed detail.

## Trust & verifiability
`trust: community` — a helpful but unofficial crowd map; verify any specific strike/action against contemporaneous news or the union involved before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-labor-strike-map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
