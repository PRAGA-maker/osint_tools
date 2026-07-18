---
id: trove
name: Trove
description: Use when you have a `name`, place, or event with an Australian angle and want historical records — returns digitised newspapers, gazettes, photos, and archived Australian websites.
url: https://trove.nla.gov.au/
category: archives-cache
path:
- archives-cache
bestFor: Searching Australia's national aggregation of digitised newspapers, government gazettes, photos, and archived websites for historical mentions of a person or place.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- dob
status: live
pricing: free
costNote: Free to search and read; a free optional account lets you save, tag, and correct text. Some linked third-party items may sit behind their holder's paywall.
opsec: passive
opsecNote: You search the National Library of Australia's aggregator, never a target — the query is invisible to anyone you're researching. No login needed to search; standard research-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the National Library of Australia, aggregating collections from Australian libraries, archives, and museums; digitised primary sources (newspapers, gazettes) are authoritative, with page images to verify against.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- National Library of Australia Trove
- trove.nla.gov.au
tags:
- Archives
- newspapers
- australia
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Trove

> Australia's national discovery service — search across digitised newspapers, gazettes, photographs, maps, and archived websites from hundreds of Australian institutions in one place.

## When to use
Your subject, family history, or event has an Australian connection and you need historical documentation. Trove's digitised newspaper archive (with full-text search back to the 1800s) is exceptional for finding births/deaths/marriages notices, court reports, and mentions of a `name` tied to a `geolocation` — invaluable for older cases, genealogy, and establishing a person's history. It also archives Australian websites (the former PANDORA/Australian Web Archive) for finding vanished pages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trove.nla.gov.au/ and search a `name`, place, or event.
2. Use the category tabs — **Newspapers & Gazettes** (full-text historical press), **Images/Photos**, **Books/Diaries/Archives**, and **Websites** (archived Australian sites).
3. Refine by date range, place, and title; open an article to read the OCR text against the original page scan.
4. For vanished web pages, use the Websites category to find archived captures of Australian domains.
5. For bulk/programmatic work, use the Trove API (free key).
6. Pivot: a newspaper notice → dates (`dob`/death), relatives, and addresses; an archived site → content Wayback may have missed; images → identification leads.

## Inputs → Outputs
- **In:** `name` / `geolocation` / event / keyword (Australian focus)
- **Out:** digitised newspaper articles, gazette notices, photos, archived web pages — surfacing `name`s, dates (`dob`), places, and relationships
- **Empty/negative result looks like:** no hits — the person/event isn't in Australian sources, the name is spelled differently in period text (OCR errors are common), or it predates coverage; try spelling variants and wildcards.

## Gotchas & OpSec
- OCR of old newspapers is imperfect — search name variants, initials, and use wildcards; the "text correction" feature shows where OCR is unreliable.
- Coverage is Australia-centric; non-Australian subjects appear only when Australian sources mention them.
- Some aggregated items link out to holders that may paywall the full record; the newspaper archive itself is free.
- Fully passive and anonymous.

## Overlaps ("do both")
- Complements the Wayback Machine and genealogy tools — Trove's Australian newspaper depth and web archive catch what global archives miss; cross-check dates/names against birth-death-marriage and registry records.

## Trust & verifiability
`trust: trusted` — a national-library service serving authoritative digitised primary sources with original page images, so any newspaper or gazette finding can be verified directly against the scan.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trove |
| category | archives-cache |
| selectorsIn → selectorsOut | name, geolocation → name, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
