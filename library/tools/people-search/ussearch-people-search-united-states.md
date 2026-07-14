---
id: ussearch-people-search-united-states
name: US Search (People Search, United States)
description: Use when you have a US name (optionally a city/state) and want an aggregated people report — returns addresses, phone numbers, relatives and associated records.
url: http://www.ussearch.com
category: people-search
path:
- people-search
bestFor: A mainstream US people-search aggregator for current/past addresses, phones and relatives from a name.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Free to run a search and see teaser results (name/age/city, relatives), but the full report — full address history, phone numbers, records — is behind a paid subscription/one-off purchase. Effectively pay-to-view detail.
opsec: passive
opsecNote: Searches query US Search's aggregated broker data, not the target, so no notification reaches the subject. Buying a report requires an account and payment, which identifies you to the vendor. Note US Search is subject to opt-out; some subjects will be absent because they opted out, not because no record exists.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial people-search (PeopleConnect/Intelius family); broad US coverage but data-broker sourcing that can be stale or conflated — treat as leads to verify, and it is explicitly not for FCRA uses.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USSearch
- ussearch.com
- US Search people finder
tags:
- toddington
- curated-directory
- people-search
- data-broker
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# US Search (People Search, United States)

> A mainstream US data-broker people-search — enter a name and get a person's address history, phones and relatives, with the detail gated behind payment.

## When to use
You have a US `name` (ideally plus a city/state to disambiguate), or a `phone`/`address` to search in reverse, and you want the broker-aggregated picture: current and prior addresses, associated phone numbers, approximate age, and — most usefully for missing-persons work — **relatives and associates**. US Search is one of the long-standing consumer people-search sites, so it's a reasonable stop alongside its peers (its data overlaps heavily with the Intelius/PeopleConnect family).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ussearch.com and search by `name` (add city/state), or use the reverse `phone`/`address` search.
2. Read the **free teaser**: age, current city, and often a relatives list — valuable even without buying.
3. To see full address history, phone numbers and records, purchase/subscribe (account + payment required).
4. Extract the concrete selectors and note that each is a broker claim to verify.
5. Pivot: relatives/associates (`associate`) feed further people-search and social lookups; an address feeds property/electoral records; a phone feeds reverse-phone tools.

## Inputs → Outputs
- **In:** `name` (+ city/state), or reverse `phone`/`address`
- **Out:** `address` history, `phone` numbers, `associate`s (relatives), approximate `dob`/age
- **Empty/negative result looks like:** no match or only a thin teaser. Absence may mean the person opted out, is young/low-footprint, or the record is under a variant name — not proof they don't exist. Cross-check other brokers.

## Gotchas & OpSec
- **Freemium/pay-to-view:** the teaser is free; real detail costs money and needs an account.
- Data-broker accuracy caveats apply — addresses and relatives can be stale or belong to a same-named person; verify before acting.
- Explicitly **not for FCRA purposes** (employment/housing/credit) — investigative/locate use only.
- Opt-out means some subjects are deliberately missing.

## Overlaps ("do both")
- Pairs with `[[anywho-whitepages-north-america]]`-style directories and other brokers — their datasets differ at the margins; run several and reconcile.
- Feeds `[[free-public-records-directory-us]]` to confirm a broker lead against an official record.

## Trust & verifiability
`trust: community` — a commercial aggregator with broad but unverified sourcing; treat every field as a lead and confirm addresses, relatives and phones against primary sources before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ussearch-people-search-united-states |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
