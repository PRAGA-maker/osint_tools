---
id: canadian-patents-database
name: Canadian Patents Database
description: Use when you have an inventor/applicant `name` (or a company) and want their Canadian patents, filing dates, and listed addresses — returns `name`, `address`, `employer-org`.
url: https://www.ic.gc.ca/opic-cipo/cpd/eng/search/basic.html
category: public-records
path:
- public-records
bestFor: Finding a person's or company's Canadian patents, with inventor names, addresses, and assignees.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official CIPO database; full patent documents and bibliographic data are viewable at no cost.
opsec: passive
opsecNote: Searching CIPO does not notify the inventor or assignee; queries are anonymous and no account is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Canadian Intellectual Property Office (CIPO) — the authoritative source for Canadian patent records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-intellectual-property-office
- canadian-trademarks-database
aliases:
- CIPO Patents Database
- Canadian Patent Database
tags:
- patents
- intellectual-property
- company-search
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Patents Database

> CIPO's official patent register — search an inventor or company `name` to surface their Canadian patents, complete with inventor names, addresses, and corporate assignees.

## When to use
Your subject is (or may be) an inventor, engineer, academic, or founder, and you want to tie them to intellectual property in Canada. Patents are unusually rich OSINT: filings list inventor `name`s, often a city/address, the assignee `employer-org`, co-inventors (`associate`), and dates. So a name search can confirm a person's technical field, employer at filing time, collaborators, and a location. Relevant when a missing person has a professional/technical background that might leave a patent trail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ic.gc.ca/opic-cipo/cpd/eng/search/basic.html.
2. Search by inventor/applicant `name`, assignee (company), or keyword; use the advanced form to scope fields precisely.
3. Open a matching patent's bibliographic page: inventors, assignee, filing/grant dates, and listed addresses.
4. Read the output: inventor names and city/address (`name`, `address`), the assignee company (`employer-org`), and co-inventors (`associate`).
5. Pivot: an assignee company feeds corporate-registry tools; co-inventors feed people-search; a listed city narrows geolocation; cross-check the US/EU/WIPO patent databases for the same inventor.

## Inputs → Outputs
- **In:** `name` (inventor/applicant) or `employer-org` (assignee)
- **Out:** `name` (co-inventors), `address` (inventor/assignee address), `employer-org` (assignee company)
- **Empty/negative result looks like:** no patents for the name — the subject may hold none, filed only abroad, or under a name variant; check international patent databases before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none; free and open.
- OpSec: passive and anonymous.
- Addresses reflect the filing date and may be old (an employer address, not a home); treat as a historical lead. Name collisions occur — confirm via field/assignee context.

## Overlaps ("do both")
- Pairs with USPTO/Espacenet/WIPO patent search and `[[canadian-intellectual-property-office]]` — inventors often file in multiple jurisdictions, so run the name across databases to get the full IP trail and reconcile addresses/employers.

## Trust & verifiability
`trust: trusted` — CIPO's official patent database, so the bibliographic records are authoritative primary documents (just remember the listed address is as-of the filing date).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-patents-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
