---
id: datasetsearch-research-google-com
name: Google Dataset Search
description: Use when you need to find a published dataset on a topic (by keyword) across thousands of repositories — returns dataset listings with descriptions, providers and download/access links.
url: https://datasetsearch.research.google.com/
category: public-records
path:
- public-records
bestFor: Discovering openly-published datasets (government, academic, NGO) on any topic via a single search engine.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Google search service; no account required (the datasets it points to may have their own access terms).
opsec: passive
opsecNote: Passive — a search engine over dataset metadata. It indexes public dataset descriptions; downloading a dataset happens on the provider's site under their terms. No target is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google service that indexes dataset metadata published with schema.org markup; a discovery layer, so vet the underlying provider for each dataset.
missingPersonsRelevance: low
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
- Google Dataset Search
- datasetsearch.research.google.com
tags:
- datasets
- open-data
- discovery
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Google Dataset Search

> A search engine for datasets — keyword-search across thousands of government, academic and NGO data repositories to find data on any topic.

## When to use
Your investigation needs a specific kind of structured data — a registry, statistical series, geospatial layer, or research dataset — and you don't know who publishes it. Dataset Search indexes dataset metadata from across the web, so a keyword query surfaces candidate datasets with descriptions, providers, update dates and links to where you can download or access them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datasetsearch.research.google.com/.
2. Enter topic keywords (e.g. "vessel registry", "voter file", "aircraft accidents [country]").
3. Scan the results — each shows the provider, description, formats, update date, and license.
4. Use the filters (update date, download format, usage rights) to narrow.
5. Follow the link to the provider to actually obtain the data; verify the provider's authority.

## Inputs → Outputs
- **In:** topic keywords
- **Out:** dataset listings — title, provider, description, formats, license, access link
- **Empty/negative result looks like:** few/irrelevant results — the data may not be published as a discoverable dataset (try the provider's site directly, or a general search); absence here isn't proof no dataset exists.

## Gotchas & OpSec
- It's a **discovery** tool — it indexes metadata, not the data itself; access/quality depends on each provider.
- Coverage depends on publishers using schema.org dataset markup; well-formatted datasets rank; obscure ones may be missing.
- Always verify the provider's credibility before relying on a dataset.

## Overlaps ("do both")
- Pairs with data platforms like BigQuery public datasets and Kaggle — Dataset Search finds *what exists*; those host and let you *work with* many of the datasets it surfaces.

## Trust & verifiability
`trust: trusted` — a first-party Google discovery service; it points to primary providers, so confirm authority and license at each dataset's source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datasetsearch-research-google-com |
