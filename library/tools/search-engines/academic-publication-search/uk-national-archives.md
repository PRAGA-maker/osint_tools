---
id: uk-national-archives
name: UK National Archives (Discovery)
description: Use when you have a `name`, place, or record reference and want UK government/historical records — returns catalogue entries (military, wills, court, migration, government files) with dates and access info.
url: https://discovery.nationalarchives.gov.uk/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Searching the UK National Archives catalogue for a person across government, military, legal, and historical records.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
status: live
pricing: freemium
costNote: The Discovery catalogue is free to search and browse; many records are free to view online, but some digitised documents carry a small download fee or are held by partner sites, and some are physical-only (in-person at Kew).
opsec: passive
opsecNote: Searching a public national-archive catalogue is passive and leaves no footprint on any living subject. Records here are overwhelmingly historical; there is no live-person surveillance surface.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official UK government archive; catalogue entries and digitised records are authoritative primary sources, though the catalogue describes holdings that may be off-site or restricted.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- findmypast-co-uk
- ancestry-family-search-engine-united-kingdom
- freebmd-org-uk
aliases:
- The National Archives Discovery
- TNA Discovery
- discovery.nationalarchives.gov.uk
tags:
- uk-records
- government-archive
- genealogy
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# UK National Archives (Discovery)

> The official UK government archive's online catalogue: search a name or reference across a thousand years of state, military, legal, and migration records held at Kew and partner archives.

## When to use
You are building the historical record of a UK-connected person — genealogy, a missing person's family history, military service, naturalisation/migration, wills and probate, criminal/court proceedings, or old government files that mention them. Discovery is the master catalogue: search a `name` and you may find record references with dates, places, and sometimes birth/death or address detail, plus whether the document is online, downloadable, off-site, or held by a partner (e.g. Findmypast, Ancestry).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discovery.nationalarchives.gov.uk/ and search the `name` (try variants/spellings), optionally narrowing by date, place, or record series.
2. Read the catalogue entry: description, covering dates, holding archive, and access status.
3. For online records, view/download directly (some carry a small fee); for off-site/partner records, follow the pointer to the holding institution or plan an in-person Kew visit.
4. Use the API for systematic catalogue queries where appropriate.
5. Pivot: dates/places feed `[[freebmd-org-uk]]` and genealogy sources; a partner-held record feeds `[[findmypast-co-uk]]` / `[[ancestry-family-search-engine-united-kingdom]]`.

## Inputs → Outputs
- **In:** `name`, place, date, or record reference (UK-focused)
- **Out:** catalogue entries with descriptions, covering dates, holding archive, and — in the record itself — potential `dob`, `address`, and family detail
- **Empty/negative result looks like:** no catalogue match — the person left no record in TNA's holdings, is recorded under a variant name, or the record sits with a local/other archive not indexed here; not proof of absence.

## Gotchas & OpSec
- Catalogue vs content: many entries describe documents that are off-site, restricted, physical-only, or held by paid partners — a hit is a pointer, not always instant access.
- Partial paywall: some digitised downloads cost a small fee, and partner-hosted records may sit behind subscriptions.
- Historical focus: strongest for the deceased and historical events; recent personal records are usually closed under access rules.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[findmypast-co-uk]]`, `[[ancestry-family-search-engine-united-kingdom]]`, and `[[freebmd-org-uk]]` — Discovery tells you a record exists and who holds it; the genealogy platforms often deliver the digitised image and index the same series with easier person-search.

## Trust & verifiability
`trust: trusted` — the authoritative UK government archive; catalogue descriptions and digitised records are primary sources you can cite, while remembering the catalogue points to holdings that may need further access steps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-national-archives |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, dob, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
