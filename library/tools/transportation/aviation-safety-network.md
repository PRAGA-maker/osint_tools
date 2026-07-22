---
id: aviation-safety-network
name: Aviation Safety Network
description: Use when you have an aircraft registration or a date/place and want its accident/incident history — returns the occurrence details, location (`geolocation`) and operator.
url: https://aviation-safety.net/
category: transportation
path:
- transportation
bestFor: Looking up aircraft accidents/incidents by registration, operator, type, date or country.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free to search and read the database (run by the Flight Safety Foundation); no account required.
opsec: passive
opsecNote: Searching a public reference database is passive — nothing is sent to any subject and no login is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Flight Safety Foundation; a long-standing, well-sourced aviation-safety reference that cites official investigation reports.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ASN
- aviation-safety.net
tags:
- bellingcat-toolkit
- transport
- aviation
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# Aviation Safety Network

> The Flight Safety Foundation's searchable database of aviation accidents and incidents — resolve an aircraft registration, operator or date into a documented occurrence with location and outcome.

## When to use
An investigation involves an aircraft: you have a tail number (registration), an operator, an airframe type, or a rough date/place and need the accident/incident record. ASN gives the occurrence date, location (`geolocation`), aircraft and operator (`employer-org`), fatalities/outcome, and links to official investigation reports — useful for corroborating a crash, a missing-flight scenario, or an aircraft's history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://aviation-safety.net/ and use the database/Wikibase search.
2. Search by aircraft registration (`vehicle-plate`), operator, type, country, or year via the browse indexes.
3. Open the occurrence page: date, phase of flight, location/coordinates, aircraft and operator, casualties, narrative, and report references.
4. Cross-reference the registration against the aircraft's earlier records for a fuller history.
5. Pivot: the location (`geolocation`) feeds mapping; the operator (`employer-org`) and registration feed corporate/registry and aircraft-tracking tools.

## Inputs → Outputs
- **In:** an aircraft registration (`vehicle-plate`), operator, type, date, or country
- **Out:** occurrence record — date, `geolocation`, aircraft/operator (`employer-org`), outcome, report links
- **Empty/negative result looks like:** no match means no *catalogued safety occurrence* for that query — most flights have none; absence is not evidence of an event, and minor incidents may be under-recorded.

## Gotchas & OpSec
- It records safety occurrences, not routine flights — for live/normal aircraft movements use a flight-tracker (ADS-B) instead.
- Coverage is strongest for airliners and notable events; light-aircraft/older records vary in completeness.
- OpSec: passive; a public database, no login.

## Overlaps ("do both")
- Pairs with ADS-B flight-tracking and aircraft-registration lookups — ASN gives the historical accident record, trackers give current/positional data, and registries tie a tail number to its owner.

## Trust & verifiability
`trust: trusted` — a Flight Safety Foundation resource that cites official investigation sources; still follow through to the primary report for evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aviation-safety-network |
