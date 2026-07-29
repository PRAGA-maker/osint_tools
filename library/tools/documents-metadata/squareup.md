---
id: squareup
name: Square (Squareup)
description: Use when you have a small-business `name`/`employer-org` or a Square receipt/store link and want to confirm a Square payment presence — returns store/receipt details tied to the merchant.
url: https://squareup.com
category: documents-metadata
path:
- documents-metadata
bestFor: Confirming a business uses Square and reading its public Square Online store or receipt pages.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Square is free to sign up for as a merchant; for an investigator it's simply a public store/receipt surface to read — no cost to view public pages.
opsec: passive
opsecNote: Viewing a Square Online store or a shared receipt page is like viewing any website — passive and not notified to the merchant. Do not attempt to make test transactions or contact the seller from an attributable identity; that becomes active and traceable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Square (Block, Inc.) is a first-party mainstream payments provider; public store/receipt pages are authentic to the merchant, though they reveal only what the merchant chose to publish.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Square
- Squareup
- Square Online
tags:
- payments
- small-business
- merchant
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Square (Squareup)

> Square's payments ecosystem, viewed as an OSINT surface: a business's public Square Online store or a shared Square receipt can confirm the merchant, its goods, and sometimes its location.

## When to use
A subject is linked to a small business, market stall, or side hustle and you want to confirm it operates and how. Many such businesses run on Square — a public **Square Online** storefront or a **Square receipt** URL (often shared by email/SMS) can verify the business name, its products/prices, and occasionally a `geolocation`/address or contact. Narrow use; Square itself is a merchant service, not a search engine, so you need a lead (store link or receipt) or the business name to start.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you have a Square Online store URL or a receipt link, open it directly and read the merchant details.
2. If you only have a business `name`, search the web for its Square Online store (`site:square.site` or the business + "square").
3. Read what's public: business name, items, prices, sometimes address/hours/contact.
4. Pivot: an address feeds mapping/business-records tools; note that Square's sibling **Cash App** ($cashtag at cash.app) is the separate surface for personal peer-to-peer lookups.

## Inputs → Outputs
- **In:** `employer-org`/business `name`, or a Square store/receipt link
- **Out:** merchant name, storefront items, and sometimes `geolocation`/contact for the business
- **Empty/negative result looks like:** no Square store found — the business uses a different processor or has no public storefront; not proof the business doesn't exist.

## Gotchas & OpSec
- Square is a payment processor, not a directory — you can't "search Square" for a person; you need a store/receipt lead or find it via web search.
- Reveals only what the merchant published; many Square users have no public storefront at all.
- Don't confuse Square (merchant) with Cash App (personal $cashtags) — different lookups.

## Overlaps ("do both")
- Pairs with business-registry and mapping tools (to corroborate the entity and address) and with Cash App $cashtag lookups for the personal-payments side Square doesn't cover.

## Trust & verifiability
`trust: trusted` — first-party payments provider, so a genuine Square store/receipt is authentic; just remember it shows only the merchant's chosen public details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | squareup |
| category | documents-metadata |
| selectorsIn → selectorsOut | employer-org, name → employer-org, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
