---
id: predicta-search
name: Predicta Search
description: Use when you have an `email`, `phone`, `username`, or `name` and want a correlated digital-footprint report of linked accounts across many platforms — returns social-profile, name and image.
url: https://predictasearch.com
category: social-networks
path:
- social-networks
bestFor: One-query reverse lookup of an email/phone into a correlated set of linked social and web accounts.
selectorsIn:
- email
- phone
- username
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: freemium
costNote: Registration required; runs on a credit model. There is a free trial (no card), after which searches consume purchased credits. Without an account/credits you get no results.
opsec: passive
opsecNote: A third-party correlation engine — it queries public sources and its own data, and does not notify the target. However, you must create an account and pay, so your identity is known to the vendor; use investigation-dedicated account details and be mindful the vendor logs your queries.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial OSINT vendor (Predicta Lab) widely used by investigators; results are correlated leads that still require manual verification and can include false links.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- PredictaSearch
- Predicta Lab
- predictasearch.com
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- digital-footprint
- reverse-lookup
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Predicta Search

> A commercial reverse-lookup engine that turns an email or phone into a correlated map of the person's linked accounts across many platforms.

## When to use
You have an `email`, `phone`, `username`, or `name` and want a fast, broad correlation of where that identifier appears online — which social networks, messaging apps, and web services it is tied to. It is strongest as an email/phone → account-graph tool, useful early to establish the shape of a subject's digital footprint before manual deep-dives. Reach for it when you have credits and need breadth quickly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://predictasearch.com and sign in / start the free trial (registration required).
2. Choose the input type and enter the `email`, `phone`, `username`, or `name`.
3. Run the search (consumes a credit). Review the returned account graph: platforms where the identifier is registered, linked profile URLs, and any surfaced display names / avatars.
4. Manually open and verify each linked profile — correlation is probabilistic and can include coincidental or outdated links.
5. Pivot: confirmed profiles feed platform-specific enrichment; a newly-found username feeds cross-site sweeps; an avatar feeds reverse-image search.

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, or `name`
- **Out:** `social-profile` links, `name`, `image` (avatars)
- **Empty/negative result looks like:** an empty report (and no credit refund) — the identifier isn't correlated in their sources; absence is not proof the person has no accounts.

## Gotchas & OpSec
- Human-in-the-loop: account creation and credits are mandatory; the free trial is limited.
- Correlations can be wrong — always click through and verify before treating a linked account as the same person.
- The vendor knows who you are and logs queries; use investigation-dedicated billing/identity where policy allows.

## Overlaps ("do both")
- Pairs with free email-to-profile tools (e.g. Epieos-style checks) and username sweeps — run the free tools first, then spend a Predicta credit for the broader correlation, and cross-check the two to filter false links.

## Trust & verifiability
`trust: community` — an established commercial OSINT vendor. Its output is a strong lead set, not verified fact; the paywall/registration and credit model gate access and tie usage to your account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | predicta-search |
| category | social-networks |
| selectorsIn → selectorsOut | email, phone, username, name → social-profile, name, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
