---
id: planningalerts-org-au
name: PlanningAlerts (Australia)
description: Use when you have an Australian `address`/area and want local development/planning applications — returns addresses, applicant details, and application descriptions.
url: https://www.planningalerts.org.au/
category: public-records
path:
- public-records
bestFor: Finding planning/development applications tied to an Australian address or neighbourhood.
selectorsIn:
- address
- name
selectorsOut:
- address
- name
- employer-org
status: live
pricing: free
costNote: Free public service run by the OpenAustralia Foundation (a non-profit); email alerts and an API are also free.
opsec: passive
opsecNote: Aggregates council-published planning notices; searching is anonymous and does not notify anyone. Applicant names in DAs are public record as councils publish them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the OpenAustralia Foundation; it republishes official local-council development-application data, so records are authoritative (subject to what each council publishes).
missingPersonsRelevance: high
coverage:
- au
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-maps
- pappers-fr
aliases:
- planningalerts.org.au
tags:
- propertysites
- Property Related Sites
- australia
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# PlanningAlerts (Australia)

> A free OpenAustralia service that surfaces local-council development/planning applications by address or area — a way to tie a person or property to building works, ownership signals, and applicant details.

## When to use
You have an Australian `address` (or a subject `name`) and want to know about planning/development activity there: who lodged a development application (DA), what for, and when. Applicant/owner names and architect/builder details on DAs can link a person to a property and to the professionals they hired — useful corroboration of residence or ownership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.planningalerts.org.au/ and search by address, suburb, or postcode (or set an email alert for an area).
2. Read the matching applications: property address, application description, date, council, and any published applicant/contact details.
3. For monitoring, subscribe to alerts for the address/area; for bulk use, query the free API.
4. Pivot: an applicant name feeds people/company search; the property address feeds mapping and land-title lookups; a builder/architect is an associate lead.

## Inputs → Outputs
- **In:** `address` / suburb / postcode (or `name` within results)
- **Out:** `address`, `name` (applicant/owner where published), `employer-org` (builder/architect firms)
- **Empty/negative result looks like:** no applications — the property may have no recent DAs, or that council may not publish to the aggregator. Absence isn't proof of no activity; check the council directly.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; official public notices, no alerts.
- Coverage varies: not every council feeds PlanningAlerts, and published applicant detail differs by council.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` — visualize the property and surroundings behind an application.
- Pairs with a land-titles/company search — turn an applicant name into ownership and corporate links.

## Trust & verifiability
`trust: trusted` — a non-profit republishing official council DA data; authoritative for what councils publish, with the only gap being uneven council participation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | planningalerts-org-au |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
