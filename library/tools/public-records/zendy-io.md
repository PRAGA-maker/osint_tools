---
id: zendy-io
name: Zendy
description: Use when you have a researcher's `name` (or a topic) and want their academic publications, affiliations and co-authors across many publishers — returns `employer-org`, `associate`.
url: https://zendy.io
category: public-records
path:
- public-records
bestFor: Searching a broad academic library (open-access + paywalled journals, articles, books) to find a person's publications and affiliation.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free tier (sign-up) gives search and open-access reading; Zendy Plus (paid) unlocks paywalled full text and AI features.
opsec: passive
opsecNote: An academic-literature search discloses nothing to the subject. A free account is needed for full access — register with a sock-puppet identity, not your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial research-library aggregator; publication metadata (authors, affiliations, dates) comes from the underlying publishers and is generally reliable, but Zendy is an intermediary, not the primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- semantic-scholar
- base-academic-search-engine
- public-library-of-science-search
aliases:
- zendy.io
- Zendy library
tags:
- public-records
- academic
- scholarly-search
- literature
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Zendy

> A one-stop academic library — search across many publishers' journals, articles and books to turn a researcher's name into their publications, affiliation and collaborators.

## When to use
Your subject may be an academic, clinician, or researcher and you want a broad sweep across scholarly literature (not just one publisher). Zendy aggregates open-access and paywalled works and lets you search by author, title, keyword, ISBN/ISSN. An author search surfaces their papers, and each paper's metadata gives their institutional affiliation, co-authors, and publication dates — useful for placing someone at an institution over time and mapping their professional network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://zendy.io and create a free account (needed for search/reading).
2. Search the author `name` (add a field/keyword or institution to disambiguate common names).
3. Open results and read author affiliations, co-authors, and dates; open-access items are fully readable, paywalled ones show metadata/abstract.
4. Record the affiliation (`employer-org`) and co-authors (`associate`); note publication dates to build a timeline.
5. Pivot: cross-check via `[[semantic-scholar]]` / `[[base-academic-search-engine]]` for an ORCID and full history, and take affiliation/email leads into people tooling.

## Inputs → Outputs
- **In:** `name` (author) or `employer-org` / topic
- **Out:** `employer-org` (institutional affiliation), `associate` (co-authors)
- **Empty/negative result looks like:** no works for the name — meaning nothing in Zendy's index under that spelling; try variant names or a dedicated index before concluding they haven't published.

## Gotchas & OpSec
- Human-in-the-loop: a free account login is required; full text of paywalled items needs Zendy Plus (use open-access copies or another source instead of paying).
- OpSec: passive — nothing reaches the subject; just don't register with your real identity.
- Zendy is an aggregator, so coverage and metadata quality depend on its sources; affiliations are as-of-publication (a past institution on an old paper). Disambiguate common names with co-authors/field/ORCID.

## Overlaps ("do both")
- Pairs with `[[semantic-scholar]]`, `[[base-academic-search-engine]]` and `[[public-library-of-science-search]]` — run several, since each indexes a different slice; Zendy's breadth complements PLOS's authoritative full text and Semantic Scholar's ORCID/citation graph.

## Trust & verifiability
`trust: community` — a commercial library aggregator; treat the underlying publisher metadata as reliable and Zendy as a convenient front-end, verifying decisive facts against the primary publication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zendy-io |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
