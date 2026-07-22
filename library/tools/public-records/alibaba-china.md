---
id: alibaba-china
name: Alibaba.com
description: Use when you have an `employer-org`, product or supplier and want the company behind it — returns `employer-org` profile, `address`, `phone` and trade/verification detail.
url: http://www.alibaba.com
category: public-records
path:
- public-records
bestFor: Identifying and profiling the manufacturer/supplier behind a product, with company address, contacts and trade history.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: freemium
costNote: Free to browse supplier profiles, product listings and company verification badges; buying/messaging requires a free account, and full trade data may be gated.
opsec: passive
opsecNote: Browsing supplier and product pages is passive. Messaging a supplier or requesting a quote is active and attributable — use a sock-puppet buyer account and never your investigation identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The world's largest B2B marketplace; supplier profiles include third-party verification badges, but self-listed company detail can still be inflated or fronted — corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Alibaba
- alibaba.com
tags:
- b2b
- supplier-research
- company-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Alibaba.com

> The world's largest B2B supplier marketplace — a route from a product or brand to the manufacturer/trading company behind it, with company address, contacts and trade footprint.

## When to use
You have a product, a brand, or an `employer-org` and want to identify or profile the supplier/manufacturer. Supplier "company profiles" often list the legal/trading name, factory or office `address`, contact `phone`/person, years in business, staff count, main markets, and verification/assessment badges. Useful for tracing counterfeit or scam-product sources, mapping a business a subject is tied to, or corroborating a company's existence and scale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.alibaba.com and search the product, brand, or `employer-org`.
2. Open a supplier's **company profile** (not just the listing): read business name, location, contact, "Verified Supplier"/assessment status, trade volume and main products.
3. Cross-check the company name/address against the relevant national company registry (e.g. China's credit system, or the supplier's stated country registry).
4. Pivot: an `address`/company name feeds registry and mapping tools; a contact `phone`/person feeds reverse-phone and name research; product images feed reverse-image on other marketplaces.

## Inputs → Outputs
- **In:** `employer-org`, product/brand, or a supplier `name`
- **Out:** `employer-org` profile, `address`, `phone`/contact person, verification status and trade history
- **Empty/negative result looks like:** generic listings with no real company profile, or a "trading company" reseller rather than the actual maker — presence on Alibaba does not confirm a legitimate or accurately-described business.

## Gotchas & OpSec
- Self-listed detail can be inflated or fronted; verification badges reduce but don't eliminate risk — corroborate with registries.
- Many sellers are intermediaries, not the manufacturer — read the business-type field.
- Browsing is passive; contacting a supplier is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with national company registries, reverse-image on product photos, and other B2B directories (Made-in-China, GlobalSources) — cross-listing a supplier confirms identity and exposes aliases.

## Trust & verifiability
`trust: community` — a legitimate, dominant marketplace with some third-party verification, but company profiles are self-listed; treat as strong leads to confirm against official registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alibaba-china |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
