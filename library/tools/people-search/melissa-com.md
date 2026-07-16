---
id: melissa-com
name: melissa.com
url: https://www.melissa.com/v2/lookups/personatorsearch/
category: people-search
path:
- people-search
description: Use when you have a US `name`, `email`, `phone` or `address` fragment and want verified, cross-linked contact data — returns matched `address`, `phone`, `email` and demographics.
bestFor: Verifying and enriching a US identity — matching a name/address/phone/email to a confirmed contact record via Melissa's Personator engine.
selectorsIn:
- name
- address
- phone
- email
selectorsOut:
- address
- phone
- email
- dob
status: live
pricing: freemium
costNote: Registration grants ~1,000 free credits; each detailed lookup spends credits, so heavy or full-data use is effectively paid. Basic demo lookups are limited.
opsec: active
opsecNote: You must register a business/account and the queries hit Melissa's servers with the target's selectors; the lookup is logged to your account. The subject is not notified. Register with a sock-puppet identity and treat credit usage as attributable to you.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Melissa is an established data-quality/identity-verification vendor whose contact and address data is used commercially for verification, so records are relatively authoritative for the US.
missingPersonsRelevance: high
coverage:
- us
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Melissa Personator
- Melissa Data lookups
tags:
- peoplesearch
- People Search Sites
- identity-verification
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- address-check-1-2-united-states
- melissa-us-2
- melissadata
---

# melissa.com

> Melissa's Personator identity/contact-verification engine — feed it any fragment (name, address, phone, email) and it matches, verifies and cross-links to a confirmed contact record.

## When to use
You have a partial or unverified US identity — a name plus city, an email, a phone, or a half-address — and want to resolve it to a verified, cross-referenced contact record (standardised address, phone, email, demographics including DOB/DOD). Strong as a *verification/enrichment* step: it confirms whether a claimed identity is real and consistent, not just a broad scrape.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at melissa.com to obtain free credits, then open the Personator search (https://www.melissa.com/v2/lookups/personatorsearch/).
2. Enter any single or combined input: `name`, `address`, `phone`, `email`, or ZIP.
3. Run the match and review the returned record: standardised address, phone, email deliverability, and demographic fields; pick the best match when several appear.
4. Note credit consumption — reserve detailed lookups for genuine leads.
5. Pivot: a verified `address`/`phone` feeds directory and property searches; a validated `email` feeds breach/account-existence checks.

## Inputs → Outputs
- **In:** `name`, `address`, `phone`, or `email` (any combination)
- **Out:** verified `address`, `phone`, `email`, `dob` (and DOD/demographics)
- **Empty/negative result looks like:** "no match" or a low-confidence result — meaning the fragment doesn't resolve to a verified record, which itself is a signal the identity may be fabricated or out-of-coverage.

## Gotchas & OpSec
- It is credit-metered: free credits run out, and full data effectively costs money.
- Best treated as verification/enrichment of a known lead, not open-ended people discovery.
- OpSec: **active** — requires an account and logs your queries; use a sock-puppet registration. No subject notification.

## Overlaps ("do both")
- Pairs with `[[switchboard]]`/`[[411-ca]]` directory lookups — those surface candidate records cheaply, while Melissa verifies and standardises the winner.

## Trust & verifiability
`trust: trusted` — Melissa's data underpins commercial address/identity verification, so matched records are relatively authoritative for the US; still confirm high-stakes facts against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | melissa-com |
| category | people-search |
| selectorsIn → selectorsOut | name, address, phone, email → address, phone, email, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
