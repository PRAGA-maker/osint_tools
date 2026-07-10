---
id: solocheck-ie
name: solocheck.ie
description: Use when you have an Irish company `name` or a director's `name` and want company profiles, directors and addresses — returns `employer-org`, `address`, `associate` (directors).
url: https://www.solocheck.ie/
category: public-records
path:
- public-records
bestFor: Irish company and director research — profiles, directorships, addresses and credit reports.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Free to start searching every Irish company and its directors (basic profile); full credit reports, financials and individual screening are paid.
opsec: passive
opsecNote: Passive — data derives from the Irish companies register (CRO) and consumer registries; the company/directors are not notified. Paid reports need an account and payment (a trail on your side) — use a sock-puppet account if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established Irish business-information reseller sourcing from official CRO filings; registry data is authoritative, the credit/analytics layer is SoloCheck's own.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- SoloCheck
- solocheck.ie
tags:
- companysites
- Company Related Sites
- ireland
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# solocheck.ie

> Ireland's go-to business-lookup site: search an Irish company or a director and get the profile, directorships, address and (paid) credit detail.

## When to use
You have an Irish company `name`, or a person's `name` you want to check for Irish directorships, and need the corporate picture: company status, registered `address`, and the directors/co-directors (`associate` leads). The people-to-companies angle is the OSINT value — mapping which Irish businesses a subject is tied to and who they run them with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.solocheck.ie/ and search a company `name` or a director's `name`.
2. Read the free profile: company status, registered `address`, incorporation detail, and director listing.
3. Follow a director to see their other Irish directorships and co-directors (`associate` pivots).
4. For financials, credit scores, or individual screening, buy the paid report (use a puppet account).
5. Pivot: cross-check people on the CRO directly; run non-Irish entities through `[[info-clipper-com]]`; UK links through `[[companycheck-co-uk]]`.

## Inputs → Outputs
- **In:** Irish company `name` or director `name`
- **Out:** `employer-org` profile, registered `address`, `associate` (directors/co-directors), status/filing detail
- **Empty/negative result looks like:** no match, or a bare profile with detail locked behind payment — the person holds no Irish directorships, or you need the paid report. Ireland-only.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — basic search is free; credit/financial detail is paid.
- OpSec: **passive** to the target; paying leaves a billing trail — sock-puppet it.
- Reseller of CRO data: verify critical director/ownership facts against the official CRO register.

## Overlaps ("do both")
- Pairs with `[[info-clipper-com]]` (global) and `[[companycheck-co-uk]]` (UK) — SoloCheck owns the Irish angle; the others extend geography.

## Trust & verifiability
`trust: community` — reputable Irish business-data reseller over authoritative CRO filings. Confirm key facts against the CRO; treat credit analytics as secondary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | solocheck-ie |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
