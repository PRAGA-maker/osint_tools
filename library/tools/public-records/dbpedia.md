---
id: dbpedia
name: DBpedia
description: Use when you have an entity `name` (person, org, place) and want structured, machine-readable facts from Wikipedia — returns linked attributes and `associate`/`employer-org` relations via SPARQL.
url: http://wiki.dbpedia.org
category: public-records
path:
- public-records
bestFor: Querying Wikipedia's content as a structured knowledge graph (SPARQL) for entity facts and relationships.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- dob
status: live
pricing: free
costNote: Free, open-source knowledge graph; public SPARQL endpoint, Linked Data access, and downloadable datasets. No account.
opsec: passive
opsecNote: Querying a public knowledge base about notable entities — no target interaction, fully passive. Note the subject must be notable enough to have a Wikipedia article for coverage to exist.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Long-running academic/community project extracting structured data from Wikipedia; accuracy inherits Wikipedia's (crowd-edited) and the extraction can lag live edits (except DBpedia Live).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- DBPedia
tags:
- public-records
- knowledge-graph
- wikipedia
- sparql
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# DBpedia

> Wikipedia as a queryable knowledge graph — pull structured facts and relationships about notable people, organisations and places via SPARQL instead of scraping article prose.

## When to use
Your subject (or a related person/company/place) is notable enough to have a Wikipedia article, and you want the facts in structured form: birth/`dob`, affiliations (`employer-org`), relationships (`associate`), locations, and links to other entities — programmatically, so you can traverse relationships rather than read pages one by one.

## How to use it (`bestInteractionPattern`: api)
1. Open the public SPARQL endpoint (https://dbpedia.org/sparql) or browse a resource page at `dbpedia.org/page/<Entity>`.
2. Query by entity `name`/URI — e.g. select an entity's properties, or find all people linked to an `employer-org`.
3. Read the returned RDF/JSON: typed properties and links to related entities.
4. Pivot: linked `associate`s and `employer-org`s become new leads; DBpedia's URIs cross-link to Wikidata and other datasets for further structured pivots.

## Inputs → Outputs
- **In:** entity `name`/URI (person, `employer-org`, place)
- **Out:** structured attributes (`dob`, affiliations) and relations (`associate`, `employer-org`)
- **Empty/negative result looks like:** no resource for the entity — the subject isn't in Wikipedia (not notable), so DBpedia has nothing; use it only for notable entities.

## Gotchas & OpSec
- Only covers Wikipedia-notable entities — useless for ordinary private individuals.
- Data is extracted periodically; a standard endpoint can lag recent Wikipedia edits (use DBpedia Live for near-real-time).
- Accuracy inherits Wikipedia's — verify important facts against the article and primary sources.

## Overlaps ("do both")
- Pairs with Wikidata and direct Wikipedia — DBpedia and Wikidata both structure Wikipedia; query both, since coverage and freshness differ, and confirm against the live article.

## Trust & verifiability
`trust: trusted` — a respected academic project, but it mirrors Wikipedia's crowd-sourced content, so treat facts as leads to corroborate, not primary evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dbpedia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
