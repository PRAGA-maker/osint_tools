---
id: usa-telephone-directory-collection
name: USA Telephone Directory Collection (Library of Congress)
description: Use when you have a historical US `name`, `phone`, or `address` (roughly 1880s–1980s) and want to place a person at an address/number in that era — returns `address`, `phone`, and `name` from scanned directories.
url: https://www.loc.gov/collections/united-states-telephone-directory-collection/
category: phone
path:
- phone
bestFor: Historical US white/yellow-pages lookups (1887–1987) for cold cases, genealogy, and confirming an era-specific address or number.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- name
status: live
pricing: free
costNote: Free digitized collection from the Library of Congress; PDFs are downloadable at no cost, no account required.
opsec: passive
opsecNote: Fully passive — you are reading digitized historical documents on loc.gov, not querying any live person or service. No subject is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by the Library of Congress; the scans are authoritative primary documents, though OCR/searchability is imperfect and you often browse a directory page-by-page.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Library of Congress telephone directories
- historical phone books US
tags:
- Phone numbers
- historical
- genealogy
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- library-of-congress-ask-a-librarian
- library-of-congress-united-states
- newspaper-navigator
- webarchive-loc-gov
---

# USA Telephone Directory Collection (Library of Congress)

> ~3,500 digitized American white- and yellow-pages directories (1887–1987) — the way to put a name, number, or address together in an era long before online people-search existed.

## When to use
You're working a cold case, a long-missing person, or genealogy, and need to place someone at a specific US address or phone number in the 20th century (or earlier). Modern people-search tools rarely reach before the 1990s; these scanned directories do, letting you confirm a historical `address`↔`name`↔`phone` linkage, identify former neighbors/associates listed nearby, or trace a family's moves across editions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the collection at loc.gov and browse/filter by state, city, and year to find the right directory edition.
2. Open the directory (viewer or downloaded PDF). White pages are alphabetical by surname; yellow pages by business category.
3. Locate the `name`, `address`, or `phone` — read across the entry for the other fields. Neighboring entries reveal people at nearby addresses (potential associates).
4. Compare across editions/years to track when someone appeared, moved, or vanished from a locality.
5. Pivot: a historical address feeds census/property records and genealogy tools; nearby listings feed associate mapping.

## Inputs → Outputs
- **In:** historical `name`, `address`, or `phone` + a place and rough year
- **Out:** period `address`, `phone`, listed `name`, and nearby listings (possible associates)
- **Empty/negative result looks like:** the person isn't in that city's directory for that year — common (unlisted numbers, too poor for a phone, wrong city/year, or a name variant). Try adjacent years, spelling variants, and nearby towns before concluding absence.

## Gotchas & OpSec
- Coverage is by scanned edition, not a unified search — you must pick the right city/year and often read pages manually; OCR search is partial.
- Directories omit the unlisted, the phoneless, and post-1987 records; a miss is not evidence of non-existence.
- Data is a historical snapshot — an address/number was valid only for that edition.
- OpSec: fully passive; nothing but you and a library archive.

## Overlaps ("do both")
- Pairs with census records, historical newspapers, and genealogy databases — directories give year-by-year address/phone granularity those lack, while census and genealogy give family structure and life events the directory omits.

## Trust & verifiability
`trust: trusted` — primary-source scans held by the Library of Congress. The documents are authoritative; the limitation is findability (right edition, OCR quality), not accuracy. Corroborate a linkage across multiple years/sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usa-telephone-directory-collection |
| category | phone |
| selectorsIn → selectorsOut | name, phone, address → address, phone, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
