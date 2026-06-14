---
id: leakpeek-com
name: Leakpeek.com
description: Use when you have an email, username, or phone and want to find which breaches expose it — returns breach sources and linked credentials/identifiers.
url: https://leakpeek.com
category: email
path:
- email
bestFor: Searching breach data by email, username, or phone with named-source results.
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
costNote: Free search confirms exposure/counts; viewing full per-breach records (passwords, linked fields) requires a paid subscription.
opsec: passive
opsecNote: Server-side query against LeakPeek's breach index; subject not notified. Use a research-only account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: LeakPeek is a known commercial breach-search service recommended across multiple curated OSINT lists (per metaosint). Names source breaches, aiding verification, but full records are paywalled and provenance is leaked data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- LeakPeek
tags:
- email
- data-breach-search-engines
source: metaosint
lastVerified: ''
enrichment: full
---

# Leakpeek.com

> Commercial breach-search engine — given an email, username, or phone, returns which breaches exposed it and the linked credential fields.

## When to use
You have a subject's `email`, `username`, or `phone` and want a source-named list of breaches that include them plus associated identifiers (other emails, usernames, sometimes names/phones). In missing-persons work this confirms account ownership, surfaces alternate handles/contacts, and gives breach context to bound an activity timeline. A solid second-line breach checker to run alongside [[leakcheck]].

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://leakpeek.com and run the search (account/subscription for full data).
2. Enter the `email`, `username`, or `phone`.
3. Read the result: named breach sources and which fields were exposed. Full record contents are paid.
4. Pivot: take newly surfaced emails/usernames/phones into [[intelligence-x-2]] or social-profile lookups; use breach dates for a timeline.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`, `domain`
- **Out:** named breach sources, exposed field types, linked `email`/`username`/`password`/`phone`/`name`
- **Empty/negative result looks like:** "no results found" — selector absent from their corpus, not proof of no exposure anywhere.

## Gotchas & OpSec
- Human-in-the-loop: free tier confirms existence; full records require a paid subscription.
- OpSec: passive toward the subject; queries tied to your account — use a dedicated research account.

## Overlaps ("do both")
- Pairs with [[leakcheck]] and [[intelligence-x-2]] because each aggregator indexes different breaches and content types.

## Trust & verifiability
`trust: community` — commercial breach engine recommended by multiple curated OSINT sources; it names source breaches, which aids corroboration. Records may be stale and provenance is leaked data — verify before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leakpeek-com |
| category | email |
| selectorsIn → selectorsOut | email, username, phone, domain → email, username, password, phone, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
