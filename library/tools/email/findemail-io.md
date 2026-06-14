---
id: findemail-io
name: findemail.io
description: Use when you have a person's name plus an employer/company domain and need to find or guess their work email address.
url: https://findemail.io/
category: email
path:
- email
bestFor: Finding a likely work email from a name + company domain.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
status: unknown
pricing: freemium
costNote: Free lookups are limited; bulk/API access is paid.
opsec: passive
opsecNote: Queries are server-side against the vendor; the target is not contacted. Avoid uploading sensitive case lists to a third-party SaaS.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial email-finder SaaS; results are pattern-guessed and not independently verified here. Treat returned emails as candidates to validate.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
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

# findemail.io

> Email-finder SaaS that infers a person's likely work address from their name and company domain.

## When to use
You have a `name` and an `employer-org` / `domain` (e.g. "Jane Doe" at acme.com) and need a contactable `email` to pivot on — for a tip-line message, a breach-database lookup, or account-existence checks. Best when the person has a corporate/business affiliation; weak for purely personal Gmail/Outlook addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://findemail.io/ and sign in (free tier requires registration).
2. Enter the person's full `name` and the company `domain`.
3. Read the returned candidate `email` plus any confidence/verification score the tool shows.
4. Pivot: take the candidate into an email-validation tool like `[[free-email-address-validator]]` and into breach/account-existence checks before relying on it.

## Inputs → Outputs
- **In:** `name` + `employer-org`/`domain`
- **Out:** `email` (candidate, often with a confidence score)
- **Empty/negative result looks like:** no address returned, or only a generic pattern guess (e.g. firstname@domain) with low confidence — do not treat as confirmed.

## Gotchas & OpSec
- Human-in-the-loop: requires account login and is rate-limited on the free tier.
- Outputs are pattern-derived guesses; always validate before acting.
- OpSec: passive toward the target, but you are disclosing the name/domain you are researching to a commercial vendor — assume it is logged.

## Overlaps ("do both")
- Pairs with `[[free-email-address-validator]]` (Verifalia) to confirm deliverability of a guessed address.

## Trust & verifiability
`trust: unverified` — commercial SaaS; this entry describes capability from the product category, not a verified test run. Validate any address it returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findemail-io |
| category | email |
| selectorsIn → selectorsOut | name, employer-org, domain → email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
