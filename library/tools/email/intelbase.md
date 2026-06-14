---
id: intelbase
name: IntelBase
description: Use when you have an email, username, or domain and want to check it against aggregated breach/leak databases — returns linked credentials and identifiers.
url: https://intelbase.is/
category: email
path:
- email
bestFor: Searching aggregated breach/leak data by email, username, or domain.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- password
- domain
status: unknown
pricing: freemium
costNote: Typically free preview / existence check with paid tiers for full leaked records; exact model unverified.
opsec: passive
opsecNote: Server-side query against a third-party breach index; subject is not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Breach-search engine referenced in awesome-osint. ".is" combo/leak search sites are numerous and short-lived; provenance and accuracy not independently verified. Treat as a lead generator only.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases: []
tags:
- email-search-email-check
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# IntelBase

> Aggregated breach/leak search engine — checks an email, username, or domain against compiled credential dumps.

## When to use
You have a subject's `email`, `username`, or a `domain` and want to find which breaches/leaks expose them and what associated identifiers (other emails, usernames, passwords) appear alongside. In missing-persons work this helps confirm an account belongs to your subject and can surface alternate handles to pivot on. Use when classic breach checkers come up short and you want broader combo-list coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intelbase.is/.
2. Enter the `email`, `username`, or `domain`.
3. Run the search; review which datasets the subject appears in and any linked credentials. Full records are commonly paywalled.
4. Pivot: feed newly found usernames/emails into [[leakcheck]], [[intelligence-x-2]], or social-profile searches.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach names, linked `email`/`username`/`password`, associated `domain`
- **Empty/negative result looks like:** no datasets returned — subject not in their compiled corpus, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: full record contents are usually behind a paywall; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. These ".is" leak-search sites change ownership/availability often — verify it is live and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[leakpeek-com]] because combo-list aggregators each index different dumps; coverage gaps differ.

## Trust & verifiability
`trust: unverified` — third-party breach aggregator with undisclosed data provenance, cited only in community lists. Confirm any actionable hit independently and assume records may be stale or mislabeled.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelbase |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, password, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
