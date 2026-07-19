---
id: arizona-genealogy-birth-and-death-certificates
name: Arizona Genealogy Birth and Death Certificates
description: Use when you have a `name` (and roughly a date/place) and want scanned Arizona birth or death certificates in the public window — returns imaged certificates with `dob`, parents/relatives, and place details.
url: http://genealogy.az.gov/
category: public-records
path:
- public-records
bestFor: Retrieving scanned Arizona birth (public after 75 yrs) and death (public after 50 yrs) certificate images by name and date.
selectorsIn:
- name
- dob
selectorsOut:
- document-id
- dob
- associate
- address
status: live
pricing: free
costNote: Free Arizona Department of Health Services genealogy service; no account or fee to search or view certificate images.
opsec: passive
opsecNote: You search a state vital-records archive; the query is not tied to any living subject and nothing is disclosed to third parties. Fully safe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Arizona Department of Health Services genealogy site; the images are scans of genuine state vital records (not certified copies), so the data is authoritative for the covered periods.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- genealogy.az.gov
- Arizona DHS genealogy
tags:
- vital-records
- genealogy
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- arizona-inmate-datasearch
---

# Arizona Genealogy Birth and Death Certificates

> Arizona's official free genealogy portal — searchable, imaged birth and death certificates once they enter the public window (births 75+ years old, deaths 50+ years old). One of the few U.S. states offering free online certificate images.

## When to use
You have a `name` tied to Arizona and want primary vital-record documentation from the historical window: a birth certificate (public 75 years after birth) or a death certificate (public 50 years after death). These scans anchor a `dob`/date of death, name parents and informants (relatives/`associate`s), and give places of birth/death/residence — invaluable for building a family tree, confirming an ancestor's identity, or extending relative chains in a long-cold case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://genealogy.az.gov/ (the search runs on the AZDHS genealogy application).
2. Choose birth or death records and search by `name`, with a date range and/or place to disambiguate.
3. Open a matching result to view the scanned original certificate image.
4. Read it for `dob`/death date, parents' and informant's names (`associate`s), and places (`address`); download the image for your file.
5. Pivot: parents/informants named on the certificate extend the family graph into other genealogy and people-search tools; places feed local-records searches.

## Inputs → Outputs
- **In:** `name` (+ approximate `dob`/date and place)
- **Out:** `document-id` (scanned certificate), confirmed `dob`, named `associate`s (parents/informants), and `address`/place details
- **Empty/negative result looks like:** no match — either the record falls outside the public window (too recent), the name/date differs from the record, or the certificate isn't digitised; broaden the date range and try name variants before concluding it's absent.

## Gotchas & OpSec
- Human-in-the-loop: none; direct search and image view.
- OpSec: fully **passive**; a state historical archive, no exposure.
- Window limits: only births ≥75 years and deaths ≥50 years old are public here — for more recent records you must go through the Arizona Office of Vital Records. Images are not certified copies (research use).
- Older handwritten certificates can be hard to read and are indexed with transcription errors; check the image itself, not just the index entry.

## Overlaps ("do both")
- Pairs with FamilySearch, findagrave, and other states' vital-record portals — Arizona gives free imaged certificates for its window; cross-state and aggregator tools fill gaps outside Arizona or outside the public date range.

## Trust & verifiability
`trust: trusted` — an official Arizona DHS service serving scans of genuine state vital records; the documents are authoritative primary sources for the covered periods, with the only caveats being the public-window limits and normal historical-transcription care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arizona-genealogy-birth-and-death-certificates |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → document-id, dob, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
