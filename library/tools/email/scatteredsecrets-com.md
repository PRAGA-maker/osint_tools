---
id: scatteredsecrets-com
name: scatteredsecrets.com
description: Use when you have an email and want to know which breaches it appears in and any exposed/cracked passwords — Scattered Secrets is a breached-credential search service.
url: https://scatteredsecrets.com/
category: email
path:
- email
bestFor: Checking an email against breach corpora to surface exposed/cracked passwords and linked accounts (account-takeover-risk and pivot data).
selectorsIn:
- email
- username
selectorsOut:
- username
- metadata-exif
- social-profile
status: live
pricing: freemium
costNote: Free notification for domains/emails you can prove you own; viewing actual cracked passwords / arbitrary addresses requires a paid subscription.
opsec: passive
opsecNote: Passive lookup against breach databases — no contact with the subject. You submit the query to the operator, so use appropriate account hygiene.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established breach-credential service run by known researchers; specializes in actually cracking hashed passwords, not just listing breach names. Data is limited to breaches it has ingested. Handle exposed credentials lawfully.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Scattered Secrets
tags:
- hackedaccounts
- Hacked / Breached Account Sites
- breach
- credentials
source: uk-osint
lastVerified: ''
enrichment: full
---

# scatteredsecrets.com

> Scattered Secrets is a breached-credential search engine — give it an `email` and it shows which breaches exposed it and (for paid/verified use) the actual cracked passwords.

## When to use
You have a subject's `email` or `username` and want their breach footprint: which leaks they appear in, reused/cracked passwords, and account linkages. For a missing person this can reveal additional online accounts (via reused passwords/usernames) and confirm an email is genuinely theirs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at scatteredsecrets.com.
2. Search a domain/email you can verify ownership of for free alerts; arbitrary email lookups (and viewing cracked passwords) require a subscription.
3. Read the breach list and any recovered plaintext passwords; note reused passwords/usernames.
4. Pivot recovered `username`s/passwords to other platforms to find linked `social-profile`s.

## Inputs → Outputs
- **In:** `email` or `username`
- **Out:** breach hits, exposed/cracked passwords, linked `username`s and `social-profile`s, breach metadata (`metadata-exif`).
- **Empty/negative result looks like:** "no exposures found" — means not in their ingested corpora, not that the address is breach-free everywhere.

## Gotchas & OpSec
- Human-in-the-loop: account-login plus paywall for full cracked-password access and non-owned lookups.
- OpSec: passive toward the subject. Possessing/using leaked credentials carries legal and ethical limits — use only for lawful investigation, never to access accounts.

## Overlaps ("do both")
- Pairs with other breach engines (`[[scylla-so]]`) — corpora differ, so an email absent in one may appear in another.

## Trust & verifiability
`trust: community` — reputable breach-research operator that uniquely cracks hashes rather than just naming breaches; coverage bounded by ingested datasets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scatteredsecrets-com |
| category | email |
| selectorsIn → selectorsOut | email, username → username, metadata-exif, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
