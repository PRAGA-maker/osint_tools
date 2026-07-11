---
id: phonebooks-com
name: Phonebooks.com
description: Use when you have a US `phone` (or `name`) and want a reverse-lookup to an owner and address — returns `name`, `address`, `associate`.
url: https://www.phonebooks.com/
category: phone
path:
- phone
bestFor: US reverse phone lookup and white-pages people search — number to name/address, or name to number.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- associate
status: live
pricing: freemium
costNote: Free basic reverse/white-pages results; deeper reports and some records route to paid background-check partners.
opsec: passive
opsecNote: Aggregates public directory/records data; the subject isn't notified and no login is needed for basic lookups. Don't hand real case details to the paid partner upsells.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party directory/reverse-lookup aggregator; data quality is variable and can be stale, and it monetizes via paid-report referrals.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Phone Books
tags:
- mobilephone
- Mobile & Phone Related
- reverse-phone
- white-pages
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Phonebooks.com

> A US white-pages and reverse-phone lookup: put in a number to get the likely owner and address, or a name to get numbers — a free first pass before paid phone tools.

## When to use
You have a US `phone` and want to know whose it is and where they are, or you have a `name` and want listed numbers/addresses. Reverse-lookup is a fast, free way to attach an identity and location to a landline or listed number early in a case — most effective for landlines and older listed numbers, weaker on mobiles and VoIP.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.phonebooks.com/ and choose reverse-phone (enter the number) or people search (enter the name + state).
2. Read the free result: listed name, address, and sometimes relatives/associates.
3. Treat "unlock full report" prompts as paid third-party referrals — skip unless you intend to pay.
4. Cross-check the returned name/address against a second source before relying on it.
5. Pivot: run the `name`/`address` through people-search, and confirm the number's line type with an authoritative tool ([[twilio]]).

## Inputs → Outputs
- **In:** `phone` (US) or `name`
- **Out:** `name`, `address`, `associate` (relatives), listed numbers
- **Empty/negative result looks like:** no listing — common for mobiles, unlisted, VoIP, or numbers registered to another party; a blank doesn't mean the number is fake.

## Gotchas & OpSec
- US-only and strongest on **landlines/listed** numbers; mobiles and VoIP often return nothing.
- Data can be stale (old address on record) — verify before acting.
- Free results funnel toward paid background-check partners; don't feed them sensitive details.

## Overlaps ("do both")
- Pairs with [[twilio]] (carrier/line-type/CNAM) and free people-search ([[xlek]]) — this gives a subscriber name/address, Twilio confirms line type, and people-search corroborates the identity.

## Trust & verifiability
`trust: unverified` — a third-party aggregator with variable, sometimes stale data and paid-referral incentives; treat any hit as a lead to confirm, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phonebooks-com |
| category | phone |
| selectorsIn → selectorsOut | phone, name → name, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
