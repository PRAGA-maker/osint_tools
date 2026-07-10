---
id: nzbn-govt-nz
name: nzbn.govt.nz
description: Use when you have a New Zealand business `name` or `employer-org` and want its official registry details — returns `employer-org`, `address`, and linked `associate` (directors/contacts).
url: https://www.nzbn.govt.nz/
category: public-records
path:
- public-records
bestFor: Official New Zealand Business Number register — verified trading names, addresses and business details.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free official government register operated by MBIE; searching NZBN records costs nothing and needs no account.
opsec: passive
opsecNote: Passive — it is a public government register; the business is not notified of a lookup. No login is required to search, so there is minimal trail on your side beyond normal server logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official register run by the New Zealand Ministry of Business, Innovation and Employment (MBIE); the data is authoritative for NZBN/entity details, though optional business-provided fields vary.
missingPersonsRelevance: high
coverage:
- nz
auth: none
api: true
localInstall: false
registration: false
aliases:
- New Zealand Business Number
- NZBN register
tags:
- companysites
- Company Related Sites
- new-zealand
- government
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# nzbn.govt.nz

> The official New Zealand Business Number register — a free, authoritative lookup for any NZ entity's trading name, address and core details.

## When to use
You have a New Zealand business `name`, `employer-org`, or `address` tied to your subject and want to confirm the entity and pull its registered details: legal/trading name, physical/postal `address`, entity type, and — for companies — links to the Companies Office where directors and shareholders (`associate` leads) live. Strong for verifying an NZ business trail in a fraud or locate investigation, and it's free and official.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nzbn.govt.nz/ and use the register search.
2. Enter the business `name`, `employer-org`, or NZBN; open the matching record.
3. Read the primary business data (NZBN, trading name, addresses, entity type, contact info where the business chose to publish it).
4. For companies, follow the link to the NZ Companies Office for directors/shareholders (`associate`).
5. Pivot: directors' names feed people-search; addresses feed mapping; non-NZ links feed `[[info-clipper-com]]`. (An open data API is also available for bulk/programmatic lookups.)

## Inputs → Outputs
- **In:** NZ business `name`, `employer-org`, `address`, or NZBN
- **Out:** `employer-org` details, registered `address`, entity type, and (via Companies Office link) `associate` directors/shareholders
- **Empty/negative result looks like:** no matching NZBN record — the entity isn't NZ-registered or uses a different legal name; some optional contact fields are simply blank because the business didn't publish them.

## Gotchas & OpSec
- Human-in-the-loop: none — open public search.
- OpSec: **passive** — official register, no login, subject not notified.
- The NZBN record holds core entity data; director/shareholder detail lives on the linked Companies Office register, so plan a two-step lookup. NZ-only.

## Overlaps ("do both")
- Pairs with `[[info-clipper-com]]` (global corporate) and the NZ Companies Office — NZBN confirms the entity and address; those add the people and cross-border links.

## Trust & verifiability
`trust: trusted` — a first-party New Zealand government register. Authoritative for entity/NZBN data; treat optional self-published fields with normal caution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nzbn-govt-nz |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
