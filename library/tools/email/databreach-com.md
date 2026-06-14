---
id: databreach-com
name: databreach.com
description: Use when you want to check whether an email/username appears in known breaches; harvested as a breach-account site but its exact function is unconfirmed — verify before relying on it.
url: https://databreach.com/
category: email
path:
- email
bestFor: Possible breach-exposure lookup for an email or username (unconfirmed scope).
selectorsIn:
- email
- username
selectorsOut:
- email
- username
- name
status: unknown
pricing: freemium
costNote: Unconfirmed; many breach-lookup sites gate full detail behind payment. Verify before assuming free.
opsec: passive
opsecNote: A breach lookup searches about a third party and does not contact the subject. If it requires an account, that changes the footprint — confirm first.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Generic domain harvested under "Hacked / Breached Account Sites"; I cannot confirm its operator, corpus, or even that it is a functioning breach engine versus a news/landing/parked page. Confirm the live site before use.
missingPersonsRelevance: medium
coverage:
- global
auth: unknown
api: false
localInstall: false
registration: false
aliases: []
tags:
- hackedaccounts
- breach-data
source: uk-osint
lastVerified: ''
enrichment: full
---

# databreach.com

> A site harvested under "Hacked / Breached Account Sites" — likely a breach-exposure lookup, but its exact function is unconfirmed.

## When to use
If it is a working breach engine, you would use it as you would any other: enter an `email` or `username` to check exposure across leaked datasets. Because the scope is unverified, treat it as a *candidate* aggregator to try and confirm, not a trusted one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and confirm it is actually a breach-search interface (it may be a news/landing/parked page given the generic domain).
2. If a search field exists, enter the `email`/`username` and review returned records.
3. Pivot: any recovered alternate `email`/`username`/`name` feeds account-discovery and username-search tools.

## Inputs → Outputs
- **In (if functional):** `email` or `username`
- **Out (if functional):** breach records with associated `email` / `username` / `name`
- **Empty/negative result looks like:** no search field at all (informational/parked page), or zero records for the selector.

## Gotchas & OpSec
- Scope unconfirmed — verify the site is a live breach engine before trusting or paying. Generic premium domains are sometimes resold/parked.
- OpSec: a breach lookup is passive toward the subject; if it demands an account, reassess.

## Overlaps ("do both")
- Prefer better-characterised aggregators first: `[[dehashed]]`, `[[checkleaked-cc]]`, `[[breachdirectory-org]]`.

## Trust & verifiability
`trust: unverified` — operator, corpus, and even functionality are unconfirmed. Do not rely on results without independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | databreach-com |
| category | email |
| selectorsIn → selectorsOut | email, username → email, username, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
