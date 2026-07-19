---
id: who-do-you-search
name: Who Do You Search (WhoDoYou)
description: Use when you have a business/service `name` or trade and a city and want local recommendations and business listings — returns local `employer-org`s and `address`es across North American regional directories.
url: https://www.whodoyou.com
category: public-records
path:
- public-records
bestFor: Finding local businesses/tradespeople by trade/occupation and city across WhoDoYou's North American regional directories.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search the public business directories; no account required to browse.
opsec: passive
opsecNote: Passive — you browse public local-business directories, transmitting nothing about a personal target. Only relevant when a subject is tied to a business/trade in a covered region.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A network of regional North American local-business/recommendation directories (Names and Numbers, COSSD, etc.); useful for business leads, not authoritative personal records.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WhoDoYou
- Names and Numbers
tags:
- toddington
- company-search
- local-business
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Who Do You Search (WhoDoYou)

> A hub of North American local-business directories — search a trade + city to surface businesses and the people/addresses behind them.

## When to use
Your subject is linked to a local business or trade (a tradesperson, shop owner, service provider) in the US/Canada, and you want to find that business's listing, `address`, and contact details. WhoDoYou aggregates regional directories (Names and Numbers, COSSD energy services, county directories), so it's a business/occupation lens rather than a personal-records search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whodoyou.com and pick the relevant regional directory, or search directly.
2. Enter a business `name`, product, occupation/trade, plus a city.
3. Read the output: matching local `employer-org`s with `address`, phone, and category.
4. Pivot: use a business address/phone to connect it to the person, then cross-reference registries and people-search tools.

## Inputs → Outputs
- **In:** a business `name` / trade / occupation + city
- **Out:** local `employer-org` listings with `address` and contact details
- **Empty/negative result looks like:** no listings for a trade+city combo means it isn't in these regional directories — try a broader term or a national business registry.

## Gotchas & OpSec
- Coverage is regional (specific US/Canadian areas), not comprehensive — a blank is not proof the business doesn't exist.
- It surfaces businesses, not people directly; you must bridge business→person yourself.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Pairs with national company registries and people-search — use this for local/trade discovery, those for authoritative ownership and personal links.

## Trust & verifiability
`trust: community` — commercial directory aggregator; verify any business detail against an official registry or the business's own site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | who-do-you-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
