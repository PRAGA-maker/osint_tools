---
id: map-of-syrian-civil-war
name: Map of Syrian Civil War (Liveuamap)
description: Use when you have a Syrian `geolocation` and date and want to know what conflict events (strikes, clashes, control changes) were reported there and when — returns dated, mapped `geolocation` events with sources.
url: https://syria.liveuamap.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Establishing what conflict activity was reported at a place and time in Syria, with links to source posts.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The live map is free to browse; historical time-travel (viewing the map on a past date) and some features require a paid subscription.
opsec: passive
opsecNote: You read a published news map; nothing you do here touches a subject or a location. Fully passive. As with any single OSINT feed, corroborate before treating a marker as fact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Liveuamap aggregates social-media and news reports into map markers in near-real-time; fast and useful for situational awareness, but individual markers are crowd/OSINT-sourced and can be wrong or propagandised — verify each via its linked source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- liveuamap
- live-universal-awareness-map
- ukraine-liveuamap-com
aliases:
- Syria Liveuamap
- syria.liveuamap.com
- Liveuamap Syria
tags:
- conflict-map
- situational-awareness
- liveuamap
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Map of Syrian Civil War (Liveuamap)

> Liveuamap's Syria instance: a near-real-time, source-linked map of conflict events — airstrikes, clashes, territorial control, incidents — across Syria.

## When to use
You have a Syrian `geolocation` and a date and need the conflict context: what was reported happening there and when. Useful when a subject was last known near a location, when corroborating a claim about events at a place, or when scoping whether an area was under a particular faction's control at a given time. Each marker links to the source post it was built from, so it doubles as a discovery tool for on-the-ground reporting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://syria.liveuamap.com/ and zoom to the area of interest.
2. Click markers to read the event summary and, crucially, follow the linked source (tweet, news item, video) back to the original report.
3. To see the map as it stood on a past date, use the time-travel/date controls (historical view is a paid feature).
4. Verify each marker independently — confirm the source, cross-check against other feeds, and watch for propaganda/misattribution.
5. Pivot: a linked source video/photo feeds geolocation and verification tools; a confirmed control/event window feeds your timeline.

## Inputs → Outputs
- **In:** `geolocation` (a place in Syria) + date/date range
- **Out:** `geolocation` — dated, mapped conflict events with linked source reports and approximate control lines
- **Empty/negative result looks like:** no markers in the area/time — either nothing was reported/aggregated there, or the reporting is below the feed's threshold; absence is not proof nothing happened.

## Gotchas & OpSec
- Single-feed risk: markers are aggregated from social/OSINT sources and can be inaccurate, delayed, or deliberately manipulated — never treat one marker as confirmed; always open the source.
- Paywalled history: the free view is roughly "now"; viewing past-dated maps needs a subscription.
- Approximate geocoding: markers are placed to the reported area, not to a precise coordinate.
- OpSec: fully passive.

## Overlaps ("do both")
- Same platform family as `[[liveuamap]]`, `[[live-universal-awareness-map]]`, and `[[ukraine-liveuamap-com]]` — and best paired with a rigorous event dataset (e.g. ACLED) for verified coding, using Liveuamap for speed and source links and the dataset for confirmed history.

## Trust & verifiability
`trust: community` — a crowd/OSINT-sourced live map: excellent for speed and for surfacing primary sources, but each marker must be verified through its linked source before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-of-syrian-civil-war |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
