---
id: usa-official-com
name: usa-official.com (USA Official / OfficialUSA)
description: Use when you have a US `name` and want a free public-records aggregation — returns address history, phones, emails, DOB/age, relatives and links to official government directories.
url: https://usa-official.com/
category: people-search
path:
- people-search
bestFor: Free first-pass US person lookup pulling address history, phones, relatives and pointers into official state/county records.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- dob
- associate
status: live
pricing: free
costNote: Core name search and public-records results are free; the site monetizes via links to paid third-party report providers, so decline upsells to stay free.
opsec: passive
opsecNote: You query an aggregator, not the subject — no notification is sent to them. No login is required, so your search leaks only to the site operator. Use a clean/sock-puppet browser session as good hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregator of bulk US public records; broad but frequently stale and mixed across same-name individuals — treat every field as a lead to corroborate.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USA Official
- OfficialUSA
- usa-official.com
tags:
- peoplesearch
- People Search Sites
- public-records
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# usa-official.com (USA Official / OfficialUSA)

> A free US public-records aggregator: one name returns address history, phones, emails, age/DOB and relatives, plus links into official government directories.

## When to use
You have a US subject's `name` and want a free, no-login first pass before spending money on paid brokers. It aggregates people records (locations, phones, emails, DOB/age, relatives) and also indexes official directories (county, university, airport, business), so it doubles as a jumping-off point to authoritative government sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://usa-official.com/ in a clean/sock-puppet browser — no account needed.
2. Enter the subject `name` in the people search; where offered, add a state or city to disambiguate common names.
3. Read the result card: current/prior `address`, `phone` numbers, `email`, `dob`/age, and listed relatives/`associate`s.
4. Ignore "see full report" style buttons that hand off to paid brokers — the free listing is the value here.
5. Follow the official-directory links for authoritative records (property, court, business registration) to upgrade a broker-grade lead into a sourced fact.
6. Pivot: addresses/phones feed reverse lookups; relatives feed a fresh name search; official links feed public-records verification.

## Inputs → Outputs
- **In:** `name` (+ optional city/state)
- **Out:** `address` history, `phone`, `email`, `dob`/age, `associate`/relatives
- **Empty/negative result looks like:** no matching person card, or a card with only sparse historical data — for a common name, expect several conflated namesakes rather than one clean record.

## Gotchas & OpSec
- Human-in-the-loop: none for the free search; only the paid-broker upsells require registration/payment (skip them).
- Data quality: this is repackaged bulk public-records data — addresses lag reality and same-name people get merged. Corroborate before relying on any single field.
- OpSec: passive toward the subject; no login means minimal exposure. Still use a compartmentalized browser session.

## Overlaps ("do both")
- Pairs with `[[inteligator-people-trace-united-states]]` — run this free aggregator first, then decide whether Inteligator's paid depth adds anything, and use each to cross-check the other's relatives/addresses.

## Trust & verifiability
`trust: community` — it is a real, widely-used free aggregator, but it resells bulk public records with the usual staleness and name-conflation issues, so its output is corroboration-grade; its links to official government directories are where you upgrade a lead to a verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usa-official-com |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, dob, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
