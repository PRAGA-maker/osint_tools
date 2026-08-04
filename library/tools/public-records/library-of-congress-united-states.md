---
id: library-of-congress-united-states
name: Library of Congress (United States)
description: Use when you have a `name`, place or topic and want historical records — newspapers, directories, photos, manuscripts, maps — that can place or identify a person — returns catalog records, digitized documents and mentions.
url: https://www.loc.gov
category: public-records
path:
- public-records
bestFor: Deep historical/archival research — digitized newspapers, city directories, photographs and manuscripts that name and place people.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free public access to catalogs and vast digitized collections; no account or payment required.
opsec: passive
opsecNote: Searching an open government library catalog is fully passive and anonymous — nothing is exposed to any individual and no login is used.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Library of Congress is the US national library; its catalogs and digitized primary sources are authoritative archival records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- library-of-congress-ask-a-librarian
- newspaper-navigator
- usa-telephone-directory-collection
- webarchive-loc-gov
- world-digital-library
aliases:
- LOC
- loc.gov
- Library of Congress
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- historical-records
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Library of Congress (United States)

> The US national library's vast free catalogs and digitized collections — a deep well for historical newspapers, directories, photos and manuscripts that name and place people the modern web forgot.

## When to use
You need historical or archival depth on a `name`, family, place, organization, or event — especially for older subjects, genealogy, cold cases, or verifying a person's past. The LOC hosts digitized historic newspapers (Chronicling America), city/telephone directory collections, photographs, maps, manuscripts and government records, many full-text searchable. This surfaces mentions, addresses and affiliations that predate or fall outside typical people-search databases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.loc.gov and search the catalog and digital collections by `name`, place, or topic.
2. Target the high-value collections: **Chronicling America** (historic newspapers, full-text), the **US Telephone/City Directory** collections (historic addresses), Prints & Photographs, and manuscript finding aids.
3. Read results: newspaper articles naming individuals, directory listings tying a `name` to a historic `address`/occupation, photos, and archival descriptions.
4. Use the LOC APIs (loc.gov JSON/`fo=json`) for programmatic queries against collections.
5. Pivot: a historic address/occupation anchors a genealogy timeline; a newspaper mention corroborates an event; a directory entry links a name to an era and place.

## Inputs → Outputs
- **In:** `name`, place, `employer-org`, or topic
- **Out:** catalog records, full-text newspaper/directory mentions, images and manuscripts — potentially a historic `name` ↔ `address`/occupation link
- **Empty/negative result looks like:** no matching records — the subject predates or falls outside the digitized holdings, or the name is spelled differently in period sources (try variants and OCR-tolerant queries). Absence isn't proof of nonexistence.

## Gotchas & OpSec
- Coverage is **deep but historical** — excellent for the past, not for current-day lookups; it complements, not replaces, live people-search.
- Full-text search relies on OCR of old print, so misspellings and misreads are common; search name variants and nearby terms.
- OpSec: **passive** — an open government catalog; nothing is exposed.

## Overlaps ("do both")
- Pairs with `[[newspaper-navigator]]`, `[[usa-telephone-directory-collection]]` and `[[webarchive-loc-gov]]` (LOC's own sub-collections) and with genealogy tools — the LOC provides the primary historical sources those workflows build on.

## Trust & verifiability
`trust: trusted` — the authoritative US national library. Digitized primary sources are reliable; the main caveat is OCR quality on old text, so confirm a critical mention against the page image itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | library-of-congress-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
