---
id: world-aviation-accident-database-2008-2021
name: NTSB CAROL Aviation Accident Database
description: Use when you have an aircraft, date, place or person tied to an aviation accident — searches the NTSB CAROL database and returns official reports with names, `geolocation` and causes.
url: https://data.ntsb.gov/carol-main-public/basic-search
category: transportation
path:
- transportation
bestFor: Official US/NTSB aviation (and other transport) accident reports searchable by date, location, aircraft, operator or person.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- geolocation
- employer-org
status: live
pricing: free
costNote: Free official US government database (NTSB CAROL); no account or payment required.
opsec: passive
opsecNote: Read-only queries against a public government records portal — you search records, not a live subject, and nothing about your query target is transmitted to them. Only your own access is logged by NTSB.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The National Transportation Safety Board's official case-analysis records portal (CAROL) — authoritative primary-source accident data for US-related aviation, rail, marine, highway and pipeline events.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- world-aviation-accident-database-1962-2007
aliases:
- NTSB CAROL
- NTSB accident database
tags:
- Maps, Geolocation and Transport
- Aviation
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# NTSB CAROL Aviation Accident Database

> The NTSB's official accident-records portal (CAROL) — search authoritative US aviation (and rail/marine/highway/pipeline) accident investigations by date, place, aircraft, operator, or the people involved.

## When to use
An investigation touches an aviation accident — you have an aircraft tail number, an operator, a date/`geolocation`, or a `name` of someone reportedly involved (pilot, crew, owner, victim). CAROL returns the official investigation records: what happened, where (with coordinates), the aircraft and operator, and often named individuals and probable cause. Good for corroborating a claimed incident or tracing a person/aircraft through a documented event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.ntsb.gov/carol-main-public/basic-search.
2. Search by keyword, date range, location, make/model, registration number, or use advanced filters for mode/severity.
3. Open a matching case for the full docket: narrative, location/coordinates, aircraft and operator, findings, and involved parties.
4. Export/note records; a public API is also available for bulk queries.
5. Pivot: an operator (`employer-org`) feeds company OSINT; coordinates feed mapping; named individuals feed people-search.

## Inputs → Outputs
- **In:** `name`, `geolocation`, or aircraft/operator/date criteria
- **Out:** official accident records — involved `name`s, `geolocation` of the event, `employer-org` (operator), aircraft and probable cause
- **Empty/negative result looks like:** no matching case — the event may be outside NTSB's jurisdiction/scope (non-US, or below reporting thresholds) or predate the modern dataset; absence isn't proof no accident occurred.

## Gotchas & OpSec
- **US-centric jurisdiction:** CAROL covers NTSB-investigated events (US and US-registered/operated abroad); foreign domestic accidents live in that country's authority instead.
- Coverage and completeness vary by era; for older aviation events see the companion 1962–2007 dataset.
- Records are factual investigation findings — accurate but focused on safety, not a person dossier; corroborate identity details elsewhere.

## Overlaps ("do both")
- Pairs with [[world-aviation-accident-database-1962-2007]] for historical coverage and with aircraft-registry/tracking tools — CAROL gives the investigation, registries give ownership, trackers give movement.

## Trust & verifiability
`trust: trusted` — an authoritative US government primary source; each case is a documented official investigation, directly citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-aviation-accident-database-2008-2021 |
| category | transportation |
| selectorsIn → selectorsOut | name, geolocation → name, geolocation, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
