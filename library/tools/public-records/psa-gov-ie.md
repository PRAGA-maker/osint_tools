---
id: psa-gov-ie
name: psa-gov.ie (PSA licence register)
description: Use when you have a contractor/employee `name` or `employer-org` in Irish private security and want to verify their PSA licence — returns licence status, holder name and firm.
url: https://www.psa-gov.ie/psa-registered-contractors/
category: public-records
path:
- public-records
bestFor: Verifying whether an Irish private-security contractor or employee holds a valid PSA licence.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free official register operated by Ireland's Private Security Authority (PSA); no account or payment.
opsec: passive
opsecNote: An official statutory register lookup — you query the PSA, not the subject, and nobody is notified. The licence register is public. Routine sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Private Security Authority, Ireland's statutory regulator for the private security industry — an authoritative first-party licence register.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- Private Security Authority Ireland
- PSA licence register
- psa-gov.ie
tags:
- professionlicensing
- Profession & Licensing Sites
- security-licensing
- ireland
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# psa-gov.ie (PSA licence register)

> Ireland's statutory register of licensed private-security contractors and employees — confirm a security firm or guard is PSA-licensed and in what capacity.

## When to use
You are checking someone connected to the Irish private-security industry — a contractor firm (CCTV/alarms/access-control installer, security guarding) or an individual employee — and want to confirm they hold a valid PSA licence, or to tie a `name` to a licensed `employer-org`. Professional/occupational licensing is a solid identity and employment signal, and the PSA maintains separate searchable registers for contractors and employees.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.psa-gov.ie/ and go to the PSA Registered Contractors (or PSA Registered Employees) search.
2. Search the register by holder `name` or firm/`employer-org`, using the available criteria.
3. Read the record: licence holder name, licensed firm, licence category/sector, and licence status (valid/expired/revoked).
4. Cross-reference contractor ↔ employee registers to link an individual to the company they work for.
5. Pivot: a licensed firm feeds Irish company records (CRO) for directors/`address`; a confirmed employee links a person to an employer and locality.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** licence status, holder `name`, licensed firm (`employer-org`), sector/category, and firm `address` where listed
- **Empty/negative result looks like:** no matching licence — the person/firm isn't PSA-licensed (unlicensed, lapsed, or not in the private-security sector). Absence only disproves the licence, not the person's existence.

## Gotchas & OpSec
- **Ireland only**, and **private-security sector only** — it won't cover other trades or Northern Ireland (separate schemes).
- Two registers (contractors vs employees) — check both; an individual may appear only in one.
- OpSec: **passive**, authoritative first-party register; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with the Irish Companies Registration Office (CRO) for a licensed firm's directors/address, and with other occupational registers (e.g. `[[pharmacyregulation-org]]`) — the PSA verifies the security licence; company/other registers add ownership and contact detail.

## Trust & verifiability
`trust: trusted` — the official PSA statutory register; licence status is authoritative for Ireland's private-security industry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | psa-gov-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
