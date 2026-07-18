---
id: integrated-companies-research-china-hong-kong
name: Integrated Companies Research (Hong Kong ICRIS)
description: Use when you have a `name` or company and want Hong Kong corporate records — searches HK-registered companies by name and directors, returning company particulars.
url: https://www.e-services.cr.gov.hk/
category: public-records
path:
- public-records
bestFor: Searching Hong Kong's official company register by company name or director to confirm registration, status, and directors/officers.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Basic index search (company name/number, directors, status) is free; purchasing full documents (annual returns, incorporation forms with director particulars) charges a per-document fee.
opsec: passive
opsecNote: Passive — you search the official registry; no subject is notified. Buying documents requires an account/payment tied to you; use appropriate separation, and note the registry logs document purchases.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Hong Kong Companies Registry's official Integrated Companies Registration Information System (ICRIS / e-Services); records are authoritative government filings.
missingPersonsRelevance: medium
coverage:
- hk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-hk
aliases:
- ICRIS
- HK Companies Registry
- Cyber Search Centre
- e-services.cr.gov.hk
tags:
- toddington
- company-search
- hong-kong
- corporate-registry
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Integrated Companies Research (Hong Kong ICRIS)

> Hong Kong's official company register — search by company or director to confirm a HK entity's existence, status, and the people behind it, a key node for tracing offshore/HK corporate structures.

## When to use
You have a `name` or `employer-org` linked to Hong Kong and want authoritative corporate records: does the company exist, is it active, who are its directors, and what's its registered address. HK is a common hub for holding companies and offshore structures, so ICRIS is high-value for corporate-ownership tracing, connecting a person to companies, and following director networks to associates. The free index search confirms the basics; paid documents reveal full director particulars.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Companies Registry e-Services / Cyber Search Centre at https://www.e-services.cr.gov.hk/ (ICRIS, formerly icris.cr.gov.hk).
2. Run a free index search by **company name/number** or **director name** to find matching entities.
3. Read the free particulars: company name, registration number, incorporation date, status (active/dissolved), and type.
4. For full detail (directors, shareholders, registered address, filings), purchase the relevant document — annual return or incorporation form — for a per-document fee.
5. Pivot: a director `name` links a person to companies and to co-directors (`associate`); a registered `address` feeds location work; the company feeds cross-registry / offshore-leak tracing.

## Inputs → Outputs
- **In:** a `name` (director) or `employer-org` (company)
- **Out:** company particulars — status, registration number, `address`, and directors/officers (`associate` links); full director data via paid documents
- **Empty/negative result looks like:** no match means no HK-registered company under that name/director — the entity may be registered elsewhere (BVI, mainland China, etc.); check the relevant jurisdiction.

## Gotchas & OpSec
- **Partial paywall:** index/status search is free, but director particulars and filings require paying per document — budget for it when you need the people behind a company.
- HK-only register; offshore structures often chain through BVI/Caymans/mainland — one ICRIS record is a link in a larger chain, not the whole ownership picture.
- Romanization of Chinese names varies — try alternative spellings and the Chinese characters if you have them.

## Overlaps ("do both")
- Pairs with `[[gov-hk]]` and offshore-registry / leak databases (e.g. OpenCorporates, ICIJ) — ICRIS is the authoritative HK layer, and those extend the chain into other jurisdictions and connected entities.

## Trust & verifiability
`trust: trusted` — the official Hong Kong Companies Registry system; records are authoritative government filings, and paid documents are the primary source for director/shareholder detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | integrated-companies-research-china-hong-kong |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
