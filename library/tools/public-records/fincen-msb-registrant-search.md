---
id: fincen-msb-registrant-search
name: FinCEN MSB Registrant Search
description: Use when you have a business `name` (or a person tied to one) and want to check whether it registered with FinCEN as a money services business — returns `employer-org` details, locations, and services.
url: https://www.fincen.gov/msb-registrant-search
category: public-records
path:
- public-records
bestFor: Confirming and profiling a US money services business (money transmitter, check casher, currency exchanger) via its FinCEN registration.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free US-government (FinCEN/BSA E-Filing) public search; no account required.
opsec: passive
opsecNote: Searches a public federal registry — no contact with the business or any person. Queries hit a government site; nothing reveals your subject to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official FinCEN (US Treasury) registrant list; authoritative for the fact of MSB registration, though the registry reflects self-reported filings.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FinCEN MSB search
- Money Services Business registrant search
tags:
- corporate
- financial-regulation
- public-records
source: metaosint
lastVerified: '2026-07-23'
---

# FinCEN MSB Registrant Search

> The US Treasury's public lookup of businesses registered with FinCEN as Money Services Businesses — money transmitters, check cashers, currency exchangers, and the like.

## When to use
You have a business `name` (or a person connected to one — a remittance shop, crypto exchanger, check-cashing operation) and want to confirm whether it registered as an MSB with FinCEN, and pull what the registration discloses: legal and DBA names, addresses/branch locations, the MSB activities it performs, and states of operation. Useful for verifying a financial business, mapping a subject's commercial footprint, or corroborating an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fincen.gov/msb-registrant-search.
2. Search by business/legal name (and optionally filter by state or MSB activity).
3. Read the record: registrant legal name, DBA(s), principal `address`, branch locations, and the categories of money-services activity registered.
4. Pivot: an address feeds reverse-address/property lookups; DBAs feed corporate-registry and web searches; the activity type frames the business's role in a financial investigation.

## Inputs → Outputs
- **In:** business `name` / `employer-org` (optionally state, activity)
- **Out:** `employer-org` registration details, `address` and branch locations, MSB activity types
- **Empty/negative result looks like:** no match — the business never registered federally as an MSB (or operates under a different legal name); absence is not proof it isn't operating, only that it isn't in this registry.

## Gotchas & OpSec
- The list reflects self-reported registrations; registration ≠ licensing or good standing, and lapsed/updated filings may lag.
- Search by the legal name and known DBAs separately — a storefront's public name often differs from its registered entity.
- OpSec: **passive** — a federal public-records query, invisible to the subject.

## Overlaps ("do both")
- Pairs with state money-transmitter licensing lookups and corporate registries — FinCEN confirms federal MSB registration; state regulators and registries add licensing, officers, and status.

## Trust & verifiability
`trust: trusted` — an authoritative government registry for the fact of registration; treat the self-reported details as a starting point to corroborate against state records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fincen-msb-registrant-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
