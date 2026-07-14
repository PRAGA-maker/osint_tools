---
id: traderegistry-ae-2
name: traderegistry.ae — Register of Directors
description: Use when you have a UAE company (`employer-org`) or a director's `name` and want official corporate records — returns the directors (name), shareholders/UBO (associate), and registered address.
url: https://traderegistry.ae/product/register-of-directors/
category: public-records
path:
- public-records
bestFor: Ordering official UAE corporate documents (register of directors, shareholders, UBO) to link a person to a UAE company or vice versa.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- associate
- address
- employer-org
status: live
pricing: freemium
costNote: Fee-per-document service — each corporate extract (register of directors, shareholders, UBO, etc.) is purchased individually; there is no free full-data search. Browsing the catalogue is free.
opsec: passive
opsecNote: Ordering a corporate extract does not notify the company's directors, but you must supply payment and often account/identity details to the portal. Use investigative-context payment and account details, and be aware the order is logged by the portal operator.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party "smart portal" that retrieves and resells UAE corporate documents; it is not the official government registry itself (the emirate economic departments / Ministry of Economy are). Verify critical facts against the official registrar where possible.
missingPersonsRelevance: high
coverage:
- ae
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- opencorporates
- uae-national-economic-register
aliases:
- UAE Trade Registry Smart Portal
- traderegistry.ae register of directors
tags:
- companysites
- Company Related Sites
- corporate-records
- uae
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# traderegistry.ae — Register of Directors

> A UAE corporate-documents portal: order an official register of directors, shareholders, or ultimate-beneficial-owner extract to tie a person to a UAE company.

## When to use
Your investigation touches the UAE and you need to connect a person to a company — either you have an `employer-org` (a UAE company name) and want its directors/owners, or you have a director's `name` and want the entities behind them. traderegistry.ae sells official corporate extracts (register of directors, shareholders' details, UBO, corporate documents) that expose the people and the registered address behind a UAE legal entity — data that is otherwise hard to reach from outside the Gulf.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://traderegistry.ae/ and browse the corporate-documents catalogue (register of directors, shareholders, UBO, etc.).
2. Identify the target company/entity and select the extract you need (e.g. "Register of Directors").
3. Register an account and order the document — this is a **paid, per-document** purchase, not a free lookup.
4. Read the delivered extract: directors' names, shareholders and shareholdings, UBO details, and the registered/business address.
5. Pivot: directors' names feed people-search and sanctions/PEP checks; the registered address feeds geolocation; co-directors/shareholders feed `associate` mapping.

## Inputs → Outputs
- **In:** `employer-org` (UAE company) or `name` (director)
- **Out:** `name` (directors), `associate` (shareholders / UBO / co-directors), `address` (registered/business), `employer-org` linkage
- **Empty/negative result looks like:** the entity isn't found in the portal's catalogue, or an ordered extract returns minimal data — the company may be in a free-zone registry not covered here; try the official registrar.

## Gotchas & OpSec
- **Payment wall:** every meaningful record is a paid per-document order; budget accordingly and expect account + payment details to be required.
- This is a **reseller/aggregator**, not the government registry — for legally consequential facts, verify against the official emirate economic department / `[[uae-national-economic-register]]`.
- UAE has many separate registries (mainland + dozens of free zones); a single portal may not cover the entity you need.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (free, broad company-officer index — check there first for a free hit) and `[[uae-national-economic-register]]` (the official UAE government business register). Use the free sources first; buy an extract here only when you need the official document or coverage the free tools lack.

## Trust & verifiability
`trust: unverified` — a third-party portal reselling UAE corporate documents. The documents themselves originate from official registries and are generally reliable, but confirm the operator is delivering genuine official extracts and cross-check key facts against the government registrar.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | traderegistry-ae-2 |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, associate, address, employer-org |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
