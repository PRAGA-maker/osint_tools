---
id: intelius-people-search-engine
name: Intelius
description: Use when you have a US `name`, `phone`, or `address` and want a consolidated background profile — returns addresses, phones, relatives, and age/DOB (full report is paywalled).
url: https://www.intelius.com
category: people-search
path:
- people-search
bestFor: US background/people-search reports linking a person to addresses, phones, relatives, and age.
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
costNote: The search and a teaser (city/state, age range, partial relatives) are free, but the full report requires a paid subscription/one-time purchase. Budget for the paywall if you need the complete record.
opsec: passive
opsecNote: Intelius is a data-broker aggregator; searching does not notify the subject. Note that Intelius is FCRA-restricted — results may not be used for employment, tenant, or credit decisions. Use a sock-puppet account and payment method if attribution matters, and be aware the broker logs your queries.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established US data broker; coverage is broad but records mix current and decades-old data, so cross-checking is essential.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Intelius
- intelius.com
tags:
- toddington
- curated-directory
- people-search
- data-broker
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Intelius

> A mainstream US data-broker people-search — turns a name/phone/address into a consolidated profile of addresses, phones, relatives, and age.

## When to use
You have a US subject's `name` (ideally with a city/state), or a `phone` or `address` to reverse, and want a single report tying together their address history, phone numbers, likely relatives/associates, and age/DOB. Useful for building a starting skeleton on a US person, especially to generate relatives and prior addresses to chase.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.intelius.com`; pick People / Phone / Address search.
2. Enter the `name` + location (or the `phone`/`address`), and run the search.
3. Read the **free teaser**: city/state, approximate age, partial relative names — often enough to confirm you've found the right person.
4. For the full report (address history, full DOB, all phones/relatives), you must purchase/subscribe — decide if the paywall is worth it versus a free alternative.
5. Pivot: prior addresses feed property/records searches; relatives feed associate mapping; a phone feeds `[[www-spydialer-com]]`.

## Inputs → Outputs
- **In:** `name` (+ location), `phone`, `address`
- **Out:** `address` (history), `phone`, `associate` (relatives), `dob`/age
- **Empty/negative result looks like:** no matching person, or a teaser with no relatives/age — either a thin record or the wrong region. Common names need a location to disambiguate.

## Gotchas & OpSec
- Human-in-the-loop: the useful detail sits behind a **paywall**; the free teaser is often enough to confirm identity but not to enumerate everything.
- Legal: FCRA-restricted — do not use for employment/tenant/credit screening.
- Data mixes current and very old records; verify before asserting a "current" address.

## Overlaps ("do both")
- Pairs with other US people-search brokers — coverage differs between brokers, so a person thin on Intelius may be rich on another. Run more than one before concluding.

## Trust & verifiability
`trust: community` — a real, established broker with broad US coverage, but aggregated and time-mixed; treat every field as a lead to corroborate, not a verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelius-people-search-engine |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
