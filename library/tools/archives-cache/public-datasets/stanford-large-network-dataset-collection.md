---
id: stanford-large-network-dataset-collection
name: Stanford Large Network Dataset Collection
description: Use when you have a research/tooling need for graph data and want ready-made social/communication network datasets — returns downloadable graph datasets (not target PII).
url: https://snap.stanford.edu/data/
category: archives-cache
path:
- archives-cache
- public-datasets
bestFor: Sourcing real-world graph datasets to prototype and validate network-analysis and link-analysis tooling.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free academic resource; open download, no account.
opsec: passive
opsecNote: You download static, pre-published academic datasets — no query touches an investigation target. Purely a methodology/tooling resource.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Stanford's SNAP group (Jure Leskovec's lab); datasets are curated, documented and widely cited in academic literature.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- palladio
- swap-stanford-edu
- highwire-free-online-full-text-articles
- regular-expression-analyzer
aliases:
- SNAP datasets
- snap.stanford.edu/data
tags:
- datasets
- graph-analysis
- academic
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Stanford Large Network Dataset Collection

> The SNAP dataset library — 200+ curated real-world network graphs (social, communication, citation, web) for building and testing link-analysis tooling, not for looking up a specific person.

## When to use
You are building or validating a network/link-analysis workflow — community detection, ego-network extraction, centrality scoring — and need real graph data to develop against before pointing your tooling at a live investigation graph. This is a **methodology and test-data** resource; it will not tell you anything about a named subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://snap.stanford.edu/data/ and browse by category (social networks, communication/email, citation, collaboration, web graphs, temporal, signed, etc.).
2. Pick a dataset (e.g. `ego-Facebook`, `email-Enron`, `wiki-Talk`) and open its page for format docs, node/edge counts, and citation.
3. Download the edge-list/graph file (typically gzipped text) and load it into your analysis stack (NetworkX, igraph, Gephi, or `[[palladio]]`).
4. Pivot: use the dataset to calibrate an algorithm, then apply the *validated* method to your own case graph.

## Inputs → Outputs
- **In:** a dataset selection (no selector from a target)
- **Out:** downloadable graph datasets + documentation (edge lists, metadata) — no target `selectorsOut`
- **Empty/negative result looks like:** a dataset page 404 or a download link that has been retired; SNAP mirrors most sets on the SuiteSparse Matrix Collection if a direct link is stale.

## Gotchas & OpSec
- These are **historical snapshots** (some over a decade old) — never present SNAP data as current facts about anyone; it is training/test data.
- No human-in-the-loop, no account, fully passive.
- Category-tagged as `documents-metadata`-adjacent test data; keep it out of case findings.

## Overlaps ("do both")
- Pairs with `[[palladio]]` for actually visualizing/analyzing the graphs, and with `[[swap-stanford-edu]]` as a sibling Stanford academic-data resource.

## Trust & verifiability
`trust: trusted` — it is Stanford's SNAP group's official, heavily-cited dataset collection, so provenance and documentation are authoritative for a research/tooling use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stanford-large-network-dataset-collection |
| category | archives-cache |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
