---
id: jersey-financial-services-commission
name: Jersey Financial Services Commission
description: Use when you have a Jersey company `name` or `employer-org` and want its registry record — returns registration status, company number and officer/`associate` leads.
url: https://www.jerseyfsc.org
category: search-engines
path:
- search-engines
bestFor: Confirming a Jersey-registered company exists and pulling its registry basics — status, number, type — as an entry point into offshore corporate structures.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Basic company-registry search (name, number, status, type) is free via the JFSC Companies Registry / myRegistry. Full filed documents and ownership detail are paid, per-document.
opsec: passive
opsecNote: Searching the public registry is anonymous and does not alert the company. Purchasing filings requires a myRegistry account but is a normal, non-alerting transaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official statutory regulator and companies registrar for Jersey; registry records are authoritative for existence/status, though beneficial ownership is not fully public.
missingPersonsRelevance: medium
coverage:
- je
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- jerseyfsc-org
aliases:
- JFSC
- jerseyfsc.org
- Jersey Companies Registry
tags:
- toddington
- curated-directory
- specialty-search
- corporate-registry
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Jersey Financial Services Commission

> Jersey's official regulator and companies registrar — a free search to confirm a Jersey-registered entity and its status, and a gateway into offshore structures often used to hold assets.

## When to use
Your subject is linked to a Jersey company, trust or fund — a common offshore layer for holding property, aircraft, or wealth — and you want to confirm it exists, get its company number and status, and identify officers or related entities to follow. Use it to turn a corporate `name` from another record into a verified registry entry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jerseyfsc.org and go to "Search Companies Registry" / myRegistry.
2. Search the company `name` or number; read status (active/dissolved), type, and registration date.
3. For officers/filed documents, use the myRegistry portal (account + per-document fee).
4. Pivot: take officer/agent `associate` names into people-search and other corporate registries (UK Companies House, other offshore registries) to unwind the ownership chain; regulated firms also appear in the JFSC's regulated-entities register.

## Inputs → Outputs
- **In:** company `name` or `employer-org` (Jersey entity)
- **Out:** registration status, company number/type; officer and related-entity (`associate`) leads via filings
- **Empty/negative result looks like:** no match — the entity may be dissolved, spelled differently, or registered in another jurisdiction (many "offshore" firms are in Guernsey, BVI, Cayman, etc.). Absence in Jersey doesn't rule out an offshore structure elsewhere.

## Gotchas & OpSec
- **Beneficial ownership isn't fully public** — Jersey maintains ownership data but access is restricted; expect officers/agents, not always the true beneficial owner.
- Deeper documents are paid and behind a myRegistry account.
- OpSec: searching is passive.

## Overlaps ("do both")
- Pairs with UK Companies House and other offshore registries — a Jersey holding company usually connects to entities/people registered elsewhere; cross-registry work is how you reach the humans.

## Trust & verifiability
`trust: trusted` — the official Jersey registrar; existence and status are authoritative. Because beneficial ownership is not fully open, corroborate the people behind an entity through linked registries and other records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jersey-financial-services-commission |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
