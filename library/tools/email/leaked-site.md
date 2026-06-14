---
id: leaked-site
name: Leaked.site
description: Use when you have an email, username, or domain and want to search compiled breach/leak data — returns exposure confirmation and linked credentials/identifiers.
url: https://www.leaked.site/
category: email
path:
- email
bestFor: Searching compiled breach/leak data by email, username, or domain.
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
costNote: Free preview/existence check with paid access for full leaked records; model unverified.
opsec: passive
opsecNote: Server-side query against a third-party leak index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Breach-search site harvested from osint4all. Provenance and accuracy not independently verified; combo-list leak sites change ownership/availability frequently. Treat as a lead source.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases: []
tags:
- data-breach-search-engines
source: osint4all
lastVerified: ''
enrichment: full
---

# Leaked.site

> Breach/leak search engine — checks an email, username, or domain against compiled credential dumps.

## When to use
You have a subject's `email`, `username`, or `domain` and want to find which breaches expose them and what associated identifiers (other emails, usernames, passwords) appear alongside. In missing-persons work this helps confirm account ownership and surface alternate handles to pivot on. Use as one of several parallel breach checkers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.leaked.site/.
2. Enter the `email`, `username`, or `domain`.
3. Review which datasets the subject appears in and any linked credentials. Full records are commonly paywalled.
4. Pivot: feed new usernames/emails into [[leakcheck]] or [[intelligence-x-2]].

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach names, linked `email`/`username`/`password`, associated `domain`
- **Empty/negative result looks like:** no datasets returned — subject not in their corpus, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: full records usually paywalled; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. These leak-search sites change ownership/availability often — verify it is live and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[leakpeek-com]] because combo-list aggregators each index different dumps.

## Trust & verifiability
`trust: unverified` — third-party breach aggregator with undisclosed provenance, harvested from a community list. Confirm any actionable hit independently; assume records may be stale or mislabeled.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaked-site |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, password, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
