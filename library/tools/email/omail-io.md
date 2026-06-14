---
id: omail-io
name: omail.io
description: Use when you have a name + company/domain and want to find or verify business email addresses — returns candidate emails (B2B lead tool, verify before relying on it).
url: https://omail.io/leads
category: email
path:
- email
bestFor: B2B email/lead finding from a name and company domain.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
- name
status: unknown
pricing: freemium
costNote: Lead/email-finder services of this type typically offer a small free quota then paid credits; pricing unconfirmed.
opsec: passive
opsecNote: Queries an aggregated email/lead index; no contact with the subject. Account-tied usage is logged.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: omail.io/leads presents as a business email/lead-generation finder, but the vendor is obscure and its data quality and freshness are unconfirmed. Treat results as unverified leads.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# omail.io

> A business email / lead-finding service that maps a name + company into candidate email addresses — vendor obscure, treat output as unverified leads.

## When to use
You have a `name` and an `employer-org` or `domain` and want a likely business `email` to pivot on. Like most lead tools, it skews toward corporate contacts, not low-footprint individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://omail.io/leads and register if required.
2. Enter the person's name and company/domain.
3. Read returned candidate email(s); note whether the tool marks them verified vs guessed.
4. Independently confirm any address (deliverability check / breach lookup) before acting.
5. Pivot a confirmed `email` to `[[osint-rocks]]` / `[[osintcat]]` for linked accounts.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `domain`
- **Out:** `email`, `name`
- **Empty/negative result looks like:** no candidate addresses, or only pattern-guessed (unverified) emails.

## Gotchas & OpSec
- Human-in-the-loop: likely account login and a paywall beyond a free quota.
- Pattern-guessed emails can be wrong — never treat as confirmed.
- OpSec: passive; queries logged to your account. Use a dedicated investigative account.

## Overlaps ("do both")
- Pairs with `[[nymeria-io]]` and `[[pipl]]`, which are more established for contact enrichment.

## Trust & verifiability
`trust: unverified` — obscure vendor; capabilities and data quality not confirmed. Corroborate every result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | omail-io |
| category | email |
| selectorsIn → selectorsOut | name, employer-org, domain → email, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
