---
id: my-life-people-search
name: MyLife People Search
description: Use when you have a `name` for a US subject and want an aggregated profile with a "reputation" angle — returns age, address history, phones, relatives, and a MyLife reputation score.
url: https://www.mylife.com/people-search
category: people-search
path:
- people-search
bestFor: Aggregated US people lookup (age, addresses, relatives, phones) plus MyLife's reputation/background teaser.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Free teaser (name, age, city, partial relatives, a "reputation score"). Full background details are paywalled behind a paid MyLife subscription, which is known for aggressive upsell and hard-to-cancel billing.
opsec: passive
opsecNote: Querying is passive — the subject is not notified of a search. However, MyLife is notorious for creating profiles and using dark-pattern billing; use a sock-puppet email/account and disposable payment if you ever subscribe, and never enter real personal details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial data broker with a poor reputation for accuracy and manipulative billing; its "reputation scores" are marketing, not fact. Treat all fields as unverified leads.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- MyLife
- mylife.com
tags:
- people-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# MyLife People Search

> A US people-search broker that wraps public-records aggregation in a "reputation score" gimmick — useful for address/relative leads, infamous for upsell and accuracy problems.

## When to use
You have a US subject's `name` (with a city/state to disambiguate) or a `phone`, and you want another broker's take on their age, address history, and relatives — worth running alongside other US people-search sites because vendors buy from different suppliers and surface different records. Ignore the "reputation score" as a signal; it's marketing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mylife.com/people-search in a clean/sock-puppet browser.
2. Enter the `name` (+ location) or `phone`.
3. Read the free teaser: matched names, approximate age (`dob` band), current city, partial relatives, and a "reputation score."
4. Decide before paying — the full report is a paid subscription with aggressive upsell; only subscribe with a disposable email/payment and cancel promptly, or skip and get the same fields from a cheaper source.
5. Pivot: relatives feed further people-search; an address feeds property/records; a phone feeds `[[phone]]` lookups.

## Inputs → Outputs
- **In:** `name` (+ city/state) or `phone`
- **Out:** age/`dob` band, `address` history, `phone`, relatives/`associate`s
- **Empty/negative result looks like:** only same-name strangers, or a teaser that won't resolve without payment. A common name with no location anchor is inconclusive.

## Gotchas & OpSec
- Dark-pattern billing: MyLife is widely reported for hard-to-cancel subscriptions and auto-created profiles — treat the paywall with caution.
- Accuracy: data is often stale or merged across same-name people; the reputation score is not evidence.
- Not FCRA: results are not for employment/tenant screening.

## Overlaps ("do both")
- Pairs with `[[ussearch-us]]` and other US brokers — run several and reconcile, because each vendor's supplier mix surfaces different addresses and relatives; don't rely on MyLife alone.

## Trust & verifiability
`trust: unverified` — a commercial broker with a poor accuracy/ethics reputation; every field is a lead to corroborate against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-life-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
