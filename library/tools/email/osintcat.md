---
id: osintcat
name: OsintCat
description: Use when you have an email, username, phone, or name and want to search aggregated breach/leak datasets for exposed credentials and linked PII — returns names, passwords-leaked-from, and linked accounts.
url: https://www.osintcat.net/
category: email
path:
- email
bestFor: Breach/leak search-engine lookups by email, username, phone, or name.
selectorsIn:
- email
- username
- phone
- name
selectorsOut:
- name
- social-profile
- username
- phone
- address
status: unknown
pricing: freemium
costNote: Breach search engines like this typically use credits/subscriptions for full record reveals; pricing unconfirmed.
opsec: passive
opsecNote: Server-side query of aggregated breach datasets; no contact with the subject. Queries tied to your account on a third-party broker.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: OsintCat (osintcat.net) is listed as a data-breach search engine in awesome-osint. It surfaces real leaked data but is an unvetted broker; accuracy and provenance vary.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- osintcat.net
tags:
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# OsintCat

> A breach/leak search engine — query an identifier against aggregated data dumps to surface leaked credentials and linked PII; unvetted, treat as leads.

## When to use
You have an `email`, `username`, `phone`, or `name` and want to know if it appears in known breaches and what PII (linked emails, passwords-leaked-from, addresses) was exposed — useful to confirm an identity is real and active.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.osintcat.net/ and register / sign in.
2. Select the selector type and enter the value.
3. Review matched breach records — note source breach and date.
4. Corroborate any returned PII independently; pivot usernames to `[[osint-rocks]]`.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`, `name`
- **Out:** `name`, `social-profile`, `username`, `phone`, `address`
- **Empty/negative result looks like:** no breach hits — identifier absent from indexed datasets.

## Gotchas & OpSec
- Human-in-the-loop: account login and likely paywall for full reveals.
- Breach data can be stale or mis-attributed; reused usernames are pivots, not proof.
- OpSec: passive against the subject; you trust a third-party broker. Use a dedicated account; mind legal/ethical limits.

## Overlaps ("do both")
- Cross-check against `[[osint-lolarchiver-com-2]]` (another breach DB) and `[[osint-industries]]` (footprint + breach modules).

## Trust & verifiability
`trust: unverified` — unvetted breach search engine; corroborate every record independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintcat |
| category | email |
| selectorsIn → selectorsOut | email, username, phone, name → name, social-profile, username, phone, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
