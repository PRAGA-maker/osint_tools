---
id: crossref
name: Crossref
description: Use when you have a person's `name` (or a DOI/title) and want their scholarly publications, co-authors and affiliations — returns employer-org, associate and document-id leads.
url: https://search.crossref.org/
category: search-engines
path:
- search-engines
bestFor: Finding a person's academic/published work and the co-authors and institutions attached to it.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- associate
- document-id
status: live
pricing: free
costNote: Free metadata search and public REST API; no account required. Registration only needed for depositing DOIs (not for lookups).
opsec: passive
opsecNote: Passive lookup of a public scholarly-metadata index; the subject is never notified and nothing is logged against them. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Crossref is the official DOI registration agency for scholarly publishers; its metadata is authoritative for published works.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Crossref Metadata Search
- search.crossref.org
tags:
- academic
- publications
- scholarly
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Crossref

> The official scholarly-DOI metadata index: search by author name or DOI and get the person's publications, co-authors, and institutional affiliations.

## When to use
Your subject is (or may be) an academic, researcher, clinician, or engineer who has published. Search their `name` in Crossref to pull a list of their papers; each record's author affiliations reveal an `employer-org` / university, and co-author lists give `associate` names to pivot on. If you already have a DOI or paper title (`document-id`), Crossref confirms authorship and funding.

## How to use it (`bestInteractionPattern`: web-manual / api)
1. Open https://search.crossref.org/ and enter the person's name (optionally with a keyword from their field to disambiguate common names).
2. Scan the returned works; open records to see the full author list and affiliation strings.
3. For automation, hit the public REST API: `https://api.crossref.org/works?query.author=Jane+Smith` (add `&rows=` and filters) — returns JSON with authors, affiliations, ORCID iDs, and funders.
4. Pivot: affiliation → `employer-org` and geographic base; co-authors → `associate` names; any ORCID iD → a richer researcher profile; funder data → grants tying the person to a project.

## Inputs → Outputs
- **In:** `name`, or `document-id` (DOI / title)
- **Out:** publications, co-authors (`associate`), affiliations (`employer-org`), ORCID iDs, and canonical DOIs (`document-id`).
- **Empty/negative result looks like:** no works returned for the name — the person has no DOI-registered publications (or publishes under a different name spelling); try initials/variants before concluding.

## Gotchas & OpSec
- Common names collide badly; disambiguate with a field keyword, co-author, or ORCID iD.
- Affiliation strings reflect the institution *at time of publication*, which may be years out of date.
- Coverage is limited to DOI-registered scholarly content — preprints on some servers, theses, and grey literature may be absent.

## Overlaps ("do both")
- Pairs with an ORCID or Google Scholar lookup — Crossref gives authoritative publisher metadata, while those add self-maintained profiles and full publication lists.

## Trust & verifiability
`trust: trusted` — Crossref is the industry DOI registry; its records come directly from publishers, so authorship and affiliation metadata are authoritative (subject to the usual name-ambiguity caveats).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crossref |
| category | search-engines |
| selectorsIn → selectorsOut | name, document-id → employer-org, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
