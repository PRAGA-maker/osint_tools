---
id: italy
name: Italy (Italian Business Register)
description: Use when you have an Italian `employer-org` or a director's `name` and want official company data — InfoCamere's register returns the company, its directors/proprietors and registered address; free search, paid documents.
url: https://italianbusinessregister.it/
category: public-records
path:
- public-records
bestFor: Confirming an Italian company and its directors/registered office via the official InfoCamere business register.
selectorsIn:
- employer-org
- name
- address
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: "\"Ricerca Imprese Gratuita\" (free company search) is free; detailed reports, filings and financial statements are paid per document by credit card."
opsec: passive
opsecNote: Searching the register is a passive, anonymous lookup against official corporate records — no notification to the company or its officers. Paid document orders attach your payment identity to the request.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The English portal of the official Italian Business Register, operated by InfoCamere SCpA (the Italian Chambers of Commerce network) — an authoritative first-party source, linked to registroimprese.it.
missingPersonsRelevance: high
coverage:
- it
auth: none
api: false
localInstall: false
registration: false
aliases:
- Italian Business Register
- InfoCamere
- Registro Imprese
tags:
- companysites
- Company Related Sites
- italy
- business-registry
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Italy (Italian Business Register)

> InfoCamere's official Italian Business Register (English portal) — confirm an Italian company and pull its directors, proprietors and registered office. Free to search, paid for documents.

## When to use
You have an Italian `employer-org`, or a person's `name` you suspect is an Italian company officer, and want authoritative confirmation: the company's existence and status, its directors/proprietors, and the registered office `address`. The free search alone confirms a business is real and names its principals — a solid anchor for tying an Italian subject to companies and locations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://italianbusinessregister.it/ and use "Ricerca Imprese Gratuita" (free company search) — by company name, or browse to a company to see its officers.
2. Read the free result: company name, status, registered office, and (via the company report) directors/proprietors.
3. For depth — full officer lists, filings, financial statements, ownership — add the document to the cart and pay by card.
4. Pivot: a director `name` feeds people-search and cross-border registers; the registered `address` feeds property/location work; the company feeds sanctions/litigation checks.

## Inputs → Outputs
- **In:** `employer-org` / director `name` / `address`
- **Out:** confirmed `employer-org` (status, IDs), director/proprietor `name`(s), registered `address`
- **Empty/negative result looks like:** no matching company — meaning it isn't registered, is mis-spelled, or (note) is in winding-up/bankruptcy, which the register explicitly excludes. Detail staying hidden usually means you've hit the paid tier, not a data gap.

## Gotchas & OpSec
- **Freemium gate** (`payment-wall-partial`): existence and headline officers are free; comprehensive filings/financials are paid.
- Companies in liquidation/bankruptcy are excluded — absence can mean insolvency proceedings, not non-existence.
- Italian legal names and abbreviations (S.r.l., S.p.A.) matter — try variants.
- OpSec: search is passive; a paid order attaches your identity.

## Overlaps ("do both")
- Pairs with OpenCorporates and EU cross-border registers — InfoCamere is the authoritative primary source; OpenCorporates aids free cross-jurisdiction pivoting and officer-name search.

## Trust & verifiability
`trust: trusted` — the official InfoCamere register. Free-search results are reliable for existence/officers; figures shown only in paid reports need the report to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | italy |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name, address → employer-org, name, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
