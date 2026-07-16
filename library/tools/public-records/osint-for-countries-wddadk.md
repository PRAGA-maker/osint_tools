---
id: osint-for-countries-wddadk
name: OSINT for Countries (wddadk)
description: Use when a lead is tied to a specific `address`/country and you want the local registries and people-search resources for it — returns pointers to national records that yield `address`, `document-id`, and `employer-org`.
url: https://github.com/wddadk/OSINT-for-countries
category: public-records
path:
- public-records
bestFor: Finding the right country-specific registries and OSINT resources for a lead abroad.
selectorsIn:
- name
- address
selectorsOut:
- address
- document-id
- employer-org
status: live
pricing: free
costNote: Free, open GitHub repository; no account needed to read (a free GitHub login only helps for starring/cloning).
opsec: passive
opsecNote: Browsing the repo is passive and leaks nothing about your target. OpSec risk shifts to the individual linked resources — some foreign registries log queries or require in-country access; assess each linked site on its own before querying.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained GitHub list (wddadk); links are curated but unverified and can rot — confirm each destination is live before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT for countries
- wddadk OSINT-for-countries
- country OSINT index
tags:
- tool-collection
- public-records
- country-specific
- github
source: ultimate-osint
lastVerified: '2026-07-16'
enrichment: full
---

# OSINT for Countries (wddadk)

> A GitHub index that maps OSINT tools, registries, and databases to individual countries — the fastest way to find the right local resource when a lead crosses a border.

## When to use
Your subject has a `name` plus a country/`address` tie abroad and you need the *local* record systems — business registries, government portals, national people-search sites, court/legal databases — rather than generic US-centric tools. This repo covers 193 UN member states plus dependent territories and disputed regions, so it turns "the trail leads to country X, now what?" into a concrete list of country-specific starting points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/wddadk/OSINT-for-countries.
2. Use the README's country index (or GitHub's in-page find, `t` / Ctrl-F) to jump to the target country.
3. Read that country's section: it lists local registries, government portals, and OSINT resources with short descriptions.
4. Open the specific linked resource that matches your selector (e.g. a company registry for an `employer-org`, a civil registry for `document-id`).
5. If the country has no direct entry, fall back to the repo's multi-country/global resources section.
6. Pivot: each linked registry becomes its own lookup — feed the `name`/`address` you have into it.

## Inputs → Outputs
- **In:** `name` and/or `address`/country context
- **Out:** pointers to national resources that in turn yield `address`, `document-id`, `employer-org`, and local social/associate leads
- **Empty/negative result looks like:** a country section that is sparse or link-rotted, or a country with only a "no dedicated resource — use the global list" note. It is an index, not a database, so it never returns a person directly.

## Gotchas & OpSec
- It's a directory, not a search engine — value depends on the freshness of the underlying links, which can rot.
- Foreign registries vary wildly in language, access rules, and logging; some are in-country-only or fee-gated. Vet each before querying.
- OpSec: reading the repo is passive; the linked resources carry their own exposure — treat each as a separate risk decision.

## Overlaps ("do both")
- Pairs with any generic public-records directory — this one is organized by *country* where broad directories are organized by *record type*, so use both when a lead is international.

## Trust & verifiability
`trust: community` — curated by a single GitHub maintainer; the curation is helpful but each destination is unverified, so confirm a linked site is live and authentic before acting on what it returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-for-countries-wddadk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, document-id, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
