---
id: documentcloud
name: DocumentCloud
description: Use when you have a `name`, org, or keyword and want to search millions of primary-source documents uploaded by journalists — returns document-id, name and employer-org leads.
url: https://www.documentcloud.org
category: documents-metadata
path:
- documents-metadata
bestFor: Full-text searching, reading, and analyzing primary-source documents published by journalists and newsrooms.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
- employer-org
status: live
pricing: freemium
costNote: Free to search and read the public collection. Uploading/annotating requires a verified journalist/researcher account (also free, but gated by approval).
opsec: passive
opsecNote: Passive — searching and reading the public archive touches only DocumentCloud and reveals nothing to any subject. If you upload documents, remember they can be made public and are OCR'd and indexed — never upload sensitive material you don't intend to publish.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nonprofit platform (run by MuckRock, long tied to investigative journalism); documents are primary sources, though each is only as reliable as its uploader and origin.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- DocumentCloud
- documentcloud.org
tags:
- document-and-slides-search
- primary-sources
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# DocumentCloud

> A vast searchable archive of primary-source documents that journalists have uploaded, OCR'd, and annotated — court filings, government records, leaks, reports — with full-text search across all public documents.

## When to use
You have a `name`, an organization (`employer-org`), a place, or a keyword and want to find it inside primary-source documents: someone named in a court filing, a company in a government contract, an address in a leaked report. Because everything is OCR'd and full-text searchable, DocumentCloud surfaces mentions buried in scanned PDFs that ordinary web search misses. Strong for corroborating facts from authoritative paperwork and for finding the documents behind a news story.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.documentcloud.org and use the search over the public collection.
2. Query the `name`/`employer-org`/keyword; refine by uploader/organization, date, or access level.
3. Open a document: read it in-browser, jump to your search term's highlighted hits, and read annotations journalists added.
4. Note the document's source/uploader and original provenance.
5. Pivot: a person named in a filing → people/records tools; the source agency/org → its other documents; export via the API for bulk analysis.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, place, or keyword
- **Out:** matching primary-source documents (`document-id`), the people (`name`) and organizations (`employer-org`) named within, plus annotations
- **Empty/negative result looks like:** no hits — the term isn't in any public document (or appears only in image-only PDFs OCR missed); absence here ≠ the fact isn't documented elsewhere.

## Gotchas & OpSec
- Only searches documents someone chose to upload/make public — it's a rich but non-exhaustive slice, skewed toward newsworthy material.
- OCR quality varies — a name in a poor scan may not be findable; try spelling variants.
- OpSec: passive to search; never upload sensitive documents you don't want indexed/published.

## Overlaps ("do both")
- Complements government record portals and `[[grep-for-osint]]` — DocumentCloud gives the searchable published documents; official portals give the primary filings, and grep extracts selectors once you download a doc.

## Trust & verifiability
`trust: trusted` — reputable journalism nonprofit; documents are primary sources, but verify each document's origin/uploader since anyone approved can upload.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | documentcloud |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, employer-org → document-id, name, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
