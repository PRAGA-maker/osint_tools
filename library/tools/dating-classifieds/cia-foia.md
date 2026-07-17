---
id: cia-foia
name: CIA FOIA
description: Use when you have a `name`, org, or event and want declassified CIA documents about it — returns full-text-searchable declassified records from the FOIA reading room.
url: https://www.cia.gov/library/readingroom/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Full-text searching declassified CIA documents for a person, organization, place, or historical event.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free official US government reading room; no account or payment.
opsec: passive
opsecNote: Searching a public government archive is anonymous and reveals nothing about your subject to anyone. Fully passive. (The old /library/readingroom/ path now redirects to cia.gov/readingroom/.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Central Intelligence Agency FOIA Electronic Reading Room; the documents are authoritative declassified government records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cia-world-factbook
- national-archives-catalog
aliases:
- CIA FOIA Reading Room
- CREST
tags:
- toddington
- curated-directory
- government-records
- foia
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# CIA FOIA

> The CIA's FOIA Electronic Reading Room — a full-text-searchable archive of declassified documents (the CREST collection), for historical and background research.

## When to use
You're researching a historical figure, organization, place, or event and want to know what appears in declassified CIA records. This is a specialist, mostly *historical* source — decades-old intelligence documents — so its relevance to a live missing-persons case is low, but it can matter for cold cases, historical identity/background work, or subjects connected to Cold War-era events, foreign governments, or notable organizations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the reading room (https://www.cia.gov/library/readingroom/ redirects to cia.gov/readingroom/).
2. Use the full-text search for a `name`, `employer-org`, place, or event; refine with document-type and date filters.
3. Open results as PDFs/scans (many are OCR'd, some are handwritten/typewritten scans of varying quality).
4. Read for names, associations, dates, and places mentioned in the documents.
5. Pivot: names/orgs surfaced → `[[national-archives-catalog]]` and other government archives; country/place context → `[[cia-world-factbook]]`.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, place, or event keyword
- **Out:** declassified documents mentioning it → `name`/`associate` links and historical context
- **Empty/negative result looks like:** no documents — the subject isn't in declassified holdings (most people never are), the material is still classified, or OCR missed the term (try spelling variants). A null says nothing about the person beyond "not in this archive."

## Gotchas & OpSec
- Overwhelmingly historical and Cold-War-weighted; not a source for living, ordinary individuals.
- Scan/OCR quality varies wildly — full-text search misses handwritten or poorly-scanned text; browse collections if search fails.
- Documents are redacted; absence of detail is often redaction, not absence of record.

## Overlaps ("do both")
- Pairs with `[[national-archives-catalog]]` — NARA holds a far broader set of US government records; the CIA reading room is the intelligence-specific slice. Search both for historical subjects.
- Pairs with `[[cia-world-factbook]]` for current country/place context alongside the historical documents.

## Trust & verifiability
`trust: trusted` — first-party US government declassified records. The documents are authoritative primary sources, though redactions and OCR limits affect what you can read.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cia-foia |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, employer-org → name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
