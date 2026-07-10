---
id: melissa-us
name: Melissa (US)
description: Use when you have a US `address` (or name/phone) and want to verify/normalise it and find associated residents — returns standardised `address`, resident `name`s, `phone` and likely relatives via Melissa's free lookups.
url: http://melissadata.com
category: people-search
path:
- people-search
bestFor: Verifying/standardising a US address and finding current residents, plus reverse address/phone lookups.
selectorsIn:
- address
- name
- phone
selectorsOut:
- name
- phone
- associate
- address
status: live
pricing: freemium
costNote: Melissa offers free web "Lookups" (limited demo lookups per day) for address/name/phone/property; bulk and API access are paid.
opsec: passive
opsecNote: Read-only lookups against Melissa's reference databases; the subject is not notified. Free lookups are rate-limited demos — don't script them. Melissa is a data vendor and logs queries; use a clean session.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Melissa is a long-established commercial data-quality vendor; its address/USPS data is authoritative, but the free consumer "Lookups" are limited demos of its paid datasets.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thats-them
- peoplebyname-us
aliases:
- MelissaData
- Melissa Lookups
- Melissa Personator
tags:
- address
- people-search
- address-verification
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Melissa (US)

> A commercial data-quality vendor whose free web "Lookups" double as OSINT utilities — verify a US address and find who lives (or lived) there.

## When to use
You have a US `address` and want to (a) confirm it is a real, deliverable USPS address and standardise it, and (b) find the current/prior residents, a household `phone`, and likely relatives (`associate`). Melissa also runs reverse phone and name lookups. Its address data is authoritative (USPS-grade), so it's a strong tool for pinning down where a subject lives and who is connected to that address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Melissa's free "Lookups" (via melissadata.com → Lookups; tools include Personator, Reverse Address, Reverse Phone, Property).
2. Enter the `address` (or `name`/`phone`) into the relevant lookup and run it.
3. Read the output: standardised/verified `address`, resident `name`(s), household `phone`, property details, and associated people.
4. Mind the daily free-lookup cap — space out queries rather than batching.
5. Pivot: a resident `name` feeds `[[thats-them]]` / `[[peoplebyname-us]]`; a verified address feeds property and mapping tools.

## Inputs → Outputs
- **In:** US `address` (or `name` / `phone`)
- **Out:** standardised `address`, resident `name`(s), `phone`, `associate` (household/relatives), property data
- **Empty/negative result looks like:** address flagged invalid/undeliverable, or no residents returned — meaning the address is bad or Melissa's consumer data has no match. Absence in the free demo is not authoritative.

## Gotchas & OpSec
- The free web lookups are **rate-limited demos** of Melissa's paid datasets — coverage/detail is capped; don't mistake a demo miss for "no data exists."
- US-focused for people/residents (Melissa does global address verification, but resident data is US).
- OpSec: **passive** — a data-vendor read; the subject isn't alerted.

## Overlaps ("do both")
- Pairs with `[[thats-them]]` and `[[peoplebyname-us]]` — Melissa's USPS-grade address verification anchors the location, while those aggregators broaden the people/phone/relative picture around it.

## Trust & verifiability
`trust: community` — authoritative address data from an established vendor, but the free consumer lookups are limited demos; corroborate resident/relative claims before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | melissa-us |
| category | people-search |
| selectorsIn → selectorsOut | address, name, phone → name, phone, associate, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
