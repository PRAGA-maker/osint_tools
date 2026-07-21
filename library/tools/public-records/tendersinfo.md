---
id: tendersinfo
name: TendersInfo
description: Use when you have an `employer-org` and want to see the government/private tenders it bids on or wins worldwide — returns procurement listings, buyers, and location leads.
url: https://www.tendersinfo.com
category: public-records
path:
- public-records
bestFor: Global government and private tender/procurement search to link companies to contracts and buyers.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: Free registration and a limited "Free Tenders" section give keyword search; full tender details and history require a paid subscription.
opsec: passive
opsecNote: Searching a procurement aggregator discloses nothing to the subject; it aggregates already-public tender notices.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial tender aggregator (26+ years) republishing public procurement notices; reliable as leads, with fullest detail gated behind subscription.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- TendersInfo
- tendersinfo.com
tags:
- Tender/shipment information search
- procurement
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# TendersInfo

> A worldwide tender and procurement database — 500k+ live government and private tenders across 100+ countries — useful for tying a company to the contracts it chases and the buyers behind them.

## When to use
You're profiling a business (`employer-org`) or a person's company and want its public-sector footprint: which tenders it bids on, wins, or is named in, and which government/private buyers it deals with. Procurement notices name entities, sectors, values, and locations, so tender search can corroborate that a firm is real and active, reveal its geography, and surface counterpart organizations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.tendersinfo.com and register for the free tier.
2. Search by company/`employer-org` name, sector keyword, or country.
3. Read the tender listings: title, buyer, country/region, sector, and deadline.
4. Open the free listings fully; for gated detail (contacts, documents, history), a subscription is required — or pivot to the buyer's own procurement portal.
5. Pivot: a named buyer or awarded firm feeds corporate registries; the tender's `address`/country narrows local records.

## Inputs → Outputs
- **In:** `employer-org` / company name, sector keyword, or country
- **Out:** procurement listings with buyer `employer-org`, sector, deadlines, and location/`address` leads
- **Empty/negative result looks like:** no tenders — the firm may simply not bid on tracked public tenders; absence isn't evidence about a person.

## Gotchas & OpSec
- **Partial paywall:** headline search is free, but full tender details and history need a paid plan — use free official procurement portals where possible.
- Aggregated notices can lag or be summarized; confirm against the issuing authority.
- OpSec: passive; public notices only.

## Overlaps ("do both")
- Pairs with official government procurement portals (TED, SAM.gov, national e-tender sites) and corporate registries — TendersInfo aggregates broadly; the official portals give authoritative, free detail.

## Trust & verifiability
`trust: community` — a commercial aggregator of public procurement notices; treat listings as leads and verify against the original tender authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tendersinfo |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
