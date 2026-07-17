---
id: poweroutage
name: PowerOutage.us
description: Use when you have a `geolocation`/region and a time and want to confirm whether a power outage was occurring there — returns live and historical outage data as event corroboration.
url: https://poweroutage.com/
category: geolocation
path:
- geolocation
bestFor: Confirming or timing a power outage in a specific area (US/Canada/UK) to corroborate or challenge a claim about conditions at a place and moment.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The live map and regional outage counts are free to view; bulk data, historical exports, alerts, and the API are enterprise/paid.
opsec: passive
opsecNote: Viewing aggregate outage maps reveals nothing about any individual and touches no target. Purely passive situational data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely referenced aggregator pulling from utility companies' own outage reporting; coverage is high in the US/Canada/UK but data is aggregate (utility/county level), not address-precise.
missingPersonsRelevance: low
coverage:
- us
- ca
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- PowerOutage.us
- poweroutage.com
tags:
- maps-geolocation-and-transport
- infrastructure
- situational-awareness
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# PowerOutage.us

> A live and historical map of electricity outages aggregated from utility reporting across the US, Canada, and UK — a way to check "was the power out there, then?"

## When to use
Corroboration and timeline work: a statement, post, or photo implies conditions at a place ("the lights went out," a dark neighbourhood at night, "we lost power for two days"). PowerOutage lets you check whether an outage was actually occurring in that region at that time — supporting or undermining a claim, or explaining why a subject was offline/uncontactable during a window. Aggregate, not address-level, so it sets context rather than pinpointing a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://poweroutage.com/ and select the country (US/Canada/UK).
2. Zoom the live map to the `geolocation`/region of interest; read the current outage counts by utility/county.
3. For a past event, use the historical/records view (some historical depth is free; deep exports are paid) to check the relevant date.
4. Note the scale and timing of any outage in that area.
5. Pivot: an confirmed outage window → align with a subject's last-contact timeline; a region + date → local news/social for on-the-ground detail.

## Inputs → Outputs
- **In:** `geolocation` / region + a time of interest
- **Out:** outage presence, scale, and timing for that area (aggregate `geolocation`-level)
- **Empty/negative result looks like:** zero outages reported for the area/time — conditions were normal, or the utility doesn't report to the aggregator. Absence at aggregate level doesn't rule out a very local outage.

## Gotchas & OpSec
- **Aggregate, not address-level:** it tells you a county/utility had outages, not that a specific house did.
- Free tier is the live/basic view; granular historical data and the API are paid.
- Coverage gaps exist where small utilities don't publish outage feeds.

## Overlaps ("do both")
- Pairs with local news and weather-history tools — an outage plus a storm record and local reporting together build a defensible picture of conditions at a place and time.

## Trust & verifiability
`trust: community` — a well-regarded aggregator of utilities' own reports. Reliable at the aggregate level it publishes; do not over-read it to individual addresses, and corroborate timing with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | poweroutage |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
