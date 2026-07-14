---
id: people-search-2
name: Radaris
description: Use when you have a `name`, `phone`, or `address` and want a US people-search profile — returns address history, phone, associate (relatives), and employer-org.
url: https://radaris.com/
category: people-search
path:
- people-search
bestFor: Building a US person's profile — address history, phones, relatives, and past employers — from a name, phone, or address.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- employer-org
status: live
pricing: freemium
costNote: Free tier shows summary results (names, approximate age, city, partial relatives/phones). Full detailed reports and unredacted contact data are sold as paid reports.
opsec: passive
opsecNote: Searching Radaris does not notify the subject. Radaris itself aggregates from public/commercial sources; browse from a sock-puppet context and expect ad-heavy pages. Do not enter your own or the subject's data into any "claim/remove" flow.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial US data broker (15+ years); broad coverage but aggregated data with the usual broker error rate — stale addresses and mismatched relatives are common.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truepeoplesearch
- fastpeoplesearch
- thatsthem
aliases:
- Radaris people search
- Radaris reverse phone lookup
tags:
- peoplesearch
- data-broker
- reverse-phone
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Radaris

> A broad US people-search and data-broker engine: name, phone, or address in — address history, phones, relatives, age, and past workplaces out.

## When to use
You have a `name` (ideally + city/state), a `phone`, or an `address` for a US subject and want to assemble a contact/associate profile. Radaris is a good breadth pass: it typically returns prior addresses, associated phone numbers, relatives (`associate` leads), approximate age, and old employers/property. Use it early to generate leads and cross-check against other brokers, since any single broker is patchy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://radaris.com/ and pick the search type: people (name), reverse phone (`/phone-lookup`), or reverse address (`/reverse-address-lookup`).
2. Enter the selector; narrow a common `name` with city/state.
3. Read the free summary: candidate matches with approximate age, current city, partial relatives and phones. Match on age + location + relatives before trusting a result.
4. The detailed report (full addresses, unredacted phones) is paywalled — decide if you need it or can corroborate free elsewhere.
5. Pivot: relatives feed `associate` mapping; a phone feeds reverse-phone tools; an address feeds reverse-address and property records.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `address` (history), `phone`, `associate` (relatives), `employer-org` (past workplaces), approximate age
- **Empty/negative result looks like:** no matching profile, or only generic same-name entries with no corroborating relatives/age — treat as "not found here," not as ground truth; try another broker.

## Gotchas & OpSec
- Aggregated broker data — expect stale addresses and occasionally wrong relatives; corroborate across at least two independent sources before relying on a datapoint.
- Detailed data is paywalled; the free tier is lead-generation, not the full picture.
- Passive, but the site is ad/upsell heavy — never submit your own identity or use the "remove my info / claim" flows during an investigation.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]` and `[[fastpeoplesearch]]` — free brokers with different coverage; run several and intersect the results, because each misses records the others catch. `[[thatsthem]]` adds email/phone reverse pivots.

## Trust & verifiability
`trust: community` — a large, established commercial broker with wide US coverage, but standard aggregated-data caveats apply. Use it to generate leads, then verify each lead against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search-2 |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
