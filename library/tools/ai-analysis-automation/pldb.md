---
id: pldb
name: PLDB
description: Use when you have a programming-language name or artifact and want authoritative background on that language (origin, ranking, features, references) — returns encyclopedic language facts.
url: https://pldb.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Identifying and researching a programming/computing language spotted in a subject's code, repos, or files.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-data project; the entire database is public-domain and downloadable. No account.
opsec: passive
opsecNote: A public reference site — you look up a language name, not a person. Nothing about your subject is submitted, so browsing is fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained open knowledge base (formerly TrueBase / the Programming Language Database) with public edit history; a reference, not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Programming Language Database
- pldb.com
- TrueBase
tags:
- Code
- reference
- ai-analysis-automation
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# PLDB

> A free, downloadable encyclopedia of 5,000+ programming and computing languages — rankings, creation history, linguistic features, and reading lists for each.

## When to use
This is a **reference/context** tool, not a people-search tool. In an investigation it helps only indirectly: you've found code, a repo, a config file, or a file extension in a subject's digital footprint and need to identify or understand the language/technology — its era, ecosystem, typical users, and canonical resources. That can date an artifact ("this language peaked in the 90s") or narrow a community. It never takes a person selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pldb.com/ and search or browse for the language name (or extension/keyword).
2. Read the language page: rank, estimated users/repos, year created, features, and lists of books/articles.
3. Use the ranking and creation-history to place an artifact in time or scene.
4. For bulk/programmatic work, download the full public-domain dataset from the site rather than scraping.

## Inputs → Outputs
- **In:** none of the person selectors — a language name / extension / keyword
- **Out:** encyclopedic facts about the language (no person data)
- **Empty/negative result looks like:** the language isn't catalogued (obscure/private DSLs may be missing) — absence here doesn't mean the technology isn't real.

## Gotchas & OpSec
- **Marginal to missing-persons OSINT** — it enriches *technical artifacts*, not identities. Keep expectations low; it's a supporting reference.
- Community-edited, so treat individual data points (user counts, rankings) as estimates.
- OpSec: **passive** — no subject data leaves your browser.

## Overlaps ("do both")
- Stands alone as a reference; pair it with your normal code/repo analysis (e.g. reviewing a subject's public GitHub) — PLDB explains *what* a language is once your other tooling has surfaced *that* the subject used it.

## Trust & verifiability
`trust: community` — an open, transparently-edited knowledge base with downloadable source data; verifiable in the sense that the data is public, but it's a crowd reference, not an official standard.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pldb |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
