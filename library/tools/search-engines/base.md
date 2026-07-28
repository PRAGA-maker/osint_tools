---
id: base
name: BASE (Bielefeld Academic Search Engine)
description: Use when you have a `name` (or topic) and want scholarly publications and grey literature by or about a person — returns academic documents revealing `employer-org` and `associate` (co-author) links.
url: https://www.base-search.net
category: search-engines
path:
- search-engines
bestFor: Searching hundreds of millions of scholarly documents (incl. repository/grey literature) by author name or topic.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free, no login; operated by Bielefeld University Library.
opsec: passive
opsecNote: A standard academic search — queries are logged by BASE and tied to your IP, but nothing touches the subject. Use a clean session for sensitive names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Bielefeld University Library; one of the largest academic search engines, indexing open repositories worldwide, so results are authoritative scholarly metadata.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- base-academic-search-engine
- bielefeld-academic-search-engine
aliases:
- BASE
- Bielefeld Academic Search Engine
- base-search.net
tags:
- academic-resources-and-grey-literature
- academic
- scholarly
- publications
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# BASE (Bielefeld Academic Search Engine)

> One of the largest scholarly search engines — index a person's publications, theses, and grey literature to reveal their field, institution, and collaborators.

## When to use
Your subject is (or may be) an academic, researcher, student, or professional who has published — and you want their scholarly footprint. Searching a `name` in BASE surfaces papers, preprints, theses, and repository documents that expose their institutional affiliation (`employer-org`), co-authors (`associate`), research topics, and often a timeline of where they were and when. Especially useful for grey literature that Google Scholar under-indexes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.base-search.net.
2. Search the subject's `name` (quote it: `"Jane A. Doe"`); use the author/advanced filters to narrow by author field, year, or document type.
3. Scan results for their publications; open records for affiliation, co-authors, dates, and links to full text in the hosting repository.
4. Use filters (repository, year, language) to disambiguate common names.
5. Pivot: an affiliation feeds `employer-org` searches; co-authors are `associate` leads; a hosting repository or ORCID link feeds further identity resolution.

## Inputs → Outputs
- **In:** `name` (or research topic)
- **Out:** scholarly documents → `employer-org` (affiliation), `associate` (co-authors), topics, dates, full-text links
- **Empty/negative result looks like:** no publications for the name — the subject likely hasn't published, or publishes under a different name/initials; try name variants before concluding.

## Gotchas & OpSec
- Common names collide — always corroborate with affiliation, field, or co-authors before attributing a paper to your subject.
- Coverage is broad but not total; cross-check with Google Scholar, ORCID, and institutional pages.
- OpSec: passive; a normal search logged by BASE, nothing reaches the subject.

## Overlaps ("do both")
- Pair with Google Scholar and ORCID — BASE is strongest on repository/grey literature; the others fill in citations and author identifiers. Same-provider siblings: [[base-academic-search-engine]], [[bielefeld-academic-search-engine]].

## Trust & verifiability
`trust: trusted` — a university-library-operated academic index; the metadata is authoritative, though name disambiguation is on you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | base |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
