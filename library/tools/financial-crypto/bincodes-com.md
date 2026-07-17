---
id: bincodes-com
name: bincodes.com
description: Use when you have the first 6–8 digits (BIN/IIN) of a payment card and want to identify the issuing bank, card brand, type, and country — returns issuer `employer-org` and card country `geolocation`.
url: https://www.bincodes.com/creditcard-checker/
category: financial-crypto
path:
- financial-crypto
bestFor: Looking up the issuing bank, brand, level, and country behind a card's BIN/IIN prefix.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: The web BIN/card checker is free to use with no account. A separate paid API with pricing tiers exists for programmatic/bulk access.
opsec: passive
opsecNote: You only submit the BIN (first 6–8 digits), never a full card number, and the query goes to bincodes' own database — nothing reaches the cardholder or bank. Never enter a complete card number into any web tool. Only enter a BIN you are lawfully entitled to research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial BIN-database site; the operators state the data is "accurate but not perfect." Treat issuer/country as a strong lead, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- bincodes BIN checker
- bincodes credit card checker
tags:
- banksites
- Banking Related Sites
- bin-lookup
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# bincodes.com

> A free BIN/IIN lookup: paste the first six-to-eight digits of a card number and learn which bank issued it, the brand, level, and country.

## When to use
You have a partial card number — the BIN/IIN prefix (first 6–8 digits) surfaced from a receipt, a leaked/breach record, or a transaction — and want to attribute it to an issuing bank, card network (Visa/Mastercard/Amex/etc.), card level, and issuing country. In an investigation this corroborates which financial institution and country a subject's card belongs to, narrowing geography or confirming a claimed bank relationship.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bincodes.com/creditcard-checker/.
2. Enter only the BIN/IIN — the first 6 (sometimes 8) digits. Do **not** enter a full card number.
3. Submit and read the result: issuing bank, brand, card type/level, and country.
4. Pivot: the issuing bank (`employer-org`) and country (`geolocation`) narrow where a subject banks; cross-check against other financial or geographic signals.

## Inputs → Outputs
- **In:** a card BIN/IIN prefix (`document-id`).
- **Out:** issuing bank (`employer-org`), card brand/type/level, issuing country (`geolocation`).
- **Empty/negative result looks like:** "BIN not found" or a blank issuer — the prefix isn't in their database (newer or niche issuers), not proof the card is invalid.

## Gotchas & OpSec
- The database is self-described as accurate but imperfect; a wrong or stale issuer is possible — corroborate before relying on it.
- Only a BIN identifies an *institution*, never a *person* or an account — do not overstate what it proves.
- Legal/ethical gate: only research BINs you have a lawful basis to look at; never enter full card numbers anywhere.

## Overlaps ("do both")
- Cross-check the same BIN against a second free BIN database — coverage of smaller issuers varies, and disagreement flags a stale record.

## Trust & verifiability
`trust: community` — a commercial BIN-database operator with broad but imperfect coverage. Useful for issuer/country attribution as a lead; verify anything decision-critical against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bincodes-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
