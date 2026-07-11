---
id: beenverified
name: BeenVerified
description: Use when you have a US `name`, `phone`, `email`, or `address` and want a consolidated background report — returns addresses, phones, relatives, and age/DOB (full report paywalled).
url: https://www.backgroundchecks.com/solutions/beenverified
category: people-search
path:
- people-search
bestFor: US people-search reports tying a person to address history, phones, emails, relatives, and possible records.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Search and a teaser preview are free, but viewing a full report requires a paid subscription (recurring). Direct site is beenverified.com. Budget for the paywall for complete data.
opsec: passive
opsecNote: BeenVerified is a data-broker aggregator; running a search does not notify the subject. It is FCRA-restricted — not for employment, tenant, or credit screening. Use a sock-puppet account and payment method if attribution matters; the broker logs your searches.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A mainstream US people-search broker; broad coverage but records blend current and dated data, so corroboration is essential.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- BeenVerified
- beenverified.com
tags:
- people-investigations
- data-broker
- background-report
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# BeenVerified

> A mainstream US background-report broker — one search turns a name/phone/email/address into a consolidated profile of addresses, contacts, and relatives.

## When to use
You have a US subject's `name` (best with a city/state), or a `phone`/`email`/`address` to reverse, and want a single report assembling their address history, phone numbers, email addresses, likely relatives/associates, and age/DOB — plus pointers to possible public records. Good for quickly scaffolding a US person and generating relatives and prior addresses to pursue.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to BeenVerified (`beenverified.com`); choose People / Phone / Email / Address search.
2. Enter the identifier (+ location for a name), and run it.
3. Read the **free teaser** (city/state, age range, partial relatives) to confirm you have the right person.
4. For the full report you must subscribe — weigh the paywall against a free alternative or another broker.
5. Pivot: prior addresses → property/records; relatives → associate mapping; a phone → `[[www-spydialer-com]]`; an email → `[[gravatar-email-checker]]`.

## Inputs → Outputs
- **In:** `name` (+location), `phone`, `email`, `address`
- **Out:** `address` (history), `phone`, `associate` (relatives), `dob`/age, record pointers
- **Empty/negative result looks like:** no match, or a teaser with no relatives/age — a thin record or wrong region. Common names need a location to disambiguate.

## Gotchas & OpSec
- Human-in-the-loop: the useful detail is **paywalled** (recurring subscription); the free teaser confirms identity but not full detail.
- Legal: FCRA-restricted — never use for employment/tenant/credit decisions.
- Data blends current and old records; verify "current" claims before relying on them.

## Overlaps ("do both")
- Pairs with `[[intelius-people-search-engine]]` and other brokers — coverage differs per broker, so a person thin on one may be rich on another; run more than one before concluding.

## Trust & verifiability
`trust: community` — a real, broad broker, but aggregated and time-mixed; treat every field as a lead to corroborate against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beenverified |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
