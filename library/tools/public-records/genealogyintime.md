---
id: genealogyintime
name: GenealogyInTime
description: Use when you have a `name` and want to sweep billions of free genealogy/ancestral records at once — returns matching records with dates, relatives and source sites.
url: http://www.genealogyintime.com/tools/genealogy-search-engine.html
category: public-records
path:
- public-records
bestFor: A single free meta-search across 2B+ ancestral records on 1,000+ genealogy sites to surface birth/death dates and family links for a name.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free to search billions of records; individual record images on the destination sites it links to may be paywalled by those providers.
opsec: passive
opsecNote: A record meta-search; the subject is not notified. No login required. Some linked destination sites may set their own cookies/logins — that is downstream of this tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running genealogy publication (GenealogyInTime Magazine). It aggregates/links other sites' records, so record quality varies by underlying source; confirm at the source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- familysearch
- geneologyintime-family-tree-search-engine
aliases:
- GenealogyInTime Magazine
- Genealogy Search Engine
tags:
- genealogy
- family
- records-search
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# GenealogyInTime

> A free genealogy meta-search: one name query sweeps billions of ancestral records across 1,000+ sites and points you to the matches.

## When to use
You have a subject's `name` (living or deceased, and their relatives) and want breadth — a single search that fans out across the world's free genealogy records instead of visiting each archive individually. Strong for surfacing birth/death dates (`dob`), family relationships (`associate`), and which specific archive holds a matching record, so you can then go deep on the right source. Its Family Tree Search Engine also finds forums/trees discussing the family.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.genealogyintime.com/tools/genealogy-search-engine.html.
2. Enter the subject's `name` (add dates/places if the interface allows, to cut noise).
3. Review the aggregated hits: records drawn from 2.2B+ ancestral records across North America, Europe, UK, Ireland, Australia/NZ and more, each linking to the host site.
4. Optionally run the Family Tree Search Engine to catch online trees/forum mentions of the family.
5. Pivot: open a promising record on its source site to confirm dates/relatives; feed a confirmed death into `[[familysearch]]` (SSDI) or cemetery records.

## Inputs → Outputs
- **In:** `name` (± dates/places)
- **Out:** matching records linking to `name`, `dob` (birth/death dates), and `associate` (relatives/family links)
- **Empty/negative result looks like:** few or no hits. Common names flood results (add dates/places), while rare or living subjects with little genealogical footprint may return nothing — absence is not proof.

## Gotchas & OpSec
- It is a *pointer* to records on other sites — record images/details may be paywalled once you click through.
- Aggregated quality varies by underlying source; always confirm a date/relationship at the origin record.
- Skews toward historical/deceased individuals; thin for living people.
- OpSec: passive; no login, no subject notification.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` — GenealogyInTime casts a wide net across many archives; FamilySearch's SSDI gives an authoritative US death confirmation to anchor a hit.

## Trust & verifiability
`trust: community` — a reputable long-running genealogy publisher, but it aggregates and links third-party records, so the trust ultimately lies with each source. Verify any date or relationship against the origin record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogyintime |
</content>
