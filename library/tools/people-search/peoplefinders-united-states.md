---
id: peoplefinders-united-states
name: PeopleFinders (United States)
description: Use when you have a `name`, `phone` or `address` and want US contact and public-record data — returns addresses, phones, relatives and background details (report behind a low paywall).
url: https://www.peoplefinders.com/
category: people-search
path:
- people-search
bestFor: US people search that expands a name/phone/address into contacts, relatives and public-record background.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- social-profile
status: live
pricing: freemium
costNote: Free 4-step preview confirms whether a matching person exists; contact details and full reports are paid (from ~$1.95 per report, or ~$9.95–$29.95/mo plans).
opsec: passive
opsecNote: A commercial data-broker lookup — you query PeopleFinders, not the subject, and no notification reaches them. Buying a report ties the search to your payment identity; prefer the free preview for triage. Use a sock-puppet browser; PeopleFinders offers a record opt-out, so a missing person may be suppressed.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running US people-search broker aggregating public records; broad coverage but the usual data-broker caveats — outdated addresses and inferred relatives are common.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- PeopleFinders
- peoplefinders.com
tags:
- toddington
- curated-directory
- people-search
- data-broker
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# PeopleFinders (United States)

> A US people-search broker: the free preview confirms you've found the right person; the paid report unlocks their contacts, relatives and background.

## When to use
You have a `name` (ideally with a city/state), a `phone`, or an `address` for a US subject and want to expand it into current contacts, address history, relatives, and public-record background. Use the free preview to confirm a match cheaply, then decide whether the paid report is worth it — a solid all-rounder when free brokers come up short.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peoplefinders.com/ in a sock-puppet browser.
2. Search by `name`, `phone`, or `address`.
3. Use the **free 4-step preview** to confirm a candidate exists (name, rough location, associated names) before paying.
4. If on-target, buy the report for full `address` history, `phone`s, relatives/`associate`s, `social-profile` links, and background (criminal/property where offered).
5. Pivot: relatives feed the associate graph; an address feeds property/voter records; a phone feeds `[[whitepages-reverse-phone]]`.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `address` history, `phone`s, relatives/`associate`s, `social-profile` links, background records (paid)
- **Empty/negative result looks like:** the preview finds no matching person — young, private, or opted-out subjects, or wrong spelling/location. PeopleFinders honors opt-outs, so absence can mean suppression.

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall gates the real data; watch for subscription auto-renewal on the monthly plans.
- Data-broker accuracy: addresses can be stale and "relatives" are inferred — corroborate before asserting.
- OpSec: **passive** to the subject; buying ties the search to your card — use the free preview for triage and a sock puppet throughout.

## Overlaps ("do both")
- Pairs with `[[thats-them]]` (free), `[[radaris-people-and-business-search-north-america]]`, and `[[skip-ease]]` — brokers hold overlapping-but-different records; run several and reconcile. Use free tools first, then pay PeopleFinders only to fill gaps.

## Trust & verifiability
`trust: unverified` — a commercial aggregator with no per-record provenance; treat results as leads and verify against authoritative records (courts, property, voter) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peoplefinders-united-states |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
