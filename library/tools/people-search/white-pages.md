---
id: white-pages
name: Whitepages
description: Use when you have a US `name`, `phone` or `address` and want current address, phone and relatives — returns address, phone, associate and approximate dob/age.
url: https://www.whitepages.com/
category: people-search
path:
- people-search
bestFor: US people/phone/address lookup — resolving a name to a current address, landline/mobile, age range and relatives.
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
costNote: Free searches show partial results (city/state, age range, some relatives, partial numbers). Full contact details, reverse-phone owner data and background reports require a paid Whitepages Premium subscription (payment wall).
opsec: passive
opsecNote: Querying Whitepages does not contact the subject, so it is passive. Note that free results are deliberately teasered to push you to pay; use a research payment method if you subscribe, and remember Whitepages also lets people opt out, so records may be missing by choice.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Large, long-established US data aggregator; data is compiled from public and commercial sources, so it is broad but can be stale or conflate people with similar names.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- WhitePages
- whitepages.com
tags:
- people-search
- phone-lookup
- reverse-phone
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Whitepages

> A staple US people-search aggregator — turn a name, phone or address into a current address, phone numbers, age range and a list of likely relatives.

## When to use
You have a US `name`, `phone`, or `address` and want to resolve it to current contact and household data: where someone lives now, their landline/mobile, an age range to confirm identity, and relatives/associates (`associate`) who become new leads. It is one of the first stops for US missing-person or identity work because of its breadth and its strong reverse-phone lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to whitepages.com and pick the search type: People (name), Reverse Phone, or Address.
2. Enter the selector; add a city/state to disambiguate common names.
3. Read the free preview: name, approximate age (`dob` band), current city, some relatives, and partial numbers.
4. For full address, complete phone numbers, and background details, a paid Premium lookup is required.
5. Pivot: relatives (`associate`) become new `name` searches; a confirmed phone feeds messaging-app and breach lookups; an address feeds property and neighbor records.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `address` (current/prior), `phone` (landline/mobile), `associate` (relatives/household), `dob` (age range)
- **Empty/negative result looks like:** "no results", a common-name list you can't disambiguate, or an opted-out record — Whitepages honours opt-outs and can lag, so absence is not proof.

## Gotchas & OpSec
- **Freemium tease:** the most useful fields sit behind Premium; budget for a subscription or use free results only to narrow, then confirm elsewhere.
- US only; data can be stale and can merge same-name individuals — cross-check age and relatives.
- Subjects can opt out, creating deliberate gaps.

## Overlaps ("do both")
- Pairs with `[[thats-them]]`, TruePeopleSearch and FastPeopleSearch — run several free aggregators, since each licenses different data and one often has the current address another misses.

## Trust & verifiability
`trust: community` — a broad, established aggregator, but compiled data can be outdated or conflated; verify any address/phone against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | white-pages |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
