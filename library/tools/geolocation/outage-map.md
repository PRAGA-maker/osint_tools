---
id: outage-map
name: Utility Outage Map (Toronto Hydro)
description: Use when you have a `geolocation`/`address` and a time and want to confirm a power outage there — utility outage maps corroborate blackout events and timelines.
url: https://www.torontohydro.com/outage-map
category: geolocation
path:
- geolocation
bestFor: Corroborating whether (and when) a power outage affected a specific area, using a utility's live outage map.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public outage map from the utility; no account. (This entry uses Toronto Hydro as the example; most electric utilities publish an equivalent map for their service area.)
opsec: passive
opsecNote: Passive read of a public utility map; you disclose only your own view, nothing about a subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the electric utility itself (Toronto Hydro), so outage data is first-party — though maps are near-real-time and typically don't retain long history.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Toronto Hydro outage map
- power outage map
tags:
- outages
- geolocation
- event-corroboration
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Utility Outage Map (Toronto Hydro)

> A utility's live power-outage map — a way to confirm whether a blackout hit a specific area at a given time, useful for corroborating events and timelines. (Toronto Hydro here; every utility publishes its own for its territory.)

## When to use
You have a `geolocation`/`address` and a claim or clue that involves a power outage — a subject says the power was out, a camera/feed went dark, a timeline hinges on a blackout, or you're corroborating storm/event impact. A utility outage map shows current (and sometimes recent) outages by area with cause and estimated restoration. For anywhere outside a given utility's territory, find that region's electric utility and use its equivalent map. It corroborates place/time events, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Identify the electric utility serving the target `geolocation` (Toronto Hydro for central Toronto; otherwise the local provider).
2. Open its outage map (e.g. https://www.torontohydro.com/outage-map) and navigate to the area.
3. Read active outages: affected zone, customers impacted, cause, and estimated restoration time.
4. Note timing to corroborate or contradict a claimed blackout window; screenshot promptly (maps refresh and don't keep history).
5. Pivot: cross-check with news, social posts, and weather for the same area/time to build a corroborated event picture.

## Inputs → Outputs
- **In:** `geolocation`/`address` (+ the relevant utility) and a time of interest
- **Out:** whether an outage affected that area, with zone, cause and restoration estimate (`geolocation`-scoped event confirmation)
- **Empty/negative result looks like:** no current outage shown — either there is none now, or the outage already resolved (most maps show only live status, not past events); capture in real time and use news/archives for history.

## Gotchas & OpSec
- OpSec: passive; nothing about your target is disclosed.
- Coverage is per-utility — this specific URL only covers Toronto Hydro's territory; you must find the right provider elsewhere.
- Live-only: outage maps rarely retain history, so screenshot immediately and corroborate past events with news/archives.

## Overlaps ("do both")
- Do both with webcam feeds (`[[city-webcams-com]]`), weather, and social monitoring — an outage map confirms the power event; those show its on-the-ground effect and timing.

## Trust & verifiability
`trust: trusted` — first-party utility data for current outages; reliable in the moment, but capture it live since it isn't archived.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | outage-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
