---
id: library-and-archives-canada-lac
name: Library and Archives Canada (LAC)
description: Use when you have a name (and rough era) and want Canadian historical records on a person — returns dob, associate/family links, address, and document-id references from census, immigration and military files.
url: https://www.bac-lac.gc.ca/eng/Pages/home.aspx
category: public-records
path:
- public-records
bestFor: Searching Canadian census, immigration, military and genealogical collections by name to build a historical/family picture of a person.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- associate
- address
- document-id
status: live
pricing: free
costNote: Free to search and view most digitised records online; ordering high-resolution copies of some archival items can carry a fee.
opsec: passive
opsecNote: Passive — you are querying a national archive's public collections, not the subject. Nothing is exposed to the person searched. Standard puppet-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official national archive of Canada (Bibliothèque et Archives Canada); records are authoritative government/archival sources.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LAC
- Bibliothèque et Archives Canada
- bac-lac.gc.ca
tags:
- genealogy
- government-records
- archives
- canada
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Library and Archives Canada (LAC)

> Canada's national archive — search it by name to pull census, immigration, military and genealogical records that anchor a person in time and place.

## When to use
You have a `name` (ideally with an approximate era or birth year) and a Canadian connection, and you want historical/biographical records: census entries, immigration and citizenship files, military service records (especially WWI), or family-history material. Strongest for older subjects, ancestry work, and confirming birth era, relatives and places of residence rather than current-day contact details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bac-lac.gc.ca/eng/Pages/home.aspx and use **Search the collection** (or the collection-specific databases: Census, Immigration, Military Heritage, Genealogy).
2. Enter the target `name`; add a birth year, place or record type to narrow a common name.
3. Open matching records — many are digitised (scanned census pages, service files) and viewable free.
4. Read out `dob`/birth era, family members (`associate`), place of residence (`address`), and the archival reference/`document-id` for citation or ordering a fuller copy.
5. Pivot: family names and places feed genealogy tools and further record searches; a document-id lets you request the complete file.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/era, place).
- **Out:** `dob`/birth era, `associate` (household/family members), `address` (historical residence), `document-id` (archival references).
- **Empty/negative result looks like:** no matching records — the person may predate/postdate the digitised holdings, have no Canadian record, or be indexed under a variant spelling; try name variants before concluding a miss.

## Gotchas & OpSec
- **Canada-only** and skewed historical — great for ancestry/older records, weak for living-person current data.
- Digitisation is uneven; some collections are index-only and require ordering the physical file.
- Common names return many hits; always corroborate with a second data point (year, place, relative).

## Overlaps ("do both")
- Complements Canadian civil/vital-records and genealogy tools: LAC provides the authoritative *archival* layer (census/military/immigration) that generic people finders don't hold.

## Trust & verifiability
`trust: trusted` — a first-party national archive (Government of Canada); the records are authoritative primary sources, though transcription/indexing errors in old documents mean spellings and dates should be read from the scanned original where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | library-and-archives-canada-lac |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → dob, associate, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
