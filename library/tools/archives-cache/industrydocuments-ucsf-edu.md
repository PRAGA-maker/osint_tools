---
id: industrydocuments-ucsf-edu
name: UCSF Industry Documents Library
description: Use when you have a `name` (executive, scientist, lobbyist) or `employer-org` and want their internal industry documents — returns document-id, associate links and name mentions in tobacco/drug/chemical/fossil-fuel files.
url: http://industrydocuments.ucsf.edu/
category: archives-cache
path:
- archives-cache
bestFor: Full-text searching millions of internal corporate documents (tobacco, drug, chemical, food, fossil-fuel, opioid) for named individuals and their communications.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
- associate
status: live
pricing: free
costNote: Free public access, no account required to search or download; run by a public university library.
opsec: passive
opsecNote: Searching a public academic archive of historical corporate documents; nothing touches any living subject and no login is needed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UCSF Library; documents are authenticated originals released via litigation, FOIA and whistleblowers, with stable citations and metadata.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Industry Documents Library
- UCSF Truth Tobacco
- industrydocuments.ucsf.edu
tags:
- Archives of documents/newspapers
- corporate-documents
- full-text-search
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# UCSF Industry Documents Library

> A free, full-text-searchable archive of ~19 million internal corporate documents (tobacco, drug, chemical, food, fossil-fuel, opioid) — the place to find an executive, scientist or lobbyist named inside company memos, emails and depositions.

## When to use
You have a `name` or an `employer-org` and want to know whether that person or company appears in the internal record of a targeted industry. These are the actual internal emails, memos, reports, depositions and marketing files released through litigation and FOIA. Searching a name can surface who someone corresponded with, what they signed, and which projects they ran — decades-deep, with exact document citations. Strong for historical/biographical profiling and for mapping professional networks (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.industrydocuments.ucsf.edu/ and use the search box (or the advanced search).
2. Enter a `name` in quotes (`"John Smith"`) or an `employer-org`; narrow with the collection facets (Tobacco, Drug, Chemical, Food, Fossil Fuel, Opioids) and document type/date.
3. Open a hit — each document has full text (OCR), a stable document ID/Bates number, dates, author/recipient fields, and a permalink.
4. Read the author/recipient/cc fields to build a contact network; note the document-id for citation.
5. Pivot: recipients and cc's become new `name`/`associate` searches; an org + era feeds broader corporate-history research. (An API and bulk data are available for scaled queries.)

## Inputs → Outputs
- **In:** `name` (person) or `employer-org`
- **Out:** matching `document-id`s (Bates numbers), `name` mentions, author/recipient `associate` links, dated internal communications
- **Empty/negative result looks like:** zero documents for a name — the person isn't in the released corpus (which is broad but industry-specific and historical); try surname-only or known aliases, and check spelling in period documents.

## Gotchas & OpSec
- Scope is specific: only the covered industries and only what was released — absence is not exoneration or proof of non-involvement.
- OCR quality varies on old scans; use fuzzy/alternate spellings and Bates-number ranges.
- Documents are historical — a match dates the activity, it doesn't imply current status.
- OpSec: passive, no account, no subject notification.

## Overlaps ("do both")
- Complements general newspaper/archive search and corporate-registry lookups — those give the public record; this gives the internal one on the same people and firms.

## Trust & verifiability
`trust: trusted` — a university-library archive of authenticated primary-source documents with stable citations; each hit is a real, citable document you can read in full, not a secondary claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | industrydocuments-ucsf-edu |
| category | archives-cache |
| selectorsIn → selectorsOut | name, employer-org → document-id, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
