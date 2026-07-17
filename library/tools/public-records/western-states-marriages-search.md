---
id: western-states-marriages-search
name: Western States Marriages Search
description: Use when you have a `name` and want historical marriage records from the western US — returns bride/groom names, dates, places, and spousal links.
url: http://abish.byui.edu/specialCollections/westernStates/search.cfm
category: public-records
path:
- public-records
bestFor: Finding pre-1900s–mid-1900s marriage records (and spouse/family links) across western US states.
selectorsIn:
- name
- dob
selectorsOut:
- name
- associate
- dob
status: live
pricing: free
costNote: Free academic genealogy index hosted by BYU-Idaho; no account or payment.
opsec: passive
opsecNote: Public historical records index; queries are anonymous and no living party is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by BYU-Idaho's McKay Library Special Collections; a curated academic index (900k+ records) extracted from primary county marriage records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- familysearch
- western-states-marriage-index
aliases:
- Western States Marriage Record Index
- WSMRI
tags:
- toddington
- curated-directory
- genealogy
- marriage-records
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Western States Marriages Search

> BYU-Idaho's Western States Marriage Record Index — 900,000+ historical marriage records from the western US, for genealogical and cold-case identity work.

## When to use
You're building out a family tree or resolving a historical identity and need marriage records from the western United States. The index covers Arizona, Idaho, Nevada (strongest, many pre-1900) plus selected counties in California, western Colorado, Montana, Oregon, Utah, eastern Washington, and Wyoming — many into the 1930s and later. Use it to confirm a spouse, a maiden name, or a marriage date/place that links people across a family — genealogical scaffolding for long-cold missing-persons and unidentified-remains work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the search form at http://abish.byui.edu/specialCollections/westernStates/search.cfm (an advanced-search form and a newer archives.byui.edu interface also exist).
2. Search by groom or bride surname/given name; narrow by state/county and date range.
3. Read the record: both spouses' names, marriage date, county/state, and the source citation.
4. Note the maiden name and spouse — these are the pivots that extend a family tree.
5. Pivot: names/dates → `[[familysearch]]` and census/obituary records to build out the family and reach living relatives who may know the subject.

## Inputs → Outputs
- **In:** a `name` (bride or groom), optionally `dob`/date range and state
- **Out:** spouse `name`/`associate`, marriage date (`dob`-adjacent), county/state, source citation
- **Empty/negative result looks like:** no match — the marriage predates/postdates coverage, occurred in a non-covered county, or the name is spelled differently in the record; try surname variants and the broader `[[familysearch]]`.

## Gotchas & OpSec
- Historical and regional: strong for western-US pre-mid-1900s, useless for recent marriages or other regions.
- Transcription/spelling variants are common in old records — search phonetic and alternate spellings.
- Coverage is county-by-county and uneven; a null is often a coverage gap, not proof no marriage occurred.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` — FamilySearch is the giant general genealogy index; this specialty index sometimes has western-state county marriages FamilySearch lacks. Cross-check both.

## Trust & verifiability
`trust: trusted` — a curated academic index by BYU-Idaho Special Collections, extracted from primary county records with citations, so entries are traceable back to source documents.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | western-states-marriages-search |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → name, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
