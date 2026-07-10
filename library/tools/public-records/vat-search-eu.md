---
id: vat-search-eu
name: vat-search.eu
description: Use when you have an EU company `name` or VAT number and want to validate/resolve it — returns the VAT-registered business `name`, `address`, and VAT status across EU member states.
url: https://vat-search.eu/
category: public-records
path:
- public-records
bestFor: Searching and validating EU VAT numbers and resolving them to a registered business name and address.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Free basic VAT-number validation and lookup (backed by the EU's VIES system and public company data); bulk/API and some detailed data are paid. No account needed for single lookups.
opsec: passive
opsecNote: Validating a VAT number is passive and does not notify the business. You disclose the query to a third-party aggregator; use a sock-puppet browser. For an authoritative check, cross-verify on the EU's official VIES service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator over the EU VIES validation system and public company registers; results are generally reliable for validation, but confirm critical facts against official VIES/national registries.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- gov-uk
- b2bhint-com
aliases:
- VAT Search EU
- vat-search.eu
tags:
- companysites
- Company Related Sites
- vat
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# vat-search.eu

> A search-and-validate front end for EU VAT numbers — confirm a VAT ID is real and resolve it (or a company name) to the registered business and address across EU member states.

## When to use
You are tracing an EU `employer-org`: you have a VAT number to validate (is it real, whose is it?) or a company `name` to find the VAT-registered entity and address behind it. Confirming VAT registration corroborates that a trader is genuine, resolves the entity behind an invoice/website, and can expose a fabricated VAT ID in a fraud/pretext scenario.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vat-search.eu/ and enter an EU VAT number or a company `name`/country.
2. Read the result: validity, the registered business `name`, and `address`.
3. For an authoritative validation, re-check the number on the EU's official VIES service (vat-search.eu aggregates over it).
4. Note member-state coverage differences — some countries expose more detail than others.
5. Pivot: the resolved company/address feeds national company-registry lookups; for UK VAT use `[[gov-uk]]`; enrich the entity via `[[b2bhint-com]]`.

## Inputs → Outputs
- **In:** EU VAT number (`employer-org` identifier) or company `name` + country
- **Out:** VAT validity/status, registered business `name`, `address`
- **Empty/negative result looks like:** "invalid / not found" — the number is unregistered, mistyped, non-EU, or the member state limits disclosure; a name-to-VAT mismatch is a red flag worth chasing.

## Gotchas & OpSec
- EU scheme only — non-EU (e.g. UK post-Brexit) numbers won't validate here; use the right national tool.
- Detail exposed varies by member state; some return only validity, not name/address.
- It's an aggregator — confirm authoritative validity via official VIES for anything decision-critical.
- OpSec: passive; the business isn't notified.

## Overlaps ("do both")
- Pairs with `[[gov-uk]]` (UK VAT) and `[[b2bhint-com]]` (company enrichment) — validate the VAT here, then resolve directors/filings via national registries.

## Trust & verifiability
`trust: community` — a reliable aggregator over EU VIES and public registers, but a third party. Treat validations as strong and confirm anything critical against official VIES/national registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vat-search-eu |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
