---
id: toofr
name: Toofr
description: Use when you have a person's name and their company/domain and want to find or guess their work email — returns predicted/verified corporate email addresses.
url: https://www.toofr.com
category: email
path:
- email
bestFor: Finding or guessing B2B/corporate email addresses from a name plus company domain.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
status: live
pricing: freemium
costNote: Limited free credits on signup; paid plans for bulk lookups and higher confidence/verification.
opsec: passive
opsecNote: Predicts addresses from known company email patterns and may run SMTP verification on its side; the subject is not notified. Account signup ties searches to you unless you use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established B2B email-finder SaaS; results are pattern-based guesses with confidence scores, not authoritative identity records.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- theharvester
aliases:
- toofr.com
tags:
- email-search-email-check
- email-finder
- b2b
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Toofr

> A B2B email-finder SaaS that predicts and verifies a person's work email from their name and company domain.

## When to use
You have a subject's `name` and a known `employer-org` / `domain`, and you want their likely work `email`. Most relevant in missing-persons work when the subject is employed and you need a contact channel or a candidate address to run through breach/people tools. Less useful for purely personal webmail subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at `https://www.toofr.com` (use a dedicated/sock-puppet account).
2. Enter the person's first name, last name, and company domain.
3. Toofr returns one or more candidate addresses with a confidence/grade based on the domain's known email pattern.
4. Pivot: take the highest-confidence `email` into SMTP verifiers ([[verify-email]], [[verify-an-email-address-mailtester]]) and reverse-lookup/breach tools ([[venacus]], [[thatsthem]]).

## Inputs → Outputs
- **In:** `name`, `employer-org`, `domain`
- **Out:** `email` (with confidence score)
- **Empty/negative result looks like:** low-confidence guess or "pattern unknown" — common for small companies with no indexed pattern, or generic free-mail domains.

## Gotchas & OpSec
- Human-in-the-loop: requires account login; free credits are limited.
- Output is a *prediction*, not proof — always verify the specific mailbox before trusting it.
- OpSec: passive toward the subject, but your account links the searches to you; use a burner account.

## Overlaps ("do both")
- Pairs with [[theharvester]] — theHarvester confirms the org's actual email format from public data; Toofr applies that format to a specific name.

## Trust & verifiability
`trust: community` — a known commercial email-finder; reliable as a pattern-based lead source but verify each address independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toofr |
| category | email |
| selectorsIn → selectorsOut | name, employer-org, domain → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
