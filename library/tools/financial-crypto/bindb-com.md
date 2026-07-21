---
id: bindb-com
name: bindb.com
description: Use when you have a card BIN/IIN or a UK/Irish bank sort code (`document-id`) from a subject and want to identify the issuing bank, branch and country — returns `employer-org` (the bank) and `geolocation`/country.
url: https://www.bindb.com/sort-codes
category: financial-crypto
path:
- financial-crypto
bestFor: Resolving a card BIN/IIN or a UK/Irish sort code to its issuing bank, branch and country of issue.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: A free online demo/lookup exists; bulk access and the full downloadable database are paid B2B products. The single-lookup demo is enough for investigative use.
opsec: passive
opsecNote: Passive — you query a reference database with a bank identifier, not the subject. Only enter the routing/BIN digits, never a full card/account number, and never a card's full PAN or CVV.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial BIN/sort-code database (marketed for fraud prevention); the free demo's data can lag reissued BIN ranges, so corroborate the bank/country for anything decisive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BinDB
- BIN/IIN lookup
tags:
- banksites
- Banking Related Sites
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# bindb.com

> A card-BIN and UK/Irish sort-code reference — turns a financial routing identifier into the issuing bank, branch and country.

## When to use
You've obtained a partial financial identifier tied to a subject — the first 6–8 digits of a card (the BIN/IIN) from a receipt/screenshot, or a UK/Irish sort code — and want to know which bank issued it, in which country, and (for sort codes) which branch. This corroborates a subject's banking footprint or narrows a country/locality.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bindb.com/ and choose the BIN/IIN lookup or the sort-code database.
2. Enter **only** the BIN (first 6–8 card digits) or the sort code — never a full card/account number.
3. Read the result: issuing bank, card network/type and country (BIN), or bank + branch (sort code).
4. Confirm against the bank's own sort-code/BIN checker for anything you'll act on.
5. Pivot: an identified bank (`employer-org`) and country (`geolocation`) narrow where a subject banks; a branch can anchor a locality.

## Inputs → Outputs
- **In:** a card BIN/IIN or UK/Irish sort code (`document-id`)
- **Out:** issuing bank (`employer-org`), country/branch `geolocation`, card network/type
- **Empty/negative result looks like:** "not found" or a generic issuer — the BIN range is unlisted/reissued; cross-check another BIN database or the bank directly.

## Gotchas & OpSec
- **Never enter a full card number, account number, or CVV** — only the non-sensitive BIN/sort-code prefix.
- Free-demo data can be stale for recently reissued BINs; corroborate.
- Legality: only use financial identifiers you hold lawfully.
- OpSec: passive; the subject is not contacted.

## Overlaps ("do both")
- Pairs with other BIN-lookup services — run the same BIN through a second database, since coverage of newer/prepaid ranges differs.

## Trust & verifiability
`trust: unverified` — a commercial fraud-prevention database; the mapping is generally reliable but the free tier can lag, so verify the bank/country against a primary source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bindb-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
