---
id: cro-ie-2
name: cro.ie (Companies Registration Office Ireland — CORE)
description: Use when you have an `employer-org` or director `name` in Ireland and want company registration, officers, and addresses — returns employer-org, address, and director-name data.
url: https://core.cro.ie/
category: public-records
path:
- public-records
bestFor: Searching Ireland's official company register (CRO/CORE) for companies, business names, directors, and their registered addresses.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: Free basic company/business-name search (name, number, status, registered address, some officer data); full filings and documents (annual returns, officer lists, accounts) are paid per document.
opsec: passive
opsecNote: Official government registry — searching does not notify anyone and reveals only your IP to the CRO. Buying documents requires a CORE account and payment (attributable). The free search is fully passive; use payment hygiene if purchasing filings.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Irish government registry (Companies Registration Office); the authoritative record of Irish companies and business names.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- companies-house
- ebra-be
aliases:
- CRO Ireland
- CORE
- Companies Registration Office
tags:
- professionlicensing
- Profession & Licensing Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# cro.ie (Companies Registration Office Ireland — CORE)

> Ireland's official company register, searchable through the CORE portal — the authoritative source for Irish companies, business names, directors, and registered offices.

## When to use
You have an `employer-org` registered in Ireland, or a `name` you suspect is an Irish company director/secretary, and you want authoritative corporate data: whether the company exists, its status, registered `address`, and officers. Ireland is a common jurisdiction in cross-border corporate tracing, so CORE is the right first-party source. Useful to confirm an employer, place a person on a board (`associate` links to co-directors), or find a registered-office address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://core.cro.ie/ and use the company/business-name search (if a browser challenge appears, complete it).
2. Search by company name, company number, or business name.
3. Read the free result: company name, number, status (normal/dissolved/etc.), company type, and registered `address`; some officer info is shown.
4. For the full picture (current/past directors and secretaries, annual returns, accounts, charges), purchase the relevant document via a CORE account.
5. Pivot: co-directors are `associate` leads; a registered office `address` feeds property/records; a UK-linked entity feeds [[companies-house]].

## Inputs → Outputs
- **In:** `employer-org` (company/business name) or number; a director `name` to match
- **Out:** company registration details, status, registered `address`, director/secretary `name`s (fuller list in paid docs), `associate` officer links
- **Empty/negative result looks like:** no match — the entity may be registered elsewhere, be a sole trader without a registered business name, or be dissolved beyond retention; absence only rules out an Irish registration.

## Gotchas & OpSec
- Republic of Ireland only — Northern Ireland companies are at UK Companies House; pick the right registry.
- The free tier gives summary + registered office; the officer/filing detail that matters most is behind a per-document paywall.
- OpSec: passive — an official register with no notification to anyone.

## Overlaps ("do both")
- Pairs with [[companies-house]] (UK, incl. NI) and [[ebra-be]] (routing to other national registries) — CORE is the authoritative Irish source; use the others for cross-border links.

## Trust & verifiability
`trust: trusted` — first-party Irish government registry. Registration facts are authoritative; individual filings are self-reported by the company but officially lodged.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cro-ie-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
