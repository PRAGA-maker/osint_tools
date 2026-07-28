---
id: catalogue-of-research-databases-occrp-id
name: OCCRP Catalogue of Research Databases
description: Use when you have a `name` or `employer-org` and need to know WHICH public register or database to search in a given country — returns pointers to corporate/court/registry sources.
url: https://investigativedashboard.org/databases
category: public-records
path:
- public-records
bestFor: Discovering which official registers and research databases exist for a country/topic before you go searching.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free catalogue maintained by OCCRP; browsing requires no account (some linked source databases have their own access rules).
opsec: passive
opsecNote: The catalogue itself is a passive directory — you only browse OCCRP's list, disclosing nothing about a target. OpSec depends on the downstream database you then open; apply the appropriate caution there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated by OCCRP (Organized Crime and Corruption Reporting Project) as part of its Investigative Dashboard; a well-regarded investigative-journalism source directory.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- investigative-dashboard
aliases:
- OCCRP ID databases
- Investigative Dashboard databases
tags:
- corporate
- registries
- occrp
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# OCCRP Catalogue of Research Databases

> OCCRP's directory of official registers and research databases worldwide — the "where do I even look?" index that points you to the right corporate registry, court record or public database for a country.

## When to use
You have a `name` or `employer-org` and know the country/jurisdiction that matters, but not which database holds the records — company registries, land/property records, court dockets, gazettes, sanctions/PEP lists, procurement. This catalogue tells you what public sources exist for that place and topic and links you to them, turning "I need this person's/company's records in country X" into a concrete list of databases to query. It's a router to primary sources, not a source of person data itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://investigativedashboard.org/databases.
2. Filter by country and/or category (business registers, court records, land, media, etc.).
3. Pick the database that fits your `name`/`employer-org` question and follow the link.
4. Search the target register directly for the entity/person; note each source's access rules.
5. Pivot: registry results (directors, addresses, related companies) become `associate`/`employer-org` leads; loop back to the catalogue for the next jurisdiction.

## Inputs → Outputs
- **In:** the jurisdiction + your `name`/`employer-org` question (used to choose a database)
- **Out:** pointers to the right registries/databases, which in turn yield `employer-org` links and `associate`/officer names
- **Empty/negative result looks like:** few or no databases listed for a country — coverage is uneven; fall back to the country's own government portals or a broader business-search tool.

## Gotchas & OpSec
- OpSec: the catalogue is passive; caution applies to whatever downstream database you open (some log queries or require accounts).
- It's a directory, not a search engine — it tells you *where* to look, you still do the lookup.
- Some linked databases are paywalled, jurisdiction-restricted, or in the local language; the catalogue notes access where it can.

## Overlaps ("do both")
- Pairs with `[[investigative-dashboard]]` (OCCRP's aggregated search across many of these datasets) — use the catalogue to understand what exists, the Dashboard to search across the indexed subset.

## Trust & verifiability
`trust: trusted` — maintained by OCCRP, a leading investigative-journalism organisation; the catalogue is a respected pointer to primary/official sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | catalogue-of-research-databases-occrp-id |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
