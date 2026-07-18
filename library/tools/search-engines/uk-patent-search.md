---
id: uk-patent-search
name: UK Patent Search (GOV.UK / IPO)
description: Use when you have a `name` or `employer-org` and want their UK patents — returns patent filings with inventors, applicants, addresses, and filing dates.
url: https://www.gov.uk/search-for-patent
category: search-engines
path:
- search-engines
bestFor: Searching UK Intellectual Property Office patent records by inventor/applicant name or keyword to tie a person/company to filings.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official government search (UK IPO); no account required.
opsec: passive
opsecNote: You query the UK IPO's public patent system, not any target — invisible to the person/company you're researching. No login; standard research-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The UK government's Intellectual Property Office — the authoritative source for UK patent records. Filing details (names, applicant addresses, dates) come straight from the register.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UK IPO patent search
- gov.uk search for patent
tags:
- toddington
- curated-directory
- specialty-search
- patents
- intellectual-property
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# UK Patent Search (GOV.UK / IPO)

> The UK Intellectual Property Office's official patent search — find UK patent applications and grants by inventor, applicant, or keyword, with the names, addresses, and dates on each filing.

## When to use
Your subject is an inventor, engineer, academic, or business owner, and you want to tie them to intellectual property. A patent filing links a `name` to co-inventors (`associate`s), an applicant `employer-org`, an applicant/agent `address`, and precise dates — corroborating employment, expertise, location, and professional network. Also use it from the company side: find what an `employer-org` has patented and who its inventors are.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gov.uk/search-for-patent — it routes to the IPO's patent search services (Ipsum for published cases, and the patents journal/register).
2. Search by inventor/applicant `name`, company, or keyword; for a known case, look it up by publication/application number.
3. Open a matching record to read: inventors, applicant/proprietor (often an `employer-org`), applicant/agent `address`, filing and publication dates, and legal status.
4. Follow through to the full published specification for technical detail and any additional named parties.
5. Pivot: co-inventors → `associate`s; applicant company → corporate registry (officers, address); applicant address → location/people search; dates → timeline.

## Inputs → Outputs
- **In:** inventor/applicant `name`, `employer-org`, or keyword/number
- **Out:** patent filings with inventor/applicant `name`s, `employer-org`, applicant/agent `address`, dates
- **Empty/negative result looks like:** no matching patents — the person/company has no UK filing (they may have filed elsewhere — try EPO/Espacenet or USPTO), or the name is spelled differently in the record.

## Gotchas & OpSec
- UK-only: for international coverage, pair with Espacenet (EPO) or USPTO/Google Patents — inventors often file in multiple jurisdictions.
- Applicant addresses may be an agent/law firm rather than the inventor's home — verify before treating as a personal address.
- Names on filings can be abbreviated or use an employer as applicant — disambiguate via co-inventors and dates.
- Fully passive and anonymous.

## Overlaps ("do both")
- Complements Espacenet/Google Patents/USPTO for non-UK filings and corporate-registry tools (resolve an applicant company to officers/address) — cross-jurisdiction patent search catches what a single office misses.

## Trust & verifiability
`trust: trusted` — the authoritative UK government IP register; every field traces to the official published patent record, which you can open in full to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-patent-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
