---
id: google-com-82
name: google.com (Dataset Search)
description: Use when you have a `name` or topic and want to find published datasets that may list people — Google Dataset Search indexes datasets across the web, returning their sources and access links.
url: https://toolbox.google.com/datasetsearch
category: search-engines
path:
- search-engines
bestFor: Discovering public datasets (voter files, salary tables, membership lists, research data) that may contain a subject.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free Google service; no account. Datasets it links to may have their own access terms or paywalls.
opsec: passive
opsecNote: Searching for datasets queries Google, not the subject — passive. Downloading a dataset from its host is a separate action against that host; use a clean/sock-puppet browser for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's own dataset-discovery index (now at datasetsearch.research.google.com) — authoritative as a finder; the datasets themselves come from third parties and vary in quality/legality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Dataset Search
- datasetsearch
tags:
- searchengines
- Search Engines
- datasets
- google
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com (Dataset Search)

> Google Dataset Search — a search engine over the web's *datasets*. Where regular search finds pages, this finds the structured data files (CSV/tables/records) that may actually list your subject.

## When to use
You have a `name`, an organization, or a topic and suspect the person appears in a published dataset — a voter file, a public-salary table, a membership roster, a leaked/aggregated list, or research data. Dataset Search surfaces these where they're indexed with metadata, pointing you to sources that page-based search buries. Treat it as a discovery layer for *where the tabular data lives*, then go to the dataset itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open Google Dataset Search (the `toolbox.google.com/datasetsearch` link redirects to `datasetsearch.research.google.com`).
2. Query by topic + qualifier — e.g. `"[state] voter registration"`, `"[university] employee salaries"`, `"[org] membership list"`.
3. Review the results: each entry shows the dataset's title, publisher, description, formats and a link to its host.
4. Open the host to access the data, then search it for the subject. Pivot: a matching record yields `name`/attributes; the publisher/source feeds provenance checks.

## Inputs → Outputs
- **In:** `name` / organization / topic (as dataset search terms)
- **Out:** dataset listings and their host links → records containing `name`/`social-profile` once you open the dataset
- **Empty/negative result looks like:** no indexed datasets for the terms — meaning nothing is published with discoverable metadata, not that no relevant data exists. Rephrase around the *dataset* topic (jurisdiction, org, year), not the person's name alone.

## Gotchas & OpSec
- **Finds datasets, not people:** it returns data *sources*; you still have to open and search each dataset for the subject.
- Indexing depends on publishers adding dataset metadata — much public data (and most raw leaks) isn't here.
- Linked datasets carry their own terms, licenses and legality — vet before use.
- OpSec: the search is passive; downloading from a host is a separate, host-visible action.

## Overlaps ("do both")
- Pairs with `site:`/filetype dorks (`filetype:csv "name"`), OCCRP Aleph, and dedicated voter/records databases — dorks catch un-indexed files, Aleph indexes leak/investigation datasets, and this covers formally published, metadata-tagged datasets.

## Trust & verifiability
`trust: trusted` — Google's authoritative dataset index. The finder is reliable; each dataset's accuracy and lawful use must be judged from its publisher and license.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-82 |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
