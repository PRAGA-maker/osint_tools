---
id: corporate-affairs-registry-database
name: New Brunswick Corporate Affairs Registry (CARD)
description: Use when you have a company `name` or a person's `name` and want New Brunswick (Canada) corporate records — returns employer-org, registered address, and director/agent associate leads.
url: https://www.pxw2.snb.ca/card_online/cardsearch.aspx
category: public-records
path:
- public-records
bestFor: Searching the official New Brunswick corporate registry (CARD) for companies, status, and associated people.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Basic corporate name search and status are free via the Service New Brunswick CARD online portal; certified documents/detailed filings may carry a fee.
opsec: passive
opsecNote: This is an official government registry lookup — querying it involves no contact with the company or its officers and alerts no one. It's the authoritative source for NB corporate records, so results are reliable, but coverage is limited to entities registered in New Brunswick.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Service New Brunswick (CARD — Corporate Affairs Registration Database); the official provincial corporate registry.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CARD
- Service New Brunswick Corporate Registry
- New Brunswick corporate search
tags:
- corporate-registry
- canada
- new-brunswick
- public-records
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# New Brunswick Corporate Affairs Registry (CARD)

> Service New Brunswick's official corporate registry — search NB companies and business names to get status, registered address, and the people (directors/agents) attached to them.

## When to use
You're placing a person or business in New Brunswick, Canada and want authoritative corporate records: a company `name`/number to profile, or a person's `name` to find entities they're tied to. CARD returns the corporation's status, type, registered office `address`, and associated officers/agents (`associate`) — solid corroboration for linking a person to a business, an address, or co-officers in a due-diligence or missing-persons context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CARD online search: https://www.pxw2.snb.ca/card_online/cardsearch.aspx.
2. Search by corporate/business `name` or registry number (`selectorsIn`).
3. Open a result: corporation status, type, registration dates, registered office `address`, and associated agent/officers (`selectorsOut`).
4. Pivot: the registered address feeds address/people search; officers/agents are `associate` leads; cross-check against pan-Canadian corporate search and other provinces' registries.

## Inputs → Outputs
- **In:** `name` (company/person) or `employer-org` (registry number)
- **Out:** `employer-org` (corporate profile/status), `address` (registered office), `associate` (directors/agents), registration details
- **Empty/negative result looks like:** no match — the entity isn't registered in New Brunswick (it may be federally or in another province); check Corporations Canada and the relevant provincial registry.

## Gotchas & OpSec
- Human-in-the-loop: none for basic search; certified documents may require payment.
- OpSec: passive — an official registry query; nobody is notified.
- Jurisdiction-bound: covers only New Brunswick entities; a person's company may be registered federally or elsewhere, so absence here isn't absence everywhere.

## Overlaps ("do both")
- Pairs with Corporations Canada (federal) and other provincial registries (e.g. [[alberta-business-search]]) — a subject's corporate footprint often spans jurisdictions, so search the relevant province(s) plus federal.

## Trust & verifiability
`trust: trusted` — the official Service New Brunswick corporate registry, authoritative for NB entities. Records are reliable and current for that province; just remember its coverage stops at the provincial boundary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corporate-affairs-registry-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
