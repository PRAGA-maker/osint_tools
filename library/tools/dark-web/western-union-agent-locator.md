---
id: western-union-agent-locator
name: Western Union Agent Locator
description: Use when you have a `geolocation`/`address` (city/country) and want the Western Union agent/pickup locations there — returns branch `address`es and hours, useful for money-transfer context.
url: https://www.westernunion.com/us/en/web/find-locations/agent-locator
category: dark-web
path:
- dark-web
bestFor: Finding the physical Western Union send/pickup agent locations in a given city or country.
selectorsIn:
- geolocation
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public store-locator on Western Union's site; no account.
opsec: passive
opsecNote: Passive — you look up public agent locations by area, not any person. Nothing about a subject is transmitted. WU may log your search; use a clean browser if the enquiry is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Western Union store locator; authoritative for where WU agent locations are, though it reveals nothing about individual transactions.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WU agent locator
tags:
- toddington
- money-transfer
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Western Union Agent Locator

> Western Union's official store finder — list the physical agent/pickup locations in a city or country.

## When to use
A lead involves a Western Union money transfer and you need to know the physical agent locations in a given area — e.g. where a subject could have collected or sent funds, or which branches serve a town they were last known in. It returns locations, not transactions, so treat it as geographic/logistical context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Western Union agent locator (https://www.westernunion.com/us/en/web/find-locations/agent-locator; regional sites like westernunion.co.uk also work).
2. Enter a city, address, or country.
3. Read the output: a list/map of agent `address`es with hours and services offered.
4. Pivot: use the locations to narrow a physical search area or to inform lawful enquiries; actual transaction data requires WU/law-enforcement channels, not this tool.

## Inputs → Outputs
- **In:** a `geolocation` / `address` (city, country)
- **Out:** Western Union agent `address`es, hours, and services in that area
- **Empty/negative result looks like:** no agents listed means WU has no presence there (or the query area was too narrow) — widen the search.

## Gotchas & OpSec
- Locations only — it exposes **nothing** about who transacted; transactional data is not public.
- Regional WU domains vary; use the one for the target country.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Complements mapping tools — this pins WU agent points; a general mapper gives surrounding context.

## Trust & verifiability
`trust: trusted` — first-party locator; location data is authoritative, but draw no conclusions about individuals from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | western-union-agent-locator |
| category | dark-web |
| selectorsIn → selectorsOut | geolocation, address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
