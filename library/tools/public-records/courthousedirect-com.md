---
id: courthousedirect-com
name: CourthouseDirect.com
description: Use when you have a `name` or property identifier and want deeds, liens, real-property and grantor/grantee records (mainly TX/NM, links nationwide) — returns `address`, `document-id` and ownership links.
url: http://www.courthousedirect.com
category: public-records
path:
- public-records
bestFor: Pulling real-property/deed records and grantor-grantee indexes (deeds, mortgages, liens, judgments) to tie a person to property and addresses, strongest in Texas and New Mexico.
selectorsIn:
- name
- address
selectorsOut:
- address
- document-id
- associate
status: live
pricing: freemium
costNote: Registration is free and some index links/searches are free, but full property-record images and "Legal Search" queries are paid per-document or subscription. Treat it as paid-for-documents.
opsec: passive
opsecNote: Property-record search does not alert the subject. Buying documents requires an account and payment, which ties the lookup to your billing identity — use a dedicated investigative account, not a personal one.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial title/records vendor. Data is sourced from county recorders (authoritative underneath) but repackaged and paywalled; confirm critical facts at the county recorder of record.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- courthousedirect
- courthousedirect.com
tags:
- court
- property
- deeds
- public-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# CourthouseDirect.com

> A commercial gateway to county real-property records — deeds, liens, and grantor/grantee indexes — best in Texas and New Mexico, with paid document images and nationwide record links.

## When to use
You have a `name` (or a property `address`/APN) and want to establish what property a person owns or has been party to, and the addresses attached to those records. Deed and lien records reliably tie an individual to a location and often surface co-owners and prior addresses — valuable for locating someone or mapping their associates. Reach for it when property/ownership is the question; for criminal/civil dockets use a court-records tool instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.courthousedirect.com and register a free account (needed for most searches).
2. Choose a search: grantor/grantee name, APN/Tax ID, subdivision/lot/block, or document type + date range.
3. Run the name or property search — free index results list matching documents (parties, dates, doc type).
4. For the full record/image (the deed, lien, mortgage), you'll hit a paid step: purchase the document or use a subscription. Decide whether the free index metadata is enough.
5. Read the record: property `address`, grantor/grantee names (`associate`/prior owners), recording date, `document-id` (instrument number).
6. Pivot: address → people-search/property tools; co-grantors → `associate` mapping; instrument number → county recorder for the authoritative copy.

## Inputs → Outputs
- **In:** `name` (grantor/grantee) or `address`/APN
- **Out:** `address` (property), `document-id` (instrument/recording number), `associate` (co-owners, prior parties), document type and dates
- **Empty/negative result looks like:** no index matches in the covered counties — the person may hold no property there, records may be in a non-covered jurisdiction, or the name is spelled differently. Coverage is deepest in TX/NM; elsewhere it mostly links out to county sites.

## Gotchas & OpSec
- **Paywall:** the searchable index is often free but the actual document images and legal searches cost money. Budget for it or stop at the free metadata.
- Coverage is uneven — strong in Texas/New Mexico, thinner elsewhere where it just forwards to the county recorder.
- OpSec: passive against the subject, but purchases tie the lookup to your payment identity; use an investigative account.

## Overlaps ("do both")
- Pairs with free county recorder sites and `[[os-birth-records]]`-style public-records directories — CourthouseDirect is faster for TX/NM deeds; the county site is authoritative and free.
- Cross-check ownership against a people-search address history to confirm the person is the same individual.

## Trust & verifiability
`trust: unverified` — a commercial reseller of county records. The underlying deeds are authoritative, but pricing, coverage gaps, and repackaging mean you should confirm any decisive record at the originating county recorder.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | courthousedirect-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, document-id, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
