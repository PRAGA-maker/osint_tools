---
id: behindtheemail-com
name: behindtheemail.com
description: Use when you have an `email` and want the person behind it — name, jobs, education, social profiles, location and breach exposure — returns an aggregated identity profile.
url: https://behindtheemail.com/
category: email
path:
- email
bestFor: Resolving an email into a full person profile (name, socials, employer, location, breaches).
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Tiered plans with per-day search limits that reset daily; upgrade if you exceed the tier. Payment via card (Stripe). A free/entry tier exists; exact limits set on the pricing page.
opsec: passive
opsecNote: Correlates publicly available data across many sources; it does not contact the target. You disclose the queried email to behindtheemail — use a research account.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial email-to-person enrichment platform (profiles, socials, breaches, exports, REST API). Aggregated data — verify before acting.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- app-profiler-me
- arkowl-com
- anymailfinder-com
aliases:
- Behind The Email
tags:
- email
- Email Related Sites
- email-enrichment
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# behindtheemail.com

> Despite the name, this is an email-to-person enrichment engine, not a header analyzer — feed an address, get the human profile behind it.

## When to use
You have a confirmed `email` for the subject and want the identity it maps to: real `name`, job titles/`employer-org`, education, social profiles (LinkedIn, GitHub, TikTok, etc.), `geolocation`/location data, Google Maps contributions, and breach exposure. A strong second source to corroborate `[[app-profiler-me]]` or `[[arkowl-com]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://behindtheemail.com/ (entry tier with a daily search cap).
2. Submit the target `email`; the service validates format and queues a correlation request.
3. Read the returned profile — professional history, education, social handles, location, breaches.
4. For volume, use bulk analysis and Excel/CSV export, or the REST API.
5. Pivot: discovered `social-profile`s go to social-networks tools; `employer-org` goes to people/biz search; cross-check `name` against people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** `name`, `social-profile`s, `employer-org`, `geolocation`, breach exposure
- **Empty/negative result looks like:** thin or empty profile — common for low-footprint or freshly created addresses; absence is not disproof.

## Gotchas & OpSec
- Human-in-the-loop: account registration required; tiers cap daily searches and full output is paywalled.
- OpSec: passive (no target contact), but you reveal the queried email to the vendor; use a research identity.
- Aggregated/correlated data can mis-merge two people who share a name — verify each linked profile independently.

## Overlaps ("do both")
- Pairs with `[[app-profiler-me]]` and `[[arkowl-com]]` — overlapping email-to-identity engines with different sources; run two and reconcile. Use after `[[anymailfinder-com]]` has found/verified the address.

## Trust & verifiability
`trust: community` — a commercial aggregator surfaced via uk-osint; profiles are leads to confirm, and name-collisions are a real risk, so verify each component against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | behindtheemail-com |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile, employer-org, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
