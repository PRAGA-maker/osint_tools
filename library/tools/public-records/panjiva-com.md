---
id: panjiva-com
name: Panjiva
description: Use when you have a company `name`/`employer-org` in trade and want its import/export shipments — returns bill-of-lading records naming suppliers, buyers, and goods.
url: https://panjiva.com/
category: public-records
path:
- public-records
bestFor: Searching global trade/shipment (bill-of-lading) data to map a company's suppliers, buyers, and shipping activity.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: freemium
costNote: Freemium — limited free search/preview of shipment records; full records, history, and analytics require a paid S&P Global Panjiva subscription.
opsec: passive
opsecNote: Searching trade data is passive — it queries shipment records, not the subject, and notifies no one. Registering for the free tier identifies you to S&P Global; use a business persona.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Owned by S&P Global; shipment data is sourced from customs bill-of-lading records — authoritative for the trade it documents, though coverage varies by country.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- panjiva-cargo
aliases:
- Panjiva.com
- S&P Global Panjiva
tags:
- Tender/shipment information search
- trade-data
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Panjiva

> A trade-intelligence platform over customs bill-of-lading data — search a company to see who it ships to and from, what goods move, and the addresses behind the trade.

## When to use
Your subject is tied to a business that imports/exports, and you want to map its trade relationships: suppliers, buyers, shipment volumes, goods, and the addresses on customs records. Panjiva turns bill-of-lading data into a supply-chain graph — useful for corporate due diligence, sanctions/evasion research, and connecting companies (and the people behind them) through their trade. Low direct missing-persons value; strong for business/associate mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (business-persona) account for the free tier at panjiva.com.
2. Search the company `name`/`employer-org`.
3. Review the free preview: counterpart companies (suppliers/buyers as `associate` entities), goods, shipment counts, and addresses on the records.
4. For full history/analytics, a paid S&P Global subscription is required — decide if warranted.
5. Pivot: counterpart companies and their `address`es feed corporate and people research; a trade relationship corroborates a business connection your investigation suspected.

## Inputs → Outputs
- **In:** company `name`/`employer-org`
- **Out:** shipment records exposing trade counterparts (`associate` companies), goods, and `address`es
- **Empty/negative result looks like:** no shipments — the company doesn't appear in covered customs data (many countries/services aren't covered, and domestic-only firms won't show), or the name differs.

## Gotchas & OpSec
- Paywall: the free tier previews; full records/history need a paid subscription.
- Coverage is customs-dependent — strong for US import data, patchier elsewhere; absence isn't proof of no trade.
- It maps companies, not individuals — pivot to registries for the people.
- OpSec: passive search; registration identifies you.

## Overlaps ("do both")
- Pairs with corporate registries (`[[lei-search]]`, OpenCorporates) and other trade-data tools — Panjiva reveals the trade relationships; registries name the humans and confirm the entities.

## Trust & verifiability
`trust: trusted` — S&P Global-owned, sourced from customs records; authoritative for documented shipments, subject to country coverage gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | panjiva-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
