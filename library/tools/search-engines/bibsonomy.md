---
id: bibsonomy
name: Bibsonomy
description: Use when you have a `name` (an academic author) or a research topic and want their publications and social bookmarks — returns publication records, author pages, and shared bookmark tags.
url: http://www.bibsonomy.org
category: search-engines
path:
- search-engines
bestFor: Finding an academic author's papers and the tags/bookmarks scholars have shared about a topic.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to search and browse; a free account is only needed to save your own bookmarks and publications.
opsec: passive
opsecNote: Searching and reading public bibliographic records is passive and does not notify any subject. Only create/register an account if you actually want to store bookmarks; browsing needs no login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running academic social-bookmarking system run by a German university research group (Kassel/Würzburg); records are user-contributed, so completeness varies by field.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BibSonomy
- blue social bookmark
tags:
- academic-resources-and-grey-literature
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Bibsonomy

> A scholarly social-bookmarking and publication-sharing system — "the blue social bookmark" — useful for tying an academic name to their body of work.

## When to use
You have a subject who is (or claims to be) an academic, researcher, or author, and you want to confirm or map their published output, co-authors, and research interests. Given a `name`, BibSonomy can surface publication records and the tag clusters other users have attached, which corroborates an affiliation (`employer-org`) or an area of expertise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.bibsonomy.org and use the search box for the author `name` or a distinctive topic phrase.
2. Filter between "publications" and "bookmarks" — publications are formal bibliographic entries; bookmarks are links users saved.
3. Open an author/user page to see their saved items, tags, and any listed affiliation.
4. Pivot: a paper's co-author list and institution feed `[[thepaperboy]]`-style local-press checks, university directory lookups, or an ORCID/Google Scholar cross-check.

## Inputs → Outputs
- **In:** `name` (author) or a topic keyword
- **Out:** publication records, `social-profile` (BibSonomy user pages), `employer-org` (institutional affiliation hints)
- **Empty/negative result looks like:** no matching author or an empty result set — common for non-academics or fields poorly covered by the community; absence here is not evidence the person has no publications.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; a CAPTCHA-free free account is only needed to save items.
- OpSec: passive — you are reading a public catalog. It also exposes a REST API if you want to script queries.
- Coverage is community-contributed and skews toward computer science and European institutions; treat a miss as "not in this corpus," not "does not exist."

## Overlaps ("do both")
- Pairs with broader academic/grey-literature search — BibSonomy adds the social-bookmark layer (what other researchers flagged) that a plain publisher search misses.

## Trust & verifiability
`trust: community` — maintained by a university research group and long-lived, but the underlying records are user-submitted, so verify any single record against the primary source (DOI, publisher).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bibsonomy |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
