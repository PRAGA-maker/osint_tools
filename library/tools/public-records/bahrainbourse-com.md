---
id: bahrainbourse-com
name: bahrainbourse.com
description: Use when you have a Bahrain-listed `employer-org` and want official market data and corporate disclosures — returns company quotes, announcements, AGM/dividend actions, and disclosed officer/ownership detail.
url: https://bahrainbourse.com/en/pages/companies.aspx
category: public-records
path:
- public-records
bestFor: Bahrain Bourse listed-company data — quotes, corporate announcements, and disclosures for entities on the Bahrain stock exchange.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public market-data portal (prices delayed ~15 minutes); no account needed to view listings and announcements.
opsec: passive
opsecNote: A public stock-exchange information site — you view market/company data, nothing reaches any subject. No login; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Bahrain Bourse (stock exchange) site; listing and disclosure data is authoritative for exchange-listed entities.
missingPersonsRelevance: low
coverage:
- bh
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bahrain Bourse
- bahrainbourse
tags:
- companysites
- Company Related Sites
- stock-exchange
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# bahrainbourse.com

> The official Bahrain stock exchange site — listed-company quotes, corporate announcements, and disclosures for entities trading on Bahrain Bourse.

## When to use
You have a Bahrain-listed company (`employer-org`) and want official market and disclosure data: share price/quotes, corporate announcements, AGM and dividend actions, and — via disclosures — board/major-shareholder detail. Useful for corporate due diligence and linking a subject to a Bahrain-listed entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bahrainbourse.com/en/pages/companies.aspx and navigate to the Markets/Quotes and Company Announcements sections.
2. Find the listed company by name (`employer-org`).
3. Read its quote, corporate announcements, AGM/dividend notices, and any published disclosures.
4. Open disclosure documents for board members, major shareholders, and financials where provided.
5. Pivot: officer/shareholder `name`s → people-search and other Gulf registries; announcements → timeline of corporate events.

## Inputs → Outputs
- **In:** `employer-org` (Bahrain-listed company)
- **Out:** `employer-org` market data (quotes, announcements, AGM/dividends) and disclosed `name`s (officers/major shareholders)
- **Empty/negative result looks like:** company not found — it isn't listed on Bahrain Bourse (private, or listed elsewhere). Only *listed* entities appear here; private Bahraini companies are in the commercial registry (MOIC), not this site.

## Gotchas & OpSec
- Covers **exchange-listed** companies only — private companies are elsewhere (Bahrain MOIC/Sijilat).
- Prices are delayed ~15 minutes; it's an information portal, not a trading terminal.
- Person-level detail is limited to what disclosures reveal (boards, major holders).

## Overlaps ("do both")
- Pairs with Bahrain's commercial registry (Sijilat/MOIC) and Gulf company databases — the bourse covers listed entities and disclosures, the registry covers private companies and directors.

## Trust & verifiability
`trust: trusted` — the official exchange; listing/disclosure data is authoritative for listed entities. Corroborate any person-level inference against the underlying disclosure documents.
