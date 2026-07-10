---
id: switzerland
name: Switzerland (Zefix)
description: Use when you have a company or director `name` in Switzerland and want official commercial-register detail — returns the company, registered `address`, and links to the cantonal register with officers.
url: https://www.zefix.ch/en/search/entity/welcome
category: public-records
path:
- public-records
bestFor: Official Swiss company-register lookups — confirm a company, its address, and route to officer/shareholder detail.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- associate
- name
status: live
pricing: free
costNote: Free official central index (Zefix); the cantonal register extracts it links to may charge for certified documents.
opsec: passive
opsecNote: Read-only search of the official Swiss central business-name index; no person is notified. Certified extracts from cantonal registries may require payment. Use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Zefix is the Central Business Name Index operated by the Swiss Federal Office of Justice — the authoritative gateway to Switzerland's cantonal commercial registers.
missingPersonsRelevance: high
coverage:
- ch
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- infogreffe-fr
- i-cyprus-com
aliases:
- Zefix
- Swiss commercial register
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Switzerland (Zefix)

> Zefix — Switzerland's official central business-name index and the authoritative gateway into the cantonal commercial registers.

## When to use
You have a `name` (company or person) tied to Switzerland and want the corporate picture: confirm a company exists, get its registered `address` and identifiers, and route into the relevant cantonal register for officers, purpose, and history. Switzerland is a common corporate/holding jurisdiction, so Zefix is the primary source for mapping a subject's Swiss business links and co-officers (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zefix.ch/en/search/entity/welcome.
2. Search by company `name`, UID (business identification number), or keyword.
3. Read the central record: legal name, UID, legal form, registered office (`address`), and status.
4. Follow the link to the **cantonal register** extract for officers/signatories, purpose, capital, and history (certified extracts may be paid).
5. Pivot: an officer's `name` feeds people-search; the registered address feeds mapping; cross-check foreign entities via other registries.

## Inputs → Outputs
- **In:** company/director `name`, `employer-org`, UID, or `address`
- **Out:** `employer-org` (company), registered `address`, `name`, and (via cantonal extract) `associate` (officers/signatories)
- **Empty/negative result looks like:** no entity match — the company isn't on the Swiss register or the name/UID is off. A central-index match with limited detail just means the officer detail lives in the cantonal extract.

## Gotchas & OpSec
- Officer/shareholder detail is in the **cantonal register** Zefix links to, not always in the central index itself; certified documents there may cost money.
- Switzerland-only.
- OpSec: **passive** — an official registry read.

## Overlaps ("do both")
- Pairs with `[[infogreffe-fr]]` and `[[i-cyprus-com]]` — a subject's companies often span jurisdictions, so run the registry for each domicile and cross-link recurring officers/addresses.

## Trust & verifiability
`trust: trusted` — the authoritative Swiss federal business-name index; central data is official, with cantonal registers as the primary source for full officer detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | switzerland |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
