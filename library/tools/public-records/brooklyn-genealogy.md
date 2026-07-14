---
id: brooklyn-genealogy
name: Brooklyn Genealogy Information Page
description: Use when you have a name tied to historical Brooklyn/Kings County NY and want transcribed records — returns census, cemetery, church, directory and institutional record entries.
url: http://bklyn-genealogy-info.stevemorse.org/index.html
category: public-records
path:
- public-records
bestFor: Researching historical Brooklyn / Kings County (NY) people via transcribed census, cemetery, church and directory records.
selectorsIn:
- name
selectorsOut:
- name
- address
- associate
- dob
status: live
pricing: free
costNote: Free to browse and search the transcribed record collections; no account.
opsec: passive
opsecNote: Reading transcribed historical records is passive and alerts no one. The site logs standard web access; VPN for sensitive work. This is historical genealogical research, inherently non-intrusive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing volunteer-transcribed genealogy resource (hosted on Steve Morse's domain); reliable as a pointer to historical records, but transcriptions can contain errors — verify against the original where it matters.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Brooklyn Genealogy Info
- bklyn-genealogy-info
- Kings County NY genealogy
tags:
- genealogy
- vital-records
- brooklyn
- new-york
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Brooklyn Genealogy Information Page

> A deep, volunteer-built archive of transcribed historical Brooklyn / Kings County (NY) records — censuses, cemeteries, churches, directories and institutions — searchable by name.

## When to use
You have a `name` connected to historical Brooklyn / Kings County, New York (family history, an old address, a deceased relative, an heir search) and want the transcribed records that predate the big commercial genealogy sites' coverage. The collection spans census extracts, cemetery/burial listings, church registers, city directories and institutional rosters — the kind of records that establish family links, dates and old addresses for building a lineage or confirming a historical identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://bklyn-genealogy-info.stevemorse.org/index.html.
2. Browse the topic index (census, cemeteries, churches, directories, institutions) or use a site search for a surname.
3. Open the relevant transcription and scan for your `name` — note associated names, dates, addresses and institutions.
4. Record the source citation so you can order/verify the original document.
5. Pivot: family names become `associate`s to trace; an old `address` feeds historical directory/map work; dates feed `[[chicago-cook-county-genealogy]]`-style vital-record confirmation in NY.

## Inputs → Outputs
- **In:** a `name` (surname works best for browsing transcriptions)
- **Out:** record entries giving `name`, historical `address`, `associate`s (family/household), and event `dob`/dates
- **Empty/negative result looks like:** no entry in the transcribed sets — the record may not be transcribed, may be spelled differently, or may fall outside Brooklyn/Kings County. Absence here is not proof; check other NY genealogy sources.

## Gotchas & OpSec
- **Historical/geographic scope:** Brooklyn / Kings County, and largely older records — not a tool for locating living people directly (it builds the family/historical scaffold).
- Volunteer transcriptions can contain errors or omissions; treat entries as leads and verify against the original record for anything consequential.
- Passive historical research; nobody is notified.

## Overlaps ("do both")
- Pairs with `[[chicago-cook-county-genealogy]]`-style One-Step vital-record searches and national genealogy sites to confirm dates and extend a lineage.
- Feeds people-search when a historical thread connects to a living relative or heir.

## Trust & verifiability
`trust: community` — a respected but volunteer-transcribed archive; excellent for surfacing hard-to-find historical Brooklyn records, but confirm names, dates and relationships against the original source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brooklyn-genealogy |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, associate, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
