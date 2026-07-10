---
id: gro-gov-uk
name: GRO (General Register Office)
description: Use when you have a `name` and want to confirm a birth, death or parentage in England & Wales — returns index entries with dates, districts and mother's maiden name, and orderable certificates.
url: https://www.gro.gov.uk/gro/content/certificates/login.asp
category: public-records
path:
- public-records
bestFor: Searching the official England & Wales birth/death index to confirm identity, DOB, death, and parents (via mother's maiden name), then ordering certificates.
selectorsIn:
- name
selectorsOut:
- dob
- name
- associate
- document-id
status: live
pricing: freemium
costNote: Free registration lets you search the online GRO index (births 1837–1922 and from 1934; deaths 1837–1957 and from 1984). Certificates cost a fee (PDF ~£8, paper ~£12.50) to order.
opsec: passive
opsecNote: Searching the civil-registration index is a passive query to a government register; the subject is not notified. Ordering a certificate ties to your GRO account and address — use an appropriately attributed account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official UK government civil-registration authority for England & Wales; index and certificate data are authoritative primary records.
missingPersonsRelevance: high
coverage:
- gb-eng
- gb-wls
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- '192'
aliases:
- General Register Office
- gro.gov.uk
- GRO index
tags:
- genealogybdmANDwills
- genealogy
- birth-death-marriage
- uk
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# GRO (General Register Office)

> The official England & Wales civil-registration authority — search the birth/death index by name to confirm a date of birth, a death, and parentage (mother's maiden name), and order the certificate for full detail.

## When to use
You have a `name` and want authoritative confirmation of a birth or death in England & Wales, or need to establish parentage/relationships. The free online GRO index returns the registration event with the year/quarter, district, and — for births — the mother's maiden name, which is gold for confirming identity and linking family. Order the certificate for full particulars (exact date, address, parents' names/occupations, informant on a death).

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://www.gro.gov.uk/ and open the certificate/index search.
2. Search births (by surname + forename + year range; you can filter by mother's maiden name) or deaths (by name + year, with age/DOB on post-1969 entries).
3. Read the index result: registration district, quarter/year, and — births — mother's maiden name (`associate`).
4. To confirm exact `dob`, addresses and parents, order the certificate (`document-id` = GRO index reference).
5. Pivot: the mother's maiden name and district narrow family searches; confirmed identities feed `[[192]]` and electoral/address tools.

## Inputs → Outputs
- **In:** `name` (with approximate year/place to narrow)
- **Out:** index entries → `dob`/death date, district, mother's maiden name (`associate`), and a GRO `document-id`; certificates add full detail
- **Empty/negative result looks like:** no index match — wrong spelling, out-of-range year, or the event was in Scotland/NI (separate registries) or abroad; absence isn't proof.

## Gotchas & OpSec
- **England & Wales only** — Scotland (ScotlandsPeople) and Northern Ireland (GRONI) are separate; overseas births are elsewhere.
- The index has coverage gaps by year (see the ranges above); a miss may be a coverage gap, not a non-event.
- Human-in-the-loop: free account to search; certificates cost a fee and take time.
- OpSec: passive; certificate orders are logged to your account/address.

## Overlaps ("do both")
- Pairs with `[[192]]` and electoral tools — GRO establishes birth/death/parentage (identity backbone); 192 places living people at addresses. Do both to build a verified family/identity picture.

## Trust & verifiability
`trust: trusted` — authoritative government primary records; the index is reliable within its year coverage, and the certificate is the definitive source when you need exact particulars.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gro-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, name, associate, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
</content>
