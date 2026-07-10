---
id: spokeo
name: Spokeo
description: Use when you have a `name`, `email`, `phone`, or `username` and want a consolidated US person report that also links social profiles — returns address, phone, email, associates, and social-profile.
url: https://www.spokeo.com
category: people-search
path:
- people-search
bestFor: Consolidated US people search that ties an email/username/phone to a person and their social profiles.
selectorsIn:
- name
- email
- phone
- username
- address
selectorsOut:
- address
- phone
- email
- social-profile
- associate
- dob
status: live
pricing: freemium
costNote: Free search shows a teaser (locations, relatives count, partial data); full reports require a paid subscription (low intro price, then recurring — watch auto-renew).
opsec: passive
opsecNote: Commercial data-broker aggregation; the subject is not notified. You disclose the searched selector and your payment identity to Spokeo. Not FCRA-permissible for employment/tenant/credit use.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Aggregated public + social + marketing data; strong at email/username→identity but prone to record-mixing and stale entries, like all brokers.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- beenverified-com
- truepeoplesearch
- pipl
aliases:
- spokeo.com
tags:
- people-investigations
- people-search
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Spokeo

> A US people-search broker whose distinctive strength is reverse lookups — turning an `email`, `username`, or `phone` into a named person and their linked social profiles.

## When to use
You have a bare `email`, `username`, or `phone` (or a name) and want to attach an identity plus social-profile links, address history, and relatives. Spokeo is especially useful when you're starting from an online selector rather than a name, which is common when a missing person's only trace is an account or a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spokeo.com and choose the search type (name, email, phone, username, or address).
2. Read the free teaser: cities, relative/associate counts, and which social networks matched.
3. To see full details, start a paid report — note the low intro price auto-renews; cancel promptly for one-offs.
4. Confirm identity (age/cities/known accounts) before trusting linked profiles — brokers mix similar records.
5. Pivot: linked social profiles feed content review; relatives feed an associate map; addresses feed property/neighbor tools.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, `username`, or `address`
- **Out:** `address` (history), `phone`, `email`, `social-profile`, `associate` (relatives), `dob`/age
- **Empty/negative result looks like:** a thin teaser or "no results" — common for young people, recent movers, and opt-outs. Absence is weak evidence; cross-check free aggregators.

## Gotchas & OpSec
- Human-in-the-loop: full data behind a paid, auto-renewing subscription.
- OpSec: **passive** toward the subject; you disclose the selector + payment to the broker.
- Legal: no FCRA-permissible uses (employment/tenant/credit).

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]` — free aggregator to validate Spokeo's teaser (addresses/relatives) before paying.
- Pairs with `[[beenverified-com]]` and `[[pipl]]` — different broker blends; cross-run to catch what one misses, especially for email/username reverse lookups.

## Trust & verifiability
`trust: unverified` — a commercial broker aggregating public, social, and marketing data; good for lead generation and reverse lookups but prone to record-mixing, so corroborate every field.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spokeo |
| category | people-search |
| selectorsIn → selectorsOut | name, email, phone, username, address → address, phone, email, social-profile, associate, dob |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
