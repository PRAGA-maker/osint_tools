---
id: snusbase
name: Snusbase
url: https://www.snusbase.com/
category: email
path:
- email
description: Use when you have an `email`, `username`, `name`, `ip-address` or hash and want breached records — returns linked emails, names, addresses, phones and password hashes.
bestFor: Fast, indexed breach-database search that pivots one selector (email/username/IP/name) into other leaked personal data.
selectorsIn:
- email
- username
- ip-address
- name
- phone
selectorsOut:
- email
- name
- address
- phone
status: live
pricing: freemium
costNote: Effectively paid — account required, and plaintext results (names, addresses, passwords) are for paying members; a free API tier (up to ~2,048 requests/day) exists for subscribers. No usable free anonymous search.
opsec: passive
opsecNote: Searching breach data does not contact or notify the subject — it is passive. But you must register and pay, tying queries to an account/payment; the operator sees exactly what you search. Use a sock-puppet account and dedicated payment for sensitive investigations.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2016) commercial breach-search service with broad indexed data; results are as accurate as the underlying breaches, which can be old, mixed-quality, or contain errors.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Snusbase
- snusbase.com
tags:
- breach
- credential-search
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Snusbase

> A commercial breach-search engine — pivot an email, username, name, IP, phone or hash into the other personal data leaked alongside it across indexed breaches.

## When to use
You have one selector (`email`, `username`, `name`, `ip-address`, `phone`, or a password hash) and want to expand it: Snusbase returns records from data breaches that tie that selector to names, addresses, phones, other emails and password hashes. Powerful for linking aliases to a real identity, corroborating an address, or confirming which accounts a person controls — subject to the ethical/legal limits of using breach data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register and subscribe at https://www.snusbase.com/ (plaintext results require a paid membership).
2. Choose the search field (email, username, name, IP, phone, hash) and enter the selector.
3. Review matched breach rows: linked emails, names, addresses, phones, and hashes, with the source breach noted.
4. Cross-reference rows to connect aliases to a real identity; be wary of collisions on common selectors.
5. Pivot: a linked `email` feeds account-existence checks; a hash feeds cracking/reuse analysis; a name/address feeds people-search and directories.

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `ip-address`, `phone`, or password hash
- **Out:** linked `email`, `name`, `address`, `phone`, password hashes (with source breach)
- **Empty/negative result looks like:** no rows — the selector isn't in Snusbase's indexed breaches, which is not proof of no exposure (other engines index different breaches). Conversely, breach data can be stale or mis-attributed, so a hit needs corroboration.

## Gotchas & OpSec
- Effectively paid: no meaningful free anonymous search; budget a subscription.
- Breach data is historical and mixed-quality — addresses/phones may be years out of date, and common names/emails collide.
- OpSec: passive toward the subject, but account+payment make your queries attributable to the operator; use a puppet account. Mind the legal/ethical constraints on breach data in your jurisdiction.

## Overlaps ("do both")
- Pairs with `[[whatbreach]]` and Have I Been Pwned — Snusbase gives plaintext pivots those often can't, while HIBP is free for breach-presence checks; run both since breach coverage differs by engine.

## Trust & verifiability
`trust: community` — an established commercial breach index; data is authentic to its source breaches but historical and error-prone, so treat any single record as a lead to confirm against a current source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snusbase |
| category | email |
| selectorsIn → selectorsOut | email, username, ip-address, name, phone → email, name, address, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
