---
id: search-our-ppp-loan-database
name: Search Our PPP Loan Database
description: Use when you have a business `name`, an `address`/area, or a person tied to a company and want their US PPP loan record — returns loan amount, employer-org, location and dates.
url: https://ppp.directory/search
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up US Paycheck Protection Program (PPP) loans by business name/location to tie a person to a company, an address, and a dollar amount.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free, public SBA-sourced data; no account.
opsec: passive
opsecNote: You search a public database of government-disclosed loan records — no subject is contacted or alerted. Standard third-party site logging only; use a clean browser if you don't want the search tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates public SBA PPP disclosures; the underlying data is official government data, but confirm decisive details against the SBA's own release.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- PPP loan lookup
- ppp.directory
tags:
- ppp
- sba
- business-records
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Search Our PPP Loan Database

> A searchable front end to the SBA's public PPP-loan disclosures — connect a person to a business, a business to an address and a loan amount, and a company to its industry.

## When to use
You have a US business `name`, an `address`/area, or a person you believe ran/owned a small business, and want financial-footprint corroboration: did they take a Paycheck Protection Program loan, for how much, at what address, in what industry, and when. It's strong for tying an individual to a company and a physical location during 2020–2021, and for confirming a business actually operated.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ppp.directory/search.
2. Search by business `name`; narrow with filters for city/county/state, ZIP, NAICS/industry, loan amount, or lender.
3. Read each result row: loan amount, business name, location, jobs retained, approval date, and NAICS industry.
4. Pivot: the business address/name feeds corporate-registry and people-search tools; the industry and amount corroborate a subject's claimed occupation or means.

## Inputs → Outputs
- **In:** business `name`, `address`/location, or a person-linked company
- **Out:** `employer-org` (business), `address` (location), loan amount, dates, industry; often an owner/`name`
- **Empty/negative result looks like:** no matching loan — the business didn't take PPP, operated under a different legal name, or is spelled differently; try name variants before concluding absence.

## Gotchas & OpSec
- Data is a 2020–2021 snapshot of the PPP program — it won't reflect businesses formed after, and small sole-proprietor records vary in detail.
- Name matching is fuzzy in practice; try DBA/legal-name variants and cross-check the address to confirm you have the right entity.
- OpSec: **passive** — public government-sourced data; nothing reaches any subject.

## Overlaps ("do both")
- Do both with the SBA's own PPP data release and a corporate-registry search: ppp.directory is fast to query, the SBA release is authoritative, and the registry ties the business to named officers.

## Trust & verifiability
`trust: community` — a convenient front end over official SBA PPP disclosures. The source data is government-published; confirm anything decisive against the SBA's own dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-our-ppp-loan-database |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
