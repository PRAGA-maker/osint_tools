---
id: casa-aircraft-search-australia
name: CASA Aircraft Register Search (Australia)
description: Use when you have an Australian aircraft mark (VH-xxx) and want the aircraft and its registered holder — returns aircraft details, employer-org/name of the registration holder and address.
url: https://www.casa.gov.au/search-centre/aircraft-register
category: transportation
path:
- transportation
bestFor: Looking up an Australian civil aircraft by its VH registration mark to reach the registered operator/holder and aircraft details.
selectorsIn:
- vehicle-plate
- name
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public search of the official Australian civil aircraft register; downloadable data files are also free.
opsec: passive
opsecNote: Querying a public government register about a registration mark, not a person directly — passive, no subject notification, no account required for the basic search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CASA (Australia's Civil Aviation Safety Authority); the authoritative source for Australian aircraft registration.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CASA aircraft register
- Australian civil aircraft register
- VH register
tags:
- toddington
- curated-directory
- specialty-search
- aviation
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# CASA Aircraft Register Search (Australia)

> Australia's official civil aircraft register — search a VH-registration mark to reach the aircraft's make/model and its registered holder/operator.

## When to use
You have an Australian aircraft mark (the `VH-xxx` painted on the tail, or spotted in a photo/record) and want to identify the aircraft and who holds its registration. A hit returns the manufacturer, model, and the registered operator/holder — which can be an individual `name` or a company (`employer-org`), sometimes with an address on file. Useful when a subject owns or is linked to an aircraft, or to identify a plane in imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.casa.gov.au/search-centre/aircraft-register.
2. Enter the VH registration mark (or search by holder/type where supported).
3. Read the record: manufacturer, model, serial, registration status, and registered holder/operator.
4. For bulk work, download CASA's free register data files and search offline.
5. Pivot: a company holder → Australian business registry (ASIC/ABN); an individual holder → people-search; an aircraft type → flight-tracking (ADS-B) for movement history.

## Inputs → Outputs
- **In:** Australian aircraft mark (`vehicle-plate` = VH-xxx), or a holder `name`
- **Out:** aircraft make/model/status, registered holder `name` or `employer-org`, sometimes an `address`
- **Empty/negative result looks like:** no record for the mark — it's deregistered, foreign, or mistyped (Australian marks start `VH-`); try CASA's downloadable data or third-party mirrors for historical marks.

## Gotchas & OpSec
- Only Australian (VH-) aircraft — foreign-registered aircraft aren't here (use the relevant national register).
- Holders can be trusts/companies that mask the beneficial individual; follow into the business registry.
- Register reflects current registration; deregistered/historical marks may need archived data files.
- OpSec: passive, no account, no subject notification.

## Overlaps ("do both")
- Pairs with ADS-B flight-tracking (movement history for a tail number) and the Australian business registry (to resolve a company holder to people).

## Trust & verifiability
`trust: trusted` — the authoritative CASA government register; registration facts are official, though beneficial ownership behind a company/trust holder needs a further step.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | casa-aircraft-search-australia |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, name → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
