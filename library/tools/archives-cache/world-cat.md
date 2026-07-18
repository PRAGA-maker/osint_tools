---
id: world-cat
name: WorldCat
description: Use when you have a book/publication title or author `name` and want to locate it — returns which libraries hold it and full bibliographic details.
url: https://worldcat.org/
category: archives-cache
path:
- archives-cache
bestFor: Finding which libraries hold a specific book/publication, and confirming an author's published works and editions.
selectorsIn:
- name
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public catalog search operated by OCLC; no account required.
opsec: passive
opsecNote: You search a global library catalog — no subject is contacted and nothing is signalled. Purely bibliographic.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by OCLC, the global library cooperative; authoritative bibliographic and holdings data aggregated from member libraries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- WorldCat
- worldcat.org
- OCLC WorldCat
tags:
- library
- books
- bibliographic
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# WorldCat

> The global union library catalog — find who has a book and where, and confirm an author's published output, editions, and the libraries (and thus places) that hold their work.

## When to use
A niche resource: you have a book/publication title or an author `name` and want to (a) locate a physical copy — which libraries hold it and where — or (b) confirm a person's authorship, editions, and publication history. Handy when a subject has written or is credited on a publication, when you're chasing a rare document, or when a book's holding library narrows a `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://worldcat.org/ and search by title, author `name`, or ISBN.
2. Open the record: full bibliographic details (author, publisher, year, editions, subjects).
3. Use "Find in a library" to see holding libraries near a location (`geolocation`), across the US, Australia, and much of Europe.
4. Pivot: confirmed authorship corroborates a professional identity; a holding library gives a place to request/inspect the physical item; editions/dates anchor a timeline.

## Inputs → Outputs
- **In:** book/publication title, ISBN, or author `name`
- **Out:** bibliographic record, editions, and holding libraries (`employer-org`/`geolocation`)
- **Empty/negative result looks like:** no record — the item isn't cataloged by an OCLC member library (self-published/very obscure/non-Western works may be absent); not proof it doesn't exist.

## Gotchas & OpSec
- It's a **library catalog**, not a full-text or people database — it locates and describes works, it won't give you the contents or the author's contact details.
- Holdings coverage is strongest in the US/Europe/Australia and thinner elsewhere.
- OpSec: fully passive — bibliographic lookup.

## Overlaps ("do both")
- Pairs with Google Books, national library catalogs, and academic indexes ([[bielefeld-academic-search-engine]]) — WorldCat is best for physical holdings/editions; the others give full text or scholarly context.

## Trust & verifiability
`trust: trusted` — OCLC's authoritative union catalog. Bibliographic and holdings data are reliable; the only limit is coverage of obscure/self-published or non-member-library items.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-cat |
