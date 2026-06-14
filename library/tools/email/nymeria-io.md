---
id: nymeria-io
name: nymeria.io
description: Use when you have a name + employer or a social/GitHub profile and want to find a person's email and contact data — returns email, phone, social profiles.
url: https://www.nymeria.io/blog/how-to-manually-find-email-addresses-for-github-users
category: email
path:
- email
bestFor: Contact/email enrichment from a name, company, or social profile (people-data B2B).
selectorsIn:
- name
- employer-org
- social-profile
- username
selectorsOut:
- email
- phone
- social-profile
- name
status: live
pricing: freemium
costNote: Free tier with limited credits; paid plans for bulk enrichment and API. Email-find is gated behind credits/subscription.
opsec: passive
opsecNote: Queries Nymeria's aggregated people-data index; no contact with the subject. Your searches are tied to your Nymeria account.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Nymeria is an established commercial people-data / contact-enrichment vendor; widely cited in OSINT email-finding lists. The harvested URL is a how-to blog post, but the underlying tool is the Nymeria platform/extension.
missingPersonsRelevance: high
coverage:
- global
- us
auth: account
api: true
localInstall: false
registration: true
aliases:
- Nymeria
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# nymeria.io

> Commercial people-data platform that resolves a name/company/profile into emails, phones, and linked social accounts.

## When to use
You have a `name` + `employer-org`, or a `social-profile` / `username` (e.g. a GitHub or LinkedIn handle), and you want a likely `email` and `phone` to pivot on. Strong when the subject has a professional footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a Nymeria account (free tier has a small credit allowance) or install the browser extension.
2. Search by name + company, or open a LinkedIn/GitHub profile with the extension active.
3. Reveal the enriched record — emails, phone(s), and linked social profiles.
4. Pivot the returned `email` to breach/account checks (`[[osintcat]]`, `[[osint-rocks]]`) and the social profiles to a username sweep.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `social-profile`, `username`
- **Out:** `email`, `phone`, `social-profile`, `name`
- **Empty/negative result looks like:** no enriched record / "no data" — common for people with little professional/online presence.

## Gotchas & OpSec
- Human-in-the-loop: account login required; full reveals consume credits / need a paid plan.
- Data skews toward business/professional contacts; weaker for minors or low-footprint subjects.
- OpSec: passive; searches are logged to your account — use a dedicated investigative account.

## Overlaps ("do both")
- Pairs with `[[pipl]]` (people search) and `[[osint-industries]]` (account/footprint mapping) — Nymeria leans toward business email/contact data.

## Trust & verifiability
`trust: community` — well-known commercial vendor frequently recommended for email discovery; treat individual records as leads to corroborate, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nymeria-io |
| category | email |
| selectorsIn → selectorsOut | name, employer-org, social-profile, username → email, phone, social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
