---
id: addresses-com
name: Addresses.com
description: Use when you have a US `name`, `phone`, or `address` and want a quick person/address lookup — returns `name`, age (`dob`), partial `phone`, and associated `address`es/`associate`s.
url: https://www.addresses.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: Quick US people and address lookups, with an Intelius-backed report upsell.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- dob
- phone
- address
- associate
status: live
pricing: freemium
costNote: Free basic teaser results (name, approximate age, partial address/phone); full reports (complete numbers, address history, relatives) require an Intelius paid subscription.
opsec: passive
opsecNote: Data-broker aggregator — searching is passive and the subject is not notified. Note the flip side: purchasing an Intelius report ties the transaction to your payment identity, and these brokers may retain your search history; use appropriate separation for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial data broker (Intelius/PeopleConnect family); aggregated data is often stale or conflated across same-name individuals — treat as leads, not facts.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Addresses.com
tags:
- people-search
- data-broker
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Addresses.com

> A US people-and-address search front end backed by Intelius — quick teaser lookups by name, phone, or address, with a paid report behind the details.

## When to use
You have a US subject and a `name`, `phone`, or `address`, and want a fast first read on their approximate age, likely current/associated addresses, and possible relatives — the kind of quick triage that tells you whether to invest in a full report or another tool. Best as one of several broker lookups you cross-check, not a single source of truth.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.addresses.com/ and pick the search type (people / reverse phone / reverse address).
2. Enter the `name` (with a state to disambiguate), `phone`, or `address`.
3. Read the free teaser: name, approximate age, city/state, partial address and phone, and possible relatives.
4. Decide whether the paid Intelius report is worth it, or carry the leads (relatives, prior cities) to free/authoritative sources.
5. Pivot: candidate relatives (`associate`) and prior `address`es feed voter/property records and other people-search.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address` (US)
- **Out:** `name`, age (`dob`), partial `phone`, associated `address`es, likely `associate`s (relatives)
- **Empty/negative result looks like:** no match or a same-name jumble — broker data frequently conflates distinct people with the same name and lags real moves by months to years. Treat every teaser field as an unverified lead.

## Gotchas & OpSec
- Freemium wall: the useful detail (full numbers, address history, confirmed relatives) sits behind an Intelius subscription.
- Data staleness and same-name conflation are the main failure modes; always disambiguate by age + location and corroborate elsewhere.
- US-only.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]`, `[[fastpeoplesearch]]`, and `[[thatsthem]]` — run the same query across several free brokers because each buys different data slices; agreement across sources raises confidence.

## Trust & verifiability
`trust: unverified` — commercial data broker; output is aggregated and error-prone, so use it to generate leads and confirm them against authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | addresses-com |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → name, dob, phone, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
