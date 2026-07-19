---
id: money-house-search-switzerland
name: Moneyhouse (Switzerland)
description: Use when you have a `name` or Swiss `employer-org` and want commercial-register data — returns company registrations, directorships and addresses linking people to businesses.
url: https://www.moneyhouse.ch/en/
category: public-records
path:
- public-records
bestFor: Linking a person to Swiss companies (and vice versa) via commercial-register directorships and addresses.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Freemium — basic company/person listings and register data are free to view; full reports, financials and some person details require a paid subscription.
opsec: passive
opsecNote: Reading published Swiss commercial-register data — no login needed for basic views, nothing written, no subject notification. Commercial-register entries are public by law, so lookups are low-risk; a paid account is attributable, so use a research identity if you subscribe.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Moneyhouse compiles the official Swiss commercial register (Handelsregister) plus other sources; register-derived facts (company, officers, address) are authoritative, while enriched/estimated fields are secondary.
missingPersonsRelevance: medium
coverage:
- ch
auth: none
api: false
localInstall: false
registration: false
aliases:
- Moneyhouse.ch
- Money House Search Switzerland
tags:
- toddington
- curated-directory
- company-search
- switzerland
- corporate-registry
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Moneyhouse (Switzerland)

> Switzerland's business-information portal over the commercial register — search a person to find the companies they direct, or a company to find its officers and address.

## When to use
You have a `name` with a Swiss business connection, or a Swiss `employer-org`, and you want the corporate paper trail: directorships and officer roles, the companies a person is tied to, registered addresses, and co-directors (`associate` leads). Moneyhouse aggregates the official Swiss Handelsregister, so a hit links an individual to businesses, places them at a registered address, and reveals their commercial network — valuable for establishing an identity, an occupation, or a location in Switzerland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.moneyhouse.ch/en/ and search by person name or company.
2. Open the profile: for a person, their mandates/directorships; for a company, its officers, register number, and address.
3. Note co-officers (`associate`s) and registered `address`es; follow to linked companies.
4. For fields behind the paywall (full reports, some person data), decide whether a subscription is warranted or cross-check the free official Zefix register.
5. Pivot: a registered `address` and `employer-org` feed mapping and further registry lookups; co-directors extend the network.

## Inputs → Outputs
- **In:** `name` or Swiss `employer-org`
- **Out:** company registrations, directorships, registered `address`, co-officers (`associate`)
- **Empty/negative result looks like:** no person/company match — meaning no Swiss commercial-register link under that name (they may have no Swiss business role, or use a name variant).

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall gates full reports and some person details — the free tier still shows register basics.
- Switzerland-only; for cross-border figures combine with other national registries.
- Enriched/estimated fields (e.g. credit indicators) are secondary — trust the register-derived facts, verify the rest.

## Overlaps ("do both")
- Pairs with the official Swiss Zefix commercial register and OpenCorporates — this adds person-centric search and enrichment; those give the authoritative free register record.

## Trust & verifiability
`trust: trusted` — built on the official Swiss commercial register; company/officer/address facts are authoritative, with enriched fields worth a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | money-house-search-switzerland |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
