---
id: search-by-filetype
name: Search by FileType
description: Use when you have a `name`, `employer-org`, or keyword and want documents — returns indexed files (PDF/DOC/XLS/PPT) matching the term via a Google Custom Search Engine.
url: https://cse.google.com/cse/publicurl?cx=013991603413798772546:mu-oio3a980
category: search-engines
path:
- search-engines
bestFor: Finding documents (PDF, Office files) tied to a person, org, or keyword using a filetype-scoped Google CSE.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account needed.
opsec: passive
opsecNote: You search Google's index of already-public documents — no target is queried. Opening a found file is passive; the file's own metadata (author, software, GPS) may reveal more than its contents, which is often the point.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community CSE that applies filetype scoping to Google's index; results are genuine index entries, but the preset's scope depends on its anonymous maintainer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- filetype search CSE
- document search engine
tags:
- documents
- google-cse
- filetype
- metadata
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Search by FileType

> A Google Custom Search Engine that hunts documents — surface the PDFs, spreadsheets, and Office files tied to a person or organisation, where the file's metadata often leaks more than the text.

## When to use
You want documents rather than web pages: reports, CVs, spreadsheets, presentations, or letters that mention a `name`/`employer-org`, or that were authored by them. Documents are gold for OSINT because their embedded metadata (author name, organisation, software, sometimes GPS/username) can reveal identities and links the visible content doesn't. Use this CSE as a quick filetype-scoped pass without hand-writing `filetype:` dorks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at its public URL (cx `013991603413798772546:mu-oio3a980`).
2. Search a `name`, organisation, project, or keyword; the engine scopes to document filetypes (PDF/DOC/XLS/PPT).
3. Read the results: indexed documents matching the term.
4. Download a hit and inspect its metadata (author, created-by, software, GPS) as well as its contents.
5. Pivot: document `metadata-exif` (author/username/org) is a strong new selector; file contents may leak contacts, addresses, or associates.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or keyword
- **Out:** indexed documents (`document-id`) and, once opened, their `metadata-exif`
- **Empty/negative result looks like:** no documents — nothing matching is public and indexed, or Google hasn't crawled it; try a raw `filetype:` Google dork as a cross-check.

## Gotchas & OpSec
- Finds only **public, indexed** files — combine with manual `filetype:`/`site:` dorks and document-metadata tools for depth.
- The real value is often the **metadata**, not the text — always inspect the file's properties, not just its content.
- CSEs can silently change scope or be retired; verify it's still returning document results.

## Overlaps ("do both")
- Pairs with manual Google dorking, [[cloud-bucket-search-engine]] (for files in exposed buckets), and a metadata extractor (ExifTool/FOCA-style) — this finds the documents; the extractor mines their hidden fields.

## Trust & verifiability
`trust: community` — a third-party CSE over Google's index. Each result is verifiable by opening the file, but the preset's filetype scope and upkeep depend on its maintainer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-by-filetype |
