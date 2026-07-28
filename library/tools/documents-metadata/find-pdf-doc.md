---
id: find-pdf-doc
name: Find-pdf-doc
description: Use when you have a `name` or `employer-org` and want to surface documents (PDF/DOC/PPT/XLS) mentioning them across the web — returns `document-id` leads and file URLs.
url: http://www.findpdfdoc.com
category: documents-metadata
path:
- documents-metadata
bestFor: Keyword search restricted to document filetypes (PDF, DOC, PPT, XLS, TXT) rather than web pages.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free document search engine; no account.
opsec: passive
opsecNote: Searching is passive, but the results link to third-party file hosts of unknown reputation. Do not open or download results on your real machine — use a sandbox/sock-puppet, since document downloads can carry tracking or malware.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A basic third-party filetype search engine that indexes documents it does not host; result quality and hosted-file safety are unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- findpdfdoc.com
- PDF DOC search engine
tags:
- document-and-slides-search
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Find-pdf-doc

> A search engine that returns only documents — PDF, DOC, PPT, XLS, TXT — so a name or org query surfaces reports, rosters, and slide decks that plain web search buries.

## When to use
You have a `name`, `employer-org`, or other keyword and want documents rather than web pages — e.g. a résumé, membership roster, conference program, meeting minutes, or report that mentions the subject. Filetype-scoped search often surfaces PDFs/spreadsheets that carry richer detail (and metadata) than a normal page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.findpdfdoc.com.
2. Choose the filetype tab (PDF / DOC / PPT / XLS / TXT, etc.) and enter your keyword — a `name`, an `employer-org`, or a distinctive phrase.
3. Review the result links; each points to an externally hosted file.
4. Download promising files **into a sandbox**, then inspect their contents and metadata (author, dates, software) with an EXIF/metadata tool.
5. Pivot: document metadata often yields a real `name`, creation software, or internal path — feed those into further searches.

## Inputs → Outputs
- **In:** `name` / `employer-org` (keyword query)
- **Out:** `document-id` (file links), `metadata-exif` (once you open the file and read its embedded metadata)
- **Empty/negative result looks like:** a results page with no listings for that keyword/filetype — try a different filetype tab or a broader query before concluding nothing exists.

## Gotchas & OpSec
- The engine **does not host files** — results live on third-party sites of unknown trust. Treat every download as untrusted: sandbox it, never open on your investigation machine.
- Coverage and freshness are limited compared to Google `filetype:` dorks — use this as a supplement, not a replacement.
- Passive to search; the risk is entirely in fetching the linked files.

## Overlaps ("do both")
- Pairs with a Google `filetype:pdf "Name"` dork — do both, since each index catches documents the other misses; then run any file through an EXIF/metadata extractor.

## Trust & verifiability
`trust: unverified` — a bare-bones third-party filetype search engine with no transparency about its index or the safety of hosted files; corroborate every hit and handle downloads defensively.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-pdf-doc |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, employer-org → document-id, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
