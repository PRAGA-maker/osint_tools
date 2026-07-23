---
id: eu-consolidated-corporate-registers
name: EU consolidated corporate registers
description: Use when you have a company `name` (or a subject's likely `employer-org`) and want to find its official registration across the EU, Iceland, Liechtenstein and Norway — returns company records and linked officers/associates.
url: https://e-justice.europa.eu/content_find_a_company-489-en.do
category: financial-crypto
path:
- financial-crypto
bestFor: Searching the interconnected business registers of all EU member states plus EEA countries from one official portal.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free to search via the EU e-Justice "Find a company" portal (BRIS). Individual national registers may charge for full certified extracts.
opsec: passive
opsecNote: Public official-record search; you query the EU portal, not the subject, so there is no signal to the target. Some national registers log access for certified documents — use the free search for reconnaissance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official EU e-Justice portal (Business Registers Interconnection System) aggregating member-state registers — authoritative primary-source data.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- BRIS
- EU Business Registers Interconnection System
- Find a company e-Justice
tags:
- financial-crypto
- companies-finance
- corporate-registry
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- e-justice-europa-eu
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- european-union-open-data-portal
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
---

# EU consolidated corporate registers

> The EU's official "Find a company" gateway — one search across the interconnected business registers of every member state plus Iceland, Liechtenstein and Norway.

## When to use
You have a company `name` or a subject's suspected `employer-org` / directorship somewhere in the EU/EEA and want the authoritative registration: legal name, registration number, status, registered `address`, and (via the national register) officers and `associate` links. Useful for placing a person in a corporate structure or confirming a business they run.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://e-justice.europa.eu/content_find_a_company-489-en.do and open the "Find a company" search.
2. Choose the country and enter the company `name` (or registration number).
3. Review the register hit: legal name, number, legal form, status, registered address.
4. Follow through to the national register for full detail (officers, filings). Pivot officer `name`s/`associate`s and the registered `address` into people-search and further corporate lookups.

## Inputs → Outputs
- **In:** `employer-org` / company `name` (optionally a country)
- **Out:** `employer-org` record, registered `address`, linked officers/`associate`s
- **Empty/negative result looks like:** no match in the selected country — the company may be registered under a different legal name, in another member state, or be a non-registrable entity; try neighbouring countries and name variants.

## Gotchas & OpSec
- The portal is a search/routing layer; depth of detail (and whether officer names are shown) depends on each national register.
- Certified extracts and some full documents are paid at the national level even though search is free.
- Coverage is EU/EEA only — for UK, US, offshore, etc. use the relevant national registry instead.

## Overlaps ("do both")
- Pairs with `[[e-justice-europa-eu]]` (the broader e-Justice portal) and `[[vat-number-validation]]` — cross-check a company's VAT number and its register entry to confirm you have the right legal entity.

## Trust & verifiability
`trust: trusted` — the official EU e-Justice BRIS portal drawing on member-state registers; data is primary-source, though completeness varies by country.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eu-consolidated-corporate-registers |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
