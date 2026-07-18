---
id: geoprotests-api
name: geoprotests API
description: Use when you have a location/date and want geolocated protest-event records for that place and time — returns geolocation and address.
url: https://rapidapi.com/gisfromscratch/api/geoprotests/
category: geolocation
path:
- geolocation
bestFor: Querying geocoded protest/civil-unrest events by area and date range as structured points.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Hosted on RapidAPI with a free tier plus paid quota tiers; requires a (free) RapidAPI account and API key.
opsec: passive
opsecNote: You query a third-party event dataset, not the subject — nothing is disclosed to any person. Standard API-key hygiene applies; don't embed the key in shared notebooks.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: unverified
trustNote: Independent developer API (gisfromscratch) aggregating open protest-event data; coverage and freshness are not independently audited.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- geoprotests
- gisfromscratch geoprotests
tags:
- geospatial
- events
- protests
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# geoprotests API

> A RapidAPI endpoint that returns geocoded protest/civil-unrest events for a place and time window — useful for placing a subject at, or near, a known event.

## When to use
You have a `geolocation`/`address` and a rough date, and you want to know what protest or civil-unrest activity occurred there — for example, to contextualise a photo, corroborate a claim that someone attended a demonstration, or narrow where crowds (and cameras/livestreams) were on a given day. It returns event points you can plot, each with coordinates and a date.

## How to use it (`bestInteractionPattern`: api)
1. Create a free RapidAPI account and subscribe to the geoprotests API to get an API key.
2. Call the endpoint with your area of interest and date range (see the RapidAPI "Endpoints" tab for exact parameters and a live test console).
3. Parse the JSON response — each record is a protest event with coordinates and a timestamp.
4. Plot the points (any GIS/mapping tool) and cross-reference with the subject's timeline.
5. Pivot: event coordinates → look for livestreams/social posts geotagged nearby (`[[youtube-dl]]`, geosocial search); a confirmed event date/place → corroborate or refute a subject's stated movements.

## Inputs → Outputs
- **In:** `geolocation` (bbox/point) and/or `address`, plus a date range
- **Out:** `geolocation` (event points), `address` (place labels), event dates
- **Empty/negative result looks like:** an empty feature set for the area/date — meaning no protest events are recorded there in the source data (absence in an aggregated dataset is not proof nothing happened).

## Gotchas & OpSec
- Human-in-the-loop: needs a RapidAPI key; the free tier is quota-limited.
- Underlying coverage depends on the aggregated event source — sparse for small/rural incidents and non-English regions. Treat gaps as unknowns, not zeros.
- OpSec: passive; you never touch the subject.

## Overlaps ("do both")
- Pairs with geosocial/media tools (e.g. `[[youtube-dl]]` for on-the-ground video, geotagged-post search) — this gives the structured event scaffold, those provide the human-generated content at those coordinates.

## Trust & verifiability
`trust: unverified` — a single-developer aggregation API; use its output as a lead and confirm any specific event against news reporting or primary footage before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoprotests-api |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
