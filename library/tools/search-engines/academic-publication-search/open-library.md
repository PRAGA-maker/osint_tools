---
id: open-library
name: Open Library
description: Use when you have an author `name`, title, or ISBN and want book records — returns editions, publication metadata, and links to readable/borrowable copies.
url: https://openlibrary.org/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Finding a person's published books and pulling bibliographic metadata, including out-of-print and historical titles.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open (an Internet Archive project); searching and metadata need no account, borrowing scanned books needs a free Archive login.
opsec: passive
opsecNote: Passive — public catalog search needs no account and notifies no one. Borrowing a scanned book requires an Internet Archive login, which logs your activity to that account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Internet Archive; bibliographic records are community- and library-sourced (some crowd-edited), so metadata is broad and generally reliable but not uniformly authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- semantic-scholar
- google-scholar-case-law
aliases:
- openlibrary.org
- Open Library Internet Archive
tags:
- books
- bibliographic
- internet-archive
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Open Library

> The Internet Archive's open book catalog — search a person's published works and pull bibliographic metadata, with many titles readable or borrowable online.

## When to use
You have an author `name` (or a title/ISBN) and want to find the books a person published, or verify a bibliographic claim. For an investigation this matters when a subject is an author, academic, or self-publisher: their catalog of works, publication dates, publishers, and any biographical blurb become corroborating identity data. It also covers out-of-print and historical books that mainstream search misses, and exposes a free API for programmatic lookups.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://openlibrary.org/ and search by author `name`, title, subject, or ISBN.
2. Open the author page to see their listed works, or the work/edition page for publication details.
3. Read the metadata: editions, publishers, dates, identifiers (ISBN/OCLC/LCCN), and cover images.
4. For scanned/borrowable copies, sign in with a free Internet Archive account to read.
5. Pivot: publication dates/publishers corroborate a timeline; author identifiers link to WorldCat/library records; for automation use the JSON API (`/search.json`, `/isbn/…json`).

## Inputs → Outputs
- **In:** author `name` (or title/ISBN)
- **Out:** book/edition records with publication metadata and identifiers (`document-id`: ISBN/OCLC/LCCN), plus author pages
- **Empty/negative result looks like:** "No results" or a bare author page with no works — the person may not have catalogued books, or their name is spelled/transliterated differently; absence is not proof they never published.

## Gotchas & OpSec
- Records are partly crowd-edited — expect duplicate editions, merged/split author records, and occasional metadata errors; verify against a library catalog for anything critical.
- Author-name disambiguation is weak; common names merge multiple people, so confirm it's your subject via dates/subjects.
- Borrowing (not searching) requires login and logs activity to your Archive account.

## Overlaps ("do both")
- Pairs with `[[semantic-scholar]]` (academic papers and author profiles) — use Open Library for books and Semantic Scholar for scholarly publications when profiling an author's full body of work.

## Trust & verifiability
`trust: trusted` — an Internet Archive project with library-sourced data; reliable for discovery, but crowd-edits mean individual records should be cross-checked against an authoritative catalog before being treated as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-library |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
