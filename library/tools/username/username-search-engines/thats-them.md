---
id: thats-them
name: Thats Them
description: Use when you have a `name`, `email`, `phone` or `address` and want free US contact and demographic data — returns addresses, phones, emails, IP, and household/demographic details.
url: https://thatsthem.com/
category: username
path:
- username
- username-search-engines
bestFor: Free US people search that cross-links name, email, phone and address into a contact and demographics profile.
selectorsIn:
- name
- email
- phone
- address
selectorsOut:
- address
- phone
- email
- associate
- ip-address
status: live
pricing: free
costNote: Free for searches (no paywall on core results); aggregates data from 50+ sources updated monthly. Not FCRA-permissible (no employment/tenant/credit use).
opsec: passive
opsecNote: Searches route through ThatsThem's servers and the subject is not notified. You hand the selector to a data broker; use a sock-puppet browser. Note ThatsThem offers a record opt-out, so a missing person may be suppressed rather than absent.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial US data broker aggregating 50+ sources; broad and genuinely free, but accuracy varies and its financial/demographic estimates (net worth, income) are modelled, not factual.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- ThatsThem
- thatsthem.com
tags:
- people-search
- data-broker
- reverse-email
- reverse-phone
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Thats Them

> A genuinely free US people-search broker: pivot between name, email, phone and address, and pull a contact + demographics profile with no paywall.

## When to use
You have any one of a `name`, `email`, `phone`, or `address` for a US subject and want to expand it into the others plus household and demographic context. Its multi-directional lookups (including free reverse-email and reverse-IP) make it a versatile hub in a people-search workflow, and being free-to-view sets it apart from paywalled brokers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://thatsthem.com/ in a sock-puppet browser.
2. Pick the search type matching your selector (name, email, phone, or address) and enter it.
3. Read the record: current/prior `address`es (with coordinates), `phone`s, `email`s, household members/`associate`s, age, and sometimes an associated `ip-address`; demographic and financial estimates are modelled.
4. Corroborate: pick the record whose age/location/associates fit, and verify facts against a second source.
5. Pivot: an email → email-OSINT and breach checks; a phone → `[[whitepages-reverse-phone]]`; associates → the relationship graph; an address → property/voter records.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, or `address`
- **Out:** `address` history, `phone`s, `email`s, household `associate`s, sometimes `ip-address`; demographic/financial estimates
- **Empty/negative result looks like:** "no results" or a bare record — young, private, or opted-out subjects. Because ThatsThem honors opt-outs, absence can mean suppression, not non-existence.

## Gotchas & OpSec
- **Estimates ≠ facts:** net worth, income, religion, ethnicity are modelled inferences and often wrong — never assert them.
- US-focused; coverage thins outside the US.
- OpSec: **passive**; the subject isn't alerted. Use a sock puppet since you feed a broker.

## Overlaps ("do both")
- Pairs with `[[radaris-people-and-business-search-north-america]]`, `[[skip-ease]]` and `[[whitepages-reverse-phone]]` — each broker holds different records, so cross-check. ThatsThem's free reverse-email/IP is a distinctive add to the others' phone/address strengths.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with no per-record provenance; contact fields are usable leads, modelled demographics are not. Verify against authoritative records before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thats-them |
| category | username |
| selectorsIn → selectorsOut | name, email, phone, address → address, phone, email, associate, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
