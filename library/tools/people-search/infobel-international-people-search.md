---
id: infobel-international-people-search
name: Infobel International People Search
url: http://www.infobel.com/en/world/index.aspx
category: people-search
path:
- people-search
description: Use when you have a `name` and a country and want an international directory listing — returns `address` and `phone` for people and businesses across 70+ countries.
bestFor: Cross-border white-pages: looking up a person or business by name in a chosen country when domestic directories fall short.
selectorsIn:
- name
- geolocation
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: freemium
costNote: Free directory search across many countries; some detailed/bulk business data (via InfobelPRO) is paid. Basic people/business lookups are free.
opsec: passive
opsecNote: A passive query against a public international directory; the subject is not notified and no login is needed for basic search. Attribution risk is that of any web request — use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of the oldest international directory aggregators (since 1995), covering 70+ countries; listing quality varies by country and skews to businesses/landlines, so treat entries as leads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Infobel
- infobel.com world directory
tags:
- toddington
- curated-directory
- people-search
- international-directory
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Infobel International People Search

> A veteran international white-pages aggregator — pick a country and search people or businesses by name to get an address and phone, covering 70+ countries.

## When to use
You have a `name` and know (or can guess) the subject's country, and domestic directories aren't enough — Infobel spans North/South America, Europe, Asia, Africa, the Middle East and the Pacific. Best when a trace crosses borders and you need a listing-grade address/phone in a country where you lack a native directory. Also useful for locating a business by name and country.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.infobel.com/ and choose the country (the "world" index lists them).
2. Select people or business search and enter the `name`, refining by region/city.
3. Read the listing: name, address, phone, and (for businesses) sector/opening details.
4. Repeat across candidate countries if the subject's location is uncertain.
5. Pivot: an `address`/`phone` feeds the country's national records and reverse-lookup tools; a business hit feeds corporate registries like `[[northdata-com]]`.

## Inputs → Outputs
- **In:** `name` + country (`geolocation`)
- **Out:** `address`, `phone`, `employer-org` (for business listings)
- **Empty/negative result looks like:** no listing for that name/country — coverage and freshness vary widely by country and skew to businesses and landlines. A miss in one country doesn't rule out a listing under a different spelling or nearby country.

## Gotchas & OpSec
- Coverage quality is very uneven per country; residential data is thin where local privacy law restricts directories.
- Data can be dated; confirm a current address before relying on it.
- OpSec: fully passive, no login, no subject notification.

## Overlaps ("do both")
- Pairs with national directories like `[[411-ca]]` (Canada) and `[[switchboard]]` (US) — Infobel is the fallback when you don't have a strong native directory for the subject's country.

## Trust & verifiability
`trust: community` — a long-established aggregator of licensed directory data; reliable as a lead source but variable by country, so verify entries against a local/native source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infobel-international-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name, geolocation → address, phone, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
