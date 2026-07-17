---
id: oec-world
name: OEC World
description: Use when you have an `employer-org` (a company or trade entity) or a country/product and want international trade-flow context — returns import/export relationships and named trading companies.
url: https://oec.world/
category: public-records
path:
- public-records
bestFor: Mapping international trade flows and identifying companies importing/exporting specific products.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Core visualizations and country/product trade data are free; company-level trade records ("Company Data" / trade shipments) and bulk data sit behind paid Pro tiers.
opsec: passive
opsecNote: Browsing macro trade data and profiles is read-only and anonymous to any subject. OEC (the vendor) sees your account/IP if you register for Pro; the free visualizations need no login.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running MIT Media Lab spin-off (Datawheel) using official UN Comtrade / national customs data; macro figures are authoritative, company-level records are third-party aggregated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- import-yeti
- panjiva
- opencorporates
aliases:
- Observatory of Economic Complexity
- oec.world
tags:
- Company information search
- trade
- import-export
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# OEC World

> The Observatory of Economic Complexity: interactive visualizations of who trades what with whom, useful for placing a company or country's imports/exports in context and surfacing trading partners.

## When to use
You are investigating an `employer-org` involved in international trade — an import/export business, a shell company that ships goods, a manufacturer — and you want to understand its trade context: what products flow between which countries, and (via the paid company data) which named firms import or export a given product. It's a macro-to-micro pivot: start from a product/country flow, then drill toward the specific companies (`associate` links) participating in it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://oec.world/ and search a country, product (HS code), or company.
2. For macro context, open a country or product profile to see top trading partners, product mix, and trade-value trends — good for corroborating that a claimed trade relationship is plausible.
3. For company-level leads, use the trade-shipment / company data features (Pro) to find firms tied to a product flow; the free tier shows aggregate flows only.
4. Use the API (`https://oec.world/en/resources/data/api`) for structured pulls of the free datasets.
5. Pivot: a named trading company feeds corporate-registry tools (`[[opencorporates]]`) and, from there, directors/owners.

## Inputs → Outputs
- **In:** `employer-org` (company / trade entity), or a country + product
- **Out:** `employer-org` (trading partners/firms), `associate` (trade relationships), import/export values and trends
- **Empty/negative result looks like:** a country/product with negligible trade in that category, or a company not present in the (paid) shipment records — absence here is not proof the entity doesn't trade, only that OEC's dataset doesn't cover it.

## Gotchas & OpSec
- The free tier is macro (country/product) data; individual-company shipment records require a paid plan — don't assume you can name specific importers for free.
- Trade data lags (customs reporting delays of months to a year); it establishes long-run relationships, not what shipped last week.
- OpSec: **passive** — purely reading published economic data; no subject interaction.

## Overlaps ("do both")
- Pairs with `[[import-yeti]]` and `[[panjiva]]` (bill-of-lading / shipment databases that name specific companies) — OEC gives the macro picture while those name the individual importers/exporters, so use them together.

## Trust & verifiability
`trust: trusted` — built by Datawheel (MIT Media Lab origin) on official UN Comtrade and national customs data; macro figures are authoritative and traceable to source, though aggregated company records warrant a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oec-world |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
