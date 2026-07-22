---
id: d-and-b-company-search
name: D&B Company Search
description: Use when you have a company `name` and want its D-U-N-S profile — registered address, industry, size, executives and corporate family — returns `employer-org` and `associate` links.
url: https://www.dnb.com
category: public-records
path:
- public-records
bestFor: Looking up a company's D&B business profile (D-U-N-S number, address, industry, key executives, corporate family tree).
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: freemium
costNote: Basic company-directory profiles are free to view; full credit reports, contacts and D&B Hoovers data require a paid subscription.
opsec: passive
opsecNote: Searching D&B's public business directory is passive research against corporate records — the subject/company is not contacted. Full reports require an account, which ties queries to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Dun & Bradstreet is a long-established commercial-data provider whose D-U-N-S numbering is an industry standard for identifying businesses.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Dun & Bradstreet
- DNB company search
- D-U-N-S lookup
tags:
- corporate
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# D&B Company Search

> Dun & Bradstreet's business directory — resolve a company name to its D-U-N-S profile: registered address, industry, size, key people and its place in a corporate family tree.

## When to use
You're building out an entity or following a person through their business ties, and you have a company `name` (or an `employer-org` from another record). D&B gives a normalised business profile — the standard D-U-N-S identifier, headquarters and registered `address`, industry codes, employee/revenue size band, named executives, and parent/subsidiary relationships — which is how you connect an individual to the organisations and other companies (`associate`) around them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.dnb.com and use the business-directory search for the company `name` (add location to disambiguate common names).
2. Open the matching profile to read the free fields: D-U-N-S number, address, industry (SIC/NAICS), size band, and often key principals.
3. Follow the corporate-family links to parents/subsidiaries (`associate`/`employer-org`) to map the group structure.
4. For full contacts, credit and financials, note these are behind D&B's paid products (Hoovers/API).
5. Pivot: the registered `address`, executives, and D-U-N-S feed corporate-registry, sanctions, and people-search tools.

## Inputs → Outputs
- **In:** a company `name` (or `employer-org`)
- **Out:** business profile — D-U-N-S number, registered `address`, industry, size, executives (`associate`), corporate family (`employer-org`)
- **Empty/negative result looks like:** a small, very new, or non-US/EU firm may have a thin or missing profile — absence in D&B doesn't mean the company doesn't exist; check the local corporate registry.

## Gotchas & OpSec
- Freemium: the directory profile is free, but contacts, financials and full family trees require a paid D&B subscription.
- Coverage and freshness are strongest for larger/US firms; small or foreign entities can be stale or absent — corroborate against the official registry.
- OpSec: passive; full-report access is tied to an account.

## Overlaps ("do both")
- Pairs with official corporate registries (e.g. `[[eu-consolidated-corporate-registers]]`) and OpenCorporates — D&B normalises identity and corporate family, while government registries give the authoritative filings and officer records.

## Trust & verifiability
`trust: trusted` — D&B is an industry-standard business-data provider (D-U-N-S is widely used for entity identification); still confirm specifics against primary registry filings for evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | d-and-b-company-search |
