---
id: hunter
name: Hunter
description: Use when you have a person's name + a company/domain and want to find or verify their work email (and the org's email pattern).
url: https://hunter.io/
category: email
path:
- email
- email-search
bestFor: Finding and verifying professional/business email addresses tied to a name and domain.
selectorsIn:
- name
- domain
- employer-org
selectorsOut:
- email
- name
- employer-org
status: live
pricing: freemium
costNote: Free tier allows limited searches/verifications per month after signup; higher volume and full API access are paid.
opsec: passive
opsecNote: Queries Hunter's index of publicly-sourced emails and does not contact the target. Email verification pings mail servers but is done by Hunter, not from your IP, and does not email the person.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hunter.io is a well-established, widely-used commercial email-finding service with a transparent confidence-scoring model and documented sources per result.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- hunter-io
- holehe
- have-i-been-pwned
aliases:
- hunter.io
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hunter

> The standard work-email finder: give it a `name` + company `domain` and it returns the likely email plus a confidence score and the org's address pattern (e.g. first.last@).

## When to use
You know a missing person (or, more often, an associate/employer contact) works at a given company and you want their `email`, or you have a domain and want the email pattern to derive it. Strongest for employment angles — finding a coworker, employer HR, or a relative's work address to reach out via legitimate channels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://hunter.io/ (free tier).
2. **Email Finder:** enter the person's full `name` + company `domain` → returns the most likely email + confidence + sources.
3. **Domain Search:** enter a `domain` → returns known emails for that org and the prevailing pattern.
4. **Email Verifier:** paste an `email` → returns deliverability/validity.
5. Pivot a confirmed email into `[[holehe]]` (which services use it) and `[[have-i-been-pwned]]` (breaches).

## Inputs → Outputs
- **In:** `name`, `domain`, `employer-org`
- **Out:** `email`, the org email pattern, confidence score, source citations
- **Empty/negative result looks like:** "no email found" or a low confidence score with no sources — treat as unconfirmed; the pattern may still let you guess the address.

## Gotchas & OpSec
- Hunter focuses on *business/professional* emails, not personal webmail — limited for someone with no corporate footprint.
- Human-in-the-loop: requires an account; free tier is rate-limited monthly.
- OpSec: passive; verification does not email the target.

## Overlaps ("do both")
- The harvested `[[hunter-io]]` entry is the Domain-Search view of this same service — same product, treat as one. Pair with `[[holehe]]` / `[[have-i-been-pwned]]` once you have an email.

## Trust & verifiability
`trust: trusted` — mature commercial service with per-result source citations and confidence scoring, making outputs auditable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunter |
| category | email |
| selectorsIn → selectorsOut | name, domain, employer-org → email, name, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
