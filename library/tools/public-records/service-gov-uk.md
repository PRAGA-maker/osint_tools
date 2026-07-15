---
id: service-gov-uk
name: service.gov.uk (Find a Will / probate search)
description: Use when you have a `name` and want to confirm a death and find the will/grant of probate in England & Wales — returns death date, probate record and the orderable will (from 1858).
url: https://probatesearch.service.gov.uk/
category: public-records
path:
- public-records
bestFor: Confirming a death and retrieving the probate record/will (executors, estate, dates) for England & Wales.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- associate
status: live
pricing: free
costNote: Searching the probate index is free; ordering a copy of a will or grant costs a small fee (£1.50 per document). No account needed to search.
opsec: passive
opsecNote: Searching probate records is a passive, anonymous lookup against a government index — no notification to anyone. Ordering a document requires supplying a delivery email/details, which attaches your identity to that order.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official HM Courts & Tribunals Service probate search for England & Wales — an authoritative first-party government record.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find a Will
- UK probate search
- probatesearch.service.gov.uk
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- probate
- wills
- uk
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# service.gov.uk (Find a Will / probate search)

> HMCTS's official probate search for England & Wales — confirm a death, find the grant of probate, and order the will itself (records from 1858 onward).

## When to use
You have a `name` and want to confirm whether someone has died and, if so, extract the rich detail a probate record and will carry: date of death, last address, executors and beneficiaries (named relatives/associates), and the estate. Confirming a death resolves many missing-persons and inheritance cases; the will's executors and beneficiaries open fresh leads on the living.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://probatesearch.service.gov.uk/ and choose the relevant index (post-1858 wills & probate; separate paths for soldiers' wills).
2. Search by surname and year/range of death.
3. Read the index hit: full name, date of death, probate date and registry, and often the last address and estate value.
4. Order the will/grant (£1.50) for executors and beneficiaries. Pivot: executors/beneficiaries feed people-search; the address feeds property/records; the death date anchors other timelines.

## Inputs → Outputs
- **In:** `name` (+ approximate year of death)
- **Out:** confirmed `name`, `dob` (date of death; DOB may appear in the will), last `address`, executors/beneficiaries (`associate`)
- **Empty/negative result looks like:** no probate record — meaning the person hasn't died, died without a grant of probate being taken out, or died in Scotland/NI (different systems), **not** proof they're alive. Widen the year range and check Scottish/NI equivalents.

## Gotchas & OpSec
- Covers **England & Wales only** — Scotland (ScotlandsPeople) and Northern Ireland (NI Courts) have separate probate systems.
- Not every death has a probate grant (small/intestate estates may not) — absence isn't confirmation of life.
- The searchable index is free; the informative detail (executors, beneficiaries) is in the ordered document.
- OpSec: search is passive; ordering a will attaches your details.

## Overlaps ("do both")
- Pairs with the GRO death index, obituary databases ([[inmemorium-canada]]-style for other countries), and Companies House — probate confirms death and estate; the others corroborate and extend to relatives.

## Trust & verifiability
`trust: trusted` — an authoritative government probate record. Index and documents are reliable; treat a "no result" as jurisdiction/threshold-limited rather than definitive proof of life.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | service-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
