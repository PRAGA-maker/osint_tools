---
id: cro-ie
name: CRO Ireland (CORE)
description: Use when you have a `name` or company (`employer-org`) in Ireland and want registration, status and directors — returns employer-org, name, address and co-director associate links.
url: https://core.cro.ie/search
category: public-records
path:
- public-records
bestFor: Searching the Irish Companies Registration Office (CRO) for company/business-name registration, status, registered address and director/officer details.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Searching the register and viewing basic company details (name, number, status, registered address) is free. Downloading filed documents (annual returns, director lists, accounts) is pay-per-document (typically a few euro each) via a CORE account.
opsec: passive
opsecNote: You query the official Irish registry, not the subject, so nothing is disclosed to the person. Purchasing documents requires a CORE account/payment, which ties that activity to your registered identity — use a research account for any paid downloads.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Irish government company registrar (Companies Registration Office); registration, status and officer data are authoritative first-party records.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- CRO Ireland
- CORE
- Companies Registration Office Ireland
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# CRO Ireland (CORE)

> The Republic of Ireland's official company registry search — confirm a company's registration, status and registered address, and identify the directors/officers behind it.

## When to use
You have an Irish `name` you think is a company director, or an `employer-org` to verify, and you need authoritative registry facts: does the company exist, is it active or dissolved, what is its registered `address`, and who are its directors and secretary? Director/officer records tie an individual to businesses and to co-directors (`associate`), corroborating identity, business ties and an address for someone whose personal footprint is thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://core.cro.ie/search and search by company/business `name` or number (free).
2. Open the company record for status (Normal/Dissolved), registration date, company type and registered `address`.
3. To see full director/officer lists and filings, purchase the relevant filed documents (annual return / B1) via a CORE account — this step is paid.
4. Extract the company details (`employer-org`), directors (`name`, `associate`) and registered address.
5. Pivot: co-directors become new `name` leads; the registered address feeds property/location work; company number feeds cross-registry checks.

## Inputs → Outputs
- **In:** company/business `name` or number (or a person's `name` to trace as a director via filings)
- **Out:** `employer-org` (company, status, dates), `address` (registered office), `name` + `associate` (directors/officers, from filings)
- **Empty/negative result looks like:** no company matches the name — meaning it isn't CRO-registered under that spelling; the free search is company-keyed, so finding a person usually means starting from a known company and buying the officer filing.

## Gotchas & OpSec
- **Freemium:** the register search and basic details are free, but officer lists/accounts sit inside paid documents.
- Republic of Ireland only — Northern Ireland companies are on the UK Companies House register instead.
- OpSec: passive toward the subject; paid downloads are logged to your CORE account.

## Overlaps ("do both")
- Pairs with `[[solocheck-ie]]` and UK Companies House / `[[bizportal-gov-za]]`-style registries — Solocheck often surfaces Irish director networks more searchably, while CRO is the authoritative primary record.

## Trust & verifiability
`trust: trusted` — first-party Irish government registrar; registration, status and officer data are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cro-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
