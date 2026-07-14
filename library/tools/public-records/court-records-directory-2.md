---
id: court-records-directory-2
name: CourtReference — US Court Records Directory
description: Use when you have a `name` and a US location and need the right court/online case-search portal to look them up — returns pointers to court dockets and case records (name, case document-id, dates).
url: https://www.courtreference.com
category: public-records
path:
- public-records
bestFor: Finding the correct US trial court and its online case/docket search for a given county/state.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- dob
status: live
pricing: free
costNote: The directory of court links is free; the site heavily promotes paid Intelius background-search products alongside the free links — ignore those and use the official court portals it points to.
opsec: passive
opsecNote: Browsing the directory is passive. OpSec risk lives in the destination court portal (some log searches or require login); assess it there. Do not route your search through the promoted paid data-broker products.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party directory (affiliated with Intelius), not an official court source; the value is its curated links to official court portals, which you should treat as the authoritative endpoints.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- courtreference.com
- Court Records Directory
tags:
- court
- inmate
- us
- directory
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# CourtReference — US Court Records Directory

> A free directory that routes you to the right US trial court and its online case/docket search — a gateway, not a records database itself.

## When to use
You have a subject's `name` and a US location and need to search court records, but US courts are fragmented across 3,000+ counties with no single portal. CourtReference indexes, by state and county, which courts exist and which offer online case/docket/calendar search, so you can jump straight to the correct official portal. Reach for it as the first hop before running a name against a specific court's records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.courtreference.com and drill down by state → county → court type.
2. Follow the link to that court's **official** online record/docket search (ignore the promoted Intelius/paid background-check widgets).
3. On the official portal, search the subject's `name`.
4. Read results there: case captions, case `document-id`/docket numbers, filing dates, and sometimes `dob`/party details.
5. Pivot: a case number feeds full docket retrieval; parties/associates in a case become new leads.

## Inputs → Outputs
- **In:** `name` (+ US county/state to locate the right court)
- **Out:** pointers to court portals that return `name`, case `document-id`, dates, and sometimes `dob`
- **Empty/negative result looks like:** no online-search link for that county — many courts have no public online records, so you may have to request records in person; and the directory itself returns records for nothing (it's a link index).

## Gotchas & OpSec
- **It's a directory, not a search engine** — it never returns case records itself; the data is at the linked official courts.
- The site aggressively upsells Intelius paid products; those are data-broker resells, not court records — stick to the official-court links.
- OpSec: passive at the directory; check the destination portal's logging/login before searching.

## Overlaps ("do both")
- Do both with `[[county-clerks-recorded-doc-s-by-state]]` (SearchSystems) — both are gateways to official US records, but they index different record types (courts vs recorded documents/vital/property).

## Trust & verifiability
`trust: community` — a third-party, Intelius-affiliated directory; trust the official court portals it links to, not the site's own paid products.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-records-directory-2 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
