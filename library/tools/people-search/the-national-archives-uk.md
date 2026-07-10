---
id: the-national-archives-uk
name: The National Archives (UK)
url: http://www.nationalarchives.gov.uk
category: people-search
path:
- people-search
description: Use when you have a `name` and want UK historical government records — returns Discovery-catalogue hits on wills, military, immigration and criminal records with `dob`/`associate`.
bestFor: Searching the UK Discovery catalogue for a named person across military, probate, immigration, criminal and census-adjacent records.
selectorsIn:
- name
- dob
selectorsOut:
- name
- dob
- associate
- document-id
status: live
pricing: freemium
costNote: Searching the Discovery catalogue is free; many record descriptions are free to view, but downloading certain digitised documents carries a per-record fee.
opsec: passive
opsecNote: Passive research on an official government catalogue; the subject is not notified and basic search needs no login. Registering (for downloads/saved searches) ties activity to an account — use a sock-puppet if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official archive of the UK government; records are primary-source and authoritative, though heavily historical and unevenly digitised.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- TNA
- Discovery catalogue
- nationalarchives.gov.uk
tags:
- people-investigations
- government-records
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# The National Archives (UK)

> The UK government's official archive and its Discovery catalogue — primary-source military, probate, immigration and criminal records searchable by person name.

## When to use
You have a `name` (optionally a `dob`/era) for a UK subject and need authoritative historical government records: military service, wills/probate, naturalisation/immigration, criminal/court, and many census-adjacent series. Best for deceased or historical subjects and for establishing verifiable life events, service history, or family links in a UK trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Discovery catalogue (discovery.nationalarchives.gov.uk) from nationalarchives.gov.uk → "Search the catalogue."
2. Enter the `name`; refine by date range, record series, or held-by archive.
3. Read the catalogue descriptions — many identify the person, dates and record type for free.
4. For digitised records, download (some free, some per-record fee); for others, note the reference to order or visit in person.
5. Pivot: a `document-id`/reference anchors a record request; named relatives/units feed `associate` and further searches; service/probate dates feed the timeline.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/date range)
- **Out:** catalogue records → `name`, `dob`/dates, `associate` (family/unit), `document-id` (archival reference)
- **Empty/negative result looks like:** no catalogue hits — common because coverage is historical and only partly digitised; the record may exist on paper only, or predate/postdate held series. A miss is not disproof.

## Gotchas & OpSec
- Heavily historical: recent/living individuals are largely absent (records are released after long closure periods).
- Digitisation is uneven — a catalogue entry may exist while the document is only viewable on-site or via paid download.
- OpSec: passive; basic search needs no login. Registering for downloads/saved searches is attributable — use a puppet account if needed.

## Overlaps ("do both")
- Pairs with `[[familysearch-2]]` and `[[censusfinder]]` — TNA holds the authoritative UK government originals, while those add family-tree context and free indexes.

## Trust & verifiability
`trust: trusted` — the official UK government archive; records are primary-source and authoritative, with the only caveats being historical scope and partial digitisation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-national-archives-uk |
| category | people-search |
| selectorsIn → selectorsOut | name, dob → name, dob, associate, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
