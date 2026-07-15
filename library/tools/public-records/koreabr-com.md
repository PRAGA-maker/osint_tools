---
id: koreabr-com
name: koreabr.com
description: Use when you have a South Korean company or a `name` (CEO) and want to confirm the business and its officers/address — a KoDATA business-credit portal; free search, paid detailed reports.
url: http://www.koreabr.com/mk/MKBRD01R0.do
category: public-records
path:
- public-records
bestFor: Confirming a South Korean company (existence, CEO, registration numbers, address) and finding companies tied to a person's name.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Basic search by company/CEO name is available, but full credit/investigation reports require an account, an order process, and credit-card payment. Treat detailed data as paywalled (payment-wall-partial).
opsec: passive
opsecNote: Searching the business directory is a passive, anonymous lookup against corporate records — nothing reaches any individual. Ordering a paid report requires an account and payment, which attaches your identity to that transaction; use a sock-puppet/company account if that matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by KoDATA, an established Korean business-credit-information agency drawing on official corporate registration data (~7 million companies); an authoritative source for Korean company facts.
missingPersonsRelevance: high
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
aliases:
- KoreaBR
- KoDATA
tags:
- companysites
- Company Related Sites
- south-korea
- business-registry
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# koreabr.com

> KoDATA's KoreaBR — a South Korean business-credit portal over ~7 million companies. Search a company or a CEO name free; pay for the deep credit/investigation report.

## When to use
You have a South Korean `employer-org` (or a person's `name` you suspect is a company officer) and want to confirm the business is real and pull its officers, registration numbers and address. The CEO-name search is the people-relevant angle — it links an individual to the companies they run. English and Chinese interfaces make it usable without Korean.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.koreabr.com/ and use the search: by company name, **CEO name**, Business Registration No., or Corporate Registration No. (filter by region/industry to narrow).
2. Read the free result: matched companies, whether they exist and are active, and headline identifiers.
3. For depth (financials, credit risk, verified status, full officer/address detail), order a report — this requires an account and payment.
4. Pivot: a CEO→company link feeds people-search and further corporate lookups; the registration numbers feed Korea's official registries; the address feeds location work.

## Inputs → Outputs
- **In:** `employer-org` / CEO `name` / registration number / `address` (region)
- **Out:** confirmed `employer-org` (existence, status, IDs), officer `name`(s), business `address`
- **Empty/negative result looks like:** no matching company — meaning it isn't in KoDATA's dataset (dissolved, very new, or mis-spelled), not necessarily that no such business existed. Detailed fields staying hidden usually means you've hit the paid tier, not a data gap.

## Gotchas & OpSec
- **Freemium gate (`payment-wall-partial`):** search/existence is free; the valuable report detail is paid — budget for it or stop at confirmation.
- Transliteration matters — Korean names/companies romanize inconsistently; try variants and the Business Registration No. when known.
- OpSec: search is passive; a paid order attaches your identity — use an appropriate account.

## Overlaps ("do both")
- Pairs with Korea's official corporate registries (DART/FSS, NICE) and other Asian company lookups — KoreaBR is a fast credit-oriented confirm, those give the authoritative filings; cross-check officers and addresses.

## Trust & verifiability
`trust: trusted` — KoDATA is an established Korean business-credit agency working from official registration data. Free search results are reliable for existence/identity; treat any figure only shown in a paid report as needing the report to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | koreabr-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
