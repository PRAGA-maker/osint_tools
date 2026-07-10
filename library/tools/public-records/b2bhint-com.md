---
id: b2bhint-com
name: b2bhint.com
description: Use when you have an `employer-org` or officer `name` and want company data across 190 countries — returns company details, current/former directors (`name`), registered `address`, beneficial owners, and affiliated `associate` entities.
url: https://b2bhint.com/en
category: public-records
path:
- public-records
bestFor: Global company registry aggregator — search a company or person across official registers in 190 countries for officers, ownership, and links.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Free to search and see core company/officer data; full financials, bulk access, and the API are behind paid plans / registration.
opsec: passive
opsecNote: You query aggregated official-register data, not the subject — no notification. A free account/registration unlocks more; use a research account and stay within a lawful (due-diligence/KYC) basis, as this is personal and corporate data.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates directly from official government registers, commercial registries, and court/financial databases (no third-party scraping), refreshed frequently — reliable, with normal caveats about register completeness.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
aliases:
- B2BHint
- b2bhint
tags:
- companysites
- Company Related Sites
- corporate-registry
- global
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# b2bhint.com

> A global company-registry search — one interface over official registers in 190 countries, returning officers, ownership, addresses, and corporate links.

## When to use
You have an `employer-org` or an officer/director `name` and need cross-border corporate intelligence: who runs a company, its registered address and status, its beneficial owners, and its parent/subsidiary/affiliate web — across almost any jurisdiction. Ideal for tracing a subject's company footprint internationally without visiting each country's registry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://b2bhint.com/en.
2. Search by company name/number (`employer-org`) or by officer `name`, optionally filtered by country.
3. Read the company record: registration details, status, legal form, registered `address`, and current/former directors/officers with appointment dates.
4. Follow ownership: shareholders, beneficial owners, parent/subsidiary and affiliated `associate` entities.
5. Pivot: officer names → people-search and other registries; shared officers/addresses across companies → network mapping; register a free account for deeper data.

## Inputs → Outputs
- **In:** `employer-org` (name/number) or officer `name` (+ optional country)
- **Out:** `employer-org` details, directors/officers (`name`), registered `address`, beneficial owners, affiliated `associate` entities, and (paid) financials/litigation
- **Empty/negative result looks like:** no match — the entity/person isn't in the covered registers, or the name/spelling differs (try local-language forms). Coverage varies by country's register openness; absence is jurisdiction-dependent.

## Gotchas & OpSec
- Full financials/litigation and bulk/API access are paid; core search is free.
- Register completeness varies by country — a thin result may reflect that jurisdiction's disclosure, not reality.
- Corporate + personal data — use for a lawful due-diligence purpose.

## Overlaps ("do both")
- Pairs with OpenCorporates, `[[companieshouse-gi]]`, `[[croatia]]` (UBO), and national registries — B2BHint is the fast global entry point; national registries give the authoritative source filings behind it.

## Trust & verifiability
`trust: trusted` — sourced directly from official registers and refreshed often; reliable, but confirm critical facts against the underlying national registry, and remember listed directors may be nominees.
