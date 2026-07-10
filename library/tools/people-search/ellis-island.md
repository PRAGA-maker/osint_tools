---
id: ellis-island
name: Ellis Island
description: Use when you have a `name` of a US immigrant ancestor (1892-1957) and want their arrival record — returns arrival date, age (`dob`), origin/destination `address`, ship, and family traveling together (`associate`).
url: http://heritage.statueofliberty.org
category: people-search
path:
- people-search
bestFor: Searching Ellis Island / Port of New York passenger arrival records (1892-1957) for immigrant ancestors.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
status: live
pricing: freemium
costNote: Free to search the passenger database and view record details; membership/purchase is offered for high-resolution manifest images and keepsakes, but the core genealogical data is free.
opsec: passive
opsecNote: Searching a historical immigration archive is passive and does not notify anyone (subjects are long-deceased). Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Statue of Liberty-Ellis Island Foundation from official Port of New York passenger manifests; records are authoritative primary sources (subject to manifest transcription/OCR quirks).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- family-search
- familysearch-s-united-states-record-collections
aliases:
- Ellis Island records
- Statue of Liberty passenger search
- heritage.statueofliberty.org
tags:
- Universal Contact Search and Leaks Search
- genealogy
- immigration
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Ellis Island

> The Statue of Liberty-Ellis Island Foundation's searchable database of ~65 million Port of New York arrivals (1892-1957) — trace an immigrant ancestor's arrival, origins, and family from the ship manifests.

## When to use
You are building a family history for a US subject whose ancestors immigrated through New York in the late-19th/early-20th century. A manifest record gives the arrival date, age (→ `dob`), town/country of origin, intended US destination (`address`), the ship, and — crucially — family members traveling together and the relative they were joining (`associate`). This anchors the immigrant generation of a family tree.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://heritage.statueofliberty.org and search the passenger `name` (try spelling variants — manifests and OCR mangle names).
2. Open a matching record: arrival date, age, ethnicity/origin, last residence, US destination, and ship.
3. Read the manifest detail for accompanying family and the "joining relative" — strong `associate` links.
4. The core data is free; buying a manifest image gives the full original for verification.
5. Pivot: origin/destination places and named relatives feed `[[family-search]]` and jurisdiction records to extend the tree.

## Inputs → Outputs
- **In:** immigrant `name` (+ approximate arrival year/origin)
- **Out:** arrival date, age (`dob`), origin/destination `address`, ship, family/`associate` links
- **Empty/negative result looks like:** no match — the ancestor may have arrived at a different port/era, under a variant spelling, or the manifest is unindexed; try variants and other ports before concluding absence.

## Gotchas & OpSec
- Covers Port of New York arrivals 1892-1957 only — other ports/eras need other databases.
- Manifest names are heavily mis-transcribed; search phonetic/spelling variants aggressively.
- OpSec: passive; a historical archive, no notification.
- The paid layer is for images/keepsakes; you rarely need it for the genealogical data.

## Overlaps ("do both")
- Complements `[[family-search]]` and `[[familysearch-s-united-states-record-collections]]` (broader immigration/census) — cross-reference the arrival with census and BDM records.

## Trust & verifiability
`trust: trusted` — authoritative primary manifests via the official foundation. Trust the source; confirm mis-transcribed names/details against the manifest image.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ellis-island |
| category | people-search |
| selectorsIn → selectorsOut | name → dob, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
