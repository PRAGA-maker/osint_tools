---
id: myaccident-traffic-accident-map
name: MyAccident — Traffic Accident Map
description: Use when you have a `vin`, `address`/`geolocation`, or crash details and want the police accident report — returns driver, vehicle, injury and location data from US crash records.
url: https://myaccident.org/
category: transportation
path:
- transportation
- vehicle-records
bestFor: Finding US police accident reports by VIN, location or case ID — revealing drivers, vehicles, injuries and fault.
selectorsIn:
- vin
- address
- geolocation
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free — the accident-report search and map are explicitly free of charge; an optional free account enables report alerts.
opsec: passive
opsecNote: Read-only search of public US crash-report data; no contact with anyone involved and no notification to them. Reports contain third parties' PII (drivers, injuries) — handle it as sensitive personal data and only use it for a legitimate investigative purpose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial service that aggregates official police crash reports; the underlying reports are authoritative, but availability lags (reports can take ~10 days to publish) and coverage varies by department.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- MyAccident.org
tags:
- vehicle
- accident-records
- crash-reports
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# MyAccident — Traffic Accident Map

> A free, searchable map of US police accident reports — pull the crash record for a VIN, a location, or a case ID and see who was driving, what they drove, and what happened.

## When to use
Your subject may have been in a US traffic collision and you want the paper trail. MyAccident lets you search police crash reports by VIN, by case ID + city + date, or by a map showing accidents within ~10 miles filtered by vehicle make/year/date. A matching report yields driver details (age, license, insurance status), the vehicle (year/make/model/VIN, damage), injuries, citations, weather, an accident diagram, and the officer's fault opinion. That's a rich people/vehicle record: it can place a person at a time and location, tie them to a vehicle, and surface other parties (`associate` leads) involved.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://myaccident.org/ and choose a search method: VIN, case ID + city + date, or the map view.
2. For the map, filter by vehicle make/year and accident date within an area; for a specific crash, use the VIN or case ID.
3. Open the report: drivers, vehicles, injuries, citations, location, diagram, fault opinion.
4. If the report isn't public yet (they can take ~10 days), set a free alert.
5. Pivot: a driver `name` + `address` feeds people-search; other involved parties are `associate` leads; the VIN feeds `[[nhtsa-vehicle-api]]`.

## Inputs → Outputs
- **In:** `vin`, `address`/`geolocation`, or case ID + city + date
- **Out:** driver `name`/`address`, vehicle details, injuries, citations, other-party `associate`s, crash `geolocation`/date
- **Empty/negative result looks like:** no matching report — the crash isn't in coverage, hasn't been published yet (~10-day lag), or occurred in a non-participating jurisdiction.

## Gotchas & OpSec
- Human-in-the-loop: none, but publication lags real crashes by up to ~10 days.
- Reports contain sensitive third-party PII — treat accordingly and use only for legitimate purposes.
- Coverage and detail depend on the reporting police department; absence isn't proof of no crash.

## Overlaps ("do both")
- Pairs with `[[nhtsa-vehicle-api]]` (decode the VIN from a report) and state DMV/registration lookups (resolve the vehicle to a current keeper).

## Trust & verifiability
`trust: community` — a commercial aggregator of authoritative police crash reports; the reports are official, but coverage/timeliness vary, so confirm specifics against the originating department where it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myaccident-traffic-accident-map |
| category | transportation |
| selectorsIn → selectorsOut | vin, address, geolocation → name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
