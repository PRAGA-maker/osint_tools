---
id: osint-industries
name: OSINT Industries
description: Use when you have an email, phone, username, or crypto wallet and want to enumerate linked accounts and breach/footprint data across 100s of platforms — returns social profiles, registration timestamps, and partial PII.
url: https://www.osint.industries/
category: email
path:
- email
- email-search
bestFor: Reverse email/phone/username enrichment — which platforms an identifier is registered on, plus breach and timeline data.
selectorsIn:
- email
- phone
- username
- crypto-wallet
selectorsOut:
- social-profile
- name
- username
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Credit/subscription based. Limited free trial; full reports and bulk/API use require payment.
opsec: passive
opsecNote: Scours public sites and databases without contacting the target; account enumeration is done server-side. Searches are tied to your account.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: OSINT Industries is a well-known commercial enrichment platform widely used by investigators and recommended in OSINT framework lists. Coverage is real but results are leads to corroborate.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- osint-rocks
- nymeria-io
- pipl
aliases:
- osint.industries
tags:
- email
- email-search
source: arf-seed
lastVerified: ''
enrichment: full
---

# OSINT Industries

> Commercial reverse-lookup engine that maps an email/phone/username/wallet to the accounts, breaches, and timeline behind it across hundreds of platforms.

## When to use
You have one strong selector — an `email`, `phone`, `username`, or `crypto-wallet` — and want to know every platform it's registered on plus any breach exposure, registration dates, and partial PII. Excellent early pivot when you have a contact point but little identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://www.osint.industries/ (trial credits or a paid plan).
2. Choose the selector type and enter the identifier.
3. Run the search; review the module results — each linked platform, account creation date, and any leaked attributes.
4. Pivot discovered `social-profile` / `username` to a deeper sweep (`[[osint-rocks]]`) and `name` to people search (`[[pipl]]`).

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, `crypto-wallet`
- **Out:** `social-profile`, `name`, `username`, `geolocation`, `metadata-exif` (registration timestamps, breach metadata)
- **Empty/negative result looks like:** few or no modules return hits — common for fresh or rarely-used identifiers.

## Gotchas & OpSec
- Human-in-the-loop: account login and a paywall beyond trial credits.
- Module hits indicate an account exists, not that profile data is current — corroborate.
- OpSec: passive against the subject; queries logged to your account. Use a dedicated investigative account.

## Overlaps ("do both")
- Pairs with `[[osint-rocks]]` (free open-source account checks) to cross-validate, and `[[nymeria-io]]`/`[[pipl]]` for identity/contact resolution.

## Trust & verifiability
`trust: community` — established, widely-used commercial tool; treat each module result as a verifiable lead (it usually links to the source platform).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-industries |
| category | email |
| selectorsIn → selectorsOut | email, phone, username, crypto-wallet → social-profile, name, username, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
