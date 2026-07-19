---
id: federal-bureau-of-investigations-value
name: FBI Records Vault (vault.fbi.gov)
description: Use when you have a `name` (person or org) and want declassified/FOIA FBI records about them — returns scanned case files, documents, and media from the FBI's public reading room.
url: https://vault.fbi.gov/
category: dark-web
path:
- dark-web
bestFor: Searching the FBI's public FOIA reading room for declassified records on a person, organisation, or historical event.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- associate
- geolocation
status: live
pricing: free
costNote: Free public U.S. government FOIA reading room; no account or payment required.
opsec: passive
opsecNote: Reading a U.S. government public records site is passive and touches no target. It's an official .gov site, so use normal browsing hygiene; a sock-puppet session is optional, not required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The FBI's official public document vault; records are authentic government FOIA releases (often redacted). Authoritative, though limited to what has been declassified and published.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vault-fbi-gov
- most-wanted
aliases:
- FBI Vault
- vault.fbi.gov
- FBI Records
tags:
- toddington
- curated-directory
- deep-web-search
- foia
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# FBI Records Vault (vault.fbi.gov)

> The FBI's official FOIA reading room — thousands of declassified, scanned records searchable by name, organisation, or topic; authoritative primary-source documents on people and events of investigative interest.

## When to use
You have a `name` (a person or `employer-org`) or a historical event and want to know whether the FBI holds released records on them. The Vault contains declassified case files, correspondence, and reports — valuable for background on deceased or historical subjects, organisations, and notable events, and for corroborating associations, locations, and timelines from primary documents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://vault.fbi.gov/ and use the search box or browse categories/recent releases.
2. Search the subject `name` or `employer-org`; try known aliases and variant spellings.
3. Open matching record sets — they're scanned PDFs (often OCR'd, often redacted). Read for names, dates, places, and associations.
4. Note redactions (black bars) and release dates; missing material may exist but be withheld.
5. Pivot: named `associate`s and `geolocation`s in documents feed further record searches; a `document-id`/file number supports a targeted FOIA request for more.

## Inputs → Outputs
- **In:** `name` or `employer-org` (person/organisation/event)
- **Out:** declassified FBI `document-id` records, with `associate` names and `geolocation`s inside them
- **Empty/negative result looks like:** no released records match — the FBI may hold nothing, or nothing has been declassified/published (living-person files are usually withheld). Absence here is not proof the FBI has no file; consider a direct FOIA request.

## Gotchas & OpSec
- Coverage is limited to *released* records — heavy on historical/deceased subjects, light on living private individuals.
- Documents are redacted; treat black-bar gaps as withheld, not nonexistent.
- OCR quality varies; search may miss text inside poorly scanned pages — browse the file too.

## Overlaps ("do both")
- Pairs with `[[most-wanted]]` and other government record sources — the Vault gives historical case files, while wanted lists and registries give current status; a direct FOIA request extends beyond what's pre-published.

## Trust & verifiability
`trust: trusted` — official U.S. government FOIA releases; documents are authentic primary sources, with the caveat that redactions and non-release limit completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-bureau-of-investigations-value |
| category | dark-web |
| selectorsIn → selectorsOut | name, employer-org → document-id, associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
