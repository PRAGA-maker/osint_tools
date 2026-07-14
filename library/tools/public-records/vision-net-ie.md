---
id: vision-net-ie
name: Vision-Net (Irish Company & Director Info)
description: Use when you have an Irish company or a director's name and want registry-sourced records — returns company filings, director details and linked directorships.
url: https://www.vision-net.ie/index.jsp
category: public-records
path:
- public-records
bestFor: Researching Irish companies and directors — official registry reports, director profiles and their other directorships.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Free to search and see basic company/director listings; full registry reports, documents, financials and credit data are paid (per-report or subscription). Operated by CRIF, a third-party reseller of Irish CRO registry data.
opsec: passive
opsecNote: Querying a company-data service is passive and does not alert the subject. Buying reports needs an account/payment, identifying you to CRIF. Use lawful public-record scope; VPN for sensitive lookups.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CRIF (a major credit/data company) and sourced from the official Irish Companies Registration Office; a reputable reseller of authoritative registry data rather than the CRO itself.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- Vision-Net
- vision-net.ie
- Irish company director search
tags:
- companysites
- Company Related Sites
- corporate-registry
- ireland
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Vision-Net (Irish Company & Director Info)

> A CRIF-run gateway to official Irish CRO company and director data — turn a company or a director's name into filings, addresses and the web of other directorships they hold.

## When to use
You have an Irish `employer-org` (company), or a `name` you believe is a company director/officer in Ireland, and you want registry-grade detail. A director search is the high-value move: it links a person to every Irish company they direct, their listed addresses, and co-directors — building an associate network and confirming identity through corporate roles. Company searches give status, registered address, filings and financials.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vision-net.ie/index.jsp.
2. Choose a **company** search (`employer-org`) or a **director/person** search (`name`).
3. Read the free listing: company status/number, registered `address`, and — for a director — the list of their directorships and co-directors.
4. Purchase the full registry report/documents (account + payment) when you need filings, financials or the officer's full history.
5. Pivot: co-directors (`associate`) feed further person/company searches; a registered address feeds mapping and property records; a company number cross-references the official CRO (core.cro.ie).

## Inputs → Outputs
- **In:** `employer-org` (company name/number), or a director `name`/`address`
- **Out:** `employer-org` records, director `name`s and their linked directorships (`associate`), registered `address`
- **Empty/negative result looks like:** no company/director match. Try spelling variants and the official CRO if Vision-Net's free tier is too thin; absence means no Irish registered entity/role under that term, not that the person doesn't exist.

## Gotchas & OpSec
- **Freemium:** listings and director links are visible free, but the substantive reports/documents/financials are paid.
- It is a reseller of CRO data — authoritative source, but for court-usable proof consider the official CRO (core.cro.ie) directly.
- Covers *registered legal entities and their officers* — you find individuals via their corporate roles, not as private residents.
- Passive; buying a report identifies you to CRIF.

## Overlaps ("do both")
- Pairs with the official Irish CRO (core.cro.ie) — Vision-Net adds director-network views and credit intelligence on top of the same registry data.
- Cross-jurisdiction, pairs with `[[lithuania]]`-style and UK Companies House searches when a director operates across borders.

## Trust & verifiability
`trust: trusted` — CRIF-operated and sourced from the official Irish CRO, so the underlying records are authoritative; verify anything critical against the CRO directly, and treat CRIF's added credit/ESG scoring as commentary, not registry fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vision-net-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
