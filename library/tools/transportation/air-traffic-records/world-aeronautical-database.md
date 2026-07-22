---
id: world-aeronautical-database
name: World Aeronautical Database
description: Use when you have an airport code, airline, or aircraft type and want reference details — returns airport/airline/aircraft data (a context reference, not target PII).
url: https://worldaerodata.com/
category: transportation
path:
- transportation
- air-traffic-records
bestFor: Quick reference lookups for airport identifiers, airline profiles, and aircraft types when contextualizing a flight or route.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free reference site; no account. Reliability is the issue, not cost.
opsec: passive
opsecNote: Static aviation reference retrieval — no query touches an investigation target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running hobby aviation reference of uncertain maintenance; it has a history of outages and returned server errors on last check — verify anything critical against an authoritative source.
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
- worldaerodata.com
- World Aero Data
tags:
- aviation
- reference
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# World Aeronautical Database

> A free hobby aviation reference for airports, airlines, and aircraft — handy for context lookups, but flaky, so keep an authoritative fallback ready.

## When to use
You are contextualizing a flight, route, or aircraft mention and need to resolve an airport code (IATA/ICAO), identify an airline, or look up an aircraft type/manufacturer. This is background/reference data to make sense of an aviation lead — it does not return information about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://worldaerodata.com/ (if it returns a server error, it is intermittently down — retry later or use a fallback below).
2. Browse/search by airport identifier, airline, or aircraft category.
3. Read the reference details (location, ICAO/IATA codes, airline profile, aircraft specs).
4. Pivot: a resolved airport/route feeds geospatial reasoning; an aircraft/airline feeds flight-tracking sources for the actual movement data.

## Inputs → Outputs
- **In:** airport code / airline name / aircraft type (reference query, no target selector)
- **Out:** airport, airline, and aircraft reference details — no individual `selectorsOut`
- **Empty/negative result looks like:** a 5xx/blank page (site is down again) or an unrecognized code — for the former, fall back rather than concluding the record does not exist.

## Gotchas & OpSec
- **Reliability:** the site has a documented history of outages and returned a server error on the last check — treat it as degraded and keep alternatives ready (OpenAIP and Airport-Data cover similar ground and are more actively maintained).
- Reference data can be dated; verify anything decision-critical against an official aeronautical source (national AIP/FAA).
- Fully passive; no login.

## Overlaps ("do both")
- Complements live flight-tracking tools — this resolves the static "what/where" of airports and aircraft; trackers provide the actual movements. Given its flakiness, cross-check with a maintained aeronautical database.

## Trust & verifiability
`trust: unverified` — an unmaintained-looking hobby reference of uncertain provenance; useful for a quick lookup, but corroborate against an authoritative aviation source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-aeronautical-database |
| category | transportation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
