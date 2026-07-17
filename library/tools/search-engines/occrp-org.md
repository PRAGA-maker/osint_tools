---
id: occrp-org
name: OCCRP.org (ID Databases Directory)
description: Use when you have a subject tied to a country/region and need to find which public-record databases exist there — returns OCCRP's curated directory of registries and data sources by continent, country, and data type.
url: https://id.occrp.org/databases/
category: search-engines
path:
- search-engines
bestFor: Discovering which official/public databases to search for a given country and record type.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, publicly browsable directory maintained by OCCRP's ID research desk; no account needed to browse the listings.
opsec: passive
opsecNote: You browse a directory of data sources; no target is contacted here. The actual lookups happen on the databases it points you to — apply that source's OpSec. Fully passive at the directory stage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated by OCCRP, a leading investigative-journalism non-profit; it is a vetted signpost to primary databases rather than a data source itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- occrp-aleph
- data-occrp-org
- organized-crime-and-corruption-reporting-project
- the-pegasus-project-occrp
- visual-investigative-scenarios
aliases:
- OCCRP databases
- OCCRP ID research databases
- id.occrp.org
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# OCCRP.org (ID Databases Directory)

> OCCRP's research-desk directory of public databases — a country- and type-indexed map of *where* to look, curated by professional investigative journalists.

## When to use
You have a subject or company tied to a particular country/region and you don't know which registry, court system, or public database to search there. This directory catalogs public data sources by continent, country, and data type (company registries, courts, land, sanctions, media), so it answers "what authoritative source exists for this jurisdiction and record?" before you start searching. It's a navigation layer for cross-border work — you come here to find the right primary database, then go search it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://id.occrp.org/databases/.
2. Filter/browse by the subject's continent and country, and by the data type you need (corporate, court, property, etc.).
3. Open a listed source to see what it covers and follow its link to the actual database.
4. Run your `name`/`employer-org` search on that primary source (its own OpSec and access rules apply).
5. Pivot: for aggregated cross-dataset search instead of a directory, jump to [[occrp-aleph]]; documents you find feed deeper reading and associate mapping.

## Inputs → Outputs
- **In:** a subject/company plus the target country (to choose a source); effectively `name` / `employer-org` context
- **Out:** pointers to the right public databases (which then yield `document-id`s) for that jurisdiction
- **Empty/negative result looks like:** few or no listed sources for a country/type — coverage is uneven and some jurisdictions have little public data. Cross-check other registry directories; absence of a listing isn't proof no registry exists.

## Gotchas & OpSec
- It is a **directory, not a database** — it doesn't return records itself; it tells you where to search. The heavy lifting happens on the linked source.
- Listings can go stale as external databases move or close; verify each link resolves.
- OpSec: **passive** at the directory; apply the destination source's OpSec when you actually search it.

## Overlaps ("do both")
- Pairs with [[occrp-aleph]] — this directory tells you which *separate* databases exist; Aleph is OCCRP's own aggregated cross-dataset search. Use the directory to find primary sources, Aleph to search indexed leaks/registries at once.

## Trust & verifiability
`trust: trusted` — curated by OCCRP's professional research desk; it's a vetted signpost, and the authority of any result ultimately comes from the primary database it directs you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | occrp-org |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
