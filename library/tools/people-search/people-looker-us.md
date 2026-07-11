---
id: people-looker-us
name: PeopleLooker (US)
description: Use when you have a US `name`, `phone`, `email` or `address` and want a consumer background-report aggregator to pull contact history, relatives and records — returns address, phone, email, associate, social-profile and dob.
url: https://www.peoplelooker.com
category: people-search
path:
- people-search
bestFor: Consolidated US background reports (contact history, relatives, court/criminal records) from a name, phone, email or address.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- dob
status: live
pricing: freemium
costNote: Not genuinely free. A search runs and shows a teaser (city, age, possible relatives) at no cost, but reading any full report requires a paid subscription (typically a low-cost multi-day trial that auto-renews into a monthly plan). Budget for the subscription and cancel deliberately.
opsec: active
opsecNote: You must create an account and pay, so the query is tied to your billing identity — never use a real personal card/identity for target research. PeopleLooker also warns subjects can opt out, and it may retain your search history. The subject is not notified of an individual lookup, but the transaction ties the search to you; use a dedicated research account and payment method.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial data broker (BeenVerified family of brands). Data is aggregated from public records and commercial sources — useful but not authoritative; expect stale and mismatched entries.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- PeopleLooker
- peoplelooker.com
tags:
- people-search
- background-check
- data-broker
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# PeopleLooker (US)

> A consumer background-report broker: give it a US identifier and it assembles a report of addresses, phones, emails, relatives and public records — behind a paywall.

## When to use
You have a US `name` (ideally with a city/state), or a `phone`/`email`/`address`, and want a single consolidated report rather than stitching public records by hand. Best when you already have a likely identity and want to expand it into contact history, relatives (`associate`) and possible records to corroborate or locate the person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peoplelooker.com and choose the lookup type (people / reverse phone / email / address / username).
2. Enter the identifier and run the search — the free teaser shows city, approximate age and possible relatives, which alone can confirm you have the right person.
3. To read the full report you must register and start a paid plan (usually a cheap trial). Use a **dedicated research account and payment method**, not your own.
4. Read the report: current/past `address`, `phone`, `email`, `associate` (relatives/roommates), `social-profile`, `dob`/age, and court/criminal record flags.
5. Pivot: relatives and prior addresses feed a location timeline; a phone/email feeds reverse lookups and breach checks; corroborate every field against an authoritative source before relying on it.

## Inputs → Outputs
- **In:** `name`, `phone`, `email`, or `address`
- **Out:** `address` (current + historical), `phone`, `email`, `associate`, `social-profile`, `dob`/age, record indicators
- **Empty/negative result looks like:** the teaser shows "no records" or only ambiguous partial matches — common for young people, recent movers, or those who have opted out. A no-hit is not proof of absence.

## Gotchas & OpSec
- **Paywall:** the free step is only a teaser; full data requires a subscription that auto-renews — set a cancellation reminder.
- Broker data is aggregated and error-prone: wrong relatives, merged identities and outdated addresses are common. Treat every field as a lead to verify, not a fact.
- OpSec: **active** — the search is tied to your billing/account identity. Isolate it behind a research persona and payment method; do not run target searches on a personal account.

## Overlaps ("do both")
- Pairs with rival broker aggregators (BeenVerified, TruthFinder, Spokeo) — brokers draw from overlapping but not identical sources, so cross-run and treat agreement as confidence.
- Pairs with authoritative public records (county, state DOC, voter/court) to confirm the broker's claims.

## Trust & verifiability
`trust: community` — a commercial aggregator, not an authority. Its convenience is bundling many sources; its weakness is that none of them are verified at the point of display, so independently confirm anything you act on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-looker-us |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, email, associate, social-profile, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial, account-login) |
