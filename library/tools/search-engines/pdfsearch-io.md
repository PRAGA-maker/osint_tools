---
id: pdfsearch-io
name: Pdfsearch.io
description: Use when you have a `name`/keyword and want it inside PDF documents/books — returns matching PDFs with author/year metadata and download links.
url: https://www.pdfsearch.io/
category: search-engines
path:
- search-engines
bestFor: Full-text and semantic search across a large index of PDF documents and books.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free searching; some features/volume may sit behind an account or paid tier.
opsec: passive
opsecNote: "Searching queries pdfsearch.io's own document index, so you don't touch any subject — passive. Your searches are logged by the site; use a sock-puppet session. Downloading a result fetches it from wherever it's hosted, and be mindful that some indexed PDFs may be copyrighted."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party PDF search engine indexing millions of documents with metadata and semantic search; coverage and freshness are unverified, so treat it as one corpus among several.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PDFSearch.io
- pdfsearch
tags:
- document-search
- pdf
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Pdfsearch.io

> A dedicated search engine over millions of indexed PDF documents and books — full-text and semantic search with author/year metadata, for finding a name or phrase buried inside documents.

## When to use
You want to find a `name`, phrase, or topic *inside* PDF documents — reports, academic papers, books, leaked/published files — rather than on web pages. Useful when a general engine buries PDFs or when you want to search by document metadata (author, publication year). A document-corpus search, so low direct missing-persons relevance, though a name appearing in a report/roster can be a lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pdfsearch.io/ and search a `name`, exact phrase (quoted), or topic.
2. Refine with metadata filters (author, year) and smart labels/categories.
3. Read results: matching PDFs with title, source, and snippet; open or download to read in context (`document-id` = the document).
4. Verify a hit by opening the actual PDF — confirm the name/phrase truly appears and note the source's credibility.
5. Pivot names/orgs/dates found inside a document into people/records searches.

## Inputs → Outputs
- **In:** `name`/keyword/phrase (optionally author/year)
- **Out:** matching PDF documents with metadata (`document-id`), snippets, links
- **Empty/negative result looks like:** no matches — the term isn't in pdfsearch.io's index (which is a subset of all PDFs online); a blank here doesn't mean no PDF mentions it, so also try Google `filetype:pdf`.

## Gotchas & OpSec
- Coverage is a partial index; complement with `filetype:pdf` on general engines rather than relying on it alone.
- Indexed PDFs may be copyrighted or low-provenance — assess the source before trusting content.
- Semantic search can return topically-related but non-matching docs; confirm the literal term is present.

## Overlaps ("do both")
- Complements general search with `filetype:pdf` operators and document-metadata tools like [[metafinder]] — pdfsearch.io searches inside documents broadly, `filetype:pdf` scopes to a site, MetaFinder harvests a specific domain's files.

## Trust & verifiability
`trust: community` — a useful but unverified third-party index; always open the actual PDF to confirm the match and judge the source, since neither coverage nor document provenance is guaranteed.
