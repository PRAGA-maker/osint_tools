---
id: home-comptroller-texas-gov
name: Texas Comptroller
description: Use when you have a `name` or business and want Texas state financial records — returns entity/franchise-tax status, sales-tax permits, and unclaimed property.
url: https://comptroller.texas.gov/
category: public-records
path:
- public-records
bestFor: Searching Texas Comptroller records — business franchise-tax/entity status, sales-tax permit holders, and unclaimed-property claims by name.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official Texas state government search tools; no account required.
opsec: passive
opsecNote: You query official Texas state databases, not the subject — nothing is signalled. Standard government-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Texas Comptroller of Public Accounts; authoritative for Texas tax-entity status and state unclaimed property.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- comptroller.texas.gov
- Texas Comptroller of Public Accounts
tags:
- texas
- public-records
- business
- unclaimed-property
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Texas Comptroller

> The Texas state financial authority's public search tools — tie a `name` or business to Texas tax-entity status, sales-tax permits, and unclaimed property.

## When to use
Your subject has a Texas nexus and you want state financial/business records. The Comptroller offers several free searches: **Franchise Tax Account Status / Taxable Entity Search** (is a business registered/in good standing, its registered agent and address), **Sales Tax Permit** holder lookup, and **Unclaimed Property** search (money the state holds for a person/business, searchable by name). Useful for confirming a business, finding an entity's address/agent, or surfacing unclaimed funds tied to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://comptroller.texas.gov/ and pick the relevant tool (Taxable Entity Search, Sales Tax Permit search, or Unclaimed Property search).
2. Enter the business `name`/entity, or a person's `name` (for unclaimed property).
3. Read the result: entity status, registered agent/`address`, permit status, or an unclaimed-property record with the holder and amount.
4. Pivot: a registered agent/address links the entity to people/locations; an unclaimed-property hit confirms a name/prior address and is a locate lead.

## Inputs → Outputs
- **In:** `name` (person, for unclaimed property) or `employer-org` (business)
- **Out:** franchise-tax/entity status, registered agent + `address`, sales-tax permit, unclaimed-property records
- **Empty/negative result looks like:** no match — no Texas registration/permit for that entity, or no unclaimed property for that name; absence is limited to Texas and doesn't rule out records elsewhere.

## Gotchas & OpSec
- Scope is **Texas** only; a subject's out-of-state entities/property won't appear here.
- Different tools cover different data (entity vs permit vs unclaimed property) — use the right one for your question.
- Unclaimed-property names can collide; confirm with a prior address before attributing.
- OpSec: passive — official state database.

## Overlaps ("do both")
- Pairs with the Texas Secretary of State business search, other states' unclaimed-property sites (and MissingMoney.com), and corporate registries — combine to cover entity formation, multi-state property, and ownership the Comptroller doesn't show.

## Trust & verifiability
`trust: trusted` — official Texas government data, authoritative for Texas tax-entity status and state-held unclaimed property. The limitation is jurisdiction (Texas), not reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | home-comptroller-texas-gov |
