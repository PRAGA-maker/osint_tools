---
id: sage-journals
name: SAGE Journals
description: Use when you have a `name`, topic or affiliation and want peer-reviewed literature — returns academic articles, author affiliations and citations across social/health sciences.
url: https://journals.sagepub.com
category: search-engines
path:
- search-engines
bestFor: Searching a major academic publisher's catalogue to find a person's publications, affiliations and research topics.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Free to search; abstracts and metadata are free, and some articles are open-access, but many full texts are paywalled or need an institutional subscription. The old online.sagepub.com now redirects to journals.sagepub.com.
opsec: passive
opsecNote: Passive catalogue search; you query names/topics, not a target's systems. No subject data is disclosed by searching.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by SAGE Publishing, an established academic publisher; article metadata (authors, affiliations, dates) is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SAGE Publishing
- online.sagepub.com
- journals.sagepub.com
tags:
- academic-resources-and-grey-literature
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# SAGE Journals

> A major academic publisher's searchable catalogue — for tying a `name` to publications, affiliations and research interests, not a direct people-lookup.

## When to use
Your subject is an academic, researcher, or professional who may have published, and you want to confirm their institutional `employer-org`, co-authors, and research focus over time. Author affiliations and publication dates are strong corroboration and pivot points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://journals.sagepub.com (or search the old `online.sagepub.com`, which redirects here).
2. Search the subject's `name`, optionally with an institution or topic to disambiguate.
3. Read each article's author affiliations, dates, and co-authors; note the listed `employer-org` and collaborators.
4. Pivot: cross-reference with ORCID, Google Scholar, and other publishers to build a full publication timeline; abstracts are free even when full text is paywalled.

## Inputs → Outputs
- **In:** `name` (optionally + affiliation/topic)
- **Out:** publications, author `employer-org` affiliations, co-authors, dates
- **Empty/negative result looks like:** no matching author — they may publish elsewhere or under a name variant; try other publishers and Google Scholar before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; full text may be paywalled (use the free abstract/metadata for OSINT).
- OpSec: passive; searching reveals nothing about your subject.
- Common names need disambiguation via affiliation, ORCID, and co-author overlap.

## Overlaps ("do both")
- Pairs with Google Scholar, ORCID, and other publisher databases: SAGE covers its own catalogue; combine sources to avoid missing publications in other venues.

## Trust & verifiability
`trust: trusted` — an established academic publisher; its article metadata (authors, affiliations, dates) is authoritative, subject to normal name-disambiguation care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sage-journals |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
