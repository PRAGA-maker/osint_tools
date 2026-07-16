---
id: ny-rent-regulated-building-search
name: NY Rent Regulated Building Search
description: Use when you have a New York `address` and want to know if the building is rent-regulated — returns the building's rent-stabilization status and registration context from NY HCR.
url: https://apps.hcr.ny.gov/BuildingSearch/
category: public-records
path:
- public-records
bestFor: Checking whether a specific NY address is a rent-regulated/stabilized building.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free official New York State (HCR) tool; no account.
opsec: passive
opsecNote: Read-only search of a public NY State building database by address; no person is queried or notified. Building-level, not tenant-level, so it exposes no individual's data directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by New York State Homes and Community Renewal (HCR) — the authoritative source for NY rent-regulation status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- royalmail-com
- new-york-state
aliases:
- NY HCR Building Search
- rent stabilized building lookup
tags:
- property
- new-york
- housing
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# NY Rent Regulated Building Search

> New York State's official lookup for whether a building is rent-regulated — address in, stabilization status out.

## When to use
You have a New York `address` associated with a subject and want housing context: is it a rent-stabilized/regulated building, and what is its registration status. This is building-level context rather than a people finder — useful for characterising where a subject lives (tenure type, likely long-term tenancy in a stabilized unit), corroborating an address, or informing outreach to a building. It does **not** return tenant names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://apps.hcr.ny.gov/BuildingSearch/.
2. Enter the NY `address` (street/borough/ZIP).
3. Read the result: whether the building is rent-regulated and its registration status/history at the building level.
4. Pivot: combine with property-ownership records (e.g. NYC ACRIS) and address-normalisation tools to build the full picture of the address.

## Inputs → Outputs
- **In:** New York `address`
- **Out:** building rent-regulation/stabilization status and registration context (`address`-level)
- **Empty/negative result looks like:** address not found or "not regulated" — meaning the building isn't in HCR's regulated set (market-rate, or outside NY's regulation scope), or the address is mistyped.

## Gotchas & OpSec
- **Building-level only** — no tenant names or individual data; don't expect person-finding output.
- New York State only.
- OpSec: **passive** — a public building-database read.

## Overlaps ("do both")
- Pairs with address-normalisation tools like `[[royalmail-com]]` (for the UK) or NY property-ownership records — this tells you the tenure/regulation type of the building; ownership records tell you who controls it.

## Trust & verifiability
`trust: trusted` — first-party NY HCR data; authoritative for rent-regulation status, but scoped to buildings, not people.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ny-rent-regulated-building-search |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
