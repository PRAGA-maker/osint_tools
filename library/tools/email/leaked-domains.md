---
id: leaked-domains
name: leaked.domains
description: Use when you have an email, username, or domain and want to check it against breached/leaked-account data — returns exposure confirmation and linked identifiers.
url: https://leaked.domains/
category: email
path:
- email
bestFor: Checking an email/username/domain against breached-account data.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- domain
status: unknown
pricing: freemium
costNote: Likely free preview/existence check with paid tiers for full records; model unverified.
opsec: passive
opsecNote: Server-side query against a third-party leak index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under Hacked/Breached Account Sites. Obscure leak-search domain; ownership, data provenance, and accuracy not independently verified. Treat as a lead source only.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases: []
tags:
- hackedaccounts
- Hacked / Breached Account Sites
- data-breach-search-engines
source: uk-osint
lastVerified: ''
enrichment: full
---

# leaked.domains

> Breached-account search site — checks whether an email, username, or domain appears in leaked/compromised datasets.

## When to use
You have a subject's `email`, `username`, or `domain` and want another breach checker to run in parallel to confirm exposure and surface linked identifiers. In missing-persons work, a hit can verify an account belongs to your subject and reveal alternate handles. Use as a supplementary aggregator, not a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://leaked.domains/.
2. Enter the `email`, `username`, or `domain`.
3. Read which datasets the subject appears in; full record contents are commonly paid.
4. Pivot: take any new emails/usernames into [[leakcheck]], [[intelligence-x-2]], or social-profile searches.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach existence flag, associated `email`/`username`/`domain`
- **Empty/negative result looks like:** no matches — subject absent from this index, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: detailed records likely paywalled; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. Obscure leak sites can be unreliable or transient — verify it is live and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[intelbase]] because each leak aggregator indexes different dumps.

## Trust & verifiability
`trust: unverified` — obscure breach site known only from a directory listing; provenance and accuracy unconfirmed. Corroborate any hit independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaked-domains |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
