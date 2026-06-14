---
id: find-emails-addresses-and-social-profiles-in-seconds
name: Find emails addresses and social profiles in seconds
description: Use when you want a commercial enrichment service (Orbitly) to turn an email or name+company into contact details and linked social profiles — returns email, social-profile, name.
url: https://www.orbitly.io
category: email
path:
- email
bestFor: B2B-style contact/email enrichment and email-to-social-profile lookup.
selectorsIn:
- email
- name
- domain
selectorsOut:
- email
- social-profile
- name
status: live
pricing: freemium
costNote: Commercial enrichment service (Orbitly); limited free credits, paid plans/API for volume.
opsec: passive
opsecNote: Passive aggregation via the vendor's data; the target is not contacted. Requires an account, so queries are tied to your identity/billing.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
- payment-wall-partial
bestInteractionPattern: api
trust: unverified
trustNote: Commercial contact-enrichment vendor (Orbitly); accuracy, coverage, and data sources are vendor claims not independently verified here.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Orbitly
tags:
- email
- enrichment
- contact-finder
source: metaosint
lastVerified: ''
enrichment: full
---

# Find emails addresses and social profiles in seconds (Orbitly)

> Orbitly is a commercial contact-enrichment service: give it an email, or a name plus company/domain, and it returns likely email addresses and linked social profiles — built for sales lead-gen, usable for OSINT.

## When to use
You have a `name` + `domain`/employer and need a probable work `email`, or you have an `email` and want associated `social-profile`/`name`. Useful in missing-persons work to connect a known affiliation to contactable addresses and profiles — but it is B2B-oriented and paid past a small free tier.

## How to use it (`bestInteractionPattern`: api)
1. Register at orbitly.io and obtain credits / an API key.
2. Submit a `name`+`domain` (to find an email) or an `email` (to enrich into profiles) via the dashboard or API.
3. Read the returned candidate addresses (with confidence scores) and linked social profiles.
4. Pivot: verify any candidate `email` with `[[emailhippo]]`, and expand confirmed addresses via `[[epieos-email-tool]]`.

## Inputs → Outputs
- **In:** `email`, `name`, `domain`
- **Out:** `email` (candidate addresses), `social-profile`, `name`
- **Empty/negative result looks like:** no candidate addresses / no profile matches — the person isn't in the vendor's B2B data (common for non-professional subjects).

## Gotchas & OpSec
- Human-in-the-loop: account, credits, and a payment wall for real volume.
- B2B bias: coverage skews to professionals/companies; weak for people without a work footprint.
- Email "finds" are predictions with confidence scores — verify deliverability before trusting.
- OpSec: passive toward the target; queries tied to your billed account.

## Overlaps ("do both")
- Try free tools first (`[[epieos-email-tool]]`, `[[holehe]]`); use Orbitly when you need name+company→email prediction at scale, then verify with `[[emailhippo]]`.

## Trust & verifiability
`trust: unverified` — a commercial enrichment vendor whose data quality and sources are not independently confirmed here; treat outputs (especially predicted emails) as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-emails-addresses-and-social-profiles-in-seconds |
| category | email |
| selectorsIn → selectorsOut | email, name, domain → email, social-profile, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (account-login, api-key, payment-wall-partial) |
