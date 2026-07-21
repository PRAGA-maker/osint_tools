---
id: european-trademark-search
name: European Trademark Search (Trademarkia)
description: Use when you have a brand `name` or `employer-org` and want EU trademark filings — returns the trademark owner `name`/`employer-org` and filing details.
url: https://www.trademarkia.com/ctm/
category: search-engines
path:
- search-engines
bestFor: Free search of European (EU/CTM/EUTM) trademarks by mark or owner to tie a brand to the person/company behind it.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: freemium
costNote: Free trademark and owner search; Trademarkia upsells paid registration/monitoring services, but searching the database is free without an account.
opsec: passive
opsecNote: Searching a public trademark database transmits nothing about your subject; no owner is notified. Fully passive. Use a VPN if you want the search off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Trademarkia is a commercial front-end over official trademark registers (EUIPO for EU marks). Reliable as an index; for legal certainty confirm against the official EUIPO eSearch.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- international-trademark-search
- trademarkia
aliases:
- Trademarkia CTM
- EU trademark search
- EUTM search
tags:
- toddington
- curated-directory
- specialty-search
- trademarks
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# European Trademark Search (Trademarkia)

> A free, searchable front-end to European trademark filings — look up a brand and find the owner (person or company) behind it.

## When to use
You have a brand or product `name`, or an `employer-org`, and want to establish ownership and corporate links in Europe. Trademark filings name the applicant/owner (often a company, sometimes an individual), the representative/agent, filing dates, and goods/services classes. This ties a brand to the entity or person controlling it, reveals a company's product portfolio, and can surface an owner's address or agent as further pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.trademarkia.com/ctm/ and search by the mark (brand name) or use the owner search to find all marks held by a person/company.
2. Open a filing to read the owner name, representative, filing/registration dates, status, and classes (which reveal what the brand covers).
3. Use owner search to enumerate a company's full trademark portfolio — a quick map of its products/sub-brands.
4. For legal-grade confirmation, verify the record against the official EUIPO eSearch plus database.
5. Pivot: an owner company feeds business-registry/Companies House lookups; an individual owner feeds people-search; the agent/representative and address are further leads.

## Inputs → Outputs
- **In:** `name` (mark) or `employer-org` (owner)
- **Out:** `employer-org`/`name` of owner, representative, filing details, goods/services classes
- **Empty/negative result looks like:** no EU trademark matches — the brand may be unregistered, registered only nationally/elsewhere, or filed under a variant spelling. Check national registries and WIPO before concluding no filing exists.

## Gotchas & OpSec
- Trademarkia is a commercial aggregator — for legal certainty, confirm against the official EUIPO register.
- EU-scope here (CTM/EUTM); national marks (e.g. UKIPO) and international (WIPO/Madrid) need their own searches.
- Fully passive — searching leaks nothing to the owner.

## Overlaps ("do both")
- Pairs with `[[international-trademark-search]]` and the official EUIPO/WIPO databases — Trademarkia is a convenient free index; the official registers give authoritative, current records.

## Trust & verifiability
`trust: community` — a reliable commercial index over official EU trademark data; treat filings as accurate leads and confirm anything decisive against the EUIPO source of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | european-trademark-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
