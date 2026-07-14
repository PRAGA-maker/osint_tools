---
id: reverse-phone-lookup-find-name-address-and-amp-more-for-any-phone-number-addresses-com
name: Addresses.com Reverse Phone Lookup
description: Use when you have a US `phone` number and want the likely owner's name and address — returns `name`, `address`, and `associate` links (full detail behind a paywall).
url: http://www.addresses.com/phone
category: phone
path:
- phone
bestFor: US reverse-phone lookup to attach a name/address to a number (teaser free, full report paid via Intelius).
selectorsIn:
- phone
selectorsOut:
- name
- address
- associate
status: live
pricing: freemium
costNote: Powered by Intelius. A free search returns teaser results (city/state, partial name); the full owner name, address, and associated people are gated behind a paid Intelius report/subscription.
opsec: active
opsecNote: Queries go to a US data broker (Intelius), which logs your searches and IP; the number's owner is not notified. Data brokers also profile searchers — use a sock-puppet identity/IP for sensitive work. Not a consumer-reporting agency; results are not FCRA-permissible for employment/tenant screening.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Addresses.com is an Intelius-powered people-search aggregator; data is compiled from public records and broker sources, so accuracy is decent but not authoritative and can be stale.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases:
- addresses.com phone
- Intelius reverse phone
tags:
- phone
- people-search
- data-broker
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Addresses.com Reverse Phone Lookup

> An Intelius-powered reverse-phone lookup: type a US number, get a teaser of the likely owner — then decide whether the full name/address report is worth the paywall.

## When to use
You have a US `phone` number and want to attach an identity — owner `name`, current/past `address`, and associated people (`associate`). Useful in a locate workflow to turn a bare number (from a call log, ad, or profile) into a named person and a place to look next. The free teaser often confirms the general region and a partial name for free; the paid report fills in specifics.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.addresses.com/phone in a sock-puppet browser.
2. Enter the US `phone` number and search.
3. Read the free teaser: typically line type, city/state, and a partial owner name — sometimes enough to confirm a lead cheaply.
4. If you need specifics, the full Intelius report (name, address history, relatives) requires payment/registration — decide if it's justified.
5. Pivot: an owner name/address feeds people-search, property, and social lookups; associates feed network mapping.

## Inputs → Outputs
- **In:** US `phone` number
- **Out:** owner `name`, `address` (current/historical), `associate`s — teaser free, full detail paid
- **Empty/negative result looks like:** "no results" or a teaser with no name — common for mobiles, VoIP, ported, or unlisted numbers. A broker miss is not proof the number is unassigned; try another broker.

## Gotchas & OpSec
- **Payment wall:** the useful detail (full name/address/relatives) is paid. Free tier is a teaser.
- Broker data is compiled and can be **stale or wrong** (old addresses, prior owner after porting) — treat as a lead to verify, never as proof.
- **Not FCRA-compliant** — do not use for employment, tenancy, or credit decisions.
- OpSec: active toward a data broker (logged); the target isn't notified. Use a sock puppet.

## Overlaps ("do both")
- Pairs with other US reverse-phone/people-search brokers (Spokeo, ThatsThem, TruePeopleSearch) and with carrier/validity tools like `[[firefly]]` — brokers vary in coverage, so run several; validity tools confirm the number is real and its carrier before you pay for an identity report.

## Trust & verifiability
`trust: community` — an aggregator over public-record and broker data; reasonably useful but not authoritative and sometimes outdated. Corroborate any name/address against a second broker or a primary record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-phone-lookup-find-name-address-and-amp-more-for-any-phone-number-addresses-com |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial) |
