---
id: tmx-tsx
name: TMX / TSX Listed Company Directory
description: Use when you have an `employer-org` listed (or seeking listing) on the Toronto Stock Exchange and want its official profile — returns employer-org details, domain, associate leads.
url: https://www.tsx.com/listings/listing-with-us/listed-company-directory
category: financial-crypto
path:
- financial-crypto
bestFor: Confirming a company's TSX/TSXV listing and pulling its ticker, sector, and official profile.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- domain
- associate
status: live
pricing: freemium
costNote: The directory and basic company profiles are free on tsx.com; deep market data/filings may sit behind TMX paid products or the separate SEDAR+ filings system.
opsec: passive
opsecNote: Browsing a public stock-exchange directory is passive and reveals nothing about your subject. Standard site logging of your own visit applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by TMX Group, the operator of the Toronto Stock Exchange (TSX) and TSX Venture Exchange — an authoritative source for which companies are listed. Corporate detail beyond listing status comes from the company/regulatory filings.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- opencorporates
- sedar
- wikipedia-list-of-registers
tags:
- companies-finance
- stock-exchange
- canada
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# TMX / TSX Listed Company Directory

> The Toronto Stock Exchange's official directory of listed companies — the authoritative check for whether a Canadian company is publicly traded, and the gateway to its ticker and profile.

## When to use
Your subject is tied to a company that is (or claims to be) listed on the TSX or TSX Venture Exchange. Confirm the listing, get the ticker and sector, and use it as the anchor for pulling the company's regulatory filings (where directors, officers, and ownership are disclosed).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the TSX Listed Company Directory.
2. Search by company name (`employer-org`) or browse by sector/exchange (TSX vs TSXV).
3. Open the company entry: ticker symbol, exchange, sector, and official company link (`domain`).
4. For people/ownership, follow through to the company's regulatory filings (management circulars, annual reports) via SEDAR+.
5. Pivot: the ticker/name → `[[sedar]]` filings for directors/officers (`associate`); the official `domain` → website/staff research; cross-jurisdiction via `[[opencorporates]]`.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** `employer-org` listing details (ticker, sector, exchange), official `domain`, and a path to `associate` (officers/directors via filings)
- **Empty/negative result looks like:** not found — the company isn't listed on TSX/TSXV (may be private, delisted, or listed elsewhere). Check other exchanges/registries rather than concluding it doesn't exist.

## Gotchas & OpSec
- The directory confirms listing and basic profile; director/officer detail lives in the filings system (SEDAR+), not here.
- TSX vs TSX Venture are different tiers — note which one; venture listings are smaller/earlier-stage.
- Passive; only public data.

## Overlaps ("do both")
- Pairs with `[[sedar]]` (Canadian securities filings — the people and financials) and `[[opencorporates]]`; use this to confirm the listing, those to get the humans behind it.

## Trust & verifiability
`trust: trusted` — the exchange operator's own directory, authoritative for listing status. Corporate/ownership specifics should be taken from the linked regulatory filings, not inferred from the directory alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tmx-tsx |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org → employer-org, domain, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
