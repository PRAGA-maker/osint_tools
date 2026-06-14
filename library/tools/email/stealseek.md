---
id: stealseek
name: StealSeek
description: Use when you have an email/username/domain and want to check exposure in infostealer logs and breach data — returns leaked credentials/accounts tied to the identifier.
url: https://stealseek.io/
category: email
path:
- email
bestFor: Searching infostealer-log and breach datasets for credentials and accounts linked to an email, username, or domain.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- social-profile
- ip-address
status: unknown
pricing: freemium
costNote: Breach/stealer-log search engines of this class typically show a teaser for free and gate full records behind a paid or credit-based plan.
opsec: passive
opsecNote: You query the engine's indexed datasets, not the subject, so the person is not alerted. Submitting case identifiers to a third-party breach engine means the query is logged — use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed as a data-breach search engine; the operator's data sourcing, accuracy, and legality of stealer-log data are unconfirmed. Capabilities inferred from name/category and not independently verified.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- breach
- stealer-logs
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# StealSeek

> A breach / infostealer-log search engine — checks whether an identifier appears in leaked credential dumps.

## When to use
You have an `email`, `username`, or `domain` for a missing person and want to know what accounts and credentials are exposed in breach corpora and infostealer (malware) logs. Stealer-log hits can reveal otherwise-hidden online accounts, login URLs the person used, and an associated `ip-address` — strong pivots for tracing recent activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stealseek.io/ and register/log in (most breach engines gate results behind an account).
2. Search by `email`, `username`, or `domain`.
3. Read the result: matched accounts, leaked credentials, the originating breach/log, and sometimes the capture `ip-address`.
4. Pivot: discovered `social-profile`s and login domains feed account enumeration; an `ip-address` can support geolocation leads.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** `email`, `username`, linked `social-profile`s, `ip-address` (from stealer logs)
- **Empty/negative result looks like:** no records found — the identifier is not in this engine's datasets (does not prove no exposure exists).

## Gotchas & OpSec
- Stealer-log data raises legal/ethical handling concerns; verify your authorization to use breach-derived credentials, and never attempt to log into the subject's accounts.
- Human-in-the-loop: account registration likely required; full records may be paywalled.
- OpSec: passive to the subject, but query from a sock-puppet — breach engines log searches.

## Overlaps ("do both")
- One of several breach search engines; corroborate hits across multiple engines since each indexes different dumps.

## Trust & verifiability
`trust: unverified` — data sourcing, completeness, and operator are unconfirmed; treat results as leads requiring corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stealseek |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, social-profile, ip-address |
| pricing / cost | freemium (unconfirmed) |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
