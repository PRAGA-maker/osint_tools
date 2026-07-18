---
id: rusprofile
name: RusProfile
description: Use when you have a Russian `name` or company and want directorships, registration and ownership links — returns employer-org, associate and address.
url: https://www.rusprofile.ru/
category: public-records
path:
- public-records
- company-profiles
bestFor: Free lookup of Russian legal entities, their directors/founders, and cross-links between people and companies.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: freemium
costNote: Core company/director data is free to view; detailed reports and some filings are paid. No account needed for basic lookups.
opsec: passive
opsecNote: Searching a public registry mirror does not touch the subject. Route Russian-site traffic through an appropriate VPN and a sock-puppet browser; be mindful of the legal/operational sensitivities of researching Russian entities.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used aggregator of Russia's official company registry (EGRUL/EGRIP) data; convenient and generally accurate, but a third-party mirror — confirm critical facts against the primary registry.
missingPersonsRelevance: medium
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- RusProfile
- rusprofile.ru
tags:
- corporate-registry
- russia
- company-research
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# RusProfile

> A free, searchable aggregation of Russia's official company registry — the go-to for tying a Russian name to companies, directorships, and the people around them.

## When to use
The subject has a Russian business dimension and you want the corporate paper trail: which legal entities they direct or founded, a company's registered `address` and officers, ownership chains, and the other individuals (`associate`s) linked through shared directorships. Searching a `name` surfaces the person's affiliations; searching a company (or INN/OGRN) surfaces its officers and history. This is one of the strongest free entry points for Russian corporate OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rusprofile.ru/ and search a person's `name`, a company name, or a tax/registration ID (INN/OGRN).
2. On a company page, read the registered address, director/founders, capital, status, and change history.
3. On a person page, read the list of companies they are or were tied to, and follow to co-directors.
4. Cross-check important findings against the primary EGRUL registry, since RusProfile is a mirror.
5. Pivot: co-directors/founders → `associate` mapping; registered `address` → location and other entities at that address; company IDs → sanctions/court databases.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or a Russian entity ID (INN/OGRN)
- **Out:** `employer-org` (companies/directorships), `associate` (co-officers/founders), `address` (registered addresses)
- **Empty/negative result looks like:** no matching person/entity, or only common-name collisions — the subject may have no Russian corporate footprint or the name is transliterated differently; try Cyrillic spelling and the primary registry.

## Gotchas & OpSec
- Transliteration matters — search the Cyrillic form; Latin spellings miss records.
- Third-party mirror: accurate in general, but verify load-bearing facts against the official EGRUL/EGRIP.
- OpSec: passive, but be deliberate about VPN/sock-puppet and the sensitivities of Russian-entity research.

## Overlaps ("do both")
- Pairs with sanctions/court databases and the primary EGRUL registry — RusProfile gives fast person↔company cross-linking, while those confirm the underlying records and add legal/enforcement context.

## Trust & verifiability
`trust: community` — a reliable convenience layer over official registry data; treat it as a strong lead source but corroborate anything critical against the primary Russian registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rusprofile |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
