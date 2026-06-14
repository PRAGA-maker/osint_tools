---
id: credenshow
name: CredenShow
description: Use when you have an email, username, phone, or domain and want to search aggregated breach/credential datasets — returns matching leaked records and associated identity fields.
url: https://credenshow.com/
category: email
path:
- email
bestFor: Breach/credential search across an aggregated leak corpus for selector expansion.
selectorsIn:
- email
- username
- phone
- domain
selectorsOut:
- email
- username
- name
- phone
status: unknown
pricing: freemium
costNote: Listed as a data-breach search engine; meaningful results and API access are typically paid.
opsec: passive
opsecNote: You search about a third party; the subject is not contacted. Operator logs queries — use a sock-puppet browser context.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Appears on the awesome-osint list as a data-breach search engine, but its corpus, provenance, and freshness are not independently verified. Treat any hit as a lead to confirm, and validate the live status before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- data-breach-search-engines
- breach-data
source: awesome-osint
lastVerified: ''
enrichment: full
---

# CredenShow

> A data-breach search engine (per awesome-osint) for finding a selector across aggregated credential leaks.

## When to use
You have an `email`, `username`, `phone`, or `domain` for a missing person or associate and want to find linked leaked records — surfacing alternate emails, usernames, names, or phone numbers that pivot to other accounts. Use as a complement to better-known aggregators, not a sole source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and enter the selector in the search field.
2. Submit and review returned breach records; deeper detail and API access are typically gated behind payment.
3. Pivot: a recovered alternate `email`/`username`/`phone` feeds account-discovery, username-search, and phone-lookup tools.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`, or `domain`
- **Out:** breach records with associated `email` / `username` / `name` / `phone`
- **Empty/negative result looks like:** no records — the selector is absent from *this* corpus only; confirm against another aggregator.

## Gotchas & OpSec
- Lesser-known engine — verify it is live and reputable before paying or trusting results; corpus provenance is unaudited.
- Human-in-the-loop: expect a partial paywall for full detail.
- OpSec: passive toward the subject; operator logs searches, so use a clean/sock-puppet session.

## Overlaps ("do both")
- Pair with `[[dehashed]]`, `[[checkleaked-cc]]`, and `[[breachdirectory-org]]`: each indexes a different set, so combine to reduce misses.

## Trust & verifiability
`trust: unverified` — listed by a community directory but not independently corroborated. Treat hits as leads requiring confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | credenshow |
| category | email |
| selectorsIn → selectorsOut | email, username, phone, domain → email, username, name, phone |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
