---
id: dehashed
name: DeHashed
description: Use when you have an email, username, name, phone, IP, address, or domain and want to search a very large aggregated breach corpus — returns matched leaked records with cross-referenced identity and credential fields.
url: https://dehashed.com/
category: email
path:
- email
- breach-data
bestFor: High-coverage multi-selector breach search with strong cross-referencing for selector expansion.
selectorsIn:
- email
- username
- name
- phone
- ip-address
- address
- domain
selectorsOut:
- email
- username
- name
- phone
- address
- ip-address
status: live
pricing: freemium
costNote: Account required; results are credit/subscription-gated. Free tier shows that hits exist but masks/limits full record reveal. API access is paid.
opsec: passive
opsecNote: You search about a third party; the subject is never contacted. DeHashed logs your account and queries — use a dedicated investigative account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Widely used, long-established commercial breach-search engine with one of the larger aggregated corpora; well-regarded in the OSINT community, though corpus provenance is still vendor-asserted. Verify high-stakes hits against primary records.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- breachdirectory-org
- checkleaked-cc
aliases:
- DeHashed
tags:
- breach-data
- hackedaccounts
- credentials
source: arf-seed
lastVerified: ''
enrichment: full
---

# DeHashed

> A large, well-established breach-search engine that searches many selector types across an aggregated leak corpus and cross-references the results into a connected identity picture.

## When to use
You have almost any identity selector — `email`, `username`, `name`, `phone`, `ip-address`, `address`, or `domain` — for a missing person or associate and want to find linked leaked records. Its strength is cross-referencing: one selector surfaces records that reveal *other* selectors (an old email reveals a phone; a username reveals a real name), making it a powerful selector-expansion hub early in a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in (account required). Choose the search field type matching your selector and enter the value; wildcard/regex search is supported.
2. Submit and review matched breach records. Full plaintext reveal consumes credits or requires a subscription.
3. Note newly revealed selectors and re-search them to expand the graph.
4. Pivot: feed recovered `email`/`username`/`phone`/`address` into account-discovery, phone-lookup, and people-search tools. The paid API supports automation in larger workflows.

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `phone`, `ip-address`, `address`, or `domain`
- **Out:** breach records cross-referencing `email` / `username` / `name` / `phone` / `address` / `ip-address`
- **Empty/negative result looks like:** zero records for the selector — meaning absence from DeHashed's corpus, not breach-free; confirm with another aggregator.

## Gotchas & OpSec
- Human-in-the-loop: account login plus a credit/subscription wall for full reveal; API needs a paid key.
- Corpus is large but undated/finite — a clean result is not exoneration, and individual records may be stale or contain errors.
- OpSec: passive toward the subject, but DeHashed ties queries to your account — use a dedicated investigative identity and account, not your personal one.

## Overlaps ("do both")
- Pair with `[[checkleaked-cc]]` and `[[breachdirectory-org]]`: corpora differ, so a DeHashed miss is often a hit elsewhere. DeHashed is usually the best single first stop.

## Trust & verifiability
`trust: community` — long-standing, broadly trusted commercial engine, but the breach corpus is vendor-asserted and unaudited. Verify high-stakes findings against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dehashed |
| category | email |
| selectorsIn → selectorsOut | email, username, name, phone, ip-address, address, domain → email, username, name, phone, address, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
