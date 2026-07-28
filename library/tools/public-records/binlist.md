---
id: binlist
name: Binlist
description: Use when you have a payment-card BIN/IIN (first 6–8 digits, a `document-id`) and want the issuing bank, brand, and country — returns employer-org (bank) and geolocation.
url: https://binlist.net
category: public-records
path:
- public-records
bestFor: Resolving a card's first 6–8 digits to its issuing bank, card scheme, type, and country.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public BIN-lookup API/site; rate-limited for anonymous use. No account for basic lookups.
opsec: passive
opsecNote: You look up only the BIN (the first 6–8 digits, which identify the bank, NOT a specific person or account) against a public database — passive and target-invisible. Never submit or store a full card number; the BIN alone is all this needs and all you should handle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: A long-standing community BIN database. Coverage is good for major issuers but not exhaustive or perfectly current; treat bank/country as a strong lead, and note BINs can be reissued.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- wikipedia-list-of-registers
tags:
- corporate
- bin-lookup
- payment-cards
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# Binlist

> A free Bank Identification Number (BIN/IIN) lookup: the first 6–8 digits of a card reveal the issuing bank, scheme (Visa/Mastercard/…), card type, and country.

## When to use
You've encountered a card BIN — in a leaked transaction, a scam payment, a receipt, or breach data — and want to know which bank issued it and in which country. That anchors a financial lead to an institution and geography without touching any personal account. Handle only the BIN, never a full number.

## How to use it (`bestInteractionPattern`: api / web-manual)
1. Take just the first 6–8 digits (the BIN/IIN) of the card.
2. Query `https://lookup.binlist.net/<BIN>` (JSON) or use the site.
3. Read the response: issuing bank/`employer-org`, scheme, card type (debit/credit/prepaid), and issuing country (`geolocation`), sometimes the bank's phone/URL.
4. Discard the digits when done; keep only the resolved bank/country.
5. Pivot: the issuing bank + country → jurisdiction/institution context for a fraud lead; combine with other transaction data to narrow origin.

## Inputs → Outputs
- **In:** a card BIN/IIN (`document-id`, first 6–8 digits only)
- **Out:** `employer-org` (issuing bank), `geolocation` (issuing country), scheme/type
- **Empty/negative result looks like:** BIN not found or partial data — coverage gaps and newly-issued/reassigned BIN ranges happen. A miss doesn't invalidate the card; try another BIN database.

## Gotchas & OpSec
- **BIN ≠ person:** it identifies the *bank*, not the cardholder. It cannot reveal an account holder's identity.
- Never handle or store full card numbers — only the BIN is needed, and only the BIN is safe.
- Database is community-maintained and imperfect; corroborate bank/country for anything critical.

## Overlaps ("do both")
- Cross-check against another BIN database for coverage gaps; combine the resolved issuer with corporate/registry research (`[[wikipedia-list-of-registers]]`) when the bank itself is the lead.

## Trust & verifiability
`trust: community` — a widely-used but unofficial BIN dataset. Reliable enough to attribute a card to a bank/country as a lead; verify with a second source before drawing firm conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | binlist |
| category | public-records |
| selectorsIn → selectorsOut | document-id → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
