---
id: breachdirectory-org
name: breachdirectory.org
description: Use when you have an email, username, or domain and want to know which public data breaches it appears in — returns breach names and (often partially masked) associated credentials/records.
url: https://breachdirectory.org/
category: email
path:
- email
bestFor: Quickly checking whether an email/username appears in known breach corpora and which breaches.
selectorsIn:
- email
- username
- domain
selectorsOut:
- username
- email
- name
- social-profile
status: live
pricing: freemium
costNote: Free web lookups expose limited/masked detail; full record reveal and API access are paid.
opsec: passive
opsecNote: You query about a third party's address; you do not contact the subject. Operator logs your searches; use a sock-puppet browser context for sensitive work.
humanInLoop: true
humanInLoopReason:
- captcha
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: One of several public breach-aggregator front-ends; provenance and freshness of its corpus are not independently audited. Cross-check hits before relying on them.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
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

# breachdirectory.org

> A public breach-lookup front-end: paste an email or username and see which leaked datasets it appears in.

## When to use
You have an `email`, `username`, or `domain` for a missing person or an associate and want to confirm exposure in breach corpora — which can surface alternate usernames, an older recovery email, a real name, or password hints that pivot to other accounts. Strong early-stage selector-expansion step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the site and enter the `email` / `username` / `domain` in the search box.
2. Solve any CAPTCHA; submit.
3. Read the list of breaches the selector appears in, plus any partially revealed associated fields. Free tier typically masks part of the record.
4. Pivot: a recovered alternate `username` or `email` feeds username-search and account-discovery tools; a recovered `name` corroborates identity.

## Inputs → Outputs
- **In:** `email`, `username`, or `domain`
- **Out:** breach source names, associated `username` / `email` / `name`, sometimes linked `social-profile`s (often masked on the free tier)
- **Empty/negative result looks like:** "no results" / zero breaches — meaning the selector is absent from *this* corpus, not that it is breach-free everywhere. Confirm against another aggregator.

## Gotchas & OpSec
- Human-in-the-loop: expect a CAPTCHA and a partial paywall — full detail is gated behind paid access/API.
- Corpus is finite and undated; a clean result is not exoneration, and a hit can be stale. Always cross-check.
- OpSec: passive — searching about a subject does not touch their accounts. The operator logs queries; use a clean/sock-puppet session.

## Overlaps ("do both")
- Pair with `[[dehashed]]` and `[[checkleaked-cc]]`: each indexes a different breach set, so a miss on one is often a hit on another.

## Trust & verifiability
`trust: community` — anonymous public aggregator; no audited provenance. Treat hits as leads to verify, not as proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | breachdirectory-org |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → username, email, name, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
