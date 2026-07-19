---
id: youcontrol
name: YouControl
description: Use when you have a Ukrainian company or a person's `name` and want ownership/connection data — returns founders, beneficial owners, addresses and linked entities.
url: https://youcontrol.com.ua/en/
category: public-records
path:
- public-records
bestFor: Profiling Ukrainian companies and their people — founders, beneficial owners, and connections across 7M+ entities from official registries.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- associate
- address
status: live
pricing: freemium
costNote: Free tier after registration — OpenData across 22 registries, ~7 profiles/day and limited monitoring; full analytics and higher volume require a paid plan.
opsec: passive
opsecNote: Searches query aggregated official registries, not the subject, so no one is notified. A free account is required and its activity is logged to you — use a dedicated account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A widely-used Ukrainian corporate-intelligence platform sourcing from 220+ official registries and used by most Ukrainian banks; the underlying data is authoritative government registry data.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- youcontrol.com.ua
tags:
- company-research
- ukraine
- beneficial-ownership
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# YouControl

> Ukraine's leading corporate-intelligence platform — full profiles of 7M+ Ukrainian companies and entrepreneurs, exposing founders, beneficial owners, and the connections between them.

## When to use
Your subject is tied to Ukraine as a company founder, director, beneficial owner, or entrepreneur — or you have a Ukrainian company and want the people behind it. YouControl aggregates 220+ official registries into one profile that names owners, maps connections (shared addresses, phones, leadership), and flags sanctions/offshore links, making it a powerful way to link a `name` to businesses, `associate`s, and addresses in Ukraine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://youcontrol.com.ua/en/ (free OpenData tier).
2. Search by company name/EDRPOU code, or by a person's `name` to find entities they're tied to.
3. Open a company profile: founders/beneficiaries, registered `address`, activities, status, and financials.
4. Use the connections view to see entities linked by shared owners, addresses, or phone numbers.
5. Mind the free-tier cap (~7 profiles/day); spend views on the most relevant entities.
6. Pivot: founders/beneficiaries → people-search and `associate` mapping; shared `address`/phone → connected companies; sanctions flags → further due diligence.

## Inputs → Outputs
- **In:** `employer-org` (Ukrainian company / EDRPOU) or a person's `name`
- **Out:** founders, beneficial owners (`name`), `associate` connections, registered `address`es, and risk flags
- **Empty/negative result looks like:** no matching entity, or a profile without beneficiary detail — some ownership is held through nominees or foreign layers the registries don't pierce. A gap in ownership isn't proof of none.

## Gotchas & OpSec
- Ukraine-scoped: authoritative for Ukrainian entities, not a global registry.
- Free tier is capped (profiles/day, limited monitoring); deep or bulk work needs a paid plan.
- Registration required; the interface is strongest in Ukrainian though English is available.
- OpSec: passive toward the subject; your logged-in searches are recorded — use a dedicated account.

## Overlaps ("do both")
- Complements OCCRP's `[[investigative-dashboard]]` and cross-border registry tools — use YouControl as the authoritative Ukraine source, then follow foreign-owner links into other jurisdictions' registries.

## Trust & verifiability
`trust: trusted` — built on 220+ official Ukrainian registries and relied on by most Ukrainian banks; the data is authoritative, with the standard caveat that nominee/offshore structures can obscure true beneficial ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youcontrol |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
