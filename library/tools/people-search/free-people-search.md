---
id: free-people-search
name: PeopleFinder
description: Use when you have a `name`, `phone` or `address` and want an aggregated US background profile — returns `address`, `phone`, `associate`, `social-profile` (full report paywalled).
url: https://www.peoplefinder.com/
category: people-search
path:
- people-search
bestFor: US people-search / background aggregation (Intelius data) — locate addresses, phones, relatives behind a paid report.
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
costNote: Search/preview is free, but the full report (addresses, phones, records) is paywalled — it's a paid Intelius-powered service, not a free directory despite the "free people search" framing.
opsec: passive
opsecNote: Aggregates public records; the subject isn't notified. Buying a report requires payment/registration, attaching your identity/billing to the lookup — use a dedicated investigative account and payment method.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Powered by Intelius, a long-established (if much-criticized) data broker; data is aggregated public records — often useful but not authoritative and sometimes stale.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- PeopleFinder.com
- Free People Search
tags:
- people-search
- background-check
- intelius
- public-records
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# PeopleFinder

> An Intelius-powered US people-search: enter a name/phone/address and it aggregates public records into a background profile — a preview is free, the full report is paid.

## When to use
You have a US subject's `name` (or a `phone`/`address` to search from) and want an aggregated profile: current/past addresses, phone numbers, relatives and associates, and linked social/records. Useful when free aggregators come up thin and you're willing to pay for a consolidated report — but note it's a paid broker, not the "free" its name implies, and it can't be used for FCRA-regulated purposes (employment/housing/credit).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peoplefinder.com/ and search by name (+ state), phone, or address.
2. Read the free preview: it typically confirms a match exists and teases available data (locations, relatives count).
3. To see the full detail, purchase/subscribe (payment + registration) — the report unlocks addresses, phones, relatives, records.
4. Corroborate report data against free sources; broker data is often stale.
5. Pivot: feed `associate` names back into search, `phone` into [[twilio]]/reverse-lookup, `address` into property records.

## Inputs → Outputs
- **In:** `name` (+ location), `phone`, or `address`
- **Out:** `address`, `phone`, `associate` (relatives), `social-profile`/records — full detail behind the paywall
- **Empty/negative result looks like:** no match in the preview — the subject may be non-US, opted out, or under a name variant; a match preview that unlocks to stale/wrong data is the other failure mode, so verify.

## Gotchas & OpSec
- **Not actually free** — the report is paywalled; the "free people search" branding is misleading.
- Broker data (Intelius) is aggregated and can be outdated — corroborate before relying.
- **FCRA:** cannot legally be used for employment, housing, credit or insurance decisions.
- US-only.

## Overlaps ("do both")
- Pairs with free aggregators ([[xlek]], FastPeopleSearch) and [[twilio]] — try the free tools first; use PeopleFinder's paid report only to fill gaps, then verify.

## Trust & verifiability
`trust: community` — a mainstream data broker; data is real aggregated public records but not authoritative and sometimes stale, so treat report fields as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
