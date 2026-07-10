---
id: radaris-people-and-business-search-north-america
name: Radaris People & Business Search (North America)
description: Use when you have a `name`, `phone` or `address` and want a US person's contacts and associates — returns addresses, phone numbers, relatives, social profiles and business/property records.
url: http://radaris.com
category: people-search
path:
- people-search
bestFor: Free first-pass US people search that ties a name to addresses, phones, relatives and public records.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free to search and view a summary (name, approximate location, relatives, phone owner/carrier/spam flag); full background reports with complete contact history are sold as paid reports.
opsec: passive
opsecNote: Radaris is a data broker — you query its aggregated public-record index, not the subject, so no notification reaches them. Your search and IP are visible to Radaris and may be logged; use a sock-puppet browser. Note Radaris also lets people opt out, so a missing record may mean suppression, not absence.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial US people-search broker with broad coverage but well-documented accuracy problems (outdated addresses, wrong relative links); good for leads, weak as proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Radaris
- radaris.com
tags:
- toddington
- curated-directory
- people-search
- data-broker
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Radaris People & Business Search (North America)

> A free US people-and-business aggregator: turn a name, phone or address into a bundle of contacts, relatives and public records.

## When to use
You have a `name` (ideally with a city/state), a `phone`, or an `address` for someone in the US and want a fast, free sketch of their footprint — where they've lived, phone numbers, likely relatives and associates, and any business/property records. A strong early-stage people-search to generate leads and an associate graph before committing to a paid report elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://radaris.com in a sock-puppet browser (also reachable via its reverse-phone and reverse-address entry points).
2. Enter the selector you have: full `name` (add state to disambiguate), `phone`, or `address`.
3. Solve any CAPTCHA and read the free summary card: current/prior `address`es, `phone`s (with carrier/spam flags on the phone tool), listed relatives/`associate`s, `social-profile` links, and business/property mentions.
4. Corroborate before trusting — pick the profile whose age/location/relatives fit, and cross-check each fact against a second source.
5. Pivot: relatives feed the associate graph and further searches; an address feeds property/voter records; a phone feeds `[[whitepages-reverse-phone]]`; a business name feeds company registries.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `address` history, `phone`s, `associate`/relatives, `social-profile` links, `employer-org`/property records
- **Empty/negative result looks like:** no matching profile, or a bare card with only a name/city — common for young, private, or opted-out subjects. Because Radaris honors opt-outs, absence can mean suppression rather than "no such person."

## Gotchas & OpSec
- Human-in-the-loop: expect a CAPTCHA; aggressive scraping is blocked, so work it by hand.
- Accuracy is uneven — addresses and especially "relatives" are algorithmically inferred and frequently wrong; never treat a Radaris link as confirmed.
- OpSec: **passive** to the subject; but consider that Radaris itself is a broker your search feeds. Use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[familytreenow]]`, `[[whitepages-reverse-phone]]` and other US brokers — each scrapes overlapping-but-different record sets, so run several and reconcile. What Radaris gets wrong on relatives, FamilyTreeNow may get right, and vice versa.

## Trust & verifiability
`trust: community` — a commercial broker aggregating public records; broad but error-prone. Use it to generate leads and associate hypotheses, then verify every fact against authoritative records (courts, property, voter, official registries).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radaris-people-and-business-search-north-america |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
