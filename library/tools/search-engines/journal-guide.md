---
id: journal-guide
name: JournalGuide
description: Use when you have a journal name/paper topic and want to identify or compare scholarly journals — returns journal profiles and matches (a reference tool, not people search).
url: https://www.journalguide.com
category: search-engines
path:
- search-engines
bestFor: Identifying and comparing academic journals by name, publisher, or by matching a paper's title/abstract.
selectorsIn:
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Completely free; no account required to search and compare.
opsec: passive
opsecNote: You look up journals, not people — no subject selector is submitted, so browsing is fully passive and leaks nothing about your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free journal-evaluation tool (from Research Square/Editage ecosystem) aggregating journal metadata; reputable for discovery, not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- journal-seek
aliases:
- JournalGuide
- journalguide.com
tags:
- academic-resources-and-grey-literature
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# JournalGuide

> A free journal-discovery and comparison tool — identify a scholarly journal by name, publisher, or by pasting a paper's title/abstract, and compare candidates side by side.

## When to use
A **reference/disambiguation** aid for academic footprints, not a people-search tool. When a subject's trail runs through scholarly publishing — a CV citing a journal, an ambiguous abbreviation, a paper you're trying to place — JournalGuide resolves and profiles the journal (scope, publisher, metrics, homepage). Its distinctive feature is *content matching*: paste a title/abstract and it suggests journals that publish similar work, which can help locate where a person's research actually appeared.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.journalguide.com.
2. Search by journal `name`, category, or publisher — or paste a paper title + abstract to find matching journals.
3. Open a journal profile: scope, publisher, metrics, and the journal `domain`/homepage.
4. Sort/filter/compare candidates to identify the most likely venue.
5. Pivot: follow the journal homepage to issue archives / editorial boards to find the subject's paper, co-authors, and affiliation.

## Inputs → Outputs
- **In:** journal `name` / publisher / a paper's title+abstract
- **Out:** journal profiles + homepage `domain`, ranked matches
- **Empty/negative result looks like:** no strong match — the journal may be obscure, predatory, or newly renamed; corroborate with the publisher site or a citation index.

## Gotchas & OpSec
- **Discovery aid, not full text** — it identifies and compares journals; you still go to the publisher for the actual paper.
- Aggregated metadata can lag; verify current scope/status on the journal's own site.
- OpSec: **passive** — no subject data leaves your browser.

## Overlaps ("do both")
- Pairs with `[[journal-seek]]` — both resolve a journal from a name/abbreviation; JournalGuide adds abstract-based matching and comparison, JournalSeek offers a broad ISSN-searchable directory. Use whichever resolves your fragment, cross-check with the other.

## Trust & verifiability
`trust: community` — a real, free, reputable discovery tool; reliable for identifying journals, but confirm specifics on the publisher's authoritative page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | journal-guide |
| category | search-engines |
| selectorsIn → selectorsOut | name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
