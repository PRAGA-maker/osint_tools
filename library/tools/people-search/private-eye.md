---
id: private-eye
name: PrivateEye
description: Use when you have a `name`, `phone`, or `email` and want a US people-search profile — returns address, phone, and associate (relatives) leads.
url: https://www.privateeye.com
category: people-search
path:
- people-search
bestFor: Building a US contact/associate profile — addresses, phones, relatives — from a name, phone, or email.
selectorsIn:
- name
- phone
- email
selectorsOut:
- address
- phone
- associate
status: live
pricing: freemium
costNote: Free to run a search and see summary matches; the full report (unredacted contact details, background records) is a paid unlock.
opsec: passive
opsecNote: Searching does not notify the subject. PrivateEye aggregates public records; browse from a sock-puppet context and never use it for FCRA-regulated purposes (it explicitly is not a consumer reporting agency).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial US people-search brand drawing on public-records aggregators; broad but with the usual data-broker error rate — stale addresses and mismatched relatives occur.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- people-search-2
- truepeoplesearch
- intelius
aliases:
- PrivateEye.com
- Private Eye people search
tags:
- people-search
- data-broker
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# PrivateEye

> A commercial US people-search engine: name, phone, or email in — address history, phones, and relatives out, with a paid full report for the details.

## When to use
You have a `name` (ideally + city/state), a `phone`, or an `email` for a US subject and want a contact/associate profile. PrivateEye is a solid breadth pass alongside other brokers: it returns prior addresses, phone numbers, and relatives (`associate` leads) from 100B+ public records. Use it to generate leads and cross-check, since no single broker is complete or fully current.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.privateeye.com and pick the search type: name, reverse phone, or email.
2. Enter the selector; narrow a common `name` with city/state.
3. Read the free summary matches: approximate age, city, partial relatives/addresses. Match on age + location + relatives before trusting a result.
4. The full report (complete addresses, unredacted phones, background records) is paywalled — decide if you need it or can corroborate free elsewhere.
5. Pivot: relatives feed associate mapping; a phone feeds reverse-phone tools; an address feeds reverse-address/property records.

## Inputs → Outputs
- **In:** `name`, `phone`, or `email`
- **Out:** `address` (history), `phone`, `associate` (relatives), approximate age
- **Empty/negative result looks like:** no match, or only generic same-name entries with no corroborating relatives/age — treat as "not found here," try another broker.

## Gotchas & OpSec
- Aggregated broker data — expect stale addresses and occasional wrong relatives; corroborate across sources.
- Full detail is paywalled; the free tier is lead-generation.
- Not FCRA-compliant — do not use for employment, tenant, or credit decisions.

## Overlaps ("do both")
- Pairs with `[[people-search-2]]` (Radaris), `[[truepeoplesearch]]`, and `[[intelius]]` — overlapping US brokers with different coverage. Run several and intersect; each catches records the others miss.

## Trust & verifiability
`trust: community` — an established commercial broker with wide US coverage but standard aggregated-data caveats. Use it to generate leads, then verify each against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | private-eye |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email → address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
