---
id: pipl-com
name: Pipl
description: Use when you have a `name`/`email`/`phone` and need deep identity resolution — but note Pipl is now an enterprise fraud/identity API, no longer a consumer people-search — returns linked identity, contact and social data to authorised business clients.
url: https://www.pipl.com/
category: people-search
path:
- people-search
bestFor: Enterprise identity resolution / fraud investigation that links a name, email or phone to a fuller identity — accessible only via a paid business account/API.
selectorsIn:
- name
- email
- phone
selectorsOut:
- email
- phone
- social-profile
- address
- associate
status: live
pricing: freemium
costNote: No longer free or consumer-facing. Pipl pivoted to an enterprise fraud-intelligence platform; access is via paid contracts / API (Contact Sales), typically for payment, marketplace and investigation teams — individuals cannot self-serve a search.
opsec: passive
opsecNote: Queries run against Pipl's own aggregated dataset via the API, not against the subject, so lookups are passive. But access requires a vetted business account, and use is governed by Pipl's terms and applicable privacy law (FCRA/GDPR) — do not assume personal or ad-hoc investigative use is permitted.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Pipl is a long-established, reputable identity-data company; its data is high quality, but it is now gated behind enterprise contracts, so most investigators will not have direct access.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- pipl.com
- Pipl SEARCH
- Pipl API
tags:
- peoplesearch
- People Search Sites
- identity-resolution
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Pipl

> Once the gold-standard consumer people-search, Pipl is now an enterprise identity-and-fraud API — powerful data, but behind a business paywall most investigators can't self-serve.

## When to use
You need to resolve a fragment — a `name`, `email`, or `phone` — into a linked identity (other contact points, social profiles, associates, locations). Historically Pipl was the go-to for this; today its capability is delivered as a B2B fraud-intelligence API to vetted organisations (payment platforms, marketplaces, investigation teams). Reach for it only if you (or your organisation) hold Pipl API access; otherwise treat this entry as a pointer to where that data now lives and choose an accessible alternative.

## How to use it (`bestInteractionPattern`: api)
1. Confirm your organisation has a Pipl contract/API key (individuals cannot sign up for ad-hoc searches).
2. Query the API with the known selector(s) — name, email, or phone — per Pipl's schema.
3. Read the resolved identity graph: linked emails/phones, social profiles, addresses, and associates, each with a match/confidence indicator.
4. Respect the permitted-use terms and applicable law (this is regulated identity data).
5. Pivot: resolved emails/phones feed `[[account-live-com]]`, `[[palenath]]`, and phone-OSINT; if you lack access, substitute `[[ufind-name]]`/`[[usphonebook]]` and manual enumeration.

## Inputs → Outputs
- **In:** `name`, `email`, or `phone`
- **Out:** linked `email`/`phone`, `social-profile`, `address`, `associate` — a resolved identity graph (to authorised clients only)
- **Empty/negative result looks like:** for most users, no access at all (the consumer search is gone); via the API, a low-confidence/empty match means the selector didn't resolve in Pipl's data.

## Gotchas & OpSec
- Access reality: the free/consumer Pipl search no longer exists — do not expect to type a name into pipl.com and get results.
- Regulated use: identity data carries legal constraints (FCRA/GDPR); confirm your use case is permitted.
- OpSec: passive against the subject, but every query is logged to your business account.

## Overlaps ("do both")
- Pairs with `[[ufind-name]]`/`[[usphonebook]]` — the accessible aggregators to fall back on when you lack Pipl access.
- Pairs with `[[palenath]]`/`[[account-live-com]]` — turn a Pipl-resolved email/phone into account enumeration.

## Trust & verifiability
`trust: trusted` — Pipl is a reputable, high-quality identity-data provider; the main caveat is access, since it is now enterprise-gated rather than open to individual investigators.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pipl-com |
