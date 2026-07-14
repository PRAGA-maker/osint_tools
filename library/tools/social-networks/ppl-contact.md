---
id: ppl-contact
name: ppl.contact
description: Use when you have a `name` + `employer-org` (or company `domain`) and want a person's business `email`/`phone` — returns B2B contact details drawn from a 278M+ contact database.
url: https://ppl.contact/
category: social-networks
path:
- social-networks
bestFor: Resolving a named professional at a known company to a verified business email and phone via a large B2B contact database.
selectorsIn:
- name
- employer-org
- domain
selectorsOut:
- email
- phone
- employer-org
- social-profile
status: live
pricing: freemium
costNote: Pay-as-you-go credit model over a 278M+ B2B contact database; effectively paid — expect only a small free trial/credit allotment before lookups consume paid credits and require signup.
opsec: passive
opsecNote: You query a third-party broker's database, not the subject, so no notification reaches them. You must create an account to spend credits, which attributes usage to that login — use a research account, and be aware the broker logs your queries.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial B2B contact/lead broker; contacts are scraped/aggregated and may be stale or wrong, and "verified" is the vendor's claim — confirm any email/phone before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ppl.contact
tags:
- linkedin
- LinkedIn & Similar Sites
- b2b
- contact-enrichment
- data-broker
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# ppl.contact

> A B2B contact-enrichment broker — turns a name-at-a-company into a business email and phone from a 278M+ contact database.

## When to use
You have a `name` and their `employer-org` (or the company's `domain`) and need business contact details — a work `email` or direct `phone` — for a professional subject. This is a lead-generation/enrichment database, so it is strongest for people with a corporate/LinkedIn-style footprint and weak for private individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ppl.contact/ and sign up (pay-as-you-go credits).
2. Search by person name + company, or by company domain to enumerate contacts.
3. Spend credits to reveal the verified business `email`/`phone` for a match.
4. Read outputs: contact details plus role/company and any linked profile.
5. Pivot: a work email feeds email-OSINT and breach checks; the confirmed employer narrows further searches.

## Inputs → Outputs
- **In:** `name` + `employer-org`, or company `domain`
- **Out:** business `email`, `phone`, `employer-org`/role, `social-profile`
- **Empty/negative result looks like:** no contact returned, or a stale/bounced address — B2B brokers miss non-corporate people entirely and carry outdated records; a null here says little about a private individual.

## Gotchas & OpSec
- Human-in-the-loop: real data sits behind signup and paid credits; the "free" surface is minimal.
- Data is aggregated and may be outdated or misattributed; "verified" is a vendor claim — validate the email/phone before acting.
- Coverage skews to business contacts in corporate directories, not personal numbers.

## Overlaps ("do both")
- Pairs with other contact-enrichment and email-verification tools — cross-check ppl.contact's output against an independent email validator before trusting it.

## Trust & verifiability
`trust: unverified` — a commercial data broker with opaque, aggregated sourcing; treat every field as a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ppl-contact |
