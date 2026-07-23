---
id: awesome-public-datasets
name: Awesome Public Datasets
description: Use when you need a free public dataset on a topic (government, geography, health, social, finance) and want a curated index of where to get it — a jumping-off catalogue, not a person-lookup.
url: https://github.com/awesomedata/awesome-public-datasets
category: search-engines
path:
- search-engines
bestFor: A curated, topic-organised index of high-quality free public datasets to source from.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open (MIT); a GitHub markdown list. The linked datasets have their own varied licences/costs.
opsec: passive
opsecNote: Browsing the list on GitHub reveals nothing about a target. Each dataset you then visit is a separate site with its own logging — apply normal sock-puppet hygiene when you follow a link.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-maintained community catalogue (70k+ stars); it's an index of pointers, so quality/freshness depends on each linked dataset, and some links go stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- awesomedata/awesome-public-datasets
tags:
- open-data
- datasets
- directory
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Awesome Public Datasets

> A curated map of where the free data lives: hundreds of open datasets sorted by topic, so you find a source instead of guessing.

## When to use
You need structured data on a subject area — geography, government, healthcare, social, economics/finance, transport, climate — and want a vetted starting index rather than blind searching. Awesome Public Datasets is a topic-organised catalogue of high-quality open datasets, useful for finding the authoritative source behind a research question or for background/context data in an investigation. It's a directory of pointers, not a tool that answers a query about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/awesomedata/awesome-public-datasets.
2. Use the topic table of contents to jump to your domain (e.g. GIS, Government, Healthcare, Social Networks).
3. Follow a listed dataset link to its host, and read that source's coverage, format, and licence.
4. Download/query the data at the source; the list itself only points you there.
5. Pivot: combine a sourced dataset with your case data — e.g. join a public geographic/economic dataset against locations or organisations you're tracking.

## Inputs → Outputs
- **In:** a topic/domain of interest (no person selector)
- **Out:** links to curated open datasets in that domain (each with its own access terms)
- **Empty/negative result looks like:** no listing for your niche, or a dead link — the catalogue is broad but not exhaustive and some entries go stale; fall back to a dataset search engine or the publisher directly.

## Gotchas & OpSec
- It's an index, not the data — every real source is one hop away with its own licence, freshness, and quality.
- Community-maintained, so some links rot; verify the target still hosts the dataset.
- Not a person-lookup — use it for aggregate/context data, not to identify individuals.
- OpSec: passive; following a link is a normal site visit — apply sock-puppet hygiene.

## Overlaps ("do both")
- Complements government open-data portals like `[[data-gov-uk]]` — the awesome list points you across many national/thematic sources, while a portal like data.gov.uk is the deep source within one jurisdiction.

## Trust & verifiability
`trust: community` — a large, long-standing curated catalogue; because it only links out, trust each dataset at its own source, and expect occasional stale entries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-public-datasets |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
