---
id: pipl
name: Pipl
description: Use when you have an email, phone, username, or name and want deep identity resolution linking it to a real person, contacts, and history — enterprise/investigations service (B2B, gated).
url: https://pipl.com
category: email
path:
- email
bestFor: Authoritative identity resolution from an email/phone/username/name to a real-person profile.
selectorsIn:
- email
- phone
- username
- name
selectorsOut:
- name
- social-profile
- address
- phone
- employer-org
- associate
status: live
costNote: No public free tier since ~2019; Pipl is an enterprise/investigations identity-resolution service requiring a vetted commercial account or API contract.
pricing: freemium
opsec: passive
opsecNote: Server-side identity resolution against Pipl's index; no contact with the subject. Queries are tied to your vetted account.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
- payment-wall-partial
bestInteractionPattern: api
trust: trusted
trustNote: Pipl is a long-established, reputable identity-resolution provider used by fraud/investigations teams. Strong data quality; access is gated to vetted business customers.
missingPersonsRelevance: high
coverage:
- global
- us
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Pipl Search
- Pipl API
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Pipl

> The heavyweight identity-resolution service — turn a thin selector (email/phone/username/name) into a corroborated real-person profile with contacts, history, and associates.

## When to use
You have an `email`, `phone`, `username`, or `name` and need to resolve it to a single real identity with linked `address`, `employer-org`, `social-profile`, and `associate` data. Best when you have authorized investigative access.

## How to use it (`bestInteractionPattern`: api)
1. Obtain a vetted Pipl business account / API key (no consumer self-serve).
2. Call the Search API (or the web console) with the selector.
3. Read the resolved person object — match scores tell you confidence; multiple candidates mean ambiguity.
4. Pivot resolved `address`/`phone`/`associate` to people-search and public-records strategies.

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, `name`
- **Out:** `name`, `social-profile`, `address`, `phone`, `employer-org`, `associate`
- **Empty/negative result looks like:** no match or low match score / multiple low-confidence candidates — don't force a single identity.

## Gotchas & OpSec
- Human-in-the-loop: vetted account + API key + payment; the public site no longer offers free consumer search.
- US/global coverage is strong but not exhaustive; weaker for minors/low-footprint subjects.
- OpSec: passive against the subject; queries logged to your account. Respect the permissible-use terms (FCRA-style restrictions may apply).

## Overlaps ("do both")
- Pairs with `[[osint-industries]]` (footprint/account mapping) and `[[nymeria-io]]` (contact enrichment); Pipl is the strongest at collapsing selectors into one identity.

## Trust & verifiability
`trust: trusted` — established, audited commercial provider with match-confidence scoring; still corroborate high-stakes conclusions against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pipl |
| category | email |
| selectorsIn → selectorsOut | email, phone, username, name → name, social-profile, address, phone, employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes |
