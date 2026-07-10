---
id: nidirect-gov-uk-2
name: nidirect.gov.uk (Land & Property Registers)
description: Use when you have a Northern Ireland `address` or owner `name` and want land/property records — the official gateway routes to registers returning ownership and `address` detail.
url: https://www.nidirect.gov.uk/information-and-services/buying-your-home/land-and-property-registers
category: public-records
path:
- public-records
bestFor: Official gateway to Northern Ireland's land and property registers (ownership, boundaries, property records).
selectorsIn:
- name
- address
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: The nidirect guidance is free; the underlying Land Registry / property searches (via Land & Property Services / LandWeb) typically charge a per-search fee. Some checks require an account.
opsec: passive
opsecNote: Searching a property register is passive and does not notify the owner. Paid searches require account/payment details, tying the lookup to you — use a role-based identity if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Northern Ireland government (nidirect) gateway to the statutory Land Registry; records are authoritative for NI property.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- land-registry-property-search
- ros-gov-uk
aliases:
- nidirect land registry
- Northern Ireland Land Registry
tags:
- propertysites
- Property Related Sites
- northern-ireland
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# nidirect.gov.uk (Land & Property Registers)

> The official Northern Ireland government gateway to land and property registers — the route to who owns a property in NI and the property records tied to an address.

## When to use
You have a Northern Ireland `address` (or a `name` you want to link to property) and need ownership/boundary/property information. NI has its own Land Registry (under Land & Property Services), separate from England & Wales and Scotland, and nidirect is the official signpost into it. Property ownership ties a subject to a location and can reveal co-owners or a controlling company (`employer-org`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the nidirect land-and-property-registers page and follow the links to Land & Property Services / LandWeb.
2. Choose the search type (registered title, property, map/boundary) and enter the `address` (or title reference).
3. Pay any per-search fee and read the record: registered owner(s), title/boundary detail, and property description.
4. Note owner names, co-owners, or a company owner as leads.
5. Pivot: owner `name`s feed people-search; a company owner feeds company-registry lookups; the address feeds electoral/utility corroboration. For GB use `[[land-registry-property-search]]` (England & Wales) or `[[ros-gov-uk]]` (Scotland).

## Inputs → Outputs
- **In:** NI `address` (or title reference), or an owner `name`
- **Out:** registered owner (`name`), property `address`/boundary detail, company owner (`employer-org`)
- **Empty/negative result looks like:** no registered title for the address (not all land is registered) or a search that needs more precise details — refine the address/title reference.

## Gotchas & OpSec
- Human-in-the-loop: the actual register searches are usually **paid** and may need an account — the nidirect page itself is just the free gateway.
- Northern Ireland only — use the correct jurisdiction's registry for GB property.
- Not all land is registered; gaps reflect registration status, not necessarily hidden ownership.
- OpSec: passive toward the owner; paid searches tie the lookup to your account/payment.

## Overlaps ("do both")
- Sits beside `[[land-registry-property-search]]` (England & Wales) and `[[ros-gov-uk]]` (Scotland) — pick the jurisdiction where the property is; the technique (register search → owner) is the same.

## Trust & verifiability
`trust: trusted` — an official government gateway to the statutory NI Land Registry, so ownership records are authoritative. Cost and registration-scope are the only limits, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nidirect-gov-uk-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
