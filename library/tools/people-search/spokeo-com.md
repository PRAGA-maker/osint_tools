---
id: spokeo-com
name: spokeo.com
description: Use when you have a `name`, `phone`, `email`, or `address` and want an aggregated US people profile — returns address history, phone/email, relatives/associates, and linked social profiles (full report is paid).
url: https://www.spokeo.com/
category: people-search
path:
- people-search
bestFor: Aggregating US contact, address history, and relatives/associates from a name, phone, email, or address.
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
status: live
pricing: freemium
costNote: Free search shows a teaser (existence + partial data); the full report requires a paid one-time purchase or subscription. Criminal-records add-on costs extra. Effectively pay-to-view for anything substantive.
opsec: active
opsecNote: Semi-active — you must create an account and pay, tying lookups to your billing identity. The subject is not contacted, but Spokeo (a data broker) logs who searched whom. Use a dedicated investigative account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A major consumer data broker; coverage is broad but records are aggregated and frequently stale or conflated across same-named people. Explicitly not an FCRA consumer-reporting agency.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Spokeo
- spokeo.com
tags:
- peoplesearch
- People Search Sites
- data-broker
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# spokeo.com

> A large US consumer data broker that aggregates public and commercial records into a single people profile — searchable by name, phone, email, or address, with the substantive report behind a paywall.

## When to use
You have any one strong US selector — `name`, `phone`, `email`, or `address` — and want a consolidated profile: current/prior addresses, associated phones/emails, relatives and `associate`s, and linked social accounts. In missing-person work Spokeo is useful for building an address history and a relative/associate network to contact, and for reverse-resolving a phone/email to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.spokeo.com/ and choose the search type (name / phone / email / address).
2. Enter the selector; the free results page shows a teaser (a match exists, partial location/age).
3. To see the full report (addresses, relatives, contact details) you must sign in and pay (subscription or one-time).
4. Read the report, but scrutinise it — Spokeo often merges records from different same-named people.
5. Pivot: relatives/associates become new subjects; an address-history entry feeds property/records tools like `[[texas-public-records-search]]`; a reverse phone/email confirms identity.

## Inputs → Outputs
- **In:** `name`, `phone`, `email`, or `address`
- **Out:** address history, `phone`/`email`, relatives/`associate`s, linked `social-profile`s (criminal add-on paid)
- **Empty/negative result looks like:** a teaser with no real matches, or a report that clearly conflates several people (mismatched ages/locations) — treat conflated data as unreliable, not as one person's record.

## Gotchas & OpSec
- Pay-to-view: the free layer is a teaser; budget for a subscription and remember to cancel (auto-renew is common).
- Data is aggregated and often stale or merged across same-named individuals — verify every field against a primary source.
- US-focused; weak outside the US.
- Not FCRA — must not be used for employment/tenant/credit decisions. Your searches are logged to your account.

## Overlaps ("do both")
- Pairs with `[[searchpeoplefree]]` and `[[canada411-advanced-search-whitepages-ca]]` — cross-check broker data across providers, since each conflates differently.
- Address/relative leads feed public-records directories (`[[texas-public-records-search]]`) and obituary/registry sources for confirmation.

## Trust & verifiability
`trust: unverified` — a commercial data broker with broad but imperfect aggregation. Any single field can be outdated or belong to a different same-named person; treat Spokeo as a lead generator and confirm everything against authoritative sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spokeo-com |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, email, associate, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
