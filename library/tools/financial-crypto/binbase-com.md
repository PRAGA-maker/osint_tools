---
id: binbase-com
name: BinBase
description: Use when you have a payment-card BIN (`document-id`, the first 6–8 digits) and want to identify the issuer — returns the issuing `employer-org` (bank), card type, and `geolocation` (country).
url: https://www.binbase.com/search.html
category: financial-crypto
path:
- financial-crypto
bestFor: Identifying the issuing bank, brand, card type, and country behind a credit/debit-card BIN.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: A free single-BIN web lookup is available; bulk/database and API access are paid.
opsec: passive
opsecNote: You look up an anonymous 6–8 digit issuer prefix, not a full card number, against BinBase's own database — nothing touches the cardholder or bank. Never enter a full card number here; the BIN alone is what identifies the issuer.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running commercial BIN database; issuer mappings are generally accurate but self-maintained, so confirm anything decisive against a second BIN source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bin-base
aliases:
- binbase.com
- BIN lookup
tags:
- banksites
- Banking Related Sites
- bin-lookup
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# BinBase

> A Bank Identification Number (BIN) lookup — feed it the first 6–8 digits of a payment card and it tells you which bank issued it, the card brand/type, and the country.

## When to use
You've encountered a partial card number in evidence — a leaked receipt, a breach record, a redacted statement showing only the BIN, a screenshot — and want to attribute it: which bank issued the card and in what country. That narrows a subject's banking relationship and likely country of residence, and can corroborate or contradict a claimed identity. Only the leading digits (the BIN) are needed and useful; the rest of the number is irrelevant to issuer identification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.binbase.com/search.html.
2. Enter the **BIN only** — the first 6 (or 8) digits of the card. Do not paste a full card number.
3. Read the result: issuing bank (`employer-org`), card brand (Visa/Mastercard/Amex), card type (credit/debit/prepaid), and issuing country (`geolocation`).
4. For many BINs, cross-check against a second free BIN database to confirm (issuer data drifts as banks merge/reissue).
5. Pivot: the issuing bank + country tightens the subject's geographic and financial profile; feed the country into location-based records work.

## Inputs → Outputs
- **In:** a card BIN (`document-id`, first 6–8 digits)
- **Out:** issuing bank (`employer-org`), card brand/type, issuing country (`geolocation`)
- **Empty/negative result looks like:** "not found" or a blank issuer — the BIN isn't in the database (newer/rarer ranges), or you entered too few digits; try 8 digits and a second source.

## Gotchas & OpSec
- **Enter the BIN only** — never a full card number. The BIN is non-sensitive issuer routing info; a full PAN is not.
- Issuer data can be stale after bank mergers/reissues; confirm decisive attributions against another BIN tool.
- Bulk/API is paid; the free web form is one lookup at a time.

## Overlaps ("do both")
- Pairs with `[[bin-base]]` (sibling BIN service) and other free BIN lookups — cross-checking two databases catches stale or wrong issuer mappings.

## Trust & verifiability
`trust: unverified` — a real, actively-updated commercial BIN database, but issuer mappings are self-maintained; treat a single lookup as a lead and confirm anything critical with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | binbase-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
