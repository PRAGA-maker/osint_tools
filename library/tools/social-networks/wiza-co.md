---
id: wiza-co
name: Wiza
description: Use when you have a `name` + `employer-org` or a LinkedIn `social-profile` and want a verified work `email` and `phone` — returns `email`, `phone`, `employer-org`.
url: https://wiza.co/
category: social-networks
path:
- social-networks
bestFor: Turning a LinkedIn profile or name+company into a verified business email and phone number.
selectorsIn:
- social-profile
- name
- employer-org
selectorsOut:
- email
- phone
- employer-org
status: live
pricing: freemium
costNote: Freemium — a limited number of free verified credits to start, then pay-per-valid-email (you are only charged for contacts that verify). Registration required; real volume is paid.
opsec: active
opsecNote: This queries a B2B data broker for the target's contact details and requires you to register an account, so your identity/billing is tied to the lookup. The subject is not notified, but you are leaving a trail with Wiza. Use a dedicated investigative account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Wiza is an established commercial sales-intelligence vendor; data is aggregated/inferred, so emails are "verified deliverable" but not guaranteed to be the person's primary or current address.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Wiza LinkedIn email finder
tags:
- linkedin
- LinkedIn & Similar Sites
- email-finder
- b2b-data
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Wiza

> A LinkedIn-centric B2B contact finder: feed it a profile or name+company and it returns a verified work email and often a phone number.

## When to use
You have a subject's professional identity — a LinkedIn `social-profile`, or a `name` plus `employer-org` — and you need a contact channel: their work `email` and possibly a direct `phone`. Strong for locating employed professionals; weak for people with no corporate/LinkedIn footprint. Because it verifies deliverability, a returned email is a usable pivot for account-existence and breach checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a (dedicated, non-personal) Wiza account; install the Chrome extension if you want to enrich directly from a LinkedIn profile page.
2. Provide the input: a LinkedIn profile URL, or search by name + company/title/location.
3. Run the enrichment; Wiza returns verified email(s), phone, current title and company, and other firmographic data points.
4. Note that you are typically charged only for contacts that verify — read the credit/plan limits before bulk work.
5. Pivot: feed the `email` into account-existence and breach-lookup tools, and the `phone` into phone-OSINT.

## Inputs → Outputs
- **In:** `social-profile` (LinkedIn), or `name` + `employer-org`
- **Out:** verified `email`, `phone`, current `employer-org`/title
- **Empty/negative result looks like:** no verified email found — the person may not be in B2B datasets, may have left the company, or uses a non-standard address; absence is not proof they lack an email.

## Gotchas & OpSec
- Requires an account and, past the free credits, payment — your billing identity is attached to lookups.
- Data is broker-aggregated and inferred; "verified" means the mailbox accepts mail, not that it's the person's main/current address.
- Best for corporate professionals; returns little for people outside the LinkedIn/B2B world.
- An API exists for programmatic enrichment at scale.

## Overlaps ("do both")
- Pairs with other email-finders (Hunter, Apollo) and with LinkedIn manual review — vendors' datasets differ, so cross-check a found email before relying on it.

## Trust & verifiability
`trust: community` — a legitimate commercial vendor, but the underlying data is aggregated/inferred; always confirm a returned email with an independent existence check before treating it as the subject's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiza-co |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, name, employer-org → email, phone, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
