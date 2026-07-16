---
id: peoplebyname-us
name: Peoplebyname (US)
description: Use when you have a US `name` and want a free first-pass on their address, landline phone and likely relatives — returns directory-style `address`/`phone`/`associate` leads to verify elsewhere.
url: http://www.peoplebyname.com
category: people-search
path:
- people-search
bestFor: A quick, free US name-to-address/phone/relatives lookup as a starting point before paid people-search.
selectorsIn:
- name
selectorsOut:
- address
- phone
- associate
status: live
pricing: free
costNote: Free directory-style lookup; results are limited and often act as a teaser toward paid people-search partners.
opsec: passive
opsecNote: Read-only directory search; the subject is not notified. As with any aggregator, the site logs your queries — use a clean/sock-puppet browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free people-directory aggregator built on public phone/address listings; data is often stale and incomplete, so treat every hit as a lead to corroborate.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thats-them
- peekyou
- peoplebyname-reverse-phone-lookup
aliases:
- peoplebyname.com
- People By Name
tags:
- people-search
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Peoplebyname (US)

> A free US name-directory lookup — quick first-pass for an address, landline, and probable relatives before you spend on paid people-search.

## When to use
You have a US `name` and want a zero-cost starting point: a possible current/prior `address`, a landline `phone`, and a list of likely relatives/associates (`associate`) to help disambiguate common names. Best treated as a cheap first sweep whose hits you then confirm against stronger sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.peoplebyname.com.
2. Enter the subject's `name` (and state if the interface allows) and search.
3. Read the results: directory-style entries with address, landline, and associated names. Use the relatives to pick the right person among namesakes.
4. Corroborate before relying on anything — this data is often years out of date.
5. Pivot: a relative's `name` or a `phone` feeds `[[thats-them]]` and reverse-phone tools; an `address` feeds property and mapping lookups.

## Inputs → Outputs
- **In:** `name` (+ optional US state)
- **Out:** `address` (current/prior), landline `phone`, `associate` (likely relatives)
- **Empty/negative result looks like:** no listing, or only a paywalled teaser — meaning the person isn't in the free directory (common for younger people, mobile-only numbers, or the unlisted). Absence proves nothing.

## Gotchas & OpSec
- Landline-era data: skews toward older, listed individuals; misses mobile-only and younger subjects.
- Often funnels you toward a paid partner — don't pay here; take the free leads elsewhere.
- Stale addresses are common; always confirm currency.
- OpSec: **passive** — a directory read; the subject isn't alerted.

## Overlaps ("do both")
- Pairs with `[[thats-them]]` and `[[peekyou]]` — cross-check the free address/phone/relatives here against those aggregators to separate real matches from stale or wrong-person data.

## Trust & verifiability
`trust: unverified` — a free aggregator over public listings; treat every field as a lead to corroborate, never as confirmed fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peoplebyname-us |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
