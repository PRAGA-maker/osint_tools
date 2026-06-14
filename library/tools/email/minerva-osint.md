---
id: minerva-osint
name: Minerva OSINT
description: Use when you have an email (or username/phone) and want an aggregator to cross-reference breach data and online accounts into a single identity profile.
url: https://minervaosint.com
category: email
path:
- email
bestFor: Email/username/phone enrichment against breach and account-discovery data.
selectorsIn:
- email
- username
- phone
selectorsOut:
- name
- social-profile
- phone
- address
status: unknown
pricing: freemium
costNote: OSINT-aggregator platforms typically gate full results behind paid credits/subscription with a limited free preview; confirm current pricing on site.
opsec: passive
opsecNote: Queries are run server-side against the platform's datasets; the target is not contacted. Your query is logged by the vendor — use a dedicated account and assume the platform sees what you search.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Minerva OSINT (minervaosint.com) presents as a commercial OSINT email/identity aggregator. Dataset coverage, freshness, and legality of sources are not independently verified.
missingPersonsRelevance: high
coverage: []
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Minerva OSINT

> Commercial OSINT aggregator — cross-references an email/username/phone against breach and account data to assemble an identity profile.

## When to use
You have a confirmed selector (`email`, `username`, or `phone`) for a missing person or associate and want a single query that pulls together linked accounts, breach appearances, and any tied `name`/`address`/`phone`. Use it as a fast pivot-finder after basic verification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/log in at minervaosint.com.
2. Enter the selector (`email`, `username`, or `phone`).
3. Review aggregated results — linked profiles, breach hits, associated identifiers; full detail is typically behind paid credits.
4. Pivot: each returned `social-profile`/`phone`/`address` is a lead to verify independently in its own tool.

## Inputs → Outputs
- **In:** `email`, `username`, `phone`
- **Out:** `name`, `social-profile`, `phone`, `address`
- **Empty/negative result looks like:** "no records" — common for low-footprint subjects; absence is not proof. Watch for over-matching on common selectors.

## Gotchas & OpSec
- Aggregators recycle breach data of varying age/accuracy; every result is a lead to corroborate, not a fact.
- The vendor logs your searches; use a separated investigative account and be mindful of jurisdiction/legality of breach-derived data.
- Pricing and dataset coverage are opaque — verify before relying on "no results" as meaningful.

## Trust & verifiability
`trust: unverified` — commercial aggregator with undisclosed sources and no independent benchmark; capability inferred from the platform's positioning and the "email-search/email-check" listing, not tested.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | minerva-osint |
| category | email |
| selectorsIn → selectorsOut | email, username, phone → name, social-profile, phone, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
