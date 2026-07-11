---
id: nigeriaphonebook
name: NigeriaPhonebook
description: Use when you have a Nigerian `phone` or `name` and want caller/owner identification or a business listing — returns name, phone, and address/business details.
url: https://nigeriaphonebook.com/
category: people-search
path:
- people-search
bestFor: Identifying Nigerian phone numbers (MTN/Airtel/Glo/9mobile) and businesses, with scam-report context.
selectorsIn:
- name
- phone
selectorsOut:
- name
- phone
- address
status: live
pricing: freemium
costNote: Browsing the business directory is free, but personal phone-number lookups are gated — last names are partially censored on free accounts and full lookups start around a $1 trial with paid plans beyond.
opsec: passive
opsecNote: Querying a number does not alert its owner. It aggregates public/crowd data of varying reliability; corroborate before acting. Use a clean browser and a payment method you're comfortable exposing if you buy lookups.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd/aggregated Nigerian directory with scam-report features; useful for leads but data provenance and freshness are unverified.
missingPersonsRelevance: high
coverage:
- ng
auth: none
api: false
localInstall: false
registration: false
aliases:
- Nigeria Phonebook
- nigeriaphonebook.com
tags:
- bellingcat-toolkit
- people
- nigeria
- reverse-phone
source: bellingcat-toolkit
lastVerified: '2026-07-11'
enrichment: full
---

# NigeriaPhonebook

> A Nigerian phone/business directory: look up a number or name to identify the caller/owner or a business, with community scam reports.

## When to use
You have a Nigerian `phone` number or a `name`/business and want to identify or characterise it — who a number is listed to, which network it's on, whether it's been reported for scams, or a business's contact details. A useful regional tool where global reverse-phone services have thin Nigerian coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open nigeriaphonebook.com.
2. Search by `phone` (caller ID/verification) or browse by `name`/business, state, or alphabetically.
3. Read the result: listed name (last name partially masked on free tier), network, business/location details, and any community scam reports.
4. To reveal full details, take the paid lookup (starts around a $1 trial).
5. Pivot: a name feeds broader people-search; a business address is a `geolocation`/`address` lead; scam reports flag risk context.

## Inputs → Outputs
- **In:** `phone` (Nigerian) or `name`/business + state
- **Out:** listed `name` (masked on free), `phone`/network, business `address`/location, scam-report history
- **Empty/negative result looks like:** no listing or comments-only — the number isn't in their data or is a fresh SIM. Absence isn't proof; Nigerian mobile records are incomplete.

## Gotchas & OpSec
- Human-in-the-loop: personal lookups are paywalled (payment-wall-partial) and free results censor last names.
- Data quality: aggregated/crowd data — treat as a lead, verify before relying on a name/owner.
- OpSec: passive to the subject; be mindful of exposing a payment method if you buy lookups.

## Overlaps ("do both")
- Pairs with global reverse-phone tools and messaging-app checks (WhatsApp/Telegram by number, very common in Nigeria) — this adds local directory/scam context; the app checks confirm the line is active and reveal a profile photo/name.

## Trust & verifiability
`trust: community` — a regional directory of unverified provenance, listed in the Bellingcat toolkit for Nigeria. Good for regional leads; never treat a single masked/aggregated result as confirmed identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nigeriaphonebook |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → name, phone, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
