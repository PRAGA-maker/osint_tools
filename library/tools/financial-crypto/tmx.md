---
id: tmx
name: TMX / Montréal Exchange (quotes)
description: Use when you have a listed `employer-org`/ticker and want Canadian market quotes and derivatives data from the Montréal Exchange — returns employer-org market data (reference lookup).
url: https://www.m-x.ca/en/trading/data/quotes
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up Montréal Exchange (Bourse de Montréal) quotes and listed derivatives for a Canadian instrument.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Delayed quotes and basic instrument data are free on m-x.ca; real-time and deep market data are paid (TMX data products).
opsec: passive
opsecNote: Browsing public market-data pages is passive and reveals nothing about your subject. Standard site logging of your own visit applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Montréal Exchange (part of TMX Group) is Canada's authoritative derivatives exchange. Market data is official; it is instrument/company-level data, not people data.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- tmx-tsx
- sedar
tags:
- companies-finance
- stock-exchange
- canada
- derivatives
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# TMX / Montréal Exchange (quotes)

> The Montréal Exchange's public quote lookup (TMX Group's derivatives market) — for confirming a Canadian listed instrument's market data and derivatives, as a corroborating reference.

## When to use
Your investigation involves a Canadian public company or a specific listed instrument and you want official exchange quote/derivatives data (e.g. to confirm a company trades, check an instrument a subject referenced, or corroborate a financial claim). This is instrument-level market data, not a people-search — use it to anchor a company lead, then follow filings for the humans.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the m-x.ca quotes page.
2. Enter the ticker/symbol (`employer-org`'s listed symbol) or search the instrument.
3. Read the market data: price/quote (delayed on the free tier), listed options/futures, and instrument details.
4. Note the exchange/instrument facts; for ownership and officers, move to the company's regulatory filings.
5. Pivot: the company/ticker → `[[tmx-tsx]]` listing profile and `[[sedar]]` filings (directors, financials, `associate`s).

## Inputs → Outputs
- **In:** `employer-org` ticker/symbol
- **Out:** `employer-org` market/derivatives data (reference; no personal selectors)
- **Empty/negative result looks like:** no matching symbol — the instrument isn't listed on the Montréal Exchange (may trade on TSX/TSXV or elsewhere). Check the sibling exchanges rather than concluding it doesn't exist.

## Gotchas & OpSec
- Free quotes are **delayed**; real-time/deep data is a paid TMX product.
- Montréal Exchange focuses on derivatives — equity listings live on TSX/TSXV; use the right TMX venue.
- Instrument data only; no people/ownership here — that's in the filings.

## Overlaps ("do both")
- Pairs with `[[tmx-tsx]]` (equity listing directory) and `[[sedar]]` (Canadian securities filings — the people and financials behind the ticker).

## Trust & verifiability
`trust: trusted` — official exchange data from TMX Group. Reliable for market/instrument facts; for anything about people or ownership, rely on the linked regulatory filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tmx |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
