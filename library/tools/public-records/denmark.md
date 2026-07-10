---
id: denmark
name: Denmark (CVR Business Register)
description: Use when you have a Danish company `name`, `address`, or CVR number (or a person's name as an owner/director) and want the official business record — returns registered company, address, and associated people.
url: https://datacvr.virk.dk/data/index.php?q=forside&language=en-gb
category: public-records
path:
- public-records
bestFor: Looking up Danish companies and their registered owners/officers in the official CVR register.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: free
costNote: Free official service — CVR is Denmark's public Central Business Register, operated by the Danish Business Authority (Erhvervsstyrelsen). No account for standard lookups.
opsec: passive
opsecNote: Passive — you query an official government business register, not the individual. Company officers are public by Danish law and are not notified. Standard government-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CVR (datacvr.virk.dk) is the authoritative Danish state business register; company and officer data is official primary-source record.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CVR
- Det Centrale Virksomhedsregister
- Virk datacvr
tags:
- companysites
- Company Related Sites
- business-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Denmark (CVR Business Register)

> Denmark's official Central Business Register (CVR) — the authoritative public source for Danish companies and the people who own or run them, searchable by company, address, CVR number, or person.

## When to use
You have a Danish business identifier — a company `name`, a CVR number, a trading `address`, or a person you suspect is a Danish company owner/director — and want the official record: the registered entity, its address, its officers, and its status. In people work this bridges a subject to a real, legally-registered business and its address, and reveals co-owners/officers (`associate`s) — Denmark makes this data unusually open.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datacvr.virk.dk/ (switch to English via the language link).
2. Search by company `name`, CVR number, `address`, or a person's `name` (owner/officer search).
3. Open the company record to read: legal name, CVR number, registered `address`, industry code, status, and associated people (owners, board, management).
4. Cross-reference officers across companies to map a person's business interests.
5. Pivot: the registered address is a location lead; co-officers are new subjects; the company links onward to Danish annual-accounts and EU business data.

## Inputs → Outputs
- **In:** company `name`, CVR number, `address`, or person `name`
- **Out:** registered `employer-org`, CVR number (`document-id`), registered `address`, officers/owners (`associate`), status
- **Empty/negative result looks like:** no matching entity/person — meaning not a registered Danish business (or not searchable by that field). Sole traders below thresholds and purely personal data won't appear.

## Gotchas & OpSec
- Scope is Danish registered businesses — it identifies people only in their capacity as company owners/officers, not the general population.
- Some personal-address protections apply; not every officer's home address is shown.
- Interface defaults to Danish; use the English toggle. An open API and bulk data are available for scale.
- Passive; nothing reaches the company or its officers.

## Overlaps ("do both")
- Pairs with `[[vat-search-co-uk]]` — CVR gives the Danish company + officers; VAT tools verify the EU VAT identity of the same entity.
- Officer names feed general people-search and other national registers when a person operates across borders.

## Trust & verifiability
`trust: trusted` — CVR is Denmark's official state business register and its records are authoritative primary source. The only limits are scope (registered businesses/officers) and privacy protections on some personal fields.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | denmark |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
