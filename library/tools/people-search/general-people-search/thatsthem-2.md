---
id: thatsthem-2
name: ThatsThem
description: Use when you have a `name`, `address`, `phone`, `email`, or `ip-address` and want free reverse-lookup contact details — returns name, address, phone, email, and associate links.
url: https://thatsthem.com/name-address-search
category: people-search
path:
- people-search
- general-people-search
bestFor: Free US reverse lookups pivoting between name, address, phone, email, and IP.
selectorsIn:
- name
- address
- phone
- email
- ip-address
selectorsOut:
- name
- address
- phone
- email
- associate
status: live
pricing: freemium
costNote: Free web lookups with no account for basic searches; soft daily limits apply. A paid API is offered for bulk/programmatic use.
opsec: passive
opsecNote: Standard aggregator query — the subject is not notified. No account needed, so a clean sock-puppet browser is enough. Data is scraped/compiled from public records and marketing sources; treat as leads.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial people-search aggregator compiling public-record and marketing data; coverage and accuracy vary and records can be stale — corroborate before relying.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- fastpeoplesearch
- truepeoplesearch
- whitepages-com
aliases:
- That's Them
- thatsthem.com
tags:
- people-search
- reverse-lookup
- aggregator
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# ThatsThem

> A free US people-search aggregator with genuine multi-selector reverse lookup: name, address, phone, email, or even IP in, contact details out.

## When to use
You have any one of `name`, `address`, `phone`, `email`, or `ip-address` for a US subject and want to pivot to the others. ThatsThem is a useful first-pass free aggregator because it accepts an unusually wide range of inputs — including reverse-email and reverse-IP — and returns linked addresses, phones, emails, and household/associate names without an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://thatsthem.com and pick the search type matching your input (name+address, phone, email, or IP).
2. Enter the selector and submit — no login required.
3. Read the record: current and prior `address`es, associated `phone`s and `email`s, approximate home value, and other names at the address (`associate`/household links).
4. Corroborate: because it's an aggregator, treat every field as a lead. Confirm the live phone/address against a second source.
5. Pivot: household names feed relative/associate mapping; a confirmed phone/email feeds carrier and account-existence checks.

## Inputs → Outputs
- **In:** `name`, `address`, `phone`, `email`, or `ip-address`
- **Out:** `name`, `address` (current + historical), `phone`, `email`, `associate` (household/linked people)
- **Empty/negative result looks like:** "no results found" or a thin record with only a name and a stale address — common for younger people, renters, and those who've opted out. A miss here doesn't rule the person out; try another aggregator.

## Gotchas & OpSec
- Data quality is uneven and can be years out of date; ThatsThem itself flags results as non-authoritative.
- Subjects can opt out, so absence isn't meaningful.
- Reverse-IP results are coarse (ISP/geo-level), not a precise identity.
- OpSec: passive; no account, no subject notification — a clean browser suffices.

## Overlaps ("do both")
- Pairs with [[fastpeoplesearch]], [[truepeoplesearch]], and [[whitepages-com]] — free aggregators draw from overlapping-but-different sources, so cross-running them fills gaps and lets you cross-validate a phone/address before trusting it.

## Trust & verifiability
`trust: unverified` — a commercial aggregator of public-record and marketing data with no guarantee of accuracy; use it to generate leads, then confirm each fact against an authoritative or second independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thatsthem-2 |
| category | people-search |
| selectorsIn → selectorsOut | name, address, phone, email, ip-address → name, address, phone, email, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
