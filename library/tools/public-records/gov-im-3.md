---
id: gov-im-3
name: Isle of Man Births, Deaths & Marriages
description: Use when you have a `name` linked to the Isle of Man and want official vital records (birth/death/marriage) — returns document-id (certificate), name, and dob leads.
url: https://services.gov.im/births-deaths-marriages/
category: public-records
path:
- public-records
bestFor: Ordering official Isle of Man birth, death, and marriage certificates to confirm identity, relationships, or a death.
selectorsIn:
- name
selectorsOut:
- document-id
- name
- dob
status: live
pricing: freemium
costNote: Searching the index is free; ordering actual certificates carries a per-certificate fee paid to the Isle of Man General Registry.
opsec: passive
opsecNote: Searching/ordering vital records does not notify the subject or their family. Ordering a certificate requires payment and contact details logged by the registry; use investigative-context details where permitted.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Isle of Man Government (General Registry) service; authoritative for IoM civil registration records.
missingPersonsRelevance: high
coverage:
- im
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gro-gov-uk
- freebmd
- gov-im
- gov-im-2
- gov-im-4
- gov-im-5
aliases:
- Isle of Man General Registry
- IoM BMD
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- vital-records
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Isle of Man Births, Deaths & Marriages

> The Isle of Man Government's official civil-registration service — the authoritative source for IoM birth, death, and marriage records, a small but distinct jurisdiction from the UK.

## When to use
Your subject was born, married, or died on the Isle of Man, or you're building a family tree that runs through it. You have a `name` and want to confirm a vital event: a birth (identity + DOB + parents), a marriage (spouse + date → `associate`), or a death (date, which resolves a missing-persons question definitively). Because IoM is a separate registration jurisdiction, these records are not in the England & Wales GRO index — you have to come here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://services.gov.im/births-deaths-marriages/.
2. Search the relevant index (birth / death / marriage) by `name` and approximate date.
3. Identify the matching record entry (the free index confirms an event exists).
4. Order the certificate (paid, per-certificate) for the full detail — parents, spouse, dates, places.
5. Pivot: a birth certificate's parents feed `associate` mapping; a death record closes the trace; a marriage links a spouse/maiden name for further searching.

## Inputs → Outputs
- **In:** `name` (+ approximate date/place)
- **Out:** `document-id` (certificate reference), `name`, `dob`, and — on the ordered certificate — parents/spouse (`associate`), places
- **Empty/negative result looks like:** no index match — the event may not have occurred on the Isle of Man, or falls outside the indexed range. Absence here points you back to the England & Wales GRO or another jurisdiction.

## Gotchas & OpSec
- **Fee gate:** the index search is free, but the substantive detail is on the paid certificate.
- IoM is separate from the UK GRO — don't assume a UK search covers it (and vice versa).
- Passive; only the certificate order exposes payment/contact details.

## Overlaps ("do both")
- Pairs with `[[gro-gov-uk]]` (England & Wales civil registration) and `[[freebmd]]` (free BMD index) — check the Isle of Man here specifically, since the mainland indices don't include it.

## Trust & verifiability
`trust: trusted` — the official Isle of Man General Registry. Records are authoritative; the free index confirms existence and the paid certificate carries the full, citable detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-im-3 |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, name, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
