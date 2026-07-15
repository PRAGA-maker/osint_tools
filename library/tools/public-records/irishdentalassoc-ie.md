---
id: irishdentalassoc-ie
name: Irish Dental Association – Find A Dentist
description: Use when you have a dentist's `name` or a location in Ireland and want to confirm they are a practising IDA member and find their practice — returns practice address and employer-org.
url: https://portal.irishdentalassoc.ie/Find-A-Dentist
category: public-records
path:
- public-records
bestFor: Confirming a dentist's professional affiliation in Ireland and locating their practice via the Irish Dental Association member directory.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free public directory search; no account required to look up a dentist.
opsec: passive
opsecNote: A standard directory lookup — searching a professional register does not notify the subject. Fully passive; you're querying a membership body's public "find a member" page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Irish Dental Association, the professional body for dentists in Ireland; listings are member-supplied but maintained by the association, making it authoritative for IDA membership.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dentalcouncil-ie
aliases:
- IDA Find A Dentist
- Irish Dental Association member finder
tags:
- professionlicensing
- Profession & Licensing Sites
- professional-register
- ireland
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Irish Dental Association – Find A Dentist

> The Irish Dental Association's public member directory: confirm a dentist's IDA affiliation and find their practice location.

## When to use
You have a subject who is (or claims to be) a dentist in Ireland, and you want to confirm the professional affiliation and locate their practice — for verification, or to establish a current work `address` and employer when a home address is unknown. Practising professionals are often easier to place through their workplace than their residence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portal.irishdentalassoc.ie/Find-A-Dentist.
2. Search by the dentist's `name` and/or a location/county in Ireland.
3. Read the listing: dentist `name`, practice/clinic (`employer-org`), and practice `address`/contact details.
4. Cross-check the name and locality against what you already have to confirm it's the right person.
5. Pivot: the practice `address` and clinic name feed company/registry lookups and mapping; confirm the licence separately via the statutory regulator.

## Inputs → Outputs
- **In:** dentist `name`, a location/county, or a practice (`employer-org`).
- **Out:** confirmed `name`, practice `employer-org`, and practice `address`/contact.
- **Empty/negative result looks like:** no match — the person may be a dentist who isn't an IDA member (membership is voluntary), practises under a different name, or isn't a dentist. A blank result is not proof they don't practise; check the statutory Dental Council register too.

## Gotchas & OpSec
- IDA membership is a professional association, not the statutory licence — absence here doesn't mean the person can't legally practise. For registration status, use the Dental Council of Ireland register.
- Listings are member-maintained, so contact details can lag reality; treat the practice address as a strong lead, not a guaranteed current location.
- Coverage is Ireland only.

## Overlaps ("do both")
- Pairs with `[[dentalcouncil-ie]]` — the Dental Council is the statutory register (proof of licence to practise), while the IDA directory is the membership/find-a-practice view; check both to separate "is a member" from "is licensed."

## Trust & verifiability
`trust: trusted` — maintained by the Irish Dental Association. It authoritatively reflects IDA membership, though it is not the statutory licence register; verify licensure with the Dental Council when that distinction matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | irishdentalassoc-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
