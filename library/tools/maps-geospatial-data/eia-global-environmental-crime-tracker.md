---
id: eia-global-environmental-crime-tracker
name: EIA Global Environmental Crime Tracker
description: Use when you have a species, country, or seizure and want verified environmental-crime cases, routes, and enforcement data — returns geolocation, associate.
url: https://eia-international.org/global-environmental-crime-tracker/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Mapping verified international environmental-crime seizures, trafficking routes, and enforcement cases.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- associate
status: live
pricing: free
costNote: Free interactive database and dashboard; no account required.
opsec: passive
opsecNote: Passive — browsing a published crime database; nothing touches any subject and no query is attributable to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Environmental Investigation Agency (an established investigative NGO) and listed in Bellingcat's toolkit; data is described as verified, though it captures only a fraction of actual activity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- EIA Environmental Crime Tracker
- Global Environmental Crime Tracker
tags:
- bellingcat-toolkit
- environment-wildlife
- crime
source: bellingcat-toolkit
lastVerified: '2026-07-29'
relatedTools:
- environmental-investigation-agency
enrichment: full
---

# EIA Global Environmental Crime Tracker

> An interactive, verified database of international environmental crime — wildlife and timber trafficking, HFC smuggling, seizures and prosecutions — mapped by location, species, and route.

## When to use
Your case touches wildlife/environmental crime — a seizure, a species (ivory, pangolin, rhino, tiger, totoaba), a smuggling route, or a region — and you want **structured, verified case records** rather than news fragments. Filter by `geolocation` (country/region) or commodity to find documented seizures, enforcement actions, and the trafficking-network context, including named actors where reported (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://eia-international.org/global-environmental-crime-tracker/ and launch the interactive dashboard/map.
2. Filter by commodity/species, crime type, country/region, or date.
3. Read the case records: what was seized, where, when, and the arrest/prosecution outcome.
4. Consult the downloadable user guide for how EIA classifies and sources entries.
5. Pivot: locations (`geolocation`) tie seizures to ports/routes for ground-level OSINT; named actors/companies feed corporate and people-search; case IDs point back to EIA's underlying reporting.

## Inputs → Outputs
- **In:** a species/commodity, `geolocation` (country/region), or seizure
- **Out:** verified case records — seizure `geolocation`s, routes, enforcement outcomes, and named `associate`s where reported
- **Empty/negative result looks like:** no records for that filter — either genuinely none catalogued, or (per EIA's own caveat) the activity happened but wasn't captured; absence is not proof of no crime.

## Gotchas & OpSec
- Passive; browsing never touches any subject.
- EIA states the dataset "likely represents only a fraction" of real activity — treat it as a floor, not a complete census.
- Records reflect enforcement/seizure reporting; a route with few entries may simply be under-enforced, not low-traffic.

## Overlaps ("do both")
- Pairs with `[[environmental-investigation-agency]]` — the tracker is the structured database, EIA's wider site holds the narrative investigations behind the entries.

## Trust & verifiability
`trust: trusted` — curated by an established investigative NGO and Bellingcat-listed; entries are described as verified, but corroborate specifics against EIA's source reporting and official seizure records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eia-global-environmental-crime-tracker |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
