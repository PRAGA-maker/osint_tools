---
id: anna-s-archive
name: Anna's Archive
description: Use when you have a `name` (author) or title/ISBN/DOI and want to find their published books/papers — returns publication metadata and `document-id` records.
url: https://annas-archive.org/
category: archives-cache
path:
- archives-cache
- web
bestFor: Discovering and confirming a person's published books, papers and their bibliographic metadata across many shadow-library sources at once.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search; no account needed for search. Optional paid membership speeds up downloads (not required to see records/metadata).
opsec: passive
opsecNote: Searching the index for titles/authors is a low-risk metadata lookup and contacts no subject. DOWNLOADING copyrighted works from shadow-library mirrors carries legal risk in many jurisdictions — for OSINT you usually only need the bibliographic record, so stop at metadata unless you have a lawful basis to retrieve a file.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known aggregator indexing multiple shadow libraries (Library Genesis, Sci-Hub, Z-Library, etc.); the bibliographic metadata is generally accurate, but sources are unofficial.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- annas-archive.org
- Anna Archive
tags:
- archive
- shadow-library
- publications
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Anna's Archive

> A search engine over multiple shadow libraries (LibGen, Sci-Hub, Z-Library and more) — most useful in OSINT as a fast way to confirm what a person has *published* and pull the bibliographic metadata, without touching any one library.

## When to use
You have an author `name`, or a title/ISBN/DOI, and want to establish a subject's published output — books, academic papers, theses — and the metadata around them (co-authors, publisher, year, affiliations printed in the work). This corroborates a claimed profession or academic history, surfaces co-authors as `associate` leads, and can attribute a document to a person. Treat it primarily as a **discovery/metadata** tool; the actual file download is a separate, legally-loaded step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://annas-archive.org/ and search by author `name`, title, ISBN or DOI.
2. Read the result records: title, author(s), publisher, year, language, identifiers (`document-id`: ISBN/DOI/OCLC) — this is the OSINT payload.
3. Use the metadata to confirm the publication exists and note co-authors/affiliations for pivots.
4. Stop at the record unless you have a lawful reason to download the file — downloading copyrighted content from mirrors carries legal risk.
5. Pivot: take co-author `name`s into scholar/people search; take a DOI to the publisher's official page or an open-access copy.

## Inputs → Outputs
- **In:** `name` (author) or title/ISBN/DOI
- **Out:** publication metadata and `document-id`s (ISBN/DOI/etc.), co-author names, publisher/year
- **Empty/negative result looks like:** no records — the person hasn't published (or not in indexed libraries), or the name/identifier is off. Absence isn't proof of no publications; check ORCID/Google Scholar too.

## Gotchas & OpSec
- Human-in-the-loop: **legal-gate** — searching metadata is low risk, but retrieving files infringes copyright in many places. Keep to metadata unless lawfully entitled.
- OpSec: **passive** for search; the subject is never contacted.
- Mirrors and domains shift; the metadata is the durable value, not any particular download link.

## Overlaps ("do both")
- Pairs with Google Scholar, ORCID and WorldCat — those are lawful, authoritative sources for the same bibliographic pivots; use them to confirm and to obtain content legally.

## Trust & verifiability
`trust: community` — a reliable aggregator of publication metadata sourced from unofficial libraries; confirm any decisive bibliographic fact against the publisher, DOI, or a library catalogue.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anna-s-archive |
| category | archives-cache |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
