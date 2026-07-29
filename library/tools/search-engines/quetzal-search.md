---
id: quetzal-search
name: Quetzal Search
description: Use when you have a `name` or research topic and want biomedical literature — returns relevant PubMed/MEDLINE articles via natural-language and semantic search.
url: https://www.quetzal-search.info
category: search-engines
path:
- search-engines
bestFor: Semantic/natural-language search of biomedical literature (PubMed and related sources) with a free tier.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: freemium
costNote: Freemium — a free Basic tier searches PubMed; Professional ($9.90/mo) and Advanced ($99/mo) add NIH grants, patents, TOXLINE, and full-text search.
opsec: passive
opsecNote: An ordinary literature-search service — you query Quertle's index, not any individual. Standard account/session logging applies on paid tiers; nothing about a searched author is disclosed to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Quertle LLC over National Library of Medicine data (PubMed/MEDLINE); an established biomedical discovery platform. Authoritative source data; ranking is proprietary.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- pubmed
- google-scholar
- semantic-scholar
aliases:
- Quetzal
- Quertle
tags:
- academic-search
- biomedical
- literature
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Quetzal Search

> A semantic biomedical-literature search over PubMed/MEDLINE — natural-language and "Power Term" queries that surface relevant papers, with a free PubMed tier.

## When to use
Narrow but real for investigations touching medicine or research: when you want to find biomedical publications by or about a `name` (e.g. establishing an academic/clinical footprint, connecting a person to research, or background on a medical topic). Its semantic ranking and entity classes ($Diseases, $Proteins, etc.) can surface relevant papers a keyword search in raw PubMed misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.quetzal-search.info (free Basic tier covers PubMed).
2. Enter a natural-language query or use Power Terms; to profile a person, search their `name` as author plus a field/affiliation term.
3. Review the ranked results — articles with save/annotate/PDF/alert options.
4. For grants, patents, TOXLINE, or full text, use the paid Professional/Advanced tiers.
5. Pivot: an author's papers give co-authors (`associate`), affiliations (`employer-org`), and topics to feed people/org searches.

## Inputs → Outputs
- **In:** `name` (as author) or research topic
- **Out:** relevant biomedical articles (titles, authors, affiliations, abstracts) — a literature set, not personal-data selectors directly
- **Empty/negative result looks like:** no relevant papers — the person has no biomedical publication record, or the topic is outside PubMed's scope; try a general scholarly index.

## Gotchas & OpSec
- Domain-specific: biomedical literature only. For non-medical fields use a general scholarly search.
- Free tier is PubMed-only; grants/patents/full-text need a paid plan.
- Author name disambiguation is hard — confirm affiliations/co-authors before attributing papers to your subject.

## Overlaps ("do both")
- Pairs with `[[pubmed]]` (the authoritative source it draws from) and general indexes `[[google-scholar]]` / `[[semantic-scholar]]`. Do both: Quetzal for semantic biomedical ranking, the general indexes for non-medical or broader coverage.

## Trust & verifiability
`trust: trusted` — built on authoritative NLM data by an established vendor. Source records are reliable; the semantic ranking is proprietary, so verify author attribution via affiliations and co-authors.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quetzal-search |
