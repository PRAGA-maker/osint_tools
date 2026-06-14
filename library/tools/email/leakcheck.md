---
id: leakcheck
name: LeakCheck
description: Use when you have an email, username, phone, or domain and want to find which breaches expose it — returns breach names and linked credentials/identifiers.
url: https://leakcheck.io/
category: email
path:
- email
bestFor: Searching breach data by email, username, phone, or domain with named-source results.
selectorsIn:
- email
- username
- phone
- domain
selectorsOut:
- email
- username
- password
- phone
- name
status: live
pricing: freemium
costNote: Free public lookup shows whether/how many breaches; full per-breach records (passwords, linked fields) require a paid plan or API key.
opsec: passive
opsecNote: Server-side query against LeakCheck's breach index; subject not notified. Use a research account; queries may be tied to your account/API key.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: LeakCheck (leakcheck.io) is a well-established commercial breach-search service with a documented API, widely used in OSINT; it names source breaches, which aids verification.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- LeakCheck.io
tags:
- email-search-email-check
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# LeakCheck

> Commercial breach-search engine — given an email, username, phone, or domain, returns which breaches exposed it and the linked credential fields.

## When to use
You have a subject's `email`, `username`, `phone`, or `domain` and want a clean, source-named list of breaches that include them, plus associated identifiers (other emails, usernames, passwords, sometimes names). In missing-persons work this confirms account ownership, surfaces alternate handles/contacts, and gives breach dates that hint at when an account was active. A strong first-line breach checker because it names sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://leakcheck.io/ and use the public search (sign in / API key for full data).
2. Enter the `email`, `username`, `phone`, or `domain`.
3. Read the result: list of named breach sources and which fields were exposed. Full record contents are paid.
4. Pivot: take newly surfaced emails/usernames/phones into [[intelligence-x-2]], [[leakpeek-com]], or social-profile lookups; use breach dates to bound an activity timeline. An API supports automation.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`, `domain`
- **Out:** named breach sources, exposed field types, linked `email`/`username`/`password`/`phone`/`name`
- **Empty/negative result looks like:** "not found in any breach" — selector absent from their corpus, not proof of no exposure anywhere.

## Gotchas & OpSec
- Human-in-the-loop: free tier confirms existence and counts; full records (passwords/linked fields) require payment or API key.
- OpSec: passive toward the subject; queries are associated with your account/API key — use a dedicated research account.

## Overlaps ("do both")
- Pairs with [[intelligence-x-2]] (documents/dark-web breadth) and [[leakpeek-com]] (different dump coverage) because no single aggregator indexes every breach.

## Trust & verifiability
`trust: trusted` — established commercial breach engine that names source breaches, making hits easier to corroborate. Individual leaked records can still be stale; verify before acting on a contact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakcheck |
| category | email |
| selectorsIn → selectorsOut | email, username, phone, domain → email, username, password, phone, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
