---
id: rocketreach-co
name: RocketReach
description: Use when you have a `name` + `employer-org` (or a company domain) and want the subject's professional email, phone and social profiles — returns email, phone and social-profile.
url: https://rocketreach.co
category: social-networks
path:
- social-networks
bestFor: Turning a name-plus-employer into professional contact details (work email, direct/mobile phone, LinkedIn) via a B2B contact database.
selectorsIn:
- name
- employer-org
selectorsOut:
- email
- phone
- social-profile
status: live
pricing: freemium
costNote: Free account gives a small number of lookups/credits per month; full contact reveals (especially phone numbers) and bulk use require a paid plan or API key.
opsec: active
opsecNote: You are querying a third-party aggregator that logs your searches, and the subject is not contacted — but registration ties queries to your account. Use a dedicated sock-puppet account and email, never a personal or agency login, and avoid revealing the target's exact identity in any shared/team workspace.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established commercial contact-data provider; data is aggregated/inferred, so email and phone accuracy varies and must be verified before use.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- hunter-io
- rocketreach
aliases:
- rocketreach.co
- RocketReach lead intelligence
tags:
- linkedin
- LinkedIn & Similar Sites
- b2b-contact-data
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# RocketReach

> A B2B contact-intelligence database: give it a person and their company and it returns likely work email, phone, and linked professional profiles.

## When to use
You have a `name` and an `employer-org` (or company domain) and need the subject's professional contact points — work email, direct/mobile phone, LinkedIn and other social profiles. Strongest for people with a corporate/professional footprint; weak for individuals with no business presence. Useful for confirming employment and finding a reachable email/phone to corroborate identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a sock-puppet account at https://rocketreach.co (free tier gives limited monthly credits).
2. Search by `name` + `employer-org`, or browse a company to its people list.
3. Reveal a contact — email and social links are usually available on the free tier; phone numbers and bulk export typically require a paid plan or the API.
4. Verify: run any returned `email` through validation and any `phone` through phone-OSINT before trusting it.
5. Pivot: a confirmed work email feeds breach/email tooling; a LinkedIn/social link feeds profile enrichment.

## Inputs → Outputs
- **In:** `name` + `employer-org` (or company domain)
- **Out:** `email` (work/inferred), `phone` (often gated behind paid tier), `social-profile` (LinkedIn etc.)
- **Empty/negative result looks like:** "no results" or only a name with no revealable contacts — common for people outside the professional/corporate world, or when credits are exhausted.

## Gotchas & OpSec
- Human-in-the-loop: account login is mandatory, and the best data (phone, volume) sits behind a paywall — the free tier is a teaser.
- Data is aggregated and inferred; a returned email may be a pattern-guess. Always verify, never cold-trust.
- OpSec: **active** — your searches are logged to your account; use a burner identity and keep the target's name out of shared workspaces.

## Overlaps ("do both")
- Pairs with `[[hunter-io]]` — Hunter is stronger on domain-wide email patterns, RocketReach on person-level phone/social. Cross-check the email each returns.

## Trust & verifiability
`trust: community` — a well-known commercial provider, but the data is aggregated and probabilistic; treat every field as a lead to verify, not fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rocketreach-co |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → email, phone, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
