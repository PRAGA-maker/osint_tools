---
id: hathitrust-digital-library
name: HathiTrust Digital Library
description: Use when you have a name or organization and want full-text hits inside millions of digitized books, directories, and yearbooks — returns employer-org, address, and associate leads.
url: https://www.hathitrust.org/
category: public-records
path:
- public-records
bestFor: Full-text searching digitized historical books, city directories, yearbooks, and institutional records for a person or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free full-text search and public-domain reading for anyone; some in-copyright volumes are search-only ("snippet") unless you are at a member institution.
opsec: passive
opsecNote: Public catalog and search; no login needed to search or read public-domain works. Searches are not tied to a target and no one is notified. A member-institution login is only needed for extended in-copyright access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nonprofit collaboration of major academic and research libraries (partner of Google Books, Internet Archive); the scans are authentic digitized originals.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- HathiTrust
- hathitrust.org
- Hathi Trust
tags:
- public-records
- digitized-books
- genealogy
- archives
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# HathiTrust Digital Library

> A nonprofit consortium of research libraries offering full-text search across tens of millions of digitized volumes — including the city directories, yearbooks, and institutional histories that name ordinary people.

## When to use
You have a `name` or `employer-org` and want to find them inside the printed record: an old city directory listing a `address`, a school yearbook placing them with classmates (`associate`), a company history naming staff, or an academic roster tying a person to an institution. HathiTrust's full-text index reaches inside book pages that a normal web search never touches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.hathitrust.org/ (or catalog.hathitrust.org) and choose "Full-text" search rather than catalog/title search.
2. Enter the person's name in quotes; add a place, employer, or year to cut noise (e.g. `"Jane A. Miller" Cleveland directory`).
3. Open matching volumes. Public-domain works (generally pre-1929 in the US) are fully readable; in-copyright works show only snippets around your term unless you are logged in at a member institution.
4. Read the hit in context — a directory entry gives an `address` and often an occupation/employer; a yearbook or roster gives `associate` names. Pivot those names/addresses into people-search, genealogy, or newspaper archives.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (institutional/company mentions), `address` (directory listings), `associate` (classmates, colleagues, family named in text)
- **Empty/negative result looks like:** zero full-text hits, or hits only inside in-copyright books where you see a snippet but can't read the page — the name may simply not appear in digitized print, especially for recent decades.

## Gotchas & OpSec
- Human-in-the-loop: none to search; extended reading of in-copyright volumes requires a member-institution login you may not have.
- OpSec: fully passive — no target is contacted, no account needed for public-domain material.
- Recency gap: coverage is strongest for older material. Common names need a disambiguating place/date, and OCR errors mean you should try spelling variants.

## Overlaps ("do both")
- Pairs with genealogy tools like `[[familysearch]]` and newspaper archives — HathiTrust surfaces the directory/yearbook mention, and a genealogy or newspaper source then anchors the person to dates, relatives, and events.

## Trust & verifiability
`trust: trusted` — HathiTrust is a well-governed library consortium and the results are page-images of real published sources you can read and cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hathitrust-digital-library |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
