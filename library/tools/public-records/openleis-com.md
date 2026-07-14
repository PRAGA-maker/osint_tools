---
id: openleis-com
name: openleis.com
description: Use when you have a company `name` or partial identifier and want its Legal Entity Identifier, registered legal name, and headquarters `address` — returns employer-org and address details.
url: https://openleis.com/
category: public-records
path:
- public-records
bestFor: Looking up a company's Legal Entity Identifier (LEI) and its officially registered name and address.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free front-end over the open GLEIF LEI dataset; no account or payment required.
opsec: passive
opsecNote: A neutral lookup against a public corporate-registry mirror — you are querying company data, not the subject. No target-side signal. Standard sock-puppet browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party search front-end over GLEIF's authoritative open LEI data; the underlying records are official but the interface is community-run, so confirm anything important against gleif.org.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gleif-org
aliases:
- Open LEIS
- OpenLEI
tags:
- companysites
- Company Related Sites
- lei
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# openleis.com

> A friendly search layer over the global Legal Entity Identifier (LEI) database: turn a company name into its LEI, official legal name, and registered address.

## When to use
You have a company `name`, a partial LEI, or an `employer-org` string tied to your subject (an employer, a shell they control, a director's business) and you want the officially registered legal name and headquarters `address`. LEIs are globally unique 20-character codes assigned to entities that transact in financial markets, so an LEI hit confirms the entity is real and gives you a canonical name/address to pivot on across jurisdictions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://openleis.com/ in a normal browser session.
2. Enter the company `name` (or a known LEI) in the search box and submit.
3. Read the result rows: each shows the entity's legal name, LEI, legal jurisdiction, and registered/headquarters address.
4. Confirm you have the right entity by matching jurisdiction and address to what you already know.
5. Pivot: feed the canonical legal name and address into a national companies registry, or cross-check the LEI at [[gleif-org]] for the authoritative record and any parent/child relationships.

## Inputs → Outputs
- **In:** `name` (company), `employer-org`, or a partial LEI
- **Out:** `employer-org` (canonical legal name + LEI), `address` (registered/HQ), jurisdiction
- **Empty/negative result looks like:** no matching rows — the entity may simply never have obtained an LEI (LEIs are only required for market-facing entities), so absence is not proof the company doesn't exist. Fall back to a national registry.

## Gotchas & OpSec
- Not every company has an LEI — small, non-market-facing businesses often won't appear. A miss here is weak evidence.
- The interface mirrors GLEIF data on a refresh cycle, so a very recently registered LEI may lag; verify time-sensitive facts at the source.
- OpSec: fully passive — you query corporate data, the subject gets no signal.

## Overlaps ("do both")
- Pairs with [[gleif-org]] — GLEIF is the authoritative issuer and exposes parent/child ownership hierarchies this front-end may flatten; use OpenLEIS for a fast name search, then GLEIF to verify and expand relationships.

## Trust & verifiability
`trust: community` — the data originates from GLEIF (authoritative), but this is an independent search front-end. Treat names/addresses as reliable leads and confirm the LEI at gleif.org before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openleis-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name, address → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
