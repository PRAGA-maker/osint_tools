---
id: accaglobal-com
name: ACCA Find-an-Accountant Directory
description: Use when you have a `name`, firm or town and want to confirm someone is a chartered certified accountant (ACCA member) — returns membership confirmation, firm (`employer-org`) and town/`address`.
url: https://www.accaglobal.com/uk/en/member/find-an-accountant/directory-of-member.html
category: public-records
path:
- public-records
bestFor: Verifying ACCA (chartered certified accountant) membership and finding a member's firm/location by name, firm, or town.
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
costNote: Free public directory; no account required.
opsec: passive
opsecNote: Public professional-directory lookup; the individual is not notified. It confirms professional status and links to a firm/town — treat as identity corroboration, not a home address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by ACCA, the global professional body for chartered certified accountants — authoritative for member status, and it links to the UK Register of Statutory Auditors for audit rights.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ACCA member directory
- accaglobal.com
- find an accountant
tags:
- professionlicensing
- profession-licensing
- public-records
- accountants
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ACCA Find-an-Accountant Directory

> ACCA's public member directory — confirm someone really is a chartered certified accountant and find the firm and town they practise in.

## When to use
You have a `name` (or a firm/town) and need to verify a claimed accounting qualification or place a subject professionally. ACCA membership confirms occupation, and the directory ties the person to a practising firm (`employer-org`) and location (`address`/town) — useful for corroborating identity, spotting fabricated credentials, or getting a professional-contact lead in a missing-person or fraud case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.accaglobal.com/uk/en/member/find-an-accountant/directory-of-member.html.
2. Search by first name + last name, and/or firm, and/or **city or town** to narrow.
3. Read results: member/firm entries confirming ACCA status, firm name, and location. Note new entries can take ~24h to appear.
4. For audit rights specifically, follow through to the UK Register of Statutory Auditors / Irish public register the page links to.
5. Pivot: firm → company registry (`[[company-information-service-gov-uk]]`) and firm address/contacts; town → localized people-search; confirmed name → other professional registers.

## Inputs → Outputs
- **In:** `name`, firm (`employer-org`), or `address`/town
- **Out:** `name` (confirmed member), `employer-org` (firm), `address` (practising town/firm location), audit-status pointer
- **Empty/negative result looks like:** no match — the person may not be ACCA (could be ICAEW/CIMA/other bodies, or unqualified), may have lapsed, or the name differs. A miss is not proof they aren't an accountant — check the other UK bodies.

## Gotchas & OpSec
- ACCA is **one** accountancy body; ICAEW, CIMA, AAT, and others have separate registers — a "not found" only rules out ACCA.
- The directory lists practising members/firms; not every ACCA-qualified individual appears (e.g. non-practising members).
- OpSec: **passive** — public professional record.

## Overlaps ("do both")
- Pairs with `[[myewc-wales]]`-style professional registers and ICAEW/CIMA directories — pick the right body; run several if the qualification is unknown.
- Feed the firm into a company registry to get addresses and co-principals.

## Trust & verifiability
`trust: trusted` — first-party professional body; membership status is authoritative. It confirms professional standing and firm, not current residence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | accaglobal-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
