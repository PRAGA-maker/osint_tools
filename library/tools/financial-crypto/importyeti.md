---
id: importyeti
name: ImportYeti
description: Use when you have a company `name`/`employer-org` and want its overseas suppliers and shipment history from US customs data — returns supplier orgs and business `associate`s.
url: https://www.importyeti.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Mapping a company's suppliers, buyers and trade relationships from 60M+ US customs sea-shipment (bill-of-lading) records.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to search the core US import shipment data; some advanced features/exports are paid.
opsec: passive
opsecNote: You search a public customs dataset, not the company — nothing is sent to the subject. Basic search works without an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built on official US Customs bill-of-lading records (the same source as Panjiva/ImportGenius); the underlying data is government-sourced and reliable, aggregation caveats aside.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Import Yeti
- importyeti.com
tags:
- bellingcat-toolkit
- companies-finance
- trade-data
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# ImportYeti

> A free search over 60M+ US customs sea-shipment records — enter a company and see who it buys from and ships to overseas, exposing supply-chain relationships.

## When to use
You're investigating a business (or a person behind one) and want to map its real-world trade ties: which foreign manufacturers supply it, which US firms import a given supplier's goods, and how those relationships change over time. US import bill-of-lading data is public, and ImportYeti makes it searchable by `employer-org`/`name`, turning shipment records into a supplier/customer network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.importyeti.com/ and search the company `name`/`employer-org`.
2. Read its shipment profile: overseas suppliers, product descriptions, shipment counts and dates.
3. Click a supplier to pivot to *its* other US customers (`associate`/`employer-org`) — revealing competitors and shared sourcing.
4. Note volumes/dates to gauge the significance and recency of a relationship.
5. Pivot: supplier/customer org names feed corporate-registry (`[[eu-consolidated-corporate-registers]]`, OpenCorporates) and sanctions checks.

## Inputs → Outputs
- **In:** a company `name`/`employer-org` (importer or supplier)
- **Out:** suppliers/customers (`employer-org`), product/shipment records, and connected businesses (`associate`)
- **Empty/negative result looks like:** a company with no US sea imports (services firm, air-freight only, or non-US trade) returns little or nothing — the dataset is US ocean freight, so absence isn't proof of no trade.

## Gotchas & OpSec
- Scope is **US import sea-shipment** bill-of-lading data — air freight, purely domestic, and non-US trade won't appear; some shippers file to keep records confidential.
- Company-name matching can be noisy (subsidiaries, spellings) — confirm you have the right entity.
- OpSec: fully passive against public customs data.

## Overlaps ("do both")
- Pairs with corporate registries and other trade-data tools (Panjiva/ImportGenius) — ImportYeti is free and fast for suppliers; registries confirm legal entity/ownership behind the trade names.

## Trust & verifiability
`trust: trusted` — sourced from official US Customs records; individual shipment lines are government data you can corroborate, though aggregation/name-matching warrants a second look.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | importyeti |
