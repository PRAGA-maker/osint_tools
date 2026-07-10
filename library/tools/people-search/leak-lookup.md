---
id: leak-lookup
name: Leak-Lookup
description: Use when you have an `email`, `username`, or `domain` and want to find which data breaches exposed it and what associated credentials/fields leaked — returns email, name, and social-profile leads.
url: https://leak-lookup.com/
category: people-search
path:
- people-search
bestFor: Searching 28B+ breach records for a selector and pulling the associated leaked fields.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- name
- social-profile
status: live
pricing: freemium
costNote: Free searches return limited results; full results use a pay-per-lookup model. A Search API and Hash API are available to registered users. Registration required for anything beyond the teaser.
opsec: passive
opsecNote: Queries go to leak-lookup.com, not the target, so no alert reaches the subject. But you disclose the searched selector to a third-party breach broker that may log it. Use a puppet account/email for the platform login.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running breach-search service (28B+ records / 4,700+ breaches) used in the OSINT community; not a first-party source and breach data can contain errors or stale/duplicated records.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- haveibeenpwned
- dehashed
- intelligence-x
aliases:
- leak-lookup.com
tags:
- bellingcat-toolkit
- breach-search
- people
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Leak-Lookup

> A data-breach search engine (28B+ records across 4,700+ breaches) that maps a selector to the breaches it appears in and the associated leaked fields.

## When to use
You have an `email`, `username`, or `domain` and want to pivot through breach data: which breaches exposed it, and what other data (names, passwords, linked accounts) was leaked alongside. Breach co-occurrence is a strong link-building tool — a shared password or a name field tied to an email can connect a subject to other accounts and identities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://leak-lookup.com/ and register (free searches give limited/teaser results).
2. Search by email, username, or domain.
3. Read the results: the list of breaches containing the selector and the fields exposed. Full field-level detail is behind the pay-per-lookup wall.
4. For bulk/automated work, use the Search API with your key.
5. Pivot: a leaked name feeds people-search; a co-occurring email/username feeds cross-platform enumeration; reused passwords hint at other accounts (never attempt to log in with them).

## Inputs → Outputs
- **In:** `email`, `username`, or `domain`
- **Out:** breach names, associated `email`/`name`/`social-profile` fields (paywalled for full detail)
- **Empty/negative result looks like:** "no breaches found" — the selector isn't in their corpus. That is not proof the person was never breached; cross-check another aggregator.

## Gotchas & OpSec
- Human-in-the-loop: free tier is a teaser; full results and API require account + payment.
- OpSec: **passive** toward the subject, but you hand the selector to a breach broker — use a puppet login. Do NOT reuse discovered passwords to access any account; that is illegal.
- Data quality: breach dumps contain stale, duplicated, and mislabeled records — corroborate before acting.

## Overlaps ("do both")
- Pairs with `[[haveibeenpwned]]` — HIBP tells you *which* breaches (free, ethical) without exposing passwords; use it to validate Leak-Lookup's breach list.
- Pairs with `[[dehashed]]` and `[[intelligence-x]]` — different breach corpora; run several since coverage differs per selector.

## Trust & verifiability
`trust: community` — a well-known breach-search service, but it aggregates third-party dumps of variable quality; treat hits as leads to corroborate, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leak-lookup |
| category | people-search |
| selectorsIn → selectorsOut | email, username, domain → email, name, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
