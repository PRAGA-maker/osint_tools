---
id: osint-lolarchiver-com-2
name: osint.lolarchiver.com
description: Use when you have an email, username, or phone and want to query lolarchiver's breach/hacked-account database directly — returns leaked credentials and linked records (paid, verify).
url: https://osint.lolarchiver.com/database_lookup
category: email
path:
- email
bestFor: Direct database/breach lookup of hacked-account records by email, username, or phone.
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
costNote: Credit/subscription based for full records; pricing unconfirmed.
opsec: passive
opsecNote: Server-side query of an aggregated breach database; no contact with the subject. Queries are tied to your account on a third-party broker.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: This is the database_lookup / "hacked accounts" view of lolarchiver. Surfaces real leaked credentials but provenance, legality and accuracy vary; operator is unvetted.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- lolarchiver database lookup
tags:
- hackedaccounts
- Hacked / Breached Account Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# osint.lolarchiver.com

> The breach-database lookup view of lolarchiver — query an identifier against hacked-account dumps for leaked credentials and linked PII; unvetted, treat as leads.

## When to use
You have an `email`, `username`, or `phone` and want to check it specifically against compromised/hacked-account databases — useful to confirm an account existed, find reused passwords/usernames, or surface old linked PII.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.lolarchiver.com/database_lookup and sign in.
2. Enter the identifier and run the database lookup.
3. Review hits — source breach, leaked username/password fragments, linked emails/phones.
4. Corroborate any returned PII before acting; pivot usernames to `[[osint-rocks]]`.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`
- **Out:** `name`, `social-profile`, `username`, `phone`, `address`
- **Empty/negative result looks like:** no database hits — identifier absent from the indexed dumps.

## Gotchas & OpSec
- Human-in-the-loop: account login and likely paywall.
- Breach data can be stale/mis-attributed; reused usernames are a strong pivot but not proof of identity.
- OpSec: passive against the subject; you trust a third-party broker with your queries. Use a dedicated account; mind legal/ethical limits on breach data.

## Overlaps ("do both")
- Same site's general view is `[[osint-lolarchiver-com]]`; cross-check breach exposure with `[[osintcat]]`.

## Trust & verifiability
`trust: unverified` — unvetted breach/hacked-account aggregator; corroborate every result independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-lolarchiver-com-2 |
| category | email |
| selectorsIn → selectorsOut | email, username, phone → name, social-profile, username, phone, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
