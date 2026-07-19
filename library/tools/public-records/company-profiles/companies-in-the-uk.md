---
id: companies-in-the-uk
name: Companies In The UK
description: Use when you have a UK company `name` or number and want a quick profile — returns employer-org details, registered address and officer/context from Companies House data.
url: https://www.companiesintheuk.co.uk/
category: public-records
path:
- public-records
- company-profiles
bestFor: A fast, readable UK company lookup (status, registered address, SIC codes, officers) built on Companies House data.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free to search and view company profiles; no account required.
opsec: passive
opsecNote: A third-party front-end over public Companies House data; queries hit its servers, not the subject. Passive, no login, no notification.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party reformatter of official Companies House data — convenient, but for authoritative/current filings confirm against the official Companies House register.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- companiesintheuk.co.uk
tags:
- company-search
- uk
- companies-house
- business-registry
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Companies In The UK

> A quick, readable front-end over UK Companies House data — search a company name or number for its status, registered address, SIC codes and officers without navigating the official register.

## When to use
You have a UK company `name` or registration number tied to your subject — a business they run, direct, or list as an employer — and want a fast profile: is it active/dissolved, where is it registered (`address`), what does it do (SIC codes), and who are its officers (`name`s to pivot on). It reformats Companies House data into an easy view; for anything you'll rely on, confirm against the official register.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.companiesintheuk.co.uk/ and search the company `name` or number.
2. Open the profile: company status, incorporation date, registered `address`, SIC/industry codes, and officers/directors where shown.
3. Note the company number, then verify current details on the official Companies House register (and pull full filings/PSC data there).
4. Pivot: director `name`s → their other UK appointments (Companies House officer search); registered address → co-located companies; SIC → sector context.

## Inputs → Outputs
- **In:** UK company `name` or registration number (`employer-org`)
- **Out:** company `employer-org` profile — status, registered `address`, SIC codes, officer `name`s
- **Empty/negative result looks like:** no match or a stale entry — the company is dissolved/renamed or the third-party mirror lags; check the official Companies House register directly.

## Gotchas & OpSec
- Third-party mirror — can be out of date relative to live Companies House filings; treat as a convenience view, verify officially.
- Registered address is often an accountant/agent address, not a home.
- UK only.
- OpSec: passive; you touch a public-data site, not the subject.

## Overlaps ("do both")
- Pairs with the official Companies House register and OpenCorporates — this gives a quick read; those give authoritative, current filings, PSC (beneficial owner) data, and full officer histories.

## Trust & verifiability
`trust: community` — a helpful reformatter of official data, but not itself authoritative; always confirm consequential facts on the official Companies House register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | companies-in-the-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
