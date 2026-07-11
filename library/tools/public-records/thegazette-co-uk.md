---
id: thegazette-co-uk
name: The Gazette (UK Official Public Record)
description: Use when you have a `name` and want official UK notices — insolvency, deceased-estates/wills, and company notices — returns published notices tying a person to bankruptcy, death/probate, or corporate events.
url: https://www.thegazette.co.uk/
category: public-records
path:
- public-records
bestFor: Searching official UK notices — personal/corporate insolvency, deceased-estates (probate), and company notices — by name.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- address
- employer-org
- dob
status: live
pricing: freemium
costNote: Searching and reading notices is free. Placing a notice and the bulk/premium "Gazette Data Service" (structured company/insolvency/deceased-estates feeds) are paid.
opsec: passive
opsecNote: Reading the public record is passive and anonymous — no subject is notified. No account needed to search. Ordinary browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official public record of the UK (published since 1665) under His Majesty's Stationery Office / The National Archives — authoritative, legally-published notices.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- London Gazette
- Edinburgh Gazette
- Belfast Gazette
- thegazette.co.uk
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# The Gazette (UK Official Public Record)

> The UK's official journal of record — the authoritative place to find published notices of bankruptcy, deceased estates/probate, and company events tied to a named person.

## When to use
You have a `name` (or a company `employer-org`) and want to check the official record for legally-published notices: personal or corporate insolvency/bankruptcy, deceased-estates and probate notices (which often list a date of death, last address, and executors), and company/regulatory notices. High value in a missing-person or estate workup — a deceased-estates notice can confirm a death and surface an `address` and next-of-kin, and an insolvency notice can pin a person to a place and date.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thegazette.co.uk/ and use the notice search (or the "All Notices" browse with filters).
2. Enter the `name` (or `employer-org`) and narrow by notice type (Insolvency, Deceased estates, Companies) and date range.
3. Read matching notices: each is a dated, official entry naming the person/company, often with an `address`, role (e.g. executor, insolvency practitioner), and relevant dates.
4. For bulk/structured extraction, use the paid Gazette Data Service or the API; for one-off lookups the free web search is enough.
5. Pivot: an executor or insolvency practitioner is a real contact; a last address feeds property/records; a date of death confirms status.

## Inputs → Outputs
- **In:** `name`, `employer-org`, sometimes `address`
- **Out:** official notice text with `name`, `address`, roles/associates, and dates (incl. approximate `dob`/date of death context)
- **Empty/negative result looks like:** no notices for the name — most people never appear (notices are event-driven: insolvency, death/probate, specific company/regulatory acts), so absence is expected and not informative.

## Gotchas & OpSec
- Event-driven coverage: only people/companies involved in a gazetted event appear — this is a confirmation source, not a general people-finder.
- Three editions: London, Edinburgh, and Belfast Gazettes cover different UK nations — search across them.
- Paid tier is only needed for structured/bulk data; individual lookups are free.

## Overlaps ("do both")
- Pairs with Companies House and `[[gov-im]]` for the corporate side, and with obituary/probate resources for the deceased-estates side — the Gazette is the authoritative legal notice, while those add surrounding detail.

## Trust & verifiability
`trust: trusted` — the official UK journal of record; notices are legally published and authoritative, so a matching notice is strong evidence of the event it describes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thegazette-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
