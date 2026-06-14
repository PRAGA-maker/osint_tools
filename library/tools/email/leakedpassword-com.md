---
id: leakedpassword-com
name: Leakedpassword.com
description: Use when you have an email or username and want to check it against breach data — returns which breaches expose it and associated identifiers.
url: https://leakedpassword.com/
category: email
path:
- email
bestFor: Checking an email/username against breached-credential datasets.
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
costNote: Free existence/preview check with paid tiers for full leaked records; model unverified.
opsec: passive
opsecNote: Server-side query against a third-party breach index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Breach-search site harvested from osint4all. Ownership, data provenance, and accuracy not independently verified; treat as a lead generator only.
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

# Leakedpassword.com

> Breach-search engine — checks whether an email, username, or domain appears in leaked credential dumps.

## When to use
You have a subject's `email`, `username`, or `domain` and want to confirm breach exposure and surface associated identifiers (other emails, usernames). In missing-persons work this helps verify account ownership and reveal alternate handles to pivot on. Use as a supplementary breach checker run in parallel with stronger engines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://leakedpassword.com/.
2. Enter the `email`, `username`, or `domain`.
3. Read which datasets the subject appears in; full record contents are commonly paid.
4. Pivot: take new emails/usernames into [[leakcheck]] or [[intelligence-x-2]].

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach existence flag, linked `email`/`username`/`password`, associated `domain`
- **Empty/negative result looks like:** no matches — subject absent from this index, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: full records likely paywalled; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. Verify the site is live and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[leakpeek-com]] because each aggregator indexes different dumps.

## Trust & verifiability
`trust: unverified` — third-party breach aggregator with undisclosed provenance, harvested from a community list. Corroborate any hit independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakedpassword-com |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, password, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
