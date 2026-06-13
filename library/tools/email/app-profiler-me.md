---
id: app-profiler-me
name: app.profiler.me
description: Use when you have an `email` (or `phone`/`username`) and want the registered accounts and social profiles tied to it — returns linked services and profile data.
url: https://app.profiler.me
category: email
path:
- email
bestFor: Reverse-resolving an email/phone/username to the online accounts and profiles it's registered on.
selectorsIn:
- email
- phone
- username
selectorsOut:
- social-profile
- name
- username
status: degraded
pricing: freemium
costNote: App is account-gated with Purchase/Billing (credit) menus, implying a paid/credit model with a possible limited free tier; exact free allowance not confirmed from the public page.
opsec: passive
opsecNote: Reverse lookups query the provider's data/connectors, not the target directly. You disclose the queried selector to profiler.me — use a research account, not your own identifiers.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial OSINT lookup web app (Search/History/Purchase/Billing). The public landing page is a JS SPA that did not expose feature detail to fetch; capabilities inferred from the app nav and uk-osint listing.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- behindtheemail-com
- account-live-com
aliases:
- Profiler
- profiler.me
tags:
- email
- Email Related Sites
- account-discovery
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# app.profiler.me

> A commercial OSINT lookup app that reverse-resolves an email (or phone/username) into the online accounts and profiles registered to it.

## When to use
You have an `email`, `phone`, or `username` for the subject and want to discover which services it is registered on and any linked `social-profile`/`name`. Useful early in an investigation to widen one identifier into a footprint to pivot through.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://app.profiler.me and sign up / log in (the app gates Search behind an account).
2. Use the Search tab; enter the `email` (or `phone`/`username`) selector.
3. Review the returned linked accounts/profiles; the History tab retains prior queries.
4. Top up credits via Purchase/Billing if the lookup is gated.
5. Pivot: take discovered `social-profile`s into the social-networks tools and confirmed `email` into `[[behindtheemail-com]]`.

## Inputs → Outputs
- **In:** `email`, `phone`, or `username`
- **Out:** `social-profile`s, registered services, `name`/`username` correlations
- **Empty/negative result looks like:** no linked accounts returned — treat as low footprint for that selector, not as identity-cleared.

## Gotchas & OpSec
- Human-in-the-loop: account registration is required and lookups appear credit/paywall-gated; the free allowance is not documented on the public page.
- Status **degraded** for reference purposes: the landing page is a JS SPA that did not surface feature/pricing detail to automated fetch — verify capabilities and current pricing live before relying on it.
- OpSec: passive toward the target, but you reveal the queried selector to the vendor; never query your own real identifiers.

## Overlaps ("do both")
- Pairs with `[[behindtheemail-com]]` — both turn an email into a profile via different connectors; run both and reconcile to reduce single-source error.

## Trust & verifiability
`trust: unverified` — a commercial lookup app whose data sources are not disclosed and whose public page did not expose details to fetch; corroborate every result against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-profiler-me |
| category | email |
| selectorsIn → selectorsOut | email, phone, username → social-profile, name, username |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
