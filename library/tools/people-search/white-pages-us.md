---
id: white-pages-us
name: Whitepages (US)
description: Use when you have a US `name`, `phone`, or `address` and want contact/identity details — returns current address, phone numbers, relatives/associates, and age.
url: https://www.whitepages.com
category: people-search
path:
- people-search
bestFor: US name/phone/address lookup returning current contact info, relatives, and age.
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
costNote: Free teaser (current city, age range, partial phone/relatives). Full contact details, background info, and reverse-phone owner data are paywalled behind Whitepages Premium.
opsec: passive
opsecNote: Searching is passive — the subject is not notified. You do disclose your query to a commercial broker; use a sock-puppet account/email and disposable payment if you subscribe.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-established US contact-data broker. Generally decent for current phone/address but aggregated from many sources, so entries can be stale or merged across same-name people.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- Whitepages
- whitepages.com
tags:
- people-investigations
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- white-pages
- whitepages-reverse-phone
---

# Whitepages (US)

> One of the oldest US contact-data brokers — turns a name, phone, or address into current contact details, relatives, and age, with a strong reverse-phone/reverse-address capability.

## When to use
You have a US subject's `name` (with a city/state), a `phone` to attribute, or an `address` to find who lives there, and you want current contact info plus relatives. A solid general-purpose US lookup for last-known address, active phone numbers, and family leads in a missing-person case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whitepages.com and pick the search mode: people (name), reverse phone, or reverse address.
2. Enter the input (`selectorsIn`); add a location to disambiguate common names.
3. Read the free teaser: current city, age range, partial relatives, partial phone. Confirm you have the right person.
4. For full phone/address/background, expect the Whitepages Premium paywall — subscribe only with a disposable account/payment, or pull the same fields from a cheaper source.
5. Pivot: relatives feed further people-search; a reverse-phone owner feeds identity confirmation; an address feeds property records.

## Inputs → Outputs
- **In:** `name` (+ location), `phone`, or `address`
- **Out:** current `address`, `phone`, relatives/`associate`s, age (`dob` band)
- **Empty/negative result looks like:** only same-name strangers or a locked teaser — a common name without a location anchor is inconclusive; not proof of absence.

## Gotchas & OpSec
- Paywall: the useful fields (full phone, background, reverse-phone owner) require Premium.
- Aggregation drift: data merges across people sharing a name; verify age/location against a second source.
- Not FCRA: not for employment/tenant screening.

## Overlaps ("do both")
- Pairs with `[[ussearch-us]]` and `[[my-life-people-search]]` — different brokers, different supplier data; run several and reconcile the address/phone/relatives.

## Trust & verifiability
`trust: unverified` — a commercial contact-data broker, reasonably reliable for current phone/address but not authoritative; corroborate before acting, especially on common names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | white-pages-us |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
