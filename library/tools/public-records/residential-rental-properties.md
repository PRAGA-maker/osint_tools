---
id: residential-rental-properties
name: Check the Register of Fair Rents (GOV.UK)
description: Use when you have a UK residential `address` and want to check the registered "fair rent" for a regulated tenancy — returns confirmation the property exists on the register plus a rent record tied to the `address`.
url: https://www.gov.uk/check-register-rents
category: public-records
path:
- public-records
bestFor: Confirming a UK regulated-tenancy property and its registered maximum rent by address (older private lettings started before 15 Jan 1989).
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free online check via GOV.UK / the Valuation Office Agency; certified copies of a register entry cost £1.
opsec: passive
opsecNote: Passive — you query a government property register by address, not a person, and no subject is notified. The register is about the property/tenancy, not directly about named occupants.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official GOV.UK / Valuation Office Agency service; the register is an authoritative government record, though pre-2004 entries may be offline and require contacting the VOA.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Fair Rents register
- check register of rents
- VOA fair rents
tags:
- propertysites
- Property Related Sites
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Check the Register of Fair Rents (GOV.UK)

> The UK government register of "fair rents" for regulated tenancies — a niche property record that confirms an address is a long-standing regulated let and the maximum rent set for it.

## When to use
You have a UK residential `address` connected to an older private tenancy (a "regulated"/protected tenancy, generally started before 15 January 1989) and want to confirm the property is on the fair-rents register and what maximum rent was set. In a locate or background workflow this corroborates that an address is a genuine long-term rented dwelling and gives a datapoint (registered rent, registration number) to tie to other property records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/check-register-rents.
2. Search by the property `address` or by a known registration number.
3. Read the result: whether the property is registered and the maximum allowable ("fair") rent for the regulated tenancy.
4. If a pre-2004 entry is missing online, use the Valuation Office Agency contact details on the page to request it (certified copies £1).
5. Pivot: a confirmed regulated-tenancy address feeds Land Registry, electoral roll, and council-tax/valuation lookups to attach names and history to the property.

## Inputs → Outputs
- **In:** UK residential `address` (or fair-rent registration number)
- **Out:** confirmation the property is on the register, its registered maximum rent, and registration reference (all keyed to the `address`)
- **Empty/negative result looks like:** "not found" — the property isn't a registered regulated tenancy (the vast majority of modern lets aren't), or the entry predates online records. Absence says nothing about who lives there.

## Gotchas & OpSec
- Very narrow scope: only **regulated/protected tenancies** (mostly pre-1989 lettings) appear. Ordinary assured shorthold tenancies are not here.
- Pre-2004 decisions may be offline; you must contact the VOA to retrieve them.
- The register describes the property/rent, not named occupants — pair with people/property tools to attach identities.
- OpSec: fully passive government lookup.

## Overlaps ("do both")
- Pairs with `[[uk-osint]]`-linked Land Registry, electoral roll, and council-tax tools — fair rents confirms the tenancy/rent, while those attach owners, occupants, and history to the same `address`.

## Trust & verifiability
`trust: trusted` — an official GOV.UK/VOA register. The data is authoritative for what it covers; its limitation is scope and pre-2004 digitization, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | residential-rental-properties |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
