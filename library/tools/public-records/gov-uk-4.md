---
id: gov-uk-4
name: GOV.UK — Copy of Decree Absolute / Final Order
description: Use when you have a `name` and want to confirm a divorce/dissolution in England & Wales and obtain the record — returns marital-status confirmation and ex-partner/associate details via a court index search.
url: https://www.gov.uk/copy-decree-absolute-final-order
category: public-records
path:
- public-records
bestFor: Confirming and obtaining a decree absolute / final order (divorce record) in England & Wales, including via a Central Family Court index search.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: freemium
costNote: Official GOV.UK / HMCTS service. Applying for a copy carries a court fee (a search of the Central Family Court index plus a copy is a modest paid application); there is no free instant online database.
opsec: passive
opsecNote: A records request to HMCTS; the individuals named are not notified. You identify yourself to the court in the application, and a name-index search is a formal request rather than an anonymous lookup.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by HM Courts & Tribunals Service via GOV.UK; the authoritative source for divorce/dissolution records in England & Wales.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- decree absolute copy
- final order divorce record
- HMCTS divorce record
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- uk
- court
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# GOV.UK — Copy of Decree Absolute / Final Order

> The official route to confirm and obtain an England & Wales divorce record (decree absolute / final order) — including a Central Family Court name-index search when you don't know the case details.

## When to use
You have a subject's `name` and want to establish or evidence a divorce/dissolution: confirm current marital status, identify the ex-partner (`associate`), or anchor a timeline. If you know the case, you apply to the handling court; if you don't, HMCTS can search the Central Family Court index by name across a date range and return the matching final order. Useful in genealogy, background, and relationship-mapping work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/copy-decree-absolute-final-order and follow the guided steps.
2. Choose your path: apply to the specific court if you know which one handled the case, or request a **Central Family Court index search** by the person's `name` and an approximate year range if you don't.
3. Pay the applicable court fee and submit; HMCTS processes it manually.
4. Read the returned final order: parties' `name`s, date of the order, and case reference.
5. Pivot: the ex-partner `name` is an `associate` lead; the order date anchors a timeline; parties' details feed further BDM/genealogy lookups.

## Inputs → Outputs
- **In:** `name` (plus approximate date/court to narrow the index search)
- **Out:** confirmation of divorce/dissolution, parties' `name`s (subject + ex-partner `associate`), order date
- **Empty/negative result looks like:** the index search returns no matching order — the divorce may not be in England & Wales (Scotland/NI differ), fall outside the searched year range, or the person may not be divorced.

## Gotchas & OpSec
- **England & Wales only** — Scotland and Northern Ireland have separate processes and registries.
- **Human-in-the-loop:** this is a paid, manually-processed application, not an instant public database; index searches need a name and a date range to be effective.
- OpSec: passive toward the subjects; you disclose your identity to the court in the application.

## Overlaps ("do both")
- Do both with GRO marriage records and genealogy platforms — those establish the marriage and family context, while this evidences its legal end and names the ex-partner.

## Trust & verifiability
`trust: trusted` — first-party HMCTS/GOV.UK records; authoritative for divorces registered in England & Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-4 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
