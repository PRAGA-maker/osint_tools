---
id: alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj
name: RACJ Alcohol Permit Register (Québec)
description: Use when you have an `employer-org`/establishment or `name` in Québec and want its alcohol-permit record — returns permit holder, `address`, and establishment details.
url: https://www.racj.gouv.qc.ca/en/registres-publics/alcool.html
category: public-records
path:
- public-records
bestFor: Looking up who holds a Québec alcohol permit and where the licensed establishment is.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free official government public register; no account or payment.
opsec: passive
opsecNote: Querying a government public register is passive and expected; the permit holder is not notified. No sock puppet needed, though normal browser hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Régie des alcools, des courses et des jeux (RACJ), Québec's official liquor/gaming regulator — an authoritative primary source for permit data.
missingPersonsRelevance: low
coverage:
- ca
aliases:
- RACJ
- Régie des alcools des courses et des jeux
- Quebec alcohol permit register
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- federal-corporation-search-canada
- canpages-search-canada
tags:
- corporate
- licensing
- quebec
- government-register
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# RACJ Alcohol Permit Register (Québec)

> Québec's official public register of alcohol permits — turns a bar, restaurant, or store name into its permit holder and licensed address.

## When to use
Your lead touches a Québec licensed establishment — a bar, restaurant, dépanneur, or event venue — or a person you think holds a liquor permit. This official register lets you confirm who holds the permit, the establishment's `address`, permit type/status, and the operating entity (`employer-org`). Useful for tying a person to a business, confirming an address, or establishing that a named venue is real and currently licensed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.racj.gouv.qc.ca/en/registres-publics/alcool.html (English) and enter the public-register search.
2. Search by establishment name (`employer-org`), permit holder `name`, or location.
3. Read the record: permit holder, establishment address, permit category, and status (active/expired/suspended).
4. Pivot: the holder entity → `[[federal-corporation-search-canada]]` for corporate officers/associates; the address → mapping and other local records; a suspended/revoked permit → a dated event to explain.

## Inputs → Outputs
- **In:** `employer-org` (establishment) or permit-holder `name`
- **Out:** permit holder, licensed `address`, permit type/status, operating `employer-org`
- **Empty/negative result looks like:** no matching permit — the establishment isn't licensed in Québec, is spelled differently, or the permit lapsed. Absence isn't proof the business doesn't exist, only that it holds no current Québec alcohol permit.

## Gotchas & OpSec
- Scope is Québec alcohol permits only — a business elsewhere in Canada won't appear; use provincial equivalents.
- Establishment names vary (legal vs trade name); try both and the address.
- OpSec: passive; a government-register lookup is routine and invisible to the subject.

## Overlaps ("do both")
- Pair with `[[federal-corporation-search-canada]]` to move from the licensed establishment to the corporation and its officers, and `[[canpages-search-canada]]` to find contact/location details for the same business.

## Trust & verifiability
`trust: trusted` — it is the Québec regulator's own register, so permit records are authoritative; still confirm identity (name/address match) before linking a person to a permit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
