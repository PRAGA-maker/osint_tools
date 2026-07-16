---
id: lei-search
name: LEI Search (GLEIF)
description: Use when you have an `employer-org` and want its legal identity and ownership chain — returns the entity's registered name, address, and parent/child company links.
url: https://search.gleif.org/#/search/
category: public-records
path:
- public-records
bestFor: Looking up a company's Legal Entity Identifier (LEI) to get its official name, registered address, and "who owns whom" parent/subsidiary relationships.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free and open — GLEIF is a nonprofit and the entire LEI database is public with a free API.
opsec: passive
opsecNote: Querying the public GLEIF database is passive — it's an authoritative registry lookup that touches nothing about the subject and notifies no one. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Global Legal Entity Identifier Foundation (GLEIF); LEI records are validated, authoritative regulatory data used across global finance.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- GLEIF LEI search
- Legal Entity Identifier search
tags:
- Company information search
- corporate-ownership
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# LEI Search (GLEIF)

> The global LEI registry — resolve a company to its official legal identity, registered address, and, crucially, its corporate ownership chain: who owns it and what it owns.

## When to use
You have an `employer-org` (a company tied to your subject — an employer, a business they run, a shell in a document) and want authoritative, cross-border corporate facts: the exact legal name, jurisdiction, registered `address`, and the parent/subsidiary relationships GLEIF records. The "who owns whom" links are the standout feature — they map corporate structures that hide a beneficial owner or connect a person's businesses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open search.gleif.org and enter the company name or a known LEI.
2. Open the entity record: legal name, legal/HQ `address`, jurisdiction, registration authority, and status.
3. Follow the relationship data — "directly/ultimately consolidated by" (parents) and children — to walk the ownership tree.
4. For bulk/automated work, use GLEIF's free API on the same data.
5. Pivot: a parent/subsidiary (`associate` entity) reveals the corporate group; a registered address and registration authority feed national-registry lookups that name directors/owners (the actual people).

## Inputs → Outputs
- **In:** `employer-org` (company name or LEI)
- **Out:** official `employer-org` legal name, registered `address`, and parent/child `associate` entities (ownership chain)
- **Empty/negative result looks like:** no LEI record — many small/private companies never obtained an LEI (LEIs are common for entities in financial markets), so absence doesn't mean the company is fake; use national registries instead.

## Gotchas & OpSec
- LEI coverage skews to entities active in financial markets; small local businesses often have no LEI.
- GLEIF gives the corporate structure and address, not the individual directors/owners — pivot to a company registry for the people.
- Data is self-reported then validated; recent changes may lag.
- OpSec: fully passive, authoritative.

## Overlaps ("do both")
- Pairs with national company registries (Companies House, OpenCorporates, etc.) — GLEIF maps the ownership tree across borders; the registries then name the humans (directors, shareholders) behind each entity.

## Trust & verifiability
`trust: trusted` — GLEIF is the authoritative global source for LEI data; records are validated regulatory data, making ownership links high-confidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lei-search |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
