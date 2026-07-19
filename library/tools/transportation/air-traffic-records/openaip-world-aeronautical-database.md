---
id: openaip-world-aeronautical-database
name: OpenAIP World Aeronautical Database
description: Use when you have an airfield/airspace `geolocation` and want aeronautical data — a free open database; returns runway, frequency, navaid, and airspace structure for a location.
url: https://www.openaip.net/
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Looking up airfields, runways, radio frequencies, navaids, and airspace structure worldwide from free open data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, community-maintained open aeronautical data; a free account/API key is needed for bulk/API access.
opsec: passive
opsecNote: Passive — you query a static open aviation dataset, not a person or aircraft; nothing reaches any subject. Registering for API access ties queries to an account; use a research account for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained open aeronautical database used in flight-planning tools; broadly reliable for airspace/airfield structure, but crowd-sourced — verify safety-critical detail against official AIP.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- OpenAIP
tags:
- aviation
- airspace
- open-data
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# OpenAIP World Aeronautical Database

> A free, open worldwide database of airfields and airspace — runways, frequencies, navaids, and airspace structure for any location.

## When to use
Your case has an aviation angle — an airfield, airstrip, or airspace near a `geolocation` of interest — and you want its aeronautical detail: runway layout/length, radio frequencies, elevation, navaids, and the surrounding airspace structure. Useful for contextualising a flight, a small airstrip, or an aviation-linked subject; it's about places/infrastructure, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.openaip.net/ and pan/search the map to your `geolocation` or airfield name.
2. Select an airfield/airspace to view its data (runways, frequencies, elevation, navaids, airspace class).
3. For bulk/automated use, register a free account and use the API/data exports.
4. Pivot: combine airfield details with flight-tracking (ADS-B) tools and satellite imagery of the site.

## Inputs → Outputs
- **In:** a `geolocation` / airfield name / airspace criteria
- **Out:** runway, frequency, elevation, navaid, and airspace-structure data for that location (`geolocation` context)
- **Empty/negative result looks like:** no entry for a remote/unregistered strip — crowd-sourced coverage has gaps; cross-check official AIP/charts.

## Gotchas & OpSec
- **Infrastructure data, not people** — it identifies airfields/airspace, not aircraft owners or pilots.
- Crowd-sourced: reliable broadly, but not for safety-critical navigation — use official AIP for that.
- Human-in-the-loop: none for map viewing (API needs a free key). OpSec: passive.

## Overlaps ("do both")
- Do both with ADS-B flight-tracking and satellite imagery — OpenAIP describes the airfield/airspace; those show live flights and the physical site.

## Trust & verifiability
`trust: community` — community-maintained open data; good for context, but verify any critical detail against the official AIP for that country.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openaip-world-aeronautical-database |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
