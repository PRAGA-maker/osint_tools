---
id: truecaller-com
name: Truecaller
description: Use when you have a `phone` number and want the name/caller-ID the crowd has associated with it — returns a likely owner name, location/carrier, and spam flags.
url: https://www.truecaller.com
category: phone
path:
- phone
bestFor: Crowd-sourced caller-ID lookup — resolving a phone number to a likely name and location.
selectorsIn:
- phone
selectorsOut:
- name
- address
- social-profile
status: live
pricing: freemium
costNote: Free basic lookups but the web/app now requires signing in with an account; deeper features (unlimited lookups, full name/details, who-viewed) sit behind Truecaller Premium.
opsec: active
opsecNote: Truecaller ties lookups to your account and historically uploads/records activity; searching a number can consume from your quota and is logged against your identity. Use a sock-puppet account, and be aware that installing the app can upload your own contacts. The number's owner is not directly notified of a lookup.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Names come from crowd-sourced address books and user tags, not an authoritative registry — often right, but can be outdated, mislabeled, or reflect a previous owner of a recycled number.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- truecaller.com
- Truecaller
tags:
- phone
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- true-caller
- truecaller
---

# Truecaller

> The largest crowd-sourced caller-ID service — resolves a phone number to the name millions of users' address books have attached to it, plus spam/location signals.

## When to use
You have a `phone` number and want a likely owner `name` and rough location/carrier — the classic "who does this number belong to" step. Strong lead-generation for missing-person and identity work because it draws on real people's contact lists, though the attribution is crowd-sourced and needs corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign into Truecaller (use a **sock-puppet** account) at https://www.truecaller.com or the app.
2. Enter the `phone` number in international format.
3. Read the result: the crowd-associated `name`, spam/flag status, carrier/region, and sometimes a linked profile or `address` hint.
4. Note free lookups are limited; deeper detail may prompt Premium. Don't upload your real contacts.
5. Pivot: a resolved `name` feeds people-search; carrier/region narrows `geolocation`; a linked profile feeds social enumeration.

## Inputs → Outputs
- **In:** `phone` number
- **Out:** likely owner `name`, spam status, carrier/region, sometimes `social-profile`/`address` hints
- **Empty/negative result looks like:** "unknown"/no name — the number isn't in the crowd data (common for new or privacy-conscious numbers). A name shown may be stale or the previous holder of a recycled number.

## Gotchas & OpSec
- Login required: web and app now gate lookups behind an account; use a throwaway.
- Crowd-sourced accuracy: names can be wrong, joke labels, or outdated — always corroborate before acting.
- Privacy footprint: installing the app can upload your address book; prefer the web lookup with a sock puppet.

## Overlaps ("do both")
- Pairs with other phone-intel tools and people-search — Truecaller gives the crowd name, then `[[ussearch-us]]`/carrier lookups verify the owner and add address/associates.

## Trust & verifiability
`trust: unverified` — crowd-sourced caller-ID, not an authoritative registry; treat the name as a strong lead to confirm, especially on recycled numbers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truecaller-com |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
