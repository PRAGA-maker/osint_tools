---
id: federalcorporation
name: FederalCorporation
description: Use when you have a `name` or `employer-org` and want Canadian federal corporation records — directors, addresses, and same-director company links — returns address, associate and employer-org leads.
url: https://federalcorporation.ca/
category: public-records
path:
- public-records
bestFor: Searching Canadian federal (Corporations Canada) company records by name, number, city, or director.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- associate
- employer-org
status: live
pricing: freemium
costNote: Free to search and view records; built on Corporations Canada open data (ISED). No account required for basic lookups.
opsec: passive
opsecNote: Passive — you query a public registry mirror, never the subject. Searches run against the site's copy of government open data, so your interest isn't disclosed to the corporation or its directors.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party mirror/reindex of official Corporations Canada open data; the underlying data is authoritative government open data, but confirm anything critical against the official Corporations Canada search.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- federalcorporation.ca
tags:
- companies-finance
- corporate-registry
- canada
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# FederalCorporation

> A searchable, free reindex of Corporations Canada open data — federal company records with director names, addresses, and the ability to trace one director across multiple corporations.

## When to use
You have a person's `name` or a Canadian company (`employer-org`) and want to establish or trace corporate ties: which federal corporations a director is attached to, a company's registered office `address`, its status and incorporation date, and other corporations sharing the same director. The same-director cross-links are the strongest OSINT payload — they surface `associate` and business-network relationships from a single name. Federal scope only (provincial incorporations need the relevant province's registry).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://federalcorporation.ca/.
2. Search by corporation name, corporation/business number, city/postal code, or **director name**.
3. Open a corporation profile: legal name, status, incorporation date, registered office `address`, directors (with addresses), and filing history.
4. From a director profile, use "other corporations with the same director" to walk the network.
5. Pivot: director addresses → people-search/address tools; linked corporations → build an org chart; confirm high-stakes facts on the official Corporations Canada search.

## Inputs → Outputs
- **In:** `name` (director) or `employer-org` / corporation number / city
- **Out:** corporation legal name/status, registered office `address`, director names+addresses (`associate`), linked corporations (`employer-org`)
- **Empty/negative result looks like:** no matching corporation/director — the entity may be provincially (not federally) incorporated, dissolved before the data snapshot, or named differently; absence here isn't proof of no company.

## Gotchas & OpSec
- Federal-only: provincial corporations (most small businesses) won't appear — use the province's registry for those.
- OpSec: fully passive; querying a public registry mirror.
- It's a third-party reindex; data can lag the official source — verify critical records on Corporations Canada directly.

## Overlaps ("do both")
- Complements provincial registry lookups and international company tools — run those in parallel when a subject's business footprint may be provincial or cross-border.

## Trust & verifiability
`trust: community` — reindex of authoritative government open data; the data is official but the site is third-party, so confirm decisive facts against Corporations Canada.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federalcorporation |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, associate, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
