---
id: filae-com
name: Filae (filae.com)
description: Use when you have a `name` and want French civil/genealogical records (births, marriages, deaths, census) — returns dob/dates, places (address), and family associate links.
url: https://en.filae.com/
category: public-records
path:
- public-records
bestFor: Searching French état civil (civil registration), parish, census, and military records by name for genealogy/identity work.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
- name
status: live
pricing: freemium
costNote: Free to register and build a tree and to run searches that show whether matches exist; viewing the indexed archive records (billions of entries) requires a paid subscription.
opsec: passive
opsecNote: Searching historical records doesn't notify anyone. Most subjects are deceased, but living relatives can appear in recent/collaborative trees — handle their data responsibly. Use a research account you don't mind associating with the queries.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial French genealogy platform combining official digitized archives with user-submitted trees. Archive records are authoritative; user trees are unverified and can contain errors.
missingPersonsRelevance: high
coverage:
- fr
auth: account
api: false
localInstall: false
registration: true
aliases:
- filae.com
- Filae genealogie
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- france
- civil-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Filae (filae.com)

> A large French genealogy platform: search names across digitized civil-registration, parish, census, and military archives (plus user family trees).

## When to use
You're researching a person with French roots or a French records trail and you need civil-status data — a `name` to birth/marriage/death dates (`dob`/dates), the towns involved (`address`), and family relationships (`associate`). Strong for confirming identity, dates, and kinship in France, and for tracing ancestry or locating relatives of a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (free) account at filae.com.
2. Search a `name`, optionally with a place and date range.
3. Free search shows whether matching records exist; open an indexed archive record (behind subscription) for the details — names, dates, places, parents/spouse.
4. Pivot: relatives found become new subjects; places anchor a geographic trail; dates confirm/deny an identity against other records.

## Inputs → Outputs
- **In:** `name` (+ place/date range)
- **Out (records, paid):** birth/marriage/death `dob`/dates, places (`address`), parents/spouse/kin (`associate`), the person's `name` as recorded
- **Empty/negative result looks like:** no matches, or match teasers you can't open without a subscription. No match may mean the record isn't digitized/indexed (coverage varies by département), not that the person didn't exist.

## Gotchas & OpSec
- Human-in-the-loop: registration required, and full record views are paywalled (payment-wall-partial).
- Two data types: official archive records (authoritative) vs. collaborative user trees (unverified — corroborate before trusting).
- Coverage is French and varies by region/era; pair with departmental archives for gaps.
- OpSec: passive; mind living relatives in recent trees.

## Overlaps ("do both")
- Pairs with Geneanet and the free departmental Archives départementales — Filae's index is broad but paywalled, Geneanet has its own trees/records, and the departmental archives offer free primary scans; cross-check across all three.

## Trust & verifiability
`trust: community` — a commercial platform whose *archive* records are authoritative (digitized official registers) but whose *user trees* are unverified. Rely on the primary record, treat trees as leads, and confirm against the original scan where it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filae-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
