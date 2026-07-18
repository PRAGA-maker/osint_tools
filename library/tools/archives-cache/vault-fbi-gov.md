---
id: vault-fbi-gov
name: Vault.fbi.gov
description: Use when you have a `name` (person, org, or topic) and want declassified FBI records — returns scanned FOIA documents that may contain historical intelligence on the subject.
url: https://vault.fbi.gov/search
category: archives-cache
path:
- archives-cache
bestFor: Searching the FBI's public FOIA reading room for declassified files on a named person, organisation, or event.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- associate
status: live
pricing: free
costNote: Free, official FBI FOIA library; no account or payment.
opsec: passive
opsecNote: A public reading room of already-released documents — searching it doesn't touch any living subject and reveals nothing to them. The FBI logs site visits like any government site; use a clean session if you'd rather not associate your IP with specific searches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The FBI's own FOIA library (The Vault); documents are authentic government records, though heavily redacted and largely historical, and coverage is limited to what has been processed for release.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fbi-common-fraud-schemes-united-states
- fbi-information-technology-united-states
- federal-bureau-of-investigations-value
- most-wanted
- most-wanted-criminal-pages
- sex-offender-registry-websites
aliases:
- The Vault
- FBI Records Vault
- vault.fbi.gov
tags:
- Archives of documents/newspapers
- foia
- government-records
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Vault.fbi.gov

> The FBI's public FOIA reading room ("The Vault") — thousands of declassified, scanned files searchable by person, organisation or topic.

## When to use
You have a `name` (an individual, a company, a group) or a topic/event and want to know whether the FBI holds a released file on it. The Vault contains declassified records — investigations, background files on public figures, historical cases — that can corroborate a subject's history, name known `associate`s, or surface documented events tied to them. Most valuable for historical or deceased subjects and for organisations; living private individuals usually won't appear unless previously investigated and released.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://vault.fbi.gov/search.
2. Search the `name`/`employer-org`/topic; also browse the alphabetical and category listings (the collection is organised into named files).
3. Open matching documents (scanned PDFs) and read for the subject's mentions, dates, locations, and named associates — noting heavy redactions.
4. Cross-reference names/events found in a file against other records to build a timeline.
5. Pivot: named associates and organisations become new selectors; document dates/locations anchor a historical timeline. For records not yet released, note you can file your own FOIA request.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or topic/keyword
- **Out:** scanned FOIA `document-id`s that may name `associate`s, places, dates and events
- **Empty/negative result looks like:** no matching file — the FBI has no *released* record under that term (it may hold unreleased material, or none). Absence here is not evidence of anything about the person.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public documents; no subject is alerted.
- Documents are **redacted and historical**; expect blacked-out names and dated material. Content is what survived FOIA review, not the full file.
- Scanned images vary in legibility and OCR quality; a name may exist in a document that keyword search misses — browse the relevant file directly.
- US-focused and limited to what's been processed for public release.

## Overlaps ("do both")
- Complements other government-records and archive tools; the Vault provides primary declassified documents, while `[[most-wanted]]` and registry tools cover current law-enforcement notices. Cross-check named individuals in people-search tools.

## Trust & verifiability
`trust: trusted` — authentic first-party FBI documents; reliable as primary sources, with the caveats that they're redacted, historical, and cover only released material.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vault-fbi-gov |
| category | archives-cache |
| selectorsIn → selectorsOut | name, employer-org → document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
