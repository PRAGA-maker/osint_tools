---
id: checkleaked-cc
name: checkleaked.cc
description: Use when you have an email, username, password, IP, or domain and want to find it across aggregated breach datasets — returns matching breach records and exposed credential fields.
url: https://checkleaked.cc/check
category: email
path:
- email
bestFor: Multi-selector breach search across a large aggregated leak corpus.
selectorsIn:
- email
- username
- domain
- ip-address
selectorsOut:
- email
- username
- name
- social-profile
status: live
pricing: freemium
costNote: Limited free lookups; deeper results, plaintext password reveal, and API access are paid.
opsec: passive
opsecNote: You search about a third party; the subject is not contacted. Operator logs queries; use a sock-puppet browser context.
humanInLoop: true
humanInLoopReason:
- captcha
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Public breach-search aggregator; corpus provenance and freshness are not independently audited. Treat hits as leads to verify.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CheckLeaked
tags:
- hackedaccounts
- breach-data
source: uk-osint
lastVerified: ''
enrichment: full
---

# checkleaked.cc

> A public breach-search engine that takes several selector types and returns matching leaked records across an aggregated corpus.

## When to use
You have an `email`, `username`, `domain`, or `ip-address` for a missing person or associate and want to find linked leaked records — recovering alternate emails, old usernames, real names, or password hints that pivot to other accounts. Useful for selector expansion early in a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search page and pick the selector type, then enter the value.
2. Solve any CAPTCHA and submit.
3. Read returned breach records and associated fields; free tier shows limited/masked detail, with full reveal behind paid access.
4. Pivot: a recovered alternate `email`/`username` feeds account-discovery and username-search tools; a recovered `name` corroborates identity.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`, or `ip-address`
- **Out:** breach source names, linked `email` / `username` / `name`, sometimes `social-profile` references
- **Empty/negative result looks like:** zero records — meaning the selector is absent from *this* corpus, not breach-free overall. Confirm against another aggregator.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA plus a partial paywall; meaningful detail often requires paying or an API key.
- Finite, undated corpus — a clean result is not exoneration; a hit may be stale.
- OpSec: passive toward the subject; the operator logs your searches, so use a clean/sock-puppet session.

## Overlaps ("do both")
- Pair with `[[dehashed]]` and `[[breachdirectory-org]]`: different corpora, so combine for fewer misses.

## Trust & verifiability
`trust: community` — public aggregator with unaudited provenance. Verify hits against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkleaked-cc |
| category | email |
| selectorsIn → selectorsOut | email, username, domain, ip-address → email, username, name, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
