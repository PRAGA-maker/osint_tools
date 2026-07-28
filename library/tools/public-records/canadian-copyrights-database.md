---
id: canadian-copyrights-database
name: Canadian Copyrights Database
description: Use when you have a `name` or work title and want Canadian copyright registrations — returns registered works with author/owner names and dates.
url: https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/copyright/canadian-copyrights-database
category: public-records
path:
- public-records
bestFor: Searching Canada's official copyright register for works, authors, and owners (registrations from 1991 on).
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free official CIPO database; no account required.
opsec: passive
opsecNote: You search a public government register, not the individual — nothing is signalled. Standard web logging on the CIPO/canada.ca side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Canadian Intellectual Property Office (CIPO / ISED); authoritative for copyright registrations filed in Canada.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CIPO Copyrights Database
- Canadian Copyright Database
tags:
- copyright
- public-records
- canada
- intellectual-property
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- canadian-business-research
- canadian-department-of-finance
- canadian-importers-database
- canadian-intellectual-property-office
- canadian-trademarks-database
- completed-access-to-information-requests
- federal-corporation-search-canada
- gov-data-canada
- government-of-canada-open-data
- search-for-a-federal-corporation
---

# Canadian Copyrights Database

> Canada's official copyright register (CIPO) — search registered works to tie a `name` to authored/owned intellectual property and the dates behind it.

## When to use
You have a `name` (author, artist, author's business) or a work title and want to check for Canadian copyright registrations. A hit links a person or organisation to specific creative works, registration dates, and often an owner (which may differ from the author) — useful for corroborating a professional identity, establishing what someone created and when, or surfacing a business (`employer-org`) that holds the rights. (The database moved from the old `ic.gc.ca` URL to the current CIPO/ISED site.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CIPO Canadian Copyrights Database at the ised-isde.canada.ca copyright page and launch the search.
2. Search by work title, or by author/owner `name` (note the register is primarily title-searchable; author/owner search is more limited).
3. Open a registration and read: title, author, owner/claimant, registration number and date, and category of work.
4. Pivot: an owner `employer-org` distinct from the author is a lead; registration dates anchor a timeline; the author name feeds further people-search.

## Inputs → Outputs
- **In:** `name` (author/owner) or work title
- **Out:** registered work(s), author and owner `name`/`employer-org`, registration number and dates
- **Empty/negative result looks like:** no registration — most works are NOT formally registered (copyright is automatic in Canada), so absence says little; and coverage starts from 1991.

## Gotchas & OpSec
- Registration is **optional** in Canada, so the vast majority of copyrighted works never appear here — a null result is weak evidence.
- Search is largely by **title**; name-based searching is limited, so you may need the work's title to find the person.
- OpSec: passive; a public government register.

## Overlaps ("do both")
- Pairs with CIPO's Trademarks and Patents databases and Canadian corporate registries — use those to round out an entity's IP and business footprint; copyright alone is a narrow slice.

## Trust & verifiability
`trust: trusted` — official CIPO/Government of Canada data, authoritative for what it records. Its limitation is scope (voluntary registrations from 1991), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-copyrights-database |
