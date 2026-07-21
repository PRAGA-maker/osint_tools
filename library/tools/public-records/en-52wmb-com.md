---
id: en-52wmb-com
name: 52WMB (Global Trade Data)
description: Use when you have an `employer-org` and want its import/export trade footprint — returns trading `associate`s (buyers/suppliers), `address` and shipment context.
url: https://en.52wmb.com
category: public-records
path:
- public-records
bestFor: Profiling a company's international trade activity — who it buys from and sells to — via customs/bill-of-lading data.
selectorsIn:
- employer-org
selectorsOut:
- associate
- address
status: live
pricing: freemium
costNote: Homepage samples and limited results are free; deep search (full buyer/supplier lists, detailed shipment records) requires a paid membership tier.
opsec: passive
opsecNote: You search a public trade-data portal about a company, not a person; the target company is not notified. Registration is only needed for deeper results — use a sock-puppet email/identity if you register, and avoid entering real details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial Chinese trade-intelligence aggregator compiling customs/bill-of-lading data from many countries; useful for leads but data provenance and freshness are not independently auditable.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- 52wmb
- en.52wmb.com
- Worldmarketbase
tags:
- Tender/shipment information search
- trade-data
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# 52WMB (Global Trade Data)

> A trade-intelligence aggregator that indexes customs / bill-of-lading records — search a company and see its international buyers, suppliers and shipments.

## When to use
You have an `employer-org` (a company a subject owns, works for, or is linked to) and want to understand its real-world commercial activity: which foreign firms it trades with, what goods it moves (by HS code), and where its counterparties are. This maps a business's network and can surface an owner/operator's other ventures — useful in due-diligence, fraud, and sanctions-adjacent work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.52wmb.com and search by company name, product name, or HS (Harmonized System) commodity code.
2. Read the free sample results: counterparties, countries, and shipment counts appear in preview form.
3. To pull full buyer/supplier lists and detailed shipment records you must register (sock-puppet identity) and, for the richest data, hold a paid membership — stop at the free tier if that suffices.
4. Note counterparty company names, countries, and any addresses/ports.
5. Pivot: counterparty company names feed business-registry lookups; a foreign supplier/buyer maps the org's network; HS codes reveal what the business actually does.

## Inputs → Outputs
- **In:** `employer-org` (company / product / HS code)
- **Out:** `associate` (trading partners — buyers/suppliers), `address` (company/port locations), shipment/commodity context
- **Empty/negative result looks like:** no records for the company — it may not trade internationally, may trade under a different legal name, or its shipments may not be in the indexed customs sources. Absence is not proof of no trade.

## Gotchas & OpSec
- Freemium: the most useful detail sits behind registration and paid tiers — plan around the free preview.
- Data is scraped/aggregated from third-party customs sources; treat counterparties and volumes as leads to corroborate, not confirmed fact.
- Company-focused — it will not find a person directly, only the businesses they are attached to. Passive from the target's view.

## Overlaps ("do both")
- Pairs with other bill-of-lading/trade-data tools (e.g. ImportYeti-style services) and business registries — cross-check counterparties across sources, since each indexes different customs feeds.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with opaque sourcing; strong for generating leads about a company's trade network, but confirm specific counterparties and shipments against an official customs or registry source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | en-52wmb-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → associate, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
