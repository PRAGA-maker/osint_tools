---
id: vat-search-co-uk
name: vat-search.co.uk
description: Use when you have an `employer-org` name or a VAT number and want to verify it and pull the registered business details — returns company name, registered address, and VAT status across 90+ countries.
url: https://vat-search.co.uk/
category: public-records
path:
- public-records
bestFor: Verifying a VAT number and resolving it to a registered company name and address.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Basic VAT number lookup/verification is free to use; bulk lookups, API access, and advanced features are paid (the site has pricing tiers and a login). Author against the free single-lookup layer.
opsec: passive
opsecNote: Passive — you query a VAT-registry aggregator (backed by official VIES/HMRC data), not the business owner. The subject is not notified. A login is only needed for paid/bulk use; single lookups need none.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial VAT-verification aggregator (600+ enterprise clients) that sits on top of official EU VIES / national VAT databases; the underlying registry data is authoritative, the aggregation layer is third-party.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- vat-search.co.uk
- VAT Search
tags:
- companysites
- Company Related Sites
- vat-lookup
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# vat-search.co.uk

> A VAT-number lookup and verification service across 90+ countries — turn a VAT ID or company name into a verified registered business name and address.

## When to use
You have a business identifier — a VAT number, an `employer-org` name, or a trading `address` — tied to a subject (their company, employer, or a business they're linked to) and you want to confirm it's a real, registered entity and resolve it to an official name and registered address. In people work this matters when a subject operates through a company: the VAT record ties a business to a real registered address and legal name you can pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vat-search.co.uk/ in a browser.
2. Enter the VAT number (or search by company `name`) and pick the country.
3. Read the result: registered company `name`, registered `address`, and current VAT validity/status (data sourced from official EU VIES / national VAT registries).
4. For UK/EU, cross-check against the primary source (HMRC VAT checker, EU VIES) for anything you'll rely on.
5. Pivot: the registered address and legal name feed company-registry lookups (Companies House) and people-search; directors named there become new `associate` leads.

## Inputs → Outputs
- **In:** VAT number, `employer-org` name, or `address`
- **Out:** verified company `name`, registered `address`, VAT validity/status
- **Empty/negative result looks like:** "invalid" / "not found" for a VAT number (either mistyped, deregistered, or never valid) — an invalid VAT ID is itself a signal. A name search may return many similarly-named entities; disambiguate by country and address.

## Gotchas & OpSec
- Free for single lookups; bulk/API and some advanced features are paywalled behind an account.
- It's an aggregator — for evidentiary use, confirm against the official VIES (EU) or HMRC (UK) checker, which are the systems of record.
- VAT data covers the business, not the individual directly — use it as a bridge to company-registry and director data, not as personal identification on its own.
- Passive; nothing reaches the business or its owners.

## Overlaps ("do both")
- Pairs with `[[ifa-org-uk]]` and other UK company/professional registries — VAT verifies the trading entity; those add regulated-status and membership detail.
- Feed the registered address/name into people-search and Companies House to reach directors (`associate`s).

## Trust & verifiability
`trust: community` — a third-party aggregation layer over authoritative government VAT registries. The underlying VAT data is reliable, but for anything decision-critical verify directly on the official EU VIES or national tax-authority checker rather than relying on the aggregator's cached view.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vat-search-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name, address → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
