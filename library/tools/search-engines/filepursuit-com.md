---
id: filepursuit-com
name: Filepursuit.com
description: Use when you have a `name`/keyword and want files exposed in open directories — returns direct download links to documents, video, audio, and images across the web.
url: https://filepursuit.com/
category: search-engines
path:
- search-engines
bestFor: Searching open/indexed web directories for files (docs, media, archives) by keyword or type.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free web search; a paid tier/API and mobile app add higher limits and features.
opsec: passive
opsecNote: "Searching FilePursuit queries its own index of already-open directories, so you don't probe any target server — passive. Downloading a listed file fetches it from its host, which logs your IP; use a proxy/sock-puppet for sensitive files, and be aware some indexed files may be copyrighted or sensitive."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running file/open-directory search engine; it indexes publicly-exposed directory listings, so results are real but their provenance and legality vary file to file.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- FilePursuit
- filepursuit.com
tags:
- file-search
- open-directories
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Filepursuit.com

> A search engine for files sitting in open web directories — enter a name or keyword and get direct links to documents, videos, audio, images, and archives the rest of the web has left exposed.

## When to use
You want a `name`, phrase, or filename that might appear in a *file* (a leaked document, a media clip, a dataset) rather than on a normal web page, and you specifically want to reach open-directory listings that general search engines under-index. Useful for surfacing exposed documents tied to a subject/org. A file-discovery engine, so low direct missing-persons relevance, though an exposed roster/document can be a strong lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://filepursuit.com/ and search a `name`/keyword.
2. Filter by file type (documents, video, audio, images, e-books, archives) and by extension.
3. Read results: direct links to files in open directories, with size/host (`document-id` = the file).
4. Before downloading, note it fetches from the host directly (logged) — proxy for sensitive files, and assess copyright/sensitivity.
5. Pivot: names, metadata, or references inside a discovered file feed the rest of the investigation.

## Inputs → Outputs
- **In:** `name`/keyword (+ file-type filter)
- **Out:** direct links to files in open directories (`document-id`)
- **Empty/negative result looks like:** no results — nothing matching is in an open directory FilePursuit has indexed; try alternate terms or Google `intitle:"index of"` dorks. Absence isn't proof no file exists.

## Gotchas & OpSec
- It indexes *open directories* — coverage is a slice of the web, so complement with `intitle:"index of"` search-engine dorks.
- Listed files can be copyrighted, malicious, or sensitive — assess before downloading, and scan anything executable.
- Links can rot as hosts remove/secure directories; a dead link isn't a finding.

## Overlaps ("do both")
- Complements dorking and document search like [[pdfsearch-io]] and [[metafinder]] — FilePursuit finds files in open directories, pdfsearch searches inside PDFs, MetaFinder harvests a specific domain's documents. Use together for full file coverage.

## Trust & verifiability
`trust: community` — a real, established index of open directories; results are genuine exposed files, but provenance varies, so verify what a file actually is (and its legitimacy) before relying on it.
