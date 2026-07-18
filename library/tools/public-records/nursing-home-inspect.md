---
id: nursing-home-inspect
name: Nursing Home Inspect
description: Use when you have a US nursing-home name or location and want its inspection/deficiency history — returns employer-org facility records and geolocation to vet or locate a care facility.
url: https://projects.propublica.org/nursing-homes/
category: public-records
path:
- public-records
bestFor: Searching US nursing-home inspection reports, deficiencies, and fines by facility name or location.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free ProPublica public-interest database built on CMS inspection data; no account required.
opsec: passive
opsecNote: Reads a public journalism database sourced from government (CMS) records; no facility or person is notified. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by ProPublica from official CMS/Medicare inspection data; a reputable, well-sourced public-interest resource.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- credibly-accused
- nonprofit-explorer
- parler-capitol-videos
- police-protest-videos
- the-nypd-files
aliases:
- ProPublica Nursing Home Inspect
- projects.propublica.org nursing homes
tags:
- public-records
- healthcare
- nursing-homes
- inspections
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Nursing Home Inspect

> ProPublica's searchable database of US nursing-home inspections — deficiencies, fines, and reports for any facility, built on official CMS data.

## When to use
You need to vet or locate a US care facility — because a subject resides in one, works at one, or you're assessing a home's safety record. Search by `employer-org` (facility name) or `geolocation` to pull the facility's inspection history, cited deficiencies, and penalties, along with its `address`. Useful for locate work (confirming a facility exists and where) and for due-diligence on a care provider.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://projects.propublica.org/nursing-homes/.
2. Search by facility name, or browse by state/city to list homes in an area.
3. Open a facility page: read the address, ownership, inspection reports, deficiency narratives, and fines/penalties over time.
4. Pivot: the facility address/ownership feeds corporate-registry and people searches; a subject connected to a home can be corroborated by its staff/ownership records; deficiency narratives sometimes name incidents to follow up.

## Inputs → Outputs
- **In:** `employer-org` (facility name) or `geolocation` (state/city)
- **Out:** `employer-org` (facility + ownership), `address`, plus inspection/deficiency/fine history
- **Empty/negative result looks like:** no facility found — the name/location isn't a CMS-certified nursing home (assisted-living and non-certified facilities may be absent), or spelling differs.

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — public data, no notification.
- Scope: CMS-certified nursing homes in the US only; data reflects reported inspections and can lag. It profiles facilities, not individual residents.

## Overlaps ("do both")
- Pairs with `[[nonprofit-explorer]]` and corporate registries — Nursing Home Inspect covers the facility's compliance record, the others reveal the ownership/nonprofit structure behind it.

## Trust & verifiability
`trust: trusted` — it is ProPublica's presentation of official CMS inspection data; verify specific findings against the underlying CMS/Medicare Care Compare record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nursing-home-inspect |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, geolocation → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
