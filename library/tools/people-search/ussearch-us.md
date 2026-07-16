---
id: ussearch-us
name: USSEARCH (US)
description: Use when you have a `name`, `phone`, or `address` for a US subject and want to pull an aggregated public-records profile — returns address history, phone, relatives, and age/dob hints.
url: https://www.ussearch.com
category: people-search
path:
- people-search
bestFor: Aggregated US public-records lookup (address history, relatives, phones) from a name, phone, or address.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- email
- associate
- dob
status: live
pricing: freemium
costNote: Free search returns teaser results (name, approximate age, city, partial relatives). The full report (complete address history, phone numbers, possible relatives/associates) is paywalled behind a paid membership/one-off report purchase.
opsec: passive
opsecNote: Querying is passive — the subject is not notified and USSearch does not alert them. You are, however, handing your search terms to a commercial data broker; use a sock-puppet account/email and a clean IP if you buy a report, and never enter your real payment identity on an investigation you want kept quiet.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial people-search broker (PeopleConnect/Intelius family). Data is aggregated from public records and marketing sources, so it can be stale, merged across same-name individuals, or wrong — corroborate before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- US Search
- ussearch.com
tags:
- people-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- ussearch-people-search-united-states
---

# USSEARCH (US)

> A long-running US people-search broker that turns a name/phone/address into an aggregated public-records profile — address history, relatives, and contact numbers.

## When to use
You have a US subject's `name` (ideally with a city/state to disambiguate), or a `phone`/`address` you want to attribute, and you need an address history plus likely relatives and phone numbers to build out a subject's footprint. Strong for reconstructing where someone has lived and who they are connected to — useful early in a missing-person workup to generate leads (last-known addresses, family to contact).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ussearch.com in a clean/sock-puppet browser session.
2. Choose the search type (name, phone, or address) and enter the input (`selectorsIn`). Add a state or city to cut down on same-name collisions.
3. Read the free teaser: matched names, approximate `dob`/age, current city, and a partial list of relatives. Use this to confirm you have the right person before paying.
4. If the teaser matches, purchase the report to unlock full `address` history, `phone` numbers, and `associate`/relative links. STOP if the teaser clearly isn't your subject — don't buy on a weak match.
5. Pivot: relatives feed further people-searches; an address feeds property/records tools; a phone feeds `[[phone]]` lookups.

## Inputs → Outputs
- **In:** `name` (+ city/state), `phone`, or `address`
- **Out:** `address` history, `phone`, possible `email`, `associate`/relatives, `dob`/age band
- **Empty/negative result looks like:** "No results found," or only same-name strangers in the wrong states — treat a common name with no location anchor as inconclusive, not as proof the person is absent.

## Gotchas & OpSec
- Human-in-the-loop: the useful fields are behind a **paywall** — expect to buy a report or start a membership to see full data.
- Data quality: broker aggregation merges records across people who share a name; verify age/location against a second source before acting.
- Not an FCRA consumer-reporting agency — results are not for employment/tenant screening, and legal use is limited to lawful investigative purposes.

## Overlaps ("do both")
- Pairs with `[[fastpeoplesearch-com]]` and other US brokers because each vendor buys from different data suppliers — one will surface an address or relative the other misses. Run several and reconcile.

## Trust & verifiability
`trust: unverified` — a commercial data broker, not an authoritative registry; treat every field as a lead to corroborate, especially on common names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ussearch-us |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
