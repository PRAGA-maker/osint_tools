---
id: osint-lolarchiver-com
name: osint.lolarchiver.com
description: Use when you have an email, username, or phone and want to pull linked records and leaked data from an aggregated breach/OSINT index — returns names, accounts, and partial PII (paid, verify).
url: https://osint.lolarchiver.com/
category: email
path:
- email
bestFor: Aggregated breach/leak and OSINT lookups by email, username, or phone.
selectorsIn:
- email
- username
- phone
selectorsOut:
- name
- social-profile
- username
- phone
- address
status: unknown
pricing: freemium
costNote: lolarchiver-style services are typically credit/subscription based for full results; pricing unconfirmed.
opsec: passive
opsecNote: Queries an aggregated leak/OSINT index server-side; no contact with the subject. Your queries are tied to your account on a third-party data broker.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: lolarchiver presents as a breach/leak aggregation service. Such tools surface real leaked data but provenance, legality, and accuracy vary; operator is not an established/audited vendor.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- lolarchiver
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# osint.lolarchiver.com

> An aggregated breach/leak lookup portal that resolves an email/username/phone into leaked records and linked accounts — useful but unvetted; treat data as leads.

## When to use
You have an `email`, `username`, or `phone` and want to check it against aggregated breach/leak corpora for linked `name`, `address`, accounts, and other PII the subject may have exposed in old breaches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.lolarchiver.com/ and register / sign in.
2. Select the identifier type and enter the value.
3. Review returned leaked records — note the source breach and date where shown.
4. Corroborate any PII against an independent source before acting.
5. Pivot discovered accounts to `[[osint-rocks]]` and `name`/`address` to people search.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`
- **Out:** `name`, `social-profile`, `username`, `phone`, `address`
- **Empty/negative result looks like:** no records / "not found" — the identifier isn't in the indexed leaks.

## Gotchas & OpSec
- Human-in-the-loop: account login and likely a paywall for full records.
- Leaked data can be stale or mis-attributed — always corroborate.
- OpSec: passive against the subject, but you are trusting a third-party broker with your queries; use a dedicated account and consider legal/ethical limits on breach data.

## Overlaps ("do both")
- See `[[osint-lolarchiver-com-2]]` (the same site's database_lookup view) and `[[osintcat]]` for an alternative breach search.

## Trust & verifiability
`trust: unverified` — unvetted breach aggregator; real leaks but inconsistent provenance. Confirm everything independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-lolarchiver-com |
| category | email |
| selectorsIn → selectorsOut | email, username, phone → name, social-profile, username, phone, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
