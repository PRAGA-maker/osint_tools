---
id: intelligencesecurity-io
name: intelligencesecurity.io
description: Use when you have an email or username and want to check it against a breach/leak index — returns exposure confirmation and any linked identifiers.
url: https://intelligencesecurity.io/
category: email
path:
- email
bestFor: Checking an email/username against breached-account data.
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
costNote: Likely free existence/preview check with paid tiers for full records; model unverified.
opsec: passive
opsecNote: Server-side query against a third-party breach index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under Hacked/Breached Account Sites. Obscure breach/leak service; ownership, data provenance, and accuracy not independently verified. Treat strictly as a lead source.
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

# intelligencesecurity.io

> Breach/leaked-account lookup service — checks whether an email, username, or domain appears in compromised-account datasets.

## When to use
You have a subject's `email`, `username`, or `domain` and want to confirm breach exposure and surface any linked identifiers. In a missing-persons workup this can verify an account belongs to your subject and reveal alternate handles. Reach for it as one of several breach checkers to run in parallel, not as a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intelligencesecurity.io/.
2. Enter the `email`, `username`, or `domain`.
3. Read the result: which datasets the subject appears in; full record contents are commonly paid.
4. Pivot: take new emails/usernames into [[leakcheck]], [[intelligence-x-2]], or social-profile searches.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach existence flag, associated `email`/`username`/`domain`
- **Empty/negative result looks like:** no matches — subject absent from this index, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: detailed records likely paywalled; free use confirms existence.
- OpSec: passive; leaks nothing to the subject. Obscure leak sites can be unreliable or short-lived — verify it is live and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[intelbase]] because each breach aggregator indexes different dumps.

## Trust & verifiability
`trust: unverified` — obscure third-party breach service known only from a directory listing; provenance and accuracy unconfirmed. Corroborate any hit independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligencesecurity-io |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
