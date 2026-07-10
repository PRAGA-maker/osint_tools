---
id: companieshouse-im
name: companieshouse.im
description: Use when you have an Isle of Man company `name` or an `employer-org` link and want registry data — returns company status, registered `address`, and filing details.
url: https://companieshouse.im/
category: public-records
path:
- public-records
bestFor: Searching Isle of Man company records (status, registered office, filings) via an open-data aggregator.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Free to search company records; ongoing monitoring/"follow" of companies is free for one company then ~£2.00-£2.50/month per company. Data is released under the Open Government Licence.
opsec: passive
opsecNote: Reading company records is passive and does not touch any individual. You disclose your query to the site; a monitoring account requires registration — use a sock-puppet identity if you subscribe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator republishing Isle of Man company data under the Open Government Licence — not the official Isle of Man Central Registry; cross-check critical facts against the official registry.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- companieshouse-gi
- company-information-service-gov-uk
aliases:
- Companies House IM
- companieshouse.im
tags:
- companysites
- Company Related Sites
- isle-of-man
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# companieshouse.im

> An open-data aggregator of Isle of Man company records — search a company's status, registered office, and filings when tracing an offshore corporate link.

## When to use
You are tracing an `employer-org` or corporate connection registered in the Isle of Man (a common offshore jurisdiction) and want to confirm the company exists, its status, registered office `address`, and filing history. Useful for corroborating a subject's stated business, mapping a corporate structure, or resolving the entity behind an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://companieshouse.im/ and search the company `name` or number.
2. Open the company record for status, registered office `address`, incorporation details, and available filings.
3. Optionally "follow" a company for change monitoring (one free; further companies are a small monthly fee).
4. Cross-check anything critical against the official Isle of Man Central Registry, since this is a republisher.
5. Pivot: a registered-office `address` and any named officers feed further corporate/address lookups.

## Inputs → Outputs
- **In:** company `name` or number (an `employer-org` link)
- **Out:** `employer-org` status/details, registered `address`, filing metadata, sometimes officer `name`s
- **Empty/negative result looks like:** no matching company — check spelling/number and the official registry before concluding the entity doesn't exist.

## Gotchas & OpSec
- This is an aggregator, **not** the official Isle of Man registry — treat it as a convenient front end and verify key facts against the government source.
- Depth of officer/beneficial-owner data may be limited compared with the official registry.
- OpSec: passive; only your query (and registration details if you subscribe to monitoring) are exposed. Use a sock puppet for accounts.

## Overlaps ("do both")
- Pairs with `[[companieshouse-gi]]` (Gibraltar) and `[[company-information-service-gov-uk]]` (UK) when a subject's corporate footprint spans multiple British Isles jurisdictions.

## Trust & verifiability
`trust: community` — republishes official IoM company data under the Open Government Licence, but as a third party. The underlying records are authoritative; confirm anything decision-critical against the official Isle of Man Central Registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | companieshouse-im |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
