---
id: rba-business-information-resources
name: RBA - Business Information Resources
description: Use when you need to find the right specialized business/company data source for a topic — returns an annotated directory of `employer-org` research databases and tools.
url: https://www.rba.co.uk/sources/
category: public-records
path:
- public-records
- additional-resources
bestFor: A curated, annotated directory pointing you to specialized business-intelligence sources by topic.
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free reference directory maintained by RBA Information Services (Karen Blakeman); no account required.
opsec: passive
opsecNote: Passive — it's a reference/link directory; you don't submit any target data to it, and there's no interaction with a subject. Clicking through to the linked sources is where actual lookups (and their own logging) happen.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, well-regarded curated resource list from an independent UK information professional; a signpost to other tools rather than a data source itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RBA Information Services sources
- rba.co.uk sources
tags:
- reference-directory
- business-intelligence
- meta-resource
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# RBA - Business Information Resources

> A curated, annotated directory of business-intelligence sources — a "where do I look?" index that points you to the right specialized company/business database for a topic.

## When to use
Not a lookup tool but a meta-resource: when you're researching a company/`employer-org` or a business topic and don't know which specialized database, registry, or news aggregator to use. Browse RBA's annotated `/sources/` directory to find the appropriate tool, then go there to do the actual search. Best as a jumping-off point early in business/corporate research.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rba.co.uk/sources/.
2. Browse by topic/category to find annotated links to business data sources, company registries, news aggregators, and research tools.
3. Read the annotations to pick the source that fits your need (jurisdiction, data type).
4. Follow the link to the chosen source and run your actual `employer-org`/topic search there.

## Inputs → Outputs
- **In:** a topic/category you browse (no target selector submitted).
- **Out:** annotated links to specialized `employer-org`/business-intelligence sources and tools.
- **Empty/negative result looks like:** no listed source for a very niche need — fall back to general search or another meta-directory.

## Gotchas & OpSec
- Signpost, not a source: it returns *pointers* to tools, not data about a person or company — the real lookup happens on the linked site.
- Link rot: a curated list can contain outdated/dead links over time — verify the destination is still live.
- OpSec: passive; the directory itself involves no target interaction.

## Overlaps ("do both")
- Pairs with company-registry and business-search tools you find *through* it — use RBA to choose the right database, then those to extract the data.

## Trust & verifiability
`trust: community` — a respected independent curated directory; reliable as a signpost, but always evaluate the linked source itself for authority and currency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rba-business-information-resources |
| category | public-records |
| selectorsIn → selectorsOut | (none) → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
